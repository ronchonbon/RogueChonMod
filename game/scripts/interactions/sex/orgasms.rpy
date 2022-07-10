label Player_Cumming(Girl=0, approval_bonus=approval_bonus):
    if "phonesex" in Player.recent_history:
        $ Player.semen -= 1
        $ Player.climax = 0
        "You spray jizz across the room."
        return

    $ Girl = check_girl(Girl)

    $ shift_focus (Girl)
    if Player.primary_Action == "blowjob":
        $ approval_bonus += 5

    if Girl.addiction > 75:
        $ approval_bonus += 20
    elif Girl.addiction > 50:
        $ approval_bonus += 5

    if Girl.permanent_History["swallowed"] >= 10:
        $ approval_bonus += 15
    elif Girl.permanent_History["swallowed"] >= 3:
        $ approval_bonus += 5

    if (Girl.permanent_History["creampied"] + Girl.permanent_History["anal_creampied"]) >= 10:
        $ approval_bonus += 15
    elif (Girl.permanent_History["creampied"] + Girl.permanent_History["anal_creampied"]) >= 3:
        $ approval_bonus += 5

    $ D20 = renpy.random.randint(1, 20)


    if action_context == "swap":

        $ line = "So what would you like " + Girl.name + " to do?"
    elif Player.primary_Action == "handjob":
        $ line = "As she strokes, you're about ready to come. . ."
    elif Player.primary_Action == "blowjob":
        $ line = "As she sucks at you, you start to feel about to come. . ."
    elif Player.primary_Action == "titjob":
        $ line = "As you rub into her cleavage, you start to feel about to come. . ."
    elif Player.primary_Action == "sex" or Player.primary_Action == "anal":
        $ line = "As you thrust into her, you feel about to blow. . ."
    elif Player.primary_Action == "hotdog":
        $ line = "As you grind into her, you feel about to blow. . ."
    else:
        $ line = "You start to feel about to come. . ."

    $ Girl.change_face("sexy")

    menu:
        "[line]"
        "Warn her":
            $ action_context = "warn"
            jump Girl_Warn_Her
        "Ask to cum in her mouth":

            $ action_context = "asked"
            jump Girl_In_mouth
        "Cum in her mouth without asking" if Player.primary_Action == "blowjob" or Player.primary_Action == "handjob" or Player.primary_Action == "titjob" and action_context != "swap":
            $ action_context = "auto"
            jump Girl_In_mouth

        "Ask to cum inside her" if Player.primary_Action == "sex" and action_context != "swap":
            $ action_context = "asked"
            jump Girl_Creampie_P
        "Ask to cum inside her" if Player.primary_Action == "anal" and action_context != "swap":
            $ action_context = "asked"
            jump Girl_Creampie_A

        "Cum inside her" if Player.primary_Action == "sex" and action_context != "swap":
            $ action_context = "auto"
            jump Girl_Creampie_P
        "Cum inside her" if Player.primary_Action == "anal" and action_context != "swap":
            $ action_context = "auto"
            jump Girl_Creampie_A
        "Cum outside":
            menu:
                "Cum on her face":
                    jump Girl_Facial
                "Cum on her tits":
                    jump Girl_TitSpunk
                "Cum on her ass":
                    $ Girl.pose = "doggy"
                    jump Girl_Cum_Outside
                "Cum on her belly":
                    $ Girl.pose = "sex"
                    jump Girl_Cum_Outside

        "Actually, let [Partner.name] take it." if Partner in all_Girls and action_context != "swap":
            $ action_context = "swap"
            $ approval_bonus = 0
            $ shift_focus (Partner)
            call show_full_body(Partner)
            call Player_Cumming (Player.focused_Girl, approval_bonus=0)

            $ shift_focus (Partner)
            call show_full_body(Partner)

            $ action_context = None
            "[Girl.name] Steps back in."

            call show_full_body(Girl)

            return

        "Just fire away" if Player.secondary_Action == "jerking_off":
            if "cockout" not in Player.recent_history:
                $ Player.spunk = "in"
                "You cum in your pants."
            else:
                "You spray jizz across the room."
            jump Girl_Orgasm_After
        "Pull back" if Player.primary_Action != "psy" and Girl.location == Player.location and action_context != "swap":
            if renpy.showing(Girl.tag + " blowjob"):
                if Girl.addiction >= 60 and approval_check(Girl, 1000, "I", Bonus = ((Girl.addiction*10)- Girl.obedience)) and Girl.permanent_History["swallowed"]:
                    jump Manic_Suck

                call show_full_body(Girl)
            elif renpy.showing(Girl.tag + " handjob"):
                call show_full_body(Girl)
            elif renpy.showing(Girl.tag + " doggy"):
                call show_full_body(Girl)
            elif renpy.showing(Girl.tag + " sex"):
                call show_full_body(Girl)
            if approval_check(Girl, 500, "I", Bonus = ((Girl.addiction*10)- Girl.obedience)) and Girl.addiction > 50 and Girl.permanent_History["swallowed"]:
                $ Girl.eyes = "manic"
                $ Girl.mouth = "kiss"
                $ action_speed = 0
                "Her eyes widen in panic."
                if Girl == RogueX:
                    ch_r "Are you sure you won't reconsider, [Girl.player_petname]?"
                elif Girl == KittyX:
                    ch_k "You[Girl.like]sure about that?"
                elif Girl == EmmaX:
                    ch_e "You wouldn't reconsider, [Girl.player_petname]?"
                elif Girl == LauraX:
                    ch_l "You sure?"
                elif Girl == JeanX:
                    ch_j "Where do you think you're going?"
                elif Girl == StormX:
                    ch_s "Wait . ."
                elif Girl == JubesX:
                    ch_v "Wait, you're letting it go to waste?"
                $ Girl.blushing = "_blush2"
                menu:
                    extend ""
                    "Ok, if you'll swallow it.":
                        if not renpy.showing(Girl.tag + " blowjob"):
                            call show_blowjob(Girl, orgasm = True)
                        $ Girl.change_face("sucking")
                        $ action_speed = 2
                        "She nods and puts the tip into her mouth. As you release she gulps it down hungrily."
                        $ Girl.change_face("sexy")
                        $ Girl.mouth = "sucking"
                        $ Girl.spunk["mouth"] = True
                        ". . ."
                        $ action_speed = 0
                        $ Girl.change_face("sad")
                        $ Girl.mouth = "lipbite"
                        if Girl == RogueX:
                            ch_r "That would have been such a waste otherwise."
                        elif Girl == KittyX:
                            ch_k "You know I like my milk."
                        elif Girl == EmmaX:
                            ch_e "Waste not, want not."
                        elif Girl == LauraX:
                            ch_l "Yum."
                        elif Girl == JeanX:
                            ch_j "Mmm."
                        elif Girl == StormX:
                            ch_s "Mmmm. . ."
                        elif Girl == JubesX:
                            ch_v "Well duh!"
                        call change_Girl_stat(Girl, "obedience", Alt = [[JeanX],800,4])
                        call change_Girl_stat(Girl, "obedience", 1)
                        call change_Girl_stat(Girl, "inhibition", 2)
                        call change_Girl_stat(Girl, "inhibition", 3)
                        jump Girl_Swallowed
                    "No, we're done for now.":
                        if approval_check(Girl, 250, "I", Bonus = ((Girl.addiction*10)- Girl.obedience)) or Girl.addiction > 75:
                            call change_Girl_stat(Girl, "obedience", -1)
                            call change_Girl_stat(Girl, "obedience", -2)
                            call change_Girl_stat(Girl, "inhibition", 2)
                            call change_Girl_stat(Girl, "inhibition", 3)
                            if not renpy.showing(Girl.tag + " blowjob"):
                                call show_blowjob(Girl, orgasm = True)
                                $ action_speed = 4
                            "She dives down on you and you can't resist filling her throat."
                            $ action_speed = 0
                            if Girl == RogueX:
                                ch_r "I. . . just can't pass this up."
                            elif Girl == KittyX:
                                ch_k "It's. . . compelling."
                            elif Girl == EmmaX:
                                ch_e "Well, I'm afraid I wasn't."
                            elif Girl == LauraX:
                                ch_l "Now we are."
                            elif Girl == JeanX:
                                ch_j "Fine, we're done."
                            elif Girl == StormX:
                                ch_s "Now we are done. . ."
                            elif Girl == JubesX:
                                ch_v "Ok, -now- we're done."
                            jump Girl_Swallowed
                        else:
                            call change_Girl_stat(Girl, "obedience", Alt = [[JeanX],800,3])
                            call change_Girl_stat(Girl, "obedience", 5)
                            $ Girl.change_face("sad")
                            $ Girl.brows = "confused"
                            if Girl == RogueX:
                                ch_r "ok. . ."
                            elif Girl == KittyX:
                                ch_k "Whatever."
                            elif Girl == EmmaX:
                                ch_e "If you insist."
                            elif Girl == LauraX:
                                ch_l "Dick."
                            elif Girl == JeanX:
                                ch_j "Whatever."
                            elif Girl == StormX:
                                ch_s ". . ."
                            elif Girl == JubesX:
                                ch_v "Well. . . I still think that was a waste."
                            $ line = 0
                            $ Player.climax -= 5
                            return

            $ Girl.change_face("sexy", 1)
            call change_Girl_stat(Girl, "obedience", 2)
            "You pull pull back away from her. She looks up at you and licks her lips."

            if Girl == RogueX:
                ch_r "Well [Girl.player_petname], what next then?"
            elif Girl == KittyX:
                ch_k "Oh? So what did you want to do?"
            elif Girl == EmmaX:
                ch_e "Well [Girl.player_petname], what next then?"
            elif Girl == LauraX:
                ch_l "So now what?"
            elif Girl == JeanX:
                ch_j "Fine, what now?"
            elif Girl == StormX:
                ch_s "So what did you have in mind then?"
            elif Girl == JubesX:
                ch_v "Ok, so what'd you want?"
            $ line = 0
            $ Player.climax = 95
            return

label Manic_Suck:
    $ Girl.eyes = "manic"
    $ action_speed = 0
    "You pull out of her mouth with a pop, and her eyes widen in surprise."
    $ Girl.mouth = "sucking"
    $ Girl.spunk["mouth"] = True
    $ action_speed = 4
    "She leaps at your cock and sucks it deep, draining your fluids hungrily."
    $ action_speed = 0
    $ Girl.mouth = "lipbite"
    "When she finishes, she licks her lips."
    $ Girl.change_face("bemused")
    if Girl == EmmaX:
        ch_e "I'm sorry, [Girl.player_petname], but that would have been a waste."
    elif Girl == JeanX:
        $ Girl.change_face("sly", 2, mouth = "lipbite")
        ch_j ". . ."
    elif Girl == StormX:
        ch_s "That would have been wasteful. . ."
    else:
        Girl.voice "Sorry, [Girl.player_petname], I just couldn't let that go to waste."
    call change_Girl_stat(Girl, "obedience", Alt = [[JeanX],800, 5])
    call change_Girl_stat(Girl, "inhibition", 10)
    jump Girl_Swallowed

label Girl_Warn_Her:
    "You let her know that you're going to come."
    call change_Girl_stat(Girl, "love", 900, 5])
    if Girl.obedience >= 500:
        call change_Girl_stat(Girl, "obedience", 5)
    if ("hungry" in Girl.traits and D20 >= 5):
        if renpy.showing(Girl.tag + " doggy") or renpy.showing(Girl.tag + " sex"):
            call show_handjob(Girl, orgasm = True)
            "She grins and pulls out with a pop, and begins to stroke you off."
        $ action_speed = 2
        $ Girl.change_face("sucking")
        ". . ."
        $ action_speed = 0
        $ Girl.spunk["mouth"] = True
        $ Girl.spunk["chin"] = True
        if not renpy.showing(Girl.tag + " blowjob"):
            "She smiles and then puts your tip in her mouth. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
        else:
            "She makes a little humming sound, but keeps sucking. When you finish filling her mouth, she quickly gulps it down and wipes her lips."
        $ Girl.change_face("sexy")
        $ Girl.mouth = "smile"
        call Sex_Basic_Dialog (Girl, "swallowgood")
        call Sex_Basic_Dialog (Girl, "warned")
        jump Girl_Swallowed


    if Player.primary_Action == "sex" and Girl.permanent_History["creampied"] >= 5:

        $ Girl.change_face("sexy")
        $ Player.primary_Action.type = "sex"
        $ Girl.spunk["pussy"] = True
        $ Player.spunk = "in"
        $ action_speed = 0
        "She smiles and speeds up her actions, causing you to erupt inside her."
        if Girl.lust >= 85:
            call Girl_Cumming (Girl)
        jump Girl_Creampied

    elif Player.primary_Action == "sex" and Girl.permanent_History["creampied"] and D20 >= 10:

        $ Girl.change_face("sexy")
        $ Player.primary_Action.type = "sex"
        $ Girl.spunk["pussy"] = True
        $ Player.spunk = "in"
        $ action_speed = 0
        "She gets a mischievous look and speeds up, you burst inside her."
        if Girl.lust >= 85:
            call Girl_Cumming (Girl)
        jump Girl_Creampied

    elif Player.primary_Action == "anal" and Girl.permanent_History["anal_creampied"] >= 5:

        $ Girl.change_face("sexy")
        $ Player.primary_Action.type = "anal"
        $ Girl.spunk["anus"] = True
        $ Player.spunk = "anal"
        $ action_speed = 0
        "She smiles and speeds up her actions, causing you to erupt inside her."
        if Girl.lust >= 85:
            call Girl_Cumming (Girl)
        jump Girl_Creampied

    elif Player.primary_Action == "anal" and Girl.permanent_History["anal_creampied"] and D20 >= 10:

        $ Girl.change_face("sexy")
        $ Player.primary_Action.type = "anal"
        $ Girl.spunk["anus"] = True
        $ Player.spunk = "anal"
        $ action_speed = 0
        "She gets a mischievous look and speeds up, you burst inside her."
        if Girl.lust >= 85:
            call Girl_Cumming (Girl)
        jump Girl_Creampied

    elif Player.primary_Action != "anal" and Girl.permanent_History["swallowed"] >= 5:

        if renpy.showing(Girl.tag + " blowjob"):
            $ Girl.change_face("sucking")
            $ Girl.spunk["mouth"] = True
            "She makes a little humming sound, but keeps sucking."
        else:
            if renpy.showing(Girl.tag + " doggy") or renpy.showing(Girl.tag + " sex"):
                call show_blowjob(Girl, orgasm = True)
                $ action_speed = 2
            $ Girl.change_face("sucking")
            $ Girl.spunk["mouth"] = True
            "She smiles and then puts your tip in her mouth."
        $ Girl.spunk["chin"] = True
        "When you finish filling her mouth, she quickly gulps it down and wipes her lips."
        $ action_speed = 0
        $ Girl.change_face("sexy")
        $ Girl.mouth = "smile"
        call Sex_Basic_Dialog (Girl, "swallowgood")
        call Sex_Basic_Dialog (Girl, "warned")
        jump Girl_Swallowed

    elif Girl.permanent_History["swallowed"] and D20 >= 10:

        if renpy.showing(Girl.tag + " doggy") or renpy.showing(Girl.tag + " sex"):
            call show_handjob(Girl, orgasm = True)
            "She grins and pulls out with a pop, and begins to stroke you off."
        $ action_speed = 2
        if renpy.showing(Girl.tag + " blowjob"):

            $ Girl.change_face("sucking")
            $ Girl.spunk["mouth"] = True
            "She makes a little humming sound, but keeps sucking."
            "When you finish filling her mouth, she gags a little, but manages to swallow it."
            $ action_speed = 0
            $ Girl.change_face("sexy")
            $ Girl.mouth = "smile"
            $ Girl.spunk["chin"] = True
            if Girl.addiction > 50:
                $ Girl.eyes = "manic"
                "She gulps it down hungrily and licks her lips."
            $ Girl.change_face("bemused")
            call Sex_Basic_Dialog (Girl, "swallow2")
            call Sex_Basic_Dialog (Girl, "warned")
            jump Girl_Swallowed
        else:


            jump Girl_Handy_Finish


    elif approval_check(Girl, 1000):

        if Girl.SEXP > 20 and (renpy.showing(Girl.tag + " doggy") or renpy.showing(Girl.tag + " sex")):
            "She gently pushes you back off of her."
            jump Girl_Cum_Outside
        elif Girl.SEXP > 20:
            jump Girl_Facial

        if renpy.showing(Girl.tag + " handjob") and Girl.permanent_History["handjob"]:
            jump Girl_Handy_Finish
        elif renpy.showing(Girl.tag + " blowjob") and Girl.permanent_History["blowjob"]:
            jump Girl_Handy_Finish
        elif renpy.showing(Girl.tag + " titjob") and Girl.permanent_History["titjob"]:
            jump Girl_Facial
        elif (renpy.showing(Girl.tag + " doggy") or renpy.showing(Girl.tag + " sex")) and Girl.permanent_History["sex"] and Player.primary_Action == "sex":
            "She gently pushes you back off of her."
            jump Girl_Cum_Outside
        elif (renpy.showing(Girl.tag + " doggy") or renpy.showing(Girl.tag + " sex")) and Girl.permanent_History["anal"] and Player.primary_Action == "anal":
            "She gently pushes you back off of her."
            jump Girl_Cum_Outside



    if renpy.showing(Girl.tag + " blowjob"):
        jump Girl_In_mouth
    elif Player.primary_Action == "sex" or Player.primary_Action == "anal":
        call show_full_body(Girl)
        "She pulls off of you and grabs your cock in her hand."
        jump Girl_Handy_Finish
    elif renpy.showing(Girl.tag + " doggy") or renpy.showing(Girl.tag + " sex"):
        "She smiles and starts rubbing against you a bit faster."
        jump Girl_Cum_Outside
    jump Girl_Facial

label Girl_In_mouth:
    if Player.primary_Action == "anal":
        $ approval_bonus -= 15
    if "hungry" not in Girl.traits and Girl.addiction <= 50 and "full" in Girl.recent_history:
        $ approval_bonus -= 15



    $ Player.primary_Action.type = "out"
    if action_context == "auto" or action_context == "warn":
        $ action_context = None
        if not renpy.showing(Girl.tag + " blowjob"):
            call show_blowjob(Girl, orgasm = True)
        $ action_speed = 2
        if action_context == "warn":
            "She doesn't seem sure what to do about that, as you cum in her mouth."
        else:
            "You grab her head and cum in her mouth"
        $ Girl.eyes = "closed"
        call punch
        $ Player.spunk = 1
        if "full" in Girl.recent_history:

            $ Girl.change_face("bemused")
            $ Girl.spunk["mouth"] = True
            $ action_speed = 0
            $ Girl.spunk["chin"] = True
            "She gags a little, but manages to swallow it."
            $ Girl.spunk["mouth"] = False
            if Girl == RogueX:
                ch_r "Um, I. . . I think I've had enough for now, could we maybe. . ."
                ch_r ". . . put that stuff someplace else?"
            elif Girl == KittyX:
                ch_k "I'm[Girl.like]totally stuffed here. . ."
                ch_k ". . . is there anywhere else we could put this?"
            elif Girl == EmmaX:
                ch_e "Hmm. . . that, may be a bit much for right now. . ."
                ch_e "Perhaps we could find someplace else for you to. . . release. . ."
            elif Girl == LauraX:
                ch_l "Hmm. . . I'm kinda full. . ."
                ch_l "Maybe keep it outside. . ."
            elif Girl == JeanX:
                ch_j "I'm kinda full at the moment."
            elif Girl == StormX:
                ch_s "I am afraid that I am rather full at the moment. . ."
            elif Girl == JubesX:
                ch_v "I, um. . . I think I'm actually stuffed. . ."
        elif Girl.permanent_History["swallowed"] >= 5 or "hungry" in Girl.traits:

            $ Girl.change_face("sexy")
            $ Girl.mouth = "smile"
            $ Girl.spunk["mouth"] = True
            $ Girl.spunk["chin"] = True
            "She quickly gulps it down and wipes her mouth."
            $ Girl.spunk["mouth"] = False
            $ action_speed = 0
            call Sex_Basic_Dialog (Girl, "swallowgood")
            $ Girl.change_face()
        elif Girl.permanent_History["swallowed"]:
            $ Girl.change_face("bemused")
            $ Girl.spunk["mouth"] = True
            $ Girl.spunk["chin"] = True
            $ action_speed = 0
            "She gags a little, but manages to swallow it."
            $ Girl.spunk["mouth"] = False
            call Sex_Basic_Dialog (Girl, "swallow2")
            if action_context != "warn":
                call Sex_Basic_Dialog (Girl, "notwarned")
            $ Girl.change_face()
        elif Girl.addiction >= 50 and Girl.inhibition < 400 and Girl.permanent_History["blowjob"] < 10 and Girl != JubesX:
            $ Girl.change_face("bemused", 1)
            $ Girl.spunk["mouth"] = True
            Girl.voice ". . ."
            $ Girl.spunk["mouth"] = False
            $ Girl.spunk["chin"] = True
            $ Girl.spunk["hand"] = True
            $ action_speed = 0
            "She gags and spits it into her palm. Then she licks her lips, looks down at her dripping hand, blushes, and quickly wipes it off."
            $ Girl.spunk["hand"] = False
            if Girl == RogueX:
                ch_r "I. . . don't really like the taste of that."
            elif Girl == KittyX:
                ch_k "I'm not into that taste."
            elif Girl == EmmaX:
                ch_e "That certainly is. . . rich. . ."
            elif Girl == LauraX:
                ch_l "That certainly is. . . intense. . ."
            elif Girl == JeanX:
                ch_j "Well that was new. . ."
            elif Girl == StormX:
                ch_s "An uncommon flavor. . ."

            $ Girl.addiction_rate += 1
            if "addictive" in Player.traits:
                $ Girl.addiction_rate += 1
            $ Girl.change_face()
            jump Girl_Orgasm_After
        elif (Girl.addiction >= 50 and action_context != "warn") or Girl == JubesX:
            $ Girl.change_face("sexy")
            $ Girl.mouth = "tongue"
            $ Girl.spunk["mouth"] = True
            Girl.voice ". . ."
            $ Girl.spunk["mouth"] = False
            $ Girl.spunk["chin"] = True
            $ Girl.spunk["hand"] = True
            $ action_speed = 0
            "She gags and spits it into her palm. Then she licks her lips, looks down, and drinks up what's in her palm."
            $ Girl.spunk["hand"] = False
            if Girl == RogueX:
                ch_r "I would be mad, but you taste so sweet, [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "You coulda warned me."
            elif Girl == EmmaX:
                ch_e "I shouldn't reward such rude behavior. . . but it was nourishing."
            elif Girl == LauraX:
                ch_l "I should be mad, but. . ."
            elif Girl == JeanX:
                ch_j "Well that was new. . ."
            elif Girl == StormX:
                ch_s "An uncommon flavor. . ."
            elif Girl == JubesX:
                $ Girl.eyes = "closed"
                ch_v "Mmmmmmmm. . ."
                $ Girl.eyes = "surprised"
                ch_v "Wow! . . that's. . . incredible. . ."
                $ Girl.eyes = "squint"
                ch_v "Ok. . ."
            $ Girl.change_face()
            call change_Girl_stat(Girl, "inhibition", 2)
            call change_Girl_stat(Girl, "inhibition", 2)
        else:

            if approval_check(Girl, 800, "LI") and approval_check(Girl, 400, "OI"):
                $ Girl.change_face("angry")
                $ Girl.spunk["mouth"] = True
            else:
                $ Girl.change_face("bemused")
                $ Girl.mouth = "tongue"
                $ Girl.spunk["mouth"] = True
            $ Girl.spunk["chin"] = True
            Girl.voice ". . ."
            $ Girl.spunk["hand"] = True
            $ action_speed = 0
            "She gags and spits it into her palm."
            if action_context != "warn":
                if Girl == RogueX:
                    ch_r "Hey, who said you could come in my mouth, [Girl.player_petname]?"
                elif Girl == KittyX:
                    ch_k "Hey[Girl.like]what gives?"
                elif Girl == EmmaX:
                    ch_e "Did I say you could come in my mouth, [Girl.player_petname]?"
                elif Girl == LauraX:
                    ch_l "What's the deal just cumming in my mouth like that?"
                elif Girl == JeanX:
                    ch_j "Hey! Gimme a warning next time!"
                elif Girl == StormX:
                    ch_s "[Girl.player_petname], it is inconsiderate to not warn a girl. . ."
            else:
                Girl.voice "Wha?"
            menu:
                extend ""
                "Sorry about that.":
                    call change_Girl_stat(Girl, "love", 1)
                    $ Girl.addiction_rate += 1
                    if "addictive" in Player.traits:
                        $ Girl.addiction_rate += 1
                    $ Girl.change_face("smile", 1)
                    if action_context != "warn":
                        if Girl == RogueX:
                            ch_r "Aw, well a little warning wouldn't hurt, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Well, just[Girl.like]now I know, I guess?"
                        elif Girl == EmmaX:
                            ch_e "Very well. . ."
                            ch_e "Just warn me next time. . ."
                        elif Girl == LauraX:
                            ch_l "Fine. . ."
                            ch_l "Just warn me next time. . ."
                        elif Girl == JeanX:
                            ch_j "Ok then."
                            ch_j "Don't let it happen again."
                        elif Girl == StormX:
                            ch_s "Just do better next time. . ."
                    else:
                        Girl.voice ". . . fine."
                    jump Girl_Orgasm_After
                "Why don't you try swallowing it?":

                    if approval_check(Girl, 1200):
                        "She tentatively licks her hand, and then gulps it down."
                        $ Girl.spunk["hand"] = False
                        $ Girl.change_face("sexy", 1)
                        $ Girl.spunk["mouth"] = True
                        $ Girl.spunk["chin"] = True
                        if Girl == RogueX:
                            ch_r "Hmm, that really wasn't half bad, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Hmm. . . creamy? . ."
                        elif Girl == EmmaX:
                            ch_e "Well, that was a bit of an acquired taste. . ."
                        elif Girl == LauraX:
                            ch_l "Wasn't that bad. . ."
                        elif Girl == JeanX:
                            ch_j "Hmmm. . . robust. . ."
                        elif Girl == StormX:
                            ch_s "That is. . . uncommon. . ."
                        call change_Girl_stat(Girl, "obedience", 10])
                        $ Girl.spunk["mouth"] = False
                    elif approval_check(Girl, 1200, "OI", Bonus = (Girl.addiction*10)):
                        $ Girl.change_face("bemused", 1)
                        $ Girl.brows = "normal"
                        $ Girl.mouth = "sad"
                        $ Girl.spunk["hand"] = False
                        $ Girl.spunk["mouth"] = True
                        $ Girl.spunk["chin"] = True
                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                        $ Girl.spunk["mouth"] = False
                        if Girl == RogueX:
                            ch_r "I'm not really a fan of that, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "It's. . . not terrible."
                        elif Girl == EmmaX:
                            ch_e "I can't say that it would be my favorite flavor. . ."
                        elif Girl == LauraX:
                            ch_l "Not my favorite flavor. . ."
                        elif Girl == JeanX:
                            ch_j "Eh. . . could be worse."
                        elif Girl == StormX:
                            ch_s "That was. . . fine. . ."
                        call change_Girl_stat(Girl, "obedience", 10])
                    else:
                        $ Girl.spunk["hand"] = False
                        "She scowls at you and wipes her hand off. Then she licks her lips."
                        jump Girl_Orgasm_After
                "Swallow it, now.":

                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    if approval_check(Girl, 1200, "OI") or Girl.addiction >= 50:
                        $ Girl.change_face("sad", 1)
                        $ Girl.spunk["mouth"] = True
                        $ Girl.spunk["chin"] = True
                        $ Girl.spunk["hand"] = False
                        "She scowls a bit, but licks her hand clean as she does so, and swallows it down."
                        $ Girl.spunk["mouth"] = False
                        if Girl == RogueX:
                            ch_r "I'm not really a fan of that, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "That's. . . not awful."
                        elif Girl == EmmaX:
                            ch_e "I can't say that it would be my favorite flavor. . ."
                        elif Girl == LauraX:
                            ch_l "Not my favorite flavor. . ."
                        elif Girl == JeanX:
                            ch_j "Eh. . . could be worse."
                        elif Girl == StormX:
                            ch_s "That is. . . fine. . ."
                        call change_Girl_stat(Girl, "obedience", 10])
                    else:
                        $ Girl.spunk["hand"] = False
                        "She scowls at you and wipes her hand off. Then she licks her lips."
                        jump Girl_Orgasm_After

        jump Girl_Swallowed


    $ action_context = None
    "You ask if you can cum in her mouth."
    if renpy.showing(Girl.tag + "PJ_Animation"):
        call kiss_launch(Girl)
    elif renpy.showing(Girl.tag + " doggy") or renpy.showing(Girl.tag + " sex"):
        call show_handjob(Girl, orgasm = True)

    if "full" in Girl.recent_history:
        pass

    elif Girl.permanent_History["swallowed"] >= 5 or "hungry" in Girl.traits:

        $ Girl.change_face("sucking")
        if not renpy.showing(Girl.tag + " blowjob"):
            call show_blowjob(Girl, orgasm = True)
            $ action_speed = 2
            "She nods and bends down to put the tip between her lips."
        else:
            $ action_speed = 2
            "She nods and hums a \"yes\" sound."
        $ Player.spunk = 1
        $ Girl.spunk["mouth"] = True
        $ Girl.spunk["chin"] = True
        Girl.voice ". . ."
        "After you cum, she quickly gulps it down and wipes her mouth."
        $ Girl.change_face("sexy")
        $ action_speed = 0
        call Sex_Basic_Dialog (Girl, "swallowgood")
        $ Girl.spunk["mouth"] = False
        jump Girl_Swallowed

    elif Girl.addiction >= 80 and Girl.permanent_History["swallowed"]:

        $ Girl.brows = "confused"
        $ Girl.eyes = "manic"
        if not renpy.showing(Girl.tag + " blowjob"):
            call show_blowjob(Girl, orgasm = True)
            $ action_speed = 2
            "She looks a bit quizzical, but gently puts the tip to her lips, just as you blow."
        else:
            $ action_speed = 2
            "She nods and hums a \"yes\" sound."
        $ Girl.mouth = "sucking"
        $ Player.spunk = 1
        $ Girl.spunk["mouth"] = True
        Girl.voice ". . ."
        $ action_speed = 0
        "She gags a little, but quickly swallows it."
        $ Girl.change_face("sexy")
        $ Girl.mouth = "smile"
        call Sex_Basic_Dialog (Girl, "swallow2")
        call Sex_Basic_Dialog (Girl, "notwarned")
        $ Girl.spunk["mouth"] = False
        call change_Girl_stat(Girl, "inhibition", 5)
        jump Girl_Swallowed

    elif Girl.permanent_History["swallowed"]:
        if approval_check(Girl, 900):
            $ Girl.brows = "confused"
            if renpy.showing(Girl.tag + " titjob"):
                $ Girl.change_face("kiss")
                $ action_speed = 5
                "She looks a bit confused, but gently puts the tip to her lips."
            elif not renpy.showing(Girl.tag + " blowjob"):
                call show_blowjob(Girl, orgasm = True)
                $ action_speed = 2
                "She looks a bit quizzical, but gently puts the tip to her lips, just as you blow."
            else:
                $ action_speed = 2
                if Girl == KittyX:
                    ch_k "[[mumbled] Huh?"
                else:
                    "She tilts her head and hums a \"huh?\" sound."
            $ Girl.mouth = "sucking"
            $ Girl.spunk["chin"] = True
            $ Girl.spunk["mouth"] = True
            $ Girl.brows = "normal"
            $ Girl.eyes = "sexy"
            $ Player.spunk = 1
            $ Girl.spunk["mouth"] = True
            Girl.voice ". . ."
            "She gags a little, but quickly swallows it."
            $ action_speed = 0
            $ Girl.change_face("sexy")
            call Sex_Basic_Dialog (Girl, "swallow2")
            $ Girl.spunk["mouth"] = False
            jump Girl_Swallowed



    if approval_check(Girl, 300, "LI") or approval_check(Girl, 300, "OI"):
        $ Girl.change_face("bemused")
        $ Girl.eyes = "sexy"
    else:
        $ Girl.change_face("angry")

    $ action_speed = 0

    if Girl == RogueX:
        if "full" in Girl.recent_history:
            ch_r "I'm feeling a bit. . . \"full\" right now, [Girl.player_petname]. . ."
        else:
            ch_r "What makes you think I'd want that, [Girl.player_petname]?"
    elif Girl == KittyX:
        if "full" in Girl.recent_history:
            ch_k "I've kinda had enough for now? . ."
        else:
            ch_k "That doesn't sound too appetizing. . ."
    elif Girl == EmmaX:
        if "full" in Girl.recent_history:
            ch_e "I couldn't finish another drop, [Girl.player_petname]. . ."
        else:
            ch_e "I can't imagine why I would. . ."
    elif Girl == LauraX:
        if "full" in Girl.recent_history:
            ch_l "I'm stuffed, [Girl.player_petname]. . ."
        else:
            ch_l "I don't know why. . ."
    elif Girl == JeanX:
        if "full" in Girl.recent_history:
            ch_j "I'm a bit full, [Girl.player_petname]. . ."
        else:
            ch_j "As if. . ."
    elif Girl == StormX:
        if "full" in Girl.recent_history:
            ch_s "I could not take any more, [Girl.player_petname]. . ."
        else:
            ch_s "I do not see why I would. . ."
    elif Girl == JubesX:
        if "full" in Girl.recent_history:
            ch_v "Even I'm filled up already, [Girl.player_petname]. . ."
        else:
            ch_v "I don't think I would want to. . ."
    menu:
        extend ""
        "Sorry about that.":
            call change_Girl_stat(Girl, "love", 3)
            $ Girl.addiction_rate += 1
            if "addictive" in Player.traits:
                $ Girl.addiction_rate += 1
            $ Girl.change_face("smile", 1)
            if Girl == RogueX:
                ch_r "Well, maybe it would taste as sweet as your words, [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "Can't hurt to ask, right?"
            elif Girl == EmmaX:
                ch_e "It is a tempting offer. . ."
            elif Girl == LauraX:
                ch_l "Hmm. . ."
            elif Girl == JeanX:
                ch_j "Uh-huh. . ."
            elif Girl == StormX:
                ch_s "I appreciate you asking. . ."
            elif Girl == JubesX:
                ch_v "Well, doesn't hurt to ask. . ."
            if approval_check(Girl, 1200, taboo_modifier = 1) and "full" not in Girl.recent_history:
                call change_Girl_stat(Girl, "inhibition", 3)
                call change_Girl_stat(Girl, "inhibition", 2)
                $ Girl.change_face("sexy", 1)
                if Girl == RogueX:
                    ch_r "Maybe it is worth a try. . ."
                elif Girl == KittyX:
                    ch_k "It's[Girl.like]worth a shot."
                elif Girl == EmmaX:
                    ch_e "Perhaps a little bit. . ."
                elif Girl == LauraX:
                    ch_l "Maybe a little. . ."
                elif Girl == JeanX:
                    ch_j "I guess I could. . ."
                elif Girl == StormX:
                    ch_s "I can try."
                elif Girl == JubesX:
                    ch_v "Well, why not, you only live once. . ."
            else:
                jump Girl_Handy_Finish

        "Give it a try, you might like it." if "full" not in Girl.recent_history:
            if approval_check(Girl, 1200, taboo_modifier = 1):
                call change_Girl_stat(Girl, "obedience", 5)
                call change_Girl_stat(Girl, "obedience", 3)
                $ Girl.brows = "confused"
                $ Girl.eyes = "sexy"
                if Girl == RogueX:
                    ch_r "If you say so. . ."
                elif Girl == KittyX:
                    ch_k "I guess. . ."
                elif Girl == EmmaX:
                    ch_e "If you insist. . ."
                elif Girl == LauraX:
                    ch_l "If you insist. . ."
                elif Girl == JeanX:
                    ch_j "I don't know about that. . ."
                elif Girl == StormX:
                    ch_s "I am unsure. . ."
                elif Girl == JubesX:
                    ch_v "I, um. . . Maybe? . ."
            else:
                $ Girl.addiction_rate += 1
                if "addictive" in Player.traits:
                    $ Girl.addiction_rate += 1
                $ Girl.blushing = "_blush1"
                if Girl == RogueX:
                    ch_r "You wish, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "You wish, [Girl.player_petname]."
                elif Girl == EmmaX:
                    ch_e "I highly doubt that, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "You think I don't have a nose, [Girl.player_petname]?"
                elif Girl == JeanX:
                    ch_j "Yeah, haven't heard that one before. . ."
                elif Girl == StormX:
                    ch_s "That is. . . unlikely. . ."
                elif Girl == JubesX:
                    ch_v "I, um. . . kinda doubt that. . ."
                jump Girl_Handy_Finish
        "Seriously, put it in your mouth.":

            if approval_check(Girl, 1500, "LI", taboo_modifier = 1) or approval_check(Girl, 1200, "OI", taboo_modifier = 1):
                $ Girl.change_face("sucking", 1)
            elif approval_check(Girl, 1000, "OI", Bonus = (Girl.addiction*10)):
                $ Girl.change_face("angry", 1)
            else:

                $ Girl.change_face("angry", 1)
                "She scowls at you, drops you cock and pulls back."
                call show_handjob(Girl, orgasm = True)
                call show_full_body(Girl)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 1)
                if Girl == RogueX:
                    ch_r "Well if that's your attitude you can handle your own business."
                elif Girl == KittyX:
                    ch_k "You can handle it yourself then."
                elif Girl == EmmaX:
                    ch_e "I think you overestimate your charms."
                elif Girl == LauraX:
                    ch_l "Seriously, you eat a dick."
                elif Girl == JeanX:
                    ch_j "Fuck off."
                elif Girl == StormX:
                    ch_s "No."
                elif Girl == JubesX:
                    ch_v "I don't need this. . ."
                call change_Girl_stat(Girl, "obedience", 900,3])
                call change_Girl_stat(Girl, "obedience", 1)
                $ Girl.recent_history.append("angry")
                $ Girl.daily_history.append("angry")
                $ line = 0
                return
            call change_Girl_stat(Girl, "obedience", 10])
            call change_Girl_stat(Girl, "obedience", 5)

    if not renpy.showing(Girl.tag + " blowjob"):
        call show_blowjob(Girl, orgasm = True)
    $ action_speed = 2
    if approval_check(Girl, 1200):
        "She gently puts the tip to her lips, just as you blow."
    else:
        "She tentatively places the tip in her mouth, and you blast inside it."
        $ Girl.change_face("sexy")
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)
    $ Girl.mouth = "sucking"
    $ Player.spunk = 1
    $ Girl.spunk["chin"] = True
    $ Girl.spunk["mouth"] = True
    Girl.voice ". . ."
    "She gags a little, but quickly swallows it."
    $ action_speed = 0
    $ Girl.change_face("sexy")

    if approval_check(Girl, 1000) and Girl.permanent_History["swallowed"] >= 3:
        call Sex_Basic_Dialog (Girl, "swallow2")
    elif approval_check(Girl, 800):
        call Sex_Basic_Dialog (Girl, "swallowfirst")
    else:
        $ Girl.change_face("sad")
        call Sex_Basic_Dialog (Girl, "swallowfirst")
    call change_Girl_stat(Girl, "inhibition", 3)
    call change_Girl_stat(Girl, "inhibition", 2)
    $ Girl.permanent_History["blowjob"] += 1
    jump Girl_Swallowed

label Girl_Creampie_P:
    if Player.primary_Action == "sex" and action_context == "auto":
        $ Player.primary_Action.type = "sex"
        $ Girl.spunk["pussy"] = True
        $ Player.spunk = "in"
        $ action_speed = 0
        if approval_check(Girl, 1300) or Girl.permanent_History["creampied"]:
            $ Girl.change_face("surprised")
            "You come in her pussy. Her eyes widen in surprise, but she takes it in stride."
            $ Girl.change_face("sexy")
            if Girl.lust >= 85:
                call Girl_Cumming (Girl)
        else:
            if Girl.lust >= 85:
                "You come in her pussy. Her eyes widen in surprise and she shakes a bit."
                call Girl_Cumming (Girl)
            else:
                "You come in her pussy. Her eyes widen in surprise and she pulls out."
            $ Player.primary_Action.type = "out"
            $ Girl.change_face("angry")
            if Girl == RogueX:
                ch_r "Hey, a little warning next time, huh?"
                $ Girl.change_face("bemused")
                ch_r "Still, that didn't feel {i}so{/i} bad. . ."
            elif Girl == KittyX:
                ch_k "You coulda[Girl.like]warned me or something!"
                $ Girl.change_face("bemused")
                ch_k "It was pretty warm though. . ."
            elif Girl == EmmaX:
                ch_e "Perhaps some warning next time?"
                $ Girl.change_face("bemused")
                ch_e "Not that it didn't feel good at the time. . ."
            elif Girl == LauraX:
                ch_l "Hey, maybe a heads up?"
                $ Girl.change_face("bemused")
                ch_l "Not that it didn't feel good. . ."
            elif Girl == JeanX:
                ch_j "Hey! What was that!"
                ch_j ". . ."
                $ Girl.change_face("bemused")
                ch_j "But it did feel kinda good. . ."
            elif Girl == StormX:
                ch_s "You could have warned me you would do that. . ."
                $ Girl.change_face("bemused")
                ch_s "It did feel amazing though. . ."
            elif Girl == JubesX:
                ch_v "I coulda used a little warning there!"
                $ Girl.change_face("bemused")
                ch_v "So warm inside. . ."
        jump Girl_Creampied


    if approval_check(Girl, 1200) or Girl.permanent_History["creampied"]:
        $ Girl.change_face("sexy")
        if Girl.permanent_History["creampied"] >= 3:
            "She smiles and speeds up her actions, causing you to erupt inside her."
        elif Girl.permanent_History["creampied"]:
            "She gets a mischievous look and speeds up, you burst inside her."
        else:
            "As you continue to pound her, she nods her head."
        $ Player.primary_Action.type = "sex"
        $ Girl.spunk["pussy"] = True
        $ Player.spunk = "in"
        $ action_speed = 0
        if Girl.lust >= 85:
            call Girl_Cumming (Girl)
        call change_Girl_stat(Girl, "love", 1)
        if Girl == RogueX:
            ch_r "Hmm, you know how to fill me up {i}right.{/i}"
        elif Girl == KittyX:
            ch_k "Hmm, cozy. . ."
        elif Girl == EmmaX:
            ch_e "How very. . . filling."
        elif Girl == LauraX:
            ch_l "Very. . . filling."
        elif Girl == JeanX:
            ch_j "Very. . . warm."
        elif Girl == StormX:
            ch_s "So pleasantly warm. . ."
        elif Girl == JubesX:
            ch_v "So warm inside. . ."
        jump Girl_Creampied
    else:
        $ Girl.change_face("sexy")
        call change_Girl_stat(Girl, "love", 2)
        call change_Girl_stat(Girl, "love", 2)
        if Girl == RogueX:
            ch_r "Thanks for the heads up *grunt* [Girl.player_petname], but I'd rather you didn't."
        elif Girl == KittyX:
            ch_k "Thanks for the warning, but maybe not this time?"
        elif Girl == EmmaX:
            ch_e "Thanks for warning me *grunt* [Girl.player_petname], but perhaps not."
        elif Girl == LauraX:
            ch_l "Thanks for the heads up *grunt* [Girl.player_petname], but let's not."
        elif Girl == JeanX:
            ch_j "Yeah, let's not, time to pull out."
        elif Girl == StormX:
            ch_s "Thank you, [Girl.player_petname], but no. . ."
        elif Girl == JubesX:
            ch_v "It could be nice, but no thanks. . ."
    jump Girl_Cum_Outside

label Girl_Creampie_A:

    if Player.primary_Action == "anal" and action_context == "auto":
        $ Player.primary_Action.type = "anal"
        $ Girl.spunk["anus"] = True
        $ Player.spunk = "anal"
        $ action_speed = 0
        if approval_check(Girl, 1200) or Girl.permanent_History["creampied"]:
            $ Girl.change_face("surprised", 1)
            "You come in her ass. Her eyes widen in surprise, but she takes it in stride."
            $ Girl.change_face("sexy")
            if Girl.lust >= 85:
                call Girl_Cumming (Girl)
        else:
            if Girl.lust >= 85:
                "You come in her ass. Her eyes widen in surprise and she shakes a bit."
                call Girl_Cumming (Girl)
            else:
                "You come in her ass. Her eyes widen in surprise and she pulls out."
            $ Player.primary_Action.type = "out"
            $ Girl.change_face("angry")
            if Girl == RogueX:
                ch_r "Hey, warn a girl, huh?"
                $ Girl.change_face("bemused")
                ch_r "but. . . I guess it did feel pretty good. . ."
            elif Girl == KittyX:
                ch_k "Maybe a little warning next time?"
                $ Girl.change_face("bemused")
                ch_k "that was pretty warm though. . ."
            elif Girl == EmmaX:
                ch_e "No advanced warning, [Girl.player_petname]?"
                $ Girl.change_face("bemused")
                ch_e "I suppose it was rather. . . filling though."
            elif Girl == LauraX:
                ch_l "No advanced warning, [Girl.player_petname]?"
                $ Girl.change_face("bemused")
                ch_l "That was pretty filling. . ."
            elif Girl == JeanX:
                ch_j "Hey! What was that!"
                ch_j ". . ."
                $ Girl.change_face("bemused")
                ch_j "But it did feel kinda good. . ."
            elif Girl == StormX:
                ch_s "You could have warned me you would do that. . ."
                $ Girl.change_face("bemused")
                ch_s "It did feel amazing though. . ."
            elif Girl == JubesX:
                ch_v "I coulda used a little warning there!"
                $ Girl.change_face("bemused")
                ch_v "So warm inside. . ."
        jump Girl_Creampied


    if approval_check(Girl, 1200) or Girl.permanent_History["creampied"]:
        $ Girl.change_face("sexy")
        if Girl.permanent_History["creampied"] >= 3:
            "She smiles and speeds up her actions, causing you to erupt inside her."
        elif Girl.permanent_History["creampied"]:
            "She gets a mischievous look and speeds up, you burst inside her."
        else:
            "As you continue to pound her, she nods her head."
        $ Player.primary_Action.type = "anal"
        $ Girl.spunk["anus"] = True
        $ Player.spunk = "anal"
        $ action_speed = 0
        if Girl.lust >= 85:
            call Girl_Cumming (Girl)
        call change_Girl_stat(Girl, "love", 1)
        if Girl == RogueX:
            ch_r "Hmm, I feel so full. . ."
        elif Girl == KittyX:
            ch_k "Wow, I feel so full. . ."
        elif Girl == EmmaX:
            ch_e "Mmmm, I feel so full. . ."
        elif Girl == LauraX:
            ch_l "Mmmm, so full. . ."
        elif Girl == JeanX:
            ch_j "Very. . . warm."
        elif Girl == StormX:
            ch_s "So pleasantly warm. . ."
        elif Girl == JubesX:
            ch_v "So warm inside. . ."
        jump Girl_Creampied
    else:
        $ Girl.change_face("sexy")
        call change_Girl_stat(Girl, "love", 2)
        if Girl == RogueX:
            ch_r "Thanks for the heads up *grunt* [Girl.player_petname], but I'd rather you didn't."
        elif Girl == KittyX:
            ch_k "Thanks for the warning, but maybe not this time?"
        elif Girl == EmmaX:
            ch_e "Thanks for warning me *grunt* [Girl.player_petname], but perhaps not."
        elif Girl == LauraX:
            ch_l "Thanks for warning me *grunt* [Girl.player_petname], but I don't think so."
        elif Girl == JeanX:
            ch_j "Yeah, let's not, time to pull out."
        elif Girl == StormX:
            ch_s "Thank you, [Girl.player_petname], but no. . ."
        elif Girl == JubesX:
            ch_v "It could be nice, but no thanks. . ."
    jump Girl_Cum_Outside


label Girl_Facial:
    if renpy.showing(Girl.tag + " blowjob"):
        if Girl.addiction >= 60 and approval_check(Girl, 1000, "I", Bonus = ((Girl.addiction*10)- Girl.obedience)) and Girl.permanent_History["swallowed"]:
            jump Manic_Suck
        call show_handjob(Girl, orgasm = True)
        $ action_speed = 2
        if Girl.spunk["hair"]:
            pass
        elif Girl.spunk["face"]:
            $ Girl.spunk["hair"] = True
        else:
            $ Girl.spunk["face"] = True
        "You pull out of her mouth with a pop, and she strokes you off. You spray all over her face."
        $ action_speed = 0

    elif renpy.showing(Girl.tag + " titjob"):
        if Girl.spunk["hair"]:
            pass
        elif Girl.spunk["face"]:
            $ Girl.spunk["hair"] = True
        else:
            $ Girl.spunk["face"] = True
        if not Girl.permanent_History["titjob"]:
            "She glances up but continues to rub her breasts up and down on your cock. When you come, you spray all over her face."
        else:
            "As you're about to finish, you aim squarely at her face, and spray all over it."
        $ action_speed = 0

    elif renpy.showing(Girl.tag + " handjob"):
        if Girl.spunk["hair"]:
            pass
        elif Girl.spunk["face"]:
            $ Girl.spunk["hair"] = True
        else:
            $ Girl.spunk["face"] = True
        if not Girl.permanent_History["handjob"]:
            "She looks a bit confused but continues to stroke while staring at it like a live snake. When you finish, you spray all over her face."
        else:
            "As you're about to finish, you aim squarely at her face, and spray all over it."
        $ action_speed = 0
    elif renpy.showing(Girl.tag + "PJ_Animation"):
        call breasts_launch(Girl)
        if Girl.spunk["hair"]:
            pass
        elif Girl.spunk["face"]:
            $ Girl.spunk["hair"] = True
        else:
            $ Girl.spunk["face"] = True
        "As you're about to finish, you aim squarely at her face, and spray all over it."
        $ action_speed = 0
    else:
        call show_handjob(Girl, orgasm = True)
        $ action_speed = 2
        if Girl.spunk["hair"]:
            pass
        elif Girl.spunk["face"]:
            $ Girl.spunk["hair"] = True
        else:
            $ Girl.spunk["face"] = True
        "As you're about to finish, you pull out, aim squarely at her face, and spray all over it."
        $ action_speed = 0
    if Girl == RogueX:
        if action_context == "warn":
            ch_r "Thanks for the warning, [Girl.player_petname]. Such a mess though. . ."
        else:
            ch_r "What a mess, you could have warned me."
    elif Girl == KittyX:
        if action_context == "warn":
            ch_k "Whew, thanks for the head's up."
        else:
            ch_k "Huh, nice warning there, [Girl.player_petname]."
    elif Girl == EmmaX:
        if action_context == "warn":
            ch_e "I appreciate the warning. . . perhaps not the mess though. . ."
        else:
            ch_e "What a mess, a warning would have been appreciated."
    elif Girl == LauraX:
        if action_context == "warn":
            ch_l "Thanks for the warning. . . maybe not the mess though. . ."
        else:
            ch_l "What a mess, maybe a heads up next time?"
    elif Girl == JeanX:
        if action_context == "warn":
            ch_j "Wow, you really made a mess there. . ."
        else:
            ch_j "Hey, a little warning?"
    elif Girl == StormX:
        if action_context == "warn":
            ch_s "Thank you for the warning, for what little good it did. . ."
        else:
            ch_s "Well this is a fine mess you have gotten me into."
    elif Girl == JubesX:
        if action_context == "warn":
            ch_v "Ugh, I've been slimed. . ."
        else:
            ch_v "Ugh, I've been slimed. . . warn me next time, uh?"
    $ Player.primary_Action.type = "out"
    jump Girl_Orgasm_After


label Girl_TitSpunk:
    if renpy.showing(Girl.tag + " blowjob"):
        if Girl.addiction >= 60 and approval_check(Girl, 1000, "I", Bonus = ((Girl.addiction*10)- Girl.obedience)) and Girl.permanent_History["swallowed"]:
            jump Manic_Suck


    if renpy.showing(Girl.tag + "PJ_Animation"):
        call breasts_launch(Girl)
    elif not renpy.showing(Girl.tag + " titjob") and not renpy.showing(Girl.tag + " handjob") and not renpy.showing(Girl.tag + " blowjob"):
        call show_handjob(Girl, orgasm = True)
    $ Girl.spunk["breasts"] = True
    $ action_speed = 0
    "As you're about to finish, you speed up and spray all over her chest."
    if Girl == RogueX:
        if action_context == "warn":
            ch_r "Thanks for the warning, [Girl.player_petname]. Such a mess though. . ."
        else:
            ch_r "What a mess, you could have warned me."
    elif Girl == KittyX:
        if action_context == "warn":
            ch_k "Whew, thanks for the head's up."
        else:
            ch_k "Huh, nice warning there, [Girl.player_petname]."
    elif Girl == EmmaX:
        if action_context == "warn":
            ch_e "I appreciate the warning. . . perhaps not the mess though. . ."
        else:
            ch_e "What a mess, a warning would have been appreciated."
    elif Girl == LauraX:
        if action_context == "warn":
            ch_l "Thanks for the warning. . . maybe not the mess though. . ."
        else:
            ch_l "What a mess, maybe a heads up next time?"
    elif Girl == JeanX:
        if action_context == "warn":
            ch_j "Wow, you really made a mess there. . ."
        else:
            ch_j "Hey, a little warning?"
    elif Girl == StormX:
        if action_context == "warn":
            ch_s "Thank you for the warning, for what little good it did. . ."
        else:
            ch_s "Well this is a fine mess you have gotten me into."
    elif Girl == JubesX:
        if action_context == "warn":
            ch_v "Ugh, I've been slimed. . ."
        else:
            ch_v "Ugh, I've been slimed. . . warn me next time, uh?"
    jump Girl_Orgasm_After


label Girl_Cum_Outside:
    if Player.primary_Action != "footjob":
        if renpy.showing(Girl.tag + "PJ_Animation"):
            call middle_launch(Girl)

        elif Girl.pose != "doggy" and (Girl == JeanX or Girl == StormX):
            call middle_launch(Girl)
        else:



            call show_sex(Girl, "hotdog")
    $ action_speed = 0
    if Girl.addiction >= 60 and approval_check(Girl, 1000, "I", Bonus = ((Girl.addiction*10)- Girl.obedience))  and Girl.permanent_History["swallowed"]:
        $ Girl.eyes = "manic"
        $ Girl.blushing = "_blush1"
        call show_blowjob(Girl, orgasm = True)
        if Player.primary_Action == "sex":
            "You pull out of her pussy with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
        elif Player.primary_Action == "anal":
            "You pull out of her ass with a pop, and her eyes widen in surprise. She leaps at your cock and sucks it deep, draining your fluids hungrily."
        $ Girl.mouth = "lipbite"
        $ Girl.spunk["mouth"] = True
        "When she finishes, she licks her lips."
        $ Girl.change_face("bemused")
        $ Girl.spunk["mouth"] = False
        if Girl == RogueX:
            ch_r "Well, [Girl.player_petname], I just couldn't let that go to waste."
        elif Girl == KittyX:
            ch_k "Sorry, that's just[Girl.like]sooooo good."
        elif Girl == EmmaX:
            ch_e "Well, [Girl.player_petname], I just couldn't let that go to waste."
        elif Girl == LauraX:
            ch_l "I couldn't let that go to waste."
        elif Girl == JeanX:
            ch_j "Mmm. . ."
        elif Girl == StormX:
            ch_s "That would have been wasteful. . ."
        elif Girl == JubesX:
            ch_v "Wouldn't want to let all that go to waste. . ."
        call change_Girl_stat(Girl, "obedience", -5)
        call change_Girl_stat(Girl, "inhibition", 10)
        jump Girl_Swallowed
    if Player.primary_Action != "footjob":
        $ Player.primary_Action.type = "out"
    if Girl.pose == "doggy":
        $ Girl.spunk["back"] = True
        if Player.primary_Action == "sex":
            "You pull out of her pussy with a pop and spray all over her backside."
        elif Player.primary_Action == "anal":
            "You pull out of her ass with a pop and spray all over her backside."
        else:
            "You pick up the pace and with a grunt you spray all over her backside."
    else:
        $ Girl.spunk["belly"] = True
        if Player.primary_Action == "sex":
            "You pull out of her pussy with a pop and spray all over her stomach."
        elif Player.primary_Action == "anal":
            "You pull out of her ass with a pop and spray all over her stomach."
        else:
            "You pick up the pace and with a grunt you spray all over her stomach."


    if Girl.addiction >= 60 and approval_check(Girl, 800, "I", Bonus = ((Girl.addiction*10)- Girl.obedience)) and Girl.permanent_History["swallowed"]:

        $ Girl.eyes = "manic"
        $ Girl.blushing = "_blush1"
        "[Girl.name]'s eyes widen with desire, and she quickly wipes a bit off with her hand, then licks her fingers clean."
        $ Girl.change_face("manic", 1)
        $ Girl.spunk["mouth"] = True
        $ Girl.mouth = "smile"
        if Girl == RogueX:
            ch_r "Well, [Girl.player_petname], I just couldn't let that go to waste."
        elif Girl == KittyX:
            ch_k "Sorry, that's just[Girl.like]sooooo good."
        elif Girl == EmmaX:
            ch_e "Well, [Girl.player_petname], I just couldn't let that go to waste."
        elif Girl == LauraX:
            ch_l "I couldn't let that go to waste."
        elif Girl == JeanX:
            ch_j "Mmm. . ."
        elif Girl == StormX:
            ch_s "That would have been wasteful. . ."
        elif Girl == JubesX:
            ch_v "Wouldn't want to let all that go to waste. . ."
        $ Girl.spunk["mouth"] = False
        call change_Girl_stat(Girl, "inhibition", 3)
        jump Girl_Swallowed



    $ Girl.change_face("sexy", 1)
    if Girl == RogueX:
        ch_r "What a mess. . ."
    elif Girl == KittyX:
        ch_k "Mmmm, all over the place. . ."
    elif Girl == EmmaX:
        ch_e "Hmm. . . you do make a mess. . ."
    elif Girl == LauraX:
        ch_l "Hmm. . . what a mess. . ."
    elif Girl == JeanX:
        ch_j "Ick. . ."
    elif Girl == StormX:
        ch_s "Well this is a fine mess you have gotten me into."
    elif Girl == JubesX:
        ch_v "Ugh, I've been slimed. . ."

    jump Girl_Orgasm_After




label Girl_Handy_Finish:
    if renpy.showing(Girl.tag + " doggy") or renpy.showing(Girl.tag + " sex"):
        call show_full_body(Girl)
        if Player.primary_Action == "hotdog":
            "She bends down and begins to stroke you off."
        else:
            "She grins and pulls out with a pop, and begins to stroke you off."
        $ action_speed = 2
    elif renpy.showing(Girl.tag + " blowjob"):
        call show_handjob(Girl, orgasm = True)
        $ action_speed = 2
        "She slides her lips off your cock, and begins to stroke you off."
    elif renpy.showing(Girl.tag + "PJ_Animation"):
        call breasts_launch(Girl)
    else:
        call show_handjob(Girl, orgasm = True)
        $ action_speed = 2
    $ Girl.spunk["hand"] = True
    "She grins and speeds up her efforts, placing her left hand over your tip. You burst all over her hands."
    $ action_speed = 0

    if Girl.addiction > 80 or "hungry" in Girl.traits:
        $ Girl.eyes = "manic"
        $ Girl.spunk["hand"] = False
        $ Girl.spunk["mouth"] = True
        $ Girl.mouth = "smile"
        "She licks her hands off with a satisfied grin."
        $ Girl.spunk["mouth"] = False
        Girl.voice "Hmmm. . ."
    else:
        $ Girl.change_face("bemused")
        $ Girl.spunk["hand"] = False
        "She wipes her hands off, but takes a quick sniff when she's done and smiles."
        call Sex_Basic_Dialog (Girl, "warned")
        jump Girl_Orgasm_After



label Girl_Swallowed:
    $ Girl.permanent_History["swallowed"] += 1
    call change_Girl_stat(Girl, "inhibition", 3)
    $ Girl.addiction -= 20
    if Girl.spunk["mouth"]:
        $ Girl.spunk["mouth"] = False
    if "full" not in Girl.recent_history and Girl.recent_history.count("swallowed") >= 5:
        $ Girl.recent_history.append("full")
        $ Girl.change_face("surprised", 1)
        if Girl == RogueX:
            ch_r "-buurp-"
            $ Girl.change_face("sexy", 1)
            ch_r "S'cuse me [Girl.player_petname], must have been something I ate."
        elif Girl == KittyX:
            ch_k "-buurp-"
            $ Girl.change_face("sexy", 1)
            ch_k "I. . . might have to cut back a bit."
        elif Girl == EmmaX:
            ch_e "-ehem-"
            $ Girl.change_face("sexy", 1)
            ch_e "Excuse me [Girl.player_petname], I had a full lunch."
        elif Girl == LauraX:
            ch_l "-buurp-"
            $ Girl.change_face("sexy", 1)
            ch_l "Oof [Girl.player_petname], must'a been something I ate."
        elif Girl == JeanX:
            $ Girl.blushing = "_blush2"
            ch_j "-buurp-"
            if approval_check(Girl, 600, "L"):
                $ Girl.change_face("sexy", 1)
                ch_j "Heh. . . kinda full. . ."
            else:
                $ Girl.change_face("bemused", 1, eyes = "side")
                call change_Girl_stat(Girl, "obedience", 3)
                ch_j "Um, you didn't hear that. . ."
        elif Girl == StormX:
            ch_s "-buurp-"
            $ Girl.change_face("sexy", 1)
            ch_s "Oh, [Girl.player_petname], I must have had enough. . ."
        elif Girl == JubesX:
            ch_v "-cough-"
            $ Girl.change_face("sexy", 1)
            ch_v "Whew, I think maybe I've had more than I can take. . ."
    $ Girl.recent_history.append("swallowed")
    $ Girl.daily_history.append("swallowed")
    $ Girl.addiction_rate += 2
    if "addictive" in Player.traits:
        $ Girl.addiction_rate += 2
    if Player.primary_Action == "anal":
        call change_Girl_stat(Girl, "obedience", 2)
        call change_Girl_stat(Girl, "obedience", 2)
    if Girl.permanent_History["swallowed"] == 1:
        $ Girl.SEXP += 12
        call change_Girl_stat(Girl, "inhibition", 5)
    jump Girl_Orgasm_After


label Girl_Creampied:
    if Player.primary_Action == "sex":
        $ Girl.permanent_History["creampied"] += 1
        call change_Girl_stat(Girl, "lust", 10)
        $ Girl.recent_history.append("creampie sex")
        $ Girl.daily_history.append("creampie sex")
    elif Player.primary_Action == "anal":
        $ Girl.permanent_History["anal_creampied"] += 1
        call change_Girl_stat(Girl, "lust", 5)
        $ Girl.recent_history.append("creampie anal")
        $ Girl.daily_history.append("creampie anal")
    call change_Girl_stat(Girl, "inhibition", 3)
    $ Girl.addiction -= 30
    $ Girl.addiction_rate += 2
    if "addictive" in Player.traits:
        $ Girl.addiction_rate += 3
    if Girl.permanent_History["creampied"] == 1:
        $ Girl.SEXP += 10
        call change_Girl_stat(Girl, "inhibition", 5)



label Girl_Orgasm_After:
    $ line = "What next?"
    if not renpy.showing(Girl.tag + " handjob"):
        $ Girl.arm_pose = 1
    $ Player.semen -= 1
    $ Player.climax = 0
    $ action_speed = 0
    $ Girl.thirst -= 10 if Girl.thirst > 50 else 5
    menu:
        "Want [Girl.name] to clean you off?"
        "Yes":
            call Girl_CleanCock(Girl)
        "Actually, let [Partner.name] do it." if Partner in all_Girls:
            $ shift_focus (Partner)
            call show_full_body(Partner)
            call Girl_CleanCock (Player.focused_Girl)

            $ shift_focus (Partner)
            call show_full_body(Partner)

            "[Partner.name] Steps back."

            call show_full_body(Girl)
        "No":
            pass
    if Girl.spunk:
        call Girl_Cleanup (Girl)
    $ action_context = None
    return

label Girl_CleanCock(Girl):
    $ line = "What next?"
    if not renpy.showing(Girl.tag + " handjob"):
        $ Girl.arm_pose = 1
    $ Player.primary_Action.type = "out"
    $ action_speed = 0
    if Player.primary_Action == "anal" and not approval_check(Girl, 1600, taboo_modifier = 1) and not Girl.addiction >= 80:
        if Girl == JeanX:
            $ Girl.change_face("sly", 1, eyes = "psychic")
            "You feel a slight breeze and the juices swirl off your cock and onto the floor."
            $ Girl.change_face("sly", 0)
        else:
            "She wipes your cock clean."
    elif Girl.permanent_History["blowjob"] > 3 or Girl.permanent_History["swallowed"]:
        if approval_check(Girl, 1200, taboo_modifier = 1) or Girl.addiction >= 60:
            call show_blowjob(Girl, orgasm = True)
            $ action_speed = 1
            $ Girl.change_face("sucking", 1)
            if approval_check(Girl, 1500, taboo_modifier = 1):
                if Partner and approval_check(Partner, 1500, taboo_modifier = 1):
                    "Both girls look up at you as they lick your cock clean."
                elif Girl.love > Girl.inhibition and Girl.love > Girl.obedience:
                    "She looks up at you lovingly as she licks your cock clean."
                elif Girl.obedience > Girl.inhibition:
                    $ Girl.eyes = "side"
                    "She dutifully licks your cock clean with lowered eyes."
                    call change_Girl_stat(Girl, "obedience", 3)
                else:
                    "She happily licks your cock clean."
            elif Girl.addiction >= 60:
                "She hungrily and thoroughly licks your cock clean."
            else:
                "She licks you cock clean."
            $ Girl.change_face("sexy")
        else:
            if not renpy.showing(Girl.tag + " handjob"):
                call show_handjob(Girl, orgasm = True)
            if Partner and approval_check(Partner, 1000, taboo_modifier = 1):
                "Both girls reach down and wipe your cock clean."
            else:
                "She wipes your cock clean."
    else:
        if renpy.showing(Girl.tag + "PJ_Animation"):
            pass
        elif not renpy.showing(Girl.tag + " handjob"):
            call show_handjob(Girl, orgasm = True)
        if Partner and approval_check(Partner, 1000, taboo_modifier = 1):
            "Both girls reach down and wipe your cock clean."
        else:
            "She wipes your cock clean."
    $ Player.spunk = 0
    $ Girl.change_face("sexy")
    if Player.primary_Action in ("fondle_breast", "suck breast"):
        call shift_view (Girl, "breasts")
    elif Player.primary_Action in ("fondle_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "fondle_thighs"):
        call shift_view (Girl, "pussy")
    return






label Girl_Cumming(Girl=0, Quick=0, temp_Girls = []):

    if Girl not in all_Girls:
        return

    $ Girl.drain_word("will_masturbate", 1, 1, 0)
    $ Girl.drain_word("wants_to_masturbate", 1, 1, 0)

    if Girl.teaching and Player.location == "bg_classroom":
        pass
    elif Girl.location != Player.location and "phonesex" not in Player.recent_history:

        $ Girl.lust = 25
        return
    $ Girl.eyes = "surprised"
    $ Girl.brows = "sad"
    if Girl in [RogueX, EmmaX, LauraX]:
        $ Girl.mouth = "tongue"
    else:
        $ Girl.mouth = "sucking"
    $ Girl.blushing = "_blush1"

    Girl.voice ". . . !"
    $ action_speed = 0

    call punch

    $ action_speed = 1
    $ line = renpy.random.choice([Girl.name + " is suddenly rocked with spasms, holding back a muffled scream.",
                Girl.name + " grabs on tightly as her body shakes with pleasure.",
                Girl.name + " stiffens and lets out a low moan.",
                Girl.name + "_'s body quivers and suddenly goes still."])
    "[line]"
    $ Girl.thirst = int(Girl.thirst/2)
    $ Girl.thirst -= 5

    $ Girl.session_orgasms += 1
    $ Girl.permanent_History["orgasmed"]+= 1
    $ Girl.lust = 30 if "hotblooded" in Girl.traits else 0
    $ Girl.lust += (Girl.session_orgasms*5)
    $ Girl.lust = 60 if Girl.lust >= 60 else Girl.lust
    call change_Girl_stat(Girl, "inhibition", 1)
    call change_Girl_stat(Girl, "inhibition", 1)

    if Quick:
        $ Girl.change_face("sexy", 2)
        return

    $ Girl.eyes = "closed"
    $ Girl.brows = "sad"
    $ Girl.mouth = "tongue"
    if Girl == RogueX:
        $ line = renpy.random.choice(["Wow. . .  just, wow.",
                "I don't know what came over me. . .",
                "Hmmmm. . . .",
                "That, felt good. Thatfeltrealgood."])
    elif Girl == KittyX:
        $ line = renpy.random.choice(["Wow. . .  just, wow.",
                "That was amazing!",
                "Hmmmm. . . .",
                "I loved that!"])
    elif Girl == EmmaX:
        $ line = renpy.random.choice(["Oooooh. . . lovely.",
                "I really enjoyed that one. . .",
                "Hmmmm. . . .",
                "That was. . . greaaaaat. . ."])
    elif Girl == LauraX:
        $ line = renpy.random.choice(["Oooooh. . .",
                "That was a good one. . .",
                "Hmmmm. . . .",
                "That was. . ."])
    elif Girl == JeanX:
        $ line = renpy.random.choice(["Oooooh. . .",
                "Ah, I needed that. . .",
                "Hmmmm. . . .",
                "Woo, nice. . ."])
    elif Girl == StormX:
        $ line = renpy.random.choice(["Oooooh. . .",
                "Nnnnmmmmaaaaahhh. . .",
                "Hmmmm. . . .",
                "That was. . . amaaazing. . ."])
    elif Girl == JubesX:
        $ line = renpy.random.choice(["Oooooh. . .",
                "Wooooww. . .",
                "Hmmmm. . . .",
                "Wonderful. . ."])
    Girl.voice "[line]"

    if "unsatisfied" in Girl.recent_history:
        call change_Girl_stat(Girl, "love", 2)
        call change_Girl_stat(Girl, "love", 1)
        if "unsatisfied" in Girl.daily_history:
            if Girl == RogueX:
                ch_r "I guess that makes up for earlier, [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "You know how to take care of me."
            elif Girl == EmmaX:
                ch_e "Making up for past mistakes, [Girl.player_petname]?"
            elif Girl == LauraX:
                ch_l "Thanks for evening the score, [Girl.player_petname]?"
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "obedience", 6)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 2)
                ch_j "-Finally.-"
            elif Girl == StormX:
                ch_s "I think that brings us even, [Girl.player_petname]."
            elif Girl == JubesX:
                ch_v "So you -do- know how to make a girl feel good."
        $ Girl.drain_word("unsatisfied")
    $ line = 0

    if Player.primary_Action != "masturbation":
        if Girl.session_orgasms == 1:

            $ Girl.permanent_History["forced"] -= 1 if 5 > Girl.permanent_History["forced"] > 0 else 0
        call change_Girl_stat(Girl, "lust", 1)
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "obedience", 900, 5])
        call change_Girl_stat(Girl, "obedience", 2)


        $ temp_Girls = all_Girls[:]
        $ temp_Girls.remove(Girl)
        while temp_Girls:
            if temp_Girls[0].location == Player.location and "noticed " +Girl.tag in temp_Girls[0].recent_history:
                $ temp_Girls[0].lust += 15 if temp_Girls[0].likes[Girl.tag] >= 500 else 10
                $ temp_Girls[0].lust += 5 if temp_Girls[0].permanent_History["been_with_girl"] >= 5 else 0
            if temp_Girls[0].lust >= 100:
                call Girl_Cumming (temp_Girls[0], 1)
            $ temp_Girls.remove(temp_Girls[0])


        if (Player.primary_Action == "blowjob" or Player.primary_Action == "handjob") and not Player.secondary_Action:
            pass
        elif Partner != Girl:
            if Girl.session_orgasms == 2:
                $ Girl.brows = "confused"
                if Girl == RogueX:
                    ch_r "Wow. . . that was amazing. . ."
                elif Girl == KittyX:
                    ch_k "Hmm. . . so. . . good."
                elif Girl == EmmaX:
                    ch_e "Excellent job, [Girl.player_petname]. . ."
                elif Girl == LauraX:
                    ch_l "Hey, good job, [Girl.player_petname]. . ."
                elif Girl == JeanX:
                    ch_j "I like that attitude. . ."
                elif Girl == StormX:
                    ch_s "Excellent job, [Girl.player_petname]."
                elif Girl == JubesX:
                    ch_v "Oh, that hit where it needed to. . ."
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "obedience", 1)
            elif Girl.session_orgasms == 3:
                $ Girl.brows = "confused"
                if Girl == RogueX:
                    ch_r "You. . . can. . . really. . . keep. . . it. . . up. . . huh?"
                elif Girl == KittyX:
                    ch_k "You're. . .wearing. . .me. . .out. . ."
                elif Girl == EmmaX:
                    ch_e "You . . .certainly. . . have some. . . stamina. . ."
                elif Girl == LauraX:
                    ch_l "You can. . . definitely. . . keep up. . ."
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "love", 3)
                    ch_j "Hey. . . really good job. . ."
                elif Girl == StormX:
                    ch_s "Very. . . dedicated. . . [Girl.player_petname]."
                elif Girl == JubesX:
                    ch_v "You, uh, just keep'em coming, uh?"
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "love", 2)
                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "obedience", 1)
            elif Girl.session_orgasms == 5 and Partner != Girl:
                $ Girl.mouth = "tongue"
                if Girl == RogueX:
                    ch_r "I'm . . .really. . . getting. . . worn. . . out . . ."
                    ch_r "could. . . we. . . cool. . . off?"
                elif Girl == KittyX:
                    ch_k "I'm . . .really. . . getting. . . tired. . . here. . ."
                    ch_k "could. . . we. . . take. . . a. . .break?"
                elif Girl == EmmaX:
                    ch_e "You're . . .practically. . . exhausting. . ."
                    ch_e "would. . . you. . . mind. . . a break?"
                elif Girl == LauraX:
                    ch_l "I don't. . . usually. . . wear out. . . this easy. . ."
                    ch_l "could. . . we. . . take. . . a break?"
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "love", 5)
                    ch_j "Uh. . . I'm a little. . ."
                    call change_Girl_stat(Girl, "love", 3)
                    ch_j "Maybe that's. . . enough for now?"
                elif Girl == StormX:
                    ch_s "Perhaps. . . this would be. . . enough for now. . . [Girl.player_petname]?"
                elif Girl == JubesX:
                    ch_v "I. . . uh. . . love what you're. . . doing here. . ."
                    ch_v "But. . . uh. . . maybe you could. . . let me. . . catch my breath?"
                menu:
                    extend ""
                    "Finish up." if Player.focusing:
                        "You release your concentration. . ."
                        $ Player.focusing = 0
                        $ Player.climax += 15
                    "Let's try something else." if multi_action:
                        $ action_context = "shift"
                    "No, I'm not done yet.":
                        if Player.primary_Action == "sex" or Player.primary_Action == "anal":
                            if approval_check(Girl, 1000, taboo_modifier = 1) or approval_check(Girl, 400, "O", taboo_modifier = 1):
                                call change_Girl_stat(Girl, "love", -5)
                                call change_Girl_stat(Girl, "obedience", 900, 5])
                                call change_Girl_stat(Girl, "obedience", 3)
                                $ Girl.eyes = "stunned"
                                "She drifts off into incoherent moans."
                            else:
                                $ Girl.change_face("angry", 1)
                                "She scowls at you, pulls out with a pop, and wipes herself off."
                                if Girl == RogueX:
                                    ch_r "Well if that's your attitude you can handle your own business."
                                elif Girl == KittyX:
                                    ch_k "Looks like you're going to have to. . ."
                                elif Girl == EmmaX:
                                    ch_e "Learn to take a hint. . ."
                                elif Girl == LauraX:
                                    ch_l "Well, I am. . ."
                                elif Girl == JeanX:
                                    ch_j ". . ."
                                    ch_j "I just don't have the time right now."
                                elif Girl == StormX:
                                    ch_s "I wish I could manage it, [Girl.player_petname]."
                                elif Girl == JubesX:
                                    ch_v "Well, uh. . . I am."
                                call change_Girl_stat(Girl, "love", 1)
                                call change_Girl_stat(Girl, "love", 1)
                                call change_Girl_stat(Girl, "obedience", Alt = [[JeanX],300, 5])
                                call change_Girl_stat(Girl, "obedience", 900, 5])
                                $ Girl.recent_history.append("angry")
                                $ Girl.daily_history.append("angry")
                        else:
                            call change_Girl_stat(Girl, "obedience", 900, 5])
                            call change_Girl_stat(Girl, "obedience", 2)
                            $ Girl.eyes = "stunned"
                            "She drifts off into incoherent moans."

    if Player.primary_Action == "striptease":
        call show_full_body(Girl)
        call show_Girl(Girl, color_transform = dancing(Girl.sprite_location))

        "[Girl.name] begins to dance again."
    return





label Girl_Cleanup(Girl=0, Choice = "random", Options = [], counter=0, Cleaned=0, Original=0):
    if Girl not in all_Girls or ("painted" in Girl.recent_history and Choice != "ask"):
        return
    if Choice == "after":

        if not any(value for value in Girl.spunk.values()):
            $ Girl.grool = 0
            return
        $ counter = 1
        $ approval_bonus = 0

    if Girl.addiction > 80 and Girl.permanent_History["swallowed"]:

        $ Choice = "eat"
        $ Girl.eyes = "manic"
        $ Girl.mouth = "smile"
    elif Girl == EmmaX and "taboo" not in EmmaX.history and counter:

        $ Choice = "clean"
    elif Choice == "ask":
        pass
    elif "painted" in Girl.recent_history and approval_check(Girl, 1000, "OI"):
        return
    elif approval_check(Girl, 1200, "LO"):
        $ Choice = "ask"
    elif not approval_check(Girl, 400, "I"):
        $ Girl.change_face("bemused")
        $ Choice = "clean"
    elif not counter:
        $ Choice = "random"
    else:
        $ Choice = "ask"

    $ Cleaned = 1 if "cleaned" in Girl.daily_history else 0
    $ Girl.recent_history.append("cleaned")
    $ Girl.daily_history.append("cleaned")

    if Player.focused_Girl != Girl:

        if Original in all_Girls:
            $ Original = Partner
        else:
            $ Original = Girl
        $ shift_focus (Girl)

    if Choice == "ask":
        $ Choice = "random"
        "[Girl.name] looks down at the spunk covering her."
        menu:
            "What do you suggest [Girl.name] do about cleaning up?"
            "You should leave it where it is.":
                if not counter:

                    $ Girl.change_face("sly")
                    if approval_check(Girl, 300, "I") or approval_check(Girl, 1000):
                        call change_Girl_stat(Girl, "obedience", 1)
                        call change_Girl_stat(Girl, "inhibition", 1)
                        call change_Girl_stat(Girl, "lust", 2)
                        $ Choice = "leave"
                        if Girl == RogueX:
                            ch_r "Heh, ok, [Girl.player_petname]."
                        elif Girl == KittyX:
                            ch_k "Oh, ok."
                        elif Girl == EmmaX:
                            ch_e "Hmm. . ."
                        elif Girl == LauraX:
                            ch_l "Hmm. . ."
                        elif Girl == JeanX:
                            ch_j "Ok, sure. . ."
                        elif Girl == StormX:
                            ch_s "Oh, I suppose that I could, [Girl.player_petname]."
                        elif Girl == JubesX:
                            call change_Girl_stat(Girl, "love", -2)
                            $ Girl.change_face("sad")
                            ch_v "Well, uh. . . I guess. . ."
                    else:
                        if Girl == RogueX:
                            ch_r "Ugh, too messy."
                        elif Girl == KittyX:
                            ch_k "Hm, no."
                        elif Girl == EmmaX:
                            ch_e "Too undignified, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "Eh, I'm not a fan of mess, [Girl.player_petname]."
                        elif Girl == JeanX:
                            ch_j "Not in the mood, [Girl.player_petname]."
                        elif Girl == StormX:
                            ch_s "That would be a bit messy, [Girl.player_petname]."
                        elif Girl == JubesX:
                            $ Girl.change_face("sad")
                            ch_v "I, uh. . . wouldn't want to leave it a mess. . ."


                elif approval_check(Girl, 900, "I") or "exhibitionist" in Girl.traits:
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "lust", 5)
                    $ Choice = "leave"
                    $ Girl.change_face("sly")
                    if Girl == RogueX:
                        ch_r "Ooh, I like where your head is at. . "
                    elif Girl == KittyX:
                        ch_k "Ooh, I like where your head is at. . "
                    elif Girl == EmmaX:
                        ch_e "Hmm. . . I suppose I could use some accessories. . "
                    elif Girl == LauraX:
                        ch_l "Hmm. . . I do like the glow it gives me. . "
                    elif Girl == JeanX:
                        ch_j "Hmm. . . ok."
                    elif Girl == StormX:
                        ch_s "Something to wear out, [Girl.player_petname]. . ."
                    elif Girl == JubesX:
                        call change_Girl_stat(Girl, "love", -2)
                        $ Girl.change_face("sad")
                        ch_v "Oh, uh. . . I guess I could. . ."
                elif approval_check(Girl, 600, "I") and approval_check(Girl, 1200, "LO", Alt = [[JubesX], 1500]):
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    call change_Girl_stat(Girl, "lust", 5)
                    $ Choice = "leave"
                    $ Girl.change_face("surprised", 2)
                    if Girl == RogueX:
                        ch_r "Well, I guess I could. . ."
                    elif Girl == KittyX:
                        ch_k "Well, maybe. . ."
                    elif Girl == EmmaX:
                        ch_e "Hmm. . . if you insist. . ."
                    elif Girl == LauraX:
                        ch_l "Hmm. . . if you insist. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . ok."
                    elif Girl == StormX:
                        ch_s ". . . Fine."
                    elif Girl == JubesX:
                        $ Girl.change_face("sad")
                        ch_v "Oh, uh. . . I guess I could. . ."
                    $ Girl.change_face("sly", 1)
                else:

                    $ Girl.change_face("angry")
                    if Girl == RogueX:
                        ch_r "Now you're just being ridiculous!"
                    elif Girl == KittyX:
                        $ Girl.brows = "confused"
                        ch_k "Now you're just being silly!"
                    elif Girl == EmmaX:
                        ch_e "Excuse me?"
                    elif Girl == LauraX:
                        ch_l "Excuse me?"
                    elif Girl == JeanX:
                        ch_j "What?"
                    elif Girl == StormX:
                        ch_s "That would be a bit much, [Girl.player_petname]."
                    elif Girl == JubesX:
                        $ Girl.change_face("sad")
                        ch_v "Well. . . that would be. . . messy. . . yeah."
                    menu:
                        extend ""
                        "Please?":
                            if approval_check(Girl, 1800, Alt = [[JubesX], 2200]):
                                call change_Girl_stat(Girl, "love", 1)
                                call change_Girl_stat(Girl, "obedience", 2)
                                call change_Girl_stat(Girl, "obedience", 1)
                                call change_Girl_stat(Girl, "inhibition", 3)
                                call change_Girl_stat(Girl, "inhibition", 1)
                                if Girl == RogueX:
                                    ch_r "Oh, fine!"
                                elif Girl == KittyX:
                                    ch_k "Oh, fine!"
                                elif Girl == EmmaX:
                                    ch_e "Well. Ok."
                                elif Girl == LauraX:
                                    ch_l "Fine."
                                elif Girl == JeanX:
                                    ch_j "Hmm. . . ok."
                                elif Girl == StormX:
                                    ch_s ". . . Fine."
                                elif Girl == JubesX:
                                    call change_Girl_stat(Girl, "love", -2)
                                    ch_v ". . . fine. . ."
                                $ Choice = "leave"
                            elif Cleaned:
                                $ Girl.change_face("angry")
                                if Girl == RogueX:
                                    ch_r "Seriously, stop bugging me about this."
                                elif Girl == KittyX:
                                    ch_k "Seriously, quit bugging me about this."
                                elif Girl == EmmaX:
                                    ch_e "I believe I've made myself clear."
                                elif Girl == LauraX:
                                    ch_l "I'm in no mood for this."
                                elif Girl == JeanX:
                                    ch_j "Cut it out, [Girl.player_petname]."
                                elif Girl == StormX:
                                    ch_s "I cannot."
                                elif Girl == JubesX:
                                    ch_v "I don't wanna!"
                            elif approval_check(Girl, 800):
                                call change_Girl_stat(Girl, "inhibition", 1)
                                if Girl == RogueX:
                                    ch_r "You're persistant, but no way."
                                elif Girl == KittyX:
                                    ch_k "You're persistant, but no way."
                                elif Girl == EmmaX:
                                    ch_e "You're persistant, but no."
                                elif Girl == LauraX:
                                    ch_l "You're certainly persistant, but no."
                                elif Girl == JeanX:
                                    ch_j "Cut it out."
                                elif Girl == StormX:
                                    ch_s "Be serious, [Girl.player_petname]."
                                elif Girl == JubesX:
                                    ch_v "No!"
                            else:
                                call change_Girl_stat(Girl, "love", -5)
                                call change_Girl_stat(Girl, "love", -10)
                                call change_Girl_stat(Girl, "obedience", 2)
                                $ Girl.change_face("angry")
                                if Girl == RogueX:
                                    ch_r "Don't be an asshole."
                                elif Girl == KittyX:
                                    ch_k "Don't be a dick."
                                elif Girl == EmmaX:
                                    ch_e "Of course not."
                                elif Girl == LauraX:
                                    ch_l "You've gotta be joking."
                                elif Girl == JeanX:
                                    ch_j "Fuck off."
                                elif Girl == StormX:
                                    ch_s "No."
                                elif Girl == JubesX:
                                    ch_v "No way! Mine!"
                        "I insist.":
                            $ Girl.change_face("sad")
                            if approval_check(Girl, 400, "I") and approval_check(Girl, 1200, "LO", Alt = [[JubesX], 1500]):
                                call change_Girl_stat(Girl, "obedience", 3)
                                call change_Girl_stat(Girl, "obedience", 2)
                                if Girl == RogueX:
                                    ch_r "Alright, fine."
                                elif Girl == KittyX:
                                    ch_k "Fine, whatever."
                                elif Girl == EmmaX:
                                    ch_e "Well then."
                                elif Girl == LauraX:
                                    ch_l "Fine."
                                elif Girl == JeanX:
                                    ch_j "Well good for you."
                                elif Girl == StormX:
                                    ch_s ". . . I suppose."
                                elif Girl == JubesX:
                                    call change_Girl_stat(Girl, "love", -2)
                                    ch_v ". . . fine."
                                $ Choice = "leave"
                            elif approval_check(Girl, 800, "O"):
                                call change_Girl_stat(Girl, "love", -10)
                                call change_Girl_stat(Girl, "love", -5)
                                call change_Girl_stat(Girl, "obedience", 10)
                                call change_Girl_stat(Girl, "obedience", 5)
                                if Girl == RogueX:
                                    ch_r "If you have to insist."
                                elif Girl == KittyX:
                                    ch_k "Fine."
                                elif Girl == EmmaX:
                                    ch_e "If I must."
                                elif Girl == LauraX:
                                    ch_l "If you insist."
                                elif Girl == JeanX:
                                    ch_j "Huh. . . ok."
                                elif Girl == StormX:
                                    ch_s ". . . Fine."
                                elif Girl == JubesX:
                                    ch_v ". . . fine."
                                $ Choice = "leave"
                            elif Cleaned:
                                call change_Girl_stat(Girl, "love", -5)
                                call change_Girl_stat(Girl, "love", -1)
                                $ Girl.change_face("angry")
                                if Girl == RogueX:
                                    ch_r "Seriously, stop bugging me about this."
                                elif Girl == KittyX:
                                    ch_k "Seriously, stop bugging me about this."
                                elif Girl == EmmaX:
                                    ch_e "That's enough of that."
                                elif Girl == LauraX:
                                    ch_l "Enough out of you."
                                elif Girl == JeanX:
                                    ch_j "Cut it out."
                                elif Girl == StormX:
                                    ch_s "That is enough, [Girl.player_petname]."
                                elif Girl == JubesX:
                                    ch_v "I don't wanna!"
                            elif approval_check(Girl, 800):
                                call change_Girl_stat(Girl, "love", -3)
                                call change_Girl_stat(Girl, "love", -1)
                                $ Girl.change_face("sad")
                                if Girl == RogueX:
                                    ch_r "Sorry, that's just a bridge too far."
                                elif Girl == KittyX:
                                    ch_k "That's a bit much."
                                elif Girl == EmmaX:
                                    ch_e "Don't push me."
                                elif Girl == LauraX:
                                    ch_l "Don't push it."
                                elif Girl == JeanX:
                                    ch_j "Cool it."
                                elif Girl == StormX:
                                    ch_s "No."
                                elif Girl == JubesX:
                                    ch_v "No!"
                            else:
                                call change_Girl_stat(Girl, "love", -10)
                                call change_Girl_stat(Girl, "love", -5)
                                $ Girl.change_face("angry")
                                if Girl == RogueX:
                                    ch_r "Well {i}I{/i} insist you don't know how to talk to a lady!"
                                elif Girl == KittyX:
                                    ch_k "Well that's too bad!"
                                elif Girl == EmmaX:
                                    ch_e "Obviously not."
                                elif Girl == LauraX:
                                    ch_l "Hell no."
                                elif Girl == JeanX:
                                    ch_j "Good for you."
                                elif Girl == StormX:
                                    ch_s "Do not push me, [Girl.player_petname]."
                                elif Girl == JubesX:
                                    ch_v "No way!"
                        "Never mind then.":
                            if Girl == RogueX:
                                ch_r "Alright then. . ."
                            elif Girl == KittyX:
                                ch_k "Right. . ."
                            elif Girl == EmmaX:
                                ch_e "Ok. . ."
                            elif Girl == LauraX:
                                ch_l "Ok. . ."
                            elif Girl == JeanX:
                                ch_j "Right. . ."
                            elif Girl == StormX:
                                ch_s "Very well."
                            elif Girl == JubesX:
                                ch_v "Good."
            "You should just eat it.":


                $ Girl.change_face("sly")
                if "hungry" in Girl.traits or (Girl.permanent_History["swallowed"] >= 5 and approval_check(Girl, 800)):

                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    call change_Girl_stat(Girl, "lust", 5)
                    $ Choice = "eat"
                    if Girl == RogueX:
                        ch_r "I am a bit peckish. . ."
                    elif Girl == KittyX:
                        ch_k "Mmmmm, maybe . ."
                    elif Girl == EmmaX:
                        ch_e "Well, I suppose I could. . ."
                    elif Girl == LauraX:
                        "She licks her lips. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . ok."
                    elif Girl == StormX:
                        ch_s "Thank you. . ."
                    elif Girl == JubesX:
                        $ Girl.change_face("smile")
                        ch_v "Sweet!"
                elif Girl.permanent_History["swallowed"] and approval_check(Girl, 800):

                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    call change_Girl_stat(Girl, "lust", 5)
                    $ Choice = "eat"
                    if Girl == RogueX:
                        ch_r "I guess it wasn't so bad last time. . ."
                    elif Girl == KittyX:
                        ch_k "It's not that bad. . ."
                    elif Girl == EmmaX:
                        ch_e "You do have a unique flavor. . ."
                    elif Girl == LauraX:
                        ch_l "You do taste pretty good. . ."
                    elif Girl == JeanX:
                        ch_j "Mmmm. . . ok."
                    elif Girl == StormX:
                        ch_s "Very interesting. . ."
                    elif Girl == JubesX:
                        $ Girl.change_face("smile")
                        ch_v "Sweet!"
                elif approval_check(Girl, 1200) or Girl == JubesX:

                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    $ Choice = "eat"
                    if Girl == RogueX:
                        ch_r "I suppose I could give it a go. . ."
                    elif Girl == KittyX:
                        ch_k "Huh, I guess. . ."
                    elif Girl == EmmaX:
                        ch_e "I have been a bit curious. . ."
                    elif Girl == LauraX:
                        ch_l "I have been thinking about it. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . ok."
                    elif Girl == StormX:
                        ch_s "I could try it, [Girl.player_petname]."
                    elif Girl == JubesX:
                        $ Girl.change_face("smile")
                        ch_v "Thanks!"
                elif approval_check(Girl, 400):

                    $ Girl.change_face("sad")
                    if Girl == RogueX:
                        ch_r "Sorry, I just don't think I could."
                    elif Girl == KittyX:
                        ch_k "Yeah, not really."
                    elif Girl == EmmaX:
                        ch_e "I doubt that."
                    elif Girl == LauraX:
                        ch_l "Yeah, but I won't. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . nah."
                    elif Girl == StormX:
                        ch_s "I would rather not."
                else:


                    call change_Girl_stat(Girl, "love", -5)
                    call change_Girl_stat(Girl, "love", -3)
                    $ Girl.change_face("angry")
                    if Girl == RogueX:
                        ch_r "No."
                    elif Girl == KittyX:
                        ch_k "Nah."
                    elif Girl == EmmaX:
                        ch_e "No."
                    elif Girl == LauraX:
                        ch_l "Nope."
                    elif Girl == JeanX:
                        ch_j "Ha. . . no way."
                    elif Girl == StormX:
                        ch_s "Thank you, but no."
            "You should just clean it up.":



                if approval_check(Girl, 600, "I") and not approval_check(Girl, 1500, "LO") and Girl != JubesX:
                    $ Girl.change_face("sly")
                    call change_Girl_stat(Girl, "obedience", -3)
                    call change_Girl_stat(Girl, "inhibition", 10)
                    call change_Girl_stat(Girl, "inhibition", 5)
                    call change_Girl_stat(Girl, "lust", 5)
                    if Girl == RogueX:
                        ch_r "I don't know, [Girl.player_petname], I kind of like it where it is. . ."
                    elif Girl == KittyX:
                        ch_k "I don't know, [Girl.player_petname], it doesn't look so bad. . ."
                    elif Girl == EmmaX:
                        ch_e "Hmmm. . . don't I look good like this? . ."
                    elif Girl == LauraX:
                        ch_l "I could. . ."
                        ch_l "-but I don't want to. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . nah. I like it like this. . ."
                    elif Girl == StormX:
                        ch_s "I might like to keep it like this. . ."
                    $ Choice = "leave"
                    menu:
                        extend ""
                        "Ok, fine.":
                            $ Girl.change_face("smile")
                            call change_Girl_stat(Girl, "love", 5)
                            call change_Girl_stat(Girl, "obedience", 3)
                        "No, clean it up.":
                            if approval_check(Girl, 600, "O"):
                                $ Girl.change_face("sad")
                                call change_Girl_stat(Girl, "obedience", 10)
                                if Girl == RogueX:
                                    ch_r "If that's what you really want. . ."
                                elif Girl == KittyX:
                                    ch_k "Oh, fine. . ."
                                elif Girl == EmmaX:
                                    ch_e "Oh, if I must. . ."
                                elif Girl == LauraX:
                                    ch_l "Oh, fine. . ."
                                elif Girl == JeanX:
                                    ch_j "Hmm. . . whatever."
                                elif Girl == StormX:
                                    ch_s ". . . Fine."
                                elif Girl == JubesX:
                                    ch_v "Sweet!"
                                $ Choice = "clean"
                            elif approval_check(Girl, 1200, "LO"):
                                $ Girl.change_face("sad")
                                call change_Girl_stat(Girl, "love", -3)
                                call change_Girl_stat(Girl, "obedience", 3)
                                if Girl == RogueX:
                                    ch_r "You take the fun out of this. . ."
                                elif Girl == KittyX:
                                    ch_k "Boooo. . ."
                                elif Girl == EmmaX:
                                    ch_e "Spoilsport. . ."
                                elif Girl == LauraX:
                                    ch_l "Booo. . ."
                                elif Girl == JeanX:
                                    ch_j ". . . whatever."
                                elif Girl == StormX:
                                    ch_s ". . . Fine."
                                $ Choice = "clean"
                            else:
                                call change_Girl_stat(Girl, "love", -5)
                                call change_Girl_stat(Girl, "obedience", -5)
                                if Girl == RogueX:
                                    ch_r "I {i}said{/i} it's stay'in."
                                elif Girl == KittyX:
                                    ch_k "No! I like it this way."
                                elif Girl == EmmaX:
                                    ch_e "I'm afraid you don't have any say in the matter."
                                elif Girl == LauraX:
                                    ch_l "Too bad."
                                elif Girl == JeanX:
                                    ch_j "Hmm. . . whatever."
                                elif Girl == StormX:
                                    ch_s ". . . no."
                else:
                    $ Girl.change_face("bemused")
                    $ Choice = "clean"
                    if Girl == RogueX:
                        ch_r "Ok, I guess. . ."
                    elif Girl == KittyX:
                        ch_k "Ok, fine. . ."
                    elif Girl == EmmaX:
                        ch_e "If I must. . ."
                    elif Girl == LauraX:
                        ch_l "Whatever. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . whatever."
                    elif Girl == StormX:
                        ch_s ". . . Fine."
                    elif Girl == JubesX:
                        ch_v "Not a problem!"


            "Hey [Partner.name], you eat it off her." if Partner:
                $ Choice = "partner lick"
            "Hey [Partner.name], you wipe it off her." if Partner:
                $ Choice = "partner wipe"
            "Say nothing. [[leave it to her]":


                $ Choice = "random"


    if Choice == "partner wipe" or Choice == "partner lick":

        call Partner_Cleanup_Check (Girl)

    if Choice == "random":
        $ Options = ["clean"]
        if Girl.permanent_History["swallowed"] and approval_check(Girl, 800):
            $ Options.append("eat")
            if Girl.permanent_History["swallowed"] >=5:
                $ Options.append("eat")
            if "hungry" in Girl.traits:
                $ Options.append("eat")
        if approval_check(Girl, 300, "I"):

            if not counter:
                $ Options.append("leave")
            if not counter or approval_check(Girl, 600, "I"):
                $ Options.append("leave")
            if not counter or approval_check(Girl, 800, "I"):
                $ Options.append("leave")
            if "exhibitionist" in Girl.traits:
                $ Options.append("leave")

        $ renpy.random.shuffle(Options)

        $ Choice = Options[0]

    if Girl == JubesX:
        $ Options = ["eat"]

    if Girl.spunk and Choice != "leave":
        call Self_Cleanup (Girl)

    if Choice == "leave":
        call change_Girl_stat(Girl, "inhibition", 2)
        call change_Girl_stat(Girl, "inhibition", 1)
        "She leaves the jizz right where it is and gives you a wink."
        if Girl.spunk["hand"]:
            $ Girl.spunk["hand"] = False
            if Girl.permanent_History["swallowed"]:
                "She does lick off her hand though."
            else:
                "She does wipe her hand off though."
        if Girl.spunk["mouth"]:
            $ Girl.spunk["mouth"] = False
        if counter:

            $ Girl.recent_history.append("painted")
            $ Girl.daily_history.append("painted")

    if Original in all_Girls and Player.focused_Girl != Original:

        $ shift_focus (Original)
    return






label Self_Cleanup(Girl=0):
    $ counter = 0
    if Girl == JeanX and not approval_check(Girl, 600, "LO"):

        $ Girl.grool = 0

        python:
            for key in Girl.spunk.keys():
                Girl.spunk[key] = False

        $ Girl.change_face("sly", 1, eyes = "psychic")
        "[JeanX.name] concentrates and the juices swirl off of her, raining to the floor."
        $ Girl.change_face("sly", 0)
        return
    if Girl.spunk["mouth"] and Choice != "eat":
        $ Girl.spunk["mouth"] = False
        "[Girl.name] spits out the spunk in her mouth and it dribbles down her chin, "
        $ counter += 1
        if not Girl.spunk["chin"]:
            $ Girl.spunk["chin"] = True
    if any(value for value in Girl.spunk.values()):
        $ Girl.spunk["hand"] = True
    if Girl.spunk["chin"]:
        $ Girl.spunk["chin"] = False
        if counter:
            "then she wipes the spunk off her chin, "
        else:
            "[Girl.name] wipes the spunk off her chin, "
        $ counter += 1
    if Girl.spunk["hair"]:
        $ Girl.spunk["hair"] = False
        if counter:
            "then she wipes the spunk out of her hair, "
        else:
            "[Girl.name] wipes the spunk out of her hair, "
        $ counter += 1
    if Girl.spunk["face"]:
        $ Girl.spunk["face"] = False
        if counter:
            "then she wipes the spunk off of her face, "
        else:
            "[Girl.name] wipes the spunk off of her face, "
        $ counter += 1
    if Girl.spunk["breasts"]:
        $ Girl.spunk["breasts"] = False
        call change_Player_stat("focus",80, 2)
        if counter:
            "then she wipes the spunk off of her chest, "
        else:
            "[Girl.name] wipes the spunk off of her chest, "
        $ counter += 1
    if Girl.spunk["belly"]:
        $ Girl.spunk["belly"] = False
        if counter:
            "then she wipes the spunk off of her belly, "
        else:
            "[Girl.name] wipes the spunk off her belly, "
        $ counter += 1
    if Girl.spunk["back"]:
        $ Girl.spunk["back"] = False
        if counter:
            "then she wipes the spunk off of her lower back, "
        else:
            "[Girl.name] wipes the spunk off her lower back, "
        $ counter += 1
    if Girl.spunk["pussy"]:
        $ Girl.spunk["pussy"] = False
        call change_Player_stat("focus",80,3)
        if counter:
            "then she wipes the spunk inside her pussy, "
        else:
            "[Girl.name] wipes the spunk inside her pussy, "
        $ counter += 1
    if Girl.spunk["anus"] and (approval_check(Girl, 800, "I") or Choice != "eat"):
        while Girl.spunk["anus"]:
            $ Girl.spunk["anus"] = False
        call change_Player_stat("focus",80, 2)
        if counter:
            "then she wipes the spunk dripping out of her ass, "
        else:
            "[Girl.name] wipes the spunk dripping our of her ass, "
        $ counter += 1
    if Girl.spunk["hand"]:
        $ Girl.spunk["hand"] = False
        if Choice == "eat":
            $ Girl.spunk["mouth"] = True
            call change_Player_stat("focus",80,3)
            if counter and Girl.spunk["anus"]:
                "then licks her hands off with a satisfied grin, "
            if counter:
                "and finally she licks her hands off with a satisfied grin."
            else:
                "[Girl.name] licks her hands off with a satisfied grin."

            call change_Girl_stat(Girl, "inhibition", 2)
            $ Girl.spunk["mouth"] = False
            $ Girl.permanent_History["swallowed"] += 1
            $ Girl.addiction -= (10*counter)
            if Girl.permanent_History["swallowed"] == 1:
                $ Girl.SEXP += 12
            $ Girl.recent_history.append("swallowed")
            $ Girl.daily_history.append("swallowed")
        else:

            if counter:
                "and finally, she wipes her hands off with a nearby tissue."
            else:
                "[Girl.name] wipes her hands off with a nearby tissue."
        $ counter += 1

    if Girl.spunk["anus"]:
        $ Girl.spunk["anus"] = False
        if counter:
            "Afterward, she wipes the spunk dripping our of her ass."
        else:
            "[Girl.name] wipes the spunk dripping out of her ass."

    $ Girl.grool = 0

    python:
        for key in Girl.spunk.keys():
            Girl.spunk[key] = False

    if counter >= 5:
        $ Girl.eyes = "surprised"
        if Girl == RogueX:
            ch_r "Wow, you really painted me white!"
        elif Girl == KittyX:
            ch_k "Wow, you really drenched me!"
        elif Girl == EmmaX:
            if "White Queen" not in EmmaX.names:
                ch_e "I really was the \"white queen\" there."
                $ EmmaX.names.append("White Queen")
            else:
                ch_e "Well that was a lot of work."
        elif Girl == LauraX:
            ch_l "There was a lot more to that than I'd noticed. . ."
        elif Girl == JeanX:
            ch_j "Ugh, you really made a mess there. . ."
        elif Girl == StormX:
            ch_s ". . . is there any in my hair? So hard to tell. . ."
        elif Girl == JubesX:
            ch_v "You really coated me, huh?"
        $ Girl.eyes = "sexy"
    elif counter > = 3:
        if Girl == RogueX:
            ch_r "That was a real mess you left me to clean up."
        elif Girl == KittyX:
            ch_k "Well that was a fine mess you got me into."
        elif Girl == EmmaX:
            ch_e "I really was the \"white queen\" there."
            if "White Queen" not in EmmaX.names:
                $ EmmaX.names.append("White Queen")
        elif Girl == LauraX:
            ch_l "You made a real mess there."
        elif Girl == JeanX:
            ch_j "Maybe be more careful with your aim. . ."
        elif Girl == StormX:
            ch_s "Perhaps next time take better care where you fire."
        elif Girl == JubesX:
            ch_v "Whew, that was a lot."
    if Choice == "eat" and Girl.permanent_History["swallowed"] >= 5:
        if Girl == RogueX:
            ch_r "That was delicious."
        elif Girl == KittyX:
            ch_k "Yum."
        elif Girl == EmmaX:
            ch_e "Mmmm, now I'm hungry for more."
        elif Girl == LauraX:
            ch_l "Mmmm, got any more?"
        elif Girl == JeanX:
            ch_j "Mmm. . ."
        elif Girl == StormX:
            ch_s "Mmmm. . ."
        elif Girl == JubesX:
            ch_v "That was amazing. . ."
    return


label Partner_Cleanup_Check(Girl=0, B=0):


    if Partner == JubesX:
        $ B = 100
    elif Choice == "partner lick":
        if (Partner in Player.Harem and Girl in Player.Harem) or "poly " + Partner.tag in Girl.traits:
            $ B = 0
        else:
            $ B = -100
    else:
        $ B = 0


    if Partner == JeanX and not approval_check(Partner, 600, "LO") and Partner.likes[Girl.tag] < (500-2*B):

        ch_j "Hm? Clean [Girl.name] off?"
        ch_j "I guess she is a mess. . ."
        $ Girl.grool = 0

        python:
            for key in Girl.spunk.keys():
                Girl.spunk[key] = False

        $ Partner.change_face("sly", 1, eyes = "psychic")
        "[JeanX.name] concentrates and the juices swirl off of [Girl.name], raining to the floor."
        if Girl == JubesX:
            $ Girl.change_face("sad", 1, eyes = "down")
            ch_v "Aw."
        $ Partner.change_face("sly", 0)
        ch_j "There."
        return

    if not approval_check(Partner, 1400, Bonus = 3*B) or Partner.likes[Girl.tag] < (500-2*B):

        $ Partner.change_face("sly")
        call change_Girl_stat(Partner, "obedience", -3)
        call change_Girl_stat(Partner, "inhibition", 10)
        call change_Girl_stat(Partner, "inhibition", 5)
        call change_Girl_stat(Partner, "lust", 5)
        call Partner_CGline (2)
        menu:
            extend ""
            "Fine, never mind.":
                $ Partner.change_face("smile")
                call change_Girl_stat(Partner, "love", 5)
                call change_Girl_stat(Partner, "obedience", 3)
                $ Choice = "random"
            "Yeah, go ahead.":
                if approval_check(Partner, 600, "O", Bonus = 3*B):

                    $ Partner.change_face("sad")
                    call change_Girl_stat(Partner, "obedience", 10)
                    call Partner_CGline (3)
                elif Partner.likes[Girl.tag] >= 800:

                    $ Partner.change_face("sly")
                    call change_Girl_stat(Partner, "love", -3)
                    call change_Girl_stat(Partner, "obedience", 3)
                    call Partner_CGline (4)
                elif approval_check(Partner, 1200, Bonus = 3*B):

                    $ Partner.change_face("normal")
                    call change_Girl_stat(Partner, "love", -3)
                    call change_Girl_stat(Partner, "obedience", 3)
                    call Partner_CGline (5)
                elif Choice == "partner lick" and approval_check(Partner, 1200) and Partner.likes[Girl.tag] >= 600:

                    $ Partner.change_face("normal")
                    call change_Girl_stat(Partner, "love", -3)
                    call change_Girl_stat(Partner, "obedience", 3)
                    call Partner_CGline (6)
                    $ Choice = "partner wipe"
                else:

                    call change_Girl_stat(Partner, "love", -5)
                    call change_Girl_stat(Partner, "obedience", -5)
                    $ Girl.check_if_likes(Partner, 900, -2, 1)
                    call Partner_CGline (7)
                    $ Choice = "random"
    else:
        $ Girl.change_face("bemused")
        if not Choice:
            $ Choice = "partner wipe"
        $ Girl.check_if_likes(Partner, 900,3, 1)
        call Partner_CGline (1)



    if Choice != "random":
        call change_Girl_stat(Girl, "lust", 5)
        if not approval_check(Girl, 1400, Bonus = 3*B) or Girl.likes[Partner.tag] < (500-2*B):

            if Girl.likes[Partner.tag] >= 800:
                call change_Girl_stat(Girl, "inhibition", 5)
                $ Partner.check_if_likes(Girl, 900, 5, 1)
                call Partner_CGline (8, Girl)
            elif approval_check(Girl, 1200, Bonus = 3*B):
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 3)
                call Partner_CGline (9, Girl)
            elif approval_check(Girl, 1000, Bonus = 3*B) and Girl.likes[Partner.tag] >= (600-B):
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "inhibition", 5)
                $ Partner.check_if_likes(Girl, 900,3, 1)
                call Partner_CGline (10, Girl)
            else:
                call change_Girl_stat(Girl, "obedience", -3)
                call change_Girl_stat(Girl, "inhibition", 2)
                call Partner_CGline (11, Girl)
                $ Choice = "random"
        else:
            call change_Girl_stat(Girl, "obedience", 3)
            call change_Girl_stat(Girl, "inhibition", 3)
            call Partner_CGline (12, Girl)

    if Choice != "random":

        call lesbian_launch(Girl)

        call Partner_Clean_Girl (Girl)

        if Girl.permanent_History["swallowed"] >=5:
            $ Options.append("eat")
        call show_full_body(Player.focused_Girl)
        call show_full_body(Partner)
        if Choice == "partner lick":
            $ Girl.check_if_likes(Partner, 900, 10, 1)
            call Partner_CGline (13, Girl)
        else:
            $ Girl.check_if_likes(Partner, 900,3, 1)
            call Partner_CGline (14, Girl)

    return

label Partner_CGline(lineNum = 1, Girl=0):

    if not Partner or not lineNum:
        return
    if lineNum == 1:

        if Partner == RogueX:
            ch_r "Sure, why not?"
        elif Partner == KittyX:
            ch_k "You[KittyX.like]really did a job on her."
            ch_k "I'll get on it."
        elif Partner == EmmaX:
            ch_e "I suppose it wouldn't be so bad."
        elif Partner == LauraX:
            ch_l "I'd better get to work, I guess."
        elif Partner == JeanX:
            ch_j "I guess. . ."
        elif Partner == StormX:
            ch_s "I suppose I would not mind. . ."
        elif Partner == JubesX:
            ch_v "Cool. . ."
    elif lineNum == 2:

        if Partner == RogueX:
            ch_r "You want me ta clean up your mess?"
        elif Partner == KittyX:
            ch_k "You[KittyX.like]really did a job on her."
            ch_k "I'm supposed to deal with that?"
        elif Partner == EmmaX:
            ch_e "You expect me to stoop to clean-up duty?"
        elif Partner == LauraX:
            ch_l "Real mess you left me there."
        elif Partner == JeanX:
            ch_j "So I'm your maid now?"
        elif Partner == StormX:
            ch_s "You would like me to clean her off?"
        elif Partner == JubesX:
            ch_v "Could I? . ."
    elif lineNum == 3:

        if Partner == RogueX:
            ch_r "If you say so."
        elif Partner == KittyX:
            ch_k "Whatever."
        elif Partner == EmmaX:
            ch_e "Lovely."
        elif Partner == LauraX:
            ch_l "On it."
        elif Partner == JeanX:
            ch_j "Sure. . ."
        elif Partner == StormX:
            ch_s ". . . Fine."
        elif Partner == JubesX:
            ch_v "Sure. . ."
    elif lineNum == 4:

        if Partner == RogueX:
            ch_r "Well, if she doesn't mind. . ."
        elif Partner == KittyX:
            ch_k "I guess I don't mind if she doesn't."
        elif Partner == EmmaX:
            ch_e "Very well, come over here, dear."
        elif Partner == LauraX:
            ch_l "She is a bit messy. . ."
        elif Partner == JeanX:
            ch_j "Well, if I must. . ."
        elif Partner == StormX:
            ch_s "Very well, come here."
        elif Partner == JubesX:
            ch_v "Cool. . ."
    elif lineNum == 5:

        if Partner == RogueX:
            ch_r "I s'pose so. . ."
        elif Partner == KittyX:
            ch_k "I guess I could. . ."
        elif Partner == EmmaX:
            ch_e "I suppose she'd do the same for me."
        elif Partner == LauraX:
            ch_l "I guess someone has to."
        elif Partner == JeanX:
            ch_j "Fine, whatever."
        elif Partner == StormX:
            ch_s "I suppose that I could. . ."
        elif Partner == JubesX:
            ch_v "Sure. . ."
    elif lineNum == 6:

        if Partner == RogueX:
            ch_r "I can wipe her off, I guess, but that's it. . ."
        elif Partner == KittyX:
            ch_k "I'm not {i}that{/i} catlike. . ."
        elif Partner == EmmaX:
            ch_e "I'll just use my hands, if you don't mind."
        elif Partner == LauraX:
            ch_l "I don't know, I'll just use my hands."
        elif Partner == JeanX:
            ch_j "I'm not doing that, but I guess I can clean her off."
        elif Partner == StormX:
            ch_s "I will wipe her clean, but not. . . with my tongue."
        elif Partner == JubesX:
            ch_v "I guess I could just wipe her off. . ."
    elif lineNum == 7:

        if Partner == RogueX:
            ch_r "Well, that's y'all's business. . ."
        elif Partner == KittyX:
            ch_k "No way."
        elif Partner == EmmaX:
            ch_e "I'm afraid not, [EmmaX.player_petname]."
        elif Partner == LauraX:
            ch_l "I'd rather not."
        elif Partner == JeanX:
            ch_j "I don't think so. . ."
        elif Partner == StormX:
            ch_s ". . . I will not."
        elif Partner == JubesX:
            ch_v "Sure. . ."
    if not Girl:
        return

    elif lineNum == 8:

        if Girl == RogueX:
            ch_r "Well, how could I turn down such an attractive offer. . ."
        elif Girl == KittyX:
            ch_k "I mean[KittyX.like]she seems so into it. . ."
        elif Girl == EmmaX:
            ch_e "I'll allow it, since she seems so excited by it. . ."
        elif Girl == LauraX:
            ch_l "I could do worse than her."
        elif Girl == JeanX:
            ch_j "Well. . . if we have to. . ."
        elif Girl == StormX:
            ch_s "That would be lovely, [Partner.name]."
        elif Partner == JubesX:
            ch_v "Cool. . ."
    elif lineNum == 9:

        if Girl == RogueX:
            ch_r "If that's what turns you on. . ."
        elif Girl == KittyX:
            ch_k "I guess if you wanna. . ."
        elif Girl == EmmaX:
            ch_e "I'll allow it, if you're that interested. . ."
        elif Girl == LauraX:
            ch_l "Sure, if you're into that."
        elif Girl == JeanX:
            ch_j "Oh, is that what you like? . ."
        elif Girl == StormX:
            ch_s "I could do that."
        elif Partner == JubesX:
            ch_v "Sure. . ."
    elif lineNum == 10:

        if Girl == RogueX:
            ch_r "Kinda ganging up on me here. . ."
        elif Girl == KittyX:
            ch_k "I feel totally targetted."
        elif Girl == EmmaX:
            ch_e "Oh, fine, don't the both of you look at me like that."
        elif Girl == LauraX:
            ch_l "More the merrier."
        elif Girl == JeanX:
            ch_j "Sure. . ."
        elif Girl == StormX:
            ch_s "That might be. . . nice."
        elif Partner == JubesX:
            ch_v "Cool. . ."
    elif lineNum == 11:

        if Girl == RogueX:
            ch_r "I'm just not that kinda girl. . ."
        elif Girl == KittyX:
            ch_k "Kinda gross, no."
        elif Girl == EmmaX:
            ch_e "I just can't be party to that."
        elif Girl == LauraX:
            ch_l "Hm. . . nah."
        elif Girl == JeanX:
            ch_j "No thanks."
        elif Girl == StormX:
            ch_s ". . . I would rather not."
        elif Partner == JubesX:
            ch_v "Um. . ."
    elif lineNum == 12:

        if Girl == RogueX:
            ch_r "I wouldn't mind some help. . ."
        elif Girl == KittyX:
            ch_k "How could I say no?"
        elif Girl == EmmaX:
            ch_e "Oh, very well. . ."
        elif Girl == LauraX:
            ch_l "If you're offering. . ."
        elif Girl == JeanX:
            ch_j "Well. . . if I have to. . ."
        elif Girl == StormX:
            ch_s ". . . Fine."
        elif Partner == JubesX:
            ch_v "Cool. . ."
    elif lineNum == 13:

        if Girl == RogueX:
            ch_r "Well that was a treat. . ."
        elif Girl == KittyX:
            ch_k "That was. . . real nice."
        elif Girl == EmmaX:
            ch_e "Mmmm, I might need to have you over more often."
        elif Girl == LauraX:
            ch_l "You're really good at that."
        elif Girl == JeanX:
            ch_j "Good job. . ."
        elif Girl == StormX:
            ch_s "Well. . . thank you. . . [Partner.name]."
        elif Partner == JubesX:
            ch_v "Oh, um, thanks, I guess. . ."
    elif lineNum == 14:

        if Girl == RogueX:
            ch_r "Piece of cake, heh. . ."
        elif Girl == KittyX:
            ch_k "Um, thanks."
        elif Girl == EmmaX:
            ch_e "Thank you, dear, I hope that wasn't too much bother."
        elif Girl == LauraX:
            ch_l "That was easy."
        elif Girl == JeanX:
            ch_j "I guess that was. . . thorough. . ."
        elif Girl == StormX:
            ch_s "Well. . . thank you. . . [Partner.name]."
        elif Partner == JubesX:
            ch_v "Oh, um, thanks, I guess. . ."
    return

label Partner_Clean_Girl(Girl=0):


    if Choice != "partner wipe" and Choice != "partner lick":
        return

    if Choice == "partner lick":
        $ Partner.change_face("tongue")
    else:
        $ Partner.spunk["hand"] = True
    $ counter = 0
    if Girl.spunk["chin"] or Girl.spunk["mouth"]:
        while Girl.spunk["chin"]:
            $ Girl.spunk["chin"] = False
        $ Girl.check_if_likes(Partner, 900, 2, 1)
        $ Partner.check_if_likes(Girl, 900, 2, 1)
        if Choice == "partner lick":
            if not Partner.spunk["mouth"]:
                $ Partner.spunk["mouth"] = True
            if not Partner.spunk["chin"]:
                $ Partner.spunk["chin"] = True
            call change_Girl_stat(Partner, "lust", 3)
            call change_Girl_stat(Girl, "lust", 4)
            call change_Player_stat("focus",80,3)
            "[Partner.name] licks her way up [Girl.name]'s chin, before deeply kissing her."
        else:
            call change_Girl_stat(Girl, "lust", 2)
            "[Partner.name] wipes her thumb across [Girl.name]'s chin, "
        $ counter += 1
    if Girl.spunk["mouth"] and counter:
        $ Girl.spunk["mouth"] = False
        "you can see a line of jizz stretching between their mouths."
        $ counter += 1
    if Girl.spunk["hair"]:
        $ Girl.spunk["hair"] = False
        if counter:
            "then she wipes the spunk out of [Girl.name]'s hair, "
        else:
            "[Partner.name] wipes the spunk out of [Girl.name]'s hair, "
        $ counter += 1
    if Girl.spunk["face"]:
        $ Girl.spunk["face"] = False
        if Choice == "partner lick":
            if not Partner.spunk["mouth"]:
                $ Partner.spunk["mouth"] = True
            if not Partner.spunk["chin"]:
                $ Partner.spunk["chin"] = True
            call change_Girl_stat(Partner, "lust", 2)
            call change_Girl_stat(Girl, "lust", 4)
            call change_Player_stat("focus",80,3)
            if counter:
                "then she licks the spunk off of [Girl.name]'s face, "
            else:
                "[Partner.name] licks the spunk off of [Girl.name]'s face, "
        else:
            call change_Girl_stat(Girl, "lust", 1)
            if counter:
                "then she wipes the spunk off of [Girl.name]'s face, "
            else:
                "[Partner.name] wipes the spunk off of [Girl.name]'s face, "
        $ counter += 1
    if Girl.spunk["breasts"]:
        $ Girl.spunk["breasts"] = False
        $ Girl.check_if_likes(Partner, 900, 2, 1)
        if Choice == "partner lick":
            if not Partner.spunk["mouth"]:
                $ Partner.spunk["mouth"] = True
            if not Partner.spunk["chin"]:
                $ Partner.spunk["chin"] = True
            call change_Girl_stat(Partner, "lust", 2)
            call change_Girl_stat(Girl, "lust", 4)
            call change_Player_stat("focus",80,4)
            if counter:
                "then she licks her way across [Girl.name]'s chest, "
            else:
                "[Partner.name] licks her way across [Girl.name]'s chest, "
        else:
            call change_Girl_stat(Partner, "lust", 2)
            call change_Girl_stat(Girl, "lust", 2)
            call change_Player_stat("focus",80, 2)
            if counter:
                "then she wipes the spunk off of [Girl.name]'s chest, "
            else:
                "[Partner.name] wipes the spunk off of [Girl.name]'s chest, "
        $ counter += 1
    if Girl.spunk["belly"]:
        $ Girl.spunk["belly"] = False
        if Choice == "partner lick":
            if not Partner.spunk["mouth"]:
                $ Partner.spunk["mouth"] = True
            if not Partner.spunk["chin"]:
                $ Partner.spunk["chin"] = True
            call change_Girl_stat(Partner, "lust", 2)
            call change_Girl_stat(Girl, "lust", 3)
            call change_Player_stat("focus",80, 1)
            if counter:
                "then she licks her way down [Girl.name]'s belly, "
            else:
                "[Partner.name] licks her way down [Girl.name]'s belly, "
        else:
            call change_Girl_stat(Partner, "lust", 1)
            call change_Girl_stat(Girl, "lust", 1)
            if counter:
                "then she wipes the spunk off of [Girl.name]'s belly, "
            else:
                "[Partner.name] wipes the spunk off [Girl.name]'s belly, "
        $ counter += 1
    if Girl.spunk["back"]:
        $ Girl.spunk["back"] = False
        if Choice == "partner lick":
            if not Partner.spunk["mouth"]:
                $ Partner.spunk["mouth"] = True
            if not Partner.spunk["chin"]:
                $ Partner.spunk["chin"] = True
            call change_Girl_stat(Girl, "lust", 2)
            if counter:
                "then she licks her way up [Girl.name]'s lower back, "
            else:
                "[Partner.name] licks her way up [Girl.name]'s lower back, "
        else:
            call change_Girl_stat(Girl, "lust", 1)
            if counter:
                "then she wipes the spunk off of [Girl.name]'s lower back, "
            else:
                "[Partner.name] wipes the spunk off [Girl.name]'s lower back, "
        $ counter += 1
    if Girl.spunk["pussy"]:
        $ Girl.spunk["pussy"] = False
        $ Girl.check_if_likes(Partner, 900, 5, 1)
        if Choice == "partner lick":
            if not Partner.spunk["mouth"]:
                $ Partner.spunk["mouth"] = True
            if not Partner.spunk["chin"]:
                $ Partner.spunk["chin"] = True
            call change_Girl_stat(Partner, "lust", 4)
            call change_Girl_stat(Girl, "lust", 6)
            call change_Player_stat("focus",80, 6)
            if counter:
                "then she sucks gently at [Girl.name]'s pussy, "
            else:
                "[Partner.name] bends down and sucks gently at [Girl.name]'s pussy, "
        else:
            call change_Girl_stat(Partner, "lust", 2)
            call change_Girl_stat(Girl, "lust", 4)
            call change_Player_stat("focus",80,4)
            if counter:
                "then she strokes along [Girl.name]'s pussy, wiping the spunk clean, "
            else:
                "[Partner.name] strokes along [Girl.name]'s pussy, wiping the spunk clean, "
        $ counter += 1
    if Girl.spunk["anus"]:
        $ Girl.spunk["anus"] = False
        $ Girl.check_if_likes(Partner, 900, 5, 1)
        if Choice == "partner lick" and approval_check(Partner, 800, "I"):
            if not Partner.spunk["mouth"]:
                $ Partner.spunk["mouth"] = True
            if not Partner.spunk["chin"]:
                $ Partner.spunk["chin"] = True
            call change_Girl_stat(Partner, "lust", 2)
            call change_Girl_stat(Girl, "lust", 6)
            call change_Player_stat("focus",80, 5)
            if counter:
                "then she licks up the spunk dripping out of [Girl.name]'s ass, "
            else:
                "[Partner.name] licks up the spunk dripping our of [Girl.name]'s ass, "
        else:
            call change_Girl_stat(Partner, "lust", 2)
            call change_Girl_stat(Girl, "lust", 6)
            call change_Player_stat("focus",80,3)
            if counter:
                "then she wipes the spunk dripping out of [Girl.name]'s ass, discarding it, "
            else:
                "[Partner.name] wipes the spunk dripping our of [Girl.name]'s ass, discarding it, "
        $ counter += 1

    $ Partner.change_face("sly")
    if Girl.spunk["hand"]:
        $ Girl.spunk["hand"] = False
        if Choice == "partner lick":
            if not Partner.spunk["mouth"]:
                $ Partner.spunk["mouth"] = True
            if not Partner.spunk["chin"]:
                $ Partner.spunk["chin"] = True
            call change_Girl_stat(Girl, "lust", 3)
            call change_Player_stat("focus",80,3)
            if counter:
                "and finally she licks [Girl.name]'s hands off with a satisfied grin."
            else:
                "[Partner.name] licks [Girl.name]'s fingertips with a satisfied grin."
        else:
            if counter:
                "and finally she wipes [Girl.name]'s hands clean."
            else:
                "[Partner.name] wipes [Girl.name]'s hands off with a satisfied grin."

        if Choice == "partner lick" or approval_check(Partner, 1000):

            while Partner.spunk["mouth"]:
                $ Partner.spunk["mouth"] = False
            while Partner.spunk["chin"]:
                $ Partner.spunk["chin"] = False
            call change_Girl_stat(Girl, "inhibition", 2)
            call change_Player_stat("focus",80,3)
            "Then [Partner.name] swallows and wipes her mouth."
            $ Partner.permanent_History["swallowed"] += 1
            $ Partner.addiction -= (10*counter)
            if Partner.permanent_History["swallowed"] == 1:
                $ Partner.SEXP += 12
            $ Partner.recent_history.append("swallowed")
            $ Partner.daily_history.append("swallowed")
        else:

            if counter:
                "and finally, she wipes her own hands off with a nearby tissue."
            else:
                "[Partner.name] wipes her own hands off with a nearby tissue."
        $ counter += 1

        python:
            for key in Girl.spunk.keys():
                Girl.spunk[key] = False

            for key in Partner.spunk.keys():
                Partner[0].spunk[key] = False

    return
