label Class_Room_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    $ Present = []
    $ bg_current = "bg classroom"
    $ Nearby = []
    call Gym_Clothes_Off #call Gym_Clothes
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    call EventCalls
    call Set_The_Scene(0) #won't display characters yet)
    $ Line = "entry"

label Class_Room:
    $ bg_current = "bg classroom"
    if "goto" in Player.RecentActions or "traveling" in Player.RecentActions:
            $ Present = []
            if Time_Count < 2 and Weekday < 5:   #pre-evening
                    call Class_Room_Seating
            $ Player.DrainWord("goto",1,0)
            $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Time_Count >= 3: # night time
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait
                call EventCalls
                call Girls_Location
    call GirlsAngry

    if Line == "entry":
            if EmmaX.Loc == "bg teacher":
                    $ Line = "As you sit down, you see "+ EmmaX.Name +" at the podium. What would you like to do?"
            elif StormX.Loc == "bg teacher":
                    $ Line = "As you sit down, you see "+ StormX.Name +" at the podium. What would you like to do?"
            elif Time_Count == 2 or Weekday > 5: #evening
                    $ Line = "You enter the classroom. What would you like to do?"
            else:
                    $ Line = "You sit down at a desk. What would you like to do?"
    else:
            if Line != "What would you like to do next?":
                    $ Line = "You are in class right now. What would you like to do?"
    #End Room Set-up

    menu:
        "[Line]"
        "Take the morning class" if Weekday < 5 and Time_Count == 0:
                if Round >= 30:
                    jump Take_Class
                else:
                    "Class is already letting out. You can hang out until the next one."
        "Take the afternoon class" if Weekday < 5 and Time_Count == 1:
                if Round >= 30:
                    jump Take_Class
                else:
                    "Class is already letting out. You can hang out until they lock up for the night."
        "There are no classes right now (locked)" if Weekday >= 5 or Time_Count >= 2:
                pass

        "Chat":
                call Chat
                $ Line = "You are in class right now. What would you like to do?"

        "Lock the door" if "locked" not in Player.Traits:
                    if Weekday >=5 or Time_Count >= 2: #evening+
                            "You lock the door"
                            $ Player.Traits.append("locked")
                            call Taboo_Level
                    else:
                            "You can't really do that during class."

        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Wait" if Time_Count < 3: #not night time
                "You hang out for a bit."
                call Wait
                call EventCalls
                call Girls_Location

                if Time_Count < 2: #not evening
                            $ Line = "A new class is in session. What would you like to do?"
                else: #evening+
                            $ Line = "Classes have let out for the day. What would you like to do?"

        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry

    $ Line = 0
    jump Class_Room

label Take_Class:
    call Set_The_Scene
    if "class" in Player.DailyActions:
            $ Line = "The session begins."
    elif Round >= 80:
            $ Line = "You make it in time for the start of the class."
    elif Round >= 50:
            $ Line = "You get in a bit late, but there's plenty of class left."
    elif Round >= 30:
            $ Line = "You're pretty late, but catch the tail end of the class."
    $ Trigger = 0

    $ D20 = renpy.random.randint(1, 20)

    if D20 > 15 and Present and ApprovalCheck(Present[0], 300, "I"):
            #if there is another girl in the room, and she is reasonably loose, call Frisky Class
            "[Line]"
            call Frisky_Class(Present[0])

    else:
        $ Line = Line + renpy.random.choice([" It was fairly boring.",
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
        "[Line]"
    $ Player.RecentActions.append("class")
    $ Player.DailyActions.append("class")
    $ Player.XP += (5 + (int(Round / 10)))

    call Wait
    call Girls_Location
    call Set_The_Scene
    call EventCalls
    $ Line = "What would you like to do next?"
    jump Class_Room

label Class_Room_Seating(Girls=[],GirlB=0,GirlLike=0,Line=0,D20=0,BO=[]):
    # Girls is the amount of girls in the room.
    # active ones get priority, then shuffled, then nearby girls
    $ Present = []
    $ BO = ActiveGirls[:]
    while BO:
        #fills the list with all girls in the room
        if BO[0].Loc == bg_current:
                $ Girls.append(BO[0])
        $ BO.remove(BO[0])

    $ renpy.random.shuffle(Girls)

    $ BO = Nearby[:]
    while BO:
        # adds any girls nearby to the back of the list
        if BO[0] not in Girls:
                $ Girls.append(BO[0])
        $ BO.remove(BO[0])

    #End Girl selections

    $ Nearby = []

    call Set_The_Scene(0) #won't display characters yet)
    if len(Girls) == 2:
            # there are two girls
            $ D20 = renpy.random.randint(500, 1500)
            if (Girls[0].GirlLikeCheck(Girls[1]) + Girls[1].GirlLikeCheck(Girls[0])) >= D20:
                "You see that [Girls[0].Name] and [Girls[1].Name] are sitting next to each other, which do you sit next to?"
            else:
                "You see that [Girls[0].Name] and [Girls[1].Name] are in the room, but on opposite sides."
                $ BO = Girls[:]
                while BO:
                    # adds both girls to Nearby
                    if BO[0] not in Nearby:
                            $ Nearby.append(BO[0])
                    $ BO.remove(BO[0])
            menu:
                extend ""
                "[Girls[0].Name]":
                        $ Present = [Girls[0]]
                        if Girls[0] in Nearby:
                                $ Nearby.remove(Girls[0])
                "[Girls[1].Name]":
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
                        $ BO = Girls[:]
                        while BO:
                            # adds both girls to Nearby
                            if BO[0] not in Nearby:
                                    $ Nearby.append(BO[0])
                            $ BO.remove(BO[0])
    #end two-girl option
    elif len(Girls) > 2:
            # there are two+ girls
            "You see several girls are in the room, who would you like to sit near?"
            while len(Present) < 2:
                    menu:
                        "Select up to two."
                        "[RogueX.Name]" if RogueX in Girls and RogueX not in Present:
                                $ Present.append(RogueX)
                        "[KittyX.Name]" if KittyX in Girls and KittyX not in Present:
                                $ Present.append(KittyX)
                        "[LauraX.Name]" if LauraX in Girls and LauraX not in Present:
                                $ Present.append(LauraX)
                        "[JeanX.Name]" if JeanX in Girls and JeanX not in Present:
                                $ Present.append(JeanX)
                        "[JubesX.Name]" if JubesX in Girls and JubesX not in Present:
                                $ Present.append(JubesX)
                        "Done":
                                $ Present.append("junk")
                                $ Present.append("junk")

    #end two-girl option
    elif Girls:
            # there is one girl
            menu:
                "You see [Girls[0].Name] is there, do you sit next to her?"
                "Yes":
                        $ Present.append(Girls[0])
                "No, I'll sit away from her a bit.":
                        $ Nearby.append(Girls[0])
    #end one-girl option
    #else: no girls at all

    while "junk" in Present:
            $ Present.remove("junk")
    if len(Present) == 2:
            "You sit between [Present[0].Name] and [Present[1].Name]."
            $ Present[0].Loc = "bg classroom"
            $ Present[1].Loc = "bg classroom"
    elif Present:
            "You sit next to [Present[0].Name]."
            $ Present[0].Loc = "bg classroom"
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
                    $ Girls[0].Loc = "nearby"
            $ Girls.remove(Girls[0])

    if Present:
            call Shift_Focus(Present[0])
    call Set_The_Scene(Quiet=1)

    return

label Frisky_Class(Girl = 0, Teacher = 0, LineB = 0, BO = []):
    if Girl not in TotalGirls:
        return

    $ Partner = 0
    $ Line = 0

    if len(Present) >= 2:
        $ Present[1].sprite_location = StageLeft
        $ Present[1].Eyes = "side"

    $ Present[0].sprite_location = StageRight

    $ BO = ActiveGirls[:]

    while BO:
        if renpy.showing(BO[0].Tag + "_Sprite"):
            if BO[0] == RogueX:
                show Rogue_Sprite at sprite_location(RogueX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == KittyX:
                show Kitty_Sprite at sprite_location(KittyX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == LauraX:
                show Laura_Sprite at sprite_location(LauraX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == JeanX:
                show Jean_Sprite at sprite_location(JeanX.sprite_location,50):
                    ease .5 ypos 250
            elif BO[0] == JubesX:
                show Jubes_Sprite at sprite_location(JubesX.sprite_location,50):
                    ease .5 ypos 250
        $ BO.remove(BO[0])

    call Shift_Focus(Girl)
    if EmmaX.Loc == "bg teacher":
        "[EmmaX.Name] is giving a lecture on mutant relations. Sitting next to you, you notice [Girl.Name] shifting uncomfortably in her seat."

        $ Teacher = EmmaX
    elif StormX.Loc == "bg teacher":
        "[StormX.Name] is giving a lecture on geography and politics. Sitting next to you, you notice [Girl.Name] shifting uncomfortably in her seat."

        $ Teacher = StormX
    else:
        "Professor McCoy is giving a lecture on the X-Gene. Sitting next to you, you notice [Girl.Name] shifting uncomfortably in her seat."

    "Occasionally, you catch her glancing over your way."
    "[Girl.Name] opens her notebook and begins scratching out a note."
    "She detaches the slip of paper from the binder, carefully folding it before sliding it in front of you."
    "She watches you as you unfold the note."

    if "friskyclass" in Girl.History:
        "It reads \"Did you want to fool around again? Y[[] N[[]\""

        menu:
            "Y":
                $ Girl.FaceChange("sly",1)
                $ Girl.Statup("Love", 80, 3)
                $ Girl.Statup("Inbt", 60, 3)

                "She smiles suggestively."

                $ D20 = renpy.random.randint(1, 15)

                jump Frisky_Class_Loop
            "N":
                $ Girl.Statup("Love", 80, -10)
                $ Girl.Statup("Love", 70, -5)
                $ Girl.Statup("Obed", 70, 5)
                $ Girl.Statup("Inbt", 60, -3)

                $ Line = "rejected"

                $ Girl.FaceChange("angry")
                $ Girl.DailyActions.append("angry")

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
        $ Girl.FaceChange("smile",2)

        "You look back and see that she's blushing slightly."
        "She slides her pen over to you so you can reply."

        $ Girl.FaceChange("smile",1)
    else:
        $ Girl.FaceChange("sly",1)

        "You look back and see that she's staring at you suggestively."
        "She slides her pen over to you so you can reply."

    menu:
        "You reply. . ."
        "What are you talking about?":
            jump Frisky_Class_End
        "Naah. Not so much.":
            $ Girl.Statup("Love", 80, -3)
            $ Girl.Statup("Inbt", 60, -3)
            $ Girl.FaceChange("confused")

            jump Frisky_Class_End
        "It's my favorite subject." if Girl in [RogueX, KittyX]:
            $ Girl.Statup("Love", 80, 5)
            $ Girl.FaceChange("smile")

            "[Girl.Name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could study together tonight?\"."

            $ Line = "continue"
        "Yeah, pretty lame." if Girl not in [RogueX, KittyX]:
            $ Girl.Statup("Love", 80, 5)
            $ Girl.FaceChange("smile")

            "[Girl.Name] reads your note and starts to smile. She quickly dashes off another note, sliding it in front of you again."
            "You unfold the note, trying not to let the teacher see you. \"Then maybe we could 'study' together tonight?\"."

            $ Line = "continue"
        "I do when it's about you." if Girl in [RogueX, KittyX]:
            $ Line = "her"
        "I was too busy thinking about you." if Girl not in [RogueX, KittyX]:
            $ Line = "her"

    if Line == "her":
        if ApprovalCheck(Girl, 500, "I") or Girl.SEXP >= 30:
            $ Girl.FaceChange("sly")

            "[Girl.Name] reads your note and smiles at you suggestively."

            $ Line = "flirt"
        elif ApprovalCheck(Girl, 900):
            if Girl in [RogueX, KittyX]:
                $ Girl.FaceChange("confused",2)

                "[Girl.Name] reads your note and blushes furiously, looking down at her notes."
            else:
                $ Girl.FaceChange("sly",1)

                "[Girl.Name] reads your note and gets a sly smile, looking down at her notes."
            $ Girl.FaceChange("bemused",1)
            $ Line = "flirt"
        else:
            if Girl in [RogueX, KittyX]:
                $ Girl.FaceChange("perplexed",2)

                "[Girl.Name] reads your note and blushes furiously. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could study tonight?\"."
            else:
                $ Girl.FaceChange("sly",1)

                "[Girl.Name] reads your note and gets a sly smile. She quickly dashes off another note, sliding it in front of you again."
                "You unfold the note, trying not to let the teacher see you. \"I meant the class! Maybe we could 'study' tonight?\"."

            $ Girl.FaceChange("bemused",1)

            $ Line = "continue"

    if Line == "continue":
        if Girl in [RogueX, KittyX]:
            "[Girl.Name]'s drawn a little heart as the period at the bottom of the question mark."

        "She's trying to act like she's paying attention to the lecture, but she can't hide the big smile on her face."

        menu:
            "You respond. . ."
            "Maybe later.":
                $ Girl.Statup("Love", 80, -3)
                $ Girl.Statup("Obed", 70, 5)
                $ Girl.Statup("Inbt", 60, -3)
                $ Girl.FaceChange("confused")

                $ Line = 0

                jump Frisky_Class_End
            "Naah. I've got better things to do.":
                $ Girl.Statup("Love", 80, -10)
                $ Girl.Statup("Love", 70, -5)
                $ Girl.Statup("Obed", 70, 5)
                $ Girl.Statup("Inbt", 60, -3)

                $ Line = "rejected"

                $ Girl.FaceChange("angry")
                $ Girl.DailyActions.append("angry")

                jump Frisky_Class_End
            "Count on it.":
                $ Girl.FaceChange("smile")

                "She smiles when she reads your reply, and throws you a wink."

                $ Girl.DailyActions.append("studydate")

                "The rest of class is uneventful."

                return
            "We could get some \"studying\" done right now.":
                    if ApprovalCheck(Girl, 1000):
                        $ Girl.FaceChange("sly",1)
                        $ Girl.Statup("Love", 80, 3)
                        $ Girl.Statup("Inbt", 60, 3)

                        "[Girl.Name] gets a mischevious grin on her face and leans towards you."

                        $ Line = "flirt"
                    elif ApprovalCheck(Girl, 700):
                        $ Girl.FaceChange("smile",1)
                        $ Girl.Statup("Inbt", 60, 2)

                        if Girl in [RogueX, KittyX]:
                            "[Girl.Name] blushes and smiles your way."
                        else:
                            "[Girl.Name] startles a bit and smiles your way."
                        $ Line = "flirt"
                    else:
                        $ Girl.FaceChange("confused",1)

                        "[Girl.Name] looks a bit surprised, then scowls at you."

                        jump Frisky_Class_End

    if Line == "flirt":
        $ Round -= 20
        $ D20 = renpy.random.randint(1, 15)

        $ Girl.FaceChange("sly")

        "You notice one of [Girl.Name]'s shoes slip from her foot beneath the desk. She tosses you a sly grin."
        if Girl.Hose:
            "You feel the smooth texture of her stockinged foot begin to slowly slide back and forth along the length of your calf."
        else:
            "You feel the smooth skin of her bare foot begin to slowly slide back and forth along the length of your calf."

        while D20 <= 21 or "go on" in Player.RecentActions:
            menu Frisky_Class_Loop:
                "Pull away from her.":
                    if Line == "fondle pussy":
                        "You slowly slide your hand from her lap and start taking notes again."

                        $ Line = "tease"
                    elif Line == "fondle breast":
                        "With a final squeeze, you move your hand back to the desktop."

                        $ Line = "tease"
                    elif Girl.OCount and Girl.Lust < 90:
                        "That'll probably do for now. . ."

                        $ Line = "tease"
                    else:
                        $ Line = "rejected"

                        $ Girl.Statup("Love", 200, -15)
                        $ Girl.Statup("Obed", 70, 2)
                        $ Girl.Statup("Inbt", 60, -2)
                    jump Frisky_Class_End
                "Look into her eyes and smile slightly." if Line == "flirt":
                    $ Girl.FaceChange("smile")
                    $ Girl.Statup("Love", 200, 5)

                    "[Girl.Name] smiles back."
                    "She looks back towards the front of the class, but her hand drifts across the top of the desk until she's holding yours."

                    $ Line = "handholding"

                    jump Frisky_Class_Loop
                "Grasp her hand gently, stroking the top of it." if Line == "handholding":
                    $ Girl.Statup("Love", 200, 5)
                    $ Girl.Statup("Lust", 50, 5)
                    $ Girl.FaceChange("smile")

                    "[Girl.Name] sighs contentedly and holds your hand for the remainder of class."

                    jump Frisky_Class_End
                "Try and slip your hand to her lap." if Line != "fondle pussy":
                    $ Line = "fondle pussy"

                    if ApprovalCheck(Girl, 1200) and Girl.FondleP and Girl.SEXP >= 40:
                        $ Girl.FaceChange("sly")
                        $ Girl.Statup("Love", 90, 5)
                        $ Girl.Statup("Obed", 70, 5)
                        $ Girl.Statup("Inbt", 60, 5)

                        "[Girl.Name] gets a mischievous grin and places her hand on your arm."
                    elif ApprovalCheck(Girl, 1400) and Girl.FondleP:
                        $ Girl.FaceChange("smile")
                        $ Girl.Statup("Love", 80, 3)
                        $ Girl.Statup("Obed", 70, 7)
                        $ Girl.Statup("Inbt", 60, 3)

                        "[Girl.Name] starts slightly as your hand travels up her thigh, but then she lets out a slight grin."
                    elif ApprovalCheck(Girl, 1500):
                        $ Girl.FaceChange("perplexed",2)
                        $ Girl.Statup("Obed", 70, 10)
                        $ Girl.Statup("Inbt", 60, 3)

                        "[Girl.Name] glances at you in alarm, but then slowly calms down."

                        $ Girl.FaceChange("smile",1)

                        $ D20 += 2
                    else:
                        $ Line = "too far"

                    if Line == "fondle pussy":
                        $ Girl.FaceChange("sly")
                        $ Girl.Statup("Lust", 94, 5)
                        if Girl.PantsNum() == 5:
                            "[Girl.Name]'s sly smile turns sultry as she feels your fingers sneak under the hem of her skirt, slowly tracing the soft contours of her mound."
                        elif Girl.PantsNum() >= 7:
                            "[Girl.Name]'s sly smile turns sultry as she feels your fingers sneak down her pants, slowly tracing the soft contours of her mound."
                        else:
                            "[Girl.Name]'s sly smile turns sultry as she feels your fingers sneak between her legs, slowly tracing the soft contours of her mound."

                        $ Girl.Statup("Lust", 94, 5)

                        if Girl.Panties == "shorts":
                            "You think her shorts are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif Girl.Panties:
                            "You think her panties are becoming damp as you stroke the thin material. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        elif Girl.Pubes:
                            "You feel her soft fur moisten as you stroke the soft flesh below. Her cheeks are flushed and her breathing's starting to become shallower and quicker."
                        else:
                            "You feel her lips moisten as you stroke the soft flesh. Her cheeks are flushed and her breathing's starting to become shallower and quicker."

                        $ Trigger = "fondle pussy"
                        $ D20 += 5
                "Keep fondling her pussy." if Line == "fondle pussy":
                    $ Girl.Statup("Obed", 70, 5)
                    $ Girl.Statup("Inbt", 60, 3)
                    $ Girl.Statup("Lust", 89, 5)
                    $ Girl.Statup("Lust", 94, 5)

                    $ LineB = renpy.random.choice(["As the class drones on, you continue to slowly massage her warm delta.",
                        "As the class continues, you continue to slowly massage her moist pussy.",
                        "As the lecture drones on, you continue to slowly stroke her clit.",
                        "As the class continues, you continue to slowly caress her labia."])
                    "[LineB]"

                    $ D20 += 5
                "Start fondling her tits." if Line != "fondle breasts":
                    $ Line = "fondle breasts"
                    if ApprovalCheck(Girl, 1100) and Girl.FondleB and Girl.SEXP >= 40:
                        $ Girl.Statup("Love", 80, 5)
                        $ Girl.Statup("Obed", 70, 5)
                        $ Girl.Statup("Inbt", 60, 3)
                        $ Girl.FaceChange("sly")

                        "[Girl.Name] closes her eyes and caresses your arm."
                    elif ApprovalCheck(Girl, 1300) and Girl.FondleB:
                        $ Girl.Statup("Love", 80, 3)
                        $ Girl.Statup("Obed", 70, 7)
                        $ Girl.Statup("Inbt", 60, 3)
                        $ Girl.FaceChange("smile",1)

                        "[Girl.Name] flinches as your hand travels up her ribcage, but she grins as you reach her breast."
                    elif ApprovalCheck(Girl, 1400):
                        $ Girl.Statup("Obed", 70, 10)
                        $ Girl.Statup("Inbt", 60, 3)
                        $ Girl.FaceChange("perplexed",2)

                        "[Girl.Name] glances at you in alarm, but then slowly calms down."

                        $ Girl.FaceChange("smile",2)
                        $ D20 += 5
                    else:
                        $ Line = "too far"

                    if Line == "fondle breasts":
                        $ Girl.FaceChange("sly")
                        $ Girl.Statup("Lust", 94, 5)

                        "[Girl.Name]'s sly eyes spakle as your hand cups her breast, giving it a casual caress."
                        "Her nipples begin to firm up and she lets out a small moan of pleasure."

                        $ D20 += 7
                        $ Trigger = "fondle breasts"
                "Keep fondling her tits." if Line == "fondle breasts":
                    $ Girl.Statup("Obed", 70, 5)
                    $ Girl.Statup("Inbt", 60, 2)
                    $ Girl.Statup("Lust", 95, 3)

                    "Barely paying attention to the lecture, you continue to pulse her breast in your palm."

                    $ D20 += 7
                "Try and pull her hand toward your lap." if not Trigger2 and Player.Semen:
                    if "hand" in Girl.RecentActions:
                        "[Girl.Name] grins and her hand grasps your cock again."
                    elif ApprovalCheck(Girl, 1200) and Girl.Hand and Girl.SEXP >= 40:
                        $ Girl.FaceChange("sly")
                        $ Girl.Statup("Love", 90, 5)
                        $ Girl.Statup("Obed", 70, 5)
                        $ Girl.Statup("Inbt", 60, 5)

                        "[Girl.Name] gets a mischievous grin and her hand starts to caress your crotch."
                    elif ApprovalCheck(Girl, 1400) and Girl.FondleP:
                        $ Girl.FaceChange("smile")
                        $ Girl.Statup("Love", 80, 3)
                        $ Girl.Statup("Obed", 70, 7)
                        $ Girl.Statup("Inbt", 60, 3)

                        "[Girl.Name] starts slightly as your move her hand up your thigh, but then she lets out a slight grin."
                    elif ApprovalCheck(Girl, 1500):
                        $ Girl.FaceChange("perplexed",2)
                        $ Girl.Statup("Obed", 70, 10)
                        $ Girl.Statup("Inbt", 60, 3)

                        "[Girl.Name] glances at you in alarm, but then slowly calms down."

                        $ Girl.FaceChange("smile",1)
                        $ D20 += 2
                    else:
                        $ Line = "too far"

                    if Line != "too far":
                        $ Girl.FaceChange("sly")
                        $ Girl.Statup("Lust", 94, 5)

                        if "cockout" not in Player.RecentActions:
                            "[Girl.Name]'s hand slowly unzips your pants and pulls your cock free."

                            $ Player.AddWord(1,"cockout")

                            call Seen_First_Peen(Girl,Partner)

                            $ Girl.Statup("Lust", 94, 5)

                        $ Trigger2 = "hand"
                        $ Girl.RecentActions.append("hand")
                        $ Girl.DailyActions.append("hand")

                        "She begins to gently stroke it. . ."

                        if "hand" not in Girl.RecentActions:
                            $ Girl.Hand += 1
                        $ D20 += 5
                "Stop her handjob." if Trigger2:
                    "You put a hand on her wrist and nudge her hand away."
                    if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 700, "O") or (Girl.Love+Girl.Obed) >= (2*Girl.Inbt):
                        $ Girl.FaceChange("sad")
                        $ Girl.Statup("Love", 90, -1)
                        $ Girl.Statup("Obed", 60, 2)
                        $ Girl.Statup("Obed", 80, 3)

                        "[Girl.Name] allows her hand to be pulled away and goes back to what she'd been doing with it."

                        $ Girl.FaceChange("sly")
                        $ Trigger2 = 0
                    else:
                            $ Girl.FaceChange("angry")
                            $ Girl.Statup("Love", 80, -3)
                            $ Girl.Statup("Love", 90, -1)
                            $ Girl.Statup("Obed", 70, -2)
                            $ Girl.Statup("Inbt", 60, 3)
                            $ Girl.Statup("Inbt", 80, 2)

                            "[Girl.Name] grasps your cock tightly, then continues to stroke it when you let go."

                            $ Girl.FaceChange("sly")
                            $ D20 += 2

            if not Trigger2 and Player.Semen and "stophand" not in Girl.RecentActions:
                if ApprovalCheck(Girl, 1200) and ApprovalCheck(Girl, 400, "I") and Girl.Hand and Girl.SEXP >= 40:
                    $ Girl.FaceChange("sly")

                    "[Girl.Name] gets a mischievous grin and her hand starts to caress your crotch."

                    menu:
                        "What do you do?"
                        "Let her":
                            "You smile and nod a little."

                            $ Girl.FaceChange("sly")
                            $ Girl.Statup("Love", 80, 1)
                            $ Girl.Statup("Inbt", 70, 3)
                            $ Girl.Statup("Inbt", 90, 2)
                            $ Girl.Statup("Lust", 94, 5)

                            if "cockout" not in Player.RecentActions:
                                "[Girl.Name]'s hand slowly unzips your pants and pulls your cock free."

                                $ Player.AddWord(1,"cockout")

                                call Seen_First_Peen(Girl,Partner)

                                $ Girl.Statup("Lust", 94, 5)

                            $ Trigger2 = "hand"

                            $ Girl.RecentActions.append("hand")
                            $ Girl.DailyActions.append("hand")

                            "She begins to gently stroke it. . ."

                            if "hand" not in Girl.RecentActions:
                                $ Girl.Hand += 1

                            $ D20 += 10
                        "Stop her":
                            "You put a hand on her wrist and nudge her hand away."

                            $ Girl.RecentActions.append("stophand")

                            if ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 700, "O") or (Girl.Love+Girl.Obed) >= (2*Girl.Inbt):
                                $ Girl.FaceChange("sad")
                                $ Girl.Statup("Love", 90, -1)
                                $ Girl.Statup("Obed", 60, 2)
                                $ Girl.Statup("Obed", 80, 3)

                                "[Girl.Name] allows her hand to be pulled away and goes back to what she'd been doing with it."

                                $ Girl.FaceChange("sly")
                                $ Trigger2 = 0
                            else:
                                $ Girl.FaceChange("angry")
                                $ Girl.Statup("Love", 80, -3)
                                $ Girl.Statup("Love", 90, -1)
                                $ Girl.Statup("Obed", 70, -2)
                                $ Girl.Statup("Inbt", 60, 3)
                                $ Girl.Statup("Inbt", 80, 2)

                                "[Girl.Name] stops, but looks really annoyed."

                                $ D20 += 10

            if Trigger2:
                "[Girl.Name]'s hand continues to caress your cock. . ."

                $ Player.Focus += 15 if Player.Focus < 60 else 10

                if Player.Focus >= 100:
                    "As you start to reach your limits, [Girl.Name] places a hand over your cock."
                    "You jiz all over her hand."

                    $ Player.Semen -= 1

                    if (Girl.Blow and ApprovalCheck(Girl, 1200)) or Girl == JubesX:
                        "She quickly licks it all up."

                        $ Girl.Addict -= 20
                        $ Girl.Swallow += 1
                        $ Girl.RecentActions.append("swallow")
                        $ Girl.DailyActions.append("swallow")
                    else:
                        "She quickly wipes her hand off under the desk."

                    $ Girl.Statup("Lust", 200, 5)

                    $ D20 += 10

                    if not Player.Semen:
                        "She continues to lightly stroke you, but you don't seem up to it for now. . ."

                        $ Trigger2 = 0

                $ D20 += 5

            if Girl.Lust >= 95:
                $ LineB = Line

                call Girl_Cumming(Girl,1)

                $ Line = LineB
                $ LineB = renpy.random.choice([Girl.Name+" collapses over her desk.",
                        Girl.Name+" mumbles something unintelligible.",
                        Girl.Name+" bites her lip as she struggles to stay upright.",
                        Girl.Name+" seems a bit flushed."])
                "[LineB]"

                $ D20 += 15

            $ Round -= 7

            if Round <= 15:
                "Unfortunately it seems like class is wrapping up. You'll have to save this for later. . ."

                $ Line = "tease"
                jump Frisky_Class_End

            if Line == "too far":
                $ Girl.FaceChange("surprised",2)
                $ Girl.Statup("Love", 80, -5)
                $ Girl.Statup("Obed", 70, 7)
                $ Girl.Statup("Inbt", 50, -3)

                "[Girl.Name] sits up straight in her seat and makes a little yelping noise."

                $ Girl.FaceChange("angry",1)

                "Between that and the icy glare she shoots you, it's enough to draw the attention of your fellow students in your direction."

                $ D20 += 20

                if "go on" in Player.RecentActions:
                    $ Line = "caught"
                    jump Frisky_Class_End
            else:
                if len(Present) >= 2 and D20 >= 15:
                    if Partner:
                        $ Partner.GirlLikeUp(Girl,2)
                        $ Girl.GirlLikeUp(Partner,2)
                        $ Partner.Statup("Lust", 95, 3)
                        $ LineB = renpy.random.choice([0,
                            0,
                            0,
                            Partner.Name+" seems into it. . .",
                            Partner.Name+"'s hand moves a bit faster.",
                            Partner.Name+" bites her lip as her hand continues to move.",
                            Partner.Name+"'s hand slows down a bit."])
                        if LineB:
                            "[LineB]"

                        if Partner.Lust >= 95:
                            $ LineB = Line

                            call Girl_Cumming(Partner,1)

                            $ Line = LineB
                            $ LineB = renpy.random.choice([Partner.Name+" collapses over her desk.",
                                    Partner.Name+" mumbles something unintelligible.",
                                    Partner.Name+" bites her lip as she struggles to stay upright.",
                                    Partner.Name+" seems a bit flushed."])

                            "[LineB]"

                            $ D20 += 15
                    elif "saw with "+ Girl.Tag in Present[1].Traits:
                        call AnyLine(Present[1],"Well!")

                        $ Present[1].GirlLikeUp(Girl,-4)
                        $ Girl.GirlLikeUp(Present[1],-2)

                        call Remove_Girl(Present[1])
                    elif ApprovalCheck(Present[1], 1500) and Present[1].GirlLikeCheck(Girl) >= 600:
                        $ Present[1].Eyes = "leftside"

                        "[Present[1].Name] seems to notice what you and [Girl.Name] are doing."

                        $ Present[1].FaceChange("sly",1)

                        "She seems to be kinda into it. . ."

                        if ApprovalCheck(Present[1], 800, "I") or "exhibitionist" in Present[1].Traits:
                            $ Girl.Statup("Inbt", 90, 3)
                            $ Present[1].GirlLikeUp(Girl,3)
                            $ Girl.GirlLikeUp(Present[1],5)
                            $ Present[1].Statup("Lust", 89, 7)

                            "You notice that [Present[1].Name]'s begun feeling herself up as well."

                            $ Present[1].AddWord(1,"frisky","frisky",0,0)
                            $ Partner = Present[1]
                    else:
                        $ Present[1].Eyes = "leftside"

                        "[Present[1].Name] seems to notice what you and [Girl.Name] are doing."

                        $ Present[1].AddWord(1,0,0,"saw with " + Girl.Tag)
                        $ Present[1].FaceChange("angry",1)

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

                        if "go on" in Player.RecentActions:
                            $ Line = "caught"
                            jump Frisky_Class_End

                if Teacher and "frisky" in Teacher.RecentActions:
                    $ Teacher.GirlLikeUp(Girl,2)
                    $ Girl.GirlLikeUp(Teacher,2)
                    $ Teacher.Statup("Lust", 95, 3)

                    $ LineB = renpy.random.choice([0,
                        0,
                        0,
                        Teacher.Name+" stumbles a bit over the delivery of the next portion of her lecture.",
                        Teacher.Name+"'s hand moves a bit faster.",
                        Teacher.Name+" bites her lip as her hand continues to move.",
                        Teacher.Name+"'s hand slows down a bit."])

                    if LineB:
                        "[LineB]"

                    if Teacher.Lust >= 95:
                        $ LineB = Line

                        call Girl_Cumming(Teacher,1)

                        $ Line = LineB

                        $ LineB = renpy.random.choice([Teacher.Name+" stumbles a bit over the delivery of the next portion of her lecture.",
                            Teacher.Name+" mumbles something unintelligible but continues the lecture.",
                            Teacher.Name+" bites her lip as she struggles to continue talking.",
                            Teacher.Name+" seems a bit under the weather.",
                            Teacher.Name+" seems a bit flushed."])

                        "[LineB]"

                        $ D20 += 15

                if D20 > 30:
                    if D20 >= 50:
                        $ LineB = renpy.random.choice([0,
                            0,
                            0,
                            "The class isn't paying attention to the lecture anymore.",
                            "The class definitely seems into the show she's putting on.",
                            "The class is hooting and hollering.",
                            "The students seem to be watching you intently."])
                    else:
                        $ LineB = renpy.random.choice([0,
                            0,
                            0,
                            "The class seems a little confused as to what she's talking about.",
                            "The class seems a little confused as to what she's doing back there.",
                            "The class is shifting strange looks your way.",
                            "A bunch of students seem to be watching you intently."])
                    if LineB:
                        "[LineB]"

        if "exhibitionist" not in Girl.Traits and not ApprovalCheck(Girl, 700,"I"):
            $ Line = "too far"

        if Line not in ("rejected", "handholding", "tease"):
                $ Girl.FaceChange("surprised")

                if Teacher:
                    $ Teacher.FaceChange("surprised",1)

                    "[Teacher.Name] stops her lecture in mid-sentence when she notices what you and [Girl.Name] are up to."

                    if ApprovalCheck(Teacher, 1500) and Teacher.GirlLikeCheck(Girl) >= 600:
                        $ Teacher.FaceChange("sly",1)

                        if Line == "too far":
                            $ Girl.Mouth = "sad"

                            if Teacher == EmmaX:
                                "She looks over at you and shrugs as she continues her lecture, but the moment has past."
                            elif Teacher == StormX:
                                "She looks over at you and smiles consolingly as she continues her lecture, but the moment has past."

                            jump Frisky_Class_End

                        "She gets a sly smile on her face and continues her lecture."

                        $ Girl.FaceChange("sly",1)

                        if ApprovalCheck(Teacher, 800, "I") or "exhibitionist" in Teacher.Traits:
                            $ Teacher.Statup("Inbt", 90, 3)
                            $ Teacher.GirlLikeUp(Girl,3)
                            $ Girl.GirlLikeUp(Teacher,5)
                            $ Teacher.Statup("Lust", 89, 7)

                            "You notice that [Teacher.Name]'s hand has snaked down beneath the podium and begun to move."

                            $ Teacher.AddWord(1,"frisky","frisky",0,0)
                            $ Player.AddWord(1,"go on","go on",0,0)

                        "[Girl.Name] looks around and shrugs. . ."
                        jump Frisky_Class_Loop
                    else:
                        $ Teacher.FaceChange("angry",1)
                        $ Girl.Mouth = "sad"

                        if Teacher == EmmaX:
                            ch_e "[EmmaX.Petname], [Girl.Tag], if you could perhaps pay more attention to the lecture, and less to each other's bodies?"
                            ch_e "Perhaps it would be best if you visited the headmaster's office and cool off?"
                        elif Teacher == StormX:
                            ch_s "[StormX.Petname], [Girl.Tag], I can appreciate your enthusiasm, but perhaps not on my time?"
                            ch_s "I think perhaps you should visit Charles and cool off?"
                else:
                    "Dr. McCoy stops his lecture in mid-sentence when he notices that the whole class is looking at you and [Girl.Name]."
                    ch_b "Oh, my stars and garters!"
                    ch_b "[Player.Name]!?! {b}WHAT ARE YOU DOING? BOTH OF YOU, TO THE PROFESSOR'S OFFICE, IMMEDIATELY!{/b}"

                $ Girl.AddWord(1, 0, 0, 0, "friskyclass")

                $ Line = 0

                $ Girl.Statup("Love", 80, -10)
                $ Girl.Statup("Obed", 70, -5)
                $ Girl.Statup("Inbt", 50, -10)

                $ Trigger = 0

                if Girl not in Rules:
                    call Girls_Caught(Girl)
                else:
                    "Since Xavier isn't concerned with your activities, you both head back to your room instead."

                    $ Girl.Loc = "bg player"

                    call CleartheRoom(Girl,0,1)
                    jump player_room

label Frisky_Class_End:
    $ Trigger = 0
    $ Partner = 0

    if Teacher:
        $ Teacher.DrainWord("frisky", 1, 0)
    if not Line:
        $ Girl.FaceChange("confused")

        "She unfolds the note and quickly reads it over."

        $ Girl.FaceChange("sad")

        "As she does, you immediately see disappointment come over her features."
        "She scratches out a reply and slides it back in front of you."
        "When you open it up, it reads: {i}Never mind.{/i}"
    elif Line == "tease":
        if Girl.Lust >= 80:
            $ Girl.FaceChange("surprised",2)

            "[Girl.Name] startles briefly."

            $ Girl.FaceChange("sad",2)

            "[Girl.Name] she looks over at you a bit upset that you ended things so abruptly."
        $ Girl.AddWord(1, 0, 0, 0, "friskyclass")
        $ Girl.FaceChange("sly",1)

        "[Girl.Name] takes in a deep breath and exhales it in a sigh, leaning in to whisper."
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
    elif Line == "rejected":
        if Girl in [RogueX, KittyX]:
            $ Girl.FaceChange("sadside")

            "[Girl.Name] looks surprised and hurt. For the rest of the class, she says nothing."
        else:
            $ Girl.FaceChange("angry")

            "[Girl.Name] looks surprised and hurt. For the rest of the class, she stares daggers at you."
        "It seems like she has a hard time looking you in the eye."
    elif Line == "caught":
        "You quickly separate and go back to trying to study. . ."

    "Eventually, [Girl.Name] seems to settle down and pay attention to the course material. You manage to do the same without falling asleep."

    $ Line = 0

    return
