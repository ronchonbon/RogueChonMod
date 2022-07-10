label classroom_seating:
    call set_the_scene(location = "bg_classroom", fade = True)

    python:
        Girls = Present[:]

        for G in reversed(Girls):
            if G in [EmmaX, StormX]:
                Girls.remove(G)
            elif G in Player.Party:
                Girls.remove(G)

        renpy.random.shuffle(Girls)

    $ Present = Player.Party if Player.Party else []

    if len(Girls) == 2:
        $ D20 = renpy.random.randint(500, 1500)

        if Girls[0].likes[Girls[1].tag] + Girls[1].likes[Girls[0].tag] >= D20:
            "You see that [Girls[0].name] and [Girls[1].name] are sitting next to each other, which do you sit next to?"
        else:
            "You see that [Girls[0].name] and [Girls[1].name] are in the room, but on opposite sides."

        menu:
            "Who do you want to sit next to?"
            "[Girls[0].name].":
                $ Present.append(Girls[0])
            "[Girls[1].name].":
                $ Present.append(Girls[1])
            "Between them." if not Nearby:
                $ Present.append(Girls[0])
                $ Present.append(Girls[1])
            "Neither":
                "You decide to sit a distance away from either of them."
    elif len(Girls) > 2:
        $ flag = False

        while not flag:
            menu:
                "You see several girls are in the room, who would you like to sit near?"
                "[RogueX.name]" if RogueX in Girls and RogueX not in Present:
                    $ Present.append(RogueX)
                "[KittyX.name]" if KittyX in Girls and KittyX not in Present:
                    $ Present.append(KittyX)
                "[LauraX.name]" if LauraX in Girls and LauraX not in Present:
                    $ Present.append(LauraX)
                "[JeanX.name]" if JeanX in Girls and JeanX not in Present:
                    $ Present.append(JeanX)
                "[JubesX.name]" if JubesX in Girls and JubesX not in Present:
                    $ Present.append(JubesX)
                "Done":
                    $ flag = True
    elif Girls:
        menu:
            "You see [Girls[0].name] is there, do you sit next to her?"
            "Yes.":
                $ Present.append(Girls[0])
            "No, I'll sit away from her a bit.":
                pass

    python:
        for G in Girls:
            if G not in Present:
                Nearby.append(G)

                G.location = "nearby"

    if Present and Player.focused_Girl not in Present:
        $ shift_focus(Present[0])

    if len(Present) > 2:
        "You figure out seating arrangements with the girls."
    elif len(Present) == 2:
        "You look for a seat between [Present[0].name] and [Present[1].name]."
    elif len(Present) == 1:
        "You look for a seat next to [Present[0].name]."
    else:
        "You look for a seat off to the side."

    call set_the_scene

    if len(Girls) > len(Present):
        "The rest are scattered around the room."

    return

label take_class:
    # if "met" not in EmmaX.history and day >= 1:
    #     call meet_Emma
    #
    #     return

    if round >= 80:
        $ line = "You make it in time for the start of the class."
    elif round >= 50:
        $ line = "You get in a bit late, but there's plenty of class left."
    else:
        $ line = "You're pretty late, but catch the tail end of the class."

    $ renpy.random.shuffle(Present)

    $ D20 = renpy.random.randint(1, 20)

    # if D20 > 15 and Present and approval_check(Present[0], 300, "I"):
    #     "[line]"
    #
    #     call frisky_class(Present[0])
    if True:
        $ line = line + renpy.random.choice([
            " It was fairly boring.",
            " It was a lesson in mutant biology.",
            " You took a math course.",
            " You watched a movie about sealions.",
            " That was fun.",
            " Applied trigonometry is surprisingly interesting, especially when Cyclops demonstrates using it for trick shots.",
            " Geopolitical science: Latveria to Madripoor.",
            " Today's lecture is on reading body language. You suppose if anyone would know about reading people. . .",
            " The topic of the day is Mutants and the larger superhuman community.",
            " Capes: What Your name and Costume Say About You turns out to be pretty lively as you participate in a debate on costume designs.",
            " The topic is \"Mutants VS Mutates.\" As it turns out, the terms aren’t interchangeable.",
            " Today's class is on how to present yourself to the public. She uses Spider-Man as an example of how bad PR makes your life harder than it needs to be.",
            " Mutant History, Apocalypse to Dark Phoenix.",
            " You spend some time learning about politics. Senator Trask seems like a real piece of work.",
            " You spend class learning about Aristotelian philosophy. Or about your teacher's breasts.",
            " You learn how civil laws apply to mutant powers by studying some high profile case studies. It's surprisingly interesting.",
            " You listen as a guest speaker describes working with a Genosha-based NGO trying to rehabilitate mutants in the States.",
            " Today the teacher is describing the theory behind mutant powers. For some reason, you get the impression she is glancing at you during the lecture.",
            " Game writing for dummies, eh?"])

        "[line]"

    $ Player.XP += 5 + int(round/10)

    return











label frisky_class(Girl):
    $ shift_focus(Girl)
    call set_the_scene

    if EmmaX.teaching:
        "[EmmaX.name] is giving a lecture on mutant relations. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."

        $ Teacher = EmmaX
    elif StormX.teaching:
        "[StormX.name] is giving a lecture on geography and politics. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."

        $ Teacher = StormX
    else:
        "Professor McCoy is giving a lecture on the X-Gene. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."

    "Occasionally, you catch her glancing over your way."
    "[Girl.name] opens her notebook and begins scratching out a note."
    "She detaches the slip of paper from the binder, carefully folding it before sliding it in front of you."
    "She watches you as you unfold the note."

    if "friskyclass" in Girl.history:
        menu:
            "It reads \"Did you want to fool around again? Y[[] N[[]\""
            "Y":
                $ Girl.change_face("sly", 1)
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "inhibition", 3)

                "She smiles suggestively."

                $ D20 = renpy.random.randint(1, 15)

                jump frisky_class_loop
            "N":
                call change_Girl_stat(Girl, "love", -10)
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 5)
                call change_Girl_stat(Girl, "inhibition", -3)

                $ Girl.change_face("angry")

                call frisky_class_end(Girl, context = "rejected")

                if Teacher:
                    $ Teacher.drain_word("frisky", 1, 0)

                return

    if Girl == RogueX:
        "In looping penstrokes, it reads: \"You like biology?\""
    elif Girl == KittyX:
        "In girly penstrokes, it reads: \"biology?\""
    elif Girl == LauraX:
        "In roughly formed penstrokes, it reads: \"Boring, right?\""
    elif Girl == JeanX:
        "In sloppy penstrokes, it reads: \"kinda dull\"."
    elif Girl == JubesX:
        "In flashy penstrokes, it reads: \"Totally boring?\""

    if Girl in [RogueX, KittyX]:
        $ Girl.change_face("smile", 2)

        "You look back and see that she's blushing slightly."
        "She slides her pen over to you so you can reply."

        $ Girl.change_face("smile", 1)
    else:
        $ Girl.change_face("sly", 1)

        "You look back and see that she's staring at you suggestively."
        "She slides her pen over to you so you can reply."

    menu:
        "You reply. . ."
        "What are you talking about?":
            call frisky_class_end(Girl, context = "ignored")

            if Teacher:
                $ Teacher.drain_word("frisky", 1, 0)

            return
        "Nah, not so much." if Girl == RogueX:
            $ Girl.change_face("confused")
            call change_Girl_stat(Girl, "love", -3)
            call change_Girl_stat(Girl, "inhibition", -3)

            call frisky_class_end(Girl, context = "ignored")

            if Teacher:
                $ Teacher.drain_word("frisky", 1, 0)

            return
        "It's my favorite subject." if Girl in [RogueX, KittyX]:
            $ Girl.change_face("smile")
            call change_Girl_stat(Girl, "love", 5)

            "[Girl.name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could study together tonight?\"."

            $ context = "continue"
        "Yeah, pretty lame." if Girl != RogueX:
            $ Girl.change_face("smile")
            call change_Girl_stat(Girl, "love", 5)

            "[Girl.name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could 'study' together tonight?\"."

            $ context = "continue"
        "I do when it's about you." if Girl == RogueX:
            $ context = "her"
        "I was too busy thinking about you." if Girl != RogueX:
            $ context = "her"

    if context == "her":
        if approval_check(Girl, 500, "I") or Girl.SEXP >= 30:
            $ Girl.change_face("sly")

            "[Girl.name] reads your note and smiles at you suggestively."

            $ context = "flirt"
        elif approval_check(Girl, 900):
            if Girl in [RogueX, KittyX]:
                $ Girl.change_face("confused", 2)

                "[Girl.name] reads your note and blushes furiously, looking down at her notes."
            else:
                $ Girl.change_face("sly", 1)

                "[Girl.name] reads your note and gets a sly smile, looking down at her notes."

            $ Girl.change_face("bemused", 1)

            $ context = "flirt"
        else:
            if Girl in [RogueX, KittyX]:
                $ Girl.change_face("perplexed", 2)

                "[Girl.name] reads your note and blushes furiously. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could study tonight?\"."
            else:
                $ Girl.change_face("sly", 1)

                "[Girl.name] reads your note and gets a sly smile. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could 'study' tonight?\"."

            $ Girl.change_face("bemused", 1)

            $ context = "continue"

    if context == "continue":
        "She's trying to act like she's paying attention to the lecture, but she can't hide the big smile on her face."

        menu:
            "You respond. . ."
            "Maybe later.":
                $ Girl.change_face("confused")
                call change_Girl_stat(Girl, "love", -3)
                call change_Girl_stat(Girl, "obedience", 5)
                call change_Girl_stat(Girl, "inhibition", -3)

                call frisky_class_end(Girl, context = "later")

                if Teacher:
                    $ Teacher.drain_word("frisky", 1, 0)

                return
            "Nah. I've got better things to do.":
                $ Girl.change_face("angry")
                call change_Girl_stat(Girl, "love", -10)
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 5)
                call change_Girl_stat(Girl, "inhibition", -3)
                $ Girl.daily_history.append("angry")

                call frisky_class_end(Girl, context = "rejected")

                if Teacher:
                    $ Teacher.drain_word("frisky", 1, 0)

                return
            "Count on it.":
                $ Girl.change_face("smile")

                "She smiles when she reads your reply, and throws you a wink."

                $ Girl.daily_history.append("studydate")

                "The rest of class is uneventful."

                return
            "We could get some \"studying\" done right now.":
                if approval_check(Girl, 1000):
                    $ Girl.change_face("sly", 1)
                    call change_Girl_stat(Girl, "love", 3)
                    call change_Girl_stat(Girl, "inhibition", 3)

                    "[Girl.name] gets a mischevious grin on her face and leans towards you."

                    $ context = "flirt"
                elif approval_check(Girl, 700):
                    $ Girl.change_face("smile", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)

                    if Girl in [RogueX, KittyX]:
                        "[Girl.name] blushes and smiles your way."
                    else:
                        "[Girl.name] startles a bit and smiles your way."

                    $ context = "flirt"
                else:
                    $ Girl.change_face("confused", 1)

                    "[Girl.name] looks a bit surprised, then scowls at you."

                    call frisky_class_end(Girl, context = "proposition")

                    if Teacher:
                        $ Teacher.drain_word("frisky", 1, 0)

                    return

    if context == "flirt":
        $ round -= 20

        $ D20 = renpy.random.randint(1, 15)

        $ Girl.change_face("sly")

        "You notice one of [Girl.name]'s shoes slip from her foot beneath the desk. She tosses you a sly grin."

        if Girl.Clothes["hose"]:
            "You feel the smooth texture of her covered foot begin to slowly slide back and forth along the length of your calf."
        else:
            "You feel the smooth skin of her bare foot begin to slowly slide back and forth along the length of your calf."

        while D20 <= 21 or "go on" in Player.recent_history:
            menu frisky_class_loop:
                "Pull away from her.":
                    if context == "fondle_pussy":
                        "You slowly slide your hand from her lap and start taking notes again."

                        $ context = "tease"
                    elif context == "fondle_breast":
                        "With a final squeeze, you move your hand back to the desktop."

                        $ context = "tease"
                    elif Girl.session_orgasms and Girl.lust < 90:
                        "That'll probably do for now. . ."

                        $ context = "tease"
                    else:
                        call change_Girl_stat(Girl, "love", -15)
                        call change_Girl_stat(Girl, "obedience", 2)
                        call change_Girl_stat(Girl, "inhibition", -2)

                    call frisky_class_end(Girl, context = "rejected")

                    if Teacher:
                        $ Teacher.drain_word("frisky", 1, 0)

                    return
                "Look into her eyes and smile slightly." if context == "flirt":
                    $ Girl.change_face("smile")
                    call change_Girl_stat(Girl, "love", 5)

                    "[Girl.name] smiles back."
                    "She looks back towards the front of the class, but her hand drifts across the top of the desk until she's holding yours."

                    $ context = "handholding"

                    jump frisky_class_loop
                "Grasp her hand gently, stroking the top of it." if context == "handholding":
                    $ Girl.change_face("smile")
                    call change_Girl_stat(Girl, "love", 5)
                    call change_Girl_stat(Girl, "lust", 5)

                    "[Girl.name] sighs contentedly and holds your hand for the remainder of class."

                    call frisky_class_end(Girl, context = "handholding")

                    if Teacher:
                        $ Teacher.drain_word("frisky", 1, 0)

                    return
                "Try and slip your hand to her lap." if context != "fondle_pussy":
                    $ context = "fondle_pussy"

                    if approval_check(Girl, 1200) and Girl.permanent_History["fondle_pussy"] and Girl.SEXP >= 40:
                        $ Girl.change_face("sly")
                        call change_Girl_stat(Girl, "love", 5)
                        call change_Girl_stat(Girl, "obedience", 5)
                        call change_Girl_stat(Girl, "inhibition", 5)

                        "[Girl.name] gets a mischievous grin and places her hand on your arm."
                    elif approval_check(Girl, 1400) and Girl.permanent_History["fondle_pussy"]:
                        $ Girl.change_face("smile")
                        call change_Girl_stat(Girl, "love", 3)
                        call change_Girl_stat(Girl, "obedience", 7)
                        call change_Girl_stat(Girl, "inhibition", 3)

                        "[Girl.name] starts slightly as your hand travels up her thigh, but then she lets out a slight grin."
                    elif approval_check(Girl, 1500):
                        $ Girl.change_face("perplexed", 2)
                        call change_Girl_stat(Girl, "obedience", 10)
                        call change_Girl_stat(Girl, "inhibition", 3)

                        "[Girl.name] glances at you in alarm, but then slowly calms down."

                        $ Girl.change_face("smile", 1)

                        $ D20 += 2
                    else:
                        $ context = "too far"

                    if context == "fondle_pussy":
                        $ Girl.change_face("sly")
                        call change_Girl_stat(Girl, "lust", 5)

                        if Girl.Clothes["skirt"]:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak under the hem of her [Girl.Clothes[skirt].name], slowly tracing the soft contours of her mound."
                        elif Girl.Clothes["pants"]:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak down her [Girl.Clothes[pants].name], slowly tracing the soft contours of her mound."
                        else:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak between her legs, slowly tracing the soft contours of her mound."

                        call change_Girl_stat(Girl, "lust", 5)

                        if Girl.Clothes["underwear"]:
                            "You think her [Girl.Clothes[underwear].name] are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif Girl.pubes:
                            "You feel her soft fur moisten as you stroke the soft flesh below. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        else:
                            "You feel her lips moisten as you stroke the soft flesh. Her cheeks are flushed and her breathing's starting to become shallower and quicker."

                        $ Player.primary_Action = ActionClass("fondle_pussy", Target = Girl)

                        $ D20 += 5
                "Keep fondling her pussy." if context == "fondle_pussy":
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 3)
                    call change_Girl_stat(Girl, "lust", 5)
                    call change_Girl_stat(Girl, "lust", 5)

                    $ line = renpy.random.choice([
                        "As the class drones on, you continue to slowly massage her warm delta.",
                        "As the class continues, you continue to slowly massage her moist pussy.",
                        "As the lecture drones on, you continue to slowly stroke her clit.",
                        "As the class continues, you continue to slowly caress her labia."])

                    "[line]"

                    $ D20 += 5
                "Start fondling her tits." if context != "fondle_breasts":
                    $ context = "fondle_breasts"

                    if approval_check(Girl, 1100) and Girl.permanent_History["fondle_breasts"]and Girl.SEXP >= 40:
                        $ Girl.change_face("sly")
                        call change_Girl_stat(Girl, "love", 5)
                        call change_Girl_stat(Girl, "obedience", 5)
                        call change_Girl_stat(Girl, "inhibition", 3)

                        "[Girl.name] closes her eyes and caresses your arm."
                    elif approval_check(Girl, 1300) and Girl.permanent_History["fondle_breasts"]:
                        $ Girl.change_face("smile", 1)
                        call change_Girl_stat(Girl, "love", 3)
                        call change_Girl_stat(Girl, "obedience", 7)
                        call change_Girl_stat(Girl, "inhibition", 3)

                        "[Girl.name] flinches as your hand travels up her ribcage, but she grins as you reach her breast."
                    elif approval_check(Girl, 1400):
                        $ Girl.change_face("perplexed", 2)
                        call change_Girl_stat(Girl, "obedience", 10)
                        call change_Girl_stat(Girl, "inhibition", 3)

                        "[Girl.name] glances at you in alarm, but then slowly calms down."

                        $ Girl.change_face("smile", 2)

                        $ D20 += 5
                    else:
                        $ context = "too far"

                    if context == "fondle_breasts":
                        $ Girl.change_face("sly")
                        call change_Girl_stat(Girl, "lust", 5)

                        "[Girl.name]'s sly eyes spakle as your hand cups her breast, giving it a casual caress."
                        "Her nipples begin to firm up and she lets out a small moan of pleasure."

                        $ Player.primary_Action = ActionClass("fondle_breasts", Target = Girl)

                        $ D20 += 7
                "Keep fondling her tits." if context == "fondle_breasts":
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    call change_Girl_stat(Girl, "lust", 3)

                    "Barely paying attention to the lecture, you continue to pulse her breast in your palm."

                    $ D20 += 7
                "Try and pull her hand toward your lap." if not Girl.primary_Action and Player.semen:
                    $ context = "handjob"

                    if "handjob" in Girl.recent_history:
                        "[Girl.name] grins and her hand grasps your cock again."
                    elif approval_check(Girl, 1200) and Girl.permanent_History["handjob"] and Girl.SEXP >= 40:
                        $ Girl.change_face("sly")
                        call change_Girl_stat(Girl, "love", 5)
                        call change_Girl_stat(Girl, "obedience", 5)
                        call change_Girl_stat(Girl, "inhibition", 5)

                        "[Girl.name] gets a mischievous grin and her hand starts to caress your crotch."
                    elif approval_check(Girl, 1400) and Girl.permanent_History["fondle_pussy"]:
                        $ Girl.change_face("smile")
                        call change_Girl_stat(Girl, "love", 3)
                        call change_Girl_stat(Girl, "obedience", 7)
                        call change_Girl_stat(Girl, "inhibition", 3)

                        "[Girl.name] starts slightly as your move her hand up your thigh, but then she lets out a slight grin."
                    elif approval_check(Girl, 1500):
                        $ Girl.change_face("perplexed", 2)
                        call change_Girl_stat(Girl, "obedience", 10)
                        call change_Girl_stat(Girl, "inhibition", 3)

                        "[Girl.name] glances at you in alarm, but then slowly calms down."

                        $ Girl.change_face("smile", 1)

                        $ D20 += 2
                    else:
                        $ context = "too far"

                    if context == "handjob":
                        $ Girl.change_face("sly")

                        call change_Girl_stat(Girl, "lust", 5)

                        if "cockout" not in Player.recent_history:
                            "[Girl.name]'s hand slowly unzips your pants and pulls your cock free."

                            $ Player.add_word(1, "cockout")

                            call Seen_First_Peen (Girl, Partner)
                            call change_Girl_stat(Girl, "lust", 5)

                        $ Girl.primary_Action = ActionClass("handjob", Target = Player)
                        $ Girl.recent_history.append("handjob")
                        $ Girl.daily_history.append("handjob")

                        "She begins to gently stroke it. . ."

                        if "handjob" not in Girl.recent_history:
                            $ Girl.permanent_History["handjob"] += 1

                        $ D20 += 5
                "Stop her handjob." if Girl.primary_Action and Girl.primary_Action.type == "handjob":
                    "You put a hand on her wrist and nudge her hand away."

                    if approval_check(Girl, 1800) or approval_check(Girl, 700, "O") or Girl.love + Girl.obedience >= 2*Girl.inhibition:
                        $ Girl.change_face("sad")
                        call change_Girl_stat(Girl, "love", -1)
                        call change_Girl_stat(Girl, "obedience", 2)
                        call change_Girl_stat(Girl, "obedience", 3)

                        "[Girl.name] allows her hand to be pulled away and goes back to what she'd been doing with it."

                        $ Girl.change_face("sly")

                        $ Girl.primary_Action = None
                    else:
                        $ Girl.change_face("angry")
                        call change_Girl_stat(Girl, "love", -3)
                        call change_Girl_stat(Girl, "love", -1)
                        call change_Girl_stat(Girl, "obedience", -2)
                        call change_Girl_stat(Girl, "inhibition", 3)
                        call change_Girl_stat(Girl, "inhibition", 2)

                        "[Girl.name] grasps your cock tightly, then continues to stroke it when you let go."

                        $ Girl.change_face("sly")

                        $ D20 += 2

            if not Girl.primary_Action and Player.semen and "stophand" not in Girl.recent_history:
                if approval_check(Girl, 1200) and approval_check(Girl, 400, "I") and Girl.permanent_History["handjob"] and Girl.SEXP >= 40:
                    $ Girl.change_face("sly")

                    "[Girl.name] gets a mischievous grin and her hand starts to caress your crotch."
                    menu:
                        "What do you do?"
                        "Let her.":
                            "You smile and nod a little."

                            $ Girl.change_face("sly")
                            call change_Girl_stat(Girl, "love", 1)
                            call change_Girl_stat(Girl, "inhibition", 3)
                            call change_Girl_stat(Girl, "inhibition", 2)
                            call change_Girl_stat(Girl, "lust", 5)

                            if "cockout" not in Player.recent_history:
                                "[Girl.name]'s hand slowly unzips your pants and pulls your cock free."

                                $ Player.add_word(1, "cockout")

                                call Seen_First_Peen (Girl, Partner)
                                call change_Girl_stat(Girl, "lust", 5)

                            $ Girl.primary_Action = ActionClass("handjob", Target = Girl)
                            $ Girl.recent_history.append("handjob")
                            $ Girl.daily_history.append("handjob")

                            "She begins to gently stroke it. . ."

                            if "handjob" not in Girl.recent_history:
                                $ Girl.permanent_History["handjob"] += 1

                            $ D20 += 10
                        "Stop her.":
                            "You put a hand on her wrist and nudge her hand away."

                            $ Girl.recent_history.append("stophand")

                            if approval_check(Girl, 1800) or approval_check(Girl, 700, "O") or Girl.love + Girl.obedience >= 2*Girl.inhibition:
                                $ Girl.change_face("sad")
                                call change_Girl_stat(Girl, "love", -1)
                                call change_Girl_stat(Girl, "obedience", 2)
                                call change_Girl_stat(Girl, "obedience", 3)

                                "[Girl.name] allows her hand to be pulled away and goes back to what she'd been doing with it."

                                $ Girl.change_face("sly")
                            else:
                                $ Girl.change_face("angry")
                                call change_Girl_stat(Girl, "love", -3)
                                call change_Girl_stat(Girl, "love", -1)
                                call change_Girl_stat(Girl, "obedience", -2)
                                call change_Girl_stat(Girl, "inhibition", 3)
                                call change_Girl_stat(Girl, "inhibition", 2)

                                "[Girl.name] stops, but looks really annoyed."

                                $ D20 += 10

            if Girl.primary_Action and Girl.primary_Action.type == "handjob":
                "[Girl.name]'s hand continues to caress your cock. . ."

                $ Player.climax += 15 if Player.climax < 60 else 10

                if Player.climax >= 100:
                    "As you start to reach your limits, [Girl.name] places a hand over your cock."
                    "You jizz all over her hand."

                    $ Player.semen -= 1

                    if (Girl.permanent_History["blowjob"] and approval_check(Girl, 1200)) or Girl == JubesX:
                        "She quickly licks it all up."

                        $ Girl.addiction -= 20
                        $ Girl.permanent_History["swallowed"] += 1
                        $ Girl.recent_history.append("swallow")
                        $ Girl.daily_history.append("swallow")
                    else:
                        "She quickly wipes her hand off under the desk."

                    call change_Girl_stat(Girl, "lust", 5)

                    $ D20 += 10

                    if not Player.semen:
                        "She continues to lightly stroke you, but you don't seem up to it for now. . ."

                        $ Girl.primary_Action = None

                $ D20 += 5

            if Girl.lust >= 95:
                $ line = context
                call Girl_Cumming (Girl, 1)
                $ context = line

                $ line = renpy.random.choice([
                    Girl.name + " collapses over her desk.",
                    Girl.name + " mumbles something unintelligible.",
                    Girl.name + " bites her lip as she struggles to stay upright.",
                    Girl.name + " seems a bit flushed."])

                "[line]"

                $ D20 += 15

            $ round -= 7

            if round <= 15:
                "Unfortunately it seems like class is wrapping up. You'll have to save this for later. . ."

                call frisky_class_end(Girl, context = "tease")

                if Teacher:
                    $ Teacher.drain_word("frisky", 1, 0)

                return

            if context == "too far":
                $ Girl.change_face("surprised", 2)
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 7)
                call change_Girl_stat(Girl, "inhibition", -3)

                "[Girl.name] sits up straight in her seat and makes a little yelping noise."

                $ Girl.change_face("angry", 1)

                "Between that and the icy glare she shoots you, it's enough to draw the attention of your fellow students in your direction."

                $ D20 += 20

                if "go on" in Player.recent_history:
                    call frisky_class_end(Girl, context = "caught")

                    if Teacher:
                        $ Teacher.drain_word("frisky", 1, 0)

                    return
            else:
                if len(Present) > 1 and D20 >= 15:
                    if Present[1].primary_Action:
                        $ Present[1].likes[Girl.tag] += 2
                        $ Girl.likes[Present[1].tag] += 2

                        call change_Girl_stat(Present[1], "lust", 3)

                        $ line = renpy.random.choice([
                            Present[1].name + " seems into it. . .",
                            Present[1].name + "'s hand moves a bit faster.",
                            Present[1].name + " bites her lip as her hand continues to move.",
                            Present[1].name + "'s hand slows down a bit.",
                            None,
                            None,
                            None])

                        if line:
                            "[line]"

                        if Present[1].lust >= 95:
                            $ line = context
                            call Girl_Cumming(Present[1], 1)
                            $ context = line

                            $ line = renpy.random.choice([
                                Present[1].name + " collapses over her desk.",
                                Present[1].name + " mumbles something unintelligible.",
                                Present[1].name + " bites her lip as she struggles to stay upright.",
                                Present[1].name + " seems a bit flushed."])

                            "[line]"

                            $ D20 += 15
                    elif "saw with " + Girl.tag in Present[1].traits:
                        Present[1].voice "Well!"

                        $ Present[1].likes[Girl.tag] += -4

                        $ Girl.likes[Present[1].tag] += -2

                        call remove_Girl(Present[1])
                    elif approval_check(Present[1], 1500) and Present[1].likes[Girl.tag] >= 600:
                        $ Present[1].eyes = "leftside"

                        "[Present[1].name] seems to notice what you and [Girl.name] are doing."

                        $ Present[1].change_face("sly", 1)

                        "She seems to be kinda into it. . ."

                        if approval_check(Present[1], 800, "I") or "exhibitionist" in Present[1].traits:
                            call change_Girl_stat(Girl, "inhibition", 3)

                            $ Present[1].likes[Girl.tag] += 3

                            $ Girl.likes[Present[1].tag] += 5

                            call change_Girl_stat(Present[1], "lust", 7)

                            "You notice that [Present[1].name]'s begun feeling herself up as well."

                            $ Present[1].add_word(1, "frisky", "frisky", 0, 0)

                            $ Present[1].primary_Action = ActionClass("fondle_pussy", Target = Present[1])
                    else:
                        $ Present[1].eyes = "leftside"

                        "[Present[1].name] seems to notice what you and [Girl.name] are doing."

                        $ Present[1].add_word(1, 0, 0, "saw with " + Girl.tag)
                        $ Present[1].change_face("angry", 1)

                        if Present[1] == RogueX:
                            ch_r "How dare you! Hussy."
                        elif Present[1] == KittyX:
                            ch_k "Hey! . . . HEY!"
                        elif Present[1] == LauraX:
                            ch_l "Cool off, you two."
                        elif Present[1] == JeanX:
                            ch_j "Hey, cut it out."

                        $ Present[1].likes[Girl.tag] += -2

                        $ Girl.likes[Present[1].tag] += -3

                        $ D20 += 15

                        if "go on" in Player.recent_history:
                            call frisky_class_end(Girl, context = "caught")

                            if Teacher:
                                $ Teacher.drain_word("frisky", 1, 0)

                            return

                if Teacher and "frisky" in Teacher.recent_history:
                    $ Teacher.likes[Girl.tag] += 2

                    $ Girl.likes[Teacher.tag] += 2

                    call change_Girl_stat(Teacher, "lust", 3)

                    $ line = renpy.random.choice([
                        Teacher.name + " stumbles a bit over the delivery of the next portion of her lecture.",
                        Teacher.name + "'s hand moves a bit faster.",
                        Teacher.name + " bites her lip as her hand continues to move.",
                        Teacher.name + "'s hand slows down a bit.",
                        None,
                        None,
                        None])

                    if line:
                        "[line]"

                    if Teacher.lust >= 95:
                        $ line = context
                        call Girl_Cumming (Teacher, 1)
                        $ context = line

                        $ line = renpy.random.choice([
                            Teacher.name + " stumbles a bit over the delivery of the next portion of her lecture.",
                            Teacher.name + " mumbles something unintelligible but continues the lecture.",
                            Teacher.name + " bites her lip as she struggles to continue talking.",
                            Teacher.name + " seems a bit under the weather.",
                            Teacher.name + " seems a bit flushed."])

                        "[line]"

                        $ D20 += 15

                if D20 > 30:
                    if D20 >= 50:
                        $ line = renpy.random.choice([
                            "The class isn't paying attention to the lecture anymore.",
                            "The class definitely seems into the show she's putting on.",
                            "The class is hooting and hollering.",
                            "The students seem to be watching you intently.",
                            None,
                            None,
                            None])
                    else:
                        $ line = renpy.random.choice([
                            "The class seems a little confused as to what she's talking about.",
                            "The class seems a little confused as to what she's doing back there.",
                            "The class is shifting strange looks your way.",
                            "A bunch of students seem to be watching you intently.",
                            None,
                            None,
                            None])

                    if line:
                        "[line]"

        if "exhibitionist" not in Girl.traits and not approval_check(Girl, 700, "I"):
            $ context = "too far"

        if context not in ["rejected", "handholding", "tease"]:
            $ Girl.change_face("surprised")

            if Teacher:
                $ Teacher.change_face("surprised", 1)

                "[Teacher.name] stops her lecture in mid-sentence when she notices what you and [Girl.name] are up to."

                if approval_check(Teacher, 1500) and Teacher.likes.[Girl.tag] >= 600:
                    $ Teacher.change_face("sly", 1)

                    if context == "too far":
                        $ Girl.mouth = "sad"

                        if Teacher == EmmaX:
                            "She looks over at you and shrugs as she continues her lecture, but the moment has past."
                        elif Teacher == StormX:
                            "She looks over at you and smiles consolingly as she continues her lecture, but the moment has past."

                        call frisky_class_end(Girl, context = "too far")

                        if Teacher:
                            $ Teacher.drain_word("frisky", 1, 0)

                        return

                    "She gets a sly smile on her face and continues her lecture."

                    $ Girl.change_face("sly", 1)

                    if approval_check(Teacher, 800, "I") or "exhibitionist" in Teacher.traits:
                        call change_Girl_stat(Teacher, "inhibition", 3)

                        $ Teacher.likes[Girl.tag] += 3

                        $ Girl.likes[Teacher.tag] += 5

                        call change_Girl_stat(Teacher, "lust", 7)

                        "You notice that [Teacher.name]'s hand has snaked down beneath the podium and begun to move."

                        $ Teacher.add_word(1, "frisky", "frisky", 0, 0)

                        $ Player.add_word(1, "go on", "go on", 0, 0)

                    "[Girl.name] looks around and shrugs. . ."

                    jump frisky_class_loop
                else:
                    $ Teacher.change_face("angry", 1)

                    $ Girl.mouth = "sad"

                    if Teacher == EmmaX:
                        ch_e "[EmmaX.player_petname], [Girl.name], if you could perhaps pay more attention to the lecture, and less to each other's bodies?"
                        ch_e "Perhaps it would be best if you visited the headmaster's office and cool off?"
                    elif Teacher == StormX:
                        ch_s "[StormX.player_petname], [Girl.name], I can appreciate your enthusaism, but perhaps not on my time?"
                        ch_s "I think perhaps you should visit Charles and cool off?"
            else:
                "Dr. McCoy stops his lecture in mid-sentence when he notices that the whole class is looking at you and [Girl.name]."

                ch_b "Oh, my stars and garters!"
                ch_b "[Player.name]!?! {b}WHAT ARE YOU DOING? BOTH OF YOU, TO THE PROFESSOR'S OFFICE, IMMEDIATELY!{/b}"

            $ Girl.add_word(1, 0, 0, 0, "friskyclass")

            call change_Girl_stat(Girl, "love", -10)
            call change_Girl_stat(Girl, "obedience", -5)
            call change_Girl_stat(Girl, "inhibition", -10)

            call stop_all_Actions

            if Girl not in Rules:
                call caught_having_sex(Girl)
            else:
                "Since Xavier isn't concerned with your activities, you both head back to your room instead."

                if Present[1].primary_Action:
                    $ Party = [Girl, Present[1]]
                else:
                    $ Party = [Girl]

                jump player_room

    call frisky_class_end(Girl, context = context)

    return

label frisky_class_end(Girl, context = None):
    call stop_all_Actions

    if context == "ignored":
        $ Girl.change_face("confused")

        "She unfolds the note and quickly reads it over."

        $ Girl.change_face("sad")

        "As she does, you immediately see disappointment come over her features."
        "She scratches out a reply and slides it back in front of you."
        "When you open it up, it reads: {i}Never mind.{/i}"
        "You both go back to trying to pay attention to the lecture."
    elif context == "tease":
        if Girl.lust >= 80:
            $ Girl.change_face("surprised", 2)

            "[Girl.name] startles briefly."

            $ Girl.change_face("sad", 2)

            "[Girl.name] she looks over at you a bit upset that you ended things so abruptly."

        $ Girl.add_word(1, 0, 0, 0, "friskyclass")
        $ Girl.change_face("sly", 1)

        "[Girl.name] takes in a deep breath and exhales it in a sigh, leaning in to whisper."

        if Girl == RogueX:
            ch_r "Tonight's \"study session\" just got a whole lot more interesting."
        elif Girl == KittyX:
            ch_k "I think we'll have[KittyX.like]a -lot- more fun tonight. . ."
        elif Girl == LauraX:
            ch_l "Tonight we can. . . finish this."
        elif Girl == JeanX:
            ch_j "I guess it can wait until later. . ."
        elif Girl == JubesX:
            ch_v "I'm looking forward to picking this up later. . ."

        "Eventually, [Girl.name] seems to settle down and pay attention to the course material. You manage to do the same without falling asleep."
    elif context == "rejected":
        if Girl in [RogueX, KittyX]:
            $ Girl.change_face("sadside")

            "[Girl.name] looks surprised and hurt. For the rest of the class, she says nothing."
        else:
            $ Girl.change_face("angry")

            "[Girl.name] looks surprised and hurt. For the rest of the class, she stares daggers at you."

        "It seems like she has a hard time looking you in the eye."
        "You both go back to trying to pay attention to the lecture."
    elif context == "caught":
        "You quickly separate and go back to trying to study. . ."
        "Eventually, [Girl.name] seems to settle down and pay attention to the course material. You manage to do the same without falling asleep."
    else:
        "[Girl.name] goes back to trying to pay attention to the course material. You manage to do the same without falling asleep."

    return
