label Class_Room_Entry:
    call Jubes_Entry_Check
    door_locked = False
    $ Present = []
    $ bg_current = "bg_classroom"
    $ Nearby = []
    call Gym_Clothes_Off #call Gym_Clothes
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    call EventCalls
    call set_the_scene(0) #won't display Girls yet)
    $ line = "entry"

label Class_Room:
    $ bg_current = "bg_classroom"
    if "goto" in Player.recent_history or "traveling" in Player.recent_history:
            $ Present = []
            if time_index < 2 and Weekday < 5:   #pre-evening
                    call Class_Room_Seating
            $ Player.DrainWord("goto",1,0)
            $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if time_index >= 3: # night time
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait
                call EventCalls
                call Girls_Location
    call GirlsAngry

    if line == "entry":
            if EmmaX.location == "bg_teacher":
                    $ line = "As you sit down, you see "+ EmmaX.name +" at the podium. What would you like to do?"
            elif StormX.location == "bg_teacher":
                    $ line = "As you sit down, you see "+ StormX.name +" at the podium. What would you like to do?"
            elif time_index == 2 or Weekday > 5: #evening
                    $ line = "You enter the classroom. What would you like to do?"
            else:
                    $ line = "You sit down at a desk. What would you like to do?"
    else:
            if line != "What would you like to do next?":
                    $ line = "You are in class right now. What would you like to do?"
    #End Room Set-up

    menu:
        "[line]"
        "Take the morning class" if Weekday < 5 and time_index == 0:
                if Round >= 30:
                    jump Take_Class
                else:
                    "Class is already letting out. You can hang out until the next one."
        "Take the afternoon class" if Weekday < 5 and time_index == 1:
                if Round >= 30:
                    jump Take_Class
                else:
                    "Class is already letting out. You can hang out until they lock up for the night."
        "There are no classes right now (locked)" if Weekday >= 5 or time_index >= 2:
                pass

        "Chat":
                call Chat
                $ line = "You are in class right now. What would you like to do?"

        "Lock the door" if not door_locked:
                    if Weekday >=5 or time_index >= 2: #evening+
                            "You lock the door"
                            $ door_locked = True
                            call Taboo_Level
                    else:
                            "You can't really do that during class."

        "Unlock the door" if door_locked:
                    "You unlock the door"
                    $ door_locked = False
                    call Taboo_Level

        "Wait" if time_index < 3: #not night time
                "You hang out for a bit."
                call Wait
                call EventCalls
                call Girls_Location

                if time_index < 2: #not evening
                            $ line = "A new class is in session. What would you like to do?"
                else: #evening+
                            $ line = "Classes have let out for the day. What would you like to do?"

        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry

    $ line = 0
    jump Class_Room

label Take_Class:
    call set_the_scene
    if "class" in Player.daily_history:
            $ line = "The session begins."
    elif Round >= 80:
            $ line = "You make it in time for the start of the class."
    elif Round >= 50:
            $ line = "You get in a bit late, but there's plenty of class left."
    elif Round >= 30:
            $ line = "You're pretty late, but catch the tail end of the class."
    $ primary_action = 0

    $ D20 = renpy.random.randint(1, 20)

    if D20 > 15 and Present and ApprovalCheck(Present[0], 300, "I"):
            #if there is another girl in the room, and she is reasonably loose, call Frisky Class
            "[line]"
            call Frisky_Class(Present[0])

    else:
        $ line = line + renpy.random.choice([" It was fairly boring.",
                " It was a lesson in mutant biology.",
                " You took a math course.",
                " You watched a movie about sealions.",
                " That was fun.",
                " Applied trigonometry is surprisingly interesting, especially when Cyclops demonstrates using it for trick shots.",
                " Geopolitical science: Latveria to Madripoor.",
                " Today's lecture is on reading body language. You suppose if anyone would know about reading people. . .",
                " The topic of the day is Mutants and the larger superhuman community.",
                " Capes: What Your Name and Costume Say About You turns out to be pretty lively as you participate in a debate on costume designs.",
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
    $ Player.recent_history.append("class")
    $ Player.daily_history.append("class")
    $ Player.XP += (5 + (int(Round / 10)))

    call Wait
    call Girls_Location
    call set_the_scene
    call EventCalls
    $ line = "What would you like to do next?"
    jump Class_Room

label Class_Room_Seating(Girls=[],GirlB=0,GirlLike=0,line=0,D20=0,Girls=[]):
    # Girls is the amount of girls in the room.
    # active ones get priority, then shuffled, then nearby girls
    $ Present = []
    $ Girls = active_Girls[:]
    while Girls:
        #fills the list with all girls in the room
        if Girls[0].location == bg_current:
                $ Girls.append(Girls[0])
        $ Girls.remove(Girls[0])

    $ renpy.random.shuffle(Girls)

    $ Girls = Nearby[:]
    while Girls:
        # adds any girls nearby to the back of the list
        if Girls[0] not in Girls:
                $ Girls.append(Girls[0])
        $ Girls.remove(Girls[0])

    #End Girl selections

    $ Nearby = []

    call set_the_scene(0) #won't display Girls yet)
    if len(Girls) == 2:
            # there are two girls
            $ D20 = renpy.random.randint(500, 1500)
            if (Girls[0].GirlLikeCheck(Girls[1]) + Girls[1].GirlLikeCheck(Girls[0])) >= D20:
                "You see that [Girls[0].name] and [Girls[1].name] are sitting next to each other, which do you sit next to?"
            else:
                "You see that [Girls[0].name] and [Girls[1].name] are in the room, but on opposite sides."
                $ Girls = Girls[:]
                while Girls:
                    # adds both girls to Nearby
                    if Girls[0] not in Nearby:
                            $ Nearby.append(Girls[0])
                    $ Girls.remove(Girls[0])
            menu:
                extend ""
                "[Girls[0].name]":
                        $ Present = [Girls[0]]
                        if Girls[0] in Nearby:
                                $ Nearby.remove(Girls[0])
                "[Girls[1].name]":
                        $ Present = [Girls[1]]
                        if Girls[1] in Nearby:
                                $ Nearby.remove(Girls[1])
                "Between them." if not Nearby:
                        $ Present = [Girls[0],Girls[1]]
                        if Girls[1] in Nearby:
                                $ Nearby.remove(Girls[1])
                        if Girls[0] in Nearby:
                                $ Nearby.remove(Girls[0])
                "Neither":
                        "You decide to sit a distance away from either of them."
                        $ Girls = Girls[:]
                        while Girls:
                            # adds both girls to Nearby
                            if Girls[0] not in Nearby:
                                    $ Nearby.append(Girls[0])
                            $ Girls.remove(Girls[0])
    #end two-girl option
    elif len(Girls) > 2:
            # there are two+ girls
            "You see several girls are in the room, who would you like to sit near?"
            while len(Present) < 2:
                    menu:
                        "Select up to two."
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
                                $ Present.append("junk")
                                $ Present.append("junk")

    #end two-girl option
    elif Girls:
            # there is one girl
            menu:
                "You see [Girls[0].name] is there, do you sit next to her?"
                "Yes":
                        $ Present.append(Girls[0])
                "No, I'll sit away from her a bit.":
                        $ Nearby.append(Girls[0])
    #end one-girl option
    #else: no girls at all

    while "junk" in Present:
            $ Present.remove("junk")
    if len(Present) == 2:
            "You sit between [Present[0].name] and [Present[1].name]."
            $ Present[0].location = "bg_classroom"
            $ Present[1].location = "bg_classroom"
    elif Present:
            "You sit next to [Present[0].name]."
            $ Present[0].location = "bg_classroom"
    else:
            "You sit off to the side."

    if len(Girls) > len(Present):
            #if there were girls not picked
            "The rest are scattered around the room."

    while Girls:
            if Girls[0] not in Present:
                    #if she wasn't added to present, move her to Nearby
                    if Girls[0] not in Nearby:
                            $ Nearby.append(Girls[0])
                    $ Girls[0].location = "nearby"
            $ Girls.remove(Girls[0])

    if Present:
            call shift_focus(Present[0])
    call set_the_scene(Quiet=1)

    return

label Frisky_Class(Girl = 0, Teacher = 0, lineB = 0, Girls = []):
    if Girl not in all_Girls:
        return

    $ Partner = 0
    $ line = 0

    if len(Present) >= 2:
        $ Present[1].sprite_location = StageLeft
        $ Present[1].Eyes = "side"

    $ Present[0].sprite_location = StageRight

    $ Girls = active_Girls[:]

    while Girls:
        if renpy.showing(Girls[0].Tag + "_Sprite"):
            if Girls[0] == RogueX:
                show Rogue_Sprite at sprite_location(RogueX.sprite_location,50):
                    ease .5 ypos 250
            elif Girls[0] == KittyX:
                show Kitty_Sprite at sprite_location(KittyX.sprite_location,50):
                    ease .5 ypos 250
            elif Girls[0] == LauraX:
                show Laura_Sprite at sprite_location(LauraX.sprite_location,50):
                    ease .5 ypos 250
            elif Girls[0] == JeanX:
                show Jean_Sprite at sprite_location(JeanX.sprite_location,50):
                    ease .5 ypos 250
            elif Girls[0] == JubesX:
                show Jubes_Sprite at sprite_location(JubesX.sprite_location,50):
                    ease .5 ypos 250
        $ Girls.remove(Girls[0])

    call shift_focus(Girl)
    if EmmaX.location == "bg_teacher":
        "[EmmaX.name] is giving a lecture on mutant relations. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."

        $ Teacher = EmmaX
    elif StormX.location == "bg_teacher":
        "[StormX.name] is giving a lecture on geography and politics. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."

        $ Teacher = StormX
    else:
        "Professor McCoy is giving a lecture on the X-Gene. Sitting next to you, you notice [Girl.name] shifting uncomfortably in her seat."

    "Occasionally, you catch her glancing over your way."
    "[Girl.name] opens her notebook and begins scratching out a note."
    "She detaches the slip of paper from the binder, carefully folding it before sliding it in front of you."
    "She watches you as you unfold the note."

    if "friskyclass" in Girl.History:
        "It reads \"Did you want to fool around again? Y[[] N[[]\""

        menu:
            "Y":
                $ Girl.change_face("sly",1)
                $ Girl.change_stat("love", 80, 3)
                $ Girl.change_stat("inhibition", 60, 3)

                "She smiles suggestively."

                $ D20 = renpy.random.randint(1, 15)

                jump Frisky_Class_Loop
            "N":
                $ Girl.change_stat("love", 80, -10)
                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 60, -3)

                $ line = "rejected"

                $ Girl.change_face("angry")
                $ Girl.daily_history.append("angry")

                jump Frisky_Class_End

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
        $ Girl.change_face("smile",2)

        "You look back and see that she's blushing slightly."
        "She slides her pen over to you so you can reply."

        $ Girl.change_face("smile",1)
    else:
        $ Girl.change_face("sly",1)

        "You look back and see that she's staring at you suggestively."
        "She slides her pen over to you so you can reply."

    menu:
        "You reply. . ."
        "What are you talking about?":
            jump Frisky_Class_End
        "Naah. Not so much.":
            $ Girl.change_stat("love", 80, -3)
            $ Girl.change_stat("inhibition", 60, -3)
            $ Girl.change_face("confused")

            jump Frisky_Class_End
        "It's my favorite subject." if Girl in [RogueX, KittyX]:
            $ Girl.change_stat("love", 80, 5)
            $ Girl.change_face("smile")

            "[Girl.name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could study together tonight?\"."

            $ line = "continue"
        "Yeah, pretty lame." if Girl not in [RogueX, KittyX]:
            $ Girl.change_stat("love", 80, 5)
            $ Girl.change_face("smile")

            "[Girl.name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could 'study' together tonight?\"."

            $ line = "continue"
        "I do when it's about you." if Girl in [RogueX, KittyX]:
            $ line = "her"
        "I was too busy thinking about you." if Girl not in [RogueX, KittyX]:
            $ line = "her"

    if line == "her":
        if ApprovalCheck(Girl, 500, "I") or Girl.SEXP >= 30:
            $ Girl.change_face("sly")

            "[Girl.name] reads your note and smiles at you suggestively."

            $ line = "flirt"
        elif ApprovalCheck(Girl, 900):
            if Girl in [RogueX, KittyX]:
                $ Girl.change_face("confused",2)

                "[Girl.name] reads your note and blushes furiously, looking down at her notes."
            else:
                $ Girl.change_face("sly",1)

                "[Girl.name] reads your note and gets a sly smile, looking down at her notes."
            $ Girl.change_face("bemused",1)
            $ line = "flirt"
        else:
            if Girl in [RogueX, KittyX]:
                $ Girl.change_face("perplexed",2)

                "[Girl.name] reads your note and blushes furiously. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could study tonight?\"."
            else:
                $ Girl.change_face("sly",1)

                "[Girl.name] reads your note and gets a sly smile. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could 'study' tonight?\"."

            $ Girl.change_face("bemused",1)

            $ line = "continue"

    if line == "continue":
        if Girl in [RogueX, KittyX]:
            "[Girl.name]'s drawn a little heart as the period at the bottom of the question mark."

        "She's trying to act like she's paying attention to the lecture, but she can't hide the big smile on her face."

        menu:
            "You respond. . ."
            "Maybe later.":
                $ Girl.change_stat("love", 80, -3)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 60, -3)
                $ Girl.change_face("confused")

                $ line = 0

                jump Frisky_Class_End
            "Naah. I've got better things to do.":
                $ Girl.change_stat("love", 80, -10)
                $ Girl.change_stat("love", 70, -5)
                $ Girl.change_stat("obedience", 70, 5)
                $ Girl.change_stat("inhibition", 60, -3)

                $ line = "rejected"

                $ Girl.change_face("angry")
                $ Girl.daily_history.append("angry")

                jump Frisky_Class_End
            "Count on it.":
                $ Girl.change_face("smile")

                "She smiles when she reads your reply, and throws you a wink."

                $ Girl.daily_history.append("studydate")

                "The rest of class is uneventful."

                return
            "We could get some \"studying\" done right now.":
                    if ApprovalCheck(Girl, 1000):
                        $ Girl.change_face("sly",1)
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("inhibition", 60, 3)

                        "[Girl.name] gets a mischevious grin on her face and leans towards you."

                        $ line = "flirt"
                    elif ApprovalCheck(Girl, 700):
                        $ Girl.change_face("smile",1)
                        $ Girl.change_stat("inhibition", 60, 2)

                        if Girl in [RogueX, KittyX]:
                            "[Girl.name] blushes and smiles your way."
                        else:
                            "[Girl.name] startles a bit and smiles your way."
                        $ line = "flirt"
                    else:
                        $ Girl.change_face("confused",1)

                        "[Girl.name] looks a bit surprised, then scowls at you."

                        jump Frisky_Class_End

    if line == "flirt":
        $ Round -= 20
        $ D20 = renpy.random.randint(1, 15)

        $ Girl.change_face("sly")

        "You notice one of [Girl.name]'s shoes slip from her foot beneath the desk. She tosses you a sly grin."
        if Girl.Hose:
            "You feel the smooth texture of her stockinged foot begin to slowly slide back and forth along the length of your calf."
        else:
            "You feel the smooth skin of her bare foot begin to slowly slide back and forth along the length of your calf."

        while D20 <= 21 or "go on" in Player.recent_history:
            menu Frisky_Class_Loop:
                "Pull away from her.":
                    if line == "fondle_pussy":
                        "You slowly slide your hand from her lap and start taking notes again."

                        $ line = "tease"
                    elif line == "fondle_breast":
                        "With a final squeeze, you move your hand back to the desktop."

                        $ line = "tease"
                    elif Girl.OCount and Girl.lust < 90:
                        "That'll probably do for now. . ."

                        $ line = "tease"
                    else:
                        $ line = "rejected"

                        $ Girl.change_stat("love", 200, -15)
                        $ Girl.change_stat("obedience", 70, 2)
                        $ Girl.change_stat("inhibition", 60, -2)
                    jump Frisky_Class_End
                "Look into her eyes and smile slightly." if line == "flirt":
                    $ Girl.change_face("smile")
                    $ Girl.change_stat("love", 200, 5)

                    "[Girl.name] smiles back."
                    "She looks back towards the front of the class, but her hand drifts across the top of the desk until she's holding yours."

                    $ line = "handholding"

                    jump Frisky_Class_Loop
                "Grasp her hand gently, stroking the top of it." if line == "handholding":
                    $ Girl.change_stat("love", 200, 5)
                    $ Girl.change_stat("lust", 50, 5)
                    $ Girl.change_face("smile")

                    "[Girl.name] sighs contentedly and holds your hand for the remainder of class."

                    jump Frisky_Class_End
                "Try and slip your hand to her lap." if line != "fondle_pussy":
                    $ line = "fondle_pussy"

                    if ApprovalCheck(Girl, 1200) and Girl.FondleP and Girl.SEXP >= 40:
                        $ Girl.change_face("sly")
                        $ Girl.change_stat("love", 90, 5)
                        $ Girl.change_stat("obedience", 70, 5)
                        $ Girl.change_stat("inhibition", 60, 5)

                        "[Girl.name] gets a mischievous grin and places her hand on your arm."
                    elif ApprovalCheck(Girl, 1400) and Girl.FondleP:
                        $ Girl.change_face("smile")
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 70, 7)
                        $ Girl.change_stat("inhibition", 60, 3)

                        "[Girl.name] starts slightly as your hand travels up her thigh, but then she lets out a slight grin."
                    elif ApprovalCheck(Girl, 1500):
                        $ Girl.change_face("perplexed",2)
                        $ Girl.change_stat("obedience", 70, 10)
                        $ Girl.change_stat("inhibition", 60, 3)

                        "[Girl.name] glances at you in alarm, but then slowly calms down."

                        $ Girl.change_face("smile",1)

                        $ D20 += 2
                    else:
                        $ line = "too far"

                    if line == "fondle_pussy":
                        $ Girl.change_face("sly")
                        $ Girl.change_stat("lust", 94, 5)
                        if Girl.wearing_skirt:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak under the hem of her skirt, slowly tracing the soft contours of her mound."
                        elif Girl.PantsNum() >= 7:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak down her pants, slowly tracing the soft contours of her mound."
                        else:
                            "[Girl.name]'s sly smile turns sultry as she feels your fingers sneak between her legs, slowly tracing the soft contours of her mound."

                        $ Girl.change_stat("lust", 94, 5)

                        if Girl.Panties == "shorts":
                            "You think her shorts are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif Girl.Panties:
                            "You think her panties are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif Girl.Pubes:
                            "You feel her soft fur moisten as you stroke the soft flesh below. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        else:
                            "You feel her lips moisten as you stroke the soft flesh. Her cheeks are flushed and her breathing's starting to become shallower and quicker."

                        $ primary_action = "fondle_pussy"
                        $ D20 += 5
                "Keep fondling her pussy." if line == "fondle_pussy":
                    $ Girl.change_stat("obedience", 70, 5)
                    $ Girl.change_stat("inhibition", 60, 3)
                    $ Girl.change_stat("lust", 89, 5)
                    $ Girl.change_stat("lust", 94, 5)

                    $ lineB = renpy.random.choice(["As the class drones on, you continue to slowly massage her warm delta.",
                        "As the class continues, you continue to slowly massage her moist pussy.",
                        "As the lecture drones on, you continue to slowly stroke her clit.",
                        "As the class continues, you continue to slowly caress her labia."])
                    "[lineB]"

                    $ D20 += 5
                "Start fondling her tits." if line != "fondle_breasts":
                    $ line = "fondle_breasts"
                    if ApprovalCheck(Girl, 1100) and Girl.FondleB and Girl.SEXP >= 40:
                        $ Girl.change_stat("love", 80, 5)
                        $ Girl.change_stat("obedience", 70, 5)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("sly")

                        "[Girl.name] closes her eyes and caresses your arm."
                    elif ApprovalCheck(Girl, 1300) and Girl.FondleB:
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 70, 7)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("smile",1)

                        "[Girl.name] flinches as your hand travels up her ribcage, but she grins as you reach her breast."
                    elif ApprovalCheck(Girl, 1400):
                        $ Girl.change_stat("obedience", 70, 10)
                        $ Girl.change_stat("inhibition", 60, 3)
                        $ Girl.change_face("perplexed",2)

                        "[Girl.name] glances at you in alarm, but then slowly calms down."

                        $ Girl.change_face("smile",2)
                        $ D20 += 5
                    else:
                        $ line = "too far"

                    if line == "fondle_breasts":
                        $ Girl.change_face("sly")
                        $ Girl.change_stat("lust", 94, 5)

                        "[Girl.name]'s sly eyes spakle as your hand cups her breast, giving it a casual caress."
                        "Her nipples begin to firm up and she lets out a small moan of pleasure."

                        $ D20 += 7
                        $ primary_action = "fondle_breasts"
                "Keep fondling her tits." if line == "fondle_breasts":
                    $ Girl.change_stat("obedience", 70, 5)
                    $ Girl.change_stat("inhibition", 60, 2)
                    $ Girl.change_stat("lust", 95, 3)

                    "Barely paying attention to the lecture, you continue to pulse her breast in your palm."

                    $ D20 += 7
                "Try and pull her hand toward your lap." if not offhand_action and Player.Semen:
                    if "handjob" in Girl.recent_history:
                        "[Girl.name] grins and her hand grasps your cock again."
                    elif ApprovalCheck(Girl, 1200) and Girl.Hand and Girl.SEXP >= 40:
                        $ Girl.change_face("sly")
                        $ Girl.change_stat("love", 90, 5)
                        $ Girl.change_stat("obedience", 70, 5)
                        $ Girl.change_stat("inhibition", 60, 5)

                        "[Girl.name] gets a mischievous grin and her hand starts to caress your crotch."
                    elif ApprovalCheck(Girl, 1400) and Girl.FondleP:
                        $ Girl.change_face("smile")
                        $ Girl.change_stat("love", 80, 3)
                        $ Girl.change_stat("obedience", 70, 7)
                        $ Girl.change_stat("inhibition", 60, 3)

                        "[Girl.name] starts slightly as your move her hand up your thigh, but then she lets out a slight grin."
                    elif ApprovalCheck(Girl, 1500):
                        $ Girl.change_face("perplexed",2)
                        $ Girl.change_stat("obedience", 70, 10)
                        $ Girl.change_stat("inhibition", 60, 3)

                        "[Girl.name] glances at you in alarm, but then slowly calms down."

                        $ Girl.change_face("smile",1)
                        $ D20 += 2
                    else:
                        $ line = "too far"

                    if line != "too far":
                        $ Girl.change_face("sly")
                        $ Girl.change_stat("lust", 94, 5)

                        if "cockout" not in Player.recent_history:
                            "[Girl.name]'s hand slowly unzips your pants and pulls your cock free."

                            $ Player.AddWord(1,"cockout")

                            call Seen_First_Peen(Girl,Partner)

                            $ Girl.change_stat("lust", 94, 5)

                        $ offhand_action = "handjob"
                        $ Girl.recent_history.append("handjob")
                        $ Girl.daily_history.append("handjob")

                        "She begins to gently stroke it. . ."

                        if "handjob" not in Girl.recent_history:
                            $ Girl.Hand += 1
                        $ D20 += 5
                "Stop her handjob." if offhand_action:
                    "You put a hand on her wrist and nudge her hand away."
                    if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 700, "O") or (Girl.love+Girl.obedience) >= (2*Girl.inhibition):
                        $ Girl.change_face("sad")
                        $ Girl.change_stat("love", 90, -1)
                        $ Girl.change_stat("obedience", 60, 2)
                        $ Girl.change_stat("obedience", 80, 3)

                        "[Girl.name] allows her hand to be pulled away and goes back to what she'd been doing with it."

                        $ Girl.change_face("sly")
                        $ offhand_action = 0
                    else:
                            $ Girl.change_face("angry")
                            $ Girl.change_stat("love", 80, -3)
                            $ Girl.change_stat("love", 90, -1)
                            $ Girl.change_stat("obedience", 70, -2)
                            $ Girl.change_stat("inhibition", 60, 3)
                            $ Girl.change_stat("inhibition", 80, 2)

                            "[Girl.name] grasps your cock tightly, then continues to stroke it when you let go."

                            $ Girl.change_face("sly")
                            $ D20 += 2

            if not offhand_action and Player.Semen and "stophand" not in Girl.recent_history:
                if ApprovalCheck(Girl, 1200) and ApprovalCheck(Girl, 400, "I") and Girl.Hand and Girl.SEXP >= 40:
                    $ Girl.change_face("sly")

                    "[Girl.name] gets a mischievous grin and her hand starts to caress your crotch."

                    menu:
                        "What do you do?"
                        "Let her":
                            "You smile and nod a little."

                            $ Girl.change_face("sly")
                            $ Girl.change_stat("love", 80, 1)
                            $ Girl.change_stat("inhibition", 70, 3)
                            $ Girl.change_stat("inhibition", 90, 2)
                            $ Girl.change_stat("lust", 94, 5)

                            if "cockout" not in Player.recent_history:
                                "[Girl.name]'s hand slowly unzips your pants and pulls your cock free."

                                $ Player.AddWord(1,"cockout")

                                call Seen_First_Peen(Girl,Partner)

                                $ Girl.change_stat("lust", 94, 5)

                            $ offhand_action = "handjob"

                            $ Girl.recent_history.append("handjob")
                            $ Girl.daily_history.append("handjob")

                            "She begins to gently stroke it. . ."

                            if "handjob" not in Girl.recent_history:
                                $ Girl.Hand += 1

                            $ D20 += 10
                        "Stop her":
                            "You put a hand on her wrist and nudge her hand away."

                            $ Girl.recent_history.append("stophand")

                            if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 700, "O") or (Girl.love+Girl.obedience) >= (2*Girl.inhibition):
                                $ Girl.change_face("sad")
                                $ Girl.change_stat("love", 90, -1)
                                $ Girl.change_stat("obedience", 60, 2)
                                $ Girl.change_stat("obedience", 80, 3)

                                "[Girl.name] allows her hand to be pulled away and goes back to what she'd been doing with it."

                                $ Girl.change_face("sly")
                                $ offhand_action = 0
                            else:
                                $ Girl.change_face("angry")
                                $ Girl.change_stat("love", 80, -3)
                                $ Girl.change_stat("love", 90, -1)
                                $ Girl.change_stat("obedience", 70, -2)
                                $ Girl.change_stat("inhibition", 60, 3)
                                $ Girl.change_stat("inhibition", 80, 2)

                                "[Girl.name] stops, but looks really annoyed."

                                $ D20 += 10

            if offhand_action:
                "[Girl.name]'s hand continues to caress your cock. . ."

                $ Player.Focus += 15 if Player.Focus < 60 else 10

                if Player.Focus >= 100:
                    "As you start to reach your limits, [Girl.name] places a hand over your cock."
                    "You jiz all over her hand."

                    $ Player.Semen -= 1

                    if (Girl.Blow and ApprovalCheck(Girl, 1200)) or Girl == JubesX:
                        "She quickly licks it all up."

                        $ Girl.Addict -= 20
                        $ Girl.Swallow += 1
                        $ Girl.recent_history.append("swallow")
                        $ Girl.daily_history.append("swallow")
                    else:
                        "She quickly wipes her hand off under the desk."

                    $ Girl.change_stat("lust", 200, 5)

                    $ D20 += 10

                    if not Player.Semen:
                        "She continues to lightly stroke you, but you don't seem up to it for now. . ."

                        $ offhand_action = 0

                $ D20 += 5

            if Girl.lust >= 95:
                $ lineB = line

                call Girl_Cumming(Girl,1)

                $ line = lineB
                $ lineB = renpy.random.choice([Girl.name+" collapses over her desk.",
                        Girl.name+" mumbles something unintelligible.",
                        Girl.name+" bites her lip as she struggles to stay upright.",
                        Girl.name+" seems a bit flushed."])
                "[lineB]"

                $ D20 += 15

            $ Round -= 7

            if Round <= 15:
                "Unfortunately it seems like class is wrapping up. You'll have to save this for later. . ."

                $ line = "tease"
                jump Frisky_Class_End

            if line == "too far":
                $ Girl.change_face("surprised",2)
                $ Girl.change_stat("love", 80, -5)
                $ Girl.change_stat("obedience", 70, 7)
                $ Girl.change_stat("inhibition", 50, -3)

                "[Girl.name] sits up straight in her seat and makes a little yelping noise."

                $ Girl.change_face("angry",1)

                "Between that and the icy glare she shoots you, it's enough to draw the attention of your fellow students in your direction."

                $ D20 += 20

                if "go on" in Player.recent_history:
                    $ line = "caught"
                    jump Frisky_Class_End
            else:
                if len(Present) >= 2 and D20 >= 15:
                    if Partner:
                        $ Partner.GirlLikeUp(Girl,2)
                        $ Girl.GirlLikeUp(Partner,2)
                        $ Partner.change_stat("lust", 95, 3)
                        $ lineB = renpy.random.choice([0,
                            0,
                            0,
                            Partner.name+" seems into it. . .",
                            Partner.name+"'s hand moves a bit faster.",
                            Partner.name+" bites her lip as her hand continues to move.",
                            Partner.name+"'s hand slows down a bit."])
                        if lineB:
                            "[lineB]"

                        if Partner.lust >= 95:
                            $ lineB = line

                            call Girl_Cumming(Partner,1)

                            $ line = lineB
                            $ lineB = renpy.random.choice([Partner.name+" collapses over her desk.",
                                    Partner.name+" mumbles something unintelligible.",
                                    Partner.name+" bites her lip as she struggles to stay upright.",
                                    Partner.name+" seems a bit flushed."])

                            "[lineB]"

                            $ D20 += 15
                    elif "saw with "+ Girl.Tag in Present[1].Traits:
                        call Anyline(Present[1],"Well!")

                        $ Present[1].GirlLikeUp(Girl,-4)
                        $ Girl.GirlLikeUp(Present[1],-2)

                        call remove_girl(Present[1])
                    elif ApprovalCheck(Present[1], 1500) and Present[1].GirlLikeCheck(Girl) >= 600:
                        $ Present[1].Eyes = "leftside"

                        "[Present[1].name] seems to notice what you and [Girl.name] are doing."

                        $ Present[1].change_face("sly",1)

                        "She seems to be kinda into it. . ."

                        if ApprovalCheck(Present[1], 800, "I") or "exhibitionist" in Present[1].Traits:
                            $ Girl.change_stat("inhibition", 90, 3)
                            $ Present[1].GirlLikeUp(Girl,3)
                            $ Girl.GirlLikeUp(Present[1],5)
                            $ Present[1].change_stat("lust", 89, 7)

                            "You notice that [Present[1].name]'s begun feeling herself up as well."

                            $ Present[1].AddWord(1,"frisky","frisky",0,0)
                            $ Partner = Present[1]
                    else:
                        $ Present[1].Eyes = "leftside"

                        "[Present[1].name] seems to notice what you and [Girl.name] are doing."

                        $ Present[1].AddWord(1,0,0,"saw with " + Girl.Tag)
                        $ Present[1].change_face("angry",1)

                        if Present[1] == RogueX:
                            ch_r "How dare you! Hussy."
                        elif Present[1] == KittyX:
                            ch_k "Hey! . . . HEY!"
                        elif Present[1] == LauraX:
                            ch_l "Cool off, you two."
                        elif Present[1] == JeanX:
                            ch_j "Hey, cut it out."

                        $ Present[1].GirlLikeUp(Girl,-2)
                        $ Girl.GirlLikeUp(Present[1],-3)
                        $ D20 += 15

                        if "go on" in Player.recent_history:
                            $ line = "caught"
                            jump Frisky_Class_End

                if Teacher and "frisky" in Teacher.recent_history:
                    $ Teacher.GirlLikeUp(Girl,2)
                    $ Girl.GirlLikeUp(Teacher,2)
                    $ Teacher.change_stat("lust", 95, 3)

                    $ lineB = renpy.random.choice([0,
                        0,
                        0,
                        Teacher.name+" stumbles a bit over the delivery of the next portion of her lecture.",
                        Teacher.name+"'s hand moves a bit faster.",
                        Teacher.name+" bites her lip as her hand continues to move.",
                        Teacher.name+"'s hand slows down a bit."])

                    if lineB:
                        "[lineB]"

                    if Teacher.lust >= 95:
                        $ lineB = line

                        call Girl_Cumming(Teacher,1)

                        $ line = lineB

                        $ lineB = renpy.random.choice([Teacher.name+" stumbles a bit over the delivery of the next portion of her lecture.",
                            Teacher.name+" mumbles something unintelligible but continues the lecture.",
                            Teacher.name+" bites her lip as she struggles to continue talking.",
                            Teacher.name+" seems a bit under the weather.",
                            Teacher.name+" seems a bit flushed."])

                        "[lineB]"

                        $ D20 += 15

                if D20 > 30:
                    if D20 >= 50:
                        $ lineB = renpy.random.choice([0,
                            0,
                            0,
                            "The class isn't paying attention to the lecture anymore.",
                            "The class definitely seems into the show she's putting on.",
                            "The class is hooting and hollering.",
                            "The students seem to be watching you intently."])
                    else:
                        $ lineB = renpy.random.choice([0,
                            0,
                            0,
                            "The class seems a little confused as to what she's talking about.",
                            "The class seems a little confused as to what she's doing back there.",
                            "The class is shifting strange looks your way.",
                            "A bunch of students seem to be watching you intently."])
                    if lineB:
                        "[lineB]"

        if "exhibitionist" not in Girl.Traits and not ApprovalCheck(Girl, 700,"I"):
            $ line = "too far"

        if line not in ("rejected", "handholding", "tease"):
                $ Girl.change_face("surprised")

                if Teacher:
                    $ Teacher.change_face("surprised",1)

                    "[Teacher.name] stops her lecture in mid-sentence when she notices what you and [Girl.name] are up to."

                    if ApprovalCheck(Teacher, 1500) and Teacher.GirlLikeCheck(Girl) >= 600:
                        $ Teacher.change_face("sly",1)

                        if line == "too far":
                            $ Girl.Mouth = "sad"

                            if Teacher == EmmaX:
                                "She looks over at you and shrugs as she continues her lecture, but the moment has past."
                            elif Teacher == StormX:
                                "She looks over at you and smiles consolingly as she continues her lecture, but the moment has past."

                            jump Frisky_Class_End

                        "She gets a sly smile on her face and continues her lecture."

                        $ Girl.change_face("sly",1)

                        if ApprovalCheck(Teacher, 800, "I") or "exhibitionist" in Teacher.Traits:
                            $ Teacher.change_stat("inhibition", 90, 3)
                            $ Teacher.GirlLikeUp(Girl,3)
                            $ Girl.GirlLikeUp(Teacher,5)
                            $ Teacher.change_stat("lust", 89, 7)

                            "You notice that [Teacher.name]'s hand has snaked down beneath the podium and begun to move."

                            $ Teacher.AddWord(1,"frisky","frisky",0,0)
                            $ Player.AddWord(1,"go on","go on",0,0)

                        "[Girl.name] looks around and shrugs. . ."
                        jump Frisky_Class_Loop
                    else:
                        $ Teacher.change_face("angry",1)
                        $ Girl.Mouth = "sad"

                        if Teacher == EmmaX:
                            ch_e "[EmmaX.Petname], [Girl.Tag], if you could perhaps pay more attention to the lecture, and less to each other's bodies?"
                            ch_e "Perhaps it would be best if you visited the headmaster's office and cool off?"
                        elif Teacher == StormX:
                            ch_s "[StormX.Petname], [Girl.Tag], I can appreciate your enthusiasm, but perhaps not on my time?"
                            ch_s "I think perhaps you should visit Charles and cool off?"
                else:
                    "Dr. McCoy stops his lecture in mid-sentence when he notices that the whole class is looking at you and [Girl.name]."
                    ch_b "Oh, my stars and garters!"
                    ch_b "[Player.name]!?! {b}WHAT ARE YOU DOING? GirlsTH OF YOU, TO THE PROFESSOR'S OFFICE, IMMEDIATELY!{/b}"

                $ Girl.AddWord(1, 0, 0, 0, "friskyclass")

                $ line = 0

                $ Girl.change_stat("love", 80, -10)
                $ Girl.change_stat("obedience", 70, -5)
                $ Girl.change_stat("inhibition", 50, -10)

                $ primary_action = 0

                if Girl not in Rules:
                    call Girls_Caught(Girl)
                else:
                    "Since Xavier isn't concerned with your activities, you both head back to your room instead."

                    $ Girl.location = "bg_player"

                    call CleartheRoom(Girl,0,1)
                    jump player_room

label Frisky_Class_End:
    $ primary_action = 0
    $ Partner = 0

    if Teacher:
        $ Teacher.DrainWord("frisky", 1, 0)
    if not line:
        $ Girl.change_face("confused")

        "She unfolds the note and quickly reads it over."

        $ Girl.change_face("sad")

        "As she does, you immediately see disappointment come over her features."
        "She scratches out a reply and slides it back in front of you."
        "When you open it up, it reads: {i}Never mind.{/i}"
    elif line == "tease":
        if Girl.lust >= 80:
            $ Girl.change_face("surprised",2)

            "[Girl.name] startles briefly."

            $ Girl.change_face("sad",2)

            "[Girl.name] she looks over at you a bit upset that you ended things so abruptly."
        $ Girl.AddWord(1, 0, 0, 0, "friskyclass")
        $ Girl.change_face("sly",1)

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
    elif line == "rejected":
        if Girl in [RogueX, KittyX]:
            $ Girl.change_face("sadside")

            "[Girl.name] looks surprised and hurt. For the rest of the class, she says nothing."
        else:
            $ Girl.change_face("angry")

            "[Girl.name] looks surprised and hurt. For the rest of the class, she stares daggers at you."
        "It seems like she has a hard time looking you in the eye."
    elif line == "caught":
        "You quickly separate and go back to trying to study. . ."

    "Eventually, [Girl.name] seems to settle down and pay attention to the course material. You manage to do the same without falling asleep."

    $ line = 0

    return
