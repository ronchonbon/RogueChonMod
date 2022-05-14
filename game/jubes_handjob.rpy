## character.Handjob //////////////////////////////////////////////////////////////////////
label Jubes_Handjob:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Hand >= 7: # She loves it
        $ temp_modifier += 10
    elif character.Hand >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif character.Hand: #You've done it before
        $ temp_modifier += 3

    if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    if character.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (3*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no hand" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no hand" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if not character.Hand and "no hand" not in character.RecentActions:
        $ character.FaceChange("confused", 2)
        ch_v "Handjob, huh. . ."
        $ character.Blush = 1

    if not character.Hand and Approval:                                                 #First time dialog
        if character.Forced:
            $ character.FaceChange("sad",1)
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy",1)
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_v "You'd like that. . ."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal",1)
            ch_v "If you want, [character.Petname]. . ."
        else: # Uninhibited
            $ character.FaceChange("lipbite",1)
            ch_v "Hmm. . ."

    elif Approval:                                                                       #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_v "Nothing more than that?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_v "Well,this is a bit more secure. . ."
        elif "hand" in character.RecentActions:
            $ character.FaceChange("sexy", 1)
            ch_v "Hmm, another handy then. . ."
            jump Jubes_HJ_Prep
        elif "hand" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Another one?",
                "I'm glad I don't grow calluses.",
                "Didn't get enough earlier?",
                "Again the with handjobs, huh?",
                "I guess you want more."])
            ch_v "[Line]"
        elif character.Hand < 3:
            $ character.FaceChange("sexy", 1)
            $ character.Brows = "confused"
            $ character.Mouth = "kiss"
            ch_v "You seem to like this one. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice(["You want some more?",
                "So you'd like another handy?",
                "You want a. . . [fist pumping hand gestures]?",
                "Another handjob?"])
            ch_v "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_v "Ok, fine."
        elif "no hand" in character.DailyActions:
            ch_v "If it'll get you off my back. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "O-kay.",
                "Fine.",
                "I suppose I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Ok, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 60, 1)
        $ character.Statup("Inbt", 70, 2)
        jump Jubes_HJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no hand" in character.RecentActions:
            ch_v "I just told you no, [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions and "no hand" in character.DailyActions:
            ch_v "I said not in public."
        elif "no hand" in character.DailyActions:
            ch_v "I told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_v "I said not in public."
        elif not character.Hand:
            $ character.FaceChange("bemused")
            ch_v "Seriously, [character.Petname]. . ."
        else:
            $ character.FaceChange("bemused")
            ch_v "Nah."
        menu:
            extend ""
            "Sorry, never mind." if "no hand" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_v "It's fine."
                return
            "Maybe later?" if "no hand" not in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_v "Maybe."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no hand")
                $ character.DailyActions.append("no hand")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                        "O-kay.",
                        "Fine.",
                        "I suppose I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Ok, ok."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_HJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                call forced_action(character, "handjob")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no hand" in character.DailyActions:
        $ character.FaceChange("angry", 1)

        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_v "No."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.DailyActions.append("tabno")
        ch_v "This area's too exposed."
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
    elif character.Hand:
        $ character.FaceChange("sad")
        ch_v "I'm not into it today. . ."
    else:
        $ character.FaceChange("normal", 1)
        ch_v "I don't know where that's been lately."
    $ character.RecentActions.append("no hand")
    $ character.DailyActions.append("no hand")
    $ temp_modifier = 0
    return


label Jubes_HJ_Prep:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    if Trigger2 == "hand":
        return

    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)

    $ character.FaceChange("sexy")
    if character.Forced:
        $ character.FaceChange("sad")
    elif not character.Hand:
        $ character.Brows = "confused"
        $ character.Eyes = "sexy"
        $ character.Mouth = "smile"

    call Seen_First_Peen(character,Partner,React=Situation)
    call Jubes_HJ_Launch("L")

    if Situation == character:
            #Jubes auto-starts
            $ Situation = 0
            if Trigger2 == "jackin":
                "[character.Name] brushes your hand aside and starts stroking your cock."
            else:
                "[character.Name] gives you a mischevious smile, and starts to fondle your cock."
            menu:
                "What do you do?"
                "Nothing.":
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 30, 2)
                    "[character.Name] continues her actions."
                "Praise her.":
                    $ character.FaceChange("sexy", 1)
                    $ character.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] continues her actions."
                    $ character.Statup("Love", 80, 1)
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ character.FaceChange("surprised")
                    $ character.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] puts it down."
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 1)
                    $ character.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ character.AddWord(1,"refused","refused")
                    return

    if not character.Hand:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no hand")
    $ character.RecentActions.append("hand")
    $ character.DailyActions.append("hand")

label Jubes_HJ_Cycle:
    while Round > 0:
        call Shift_Focus(character)
        call Jubes_HJ_Launch
        $ character.LustFace()

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
                                            if character.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if character.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_HJ_After
                                                                        call Jubes_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(character,"tired")

                                                        "How about a titjob?":
                                                                    if character.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_HJ_After
                                                                        call Jubes_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(character,"tired")
                                                        "Never Mind":
                                                                jump Jubes_HJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Jubes_HJ_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_HJ_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Jubes_HJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And Jubes is unsatisfied,
                                "[character.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_HJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ character.Brows = "angry"
                    menu:
                        ch_v "Hmm, this is boring, can we take a break?"
                        "How about a BJ?" if character.Action and MultiAction:
                                $ Situation = "shift"
                                call Jubes_HJ_After
                                call Jubes_Blowjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                jump Jubes_HJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jubes_HJ_Reset
                                $ Situation = "shift"
                                jump Jubes_HJ_After
                        "No, get back down there.":
                                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                    $ character.Statup("Love", 200, -5)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ character.FaceChange("angry", 1)
                                    "She scowls at you, drops you cock and pulls back."
                                    ch_v "I have better things to do with my time."
                                    $ character.Statup("Love", 50, -3, 1)
                                    $ character.Statup("Love", 80, -4, 1)
                                    $ character.Statup("Obed", 30, -1, 1)
                                    $ character.Statup("Obed", 50, -1, 1)
                                    $ character.RecentActions.append("angry")
                                    $ character.DailyActions.append("angry")
                                    jump Jubes_HJ_After
        elif Cnt == 10 and character.SEXP <= 100 and not ApprovalCheck(character, 1200, "LO"):
                    $ character.Brows = "confused"
                    ch_v "This working for you?"
        #End Count check

        call Escalation(character) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_HJ_After:
    $ character.FaceChange("sexy")

    $ character.Hand += 1
    $ character.Action -=1
    $ character.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1
    $ character.Statup("Lust", 90, 5)

    call Partner_Like(character,1)

    if "Jubes Handi-Queen" in Achievements:
            pass
    elif character.Hand >= 10:
            $ character.FaceChange("smile", 1)
            ch_v "Looks like you filled out the punch card, [character.Petname]."
            $ Achievements.append("Jubes Handi-Queen")
            $character.SEXP += 5
    elif character.Hand == 1:
            $character.SEXP += 10
            if character.Love >= 500:
                $ character.Mouth = "smile"
                ch_v "That was kind of. . . pleasant. . ."
            elif Player.Focus <= 20:
                $ character.Mouth = "sad"
                ch_v "Did that do it for you?"
    elif character.Hand == 5:
                ch_v "I think I've got this down, maybe I should get a punch card."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_v "Ok, so what did you have in mind?"
    else:
        call Jubes_HJ_Reset
    call Checkout
    return

## end character.Handjob //////////////////////////////////////////////////////////////////////


## character.Titjob //////////////////////////////////////////////////////////////////////
label Jubes_Titjob:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Tit >= 7: # She loves it
        $ temp_modifier += 10
    elif character.Tit >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif character.Tit: #You've done it before
        $ temp_modifier += 5

    if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 15
    elif character.Addict >= 75:
        $ temp_modifier += 5

    if character.SeenChest and ApprovalCheck(character, 500): # You've seen her tits.
        $ temp_modifier += 10
    if not character.Chest and not character.Over: #She's already topless
        $ temp_modifier += 10
    if character.Lust > 75: #She's really horny
        $ temp_modifier += 10
    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (5*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 30
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no titjob" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no titjob" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1200, TabM = 4) # 120, 135, 150, Taboo -200(320)

    if not character.Tit and "no titjob" not in character.RecentActions:
        $ character.FaceChange("surprised", 1)
        $ character.Mouth = "kiss"
        ch_v "You want a titjob, huh?"

    if not character.Tit and Approval:                                                 #First time dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy")
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_v "Well, maybe you deserve it."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal")
            ch_v "If you'd like that. . ."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_v "Hmmmm. . . ."
        else: # Uninhibited
            $ character.FaceChange("sad")
            $ character.Mouth = "smile"
            ch_v "Sounds fun. . ."
    elif Approval:                                                                       #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_v "You're kinda pushing it."
        elif not Taboo and "tabno" in character.DailyActions:
            ch_v "Ok, I guess this is secluded enough. . ."
        elif "titjob" in character.RecentActions:
            $ character.FaceChange("sexy", 1)
            ch_v "Huh, again?"
            jump Jubes_TJ_Prep
        elif "titjob" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back for more?",
                "You're really working these puppies.",
                "Didn't get enough earlier?",
                "You're really working these puppies."])
            ch_v "[Line]"
        elif character.Tit < 3:
            $ character.FaceChange("sexy", 1)
            $ character.Brows = "confused"
            $ character.Mouth = "kiss"
            ch_v "Another titjob??"
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice(["You want some of this action [rubs her chest]?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "So you'd like another titjob?",
                "Another titjob?",
                "A little [points at her chest]?"])
            ch_v "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_v "Well, could be worse. . ."
        elif "no titjob" in character.DailyActions:
            ch_v "Hmm, I guess. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Well, sure, put it here.",
                "Well. . . ok.",
                "Yum.",
                "Sure, whip it out.",
                "Fine. . . [She drools a bit into her cleavage].",
                "Heh, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 70, 1)
        $ character.Statup("Inbt", 80, 2)
        jump Jubes_TJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no titjob" in character.RecentActions:
            ch_v "I {i}just{/i} told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions and "no titjob" in character.DailyActions:
            ch_v "This is just way too exposed!"
        elif "no titjob" in character.DailyActions:
            ch_v "I already told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_v "This is just way too exposed!"
        elif not character.Tit:
            $ character.FaceChange("bemused")
            ch_v "I'm not really into that, [character.Petname]. . ."
        else:
            $ character.FaceChange("bemused")
            ch_v "Not right now [character.Petname]. . ."

        menu:
            extend ""
            "Sorry, never mind." if "no titjob" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_v "Yeah, ok, [character.Petname]."
                return
            "Maybe later?" if "no titjob" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_v "Maybe."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no titjob")
                $ character.DailyActions.append("no titjob")
                return
            "I think this could be fun for both of us. . .":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 80, 2)
                    $ character.Statup("Obed", 40, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Well, ok, put it here.",
                        "Well. . . ok.",
                        "I guess.",
                        "I guess, whip it out.",
                        "Fine. . . [She drools a bit into her cleavage].",
                        "Heh, ok."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_TJ_Prep
                else:
                    $ Approval = ApprovalCheck(character, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)             Handy instead?
                    if Approval >= 2 and character.Blow:
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.FaceChange("confused", 1)
                        ch_v "I could maybe blow you?"
                        menu:
                            ch_v "How about that [[blowjob]?"
                            "Ok, get down there.":
                                $ character.Statup("Love", 80, 2)
                                $ character.Statup("Inbt", 60, 1)
                                $ character.Statup("Obed", 50, 1)
                                jump Jubes_BJ_Prep
                            "Nah, it's all about dem titties.":
                                $ Line = "no BJ"
                    if Approval and character.Hand:
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.FaceChange("confused", 1)
                        ch_v "I could give you a handy?"
                        menu:
                            ch_v "What do you say?"
                            "Sure, that's fine.":
                                $ character.Statup("Love", 80, 2)
                                $ character.Statup("Inbt", 60, 1)
                                $ character.Statup("Obed", 50, 1)
                                jump Jubes_HJ_Prep
                            "Seriously, titties." if Line == "no BJ":
                                $ Line = 0
                            "Nah, it's all about dem titties." if Line != "no BJ":
                                pass
                    $ character.Statup("Love", 200, -2)
                    ch_v "Nah."
                    $ character.Statup("Obed", 70, 2)


            "Come on, let me fuck those titties, [character.Pet]":                                               # Pressured into it
                $ character.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(character, 700, "OI", TabM = 4) # 70, 85, 100, -160(230)
                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 200, -2)
                    ch_v
                    $ character.Statup("Obed", 50, 4)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Forced = 1
                    jump Jubes_TJ_Prep
                else:
                    $ character.Statup("Love", 200, -15)
                    $ character.RecentActions.append("angry")
                    $ character.DailyActions.append("angry")

    #She refused all offers.
    if "no titjob" in character.DailyActions:
        $ character.FaceChange("angry", 1)

        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_v "No, try something else."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.DailyActions.append("tabno")
        ch_v "You really expect me to do that here? This isn't exactly \"covert.\""
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
    elif character.Tit:
        $ character.FaceChange("sad")
        ch_v "You'll know when it's time for that."
    else:
        $ character.FaceChange("normal", 1)
        ch_v "Nah."
    $ character.RecentActions.append("no titjob")
    $ character.DailyActions.append("no titjob")
    $ temp_modifier = 0
    return

label Jubes_TJ_Prep:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)


    $ character.FaceChange("sexy")
    if character.Forced:
        $ character.FaceChange("sad")
    elif not character.Tit:
        $ character.Brows = "confused"
        $ character.Eyes = "sexy"
        $ character.Mouth = "smile"

    call Seen_First_Peen(character,Partner,React=Situation)
    call Jubes_TJ_Launch("L")

    if Situation == character:
            #Jubes auto-starts
            $ Situation = 0
            "[character.Name] slides down and sandwiches your dick between her tits."
            menu:
                "What do you do?"
                "Nothing.":
                    $ character.Statup("Inbt", 80, 3)
                    $ character.Statup("Inbt", 40, 2)
                    "[character.Name] starts to slide them up and down."
                "Praise her.":
                    $ character.FaceChange("sexy", 1)
                    $ character.Statup("Inbt", 80, 3)
                    ch_p "Oh, that sounds like a good idea, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] continues her actions."
                    $ character.Statup("Love", 85, 1)
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ character.FaceChange("confused")
                    $ character.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] lets it drop out from between her breasts."
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ character.AddWord(1,"refused","refused")
                    return

    if not character.Tit:
        if character.Forced:
            $ character.Statup("Love", 90, -25)
            $ character.Statup("Obed", 70, 30)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no titjob")
    $ character.RecentActions.append("titjob")
    $ character.DailyActions.append("titjob")

label Jubes_TJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(character)
        call Jubes_TJ_Launch
        $ character.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if Speed == 0:
                                    call Speed_Shift(1)

                        "Speed up. . ." if  Speed == 1:
                                    call Speed_Shift(2)
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 2:
                                    pass

                        "Stop moving" if Speed != 0:
                                    call Speed_Shift(0)
                        "Slow Down. . ." if Speed == 2:
                                    call Speed_Shift(1)
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
                                            if character.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                if character.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Jubes_TJ_After
                                                                    call Jubes_Blowjob
                                                                else:
                                                                    call Sex_Basic_Dialog(character,"tired")

                                                        "How about a handy?":
                                                                if character.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Jubes_BJ_After
                                                                    call Jubes_Handjob
                                                                else:
                                                                    call Sex_Basic_Dialog(character,"tired")
                                                        "Never Mind":
                                                                jump Jubes_TJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Jubes_TJ_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_TJ_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Jubes_TJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And Jubes is unsatisfied,
                                "[character.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_TJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        if Speed >= 4:
                call Speed_Shift(0) #resets speed after orgasm
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
                pass
        elif Cnt == (5 + character.Tit):
                $ character.Brows = "confused"
                ch_v "Are you getting close here? I'm getting bored."
        if Cnt == (10 + character.Tit):
                $ character.Brows = "angry"
                menu:
                    ch_v "Seriously, can we do something else?"
                    "How about a BJ?" if character.Action and MultiAction:
                        $ Situation = "shift"
                        call Jubes_TJ_After
                        call Jubes_Blowjob
                        return
                    "Finish up." if Player.FocusX:
                        "You release your concentration. . ."
                        $ Player.FocusX = 0
                        $ Player.Focus += 15
                        jump Jubes_TJ_Cycle
                    "Let's try something else." if MultiAction:
                        $ Line = 0
                        call Jubes_TJ_Reset
                        $ Situation = "shift"
                        jump Jubes_TJ_After
                    "No, get back down there.":
                        if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                            $ character.Statup("Love", 200, -5)
                            $ character.Statup("Obed", 50, 3)
                            $ character.Statup("Obed", 80, 2)
                            "She grumbles but gets back to work."
                        else:
                            $ character.FaceChange("angry", 1)
                            "She scowls at you, drops you cock and pulls back."
                            ch_v "Well fuck you then."
                            $ character.Statup("Love", 50, -3, 1)
                            $ character.Statup("Love", 80, -4, 1)
                            $ character.Statup("Obed", 30, -1, 1)
                            $ character.Statup("Obed", 50, -1, 1)
                            $ character.RecentActions.append("angry")
                            $ character.DailyActions.append("angry")
                            jump Jubes_TJ_After
            #End Count check

        call Escalation(character) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_TJ_After:
    $ character.FaceChange("sexy")

    $ character.Tit += 1
    $ character.Action -=1
    $ character.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

    call Partner_Like(character,4)

    if character.Tit > 5:
        pass
    elif character.Tit == 1:
        $ character.SEXP += 12
        if character.Love >= 500:
            $ character.Mouth = "smile"
            ch_v "That was fun."
        elif Player.Focus <= 20:
            $ character.Mouth = "sad"
            ch_v "Well I hope you got something out of that."
    elif character.Tit == 5:
            ch_v "You seem to enjoy that."

    $ temp_modifier = 0

    if Situation == "shift":
            ch_v "Mmm, so what else did you have in mind?"
    else:
            call Jubes_TJ_Reset
    call Checkout
    return

## end character.Titjob //////////////////////////////////////////////////////////////////////



# character.Blowjob //////////////////////////////////////////////////////////////////////

label Jubes_Blowjob:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Blow >= 7: # She loves it
        $ temp_modifier += 15
    elif character.Blow >= 3: #You've done it before several times
        $ temp_modifier += 10
    elif character.Blow: #You've done it before
        $ temp_modifier += 7

    if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 25
    elif character.Addict >= 75: #She's really strung out
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (4*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no blow" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no blow" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)

    if not character.Blow and "no blow" not in character.RecentActions:
        $ character.FaceChange("surprised", 2)
        $ character.Mouth = "kiss"
        ch_v "You want me to suck your cock?"
        if character.Hand:
            $ character.Mouth = "smile"
            ch_v "Handjobs not enough now?"
        $ character.Blush = 1

    if not character.Blow and Approval:                                                 #First time dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy")
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_v "I have wondered how you taste."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal")
            ch_v "If that's what you want. . ."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_v "[[wipes away a little drool]"
        else: # Uninhibited
            $ character.FaceChange("sad")
            $ character.Mouth = "smile"
            ch_v "Huh. . ."
    elif Approval:                                                                       #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_v "Again?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_v "Hmm, this is private enough. . ."
        elif "blow" in character.RecentActions:
            $ character.FaceChange("sexy", 1)
            ch_v "Mmm, again? [[yawns]"
            jump Jubes_BJ_Prep
        elif "blow" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            $ Line = renpy.random.choice(["Back again so soon?",
                "Wear'in me out here.",
                "I must be too good at this.",
                "Let me get some saliva going.",
                "Didn't get enough earlier?"])
            ch_v "[Line]"
        elif character.Blow < 3:
            $ character.FaceChange("sexy", 1)
            $ character.Brows = "confused"
            $ character.Mouth = "kiss"
            ch_v "You'd like another blowjob?"
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to [mimes blowing]?",
                "So you want another blowjob?",
                "You want me to lick you?",
                "You want me to suck you off?",
                "A little bj?"])
            ch_v "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_v "Whatever."
        elif "no blow" in character.DailyActions:
            ch_v "Fine. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
                "Well. . . alright.",
                "Yum.",
                "Sure, whip it out.",
                "Ok. . . [She licks her lips].",
                "Alright, let's see it."])
            ch_v "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 70, 1)
        $ character.Statup("Inbt", 80, 2)
        jump Jubes_BJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no blow" in character.RecentActions:
            ch_v "Just told you I wouldn't, [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions and "no blow" in character.DailyActions:
            ch_v "Like I told you, not in public."
        elif "no blow" in character.DailyActions:
            ch_v "Told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_v "Like I told you, too public!"
        elif not character.Blow:
            $ character.FaceChange("bemused")
            ch_v "I don't know if your taste will match your scent, [character.Petname]. . ."
        else:
            $ character.FaceChange("bemused")
            ch_v "I don't know, [character.Petname]!"
        menu:
            extend ""
            "Sorry, never mind." if "no blow" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_v "Cool."
                return
            "Maybe later?" if "no blow" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_v "Yeah, maybe, [character.Petname]."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no blow")
                $ character.DailyActions.append("no blow")
                return
            "Come on, please?":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure. Ahhhhhh.",
                        "Well. . . alright.",
                        "Yum.",
                        "Sure, whip it out.",
                        "Ok. . . [She licks her lips].",
                        "Alright, let's see it."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_BJ_Prep
                else:
                    if ApprovalCheck(character, 1100, TabM = 3): # 110, 125, 140, Taboo -120(230)             Handy instead?
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.FaceChange("confused", 1)
                        $ character.ArmPose = 2
                        if character.Hand:
                            ch_v "Couldn't I just use my hand again?"
                            ch_v "You seemed to like that."
                        else:
                            ch_v "I could maybe use my hand instead, how's that sound?"
                        menu:
                            extend ""
                            "Sure, that's fine.":
                                $ character.Statup("Love", 80, 2)
                                $ character.Statup("Inbt", 60, 1)
                                $ character.Statup("Obed", 50, 1)
                                jump Jubes_HJ_Prep
                            "Nah, if it's not a BJ, forget it.":
                                $ character.Statup("Love", 200, -2)
                                $ character.ArmPose = 1
                                ch_v "Fine, be that way."
                                $ character.Statup("Obed", 70, 2)


            "Suck it, [character.Pet]":                                               # Pressured into it
                $ character.NameCheck() #checks reaction to petname
                $ Approval = ApprovalCheck(character, 750, "OI", TabM = 3) # 75, 90, 105, -120(195)
                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 200, -2)
                    ch_v
                    $ character.Statup("Obed", 50, 4)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Forced = 1
                    jump Jubes_BJ_Prep
                else:
                    $ character.Statup("Love", 200, -15)
                    $ character.RecentActions.append("angry")
                    $ character.DailyActions.append("angry")

    #She refused all offers.
    if "no blow" in character.DailyActions:
        $ character.FaceChange("angry", 1)
        $ character.ArmPose = 2
        $ character.Claws = 1

        $ character.ArmPose = 1
        $ character.Claws = 0
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_v "That's just pushing it."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
        $ character.RecentActions.append("no blow")
        $ character.DailyActions.append("no blow")
        return
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.DailyActions.append("tabno")
        ch_v "This area's too exposed."
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
        return
    elif character.Blow:
        $ character.FaceChange("sad")
        ch_v "Nah, not this time."
    else:
        $ character.FaceChange("normal", 1)
        ch_v "Nope."
    $ character.RecentActions.append("no blow")
    $ character.DailyActions.append("no blow")
    $ temp_modifier = 0
    return


label Jubes_BJ_Prep:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    if renpy.showing("Jubes_HJ_Animation"):
        hide Jubes_HJ_Animation with easeoutbottom
    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)

    $ character.FaceChange("sexy")
    if character.Forced:
        $ character.FaceChange("sad")
    elif not character.Blow:
        $ character.Brows = "confused"
        $ character.Eyes = "sexy"
        $ character.Mouth = "smile"

    call Seen_First_Peen(character,Partner,React=Situation)
    call Jubes_BJ_Launch("L")
    if Situation == character:
            #Jubes auto-starts
            $ Situation = 0
            "[character.Name] slides down and gives your cock a little lick."
            menu:
                "What do you do?"
                "Nothing.":
                    $ character.Statup("Inbt", 80, 3)
                    $ character.Statup("Inbt", 40, 2)
                    "[character.Name] continues licking at it."
                "Praise her.":
                    $ character.FaceChange("sexy", 1)
                    $ character.Statup("Inbt", 80, 3)
                    ch_p "Hmmm, keep doing that, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] continues her actions."
                    $ character.Statup("Love", 85, 1)
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ character.FaceChange("surprised")
                    $ character.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] puts it down."
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 3)
                    $ Player.RecentActions.append("nope")
                    $ character.AddWord(1,"refused","refused")
                    return
    if not character.Blow:
        if character.Forced:
            $ character.Statup("Love", 90, -70)
            $ character.Statup("Obed", 70, 45)
            $ character.Statup("Inbt", 80, 60)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 35)
            $ character.Statup("Inbt", 80, 40)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no blow")
    $ character.RecentActions.append("blow")
    $ character.DailyActions.append("blow")

label Jubes_BJ_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(character)
        call Jubes_BJ_Launch
        $ character.LustFace()

        if Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Lick it. . ." if Speed != 1:
                                call Speed_Shift(1)
                        "Lick it. . . (locked)" if Speed == 1:
                                pass

                        "Just the head. . ." if Speed != 2:
                                call Speed_Shift(2)
                        "Just the head. . . (locked)" if Speed == 2:
                                pass

                        "Suck on it." if Speed != 3:
                                call Speed_Shift(3)
                                if Trigger2 == "jackin":
                                    "She dips her head a bit lower, and you move your hand out of the way."

                                if "Gwentro" not in character.History: #calls the special Gwentro event
                                            call Gwentro

                        "Suck on it. (locked)" if Speed == 3:
                                pass

                        "Take it deeper." if Speed != 4:
                                    if Trigger2 == "jackin" and Speed != 3:
                                        "She takes it to the root, and you move your hand out of the way."
                                    call Speed_Shift(4)
                        "Take it deeper. (locked)" if Speed == 4:
                                pass

                        "Set your own pace. . .":
                                "[character.Name] hums contentedly."
                                if "setpace" not in character.RecentActions:
                                    $ character.Statup("Love", 80, 2)
                                $ D20 = renpy.random.randint(1, 20)
                                if character.Blow < 5:
                                    $ D20 -= 10
                                elif character.Blow < 10:
                                    $ D20 -= 5

                                if D20 > 15:
                                    call Speed_Shift(4)
                                    if "setpace" not in character.RecentActions:
                                        $ character.Statup("Inbt", 80, 3)
                                elif D20 > 10:
                                    call Speed_Shift(3)
                                elif D20 > 5:
                                    call Speed_Shift(2)
                                else:
                                    call Speed_Shift(1)
                                $ character.RecentActions.append("setpace")

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
                                            if character.Action and MultiAction:
                                                $ Trigger2 = "fondle breasts"
                                                "You start to fondle her breasts."
                                                $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "How about a handy?":
                                                                if character.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Jubes_BJ_After
                                                                    call Jubes_Handjob
                                                                else:
                                                                    ch_v "I need a break, can we wrap on this?"
                                                        "How about a titjob?":
                                                                if character.Action and MultiAction:
                                                                    $ Situation = "shift"
                                                                    call Jubes_BJ_After
                                                                    call Jubes_Titjob
                                                                else:
                                                                    ch_v "I need a break, can we wrap on this?"
                                                        "Never Mind":
                                                                jump Jubes_BJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1
        if Speed:
            $ Player.Wet = 1 #wets penis
            $ Player.Spunk = 0 if Player.Spunk else Player.Spunk #cleans you off after one cycle

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Jubes_BJ_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2 and character.SEXP >= 20:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_BJ_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Jubes_BJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."

                            if "unsatisfied" in character.RecentActions:#And Jubes is unsatisfied,
                                "[character.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_BJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (10 + character.Blow):
                $ character.Brows = "angry"
                menu:
                    ch_v "I'm getting kinda bored. Can we do something else?"
                    "How about a Handy?" if character.Action and MultiAction:
                            $ Situation = "shift"
                            call Jubes_BJ_After
                            call Jubes_Handjob
                            return
                    "Finish up." if Player.FocusX:
                            "You release your concentration. . ."
                            $ Player.FocusX = 0
                            $ Player.Focus += 15
                            jump Jubes_BJ_Cycle
                    "Let's try something else." if MultiAction:
                            $ Line = 0
                            call Jubes_BJ_Reset
                            $ Situation = "shift"
                            jump Jubes_BJ_After
                    "No, get back down there.":
                            if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                $ character.Statup("Love", 200, -5)
                                $ character.Statup("Obed", 50, 3)
                                $ character.Statup("Obed", 80, 2)
                                "She grumbles but gets back to work."
                            else:
                                $ character.FaceChange("angry", 1)
                                "She scowls at you, drops you cock and pulls back."
                                ch_v "Well fuck you then."
                                $ character.Statup("Love", 50, -3, 1)
                                $ character.Statup("Love", 80, -4, 1)
                                $ character.Statup("Obed", 30, -1, 1)
                                $ character.Statup("Obed", 50, -1, 1)
                                $ character.RecentActions.append("angry")
                                $ character.DailyActions.append("angry")
                                jump Jubes_BJ_After
        elif Cnt == (5 + character.Blow) and character.SEXP <= 100 and not ApprovalCheck(character, 1200, "LO"):
                    $ character.Brows = "confused"
                    ch_v "Are you getting close here? I'm bored."
        #End Count check

        call Escalation(character) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_BJ_After:
    $ character.FaceChange("sexy")

    $ character.Blow += 1
    $ character.Action -=1
    $ character.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1

    call Partner_Like(character,2)

    if "Jubes Jobber" in Achievements:
        pass
    elif character.Blow >= 10:
        $ character.FaceChange("smile", 1)
        ch_v "Your flavor is intoxicating."
        $ Achievements.append("Jubes Jobber")
        $character.SEXP += 5
    elif Situation == "shift":
        pass
    elif character.Blow == 1:
            $character.SEXP += 15
            if character.Love >= 500:
                $ character.Mouth = "smile"
                ch_v "Hey, whaddaya know, that wasn't bad."
            elif Player.Focus <= 20:
                $ character.Mouth = "sad"
                ch_v "I hope you enjoyed that."
    elif character.Blow == 5:
        ch_v "I'm really getting the hang of this. . . right?"
        menu:
            "[[nod]":
                $ character.FaceChange("smile", 1)
                $ character.Statup("Love", 90, 15)
                $ character.Statup("Obed", 80, 5)
                $ character.Statup("Inbt", 90, 10)
            "[[shake head \"no\"]":
                if ApprovalCheck(character, 500, "O"):
                    $ character.FaceChange("sad", 2)
                    $ character.Statup("Love", 200, -5)
                else:
                    $ character.FaceChange("angry", 2)
                    $ character.Statup("Love", 200, -25)
                $ character.Statup("Obed", 80, 10)
                ch_v ". . ."
                $ character.FaceChange("sad", 1)

    $ temp_modifier = 0
    if Situation != "shift":
        call Jubes_BJ_Reset
    call Checkout
    return



# end character.Blowjob                                 //////////////////////////////////////////////////////////////////////////////

# ////////////////////////////////////////////////////////////////////////Start Insert Pussy
label Jubes_Dildo_Check:
    if "dildo" in Player.Inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in character.Inventory:
        "You ask [character.Name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."
        return 0
    return 1

label Jubes_Dildo_Pussy:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    call Jubes_Dildo_Check
    if not _return:
        return

    if character.DildoP: #You've done it before
        $ temp_modifier += 15
    if character.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if character.Lust > 95:
        $ temp_modifier += 20
    elif character.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (5*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)

    if Situation == character:                                                                  #Jubes auto-starts
                if Approval > 2:                                                      # fix, add jubes auto stuff here
                    if character.PantsNum() == 5:
                        "[character.Name] grabs her dildo, hiking up her skirt as she does."
                        $ character.Upskirt = 1
                    elif character.PantsNum() >= 6:
                        "[character.Name] grabs her dildo, pulling down her pants as she does."
                        $ character.Legs = 0
                    else:
                        "[character.Name] grabs her dildo, rubbing is suggestively against her crotch."
                    $ character.SeenPanties = 1
                    call Jubes_First_Bottomless(1)
                    "She slides the tip along her pussy and seems to want you to insert it."
                    menu:
                        "What do you do?"
                        "Nothing.":
                            $ character.Statup("Inbt", 80, 3)
                            $ character.Statup("Inbt", 50, 2)
                            "[character.Name] slides it in."
                        "Go for it.":
                            $ character.FaceChange("sexy", 1)
                            $ character.Statup("Inbt", 80, 3)
                            ch_p "Oh yeah, [character.Pet], let's do this."
                            $ character.NameCheck() #checks reaction to petname
                            "You grab the dildo and slide it in."
                            $ character.Statup("Love", 85, 1)
                            $ character.Statup("Obed", 90, 1)
                            $ character.Statup("Obed", 50, 2)
                        "Ask her to stop.":
                            $ character.FaceChange("surprised")
                            $ character.Statup("Inbt", 70, 1)
                            ch_p "Let's not do that right now, [character.Pet]."
                            $ character.NameCheck() #checks reaction to petname
                            "[character.Name] sets the dildo down."
                            $ character.OutfitChange()
                            $ character.Statup("Obed", 90, 1)
                            $ character.Statup("Obed", 50, 1)
                            $ character.Statup("Obed", 30, 2)
                            return
                    jump Jubes_DP_Prep
                else:
                    $ temp_modifier = 0                               # fix, add jubes auto stuff here
                    $ Trigger2 = 0
                return

    if Situation == "auto":
                "You rub the dildo across her body, and along her moist slit."
                $ character.FaceChange("surprised", 1)

                if (character.DildoP and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                    "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 70, 3)
                    $ character.Statup("Inbt", 50, 3)
                    $ character.Statup("Inbt", 70, 1)
                    ch_v "Ooo, [character.Petname], toys!"
                    jump Jubes_DP_Prep
                else:                                                                                                            #she's questioning it
                    $ character.Brows = "angry"
                    menu:
                        ch_v "Hey, what are you planning to do with that?!"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                $ character.FaceChange("sexy", 1)
                                $ character.Statup("Obed", 70, 3)
                                $ character.Statup("Inbt", 50, 3)
                                $ character.Statup("Inbt", 70, 1)
                                ch_v "Well, now that you mention it. . ."
                                jump Jubes_DP_Prep
                            "You pull back before you really get it in."
                            $ character.FaceChange("bemused", 1)
                            if character.DildoP:
                                ch_v "Well ok, [character.Petname], maybe warn me next time?"
                            else:
                                ch_v "Well ok, [character.Petname], that's a little much. . . for now . . ."
                        "Just playing with my favorite toys.":
                            $ character.Statup("Love", 80, -10, 1)
                            $ character.Statup("Love", 200, -10)
                            "You press it inside some more."
                            $ character.Statup("Obed", 70, 3)
                            $ character.Statup("Inbt", 50, 3)
                            if not ApprovalCheck(character, 700, "O", TabM=1): #Checks if Obed is 700+
                                $ character.FaceChange("angry")
                                "[character.Name] shoves you away and slaps you in the face."
                                ch_v "Jerk!"
                                ch_v "Ask nice if you want to stick something in my pussy!"
                                $ character.Statup("Love", 50, -10, 1)
                                $ character.Statup("Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                if renpy.showing("Jubes_SexSprite"):
                                    call Jubes_Sex_Reset
                                $ character.RecentActions.append("angry")
                                $ character.DailyActions.append("angry")
                            else:
                                $ character.FaceChange("sad")
                                "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."
                                jump Jubes_DP_Prep
                return
    #end Auto

    if not character.DildoP:
            #first time
            $ character.FaceChange("surprised", 1)
            $ character.Mouth = "kiss"
            ch_v "Hmmm, so you'd like to try out some toys?"
            if character.Forced:
                $ character.FaceChange("sad")
                ch_v "I suppose there are worst things you could ask for."

    if not character.DildoP and Approval:
            #First time dialog
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
            elif character.Love >= (character.Obed + character.Inbt):
                $ character.FaceChange("sexy")
                $ character.Brows = "sad"
                $ character.Mouth = "smile"
                ch_v "I've had a reasonable amount of experience with these, you know. . ."
            elif character.Obed >= character.Inbt:
                $ character.FaceChange("normal")
                ch_v "If that's what you want, [character.Petname]. . ."
            else: # Uninhibited
                $ character.FaceChange("sad")
                $ character.Mouth = "smile"
                ch_v "I guess it could be fun with a partner. . ."

    elif Approval:
            #Second time+ dialog
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
                ch_v "The toys again?"
            elif not Taboo and "tabno" in character.DailyActions:
                ch_v "Well, at least you got us some privacy this time. . ."
            elif "dildo pussy" in character.RecentActions:
                $ character.FaceChange("sexy", 1)
                ch_v "Mmm, again? Ok, let's get to it."
                jump Jubes_DP_Prep
            elif "dildo pussy" in character.DailyActions:
                $ character.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "You're going to wear me out."])
                ch_v "[Line]"
            elif character.DildoP < 3:
                $ character.FaceChange("sexy", 1)
                $ character.Brows = "confused"
                $ character.Mouth = "kiss"
                ch_v "You want to stick it in my pussy again?"
            else:
                $ character.FaceChange("sexy", 1)
                $ character.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my pussy again?",
                    "You want me ta lube up your toy?"])
                ch_v "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Inbt", 60, 1)
                ch_v "Ok, fine."
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
                ch_v "[Line]"
                $ Line = 0
            $ character.Statup("Obed", 20, 1)
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 70, 2)
            jump Jubes_DP_Prep

    else:
            #She's not into it, but maybe. . .
            $ character.FaceChange("angry")
            if "no dildo" in character.RecentActions:
                ch_v "What part of \"no,\" did you not get, [character.Petname]?"
            elif Taboo and "tabno" in character.DailyActions and "no dildo" in character.DailyActions:
                ch_v "Stop swinging that thing around in public!"
            elif "no dildo" in character.DailyActions:
                ch_v "I already told you \"no,\" [character.Petname]."
            elif Taboo and "tabno" in character.DailyActions:
                ch_v "Stop swinging that thing around in public!"
            elif not character.DildoP:
                $ character.FaceChange("bemused")
                ch_v "I'm just not into toys, [character.Petname]. . ."
            else:
                $ character.FaceChange("bemused")
                ch_v "I don't think we need any toys, [character.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in character.DailyActions:
                    $ character.FaceChange("bemused")
                    ch_v "Yeah, ok, [character.Petname]."
                    return
                "Maybe later?" if "no dildo" not in character.DailyActions:
                    $ character.FaceChange("sexy")
                    ch_v "Maybe I'll practice on my own time, [character.Petname]."
                    $ character.Statup("Love", 80, 2)
                    $ character.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ character.RecentActions.append("tabno")
                        $ character.DailyActions.append("tabno")
                    $ character.RecentActions.append("no dildo")
                    $ character.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ character.FaceChange("sexy")
                        $ character.Statup("Obed", 90, 2)
                        $ character.Statup("Obed", 50, 2)
                        $ character.Statup("Inbt", 70, 3)
                        $ character.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_v "[Line]"
                        $ Line = 0
                        jump Jubes_DP_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(character, 950, "OI", TabM = 3) # 95, 110, 125, -120(215)
                    if Approval > 1 or (Approval and character.Forced):
                        $ character.FaceChange("sad")
                        $ character.Statup("Love", 70, -5, 1)
                        $ character.Statup("Love", 200, -5)
                        ch_v
                        $ character.Statup("Obed", 80, 4)
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.Forced = 1
                        jump Jubes_DP_Prep
                    else:
                        $ character.Statup("Love", 200, -20)
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no dildo" in character.DailyActions:

            $ character.RecentActions.append("angry")
            $ character.DailyActions.append("angry")
    elif character.Forced:
            $ character.FaceChange("angry", 1)
            ch_v "I'm not going to let you use that on me."
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
            ch_v "Not here!"
            $ character.Statup("Lust", 200, 5)
            $ character.Statup("Obed", 50, -3)
    elif character.DildoP:
            $ character.FaceChange("sad")
            ch_v "Sorry, you can keep your toys to yourself."
    else:
            $ character.FaceChange("normal", 1)
            ch_v "No way."
    $ character.RecentActions.append("no dildo")
    $ character.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Jubes_DP_Prep: #Animation set-up
    if Trigger2 == "dildo pussy":
        return

    if not character.Forced and Situation != "auto":
        $ temp_modifier = 15 if character.PantsNum() >= 6 else 0
        call Bottoms_Off(character)
        if "angry" in character.RecentActions:
            return

    $ temp_modifier = 0
    call Jubes_Pussy_Launch("dildo pussy")
    if not character.DildoP:
        if character.Forced:
            $ character.Statup("Love", 90, -75)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 45)
    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no dildo")
    $ character.RecentActions.append("dildo pussy")
    $ character.DailyActions.append("dildo pussy")

label Jubes_DP_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(character)
        call Jubes_Pussy_Launch("dildo pussy")
        $ character.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(character)
                                jump Jubes_DP_Cycle

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
                                            if character.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her ass.":
                                                                $ Situation = "shift"
                                                                call Jubes_DP_After
                                                                call Jubes_Insert_Ass
                                                        "Just stick a finger in her ass without asking.":
                                                                $ Situation = "auto"
                                                                call Jubes_DP_After
                                                                call Jubes_Insert_Ass
                                                        "I want to shift the dildo to her ass.":
                                                                $ Situation = "shift"
                                                                call Jubes_DP_After
                                                                call Jubes_Dildo_Ass
                                                        "Never Mind":
                                                                jump Jubes_DP_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

        #End menu (if Line)

        if character.Panties or character.PantsNum() >= 6 or character.HoseNum() >= 5: #This checks if Jubes wants to strip down.
                call Girl_Undress(character,"auto")

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Jubes_Pos_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_DP_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Jubes_DP_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And Jubes is unsatisfied,
                                "[character.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_DP_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (5 + character.DildoP):
                    $ character.Brows = "confused"
                    ch_v "What are you even doing down there?"
        elif character.Lust >= 80:
                    pass
        elif Cnt == (15 + character.DildoP) and character.SEXP >= 15 and not ApprovalCheck(character, 1500):
                    $ character.Brows = "confused"
                    menu:
                        ch_v "[character.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Jubes_DP_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jubes_DP_After
                        "No, this is fun.":
                                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                    $ character.Statup("Love", 200, -5)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ character.FaceChange("angry", 1)
                                    call Jubes_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_v "Well if that's your attitude, I don't need your \"help\"."
                                    $ character.Statup("Love", 50, -3, 1)
                                    $ character.Statup("Love", 80, -4, 1)
                                    $ character.Statup("Obed", 30, -1, 1)
                                    $ character.Statup("Obed", 50, -1, 1)
                                    $ character.RecentActions.append("angry")
                                    $ character.DailyActions.append("angry")
                                    jump Jubes_DP_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "Ok, that's it, I need a break."


label Jubes_DP_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jubes_Pos_Reset

    $ character.FaceChange("sexy")

    $ character.DildoP += 1
    $ character.Action -=1

    call Partner_Like(character,1)

    if character.DildoP == 1:
            $ character.SEXP += 10
            if not Situation:
                if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                    ch_v "Thanks for the extra hand. . ."
                elif character.Obed <= 500 and Player.Focus <= 20:
                    $ character.FaceChange("perplexed", 1)
                    ch_v "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_v "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end character.Dildo Pussy /////////////////////////////////////////////////////////////////////////////


# ////////////////////////////////////////////////////////////////////////Start Insert Ass

label Jubes_Dildo_Ass:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    call Jubes_Dildo_Check
    if not _return:
        return

    if character.Loose:
        $ temp_modifier += 30
    elif "anal" in character.RecentActions or "dildo anal" in character.RecentActions:
        $ temp_modifier -= 20
    elif "anal" in character.DailyActions or "dildo anal" in character.DailyActions:
        $ temp_modifier -= 10
    elif (character.Anal + character.DildoA + character.Plug) > 0: #You've done it before
        $ temp_modifier += 20

    if character.Legs == "pants:": # she's got pants on.
        $ temp_modifier -= 20

    if character.Lust > 95:
        $ temp_modifier += 20
    elif character.Lust > 85: #She's really horny
        $ temp_modifier += 15

    if Situation == "shift":
        $ temp_modifier += 10
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (5*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no dildo" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no dildo" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)

    if Situation == character:
            #Jubes auto-starts
            if Approval > 2:                                                      # fix, add jubes auto stuff here
                if character.PantsNum() == 5:
                    "[character.Name] grabs her dildo, hiking up her skirt as she does."
                    $ character.Upskirt = 1
                elif character.PantsNum() >= 6:
                    "[character.Name] grabs her dildo, pulling down her pants as she does."
                    $ character.Legs = 0
                else:
                    "[character.Name] grabs her dildo, rubbing is suggestively against her ass."
                $ character.SeenPanties = 1
                call Jubes_First_Bottomless(1)
                "She slides the tip against her asshole, and seems to want you to insert it."
                menu:
                    "What do you do?"
                    "Nothing.":
                        $ character.Statup("Inbt", 80, 3)
                        $ character.Statup("Inbt", 50, 2)
                        "[character.Name] slides it in."
                    "Go for it.":
                        $ character.FaceChange("sexy", 1)
                        $ character.Statup("Inbt", 80, 3)
                        ch_p "Oh yeah, [character.Pet], let's do this."
                        $ character.NameCheck() #checks reaction to petname
                        "You grab the dildo and slide it in."
                        $ character.Statup("Love", 85, 1)
                        $ character.Statup("Obed", 90, 1)
                        $ character.Statup("Obed", 50, 2)
                    "Ask her to stop.":
                        $ character.FaceChange("surprised")
                        $ character.Statup("Inbt", 70, 1)
                        ch_p "Let's not do that right now, [character.Pet]."
                        $ character.NameCheck() #checks reaction to petname
                        "[character.Name] sets the dildo down."
                        $ character.OutfitChange()
                        $ character.Statup("Obed", 90, 1)
                        $ character.Statup("Obed", 50, 1)
                        $ character.Statup("Obed", 30, 2)
                        return
                jump Jubes_DA_Prep
            else:
                $ temp_modifier = 0                               # fix, add jubes auto stuff here
                $ Trigger2 = 0
            return

    if Situation == "auto":
            "You rub the dildo across her body, and against her tight anus."
            $ character.FaceChange("surprised", 1)

            if (character.DildoA and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                "[character.Name] is briefly startled and turns towards you, but then smiles and makes a little humming noise."
                $ character.FaceChange("sexy")
                $ character.Statup("Obed", 70, 3)
                $ character.Statup("Inbt", 50, 3)
                $ character.Statup("Inbt", 70, 1)
                ch_v "Ooo, [character.Petname], toys!"
                jump Jubes_DA_Prep
            else:
                #she's questioning it
                $ character.Brows = "angry"
                menu:
                    ch_v "Hey, what are you planning to do with that?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            $ character.FaceChange("sexy", 1)
                            $ character.Statup("Obed", 70, 3)
                            $ character.Statup("Inbt", 50, 3)
                            $ character.Statup("Inbt", 70, 1)
                            ch_v "Well, now that you mention it. . ."
                            jump Jubes_DA_Prep
                        "You pull back before you really get it in."
                        $ character.FaceChange("bemused", 1)
                        if character.DildoA:
                            ch_v "Well ok, [character.Petname], maybe warn me next time?"
                        else:
                            ch_v "Well ok, [character.Petname], that's a little much. . . for now . . ."
                    "Just playing with my favorite toys.":
                        $ character.Statup("Love", 80, -10, 1)
                        $ character.Statup("Love", 200, -10)
                        "You press it inside some more."
                        $ character.Statup("Obed", 70, 3)
                        $ character.Statup("Inbt", 50, 3)
                        if not ApprovalCheck(character, 700, "O", TabM=1): #Checks if Obed is 700+
                            $ character.FaceChange("angry")
                            "[character.Name] shoves you away and slaps you in the face."
                            ch_v "Jerk!"
                            ch_v "Ask nice if you want to stick something in my ass!"
                            $ character.Statup("Love", 50, -10, 1)
                            $ character.Statup("Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            if renpy.showing("Jubes_SexSprite"):
                                call Jubes_Sex_Reset
                            $ character.RecentActions.append("angry")
                            $ character.DailyActions.append("angry")
                        else:
                            $ character.FaceChange("sad")
                            "[character.Name] doesn't seem to be into this, you're lucky she's so obedient."
                            jump Jubes_DA_Prep
            return
    #end auto

    if not character.DildoA:
            #first time
            $ character.FaceChange("surprised", 1)
            $ character.Mouth = "kiss"
            ch_v "You want to try and fit that. . .?"
            if character.Forced:
                $ character.FaceChange("sad")
                ch_v "Always about the butt, huh?"

    if not character.Loose and ("dildo anal" in character.RecentActions or "anal" in character.RecentActions or "dildo anal" in character.DailyActions or "anal" in character.DailyActions):
            $ character.FaceChange("bemused", 1)
            ch_v "I'm still sore from earlier. . ."

    if not character.DildoA and Approval:
            #First time dialog
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
            elif character.Love >= (character.Obed + character.Inbt):
                $ character.FaceChange("sexy")
                $ character.Brows = "sad"
                $ character.Mouth = "smile"
                ch_v "I haven't actually used one of these, back there before. . ."
            elif character.Obed >= character.Inbt:
                $ character.FaceChange("normal")
                ch_v "If that's what you want, [character.Petname]. . ."
            else: # Uninhibited
                $ character.FaceChange("sad")
                $ character.Mouth = "smile"
                ch_v "I guess it could be fun two-player. . ."

    elif Approval:
            #Second time+ dialog
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Love", 70, -3, 1)
                $ character.Statup("Love", 20, -2, 1)
                ch_v "The toys again?"
            elif not Taboo and "tabno" in character.DailyActions:
                ch_v "Well, at least you got us some privacy this time. . ."
            elif "dildo anal" in character.DailyActions and not character.Loose:
                pass
            elif "dildo anal" in character.DailyActions:
                $ character.FaceChange("sexy", 1)
                $ Line = renpy.random.choice(["Breaking out the toys again?",
                    "Didn't get enough earlier?",
                    "I'm still a bit sore from earlier.",
                    "You're going to wear me out."])
                ch_v "[Line]"
            elif character.DildoA < 3:
                $ character.FaceChange("sexy", 1)
                $ character.Brows = "confused"
                $ character.Mouth = "kiss"
                ch_v "You want to stick it in my ass again?"
            else:
                $ character.FaceChange("sexy", 1)
                $ character.ArmPose = 2
                $ Line = renpy.random.choice(["You want some of this action?",
                    "So you'd like another go?",
                    "You want to stick it in my ass again?",
                    "You want me ta lube up your toy?"])
                ch_v "[Line]"
                $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if character.Forced:
                $ character.FaceChange("sad")
                $ character.Statup("Obed", 90, 1)
                $ character.Statup("Inbt", 60, 1)
                ch_v "Ok, fine."
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
                ch_v "[Line]"
                $ Line = 0
            $ character.Statup("Obed", 20, 1)
            $ character.Statup("Obed", 60, 1)
            $ character.Statup("Inbt", 70, 2)
            jump Jubes_DA_Prep

    else:
            #She's not into it, but maybe. . .
            $ character.FaceChange("angry")
            if "no dildo" in character.RecentActions:
                ch_v "What part of \"no,\" did you not get, [character.Petname]?"
            elif Taboo and "tabno" in character.DailyActions and "no dildo" in character.DailyActions:
                ch_v "Stop swinging that thing around in public!"
            elif "no dildo" in character.DailyActions:
                ch_v "I already told you \"no,\" [character.Petname]."
            elif Taboo and "tabno" in character.DailyActions:
                ch_v "I already told you that I wouldn't do that out here!"
            elif not character.DildoA:
                $ character.FaceChange("bemused")
                ch_v "I'm just not into toys, [character.Petname]. . ."
            elif not character.Loose and "dildo anal" not in character.DailyActions:
                $ character.FaceChange("perplexed")
                ch_v "You could have been a bit more gentle last time, [character.Petname]. . ."
            else:
                $ character.FaceChange("bemused")
                ch_v "I don't think we need any toys, [character.Petname]."
            menu:
                extend ""
                "Sorry, never mind." if "no dildo" in character.DailyActions:
                    $ character.FaceChange("bemused")
                    ch_v "Yeah, ok, [character.Petname]."
                    return
                "Maybe later?" if "no dildo" not in character.DailyActions:
                    $ character.FaceChange("sexy")
                    ch_v "Maybe I'll practice on my own time, [character.Petname]."
                    $ character.Statup("Love", 80, 2)
                    $ character.Statup("Inbt", 70, 2)
                    if Taboo:
                        $ character.RecentActions.append("tabno")
                        $ character.DailyActions.append("tabno")
                    $ character.RecentActions.append("no dildo")
                    $ character.DailyActions.append("no dildo")
                    return
                "I think you'd like it. . .":
                    if Approval:
                        $ character.FaceChange("sexy")
                        $ character.Statup("Obed", 90, 2)
                        $ character.Statup("Obed", 50, 2)
                        $ character.Statup("Inbt", 70, 3)
                        $ character.Statup("Inbt", 40, 2)
                        $ Line = renpy.random.choice(["Well, sure, stick it in.",
                            "I suppose. . .",
                            "You've got me there."])
                        ch_v "[Line]"
                        $ Line = 0
                        jump Jubes_DA_Prep
                    else:
                        pass

                "[[press it against her]":                                               # Pressured into it
                    $ Approval = ApprovalCheck(character, 1050, "OI", TabM = 3) # 105, 120, 135, -120(225)
                    if Approval > 1 or (Approval and character.Forced):
                        $ character.FaceChange("sad")
                        $ character.Statup("Love", 70, -5, 1)
                        $ character.Statup("Love", 200, -5)

                        $ character.Statup("Obed", 80, 4)
                        $ character.Statup("Inbt", 80, 1)
                        $ character.Statup("Inbt", 60, 3)
                        $ character.Forced = 1
                        jump Jubes_DA_Prep
                    else:
                        $ character.Statup("Love", 200, -20)
                        $ character.RecentActions.append("angry")
                        $ character.DailyActions.append("angry")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no dildo" in character.DailyActions:

            $ character.RecentActions.append("angry")
            $ character.DailyActions.append("angry")
    elif character.Forced:
            $ character.FaceChange("angry", 1)
            ch_v "I'm not going to let you use that on me."
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
            ch_v "Not here!"
            $ character.Statup("Lust", 200, 5)
            $ character.Statup("Obed", 50, -3)
    elif not character.Loose and "dildo anal" in character.DailyActions:
            $ character.FaceChange("bemused")
            ch_v "Sorry, I just need a little break back there, [character.Petname]."
    elif character.DildoA:
            $ character.FaceChange("sad")
            ch_v "Sorry, you can keep your toys out of there."
    else:
            $ character.FaceChange("normal", 1)
            ch_v "No way."
    $ character.RecentActions.append("no dildo")
    $ character.DailyActions.append("no dildo")
    $ temp_modifier = 0
    return

label Jubes_DA_Prep: #Animation set-up
    if Trigger2 == "dildo anal":
        return

    if not character.Forced and Situation != "auto":
        $ temp_modifier = 20 if character.PantsNum() >= 6 else 0
        call Bottoms_Off(character)
        if "angry" in character.RecentActions:
            return

    $ temp_modifier = 0
    call Jubes_Pussy_Launch("dildo anal")
    if not character.DildoA:
        if character.Forced:
            $ character.Statup("Love", 90, -75)
            $ character.Statup("Obed", 70, 60)
            $ character.Statup("Inbt", 80, 35)
        else:
            $ character.Statup("Love", 90, 10)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 45)
    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no dildo")
    $ character.RecentActions.append("dildo anal")
    $ character.DailyActions.append("dildo anal")

label Jubes_DA_Cycle: #Repeating strokes
    while Round > 0:
        call Shift_Focus(character)
        call Jubes_Pussy_Launch("dildo anal")
        $ character.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                call Slap_Ass(character)
                                jump Jubes_DA_Cycle

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
                                            if character.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "I want to stick a finger in her pussy.":
                                                                $ Situation = "shift"
                                                                call Jubes_DA_After
                                                                call Jubes_Fondle_Pussy
                                                        "Just stick a finger in her pussy without asking.":
                                                                $ Situation = "auto"
                                                                call Jubes_DA_After
                                                                call Jubes_Fondle_Pussy
                                                        "I want to shift the dildo to her pussy.":
                                                                $ Situation = "shift"
                                                                call Jubes_DA_After
                                                                call Jubes_Dildo_Pussy
                                                        "Never Mind":
                                                                jump Jubes_DA_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift your focus" if Trigger2:
                                                $ Situation = "shift focus"
                                                call Jubes_DA_After
                                                call Offhand_Set
                                    "Shift your focus (locked)" if not Trigger2:
                                                pass

        #End menu (if Line)

        if character.Panties or character.PantsNum() >= 6 or character.HoseNum() >= 5: #This checks if Jubes wants to strip down.
                call Girl_Undress(character,"auto")

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Jubes_Pos_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_DA_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Jubes_DA_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And Jubes is unsatisfied,
                                "[character.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_DA_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 12 if Player.FocusX and Player.Focus > 50 else 0

        if character.SEXP >= 100 or ApprovalCheck(character, 1200, "LO"):
            pass
        elif Cnt == (5 + character.DildoA):
                    $ character.Brows = "confused"
                    ch_v "What are you even doing down there?"
        elif character.Lust >= 80:
                    pass
        elif Cnt == (15 + character.DildoA) and character.SEXP >= 15 and not ApprovalCheck(character, 1500):
                    $ character.Brows = "confused"
                    menu:
                        ch_v "[character.Petname], this is getting uncomfortable, maybe we could try something else."
                        "Finish up.":
                                "You let go. . ."
                                jump Jubes_DA_After
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                $ Situation = "shift"
                                jump Jubes_DA_After
                        "No, this is fun.":
                                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                    $ character.Statup("Love", 200, -5)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 80, 2)
                                    "She grumbles but lets you keep going."
                                else:
                                    $ character.FaceChange("angry", 1)
                                    call Jubes_Pos_Reset
                                    "She scowls at you and pulls back."
                                    ch_v "Well if that's your attitude, I don't need your \"help\"."
                                    $ character.Statup("Love", 50, -3, 1)
                                    $ character.Statup("Love", 80, -4, 1)
                                    $ character.Statup("Obed", 30, -1, 1)
                                    $ character.Statup("Obed", 50, -1, 1)
                                    $ character.RecentActions.append("angry")
                                    $ character.DailyActions.append("angry")
                                    jump Jubes_DA_After
        #End Count check

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_DA_After:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        call Jubes_Pos_Reset

    $ character.FaceChange("sexy")

    $ character.DildoA += 1
    $ character.Action -=1

    call Partner_Like(character,1)

    if character.DildoA == 1:
            $ character.SEXP += 10
            if not Situation:
                if character.Love >= 500 and "unsatisfied" not in character.RecentActions:
                    if character.Loose:
                        ch_v "That was. . . interesting. . ."
                    else:
                        ch_v "Ouch. . ."
                elif character.Obed <= 500 and Player.Focus <= 20:
                    $ character.FaceChange("perplexed", 1)
                    ch_v "Did you like that?"

    $ temp_modifier = 0
#    if Situation == "shift":
#        ch_v "Mmm, so what else did you have in mind?"
    call Checkout
    return

# end character.Dildo Ass /////////////////////////////////////////////////////////////////////////////

label Jubes_Vibrator_Check:                                                                                 #fix this whole section is copy/paste unfinished
    if "vibrator" in Player.Inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in character.Inventory:
        "You ask [character.Name] to get out her vibrator."
    else:
        "You don't have one of those on you."
        return 0
    return 1

## character.Footjob //////////////////////////////////////////////////////////////////////
label Jubes_Footjob:
    #fix remove
    "This option is currently unavailable. It will be added in a later update."
    return
    #fix remove

    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(character)
    if character.Foot >= 7: # She loves it
        $ temp_modifier += 10
    elif character.Foot >= 3: #You've done it before several times
        $ temp_modifier += 7
    elif character.Foot: #You've done it before
        $ temp_modifier += 3

    if character.Addict >= 75 and character.Swallow >=3: #She's really strung out and has swallowed
        $ temp_modifier += 10
    if character.Addict >= 75:
        $ temp_modifier += 5

    if Situation == "shift":
        $ temp_modifier += 15
    if "exhibitionist" in character.Traits:
        $ temp_modifier += (3*Taboo)
    if character in Player.Harem or "sex friend" in character.Petnames:
        $ temp_modifier += 10
    elif "ex" in character.Traits:
        $ temp_modifier -= 40
    if character.ForcedCount and not character.Forced:
        $ temp_modifier -= 5 * character.ForcedCount

    if Taboo and "tabno" in character.DailyActions:
        $ temp_modifier -= 10

    if "no foot" in character.DailyActions:
        $ temp_modifier -= 5
        $ temp_modifier -= 10 if "no foot" in character.RecentActions else 0

    $ Approval = ApprovalCheck(character, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)

    if Situation == character:                                                                  #Jubes auto-starts
        if Approval > 2:                                                      # fix, add jubes auto stuff here
            "[character.Name] leans back  and starts rubbing your cock with her foot."
            menu:
                "What do you do?"
                "Nothing.":
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 30, 2)
                    "[character.Name] continues her actions."
                "Praise her.":
                    $ character.FaceChange("sexy", 1)
                    $ character.Statup("Inbt", 70, 3)
                    ch_p "Oooh, that's good, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] continues her actions."
                    $ character.Statup("Love", 80, 1)
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 2)
                "Ask her to stop.":
                    $ character.FaceChange("surprised")
                    $ character.Statup("Inbt", 70, 1)
                    ch_p "Let's not do that for now, [character.Pet]."
                    $ character.NameCheck() #checks reaction to petname
                    "[character.Name] puts it down."
                    $ character.Statup("Obed", 90, 1)
                    $ character.Statup("Obed", 50, 1)
                    $ character.Statup("Obed", 30, 2)
                    return
            if Trigger:
                $ Trigger3 = "foot"
                return
            jump Jubes_FJ_Prep
        else:
            $ temp_modifier = 0                               # fix, add jubes auto stuff here
            $ Trigger2 = 0
            return

    if not character.Foot and "no foot" not in character.RecentActions:
        $ character.FaceChange("confused", 2)
        ch_v "Standard footjob?"
        $ character.Blush = 1

    if not character.Foot and Approval:                                                 #First time dialog
        if character.Forced:
            $ character.FaceChange("sad",1)
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
        elif character.Love >= (character.Obed + character.Inbt):
            $ character.FaceChange("sexy",1)
            $ character.Brows = "sad"
            $ character.Mouth = "smile"
            ch_v "I guess it couldn't hurt. . ."
        elif character.Obed >= character.Inbt:
            $ character.FaceChange("normal",1)
            ch_v "If you want, [character.Petname]. . ."
        elif character.Addict >= 50:
            $ character.FaceChange("manic", 1)
            ch_v "Okay. . ."
        else: # Uninhibited
            $ character.FaceChange("lipbite",1)
            ch_v "Sure. . ."

    elif Approval:                                                                       #Second time+ dialog
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Love", 70, -3, 1)
            $ character.Statup("Love", 20, -2, 1)
            ch_v "That's it?"
        elif not Taboo and "tabno" in character.DailyActions:
            ch_v "Um, I guess this is secure enough. . ."
        elif "foot" in character.DailyActions:
            $ character.FaceChange("sexy", 1)
            ch_v "More of that, huh. . ."
            jump Jubes_FJ_Prep
#        elif "foot" in character.DailyActions:
#            $ character.FaceChange("sexy", 1)
#            $ Line = renpy.random.choice(["Another one?",
#                "Didn't get enough earlier?",
#                "My feet are kinda sore from earlier.",
#                "My feet are kinda sore from earlier."])
#            ch_v "[Line]"
        elif character.Foot < 3:
            $ character.FaceChange("sexy", 1)
            $ character.Brows = "confused"
            $ character.Mouth = "kiss"
            ch_v "Hmm, magic toes. . ."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.ArmPose = 2
            $ Line = renpy.random.choice(["You want me to use my feet?",
                "So you'd like another footjob?",
                "A little. . . [she rubs her foot along your leg]?",
                "A little TLC?"])
            ch_v "[Line]"
        $ Line = 0

    if Approval >= 2:                                                                   #She's into it. . .
        if character.Forced:
            $ character.FaceChange("sad")
            $ character.Statup("Obed", 90, 1)
            $ character.Statup("Inbt", 60, 1)
            ch_v "Ok, sure."
        elif "no foot" in character.DailyActions:
            ch_v "Fine."
        else:
            $ character.FaceChange("sexy", 1)
            $ character.Statup("Love", 90, 1)
            $ character.Statup("Inbt", 50, 3)
            $ Line = renpy.random.choice(["Sure, I guess.",
                "OK.",
                "Fine, lemme see it.",
                "I guess I could. . .",
                "Ok. . . [She gestures for you to come over].",
                "Heh, ok, ok."])
            ch_v "[Line]"
            $ Line = 0
        $ character.Statup("Obed", 20, 1)
        $ character.Statup("Obed", 60, 1)
        $ character.Statup("Inbt", 70, 2)
        jump Jubes_FJ_Prep

    else:                                                                               #She's not into it, but maybe. . .
        $ character.FaceChange("angry")
        if "no foot" in character.RecentActions:
            ch_v "You should listen better, [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions and "no foot" in character.DailyActions:
            ch_v "I said not in public."
        elif "no foot" in character.DailyActions:
            ch_v "I told you \"no,\" [character.Petname]."
        elif Taboo and "tabno" in character.DailyActions:
            ch_v "I said not in public!"
        elif not character.Foot:
            $ character.FaceChange("bemused")
            ch_v "Eh, [character.Petname]. . ."
        else:
            $ character.FaceChange("bemused")
            ch_v "Not now, ok?"
        menu:
            extend ""
            "Sorry, never mind." if "no foot" in character.DailyActions:
                $ character.FaceChange("bemused")
                ch_v "Sure, no problem."
                return
            "Maybe later?" if "no foot" not in character.DailyActions:
                $ character.FaceChange("sexy")
                ch_v ". . ."
                ch_v "Maybe."
                $ character.Statup("Love", 80, 2)
                $ character.Statup("Inbt", 70, 2)
                if Taboo:
                    $ character.RecentActions.append("tabno")
                    $ character.DailyActions.append("tabno")
                $ character.RecentActions.append("no foot")
                $ character.DailyActions.append("no foot")
                return
            "I'd really appreciate it. . .":
                if Approval:
                    $ character.FaceChange("sexy")
                    $ character.Statup("Obed", 90, 2)
                    $ character.Statup("Obed", 50, 2)
                    $ character.Statup("Inbt", 70, 3)
                    $ character.Statup("Inbt", 40, 2)
                    $ Line = renpy.random.choice(["Sure, I guess.",
                        "OK.",
                        "Fine, lemme see it.",
                        "I guess I could. . .",
                        "Ok. . . [She gestures for you to come over].",
                        "Heh, ok, ok."])
                    ch_v "[Line]"
                    $ Line = 0
                    jump Jubes_FJ_Prep
                else:
                    pass

            "Come on, get to work.":                                               # Pressured into it
                $ Approval = ApprovalCheck(character, 400, "OI", TabM = 3) # 35, 50, 65, -120(155)
                if Approval > 1 or (Approval and character.Forced):
                    $ character.FaceChange("sad")
                    $ character.Statup("Love", 70, -5, 1)
                    $ character.Statup("Love", 200, -2)
                    ch_v
                    $ character.Statup("Obed", 50, 4)
                    $ character.Statup("Inbt", 80, 1)
                    $ character.Statup("Inbt", 60, 3)
                    $ character.Forced = 1
                    jump Jubes_FJ_Prep
                else:
                    $ character.Statup("Love", 200, -15)
                    $ character.RecentActions.append("angry")
                    $ character.DailyActions.append("angry")

    #She refused all offers.
    $ character.ArmPose = 1
    if "no foot" in character.DailyActions:
        $ character.FaceChange("angry", 1)

        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif character.Forced:
        $ character.FaceChange("angry", 1)
        ch_v "You understand that I have claws down there too. . ."
        $ character.Statup("Lust", 200, 5)
        if character.Love > 300:
                $ character.Statup("Love", 70, -2)
        $ character.Statup("Obed", 50, -2)
        $ character.RecentActions.append("angry")
        $ character.DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        $ character.FaceChange("angry", 1)
        $ character.DailyActions.append("tabno")
        ch_v "This is too exposed."
        $ character.Statup("Lust", 200, 5)
        $ character.Statup("Obed", 50, -3)
    elif character.Foot:
        $ character.FaceChange("sad")
        ch_v "Not right now."
    else:
        $ character.FaceChange("normal", 1)
        ch_v "I'd rather not."
    $ character.RecentActions.append("no foot")
    $ character.DailyActions.append("no foot")
    $ temp_modifier = 0
    return


label Jubes_FJ_Prep:
    if Trigger2 == "foot":
        return

    if Taboo:
        $ character.Inbt += int(Taboo/10)
        $ character.Lust += int(Taboo/5)

    $ character.FaceChange("sexy")
    if character.Forced:
        $ character.FaceChange("sad")
    elif not character.Foot:
        $ character.Brows = "confused"
        $ character.Eyes = "sexy"
        $ character.Mouth = "smile"

    call Seen_First_Peen(character,Partner)

    if not character.Foot:
        if character.Forced:
            $ character.Statup("Love", 90, -20)
            $ character.Statup("Obed", 70, 25)
            $ character.Statup("Inbt", 80, 30)
        else:
            $ character.Statup("Love", 90, 5)
            $ character.Statup("Obed", 70, 20)
            $ character.Statup("Inbt", 80, 20)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    if Taboo:
        $ character.DrainWord("tabno")
    $ character.DrainWord("no foot")
    $ character.RecentActions.append("foot")
    $ character.DailyActions.append("foot")

label Jubes_FJ_Cycle:
    while Round > 0:
        call Shift_Focus(character)
        call Jubes_Sex_Launch("foot")
        $ character.LustFace()

        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1

                        "Speed up. . ." if Speed < 2:
                                    $ Speed += 1
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
                                    $ character.Pose = "doggy" if character.Pose != "doggy" else "sex"
                                    "You turn her around. . ."
                                    jump Jubes_FJ_Cycle

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if character.Action and MultiAction:
                                                call Offhand_Set
                                                if Trigger2:
                                                     $ character.Action -= 1
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

                                    "Shift primary action":
                                            if character.Action and MultiAction:
                                                    menu:
                                                        "How about a blowjob?":
                                                                    if character.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_FJ_After
                                                                        call Jubes_Blowjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(character,"tired")
                                                        "How about a handjob?":
                                                                    if character.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_FJ_After
                                                                        call Jubes_Handjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(character,"tired")

                                                        "How about a titjob?":
                                                                    if character.Action and MultiAction:
                                                                        $ Situation = "shift"
                                                                        call Jubes_FJ_After
                                                                        call Jubes_Titjob
                                                                    else:
                                                                        call Sex_Basic_Dialog(character,"tired")



                                                        "Never Mind":
                                                                jump Jubes_FJ_Cycle
                                            else:
                                                call Sex_Basic_Dialog(character,"tired")

        #End menu (if Line)

        call Shift_Focus(character)
        call Sex_Dialog(character,Partner)

        #If either of you could cum

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or character.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(character)
                            if "angry" in character.RecentActions:
                                call Jubes_Sex_Reset
                                return
                            $ character.Statup("Lust", 200, 5)
                            if 100 > character.Lust >= 70 and character.OCount < 2:
                                $ character.RecentActions.append("unsatisfied")
                                $ character.DailyActions.append("unsatisfied")

                            if Player.Focus > 80:
                                jump Jubes_FJ_After
                            $ Line = "came"

                    if character.Lust >= 100:
                            #If Jubes can cum
                            call Girl_Cumming(character)
                            if Situation == "shift" or "angry" in character.RecentActions:
                                jump Jubes_FJ_After

                    if Line == "came": #ex Player.Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not Player.Semen:
                                "You're emptied out, you should probably take a break."


                            if "unsatisfied" in character.RecentActions:#And Jubes is unsatisfied,
                                "[character.Name] still seems a bit unsatisfied with the experience."
                                menu:
                                    "Finish her?"
                                    "Yes, keep going for a bit.":
                                        $ Line = "You get back into it"
                                    "No, I'm done.":
                                        "You pull back."
                                        jump Jubes_FJ_After
        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if Cnt == 20:
                    $ character.Brows = "angry"
                    menu:
                        ch_v "Hmm, this is getting a bit boring."
                        "How about a BJ?" if character.Action and MultiAction:
                                $ Situation = "shift"
                                call Jubes_FJ_After
                                call Jubes_Blowjob
                        "How about a Handy?" if character.Action and MultiAction:
                                $ Situation = "shift"
                                call Jubes_FJ_After
                                call Jubes_Handjob
                        "Finish up." if Player.FocusX:
                                "You release your concentration. . ."
                                $ Player.FocusX = 0
                                $ Player.Focus += 15
                                $ Cnt += 1
                                "[Line]"
                                jump Jubes_FJ_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Jubes_Sex_Reset
                                $ Situation = "shift"
                                jump Jubes_FJ_After
                        "No, get back down there.":
                                if ApprovalCheck(character, 1200) or ApprovalCheck(character, 500, "O"):
                                    $ character.Statup("Love", 200, -5)
                                    $ character.Statup("Obed", 50, 3)
                                    $ character.Statup("Obed", 80, 2)
                                    "She grumbles but gets back to work."
                                else:
                                    $ character.FaceChange("angry", 1)
                                    "She scowls at you and pulls back."
                                    ch_v "Not interested."
                                    $ character.Statup("Love", 50, -3, 1)
                                    $ character.Statup("Love", 80, -4, 1)
                                    $ character.Statup("Obed", 30, -1, 1)
                                    $ character.Statup("Obed", 50, -1, 1)
                                    $ character.RecentActions.append("angry")
                                    $ character.DailyActions.append("angry")
                                    jump Jubes_FJ_After
        elif Cnt == 10 and character.SEXP <= 100 and not ApprovalCheck(character, 1200, "LO"):
                    $ character.Brows = "confused"
                    ch_v "Ok, seriously, let's try something different."
        #End Count check

        call Escalation(character) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(character,10) #"I could use a break soon. . ."
        elif Round == 5:
                call Sex_Basic_Dialog(character,5)   #". . . I could really use a break here. . ."

    #Round = 0 loop breaks
    $ character.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(character,"done") # ch_s "Ok, that's it, I need a break."

label Jubes_FJ_After:
    $ character.FaceChange("sexy")

    $ character.Foot += 1
    $ character.Action -=1
    $ character.Addictionrate += 1
    if "addictive" in Player.Traits:
        $ character.Addictionrate += 1
    $ character.Statup("Lust", 90, 5)

    call Partner_Like(character,1)

    if "Jubespedi" in Achievements:
            pass
    elif character.Foot >= 10:
            $ character.FaceChange("smile", 1)
            ch_v "I think I'm finally back into practice on this."
            $ Achievements.append("Jubespedi")
            $ character.SEXP += 5
    elif character.Foot == 1:
            $ character.SEXP += 10
            if character.Love >= 500:
                $ character.Mouth = "smile"
                ch_v "Did you like that? . ."
            elif Player.Focus <= 20:
                $ character.Mouth = "sad"
                ch_v "Did that do it for you?"
    elif character.Foot == 5:
                ch_v "I'm getting used to this. . ."

    $ temp_modifier = 0
    if Situation == "shift":
        ch_v "Ok, so what did you have in mind?"
    else:
        call Jubes_Sex_Reset
    call Checkout
    return

## end character.Footjob //////////////////////////////////////////////////////////////////////
