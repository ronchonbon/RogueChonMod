label kiss(character):
    $ Player.primary_action = "kiss"

    $ Round -= 5 if Round > 5 else (Round-1)

    call Shift_Focus(character)

    $ Approval = ApprovalCheck(character, 700, TabM=1,Alt=[[RogueX,JeanX],500]) #reduced check for Rogue

    if character == EmmaX and not ApprovalCheck(character, 1000):
        $ character.FaceChange("sadside")

        ch_e "Not when we barely know each other. . ."

        $ character.RecentActions.append("no kissing")
        $ character.DailyActions.append("no kissing")
        return
    if Approval > 1 and not character.Kissed and not character.Forced:
        $ character.FaceChange("sexy")
        $ character.Eyes = "side"

        if character == RogueX:
            ch_r "I've never really been able to do this, so I'm a bit excited to try. . ."
        elif character == KittyX:
            ch_k "You are kinda cute. . ."
        elif character == EmmaX:
            ch_e "Well, I suppose it couldn't hurt. . ."
        elif character == LauraX:
            ch_l "Worth a shot. . ."
        elif character == JeanX:
            ch_j "Why not?"
        elif character == StormX:
            ch_s "I would like that."
        elif character == JubesX:
            ch_v "I guess we did get off to a poor start. . ."
    elif Approval and not character.Kissed:
        $ character.FaceChange("sexy")
        $ character.Eyes = "side"

        if character == RogueX:
            ch_r "I guess it's worth a shot. . ."
        elif character == KittyX:
            ch_k "I'll give it a go. . ."
        elif character == EmmaX:
            ch_e "We could. . ."
        elif character == LauraX:
            ch_l "If you insist. . ."
        elif character == JeanX:
            ch_j "I mean, whatever. . ."
        elif character == StormX:
            ch_s "I suppose."
        elif character == JubesX:
            ch_v "I suppose we could. . ."
    elif Approval and "kissing" in character.RecentActions:
        $ character.FaceChange("sexy", 1)

        if character == KittyX:
            ch_k "Prrr. . ."
        else:
            call AnyLine(character,"Mmmm. . .")

        jump before_kiss
    elif Approval and "kissing" in character.DailyActions:
        $ character.FaceChange("sexy", 1)

        $ Line = renpy.random.choice(["A","B","C"])
        if Line == "A":
            call AnyLine(character,"Didn't get enough earlier?")
        elif character == RogueX:
            if Line == "B":
                ch_r "{i}I'm{/i} used to being the one sucking people dry. . ."
            else:
                ch_r "Gimme some sugar, sugar."
        elif character == KittyX:
            if Line == "B":
                ch_k "Meow."
            else:
                ch_k "Come'ere tasty."
        elif character == EmmaX:
            if Line == "B":
                ch_e "Mmmm. . ."
            else:
                ch_e "Come and get it."
        elif character == LauraX:
            if Line == "B":
                ch_l "Mmmmmm."
            else:
                ch_l "Get over here."
        elif character == JeanX:
            if Line == "B":
                ch_j "MmMmmm. . ."
            else:
                ch_j "Oh, get over here."
        elif character == StormX:
            if Line == "B":
                ch_s "Mmmm. . ."
            else:
                ch_s "Yes, let's."
        elif character == JubesX:
            if Line == "B":
                ch_v "Mmmm. . ."
            else:
                ch_v "Sure, come to me."

        $ Line = 0
    elif Approval > 1 and character.Love > character.Obed:
        $ character.FaceChange("sexy")

        if character == RogueX:
            ch_r "Sure, why not?"
        elif character == KittyX:
            ch_k "Smooches!"
        elif character == EmmaX:
            ch_e "Mwa."
        elif character == LauraX:
            ch_l "Mmmmm. . ."
        elif character == JeanX:
            ch_j "MmMmmmm. . ."
        elif character == StormX:
            ch_s "Hrm. . ."
        elif character == JubesX:
            ch_v "Mmmm. . ."
    elif ApprovalCheck(character, 500, "O") and character.Obed > character.Love:
        $ character.FaceChange("normal")

        if character == RogueX:
            ch_r "If you wish."
        elif character == KittyX:
            ch_k "Sure, ok."
        elif character == EmmaX:
            ch_e "Of course."
        elif character == LauraX:
            ch_l "If you want."
        elif character == JeanX:
            ch_j "Ok. . ."
        elif character == StormX:
            ch_s "Very well. . ."
        elif character == JubesX:
            ch_v "Sure. . ."

        $ character.Statup("Obed", 60, 1)
    elif ApprovalCheck(character, 250, "O",Alt=[[KittyX,LauraX],300]) and ApprovalCheck(character, 250, "L",Alt=[[KittyX,LauraX],200]):
        $ character.FaceChange("bemused")

        call AnyLine(character,"Ok, fine.")

        $ character.Statup("Obed", 50, 3)
    elif character.Addict >= 50:
        $ character.FaceChange("sexy")
        $ character.Eyes = "manic"

        if character == RogueX:
            ch_r "Hm. . . ok, let's do this."
        elif character == KittyX:
            ch_k "I kinda have to."
        elif character == EmmaX:
            ch_e ". . . yes."
        elif character == LauraX:
            ch_l "I have to."
        elif character == JeanX:
            ch_j "Um. . . yeah. . ."
        elif character == StormX:
            ch_s ". . . yes. . ."
        elif character == JubesX:
            ch_v "Oh yes. . ."
    elif Approval:
        $ character.FaceChange("bemused")

        if character == RogueX:
            ch_r "hmm, ok."
        elif character == KittyX:
            ch_k "Yeah, whatever."
        elif character == EmmaX:
            ch_e "Very well."
        elif character == LauraX:
            ch_l "Sure."
        elif character == JeanX:
            ch_j "Whatever. . ."
        elif character == StormX:
            ch_s "Fine."
        elif character == JubesX:
            ch_v "Sure, ok. . ."
    else:
        $ character.FaceChange("normal") # Else
        $ character.Mouth = "sad"

        if character == RogueX:
            ch_r "Nah, I don't think I'm interested."
        elif character == KittyX:
            ch_k "Nope."
        elif character == EmmaX:
            ch_e "Hmmm, no."
        elif character == LauraX:
            ch_l "No."
        elif character == JeanX:
            ch_j "You wish. . ."
        elif character == StormX:
            ch_s "I do not think so."
        elif character == JubesX:
            ch_v "No thanks. . ."

        $ character.RecentActions.append("no kissing")
        $ character.DailyActions.append("no kissing")

        return

    jump before_kiss

label before_kiss:
    $ Player.focused_girl.Statup("Inbt", 10, 1)
    $ Player.focused_girl.Statup("Inbt", 20, 1)

    call kissing_launch(Player.focused_girl, "kiss_you")

    if Player.focused_girl.Kissed >= 10 and Player.focused_girl.Inbt >= 300:
        $ Player.focused_girl.FaceChange("sucking")
    elif Player.focused_girl.Kissed > 1 and Player.focused_girl.Addict >= 50:
        $ Player.focused_girl.FaceChange("sucking")
    else:
        $ Player.focused_girl.FaceChange("kiss",2)

    if Taboo:
        $ Player.focused_girl.DrainWord("tabno")

    $ Player.focused_girl.DrainWord("no kissing")

    if Player.focused_girl == RogueX and not Player.focused_girl.Kissed:
        "You lean in and your lips meet [Player.focused_girl.Name]'s."

        $ Player.focused_girl.Eyes = "surprised"
        $ Player.focused_girl.Statup("Love", 90, 15)
        $ Player.focused_girl.Statup("Love", 60, 30)

        "A slight spark passes between you and her eyes widen with surprise."

        $ Player.focused_girl.Statup("Lust", 70, 5)

        ch_r "Wow, [Player.focused_girl.Petname], that was really something. . ."

        $ Player.focused_girl.FaceChange("bemused",1)

        ch_r "Not the kind of zap I'm used to."

        $ Player.focused_girl.Addict -= 5
        $ Player.focused_girl.Statup("Obed", 30, 20)
        $ Player.focused_girl.Statup("Inbt", 30, 30)

        jump after_kiss

    if Situation == Player.focused_girl:
        $ Situation = 0

        "[Player.focused_girl.Name] presses her body against yours, and kisses you deeply."
        menu:
            "What do you do?"
            "Go with it.":
                    $ Player.focused_girl.Statup("Inbt", 80, 3)
                    $ Player.focused_girl.Statup("Inbt", 50, 2)

                    "You lean in to the kiss."
            "Praise her.":
                    $ Player.focused_girl.FaceChange("sexy", 1)
                    $ Player.focused_girl.Statup("Inbt", 80, 3)

                    ch_p "Mmm, this is a nice surprise, [Player.focused_girl.Pet]."

                    $ Player.focused_girl.NameCheck() #checks reaction to petname

                    "You lean in to the kiss."

                    $ Player.focused_girl.Statup("Love", 85, 1)
                    $ Player.focused_girl.Statup("Obed", 90, 1)
                    $ Player.focused_girl.Statup("Obed", 50, 2)
            "Ask her to stop.":
                    "You pull back."
                    $ Player.focused_girl.FaceChange("surprised")
                    $ Player.focused_girl.Statup("Inbt", 70, 1)

                    ch_p "Let's not do that right now, [Player.focused_girl.Pet]."

                    $ Player.focused_girl.NameCheck() #checks reaction to petname
                    $ Player.focused_girl.Statup("Obed", 90, 1)
                    $ Player.focused_girl.Statup("Obed", 50, 1)
                    $ Player.focused_girl.Statup("Obed", 30, 2)
                    $ Player.RecentActions.append("nope")
                    $ Player.focused_girl.AddWord(1,"refused","refused")
                    return

    if Player.focused_girl.Kissed >= 10 and Player.focused_girl.Lust >= 80:
        $ Line = renpy.random.choice(["She's all over you, running her hands along your body.",
            "She's all over you, licking all over your face and neck.",
            "She's all over you, kissing all over your face and grinding against you."])
    elif Player.focused_girl.Kissed > 7:
        $ Line = renpy.random.choice(["She's really sucking face.",
            "You kiss deeply and passionately.",
            "You kiss deeply and passionately.",
            "You kiss deeply and passionately."])
    elif Player.focused_girl.Kissed > 3:
        $ Line = renpy.random.choice(["She's really getting into it.",
            "She's really getting into it, her tongue's going at it.",
            "She's really getting into it, there's some heavy tongue action."])
    else:
        $ Line = "You and "+ Player.focused_girl.Name +" make out for a while."

    "[Line]"

    $ Cnt = 0
    $ Trigger = "kiss_you"
    $ Line = 0

    if Situation:
        $ renpy.pop_call()

        $ Situation = 0

label kiss_cycle:
    while Round > 0:
        call Shift_Focus(Player.focused_girl)
        call kissing_launch(Player.focused_girl, "kiss_you")

        $ Player.focused_girl.LustFace()

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":
                    call Slap_Ass(Player.focused_girl)

                    $ Cnt += 1
                    $ Round -= 1

                    jump kiss_cycle
                "Focus to last longer [[not unlocked]. (locked)" if "focus" not in Player.Traits:
                    pass
                "Focus to last longer." if not Player.FocusX and "focus" in Player.Traits:
                    "You concentrate on not burning out too quickly."

                    $ Player.FocusX = 1
                "Release your focus." if Player.FocusX:
                    "You release your concentration. . ."

                    $ Player.FocusX = 0
                "Start jack'in it." if MultiAction and Trigger2 != "jackin":
                    call Jackin(Player.focused_girl)
                "Stop jack'in it." if MultiAction and Trigger2 == "jackin":
                    "You stop jack'in it."

                    $ Trigger2 = 0
                "Other options":
                    menu:
                        "Offhand action":
                            if Player.focused_girl.Action and MultiAction:
                                call Offhand_Set

                                if Trigger2:
                                     $ Player.focused_girl.Action -= 1
                            else:
                                call tired_lines(Player.focused_girl)
                        "Shift primary action":
                            if Player.focused_girl.Action and MultiAction:
                                menu:
                                    "Move a hand to her breasts. . ." if Player.focused_girl.Kissed >= 1 and MultiAction:
                                        if Player.focused_girl.Action and MultiAction:
                                            $ Situation = "auto"

                                            call after_kiss
                                            call fondle_breasts(Player.focused_girl)

                                            if Trigger == "fondle breasts":
                                                $ Trigger2 = "kiss_you"

                                                $ Player.primary_action = "fondle_breasts"

                                                call before_fondle
                                            else:
                                                $ Trigger = "kiss_you"
                                        else:
                                            "As your hands creep upwards, she grabs your wrists."

                                            call tired_lines(Player.focused_girl)
                                    "Move a hand to her thighs. . ." if Player.focused_girl.Kissed >= 1 and MultiAction:
                                        if Player.focused_girl.Action and MultiAction:
                                            $ Situation = "auto"

                                            call after_kiss
                                            call fondle_thighs

                                            if Trigger == "fondle thighs":
                                                    $ Trigger2 = "kiss_you"

                                                    $ Player.primary_action = "fondle_thighs"

                                                    call before_fondle
                                            else:
                                                $ Trigger = "kiss_you"
                                        else:
                                            "As your hands creep downwards, she grabs your wrists."

                                            call tired_lines(Player.focused_girl)
                                    "Never Mind":
                                        jump kiss_cycle
                            else:
                                call tired_lines(Player.focused_girl)
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [Player.focused_girl.Name] to do something else with [Partner.Name]" if Trigger == "lesbian":
                                    call Les_Change(Player.focused_girl)
                                "Ask [Player.focused_girl.Name] to do something else with [Partner.Name] (locked)" if Trigger != "lesbian":
                                    pass
                                "Ask [Partner.Name] to do something else":
                                    call Three_Change(Player.focused_girl)
                                "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                    $ ThreeCount = 0
                                "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                    $ ThreeCount = 0
                                "Swap to [Partner.Name]":
                                    call Trigger_Swap(Player.focused_girl)
                                "Undress [Partner.Name]":
                                    call Girl_Undress(Partner)
                                    call Shift_Focus(Partner)

                                    jump kiss_cycle
                                "Clean up Partner":
                                    call Girl_Cleanup(Partner,"ask")

                                    jump kiss_cycle
                                "Never mind":
                                    jump kiss_cycle
                        "Undress [Player.focused_girl.Name]":
                            call Girl_Undress(Player.focused_girl)
                        "Clean up [character.Name] (locked)" if not Player.focused_girl.Spunk:
                            pass
                        "Clean up [Player.focused_girl.Name]" if Player.focused_girl.Spunk:
                            call Girl_Cleanup(Player.focused_girl,"ask")
                        "Never mind":
                            jump kiss_cycle
                "Back to Sex Menu" if MultiAction and Player.focused_girl.Kissed >= 5:
                    ch_p "Let's try something else."

                    $ Situation = "shift"
                    $ Line = 0

                    jump after_kiss
                "End Scene":
                    ch_p "Let's stop for now."

                    $ Line = 0

                    jump after_kiss

        call Shift_Focus(Player.focused_girl)
        call Sex_Dialog(Player.focused_girl,Partner)

        $ Cnt += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or Player.focused_girl.Lust >= 100:
            if Player.Focus >= 100:
                call Player_Cumming(Player.focused_girl)

                if "angry" in Player.focused_girl.RecentActions:
                    call reset_position(Player.focused_girl)

                    return

                $ Player.focused_girl.Statup("Lust", 200, 5)

                if 100 > Player.focused_girl.Lust >= 70 and Player.focused_girl.OCount < 2 and Player.focused_girl.SEXP >= 20:
                    $ Player.focused_girl.RecentActions.append("unsatisfied")
                    $ Player.focused_girl.DailyActions.append("unsatisfied")

                if Player.Focus > 80:
                    jump after_kiss

                $ Line = "came"

            if Player.focused_girl.Lust >= 100:
                call Girl_Cumming(Player.focused_girl)

                if Situation == "shift" or "angry" in Player.focused_girl.RecentActions:
                    jump after_kiss

            if Line == "came":
                if not Player.Semen:
                    "You're pretty wiped, better stop for now."

                $ Line = 0

                jump after_kiss

        if Partner and Partner.Lust >= 100:
            call Girl_Cumming(Partner)

        call Escalation(Player.focused_girl) #sees if she wants to escalate things

        if Round == 10:
            call wrap_this_up_lines(Player.focused_girl)
        elif Round == 5:
            call time_to_stop_soon_lines(Player.focused_girl)

    $ Player.focused_girl.FaceChange("bemused", 0)

    $ Line = 0

    call im_done_lines

label after_kiss:
    $ Player.focused_girl.FaceChange("sexy")

    $ Player.focused_girl.Kissed += 1
    $ Player.focused_girl.Action -= 1
    $ Player.focused_girl.Addictionrate += 2 if Player.focused_girl.Addictionrate < 5 else 1
    $ Player.focused_girl.Addictionrate += 1 if "addictive" in Player.Traits else 0

    call Partner_Like(Player.focused_girl, 1) #raises other girl's like levels if watching

    if "kissing" not in Player.focused_girl.RecentActions:
        if Player.focused_girl.Love > 300:
            $ Player.focused_girl.Statup("Love", 60, 4)

        $ Player.focused_girl.Statup("Love", 70, 1)
        $ Player.focused_girl.RecentActions.append("kissing")
        $ Player.focused_girl.DailyActions.append("kissing")

    if Player.focused_girl.Kissed > 10:
        pass
    elif Player.focused_girl.Kissed == 10:
        $ Player.focused_girl.FaceChange("smile", 1)
        if Player.focused_girl == RogueX:
            ch_r "You must really like my lips, huh?"
        elif Player.focused_girl == KittyX:
            ch_k "I could eat you up."
        elif Player.focused_girl == EmmaX:
            ch_e "This has been a pleasant surprise."
        elif Player.focused_girl == LauraX:
            ch_l "I could do this every day."
        elif Player.focused_girl == JeanX:
            ch_j "You've made some serious improvement. . ."
            ch_j "I must be rubbing off on you. . ."
        elif Player.focused_girl == StormX:
            ch_s "I have grown to enjoy this quite a bit."
        elif Player.focused_girl == JubesX:
            ch_v "I love the taste of your lips. . ."
    elif Player.focused_girl.Kissed == 5:
        if Player.focused_girl == RogueX:
            ch_r "We're really making this a regular thing."
        elif Player.focused_girl == KittyX:
            ch_k "You're good at this. . ."
        elif Player.focused_girl == EmmaX:
            ch_e "You're surprisingly talented. . ."
        elif Player.focused_girl == LauraX:
            ch_l "You're really talented. . ."
        elif Player.focused_girl == JeanX:
            ch_j "MmMmmm, that was nice. . ."
        elif Player.focused_girl == StormX:
            ch_s "Mmmm, has anyone told you that you are quite good at this?"
        elif Player.focused_girl == JubesX:
            ch_v "Kissing you really feels great!"
    elif Player.focused_girl.Kissed == 1:
        if Player.focused_girl == JubesX:
            "[Player.focused_girl.Name] bites your lip as she pulls back, and licks some blood off her lips."

            ch_v "Sorry about that. . ."
            ch_v "Won't happen again."

        $ Player.focused_girl.SEXP += 1

    if not Situation and Player.focused_girl.Kissed > 5 and Player.focused_girl.Lust > 50 and ApprovalCheck(Player.focused_girl, 950):
        $ Player.focused_girl.FaceChange("sexy", 1)
        $ Player.focused_girl.Brows = "sad"

        if Player.focused_girl == RogueX:
            ch_r "You maybe want to try something more?"
        elif Player.focused_girl == KittyX:
            ch_k "Is that it?"
        elif Player.focused_girl == EmmaX:
            ch_e "You wouldn't be interested in something more? . ."
        elif Player.focused_girl == LauraX:
            ch_l "Huh, that's all there is to it?"
        elif Player.focused_girl == JeanX:
            ch_j "That was nice. . ."
        elif Player.focused_girl == StormX:
            ch_s "Oh. . . that was lovely."
        elif Player.focused_girl == JubesX:
            ch_v "Did you want. . . more?"

    $ temp_modifier = 0

    call Checkout

    if Situation:
        call Sex_Basic_Dialog(Player.focused_girl, "switch")
    else:
        call reset_position(Player.focused_girl)

    return
