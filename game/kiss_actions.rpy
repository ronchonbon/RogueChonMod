label kiss(Girl):
    $ primary_action = "kiss"

    $ Round -= 5 if Round > 5 else (Round-1)

    call shift_focus(Girl)

    $ Approval = ApprovalCheck(Girl, 700, TabM=1,Alt=[[RogueX,JeanX],500]) #reduced check for Rogue

    if Girl == EmmaX and not ApprovalCheck(Girl, 1000):
        $ Girl.change_face("sadside")

        ch_e "Not when we barely know each other. . ."

        $ Girl.recent_history.append("no_kissing")
        $ Girl.daily_history.append("no_kissing")
        return
    if Approval > 1 and not Girl.Kissed and not Girl.Forced:
        $ Girl.change_face("sexy")
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
        $ Girl.change_face("sexy")
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
    elif Approval and "kissing" in Girl.recent_history:
        $ Girl.change_face("sexy", 1)

        if Girl == KittyX:
            ch_k "Prrr. . ."
        else:
            call Anyline(Girl,"Mmmm. . .")

        jump before_kiss
    elif Approval and "kissing" in Girl.daily_history:
        $ Girl.change_face("sexy", 1)

        $ line = renpy.random.choice(["A","B","C"])
        if line == "A":
            call Anyline(Girl,"Didn't get enough earlier?")
        elif Girl == RogueX:
            if line == "B":
                ch_r "{i}I'm{/i} used to being the one sucking people dry. . ."
            else:
                ch_r "Gimme some sugar, sugar."
        elif Girl == KittyX:
            if line == "B":
                ch_k "Meow."
            else:
                ch_k "Come'ere tasty."
        elif Girl == EmmaX:
            if line == "B":
                ch_e "Mmmm. . ."
            else:
                ch_e "Come and get it."
        elif Girl == LauraX:
            if line == "B":
                ch_l "Mmmmmm."
            else:
                ch_l "Get over here."
        elif Girl == JeanX:
            if line == "B":
                ch_j "MmMmmm. . ."
            else:
                ch_j "Oh, get over here."
        elif Girl == StormX:
            if line == "B":
                ch_s "Mmmm. . ."
            else:
                ch_s "Yes, let's."
        elif Girl == JubesX:
            if line == "B":
                ch_v "Mmmm. . ."
            else:
                ch_v "Sure, come to me."

        $ line = 0
    elif Approval > 1 and Girl.love > Girl.obedience:
        $ Girl.change_face("sexy")

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
    elif ApprovalCheck(Girl, 500, "O") and Girl.obedience > Girl.love:
        $ Girl.change_face("normal")

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
            ch_v "Sure. . ."

        $ Girl.change_stat("obedience", 60, 1)
    elif ApprovalCheck(Girl, 250, "O",Alt=[[KittyX,LauraX],300]) and ApprovalCheck(Girl, 250, "L",Alt=[[KittyX,LauraX],200]):
        $ Girl.change_face("bemused")

        call Anyline(Girl,"Ok, fine.")

        $ Girl.change_stat("obedience", 50, 3)
    elif Girl.Addict >= 50:
        $ Girl.change_face("sexy")
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
        $ Girl.change_face("bemused")

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
        $ Girl.change_face("normal") # Else
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

        $ Girl.recent_history.append("no_kissing")
        $ Girl.daily_history.append("no_kissing")

        return

    jump before_kiss

label before_kiss:
    $ focused_Girl.change_stat("inhibition", 10, 1)
    $ focused_Girl.change_stat("inhibition", 20, 1)

    call kissing_launch(focused_Girl, "kiss")

    if focused_Girl.Kissed >= 10 and focused_Girl.inhibition >= 300:
        $ focused_Girl.change_face("sucking")
    elif focused_Girl.Kissed > 1 and focused_Girl.Addict >= 50:
        $ focused_Girl.change_face("sucking")
    else:
        $ focused_Girl.change_face("kiss",2)

    if Taboo:
        $ focused_Girl.DrainWord("tabno")

    $ focused_Girl.DrainWord("no_kissing")

    if focused_Girl == RogueX and not focused_Girl.Kissed:
        "You lean in and your lips meet [focused_Girl.name]'s."

        $ focused_Girl.Eyes = "surprised"
        $ focused_Girl.change_stat("love", 90, 15)
        $ focused_Girl.change_stat("love", 60, 30)

        "A slight spark passes between you and her eyes widen with surprise."

        $ focused_Girl.change_stat("lust", 70, 5)

        ch_r "Wow, [focused_Girl.Petname], that was really something. . ."

        $ focused_Girl.change_face("bemused",1)

        ch_r "Not the kind of zap I'm used to."

        $ focused_Girl.Addict -= 5
        $ focused_Girl.change_stat("obedience", 30, 20)
        $ focused_Girl.change_stat("inhibition", 30, 30)

        jump after_kiss

    if action_context == focused_Girl:
        $ action_context = 0

        "[focused_Girl.name] presses her body against yours, and kisses you deeply."
        menu:
            "What do you do?"
            "Go with it.":
                    $ focused_Girl.change_stat("inhibition", 80, 3)
                    $ focused_Girl.change_stat("inhibition", 50, 2)

                    "You lean in to the kiss."
            "Praise her.":
                    $ focused_Girl.change_face("sexy", 1)
                    $ focused_Girl.change_stat("inhibition", 80, 3)

                    ch_p "Mmm, this is a nice surprise, [focused_Girl.Pet]."

                    $ focused_Girl.nameCheck() #checks reaction to petname

                    "You lean in to the kiss."

                    $ focused_Girl.change_stat("love", 85, 1)
                    $ focused_Girl.change_stat("obedience", 90, 1)
                    $ focused_Girl.change_stat("obedience", 50, 2)
            "Ask her to stop.":
                    "You pull back."
                    $ focused_Girl.change_face("surprised")
                    $ focused_Girl.change_stat("inhibition", 70, 1)

                    ch_p "Let's not do that right now, [focused_Girl.Pet]."

                    $ focused_Girl.nameCheck() #checks reaction to petname
                    $ focused_Girl.change_stat("obedience", 90, 1)
                    $ focused_Girl.change_stat("obedience", 50, 1)
                    $ focused_Girl.change_stat("obedience", 30, 2)
                    $ Player.recent_history.append("nope")
                    $ focused_Girl.AddWord(1,"refused","refused")
                    return

    if focused_Girl.Kissed >= 10 and focused_Girl.lust >= 80:
        $ line = renpy.random.choice(["She's all over you, running her hands along your body.",
            "She's all over you, licking all over your face and neck.",
            "She's all over you, kissing all over your face and grinding against you."])
    elif focused_Girl.Kissed > 7:
        $ line = renpy.random.choice(["She's really sucking face.",
            "You kiss deeply and passionately.",
            "You kiss deeply and passionately.",
            "You kiss deeply and passionately."])
    elif focused_Girl.Kissed > 3:
        $ line = renpy.random.choice(["She's really getting into it.",
            "She's really getting into it, her tongue's going at it.",
            "She's really getting into it, there's some heavy tongue action."])
    else:
        $ line = "You and "+ focused_Girl.name +" make out for a while."

    "[line]"

    $ counter = 0
    $ primary_action = "kiss"
    $ line = 0

    if action_context:
        $ renpy.pop_call()

        $ action_context = 0

label kiss_cycle:
    while Round > 0:
        call shift_focus(focused_Girl)
        call kissing_launch(focused_Girl, "kiss")

        $ focused_Girl.lustFace()

        $ Player.Focus -= 10 if Player.FocusX and Player.Focus > 50 else 0

        if  Player.Focus < 100:
            menu:
                "Keep going. . .":
                    pass
                "Slap her ass":
                    call Slap_Ass(focused_Girl)

                    $ counter += 1
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
                "Start jack'in it." if multi_action and offhand_action != "jackin":
                    call Jackin(focused_Girl)
                "Stop jack'in it." if multi_action and offhand_action == "jackin":
                    "You stop jack'in it."

                    $ offhand_action = 0
                "Other options":
                    menu:
                        "Offhand action":
                            if focused_Girl.Action and multi_action:
                                call Offhand_Set

                                if offhand_action:
                                     $ focused_Girl.Action -= 1
                            else:
                                call tired_lines(focused_Girl)
                        "Shift primary action":
                            if focused_Girl.Action and multi_action:
                                menu:
                                    "Move a hand to her breasts. . ." if focused_Girl.Kissed >= 1 and multi_action:
                                        if focused_Girl.Action and multi_action:
                                            $ action_context = "auto"

                                            call after_kiss
                                            call fondle_breasts(focused_Girl)

                                            if primary_action == "fondle_breasts":
                                                $ offhand_action = "kiss"

                                                $ primary_action = "fondle_breasts"

                                                call before_fondle
                                            else:
                                                $ primary_action = "kiss"
                                        else:
                                            "As your hands creep upwards, she grabs your wrists."

                                            call tired_lines(focused_Girl)
                                    "Move a hand to her thighs. . ." if focused_Girl.Kissed >= 1 and multi_action:
                                        if focused_Girl.Action and multi_action:
                                            $ action_context = "auto"

                                            call after_kiss
                                            call fondle_thighs

                                            if primary_action == "fondle_thighs":
                                                    $ offhand_action = "kiss"

                                                    $ primary_action = "fondle_thighs"

                                                    call before_fondle
                                            else:
                                                $ primary_action = "kiss"
                                        else:
                                            "As your hands creep downwards, she grabs your wrists."

                                            call tired_lines(focused_Girl)
                                    "Never Mind":
                                        jump kiss_cycle
                            else:
                                call tired_lines(focused_Girl)
                        "Threesome actions (locked)" if not Partner:
                            pass
                        "Threesome actions" if Partner:
                            menu:
                                "Ask [focused_Girl.name] to do something else with [Partner.name]" if primary_action == "lesbian":
                                    call Les_Change(focused_Girl)
                                "Ask [focused_Girl.name] to do something else with [Partner.name] (locked)" if primary_action != "lesbian":
                                    pass
                                "Ask [Partner.name] to do something else":
                                    call Three_Change(focused_Girl)
                                "Don't stop what you're doing. . .(locked)" if not position_change_timer or not Partner_primary_action:
                                    $ position_change_timer = 0
                                "Don't stop what you're doing. . ." if position_change_timer and Partner_primary_action:
                                    $ position_change_timer = 0
                                "Swap to [Partner.name]":
                                    call primary_action_Swap(focused_Girl)
                                "Undress [Partner.name]":
                                    call Girl_Undress(Partner)
                                    call shift_focus(Partner)

                                    jump kiss_cycle
                                "Clean up Partner":
                                    call Girl_Cleanup(Partner,"ask")

                                    jump kiss_cycle
                                "Never mind":
                                    jump kiss_cycle
                        "Undress [focused_Girl.name]":
                            call Girl_Undress(focused_Girl)
                        "Clean up [Girl.name] (locked)" if not focused_Girl.Spunk:
                            pass
                        "Clean up [focused_Girl.name]" if focused_Girl.Spunk:
                            call Girl_Cleanup(focused_Girl,"ask")
                        "Never mind":
                            jump kiss_cycle
                "Back to Sex Menu" if multi_action and focused_Girl.Kissed >= 5:
                    ch_p "Let's try something else."

                    $ action_context = "shift"
                    $ line = 0

                    jump after_kiss
                "End Scene":
                    ch_p "Let's stop for now."

                    $ line = 0

                    jump after_kiss

        call shift_focus(focused_Girl)
        call Sex_Dialog(focused_Girl,Partner)

        $ counter += 1
        $ Round -= 1

        $ Player.Focus = 50 if not Player.Semen and Player.Focus >= 50 else Player.Focus #Resets Player.Focus if can't get it up

        if Player.Focus >= 100 or focused_Girl.lust >= 100:
            if Player.Focus >= 100:
                call Player_Cumming(focused_Girl)

                if "angry" in focused_Girl.recent_history:
                    call reset_position(focused_Girl)

                    return

                $ focused_Girl.change_stat("lust", 200, 5)

                if 100 > focused_Girl.lust >= 70 and focused_Girl.OCount < 2 and focused_Girl.SEXP >= 20:
                    $ focused_Girl.recent_history.append("unsatisfied")
                    $ focused_Girl.daily_history.append("unsatisfied")

                if Player.Focus > 80:
                    jump after_kiss

                $ line = "came"

            if focused_Girl.lust >= 100:
                call Girl_Cumming(focused_Girl)

                if action_context == "shift" or "angry" in focused_Girl.recent_history:
                    jump after_kiss

            if line == "came":
                if not Player.Semen:
                    "You're pretty wiped, better stop for now."

                $ line = 0

                jump after_kiss

        if Partner and Partner.lust >= 100:
            call Girl_Cumming(Partner)

        call Escalation(focused_Girl) #sees if she wants to escalate things

        if Round == 10:
            call wrap_this_up_lines(focused_Girl)
        elif Round == 5:
            call time_to_stop_soon_lines(focused_Girl)

    $ focused_Girl.change_face("bemused", 0)

    $ line = 0

    call im_done_lines

label after_kiss:
    $ focused_Girl.change_face("sexy")

    $ focused_Girl.Kissed += 1
    $ focused_Girl.Action -= 1
    $ focused_Girl.Addictionrate += 2 if focused_Girl.Addictionrate < 5 else 1
    $ focused_Girl.Addictionrate += 1 if Player.addictive else 0

    call Partner_Like(focused_Girl, 1) #raises other girl's like levels if watching

    if "kissing" not in focused_Girl.recent_history:
        if focused_Girl.love > 300:
            $ focused_Girl.change_stat("love", 60, 4)

        $ focused_Girl.change_stat("love", 70, 1)
        $ focused_Girl.recent_history.append("kissing")
        $ focused_Girl.daily_history.append("kissing")

    if focused_Girl.Kissed > 10:
        pass
    elif focused_Girl.Kissed == 10:
        $ focused_Girl.change_face("smile", 1)
        if focused_Girl == RogueX:
            ch_r "You must really like my lips, huh?"
        elif focused_Girl == KittyX:
            ch_k "I could eat you up."
        elif focused_Girl == EmmaX:
            ch_e "This has been a pleasant surprise."
        elif focused_Girl == LauraX:
            ch_l "I could do this every day."
        elif focused_Girl == JeanX:
            ch_j "You've made some serious improvement. . ."
            ch_j "I must be rubbing off on you. . ."
        elif focused_Girl == StormX:
            ch_s "I have grown to enjoy this quite a bit."
        elif focused_Girl == JubesX:
            ch_v "I love the taste of your lips. . ."
    elif focused_Girl.Kissed == 5:
        if focused_Girl == RogueX:
            ch_r "We're really making this a regular thing."
        elif focused_Girl == KittyX:
            ch_k "You're good at this. . ."
        elif focused_Girl == EmmaX:
            ch_e "You're surprisingly talented. . ."
        elif focused_Girl == LauraX:
            ch_l "You're really talented. . ."
        elif focused_Girl == JeanX:
            ch_j "MmMmmm, that was nice. . ."
        elif focused_Girl == StormX:
            ch_s "Mmmm, has anyone told you that you are quite good at this?"
        elif focused_Girl == JubesX:
            ch_v "Kissing you really feels great!"
    elif focused_Girl.Kissed == 1:
        if focused_Girl == JubesX:
            "[focused_Girl.name] bites your lip as she pulls back, and licks some blood off her lips."

            ch_v "Sorry about that. . ."
            ch_v "Won't happen again."

        $ focused_Girl.SEXP += 1

    if not action_context and focused_Girl.Kissed > 5 and focused_Girl.lust > 50 and ApprovalCheck(focused_Girl, 950):
        $ focused_Girl.change_face("sexy", 1)
        $ focused_Girl.Brows = "sad"

        if focused_Girl == RogueX:
            ch_r "You maybe want to try something more?"
        elif focused_Girl == KittyX:
            ch_k "Is that it?"
        elif focused_Girl == EmmaX:
            ch_e "You wouldn't be interested in something more? . ."
        elif focused_Girl == LauraX:
            ch_l "Huh, that's all there is to it?"
        elif focused_Girl == JeanX:
            ch_j "That was nice. . ."
        elif focused_Girl == StormX:
            ch_s "Oh. . . that was lovely."
        elif focused_Girl == JubesX:
            ch_v "Did you want. . . more?"

    $ temp_modifier = 0

    call Checkout

    if action_context:
        call Sex_Basic_Dialog(focused_Girl, "switch")
    else:
        call reset_position(focused_Girl)

    return
