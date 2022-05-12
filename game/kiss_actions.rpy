label Makeout(Girl = 0):
    if Girl not in TotalGirls:
        return
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus(Girl)

    $ Approval = ApprovalCheck(Girl, 700, TabM=1,Alt=[[RogueX,JeanX],500]) #reduced check for Rogue

    if Girl == EmmaX and not ApprovalCheck(Girl, 1000):
        $ Girl.FaceChange("sadside")
        ch_e "Not when we barely know each other. . ."
        $ Girl.RecentActions.append("no kissing")
        $ Girl.DailyActions.append("no kissing")
        return
    if Approval > 1 and not Girl.Kissed and not Girl.Forced:
            #first time and she's into it
            $ Girl.FaceChange("sexy")
            $ Girl.Eyes = "side"
            if Girl == RogueX:
                    ch_r "I've never really been able to do this, so I'm a bit excited to try. . ."
            elif Girl == KittyX:
                    ch_k "You are kinda cute. . ."
            elif Girl == EmmaX:
                    ch_e "Well, I suppose it couldn't hurt. . ."
            elif Girl == LauraX:
                    ch_l "Worth a shot. . ."
            elif Girl == JeanX:
                    ch_j "Why not?"
            elif Girl == StormX:
                    ch_s "I would like that."
            elif Girl == JubesX:
                    ch_v "I guess we did get off to a poor start. . ."
    elif Approval and not Girl.Kissed:
            #first time, lower enthusiasm
            $ Girl.FaceChange("sexy")
            $ Girl.Eyes = "side"
            if Girl == RogueX:
                    ch_r "I guess it's worth a shot. . ."
            elif Girl == KittyX:
                    ch_k "I'll give it a go. . ."
            elif Girl == EmmaX:
                    ch_e "We could. . ."
            elif Girl == LauraX:
                    ch_l "If you insist. . ."
            elif Girl == JeanX:
                    ch_j "I mean, whatever. . ."
            elif Girl == StormX:
                    ch_s "I suppose."
            elif Girl == JubesX:
                    ch_v "I suppose we could. . ."
    elif Approval and "kissing" in Girl.RecentActions:
            # you were just kissing earlier
            $ Girl.FaceChange("sexy", 1)
            if Girl == KittyX:
                    ch_k "Prrr. . ."
            else:
                    call AnyLine(Girl,"Mmmm. . .")
            jump KissPrep
    elif Approval and "kissing" in Girl.DailyActions:
            #you'd been kissing earlier in the day
            $ Girl.FaceChange("sexy", 1)

            $ Line = renpy.random.choice(["A","B","C"])
            if Line == "A":
                call AnyLine(Girl,"Didn't get enough earlier?")
            elif Girl == RogueX:
                if Line == "B":
                        ch_r "{i}I'm{/i} used to being the one sucking people dry. . ."
                else:
                        ch_r "Gimme some sugar, sugar."
            elif Girl == KittyX:
                if Line == "B":
                        ch_k "Meow."
                else:
                        ch_k "Come'ere tasty."
            elif Girl == EmmaX:
                if Line == "B":
                        ch_e "Mmmm. . ."
                else:
                        ch_e "Come and get it."
            elif Girl == LauraX:
                if Line == "B":
                        ch_l "Mmmmmm."
                else:
                        ch_l "Get over here."
            elif Girl == JeanX:
                if Line == "B":
                        ch_j "MmMmmm. . ."
                else:
                        ch_j "Oh, get over here."
            elif Girl == StormX:
                if Line == "B":
                        ch_s "Mmmm. . ."
                else:
                        ch_s "Yes, let's."
            elif Girl == JubesX:
                if Line == "B":
                        ch_v "Mmmm. . ."
                else:
                        ch_v "Sure, come to me."
            $ Line = 0
    elif Approval > 1 and Girl.Love > Girl.Obed:
            # love is higher than obedience
            $ Girl.FaceChange("sexy")
            if Girl == RogueX:
                    ch_r "Sure, why not?"
            elif Girl == KittyX:
                    ch_k "Smooches!"
            elif Girl == EmmaX:
                    ch_e "Mwa."
            elif Girl == LauraX:
                    ch_l "Mmmmm. . ."
            elif Girl == JeanX:
                    ch_j "MmMmmmm. . ."
            elif Girl == StormX:
                    ch_s "Hrm. . ."
            elif Girl == JubesX:
                    ch_v "Mmmm. . ."
    elif ApprovalCheck(Girl, 500, "O") and Girl.Obed > Girl.Love:
            # if Obedience is higher
            $ Girl.FaceChange("normal")
            if Girl == RogueX:
                    ch_r "If you wish."
            elif Girl == KittyX:
                    ch_k "Sure, ok."
            elif Girl == EmmaX:
                    ch_e "Of course."
            elif Girl == LauraX:
                    ch_l "If you want."
            elif Girl == JeanX:
                    ch_j "Ok. . ."
            elif Girl == StormX:
                    ch_s "Very well. . ."
            elif Girl == JubesX:
                    ch_v "sure. . ."
            $ Girl.Statup("Obed", 60, 1)
    elif ApprovalCheck(Girl, 250, "O",Alt=[[KittyX,LauraX],300]) and ApprovalCheck(Girl, 250, "L",Alt=[[KittyX,LauraX],200]):
            #if not that into it
            $ Girl.FaceChange("bemused")
            call AnyLine(Girl,"Ok, fine.")
            $ Girl.Statup("Obed", 50, 3)
    elif Girl.Addict >= 50:
            #high addiction
            $ Girl.FaceChange("sexy")
            $ Girl.Eyes = "manic"
            if Girl == RogueX:
                    ch_r "Hm. . . ok, let's do this."
            elif Girl == KittyX:
                    ch_k "I kinda have to."
            elif Girl == EmmaX:
                    ch_e ". . . yes."
            elif Girl == LauraX:
                    ch_l "I have to."
            elif Girl == JeanX:
                    ch_j "Um. . . yeah. . ."
            elif Girl == StormX:
                    ch_s ". . . yes. . ."
            elif Girl == JubesX:
                    ch_v "Oh yes. . ."
    elif Approval:
            #she's barely into it
            $ Girl.FaceChange("bemused")
            if Girl == RogueX:
                    ch_r "hmm, ok."
            elif Girl == KittyX:
                    ch_k "Yeah, whatever."
            elif Girl == EmmaX:
                    ch_e "Very well."
            elif Girl == LauraX:
                    ch_l "Sure."
            elif Girl == JeanX:
                    ch_j "Whatever. . ."
            elif Girl == StormX:
                    ch_s "Fine."
            elif Girl == JubesX:
                    ch_v "Sure, ok. . ."
    else:
            #she's out
            $ Girl.FaceChange("normal") # Else
            $ Girl.Mouth = "sad"
            if Girl == RogueX:
                    ch_r "Nah, I don't think I'm interested."
            elif Girl == KittyX:
                    ch_k "Nope."
            elif Girl == EmmaX:
                    ch_e "Hmmm, no."
            elif Girl == LauraX:
                    ch_l "No."
            elif Girl == JeanX:
                    ch_j "You wish. . ."
            elif Girl == StormX:
                    ch_s "I do not think so."
            elif Girl == JubesX:
                    ch_v "No thanks. . ."
            $ Girl.RecentActions.append("no kissing")
            $ Girl.DailyActions.append("no kissing")
            return

label KissPrep(Girl=Ch_Focus):
    $ Girl = GirlCheck(Girl)

    $ Girl.Statup("Inbt", 10, 1)
    $ Girl.Statup("Inbt", 20, 1)

    call kissing_launch(Girl, "kiss you")

    if Girl.Kissed >= 10 and Girl.Inbt >= 300:
            $ Girl.FaceChange("sucking")
    elif Girl.Kissed > 1 and Girl.Addict >= 50:
            $ Girl.FaceChange("sucking")
    else:
            $ Girl.FaceChange("kiss",2)
    if Taboo:
            $ Girl.DrainWord("tabno")
    $ Girl.DrainWord("no kissing")

    if Girl == RogueX and not Girl.Kissed:
            #If it's Rogue's first time, it's only a simple kiss and then ends
            "You lean in and your lips meet [Girl.Name]'s."
            $ Girl.Eyes = "surprised"
            $ Girl.Statup("Love", 90, 15)
            $ Girl.Statup("Love", 60, 30)
            "A slight spark passes between you and her eyes widen with surprise."
            $ Girl.Statup("Lust", 70, 5)
            ch_r "Wow, [Girl.Petname], that was really something. . ."
            $ Girl.FaceChange("bemused",1)
            ch_r "Not the kind of zap I'm used to."
            $ Girl.Addict -= 5
            $ Girl.Statup("Obed", 30, 20)
            $ Girl.Statup("Inbt", 30, 30)
            jump Kiss_After

    if Situation == Girl:
            #Girl auto-starts
            $ Situation = 0
            "[Girl.Name] presses her body against yours, and kisses you deeply."
            menu:
                "What do you do?"
                "Go with it.":
                        $ Girl.Statup("Inbt", 80, 3)
                        $ Girl.Statup("Inbt", 50, 2)
                        "You lean in to the kiss."
                "Praise her.":
                        $ Girl.FaceChange("sexy", 1)
                        $ Girl.Statup("Inbt", 80, 3)
                        ch_p "Mmm, this is a nice surprise, [Girl.Pet]."
                        $ Girl.NameCheck() #checks reaction to petname
                        "You lean in to the kiss."
                        $ Girl.Statup("Love", 85, 1)
                        $ Girl.Statup("Obed", 90, 1)
                        $ Girl.Statup("Obed", 50, 2)
                "Ask her to stop.":
                        "You pull back."
                        $ Girl.FaceChange("surprised")
                        $ Girl.Statup("Inbt", 70, 1)
                        ch_p "Let's not do that right now, [Girl.Pet]."
                        $ Girl.NameCheck() #checks reaction to petname
                        $ Girl.Statup("Obed", 90, 1)
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Obed", 30, 2)
                        $ Player.RecentActions.append("nope")
                        $ Girl.AddWord(1,"refused","refused")
                        return
            #end auto

    if Girl.Kissed >= 10 and Girl.Lust >= 80:
            $ Line = renpy.random.choice(["She's all over you, running her hands along your body.",
                    "She's all over you, licking all over your face and neck.",
                    "She's all over you, kissing all over your face and grinding against you."])
    elif Girl.Kissed > 7:
            $ Line = renpy.random.choice(["She's really sucking face.",
                    "You kiss deeply and passionately.",
                    "You kiss deeply and passionately.",
                    "You kiss deeply and passionately."])
    elif Girl.Kissed > 3:
            $ Line = renpy.random.choice(["She's really getting into it.",
                    "She's really getting into it, her tongue's going at it.",
                    "She's really getting into it, there's some heavy tongue action."])
    else:
            $ Line = "You and "+ Girl.Name +" make out for a while."
    "[Line]"
    $ Cnt = 0
    $ Trigger = "kiss you"
    $ Line = 0
    if Situation:
        $ renpy.pop_call()
        $ Situation = 0

label KissCycle(Girl=0):
    $ Girl = GirlCheck(Girl)

    while Round > 0:
        call Shift_Focus(Girl)
        call kissing_launch(Girl, "kiss you")
        $ Girl.LustFace()
        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0
        if  Player.Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . .":
                                    pass

                        "Slap her ass":
                                    call Slap_Ass(Girl)
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump KissCycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                                    pass
                        "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ Player.FocusX = 1
                        "Release your focus." if Player.FocusX:
                                    "You release your concentration. . ."
                                    $ Player.FocusX = 0

                        "Start jack'in it." if MultiAction and Trigger2 != "jackin":
                                    call Jackin(Girl)
                        "Stop jack'in it." if MultiAction and Trigger2 == "jackin":
                                    "You stop jack'in it."
                                    $ Trigger2 = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if Girl.Action and MultiAction:
                                                    call Offhand_Set
                                                    if Trigger2:
                                                         $ Girl.Action -= 1
                                            else:
                                                    call tired_dialog(Girl)
                                                    #"I'm actually getting a little tired, so maybe we could wrap this up?"

                                    "Shift primary action":
                                            if Girl.Action and MultiAction:
                                                    menu:
                                                        "Move a hand to her breasts. . ." if Girl.Kissed >= 1 and MultiAction:
                                                                if Girl.Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call Kiss_After
                                                                    call fondle_breasts(Girl)
                                                                    if Trigger == "fondle breasts":
                                                                        $ Trigger2 = "kiss you"
                                                                        call fondle_breasts_prep(Girl)
                                                                    else:
                                                                        $ Trigger = "kiss you"
                                                                else:
                                                                    "As your hands creep upwards, she grabs your wrists."
                                                                    call tired_dialog(Girl)
                                                                    #"I'm actually getting a little tired, so maybe we could wrap this up?"
                                                        "Move a hand to her thighs. . ." if Girl.Kissed >= 1 and MultiAction:
                                                                if Girl.Action and MultiAction:
                                                                    $ Situation = "auto"
                                                                    call Kiss_After
                                                                    call fondle_thighs(Girl)
                                                                    if Trigger == "fondle thighs":
                                                                            $ Trigger2 = "kiss you"
                                                                            call fondle_thighs_prep(Girl)
                                                                    else:
                                                                            $ Trigger = "kiss you"
                                                                else:
                                                                    "As your hands creep downwards, she grabs your wrists."
                                                                    call tired_dialog(Girl)
                                                                    #"I'm actually getting a little tired, so maybe we could wrap this up?"
                                                        "Never Mind":
                                                                    jump KissCycle
                                            else:
                                                                    call tired_dialog(Girl)
                                                                    #"I'm actually getting a little tired, so maybe we could wrap this up?"
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask [Girl.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                                        call Les_Change(Girl)

                                            "Ask [Girl.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner.Name] to do something else":
                                                        call Three_Change(Girl)

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner.Name]":
                                                        call Trigger_Swap(Girl)
                                            "Undress [Partner.Name]":
                                                        call Girl_Undress(Partner)
                                                        call Shift_Focus(Partner)
                                                        jump KissCycle
                                            "Clean up Partner":
                                                        call Girl_Cleanup(Partner,"ask")
                                                        #call Shift_Focus(Partner)
                                                        jump KissCycle
                                            "Never mind":
                                                        jump KissCycle
                                    "Undress [Girl.Name]":
                                            call Girl_Undress(Girl)
                                    "Clean up [Girl.Name] (locked)" if not Girl.Spunk:
                                            pass
                                    "Clean up [Girl.Name]" if Girl.Spunk:
                                            call Girl_Cleanup(Girl,"ask")
                                    "Never mind":
                                            jump KissCycle

                        "Back to Sex Menu" if MultiAction and Girl.Kissed >= 5:
                                ch_p "Let's try something else."

                                $ Situation = "shift"
                                $ Line = 0

                                jump Kiss_After
                        "End Scene":
                                ch_p "Let's stop for now."
                                $ Line = 0
                                jump Kiss_After
        #End menu (if Line)

        call Shift_Focus(Girl)
        call Sex_Dialog(Girl,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up
        if Player.Focus >= 100 or Girl.Lust >= 100:
                    #If either of you could cum
                    if Player.Focus >= 100:
                            #If you can cum:
                            call Player_Cumming(Girl)
                            if "angry" in Girl.RecentActions:
                                    call reset_position(Girl)
                                    return
                            $ Girl.Statup("Lust", 200, 5)
                            if 100 > Girl.Lust >= 70 and Girl.OCount < 2 and Girl.SEXP >= 20:
                                    $ Girl.RecentActions.append("unsatisfied")
                                    $ Girl.DailyActions.append("unsatisfied")
                            if Player.Focus > 80:
                                    jump Kiss_After
                            $ Line = "came"

                    if Girl.Lust >= 100:
                            #If you're still going at it and Rogue can cum
                            call Girl_Cumming(Girl)
                            if Situation == "shift" or "angry" in Girl.RecentActions:
                                    jump Kiss_After

                    #If you came
                    if Line == "came":
                                    if not Player.Semen:
                                            "You're pretty wiped, better stop for now."
                                    $ Line = 0
                                    jump Kiss_After

        if Partner and Partner.Lust >= 100:
                #Checks if partner could orgasm
                call Girl_Cumming(Partner)
        #End orgasm

        call Escalation(Girl) #sees if she wants to escalate things

        if Round == 10:
                call Sex_Basic_Dialog(Girl,10) #"You might want to wrap this up, it's getting late."
        elif Round == 5:
                call Sex_Basic_Dialog(Girl,5)   #"Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    $ Girl.FaceChange("bemused", 0)
    $ Line = 0
    call Sex_Basic_Dialog(Girl,"done") #"Ok, [Girl.Petname], that's enough of that for now."

label Kiss_After:
    $ Girl = GirlCheck(Girl)
    $ Girl.FaceChange("sexy")

    $ Girl.Kissed += 1
    $ Girl.Action -= 1
    $ Girl.Addictionrate += 2 if Girl.Addictionrate < 5 else 1
    $ Girl.Addictionrate += 1 if "addictive" in Player.Traits else 0

    call Partner_Like(Girl, 1) #raises other girl's like levels if watching

    if "kissing" not in Girl.RecentActions:
        if Girl.Love > 300:
            $ Girl.Statup("Love", 60, 4)
        $ Girl.Statup("Love", 70, 1)
        $ Girl.RecentActions.append("kissing")
        $ Girl.DailyActions.append("kissing")

    if Girl.Kissed > 10:
        pass
    elif Girl.Kissed == 10:
        $ Girl.FaceChange("smile", 1)
        if Girl == RogueX:
            ch_r "You must really like my lips, huh?"
        elif Girl == KittyX:
            ch_k "I could eat you up."
        elif Girl == EmmaX:
            ch_e "This has been a pleasant surprise."
        elif Girl == LauraX:
            ch_l "I could do this every day."
        elif Girl == JeanX:
            ch_j "You've made some serious improvement. . ."
            ch_j "I must be rubbing off on you. . ."
        elif Girl == StormX:
            ch_s "I have grown to enjoy this quite a bit."
        elif Girl == JubesX:
            ch_v "I love the taste of your lips. . ."
    elif Girl.Kissed == 5:
        if Girl == RogueX:
            ch_r "We're really making this a regular thing."
        elif Girl == KittyX:
            ch_k "You're good at this. . ."
        elif Girl == EmmaX:
            ch_e "You're surprisingly talented. . ."
        elif Girl == LauraX:
            ch_l "You're really talented. . ."
        elif Girl == JeanX:
            ch_j "MmMmmm, that was nice. . ."
        elif Girl == StormX:
            ch_s "Mmmm, has anyone told you that you are quite good at this?"
        elif Girl == JubesX:
            ch_v "Kissing you really feels great!"
    elif Girl.Kissed == 1:
        if Girl == JubesX:
            "[Girl.Name] bites your lip as she pulls back, and licks some blood off her lips."
            ch_v "Sorry about that. . ."
            ch_v "Won't happen again."
        $ Girl.SEXP += 1

    if not Situation and Girl.Kissed > 5 and Girl.Lust > 50 and ApprovalCheck(Girl, 950):
        $ Girl.FaceChange("sexy", 1)
        $ Girl.Brows = "sad"
        if Girl == RogueX:
            ch_r "You maybe want to try something more?"
        elif Girl == KittyX:
            ch_k "Is that it?"
        elif Girl == EmmaX:
            ch_e "You wouldn't be interested in something more? . ."
        elif Girl == LauraX:
            ch_l "Huh, that's all there is to it?"
        elif Girl == JeanX:
            ch_j "That was nice. . ."
        elif Girl == StormX:
            ch_s "Oh. . . that was lovely."
        elif Girl == JubesX:
            ch_v "Did you want. . . more?"

    $ temp_modifier = 0

    if Situation:
        call Sex_Basic_Dialog(Girl, "switch")
    else:
        call reset_position(Girl)

    call Checkout

    return
