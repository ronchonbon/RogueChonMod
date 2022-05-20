

label Worldmap:
    $ Taboo = 0
    menu:
        "Where would you like to go?"
        "My Room":
            $ renpy.pop_call()
            jump player_room_Entry
        "Girl's Rooms":
            menu:
                "[RogueX.name]'s Room":
                    call girls_room_entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call girls_room_entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call girls_room_entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call girls_room_entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call girls_room_entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call girls_room_entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call girls_room_entry (JubesX)
                "Back":
                    jump Worldmap
        "University Square":
            $ renpy.pop_call()
            jump Campus_Entry
        "Class":
            if time_index < 3:
                $ renpy.pop_call()
                jump Class_Room_Entry
            elif "Xavier" in Keys:
                "The door is locked, but you were able to use Xavier's key to get in."
                $ renpy.pop_call()
                jump Class_Room_Entry
            else:
                "It's late for classes and the classrooms are locked down."
                jump Worldmap
        "The Danger Room":
            $ renpy.pop_call()
            jump Danger_Room_Entry
        "The showers":
            $ renpy.pop_call()
            jump Shower_Room_Entry
        "The pool":
            $ renpy.pop_call()
            jump Pool_Entry
        "Xavier's Study":
            $ renpy.pop_call()
            jump Study_Room_Entry

        "Go to the mall" if "mall" in Player.history and time_index < 3:
            call Mall_Entry
            jump Campus

        "Attic" if "attic" in Player.history:
            jump StormMeet
        "Stay where I am.":
            return
    return




label Misplaced:
    if primary_action and primary_action in all_Girls:

        call expression primary_action.tag + "_SexMenu"


    scene onlayer black
    $ Player.drain_word("locked",0,0,1)
    $ StackDepth = renpy.call_stack_depth()
    while StackDepth > 0:
        $ StackDepth -= 1
        $ renpy.pop_call()
    if bg_current == "bg_player":
        jump player_room
    if bg_current == "bg_rogue":
        call girls_room(RogueX)
        return
    if bg_current == "bg_kitty":
        call girls_room(KittyX)
        return
    if bg_current == "bg_emma":
        call girls_room(EmmaX)
        return
    if bg_current == "bg_laura":
        call girls_room(LauraX)
        return
    if bg_current == "bg_jean":
        call girls_room(JeanX)
        return
    if bg_current == "bg_storm":
        call girls_room(StormX)
        return
    if bg_current == "bg_jubes":
        call girls_room(JubesX)
        return
    if bg_current == "bg_dangerroom":
        jump Danger_Room
    if bg_current == "bg_classroom":
        jump Class_Room
    if bg_current == "bg_showerroom":
        jump Shower_Room
    if bg_current == "bg_study":
        jump Study_Room
    if bg_current == "bg_pool":
        jump Pool_Entry
    if bg_current in ("bg_mall","bg_shop","bg_dressing"):
        call Shopping_Mall
        return
    jump Campus

    return





label Campus_Map:
    $ Line = 0
    $ primary_action = 0
    $ offhand_action = 0
    $ girl_offhand_action = 0
    $ second_girl_primary_action = 0
    $ second_girl_offhand_action = 0
    $ bg_current = "bg_campus"
    $ Player.drain_word("locked",0,0,1)
    call set_the_scene
    if not TravelMode:
        call Worldmap
    jump Campus

label Campus_entering:
    call Jubes_Entry_Check
    $ Player.drain_word("locked",0,0,1)
    $ bg_current = "bg_campus"
    $ Nearby = []
    call Gym_Clothes_Off
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    call EventCalls
    call set_the_scene

label Campus:
    $ bg_current = "bg_campus"
    $ Player.drain_word("traveling",1,0)
    call Taboo_Level
    call set_the_scene (silent=1)
    call QuickEvents
    call checkout (1)
    call GirlsAngry
    if time_index == 2 and "yesdate" in Player.daily_history:

        menu:
            "Ready to go on that date?"
            "Yes":
                call DateNight
                if "yesdate" in Player.daily_history:
                    $ Player.daily_history.remove("yesdate")
            "One moment. . .":
                pass
    if Round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."
            jump player_room
        call Wait
        call EventCalls
        call girls_location



    menu:
        "You are in the university square. What would you like to do?"
        "Chat":

            call Chat

        "Wait." if time_index < 3:
            "You wait around a bit."
            call Wait
            call EventCalls
            call girls_location

        "Go to my Room" if TravelMode:
            jump player_room_Entry
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call girls_room_entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call girls_room_entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call girls_room_entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call girls_room_entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call girls_room_entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call girls_room_entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call girls_room_entry (JubesX)
                "Back":
                    pass
        "Go to the classroom" if TravelMode:
            if time_index < 3:
                jump Class_Room_Entry
            elif "Xavier" in Keys:
                "The door is locked, but you were able to use Xavier's key to get in."
                jump Class_Room_Entry
            else:
                "It's late for classes and the classrooms are locked down."
        "Go to the Danger Room" if TravelMode:
            jump Danger_Room_Entry
        "Go to the showers" if TravelMode:
            jump Shower_Room_Entry
        "Go to the pool" if TravelMode:
            jump Pool_Entry
        "Xavier's Study" if TravelMode:
            jump Study_Room_Entry
        "Go to the mall" if TravelMode and "mall" in Player.history:
            call Mall_Entry

        "Leave" if not TravelMode:
            call Worldmap

    jump Campus






label Class_Room_entering:
    call Jubes_Entry_Check
    $ Player.drain_word("locked",0,0,1)
    $ Present = []
    $ bg_current = "bg_classroom"
    $ Nearby = []
    call Gym_Clothes_Off
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    call EventCalls
    call set_the_scene (0)
    $ Line = "entry"

label Class_Room:
    $ bg_current = "bg_classroom"
    if "goto" in Player.recent_history or "traveling" in Player.recent_history:
        $ Present = []
        if time_index < 2 and Weekday < 5:
            call Class_Room_Seating
        $ Player.drain_word("goto",1,0)
        $ Player.drain_word("traveling",1,0)
    call Taboo_Level
    call set_the_scene (silent=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."
            jump player_room
        call Wait
        call EventCalls
        call girls_location
    call GirlsAngry

    if Line == "entry":
        if EmmaX.location == "bg_teacher":
            $ Line = "As you sit down, you see "+ EmmaX.name +" at the podium. What would you like to do?"
        elif StormX.location == "bg_teacher":
            $ Line = "As you sit down, you see "+ StormX.name +" at the podium. What would you like to do?"
        elif time_index == 2 or Weekday > 5:
            $ Line = "You enter the classroom. What would you like to do?"
        else:
            $ Line = "You sit down at a desk. What would you like to do?"
    else:
        if Line != "What would you like to do next?":
            $ Line = "You are in class right now. What would you like to do?"



    menu:
        "[Line]"
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
            $ Line = "You are in class right now. What would you like to do?"

        "Lock the door" if "locked" not in Player.traits:
            if Weekday >=5 or time_index >= 2:
                "You lock the door"
                $ Player.traits.append("locked")
                call Taboo_Level
            else:
                "You can't really do that during class."

        "Unlock the door" if "locked" in Player.traits:
            "You unlock the door"
            $ Player.traits.remove("locked")
            call Taboo_Level

        "Wait" if time_index < 3:
            "You hang out for a bit."
            call Wait
            call EventCalls
            call girls_location

            if time_index < 2:
                $ Line = "A new class is in session. What would you like to do?"
            else:
                $ Line = "Classes have let out for the day. What would you like to do?"

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    $ Line = 0
    jump Class_Room



label Take_Class:
    call set_the_scene
    if "class" in Player.daily_history:
        $ Line = "The session begins."
    elif Round >= 80:
        $ Line = "You make it in time for the start of the class."
    elif Round >= 50:
        $ Line = "You get in a bit late, but there's plenty of class left."
    elif Round >= 30:
        $ Line = "You're pretty late, but catch the tail end of the class."
    $ primary_action = 0

    $ D20 = renpy.random.randint(1, 20)





    if D20 > 15 and Present and approval_check(Present[0], 300, "I"):

        "[Line]"
        call Frisky_Class (Present[0])
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
        "[Line]"
    $ Player.recent_history.append("class")
    $ Player.daily_history.append("class")
    $ Player.XP += (5 + (int(Round / 10)))

    call Wait
    call girls_location
    call set_the_scene
    call EventCalls
    $ Line = "What would you like to do next?"
    jump Class_Room




label Class_Room_Seating(Girls=[], GirlB=0, GirlLike=0, Line=0, D20=0, BO=[]):


    $ Present = []
    $ BO = active_Girls[:]
    while BO:

        if BO[0].location == bg_current:
            $ Girls.append(BO[0])
        $ BO.remove(BO[0])

    $ renpy.random.shuffle(Girls)

    $ BO = Nearby[:]
    while BO:

        if BO[0] not in Girls:
            $ Girls.append(BO[0])
        $ BO.remove(BO[0])



    $ Nearby = []

    call set_the_scene (0)
    if len(Girls) == 2:

        $ D20 = renpy.random.randint(500, 1500)
        if (Girls[0].GirlLikeCheck(Girls[1]) + Girls[1].GirlLikeCheck(Girls[0])) >= D20:
            "You see that [Girls[0].name] and [Girls[1].name] are sitting next to each other, which do you sit next to?"
        else:
            "You see that [Girls[0].name] and [Girls[1].name] are in the room, but on opposite sides."
            $ BO = Girls[:]
            while BO:

                if BO[0] not in Nearby:
                    $ Nearby.append(BO[0])
                $ BO.remove(BO[0])
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
                $ BO = Girls[:]
                while BO:

                    if BO[0] not in Nearby:
                        $ Nearby.append(BO[0])
                    $ BO.remove(BO[0])

    elif len(Girls) > 2:

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


    elif Girls:

        menu:
            "You see [Girls[0].name] is there, do you sit next to her?"
            "Yes":
                $ Present.append(Girls[0])
            "No, I'll sit away from her a bit.":
                $ Nearby.append(Girls[0])



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

        "The rest are scattered around the room."

    while Girls:
        if Girls[0] not in Present:

            if Girls[0] not in Nearby:
                $ Nearby.append(Girls[0])
            $ Girls[0].location = "nearby"
        $ Girls.remove(Girls[0])

    if Present:
        call shift_focus (Present[0])
    call set_the_scene (silent=1)

    return






label Danger_Room_entering:
    call Jubes_Entry_Check
    $ Player.drain_word("locked",0,0,1)
    $ bg_current = "bg_dangerroom"
    $ Nearby = []
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    call EventCalls
    call Gym_Entry
    call set_the_scene

label Danger_Room:
    $ bg_current = "bg_dangerroom"
    $ Player.drain_word("traveling",1,0)
    call Taboo_Level
    call set_the_scene (silent=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        "Looks like shifts are changing. . ."
        if time_index >=3:
            "You're getting tired, you head back to your room."
            jump player_room
        call Wait
        call EventCalls
        call girls_location
        call Gym_Clothes_Off
    call GirlsAngry



    menu:
        "This is the Danger Room. What would you like to do?"
        "Train":

            if time_index >= 3:
                "The Danger Room has been powered off for the night, maybe take a break."
            elif Round >= 30:
                jump Training
            else:
                "There really isn't time to do much before the next rotation, maybe wait a bit."
        "Chat":

            call Chat
        "Historical Simulator":
            ch_danger "This function allows you to revisit previous events in your history."
            ch_danger "Unfortunately, this function is temporarily disabled."


        "Lock the door" if "locked" not in Player.traits:
            if time_index >= 3:
                "You lock the door"
                $ Player.traits.append("locked")
                call Taboo_Level
            else:
                "You can't really do that during free hours."

        "Unlock the door" if "locked" in Player.traits:
            "You unlock the door"
            $ Player.traits.remove("locked")
            call Taboo_Level

        "Wait. (locked)" if time_index >= 3:
            pass
        "Wait." if time_index < 3:
            "You hang out for a bit."
            call Wait
            call EventCalls
            call girls_location
            call Gym_Clothes_Off

        "Leave" if not TravelMode:
            call Gym_Exit
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            call Gym_Exit
            jump Campus_Entry

        "Go to the showers" if TravelMode:
            call Gym_Exit
            jump Shower_Room_Entry
    jump Danger_Room

label Training:
    $ D20 = renpy.random.randint(1, 20)



    $ Player.XP += (5 + (int(Round / 10)))
    $ Player.daily_history.append("dangerroom")
    call set_the_scene

    if Round >= 80:
        $ Line = "You have a long session in the Danger Room."
    elif Round >= 50:
        $ Line = "You have a short workout in the Danger Room."
    else:
        $ Line = "You squeeze in a quick session in the Danger Room."

    $ primary_action = 0
    if D20 >= 18:

        "[Line] During the exercise, Cyclops accidentally shoots you."
        "Luckily you're immune to the beams, but your clothes weren't so lucky."
        call RoomStatboost ("love", 80, 2)
        call RoomStatboost ("lust", 80, 5)
    elif D20 >= 17:
        "[Line] You participate in a hand-to-hand combat class."
        "Before you begin, Cyclops explains that it’s always good to know how to defend yourself when you can’t rely on your powers."
        "It sounds like there’s a story there."
    elif D20 >= 16:
        "Some of the senior students walk over to talk about your powers."
        "Nightcrawler wonders aloud what would happen if he grabbed you and tried to teleport while you tried to disable his powers."
        "You succeed in freaking each other out."
    else:
        $ Line = Line + renpy.random.choice([" It was fairly boring.",
                    " You do some training with basic firearms.",
                    " You run the obstacle course.",
                    " You fight in a simulated battle against the Brotherhood.",
                    " You help take down a holographic Sentinel.",
                    " You take part in a training exercise against the Avengers. As if the X-Men and Avengers would ever fight.",
                    " You and some of the others take part in a survival exercise. . . also known as \"try to last as long as you can while Wolverine hunts you down one by one.\"",
                    " You decide to test yourself by facing off against Magneto solo. It goes about as well as you’d expect.",
                    " You use the Danger Room’s holograms to relive some of the original X-Men’s biggest battles. You learn quite a bit about teamwork.",
                    " Beast is teaching a class on parkour. You take part and pick up a few pointers. You’re no Spider-Man, but at least you pick up a few things.",
                    " You participate in an emergency drill. You pick up quite a few tips about first aid, triage and the proper way to move injured people.",
                    " You take part in an urban emergency situation exercise. Cyclops takes the time to explain to you how to use cover to get close enough to use your powers.",
                    " You take part in a jungle simulation exercise under Wolverine. You learn some basic survival techniques, but you privately hope you never need them.",
                    " Your team fight a simulation of Magneto."])
        "[Line]"

    $ Options = active_Girls[:]
    while Options:

        if Options[0].location == bg_current:
            call Girl_TightsRipped (Options[0])
        $ Options.remove(Options[0])
    call Wait
    call girls_location
    call set_the_scene
    $ Line = "The training session has ended, what would you like to do next?"

    jump Danger_Room

label Rogue_TightsRipped(Count=0):
    if RogueX.hose == "_tights":
        $ Count = 1
        $ RogueX.hose = "ripped_tights"
        $ RogueX.change_face("_angry")
        if "ripped_tights" in RogueX.inventory:
            ch_r "Damnation, that's another pair ruined!"
        else:
            $ Count = 2
            ch_r "Well that's a good pair of tights down the chute."
    elif RogueX.hose == "pantyhose":
        $ Count = 1
        $ RogueX.hose = "ripped_pantyhose"
        $ RogueX.change_face("_angry")
        if "ripped_pantyhose" in RogueX.inventory:
            ch_r "Tsk, another pair ruined!"
        else:
            $ Count = 2
            ch_r "I hate getting a run in these things."
    if Count:

        if not RogueX.legs and RogueX.underwear != "_shorts":
            if RogueX.underwear:
                if RogueX.SeenPanties:
                    $ Count = 3 if not approval_check(RogueX, 600) else Count
                else:
                    $ RogueX.SeenPanties = 1
                    $ Count = 3 if not approval_check(RogueX, 900) else Count
                $ RogueX.change_stat("lust", 60, 2)
            else:
                if RogueX.SeenPussy:
                    $ Count = 3 if not approval_check(RogueX, 900) else Count
                else:
                    call Rogue_First_Bottomless
                    $ Count = 3 if not approval_check(RogueX, 1400) else Count

        if Count == 2:

            menu:
                extend ""
                "I think those look really good on you.":
                    $ RogueX.change_face("_smile", 1)
                    $ RogueX.inventory.append(RogueX.hose)
                    ch_r "You think so? That's sweet, maybe I'll keep them on hand."
                "Yeah, too bad.":
                    $ RogueX.change_face("_bemused")
                    ch_r ". . ."
                "Ha! Those don't leave much to the imagination!":
                    ch_r "Thanks for that. . ."

        elif Count == 3:
            $ RogueX.change_face("startled", 2)
            ch_r "I, um, I should get out of here."
            $ RogueX.blushing = "_blush1"
            call Remove_Girl (RogueX)
            $ RogueX.change_outfit()

    return






label Pool_entering:
    call Jubes_Entry_Check
    $ Player.drain_word("locked",0,0,1)
    $ bg_current = "bg_pool"
    $ Nearby = []
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    call EventCalls
    call Gym_Clothes_Off
    call SwimSuit
    call set_the_scene

label Pool_Room:
    $ bg_current = "bg_pool"
    $ Player.drain_word("traveling",1,0)
    call Taboo_Level
    call set_the_scene (silent=1, Dress=0)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."
            jump player_room
        call Wait
        call EventCalls
        call girls_location
    call GirlsAngry



    menu:
        "You're at the pool. What would you like to do?"
        "Chat":

            call Chat

        "Want to sunbathe?" if time_index < 2:
            call Pool_Sunbathe
            $ Round -= 20 if Round >= 20 else Round
            "You just hang out for a little while."
        "Want to swim?":
            if time_index >= 3 and AloneCheck():
                "It's a bit late for a swim."
            else:
                call Pool_Swim
        "Want to skinnydip?":
            call Pool_Skinnydip

        "Wait. (locked)" if time_index >= 3:
            pass
        "Wait." if time_index < 3:
            "You hang out for a bit."
            call Wait
            call EventCalls
            call girls_location

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

        "Go to the showers" if TravelMode:
            jump Shower_Room_Entry
    jump Pool_Room

label Pool_Swim(Swimmers=[], BO=[]):
    $ D20 = renpy.random.randint(1, 20)

    $ Player.daily_history.append("swim")
    call set_the_scene

    $ Line = ""
    $ PassLine = 0
    $ BO = all_Girls[:]
    while BO:
        if bg_current == BO[0].location and approval_check(BO[0], 700):
            if BO[0].bra == BO[0].Swim[5] and BO[0].underwear == BO[0].Swim[6]:

                $ Swimmers.append(BO[0])
            elif not BO[0].ChestNum() and not BO[0].OverNum() and not BO[0].PantiesNum() and not BO[0].PantsNum() and not BO[0].HoseNum():

                $ Swimmers.append(BO[0])
            else:
                if Line or PassLine:

                    call Display_Girl (BO[0], 0, 0, 950, 150)
                else:
                    call Display_Girl (BO[0], 0, 0, 800, 150)
                if BO[0].change_outfit("swimwear"):

                    $ Line = "" if Swimmers and not PassLine else "s"
                    $ Swimmers.append(BO[0])
                else:

                    $ Line = "" if PassLine and not Swimmers else "s"
                    $ PassLine = PassLine + " and " + BO[0].name if PassLine else BO[0].name
        $ BO.remove(BO[0])

    if len(Swimmers) >= 2:
        "The girls get[Line] changed and join you."
    elif Swimmers:
        "[Swimmers[0].name] get[Line] changed and joins you."
    if PassLine:
        "[PassLine] chill[Line] out poolside."
    $ PassLine = 0
    $ Line = 0

    call ShowPool (Swimmers[:])

    if D20 >= 15 and Swimmers:
        call Pool_Topless (Swimmers[0])
    if D20 >= 11:
        "You take a nice, refreshing swim."
    elif D20 == 2:
        "You join some of the others in a rousing game of Marco Polo."
    elif D20 == 3:
        "You manage to snag one of the floating chairs and drift lazily on the water."
    elif D20 == 4:
        "You manage to snag one of the floating chairs and drift lazily on the water."
        "Until, that is, Kurt teleports up in the air nearby and performs an admittedly awesome cannonball."
        "Too bad it capsizes your chair."
    elif D20 == 5:
        "You test yourself by swimming from one end of the pool to the other."
    elif D20 == 6:
        "You try to impress some of the girls by doing a running jump into the pool."
        "You wind up triggering a cannonball competition that’s ironically NOT won by Cannonball, much to his shock."
    elif D20 == 7:
        "You are about to get into the pool when you hear annoyed cries and shouts of, \"Bobby!\""
        "Looks like Iceman made himself a floating chair again."
        "You stick to the far end of the pool, where it isn’t freezing cold."
    elif D20 == 8:
        "You relax on one of the poolside chairs instead."
    elif D20 == 9:
        "Cyclops is instructing some of the other students in water rescues."
        "You listen in as he talks about approaching a drowning victim from behind so that their panicked flailing won’t cause you injury."
    elif D20 == 10:
        "You decide to make use of the diving board. You do a couple of dives before taking it easy and just swimming around."

    call GirlWaitUp (1, 80, 3)
    call RoomStatboost ("love", 80, 3)
    call RoomStatboost ("lust", 30, 5)
    $ Round -= 20 if Round >= 20 else Round
    hide FullPool
    call set_the_scene (1, 0, 0)
    "You all get out of the pool and rest for a bit."
    return




label SwimSuit(BO=[]):

    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current and BO[0].Swim[0] and BO[0] not in Party and BO[0].Schedule[Weekday][time_index] == "bg_pool":


            $ BO[0].change_outfit("swimwear")
        $ BO.remove(BO[0])
    return

image FullPool:

    AlphaMask("bg_pool", "images/PoolMask.png")

label ShowPool(BO=[], PoolLoc=0):



    while BO:
        if BO[0].location == bg_current:
            $ BO[0].add_word(0,"swim","swim",0,0)
            $ BO[0].Water = 1
            $ BO[0].spunk = []
            $ PoolLoc = 500 if len(BO) > 1 else 650
            if BO[0] == RogueX:
                show Rogue_sprite zorder 50 at Pool_Bob(PoolLoc)
            elif BO[0] == KittyX:
                show Kitty_sprite zorder 50 at Pool_Bob(PoolLoc)
            elif BO[0] == EmmaX:
                show Emma_Sprite zorder 50 at Pool_Bob(PoolLoc)
            elif BO[0] == LauraX:
                show Laura_Sprite zorder 50 at Pool_Bob(PoolLoc)
            elif BO[0] == JeanX:
                show Jean_Sprite zorder 50 at Pool_Bob(PoolLoc)
            elif BO[0] == StormX:
                show Storm_Sprite zorder 50 at Pool_Bob(PoolLoc)
            elif BO[0] == JubesX:
                show Jubes_Sprite zorder 50 at Pool_Bob(PoolLoc)
        $ BO.remove(BO[0])
    show FullPool zorder 60
    return










transform Pool_Bob(PoolLoc=500):
    subpixel True
    pos (PoolLoc,450)
    alpha 1
    zoom .45
    offset (0,0)
    anchor (0.5, 0.0)
    xoffset 0
    yoffset 0
    choice:
        yoffset 0
    choice:
        pause .3
    choice:
        pause .5
    block:
        ease 1 yoffset 10
        ease 1.5 yoffset 0
        repeat


label Shower_Room_entering:
    call Jubes_Entry_Check
    $ bg_current = "bg_showerroom"
    $ Player.drain_word("locked",0,0,1)
    $ Nearby = []
    $ Present = []
    call Taboo_Level
    call set_the_scene (0, 1, 0)
    $ Round -= 5 if Round >= 5 else Round
    if Round <= 10 or len(Party) >= 2:
        jump Shower_Room


    if Day >= 9 and "met" not in JeanX.history and "met" in EmmaX.history:
        call JeanMeet
        jump Shower_Room

    $ Options = []
    $ Line = active_Girls[:]
    while Line:

        if Line[0] not in Party and "showered" not in Line[0].daily_history and (Line[0].location == Line[0].home or Line[0].location == "bg_dangerroom"):

            $ Options.append(Line[0])
        $ Line.remove(Line[0])
    $ Line = 0

    if Options:
        $ renpy.random.shuffle(Options)

    $ D20 = renpy.random.randint(1, 20)



    if D20 < 5 or (len(Options) + len(Party) > 2):

        while Options and (D20 < 5 or len(Options) + len(Party) > 2):

            $ Nearby.append(Options[0])
            $ Options[0].location = "nearby"
            $ Options.remove(Options[0])

    if not Party and Options and Options[0] in all_Girls:
        if D20 > 15:
            call Girl_Caught_Shower (Options[0])
            jump Shower_Room
        elif D20 > 13:
            $ Options[0].add_word(1,"showered","showered",0,0)
            call Girl_Caught_Changing (Options[0])
            jump Shower_Room



    $ Line = Options[:]
    while Line:

        $ Line[0].location = bg_current
        $ Line.remove(Line[0])
    $ Line = 0

    call Present_Check (0)

    $ Line = Options[:]
    while Line:

        if Line[0].location == bg_current and Line[0] not in Party:
            if D20 >= 10:
                $ Line[0].add_word(1,"showered","showered",0,0)
            $ Line[0].change_outfit("_towel")
        $ Line.remove(Line[0])
    $ Line = 0


    call set_the_scene (Dress=0)
    if Party:
        $ Line = " and " + Party[0].name
    else:
        $ Line = ""
    if len(Options) >= 2:
        "As you enter, you[Line] see [Options[0].name] and [Options[1].name] standing there."
    elif Options:
        "As you enter, you[Line] see [Options[0].name] standing there."
    $ Line = 0

    if Options:
        $ Line = 0
        if Options[0] == RogueX:
            ch_r "Hey, [RogueX.player_petname]."
            if "showered" in RogueX.recent_history:
                ch_r "I was just getting ready to head out."
            if not approval_check(Options[0], 900):
                ch_r "See ya later."
        if Options[0]  == KittyX:
            ch_k "Hey, [KittyX.player_petname]."
            if "showered" in KittyX.recent_history:
                ch_k "I just got finished."
            if not approval_check(Options[0], 900):
                ch_k "Oh, um, I should get out of your way. . ."
        if Options[0]  == EmmaX:
            ch_e "Oh, hello, [EmmaX.player_petname]."
            if "showered" in EmmaX.recent_history:
                ch_e "I was about finished here."
            if not approval_check(Options[0], 900):
                ch_e "I should get going."
        if Options[0]  == LauraX:
            ch_l "Oh, hey."
            if "showered" in LauraX.recent_history:
                ch_l "I'm done here."
            if not approval_check(Options[0], 900):
                ch_l "See you later."
        if Options[0]  == JeanX:
            ch_j "Oh, hey. . . you."
            if "showered" in JeanX.recent_history:
                ch_j "I'm wrapping up here."
            if not approval_check(Options[0], 900):
                ch_j "Later."
        if Options[0]  == StormX:
            ch_s "Oh, hello, [StormX.player_petname]."
            if "showered" in StormX.recent_history:
                ch_s "I was finishing up here."
            if not approval_check(Options[0], 600):
                ch_s "I am heading out at the moment."
        if Options[0]  == JubesX:
            ch_v "Yo, [JubesX.player_petname]."
            if "showered" in JubesX.recent_history:
                ch_v "I just finished up here."
            if not approval_check(Options[0], 900):
                ch_v "I should, uh, get going. . ."
        if len(Options) >= 2:
            if Options[1] == RogueX:
                if not approval_check(Options[0], 900) and not approval_check(Options[1], 900):

                    ch_r "Yeah, I'll see you too."
                elif not approval_check(Options[1], 900):

                    ch_r "Yeah, I should get going though."
                else:

                    ch_r "Yeah, hey."
            if Options[1] == KittyX:
                if not approval_check(Options[0], 900) and not approval_check(Options[1], 900):
                    ch_k "Yeah, see ya."
                elif not approval_check(Options[1], 900):
                    ch_k "Oh, well. . . I should get going."
                else:
                    ch_k "Yeah, hi."
            if Options[1] == EmmaX:
                if not approval_check(Options[0], 900) and not approval_check(Options[1], 900):
                    ch_e "Yes, I should also get going."
                elif not approval_check(Options[1], 900):
                    ch_e "You two look like you have some business. . ."
                else:
                    ch_e "Yes, hello."
            if Options[1] == LauraX:
                if not approval_check(Options[0], 900) and not approval_check(Options[1], 900):
                    ch_l "Yeah, I'm heading out too."
                elif not approval_check(Options[1], 900):
                    ch_l "I'll get out of your way."
                else:
                    ch_l "Hey."
            if Options[1] == JeanX:
                if not approval_check(Options[0], 900) and not approval_check(Options[1], 900):
                    ch_j "Yeah, I'm done too."
                elif not approval_check(Options[1], 900):
                    ch_j "I'm headed out."
                else:
                    ch_j "Hey."
            if Options[1] == StormX:
                if not approval_check(Options[0], 900) and not approval_check(Options[1], 600):
                    ch_s "Yes, I am also leaving."
                elif not approval_check(Options[1], 900):
                    ch_s "I wouldn't want to be a bother. . ."
                else:
                    ch_s "Yes, hello."
            if Options[1] == JubesX:
                if not approval_check(Options[0], 900) and not approval_check(Options[1], 900):
                    ch_v "Yeah, see ya."
                elif not approval_check(Options[1], 900):
                    ch_v "Oh, so. . . I should head out."
                else:
                    ch_v "Yeah, hey."

            if not approval_check(Options[1], 900):
                call Remove_Girl (Options[1])
        if not approval_check(Options[0], 900):
            call Remove_Girl (Options[0])

        if Options:
            if RogueX in Party:
                ch_r "Hey, [Options[0].name]."
            if KittyX in Party:
                ch_k "Hi, [Options[0].name]."
            if EmmaX in Party:
                ch_e "Oh, hello, [Options[0].name]."
            if LauraX in Party:
                ch_l "Hey."
            if JeanX in Party:
                ch_j "Yeah, hey."
            if StormX in Party:
                ch_s "Hello, [Options[0].name]."
            if JubesX in Party:
                ch_v "Hey, [Options[0].name]."
    $ Line = 0

    $ Options = []




label Shower_Room:
    $ bg_current = "bg_showerroom"
    $ Player.drain_word("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Dress=0)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        if time_index == 3:
            "You're getting tired, you head back to your room."
            jump player_room
        call Wait
        call EventCalls
        call girls_location
    call GirlsAngry



    menu:
        "You're in the showers. What would you like to do?"
        "Chat":

            call Chat

        "Shower" if Round > 30:
            call Showering
        "Shower [[no time](locked)" if Round <= 30:
            pass












        "Wait." if time_index < 3:
            "You hang out for a bit."
            if Round > 30:
                "In the showers."
                "Not gonna lie, kinda weird."
            call Wait
            call EventCalls
            call girls_location


            if renpy.random.randint(1, 20) < 5:
                $ Nearby = []
                $ Line = active_Girls[:]
                while Line:

                    if Line[0].location != bg_current and "showered" not in Line[0].daily_history and (Line[0].location == Line[0].home or Line[0].location == "bg_dangerroom"):

                        $ Nearby.append(Line[0])
                    $ Line.remove(Line[0])
                $ Line = 0
                if Nearby:
                    $ renpy.random.shuffle(Nearby)
                    while len(Nearby) > 2:

                        $ Nearby.remove(Nearby[0])
                    if len(Nearby) > 1:
                        $ Nearby[1].location = "nearby"
                    $ Nearby[0].location = "nearby"
        "Wait. [[no time](locked)" if time_index >= 3:
            pass

        "Go to the Danger Room" if TravelMode:
            call No_Towels
            jump Danger_Room_Entry
        "Return to Your Room" if TravelMode:
            call No_Towels
            jump player_room_Entry
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call No_Towels
                    call girls_room_entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call No_Towels
                    call girls_room_entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call No_Towels
                    call girls_room_entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call No_Towels
                    call girls_room_entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call No_Towels
                    call girls_room_entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call No_Towels
                    call girls_room_entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call No_Towels
                    call girls_room_entry (JubesX)
                "Back":

                    pass
        "Leave" if not TravelMode:
            call QuickEvents
            call No_Towels
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            call QuickEvents
            call No_Towels
            jump Campus_Entry

    jump Shower_Room


label No_Towels:

    $ BO = all_Girls[:]
    while BO:

        if BO[0].location == "bg_showerroom":
            $ BO[0].add_word(1,"showered","showered")
        if "met" in BO[0].history and BO[0] not in Party:
            $ BO[0].location = BO[0].Schedule[Weekday][time_index]
        $ BO[0].change_outfit(BO[0].OutfitDay)
        $ BO.remove(BO[0])
    return





label Study_Room_entering:
    call Jubes_Entry_Check
    $ Player.drain_word("locked",0,0,1)
    $ Nearby = []
    $ bg_current = "bg_study"
    call Gym_Clothes_Off
    call Taboo_Level
    call set_the_scene (Entry=1)
    $ Round -= 5 if Round >= 5 else Round
    menu:
        "You're at the door, what do you do?"
        "Knock politely":
            $ Line = "knock"
        "Enter without knocking":

            if time_index >= 3:
                "The door is locked. It's not like you could just walk through it."
                jump Study_Room_Entry

        "Use the key to enter" if time_index >= 3 and "Xavier" in Keys:
            "You use your key."
            $ Line = 0

        "Ask [KittyX.name]" if time_index >= 3 and KittyX in Party:
            $ Line = "kitty"
        "Ask [StormX.name]" if time_index >= 3 and StormX in Party:
            $ Line = "storm"
        "Leave":

            "You head back."
            jump Campus_Map

    if Line == "knock":
        if time_index >= 3:
            "There's no answer, he's probably asleep."
            jump Study_Room_Entry
        else:
            ch_x "Yes, enter. . ."
            "You enter the room."
    elif Line == "kitty":
        ch_k "Yeah?"
        while True:
            menu:
                extend ""
                "Could you phase through the door and open it for me?":
                    if "Sneakthief" in KittyX.traits:
                        ch_k "No problem. . ."
                        jump Study_Room
                    elif "no_thief" in KittyX.recent_history:
                        ch_k "I told you, no."
                    elif approval_check(KittyX, 400, "I") or approval_check(KittyX, 1400):
                        $ KittyX.change_stat("love", 90, 3)
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_stat("inhibition", 60, 10)
                        ch_k "Heh, you have a wicked mind. . ."
                        $ KittyX.traits.append("Sneakthief")
                        jump Study_Room
                    else:
                        $ KittyX.change_stat("love", 90, -3)
                        $ KittyX.change_stat("obedience", 50, 2)
                        $ KittyX.change_stat("inhibition", 60, 2)
                        ch_k "Um, I don't really feel comfortable doing that. . ."
                        $ KittyX.recent_history.append("no_thief")
                "Open the door.":
                    if "Sneakthief" in KittyX.traits:
                        ch_k "No problem. . ."
                        jump Study_Room
                    elif "no_thief" in KittyX.recent_history:
                        ch_k "I told you, no."
                    elif approval_check(KittyX, 500, "O") or approval_check(KittyX, 1600):
                        $ KittyX.change_stat("obedience", 50, 15)
                        $ KittyX.change_stat("inhibition", 60, 10)
                        ch_k "Heh, if you say so. . ."
                        $ KittyX.traits.append("Sneakthief")
                        jump Study_Room
                    else:
                        $ KittyX.change_stat("love", 90, -5)
                        $ KittyX.change_stat("obedience", 50, 2)
                        $ KittyX.change_stat("inhibition", 60, 2)
                        ch_k "Um, no."
                        $ KittyX.recent_history.append("no_thief")
                "Never mind. [[Leave]":
                    "You head back."
                    jump Campus_Map
        jump Study_Room_Entry
    elif Line == "storm":
        ch_s "What is it?"
        while True:
            menu:
                extend ""
                "Do you think you could pick that lock?" if "Sneakthief" not in StormX.traits:
                    if "no_thief" in StormX.recent_history:
                        ch_s "I told you, I won't do that."
                    elif approval_check(StormX, 400, "I") or approval_check(StormX, 1400):
                        $ StormX.change_stat("love", 90, 3)
                        $ StormX.change_stat("obedience", 80, 10)
                        $ StormX.change_stat("inhibition", 60, 10)
                        $ StormX.change_face("_sly")
                        ch_s "Oh, this should be interesting. . ."
                        "She pulls some picks from behind her ear."
                        ch_s "Ok, we've got a click on 1. . . 2 is binding. . ."
                        ch_s "Click on 3. . . 4. . . click on 5, back to 2. . . and we're in."
                        $ StormX.traits.append("Sneakthief")
                        $ StormX.change_face("_normal")
                        jump Study_Room
                    else:
                        $ StormX.change_stat("love", 90, -3)
                        $ StormX.change_stat("obedience", 50, 2)
                        $ StormX.change_stat("inhibition", 60, 2)
                        ch_s "I don't think that's really appropriate behavior. . ."
                        $ StormX.recent_history.append("no_thief")
                "Could you pick the lock again?" if "Sneakthief" in StormX.traits:
                    ch_s "No problem. . ."
                    jump Study_Room
                "Never mind. [[Leave]":
                    "You head back."
                    jump Campus_Map
        jump Study_Room_Entry

    elif time_index < 3:
        ch_x "You know, [Player.name], it is not polite to enter a room unannounced."
    $ counter = 0

label Study_Room:
    $ bg_current = "bg_study"
    $ Player.drain_word("traveling",1,0)
    call Taboo_Level
    call set_the_scene (silent=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        if time_index >= 3:
            "It's late, you head back to your room."
            jump player_room
        else:
            call Wait
            call girls_location

    call GirlsAngry
    call change_Xavier_face ("_happy")


    if time_index >= 3:
        $ Line = "You are in Xavier's Study, but he isn't in at the moment. What would you like to do?"
    else:
        $ Line = "You are in Xavier's Study. What would you like to do?"
    menu:
        "[Line]"
        "Chat" if time_index >= 3:
            call Chat

        "Plan Omega!" if time_index < 3 and RogueX.location == bg_current and Player.level >= 5:
            if approval_check(RogueX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (RogueX)
            else:
                ch_r "I don't want to do that. . ."
        "Plan Kappa!" if time_index < 3 and KittyX.location == bg_current and Player.level >= 5:
            if "Xavier's photo" in Player.inventory and approval_check(KittyX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (KittyX)
            elif "Xavier's photo" in Player.inventory:
                ch_k "I don't really want to do that. . ."
            else:
                ch_k "What?"
        "Plan Psi!" if time_index < 3 and EmmaX.location == bg_current and Player.level >= 5:
            if approval_check(EmmaX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (EmmaX)
            else:
                ch_e "I'd rather not. . ."
        "Plan Chi!" if time_index < 3 and LauraX.location == bg_current and Player.level >= 5:
            if LauraX.level >= 2 and approval_check(LauraX, 1500, TabM=1, Loc="No") and approval_check(LauraX, 750, "I"):
                call Xavier_Plan (LauraX)
            elif LauraX.level < 2 or not approval_check(LauraX, 750, "I"):
                ch_l "I'm not ready for that."
            else:
                ch_l "Huh?"
        "Plan Alpha!" if time_index < 3 and JeanX.location == bg_current and Player.level >= 5:
            if approval_check(JeanX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (JeanX)
            else:
                ch_j "You're on your own there."
        "Plan Rho!" if time_index < 3 and StormX.location == bg_current and Player.level >= 5:
            if "Xavier's files" in Player.inventory and approval_check(StormX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (StormX)
            elif "Xavier's files" in Player.inventory:
                ch_s "I do not believe that would be approrpriate."
            else:
                ch_s "What is that?"
        "Plan Zeta!" if time_index < 3 and JubesX.location == bg_current and Player.level >= 5:
            if approval_check(JubesX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (JubesX)
            else:
                ch_v "What's a \"Zeta?\""
        "Explore" if time_index >= 3 and "explore" not in Player.recent_history:
            $ counter = 0
            $ Player.recent_history.append("explore")
            jump Study_Room_Explore
        "Wait":

            if time_index >= 3:
                "You probably don't want to be here when Xavier gets in."
            elif time_index >=2:
                ch_x "If you don't mind, I would like to close up for the evening?"
                "You return to your room."
                jump player_room
            else:
                call Wait
                call girls_location
                ch_x "Not that I mind the company, but is there something I can do for you?"

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry
        "Return to Your Room" if TravelMode:
            jump player_room_Entry

    jump Study_Room


label Study_Room_Explore:
    $ Line = 0
    $ D20 = renpy.random.randint(1, 20)
    menu:
        "Where would you like to look?"
        "Bookshelf":
            if D20 >= 5 + counter:
                $ Line = "book"
            else:
                "As you search the bookshelf, you accidentally knock one of the books off."
                "It hammers against the floor, and a little light blinks on the desk."
        "Left Desk Drawer":
            if KittyX.location != bg_current and StormX.location != bg_current:
                "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 10 + counter:
                $ Line = "left"
            else:
                "As you open the drawer, it makes a loud a squeak."
                "As you look around, you notice a little light starts blinking on the desk."
        "Middle Desk Drawer":
            if KittyX.location != bg_current and StormX.location != bg_current:
                "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 15 + counter:
                $ Line = "mid"
            else:
                "As you open the drawer, it makes a loud a squeak."
                "As you look around, you notice a little light starts blinking on the desk."
        "Right Desk Drawer":
            if KittyX.location != bg_current and StormX.location != bg_current:
                "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 5 + counter:
                $ Line = "right"
            else:
                "As you open the drawer, it makes a loud a squeak."
                "As you look around, you notice a little light starts blinking on the desk."
        "Never mind [[back]":
            jump Study_Room

    $ D20 = renpy.random.randint(1, 20)
    if not Line:
        "Probably best to get out of here."
        "You slip out and head back to your room."
        jump player_room_Entry
    elif Line == "book":
        if D20 >= 15 and "Well Studied" not in Achievements:
            "As you check the books on the shelf, you notice that one of them is actually a disguised lockbox."
            if KittyX.location == bg_current:
                menu:
                    "Since [KittyX.name] is around, have her check inside?"
                    "Check in the box":
                        if approval_check(KittyX, 700, "I") or approval_check(KittyX, 1800):
                            if "Well Studied" not in Achievements:
                                $ KittyX.change_stat("obedience", 50, 10)
                                $ KittyX.change_stat("inhibition", 60, 15)
                                ch_k "Sounds like a plan."
                                "[KittyX.name] swipes her hand through the box, and pulls out a stack of bills."
                                "Looks like Xavier was hiding a rainy day fund in here."
                                $ Player.cash += 500
                                "[[$500 acquired.]"
                                $ Achievements.append("Well Studied")
                            else:
                                "Looks like this has been thoroughly looted."
                        else:
                            $ KittyX.change_stat("love", 90, -3)
                            $ KittyX.change_stat("obedience", 50, 1)
                            $ KittyX.change_stat("inhibition", 60, 2)
                            ch_k "I really don't think we should do that."
                    "Put it back.":
                        "You place the box back on the shelf."
            elif StormX.location == bg_current:
                menu:
                    "Since [StormX.name] is around, have her check inside?"
                    "Check in the box":
                        if approval_check(StormX, 700, "I") or approval_check(StormX, 1800):
                            if "Well Studied" not in Achievements:
                                $ StormX.change_stat("obedience", 50, 10)
                                $ StormX.change_stat("inhibition", 60, 15)
                                ch_s "I suppose I could. . ."
                                "[StormX.name] picks the lock on the box, and pulls out a stack of bills."
                                "Looks like Charles had some money set aside. . ."
                                $ Player.cash += 500
                                "[[$500 acquired.]"
                                $ Achievements.append("Well Studied")
                            else:
                                "Looks like this has been thoroughly looted."
                        else:
                            $ StormX.change_stat("love", 90, -3)
                            $ StormX.change_stat("obedience", 50, 1)
                            $ StormX.change_stat("inhibition", 60, 2)
                            ch_s "I really don't think we should do that."
                    "Put it back.":
                        "You place the box back on the shelf."
            else:
                "You can't think of any way to get it open, too bad you aren't a ghost or something."
                "You place the box back on the shelf."
        elif D20 >= 15:
            "There doesn't seem to be anything more of interest in here."
        else:
            "You search through the books for a few minutes, but don't find anything."
            "It would probably take a more thorough search."
    elif Line == "left":
        if "Xavier's photo" not in Player.inventory:
            if D20 >= 10:
                "Buried under a pile of documents, you find a printed out photo."
                "It appears to be a selfie of Mystique making out with Xavier."
                "She's reaching down to adjust his . . . oh, {i}that's{/i} interesting."
                if StormX.location == bg_current:
                    ch_s "You should probably put that back, it looks personal."
                else:
                    "[[Xavier's photo acquired.]"
                    $ Player.inventory.append("Xavier's photo")
                    if "kappa" in Player.history:
                        $ Player.history.remove("kappa")
            else:
                "You search through some documents, but don't find anything."
                "It would probably take a more thorough search."
        else:
            "There doesn't seem to be anything more of interest in here."
    elif Line == "mid":
        if "All" not in Keys:
            "Under a few trinkets, you find a small keyring."
            "[[Keyring acquired.]"
            if "Xavier" not in Keys:
                $ Keys.append("Xavier")
            if RogueX not in Keys:
                $ Keys.append(RogueX)
            if KittyX not in Keys:
                $ Keys.append(KittyX)
            if EmmaX not in Keys:
                $ Keys.append(EmmaX)
            if LauraX not in Keys:
                $ Keys.append(LauraX)
            if JeanX not in Keys:
                $ Keys.append(JeanX)
            if StormX not in Keys:
                $ Keys.append(StormX)
            if JubesX not in Keys:
                $ Keys.append(JubesX)
            if "All" not in Keys:
                $ Keys.append("All")
        else:
            "There doesn't seem to be anything interesting in here."
    elif Line == "right":
        "There doesn't seem to be anything more of interest in here, maybe later?"
        if "Xavier's files" not in Player.inventory:
            if D20 >= 10:
                "You search through some documents, but don't find anything."
                if StormX.location == bg_current:
                    ch_s "Hmm. . ."
                    "She reaches under some of the documents and finds a small notch."
                    "With a soft \"click\"a panel flips open in the drawer, revealing some file folders."
                    "Inside are some fairly. . . detailed reports on the girls at the school."
                    $ StormX.change_face("_surprised",2)
                    "These include body measurements, sexual histories. . . masturbation habits?"
                    $ StormX.change_stat("obedience", 70, 5)
                    $ StormX.change_stat("inhibition", 70, 5)
                    $ StormX.change_face("_angry")
                    ch_s "Well, I don't think Charles should be holding information like this. . ."
                    $ StormX.change_face("_normal",1)
                    "[[Xavier's files acquired.]"
                    $ Player.inventory.append("Xavier's files")
                    if "rho" in Player.history:
                        $ Player.history.remove("rho")
            else:
                "You search through some documents, but don't find anything."
                "It would probably take a more thorough search."
        else:
            "There doesn't seem to be anything more of interest in here."

    $ counter += 3
    jump Study_Room_Explore
