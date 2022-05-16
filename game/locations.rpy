

label Worldmap:
    scene bg_campus onlayer backdrop
    scene
    $ Taboo = 0
    menu:
        "Where would you like to go?"
        "My Room":
            $ renpy.pop_call()
            jump Player_Room_Entry
        "Girl's Rooms":
            menu:
                "[RogueX.name]'s Room":
                    call Girls_Room_Entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call Girls_Room_Entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call Girls_Room_Entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call Girls_Room_Entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call Girls_Room_Entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call Girls_Room_Entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call Girls_Room_Entry (JubesX)
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

        call expression primary_action.Tag + "_SexMenu"


    scene onlayer black
    $ Player.DrainWord("locked",0,0,1)
    $ StackDepth = renpy.call_stack_depth()
    while StackDepth > 0:
        $ StackDepth -= 1
        $ renpy.pop_call()
    if bg_current == "bg_player":
        jump Player_Room
    if bg_current == "bg_rogue":
        jump Rogue_Room
    if bg_current == "bg_kitty":
        jump Kitty_Room
    if bg_current == "bg_emma":
        jump Emma_Room
    if bg_current == "bg_laura":
        jump Laura_Room
    if bg_current == "bg_jean":
        jump Jean_Room
    if bg_current == "bg_storm":
        jump Storm_Room
    if bg_current == "bg_jubes":
        jump Jubes_Room
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




label Player_Room_Entry:

    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg_player"
    call Gym_Clothes_Off
    $ Player.recent_history.append("traveling")
    $ Nearby = []
    $ Round -= 5 if Round >= 5 else Round
    call EventCalls
    call set_the_scene
    jump Clear_Stack

label Player_Room:
    $ bg_current = "bg_player"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls
    call GirlsAngry


    menu:
        "You are in your room. What would you like to do?"
        "Chat":
            call Chat
        "Study":

            call Study_Session

        "Lock the door" if "locked" not in Player.Traits:
            "You lock the door"
            $ Player.Traits.append("locked")
            call Taboo_Level

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level


        "Sleep." if time_index >= 3:
            call Round10
            call Girls_Location
            call EventCalls
        "Wait." if time_index < 3:
            "You wait around a bit."
            call Round10
            call Girls_Location
            call EventCalls
        "Shop":

            call Shop
        "Special Options":
            call SpecialMenu


        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call Girls_Room_Entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call Girls_Room_Entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call Girls_Room_Entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call Girls_Room_Entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call Girls_Room_Entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call Girls_Room_Entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call Girls_Room_Entry (JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry
        "Attic" if TravelMode and "attic" in Player.history:
            jump StormMeet

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    jump Player_Room






label Campus_Map:
    $ Line = 0
    $ primary_action = 0
    $ offhand_action = 0
    $ girl_offhand_action = 0
    $ second_girl_primary_action = 0
    $ second_girl_offhand_action = 0
    $ bg_current = "bg_campus"
    $ Player.DrainWord("locked",0,0,1)
    call set_the_scene
    if not TravelMode:
        call Worldmap
    jump Campus

label Campus_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg_campus"
    $ Nearby = []
    call Gym_Clothes_Off
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    call EventCalls
    call set_the_scene

label Campus:
    $ bg_current = "bg_campus"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
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
            jump Player_Room
        call Wait
        call EventCalls
        call Girls_Location



    menu:
        "You are in the university square. What would you like to do?"
        "Chat":

            call Chat

        "Wait." if time_index < 3:
            "You wait around a bit."
            call Wait
            call EventCalls
            call Girls_Location

        "Go to my Room" if TravelMode:
            jump Player_Room_Entry
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call Girls_Room_Entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call Girls_Room_Entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call Girls_Room_Entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call Girls_Room_Entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call Girls_Room_Entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call Girls_Room_Entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call Girls_Room_Entry (JubesX)
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






label Class_Room_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
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
        $ Player.DrainWord("goto",1,0)
        $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."
            jump Player_Room
        call Wait
        call EventCalls
        call Girls_Location
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

        "Lock the door" if "locked" not in Player.Traits:
            if Weekday >=5 or time_index >= 2:
                "You lock the door"
                $ Player.Traits.append("locked")
                call Taboo_Level
            else:
                "You can't really do that during class."

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level

        "Wait" if time_index < 3:
            "You hang out for a bit."
            call Wait
            call EventCalls
            call Girls_Location

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
    call Girls_Location
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
    call set_the_scene (Quiet=1)

    return






label Danger_Room_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
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
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        "Looks like shifts are changing. . ."
        if time_index >=3:
            "You're getting tired, you head back to your room."
            jump Player_Room
        call Wait
        call EventCalls
        call Girls_Location
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


        "Lock the door" if "locked" not in Player.Traits:
            if time_index >= 3:
                "You lock the door"
                $ Player.Traits.append("locked")
                call Taboo_Level
            else:
                "You can't really do that during free hours."

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level

        "Wait. (locked)" if time_index >= 3:
            pass
        "Wait." if time_index < 3:
            "You hang out for a bit."
            call Wait
            call EventCalls
            call Girls_Location
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
    call Girls_Location
    call set_the_scene
    $ Line = "The training session has ended, what would you like to do next?"

    jump Danger_Room

label Rogue_TightsRipped(Count=0):
    if RogueX.hose == "tights":
        $ Count = 1
        $ RogueX.hose = "ripped_tights"
        $ RogueX.change_face("angry")
        if "ripped_tights" in RogueX.Inventory:
            ch_r "Damnation, that's another pair ruined!"
        else:
            $ Count = 2
            ch_r "Well that's a good pair of tights down the chute."
    elif RogueX.hose == "pantyhose":
        $ Count = 1
        $ RogueX.hose = "ripped_pantyhose"
        $ RogueX.change_face("angry")
        if "ripped_pantyhose" in RogueX.Inventory:
            ch_r "Tsk, another pair ruined!"
        else:
            $ Count = 2
            ch_r "I hate getting a run in these things."
    if Count:

        if not RogueX.legs and RogueX.underwear != "shorts":
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
                    $ RogueX.change_face("smile", 1)
                    $ RogueX.Inventory.append(RogueX.hose)
                    ch_r "You think so? That's sweet, maybe I'll keep them on hand."
                "Yeah, too bad.":
                    $ RogueX.change_face("bemused")
                    ch_r ". . ."
                "Ha! Those don't leave much to the imagination!":
                    ch_r "Thanks for that. . ."

        elif Count == 3:
            $ RogueX.change_face("startled", 2)
            ch_r "I, um, I should get out of here."
            $ RogueX.blushing = 1
            call Remove_Girl (RogueX)
            $ RogueX.change_outfit()

    return






label Pool_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
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
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1, Dress=0)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."
            jump Player_Room
        call Wait
        call EventCalls
        call Girls_Location
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
            call Girls_Location

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
            $ BO[0].AddWord(0,"swim","swim",0,0)
            $ BO[0].Water = 1
            $ BO[0].Spunk = []
            $ PoolLoc = 500 if len(BO) > 1 else 650
            if BO[0] == RogueX:
                show Rogue_Sprite zorder 50 at Pool_Bob(PoolLoc)
            elif BO[0] == KittyX:
                show Kitty_Sprite zorder 50 at Pool_Bob(PoolLoc)
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


label Shower_Room_Entry:
    call Jubes_Entry_Check
    $ bg_current = "bg_showerroom"
    $ Player.DrainWord("locked",0,0,1)
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
            $ Options[0].AddWord(1,"showered","showered",0,0)
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
                $ Line[0].AddWord(1,"showered","showered",0,0)
            $ Line[0].change_outfit("towel")
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
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Dress=0)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        if time_index == 3:
            "You're getting tired, you head back to your room."
            jump Player_Room
        call Wait
        call EventCalls
        call Girls_Location
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
            call Girls_Location


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
            jump Player_Room_Entry
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call No_Towels
                    call Girls_Room_Entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call No_Towels
                    call Girls_Room_Entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call No_Towels
                    call Girls_Room_Entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call No_Towels
                    call Girls_Room_Entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call No_Towels
                    call Girls_Room_Entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call No_Towels
                    call Girls_Room_Entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call No_Towels
                    call Girls_Room_Entry (JubesX)
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
            $ BO[0].AddWord(1,"showered","showered")
        if "met" in BO[0].history and BO[0] not in Party:
            $ BO[0].location = BO[0].Schedule[Weekday][time_index]
        $ BO[0].change_outfit(BO[0].OutfitDay)
        $ BO.remove(BO[0])
    return

label Showering(Occupants=[], StayCount=[] , Showered=0, Line=0, BO=[]):


    $ BO = all_Girls[:]
    while BO:

        if BO[0] not in active_Girls:
            $ BO[0].location = "hold"
        if BO[0].location == "bg_showerroom" and BO[0] not in Occupants:
            $ Occupants.append(BO[0])
        $ BO.remove(BO[0])
    if Occupants:
        ch_p "I'm taking a shower, care to join me?"
        if Occupants[0] == RogueX and "showered" in RogueX.recent_history:
            if len(Occupants) > 1:

                ch_r "We actually just finished up, so we'll head out."
            else:
                ch_r "I actually just finished up, so I'll head out."
            $ Showered = 1
        elif Occupants[0] == KittyX and "showered" in KittyX.recent_history:
            if len(Occupants) > 1:

                ch_k "We actually just showered, so we're heading out."
            else:
                ch_k "I actually just showered, so I'm heading out."
            $ Showered = 1
        elif Occupants[0] == EmmaX and "showered" in EmmaX.recent_history:
            if len(Occupants) > 1:

                ch_e "We were actually finishing up, so we're heading out."
            else:
                ch_e "I was actually finishing up, so I'm heading out."
            $ Showered = 1
        elif Occupants[0] == LauraX and "showered" in LauraX.recent_history:
            if len(Occupants) > 1:

                ch_l "We were done, actually."
            else:
                ch_l "I'm heading out now."
            $ Showered = 1
        elif Occupants[0] == JeanX and "showered" in JeanX.recent_history:
            if len(Occupants) > 1:

                ch_j "We were done."
            else:
                ch_j "I'm heading out."
            $ Showered = 1
        elif Occupants[0] == StormX and "showered" in StormX.recent_history:
            if len(Occupants) > 1:

                ch_s "I think we're about finished and heading out now."
            else:
                ch_s "I was about finished and heading out now."
            $ Showered = 1
        elif Occupants[0] == JubesX and "showered" in JubesX.recent_history:
            if len(Occupants) > 1:

                ch_v "We finished getting showered, so we're taking off."
            else:
                ch_v "I finished getting showered, so I'm taking off."
            $ Showered = 1
        else:

            if Occupants[0] == RogueX:
                if approval_check(RogueX, 1200) or (approval_check(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy):

                    ch_r "I suppose I could stick around. . ."
                    $ StayCount.append(RogueX)
                else:

                    ch_r "Nah, I should probably get going."
            elif Occupants[0] == KittyX:
                if approval_check(KittyX, 1400) or (approval_check(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy):
                    ch_k "Yeah, I could stick around."
                    $ StayCount.append(KittyX)
                else:
                    ch_k "I've got to get going."
            elif Occupants[0] == EmmaX:
                if not "classcaught" in EmmaX.history or "three" not in EmmaX.history:
                    ch_e "I really should be going. . ."
                elif approval_check(EmmaX, 1400) or (approval_check(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy):
                    ch_e "I suppose I could stay, for a bit."
                    $ StayCount.append(EmmaX)
                else:
                    ch_e "I'm afraid I really must be going."
            elif Occupants[0] == LauraX:
                if approval_check(LauraX, 1400) or (approval_check(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy):
                    ch_l "I got nothing better to do."
                    $ StayCount.append(LauraX)
                else:
                    ch_l "I gotta get going."
            elif Occupants[0] == JeanX:
                if approval_check(JeanX, 1400) or (approval_check(JeanX, 700) and JeanX.SeenChest and JeanX.SeenPussy):
                    ch_j "Sure, why not."
                    $ StayCount.append(JeanX)
                else:
                    ch_j "Nah, lol."
            elif Occupants[0] == StormX:
                if approval_check(StormX, 700):
                    ch_s "I could stay, I suppose."
                    $ StayCount.append(StormX)
                else:
                    ch_s "I really do have things to do, [StormX.player_petname]."
            elif Occupants[0] == JubesX:
                if approval_check(JubesX, 1400) or (approval_check(JubesX, 700) and JubesX.SeenChest and JubesX.SeenPussy):
                    ch_v "I guess I could stay a minute. . ."
                    $ StayCount.append(JubesX)
                else:
                    ch_v "I'm kinda busy, [JubesX.player_petname]."


            if len(Occupants) >= 2:

                if Occupants[1] == RogueX:
                    if approval_check(RogueX, 1200) or (approval_check(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy):
                        if StayCount:

                            ch_r "I could stick around too. . ."
                        else:

                            ch_r "Well, I could probably stay."
                        $ StayCount.append(RogueX)
                    else:
                        if StayCount:

                            ch_r "I can't though . ."
                        else:

                            ch_r "I should get going too."

                elif Occupants[1] == KittyX:
                    if approval_check(KittyX, 1400) or (approval_check(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy):
                        if StayCount:

                            ch_k "I guess I could stay too. . ."
                        else:

                            ch_k "Well, I could stay though."
                        $ StayCount.append(KittyX)
                    else:
                        if StayCount:

                            ch_k "I've really got to go though. . ."
                        else:

                            ch_k "Yeah, I should head out too."

                elif Occupants[1] == EmmaX:
                    if not "classcaught" in EmmaX.history or "three" not in EmmaX.history:
                        ch_e "I really should be going. . ."
                    elif approval_check(EmmaX, 1400) or (approval_check(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy):
                        if StayCount:

                            ch_e "I suppose I could also stay. . ."
                        else:

                            ch_e "But {i}I{/i} could stick around. . ."
                        $ StayCount.append(EmmaX)
                    else:
                        if StayCount:

                            ch_e "But I really must be going. . ."
                        else:

                            ch_e "Yes, let's go."

                elif Occupants[1] == LauraX:
                    if approval_check(LauraX, 1400) or (approval_check(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy):
                        if StayCount:

                            ch_l "I could stay too. . ."
                        else:

                            ch_l "I could stick around."
                        $ StayCount.append(LauraX)
                    else:
                        if StayCount:

                            ch_l "I gotta get going though. . ."
                        else:

                            ch_l "Yeah, me too."

                elif Occupants[1] == JeanX:
                    if approval_check(JeanX, 1000) or (approval_check(JeanX, 600) and JeanX.SeenChest and JeanX.SeenPussy):
                        if StayCount:

                            ch_j "I guess I could stay too. . ."
                        else:

                            ch_j "I could stick around."
                        $ StayCount.append(JeanX)
                    else:
                        if StayCount:

                            ch_j "I'm heading out though. . ."
                        else:

                            ch_j "Yeah."

                elif Occupants[1] == StormX:
                    if approval_check(StormX, 700):
                        if StayCount:

                            ch_s "I could also stay. . ."
                        else:

                            ch_s "I could stay for a moment though. . ."
                        $ StayCount.append(StormX)
                    else:
                        if StayCount:

                            ch_s "Well I'm afraid I must be going. . ."
                        else:

                            ch_s "Yes, let's."

                elif Occupants[1] == JubesX:
                    if approval_check(JubesX, 1400) or (approval_check(JubesX, 700) and JubesX.SeenChest and JubesX.SeenPussy):
                        if StayCount:

                            ch_k "I could kinda stay too. . ."
                        else:

                            ch_k "Well, -I'm- not that busy. . ."
                        $ StayCount.append(JubesX)
                    else:
                        if StayCount:

                            ch_k "I'm really busy right now though. . ."
                        else:

                            ch_k "Oh, yeah, I gotta go too. . ."


        if len(Occupants) > len(StayCount):

            menu:
                extend ""
                "Ok, see you later then.":
                    if RogueX.location == bg_current and RogueX not in StayCount:
                        ch_r "Yeah, later."
                    if KittyX.location == bg_current and KittyX not in StayCount:
                        ch_k "Bye!"
                    if EmmaX.location == bg_current and EmmaX not in StayCount:
                        ch_e "Yes, later."
                    if LauraX.location == bg_current and LauraX not in StayCount:
                        ch_l "Yup."
                    if JeanX.location == bg_current and JeanX not in StayCount:
                        ch_j "Ok."
                    if StormX.location == bg_current and StormX not in StayCount:
                        ch_s "Yes, I'll see you."
                    if JubesX.location == bg_current and JubesX not in StayCount:
                        ch_v "Laters!"

                "Sure you got every spot?" if Showered:
                    $ Line = "spot"
                "Maybe you could stay and watch?":



                    $ Line = "watch me"

                "But I didn't get to watch." if Showered:
                    $ Line = "watch you"
            if Line:
                $ BO = Occupants[:]
                while BO:

                    if BO[0].location == bg_current and BO[0] not in StayCount:
                        if BO[0] == EmmaX and (not "classcaught" in EmmaX.history or (StayCount and "three" not in EmmaX.history)):

                            pass
                        elif BO[0] == JeanX and approval_check(BO[0], 600):
                            $ StayCount.append(BO[0])
                        elif BO[0] == StormX:
                            if approval_check(BO[0], 700, "LO"):
                                $ StayCount.append(BO[0])
                        elif approval_check(BO[0], 1200,Alt=[[KittyX],1400]) or (approval_check(BO[0], 600,Alt=[[KittyX],700]) and BO[0].SeenChest and BO[0].SeenPussy):
                            $ StayCount.append(BO[0])
                        elif Line == "spot" and approval_check(BO[0], 1000, "LI",Alt=[[KittyX],1200]):
                            $ StayCount.append(BO[0])
                        elif Line == "watch you" and approval_check(BO[0], 600, "O",Alt=[[EmmaX],500]):
                            $ StayCount.append(BO[0])

                    $ BO.remove(BO[0])

                if Line == "spot":

                    if StayCount:

                        if StayCount[0] == RogueX:

                            ch_r "Fine, I could use another scrub."
                        elif StayCount[0] == KittyX:

                            ch_k "Oh, I guess I could take another pass at it."
                        elif StayCount[0] == EmmaX:

                            ch_e "I suppose we could take a look. . ."
                        elif StayCount[0] == LauraX:

                            ch_l "Well, maybe. . ."
                        elif StayCount[0] == JeanX:

                            ch_j "Well. . ."
                        elif StayCount[0] == StormX:

                            ch_s "Well, another pass couldn't hurt. . ."
                        elif StayCount[0] == JubesX:

                            ch_v "I mean, you can never be -too- clean. . ."
                    if RogueX.location == bg_current and RogueX not in StayCount:

                        if StayCount:
                            ch_r "Well, [RogueX.player_petname], I think I'm fine."
                        else:
                            ch_r "No, [RogueX.player_petname], I think I'm covered."
                    if KittyX.location == bg_current and KittyX not in StayCount:

                        if StayCount:
                            ch_k "Oh, well I think I[KittyX.like]got it?"
                            ch_k "See you later, [KittyX.player_petname]."
                        else:
                            ch_k "Ha, I'm squeaky clean, [KittyX.player_petname], see you later."
                    if EmmaX.location == bg_current and EmmaX not in StayCount:

                        if StayCount:
                            ch_e "Well it appears you'll be taken care of."
                            ch_e "I'll be going, [EmmaX.player_petname]."
                        else:
                            ch_e "I'm afraid not, [EmmaX.player_petname], I'll be going."
                    if LauraX.location == bg_current and LauraX not in StayCount:

                        if StayCount:
                            ch_l "Looks like you got this handled."
                            ch_l "I'm out, [LauraX.player_petname]."
                        else:
                            ch_l "I'm out."
                    if JeanX.location == bg_current and JeanX not in StayCount:

                        if StayCount:
                            ch_j "Well, looks like you guys are going to have fun."
                            ch_j "I'll head out, [JeanX.player_petname]."
                        else:
                            ch_j "I'll head out."
                    if StormX.location == bg_current and StormX not in StayCount:

                        if StayCount:
                            ch_s "It looks like you'll be occupied."
                            ch_s "I'll be going, [StormX.player_petname]."
                        else:
                            ch_s "I really doubt that I could have, [StormX.player_petname], I'll be going."
                    if JubesX.location == bg_current and JubesX not in StayCount:

                        if StayCount:
                            ch_v "Nah, I think you'll be fine."
                            ch_v "Later, guys."
                        else:
                            ch_v "Nah, I'm good. Later, [JubesX.player_petname]."


                elif Line == "watch me":

                    if StayCount:
                        if StayCount[0] == RogueX:

                            ch_r "Yeah, I guess I do enjoy the view."
                        elif StayCount[0] == KittyX:

                            ch_k "I. . . guess I wouldn't mind that. . ."
                        elif StayCount[0] == LauraX:

                            ch_l "Ok, let's see what you got."
                        elif StayCount[0] == JeanX:

                            ch_j "Ohh, this should be good. . ."
                        elif StayCount[0] == StormX:

                            ch_s "I suppose that I could. . ."
                        elif StayCount[0] == JubesX:

                            ch_v ". . . Yeah, ok."

                    if RogueX.location == bg_current and RogueX not in StayCount:

                        if StayCount:
                            ch_r "Oh, well, I'm gonna pass on that, [RogueX.player_petname]."
                        else:
                            ch_r "Yeah, I'm gonna pass on that, [RogueX.player_petname]."
                    if KittyX.location == bg_current and KittyX not in StayCount:

                        if StayCount:
                            ch_k "Well, [KittyX.like]I don't need to see that."
                            ch_k "See you later, [KittyX.player_petname]."
                        else:
                            ch_k "[KittyX.Like]I don't need to see that."
                    if EmmaX.location == bg_current and EmmaX not in StayCount:

                        if StayCount:
                            ch_e "You appear to have enough of an audience."
                            ch_e "I'll be going, [EmmaX.player_petname]."
                        else:
                            ch_e "I think I'll be fine, [EmmaX.player_petname], I'll be going."
                    if LauraX.location == bg_current and LauraX not in StayCount:

                        if StayCount:
                            ch_l "She's got you covered."
                            ch_l "I'm out, [LauraX.player_petname]."
                        else:
                            ch_l "I'm out."
                    if JeanX.location == bg_current and JeanX not in StayCount:

                        if StayCount:
                            ch_j "Well, looks like you guys are going to have fun."
                            ch_j "I'll head out, [JeanX.player_petname]."
                        else:
                            ch_j "I'll head out."
                    if StormX.location == bg_current and StormX not in StayCount:

                        if StayCount:
                            ch_s "Oh, I think someone else wants the show."
                            ch_s "I'll be going, [StormX.player_petname]."
                        else:
                            ch_s "I don't see why I would, [StormX.player_petname]. I'll be going."
                    if JubesX.location == bg_current and JubesX not in StayCount:

                        if StayCount:
                            ch_v "Um, no thanks. . ."
                            ch_v "See you later, [JubesX.player_petname]."
                        else:
                            ch_v "Um, no thanks."


                elif Line == "watch you":

                    if StayCount:
                        if StayCount[0] == RogueX:

                            ch_r "Well, I don't mind putting on a show."
                        elif StayCount[0] == KittyX:

                            ch_k "You want to watch me. . ."
                            ch_k "Ok."
                        elif StayCount[0] == EmmaX:

                            ch_e "I suppose I can't blame you for that. . ."
                        elif StayCount[0] == LauraX:

                            ch_l "Huh. Suit yourself."
                        elif StayCount[0] == JeanX:

                            ch_j "Well, we can't have that. . ."
                        elif StayCount[0] == StormX:

                            ch_s ". . ."
                        elif StayCount[0] == JubesX:

                            ch_v "Well. . . I guess we should make up for that. . ."

                    if RogueX.location == bg_current and RogueX not in StayCount:

                        if StayCount:
                            ch_r "Really? Well not me."
                            ch_r "Have fun, [RogueX.player_petname]."
                        else:
                            ch_r "Keep dreaming, [RogueX.player_petname]."
                    if KittyX.location == bg_current and KittyX not in StayCount:

                        if StayCount:
                            ch_k "Seriously?! Well I'm not into that."
                            ch_k "Later, [KittyX.player_petname]."
                        else:
                            ch_k "[KittyX.Like]no way!"
                    if EmmaX.location == bg_current and EmmaX not in StayCount:

                        if StayCount:
                            ch_e "I wouldn't want to intrude."
                            ch_e "I'll be going."
                        else:
                            ch_e "Hmm, I doubt you could handle it."
                            ch_e "I'll be going."
                    if LauraX.location == bg_current and LauraX not in StayCount:

                        if StayCount:
                            ch_l "She's got you covered."
                            ch_l "I'm out, [LauraX.player_petname]."
                        else:
                            ch_l "I'm out."
                    if JeanX.location == bg_current and JeanX not in StayCount:

                        if StayCount:
                            ch_j "Well, looks like you guys are going to have fun."
                            ch_j "I'll head out, [JeanX.player_petname]."
                        else:
                            ch_j "I'll head out."
                    if StormX.location == bg_current and StormX not in StayCount:

                        if StayCount:
                            ch_s "Well, you two enjoy yourselves."
                            ch_s "I'll be going."
                        else:
                            ch_s "I'm flattered, but no."
                            ch_s "I'll be going."
                    if JubesX.location == bg_current and JubesX not in StayCount:

                        if StayCount:
                            ch_v "Ok, looks like you two can have fun with that."
                            ch_v "Later, [JubesX.player_petname]."
                        else:
                            ch_v "Yeah, no way."


            if len(StayCount) > 1:

                if StayCount[1].GirlLikeCheck(StayCount[0]) > 500:

                    if StayCount[1] == RogueX:
                        ch_r "I guess I could too."
                    elif StayCount[1] == EmmaX:
                        ch_e "I suppose I don't want to be left out of this. . ."
                    elif StayCount[1] == JeanX:
                        ch_j "Well, it does look like fun. . ."
                else:
                    if StayCount[1] == RogueX:
                        ch_r "Well I guess if she's in, I am too!"
                    elif StayCount[1] == EmmaX:
                        ch_e "I wouldn't want to leave you alone with. . . this."
                    elif StayCount[1] == JeanX:
                        ch_j "Hmm, maybe I should stick around. . ."
                if StayCount[1] == KittyX:
                    ch_k "I- yeah, me neither!"
                elif StayCount[1] == LauraX:
                    ch_l "Fine."
                elif StayCount[1] == StormX:
                    ch_s "Well I suppose I should join you. . ."
                elif StayCount[1] == JubesX:
                    ch_v "Um, yeah, let's do this."

        $ BO = Occupants[:]
        while BO:

            if BO[0].location == bg_current:
                if BO[0] in StayCount:

                    $ BO[0].change_outfit("nude")
                    $ BO[0].Water = 1
                    $ BO[0].Spunk = []
                    $ BO[0].recent_history.append("showered")
                    $ BO[0].daily_history.append("showered")
                    call expression BO[0].Tag + "_First_Bottomless" pass (1)
                    call expression BO[0].Tag + "_First_Topless" pass (1)
                else:

                    call Remove_Girl (BO[0])
                while BO[0] in Nearby:
                    $ Nearby.remove(BO[0])
            $ BO.remove(BO[0])





    call Seen_First_Peen (0, 0, 0, 1)

    while len(StayCount) >= 2 and StayCount[1] in Nearby:

        $ Nearby.remove(StayCount[1])
    while StayCount and StayCount[0] in Nearby:

        $ Nearby.remove(StayCount[0])

    if Nearby and len(StayCount) < 2:

        $ renpy.random.shuffle(Nearby)

        while Nearby and (len(Nearby) + len(StayCount)) > 2:

            $ Nearby.remove(Nearby[0])

        if len(Nearby) >= 2:
            "As you finish getting undressed, [Nearby[0].name] and [Nearby[1].name] enter the room."
            $ Nearby[1].location = bg_current
        else:
            "As you finish getting undressed, [Nearby[0].name] enters the room."
        $ Nearby[0].location = bg_current

        $ BO = Nearby[:]


        call set_the_scene (Dress=0)

        call Seen_First_Peen (0, 0, 1, 1)

        if RogueX in BO:
            if RogueX.SeenPeen == 1:
                $ RogueX.change_face("surprised",2,Eyes="down")
                ch_r "Oh!"
                $ RogueX.change_face("bemused",1,Eyes="side")
                ch_r "I am so sorry, I should {i}not{/i} have just barged in like that."
            else:
                $ RogueX.change_face("bemused",1,Eyes="side")
                ch_r "I simply {i}must{/i} be more careful. . ."
        if KittyX in BO:
            $ KittyX.change_face("bemused",2,Eyes="side")
            if KittyX.SeenPeen == 1:
                ch_k "Sorry! Sorry! I need to stop just casually phasing into places!"
            else:
                ch_k "I have {i}got{/i} to knock more. . ."
        if EmmaX in BO:
            if EmmaX.SeenPeen == 1:
                $ EmmaX.change_face("surprised")
                ch_e "Oh! Dreadfully sorry."
                $ EmmaX.change_face("sexy",Eyes="down")
                ch_e "I hope we can meet again under. . . different circumstances."
            else:
                $ EmmaX.change_face("sexy",Eyes="down")
                ch_e "I really should pay closer attention. . ."
            if "classcaught" not in EmmaX.history or ((StayCount or len(Nearby) >= 2) and "three" not in EmmaX.history):

                "[EmmaX.name] decides to leave immediately."
                call Remove_Girl (EmmaX)
                $ BO.remove(EmmaX)
                $ EmmaX.change_outfit()
        if LauraX in BO:
            if LauraX.SeenPeen == 1:
                $ LauraX.change_face("surprised",Eyes="down")
                ch_l "Hey. That's interesting. . ."
            else:
                $ LauraX.change_face("normal",Eyes="down")
                ch_l ". . ."
                $ LauraX.change_face("normal")
                ch_l "I'm supposed to knock, aren't I."
        if JeanX in BO:
            if JeanX.SeenPeen == 1:
                $ JeanX.change_face("surprised",Eyes="down")
                ch_j "Well what do we have here? . ."
            else:
                $ JeanX.change_face("normal",Eyes="down")
                ch_j ". . ."
                $ JeanX.change_face("normal")
                ch_j "Oh, nice to catch you. . . like this. . ."
        if StormX in BO:
            if StormX.SeenPeen == 1:
                $ StormX.change_face("surprised")
                ch_s "Oh! Hello there."
                $ StormX.change_face("sexy",Eyes="down")
                ch_s "And hello to you as well. . ."
            else:
                $ StormX.change_face("sexy",Eyes="down")
                ch_s "I'm sorry to intrude. . ."
            $ StormX.change_face("sexy")
        if JubesX in BO:
            $ JubesX.change_face("bemused",2,Eyes="side")
            if JubesX.SeenPeen == 1:
                ch_v "Oh, sorry! I wasn't paying attention."
                $ JubesX.eyes = "down"
                pause 1
                $ JubesX.eyes = "side"
                ch_v "um. . . hey. . ."
            else:
                ch_v "Oh, sorry! I wasn't paying attention."

        if EmmaX in StayCount and "three" not in EmmaX.history:

            if len(BO) >= 2:
                "Seeing the other girls arrive, [EmmaX.name] quickly excuses herself."
            else:
                "Seeing [BO[0].name] arrive, [EmmaX.name] quickly excuses herself."
            $ StayCount.remove(EmmaX)
            call Remove_Girl (EmmaX)
            $ EmmaX.change_outfit()

        if BO:

            if approval_check(BO[0], 1200):
                $ StayCount.append(BO[0])
            if len(BO) >=2 and approval_check(BO[1], 1200) and len(StayCount) < 2:
                $ StayCount.append(BO[1])

            if len(BO) >=2:
                if BO[0] not in StayCount and BO[1] not in StayCount:
                    "They both turn right back around."
                    call Remove_Girl (BO[0])
                    call Remove_Girl (BO[1])
                    $ BO = []
                elif BO[0] not in StayCount:
                    "[BO[0].name] turns right back around, but [BO[1].name] stays."
                    call Remove_Girl (BO[0])
                    $ BO.remove(BO[0])
                elif BO[1] not in StayCount:
                    "[BO[1].name] turns right back around, but [BO[0].name] stays."
                    call Remove_Girl (BO[1])
                    $ BO.remove(BO[1])
            elif BO[0] not in StayCount:
                "She turns right back around."
                call Remove_Girl (BO[0])
                $ BO.remove(BO[0])

            while BO:


                $ BO[0].change_outfit("nude")
                $ BO[0].Water = 1
                $ BO[0].Spunk = []
                $ BO[0].recent_history.append("showered")
                $ BO[0].daily_history.append("showered")
                call expression BO[0].Tag + "_First_Bottomless" pass (1)
                call expression BO[0].Tag + "_First_Topless" pass (1)
                if BO[0] == RogueX:
                    ch_r "I wouldn't mind stick'in around though."
                elif BO[0] == KittyX:
                    ch_k "I {i}could{/i} get in on this."
                elif BO[0] == EmmaX:
                    ch_e "But, I could use some face time."
                elif BO[0] == LauraX:
                    ch_l "Scoot over."
                elif BO[0] == JeanX:
                    ch_j "You're hogging the water."
                elif BO[0] == StormX:
                    ch_s "Oh, goodbye then. . ."
                elif BO[0] == JubesX:
                    ch_v "Well, I could always join ya."
                $ BO.remove(BO[0])



    $ Round -= 30 if Round >= 30 else Round
    $ primary_action = 0

    if StayCount:

        if len(StayCount) > 1 and StayCount[0] == StayCount[1]:
            $ StayCount.remove(StayCount[0])
        if len(StayCount) > 1:

            call shift_focus (StayCount[0], StayCount[1])
            "You take a quick shower with [StayCount[0].name] and [StayCount[1].name]."
        else:
            call shift_focus (StayCount[0])
            "You take a quick shower with [StayCount[0].name]."

        call Shower_Sex

        if StayCount[0] == RogueX:

            ch_r "That was real nice, [RogueX.player_petname]."
        elif StayCount[0] == KittyX:

            ch_k "That was. . . nice."
        elif StayCount[0] == EmmaX:

            ch_e "That was. . . distracting."
        elif StayCount[0] == LauraX:

            ch_l "Well that was fun."
        elif StayCount[0] == JeanX:

            ch_j "That was fun."
        elif StayCount[0] == StormX:

            ch_s "Ah, that was relaxing."
        elif StayCount[0] == JubesX:

            ch_v "That was fun, [JubesX.player_petname]."

        if len(StayCount) > 1:

            if StayCount[1] == RogueX:

                ch_r "Yeah."
            elif StayCount[1] == KittyX:

                ch_k "Yeah, I had fun."
            elif StayCount[1] == EmmaX:

                ch_e "Indeed."
            elif StayCount[1] == LauraX:

                ch_l "Yup."
            elif StayCount[1] == JeanX:

                ch_j "Yeah, it was."
            elif StayCount[1] == StormX:

                ch_s "Certainly."
            elif StayCount[1] == JubesX:

                ch_v "Yeah, totally."
    else:


        $ Line = "You take a quick shower" + renpy.random.choice([". It was fairly uneventful.",
                        ". A few people came and went as you did so.",
                        ". That was refreshing."])
        "[Line]"

    $ Player.recent_history.append("showered")
    $ Player.daily_history.append("showered")
    if "scent" in Player.daily_history:
        $ Player.daily_history.remove("scent")

    call Get_Dressed
    if RogueX.location == bg_current:
        $ RogueX.change_outfit("towel")
    if KittyX.location == bg_current:
        $ KittyX.change_outfit("towel")
    if EmmaX.location == bg_current:
        $ EmmaX.change_outfit("towel")
    if LauraX.location == bg_current:
        $ LauraX.change_outfit("towel")
    if JeanX.location == bg_current:
        $ JeanX.change_outfit("towel")


    if JubesX.location == bg_current:
        $ JubesX.change_outfit("towel")

    $ Options = []









    return




label Shower_Sex(Options=0, Line=0):

    if len(StayCount) > 1 and (approval_check(StayCount[1], 1800,Check=1) > approval_check(StayCount[0], 1800,Check=1)):
        $ renpy.random.shuffle(StayCount)
    call shift_focus (StayCount[0])

    $ D20 = renpy.random.randint(1,20)
    $ D20 += 5 if approval_check(StayCount[0], 1800) else 0

    if "showered" in Player.recent_history:
        $ D20 = 0

    $ StayCount[0].change_face("sly")

    if len(StayCount) > 1 and D20 >= 10:
        "As you do so, both girls press their bodies body up against yours."
        $ Line = StayCount[0].name
        call Close_Launch (StayCount[0], StayCount[1])
    elif D20 >= 5:
        "As you do so, [StayCount[0].name] presses her body up against you."
        $ Line = "She"
        call Close_Launch (StayCount[0])
    else:
        $ Line = renpy.random.choice(["It was fairly uneventful.",
                    "A few people came and went as you did so.",
                    "That was refreshing."])
        "[Line]"
        if len(StayCount) > 1:
            $ StayCount[0].change_stat("lust", 50, 15)
            $ StayCount[1].change_stat("lust", 50, 15)
            $ StayCount[0].change_stat("lust", 90, 10)
            $ StayCount[1].change_stat("lust", 90, 10)
            "You got a good look at them washing off, and they didn't seem to mind the view either."
            $ StayCount[0].GLG(StayCount[1],600,4,1)
            $ StayCount[1].GLG(StayCount[0],600,4,1)
            $ StayCount[0].GLG(StayCount[1],800,2,1)
            $ StayCount[1].GLG(StayCount[0],800,2,1)
        else:
            $ StayCount[0].change_stat("lust", 50, 15)
            $ StayCount[0].change_stat("lust", 90, 10)
            "You got a good look at her washing off, and she didn't seem to mind the view either."
        return

    if Line:
        if len(StayCount) > 1:
            $ StayCount[0].change_stat("lust", 50, 5)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ StayCount[1].change_stat("lust", 50, 5)
            $ StayCount[1].change_stat("lust", 70, 3)
        else:
            $ StayCount[0].change_stat("lust", 50, 6)
            $ StayCount[0].change_stat("lust", 70, 3)
        $ Player.change_stat("focus", 50, 5)
        $ Player.change_stat("focus", 80, 2)
        menu:
            extend ""
            "Continue?":
                pass
            "Stop her." if len(StayCount) < 2:
                $ Line = 0
                call expression StayCount[0].Tag + "_Pos_Reset"
                "You take a step back, pulling away from her."
                $ StayCount[0].change_stat("love", 80, -1)
                $ StayCount[0].change_stat("obedience", 80, 5)
                $ StayCount[0].change_stat("inhibition", 80, -1)
                $ StayCount[0].change_face("sad")
                "She seems a bit disappointed."
            "Stop them." if len(StayCount) > 1:
                $ Line = 0
                call expression StayCount[1].Tag + "_Pos_Reset"
                call expression StayCount[0].Tag + "_Pos_Reset"
                "You take a step back, pulling away from them."
                $ StayCount[0].change_stat("love", 80, -1)
                $ StayCount[0].change_stat("obedience", 80, 5)
                $ StayCount[0].change_stat("inhibition", 80, -1)
                $ StayCount[1].change_stat("obedience", 80, 5)
                $ StayCount[1].change_stat("inhibition", 80, -1)
                $ StayCount[0].change_face("sad")
                $ StayCount[1].change_face("sad")
                "They seem a bit disappointed."
    if Line:

        $ Options = [1]
        if len(StayCount) > 1:
            if approval_check(StayCount[0], 1300) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 800:
                $ Options.append(2)
            if approval_check(StayCount[0], 1200) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 700:
                $ Options.append(3)

        if approval_check(StayCount[0], 1300):
            $ Options.append(4)
        if approval_check(StayCount[0], 1400):
            $ Options.append(5)

        if approval_check(StayCount[0], 1300):
            $ Options.append(6)
        if approval_check(StayCount[0], 1200):
            $ Options.append(7)

        if not approval_check(StayCount[0], 1400):

            if approval_check(StayCount[0], 1000):
                $ Options.append(8)
            if approval_check(StayCount[0], 1100):
                $ Options.append(9)
            if approval_check(StayCount[0], 1000):
                $ Options.append(10)
            if approval_check(StayCount[0], 1100):
                $ Options.append(11)

        $ renpy.random.shuffle(Options)



        if Options[0] == 2:
            $ StayCount[0].change_stat("lust", 50, 5)
            $ StayCount[0].change_stat("lust", 70, 2)
            $ StayCount[1].change_stat("lust", 50, 7)
            $ StayCount[1].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 4)
            "[Line] reaches over to [StayCount[1].name] and begins soaping up her chest."
        elif Options[0] == 3:
            $ StayCount[0].change_stat("lust", 50, 7)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ StayCount[1].change_stat("lust", 50, 8)
            $ StayCount[1].change_stat("lust", 70, 4)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 5)
            "[Line] reaches over to [StayCount[1].name] and begins soaping up her pussy."


        elif Options[0] == 4:
            if len(StayCount) > 1:
                $ StayCount[0].change_stat("lust", 50, 10)
                $ StayCount[0].change_stat("lust", 70, 7)
            else:
                $ StayCount[0].change_stat("lust", 50, 8)
                $ StayCount[0].change_stat("lust", 70, 5)
            $ Player.change_stat("focus", 50, 10)
            $ Player.change_stat("focus", 80, 6)
            "[Line] reaches down and takes your cock in her hand, soaping it up."
        elif Options[0] == 5:
            if len(StayCount) > 1:
                $ StayCount[0].change_stat("lust", 50, 12)
                $ StayCount[0].change_stat("lust", 70, 8)
            else:
                $ StayCount[0].change_stat("lust", 50, 9)
                $ StayCount[0].change_stat("lust", 70, 6)
            $ Player.change_stat("focus", 50, 10)
            $ Player.change_stat("focus", 80, 4)
            "[Line] kneels down and wraps her breasts around your cock, soaping it up."


        elif Options[0] == 6:
            if len(StayCount) > 1:
                $ StayCount[0].change_stat("lust", 50, 11)
                $ StayCount[0].change_stat("lust", 70, 6)
            else:
                $ StayCount[0].change_stat("lust", 50, 9)
                $ StayCount[0].change_stat("lust", 70, 5)
            $ Player.change_stat("focus", 50, 9)
            $ Player.change_stat("focus", 80, 4)
            "[Line] reaches down and begins fondling her own pussy, building a nice lather."
        elif Options[0] == 7:
            if len(StayCount) > 1:
                $ StayCount[0].change_stat("lust", 50, 10)
                $ StayCount[0].change_stat("lust", 70, 5)
            else:
                $ StayCount[0].change_stat("lust", 50, 9)
                $ StayCount[0].change_stat("lust", 70, 4)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 3)
            "[Line] begins rubbing her own breasts in circles, building a nice lather."


        elif Options[0] == 8:
            $ StayCount[0].change_stat("lust", 50, 6)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 7)
            $ Player.change_stat("focus", 80, 3)
            "[Line] draws her breasts up and down your arm, the soap bubbles squirting out."
        elif Options[0] == 9:
            $ StayCount[0].change_stat("lust", 50, 8)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 3)
            "[Line] kneels down and rubs her breasts against your leg, soaping it up."
        elif Options[0] == 10:
            $ StayCount[0].change_stat("lust", 50, 7)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 6)
            $ Player.change_stat("focus", 80, 3)
            "[Line] presses against your back, her soapy breasts rubbing back and forth against it."
        elif Options[0] == 11:
            $ StayCount[0].change_stat("lust", 50, 7)
            $ StayCount[0].change_stat("lust", 70, 3)
            $ Player.change_stat("focus", 50, 8)
            $ Player.change_stat("focus", 80, 4)
            "[Line] presses against your chest, her soapy breasts rubbing back and forth against it."
        elif Options[0] == 1:
            $ StayCount[0].change_stat("lust", 50, 5)
            $ StayCount[0].change_stat("lust", 70, 2)
            $ Player.change_stat("focus", 50, 6)
            $ Player.change_stat("focus", 80, 3)
            "[Line] stares silently at you as she moves her hands along her soapy body. . ."
            $ Line = 0

    if Line and len(StayCount) > 1:

        $ D20 += 5 if approval_check(StayCount[1], 1800) else 0
        if StayCount[1].GirlLikeCheck(StayCount[0]) <= 800 and 2 <= Options[0] <=3:
            $ D20 -= 5
        if StayCount[1].GirlLikeCheck(StayCount[0]) <= 600:
            $ D20 -= 5

        if 2 <= Options[0] <= 3:

            if approval_check(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 800:
                $ StayCount[1].change_face("sexy",1)
                $ StayCount[0].change_stat("lust", 50, 5)
                $ StayCount[0].change_stat("lust", 70, 5)
                $ StayCount[1].change_stat("lust", 50, 12)
                $ StayCount[1].change_stat("lust", 70, 12)
                call Close_Launch (StayCount[0], StayCount[1])
                "[StayCount[1].name] seems really into this, and returns the favor."
                $ Player.change_stat("focus", 50, 7)
                $ Player.change_stat("focus", 80, 3)
                $ Line = 4
            elif approval_check(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700:
                $ StayCount[1].change_face("sexy",2,Eyes="closed")
                $ StayCount[1].change_stat("lust", 50, 10)
                $ StayCount[1].change_stat("lust", 70, 10)
                $ Player.change_stat("focus", 50, 5)
                $ Player.change_stat("focus", 80, 3)
                call Close_Launch (StayCount[0], StayCount[1])
                "[StayCount[1].name] seems really into this, and leans into it."
            else:
                $ StayCount[1].change_stat("lust", 50, 10)
                $ StayCount[1].change_face("sadside",Brows="confused")
                "[StayCount[1].name] doesn't really seem to appreciate this."
                "She pulls away."
                $ Line = 3
        else:

            if (approval_check(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700) or approval_check(StayCount[1], 2000):
                if Options[0] == 5:
                    $ StayCount[1].change_stat("lust", 50, 10)
                    $ StayCount[1].change_stat("lust", 70, 5)
                    $ Player.change_stat("focus", 50, 6)
                    $ Player.change_stat("focus", 80, 3)
                    call Close_Launch (StayCount[0], StayCount[1])
                    "[StayCount[1].name] seems really into this, slowly rubbing against you as she watches."
                else:
                    $ StayCount[1].change_stat("lust", 50, 10)
                    $ StayCount[1].change_stat("lust", 70, 5)
                    $ Player.change_stat("focus", 50, 5)
                    $ Player.change_stat("focus", 80, 3)
                    call Close_Launch (StayCount[0], StayCount[1])
                    "[StayCount[1].name] seems really into this, and joins her on the other side."
                $ Line = 4
            elif ((approval_check(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 600)) or approval_check(StayCount[1], 1600):
                $ StayCount[1].change_face("sexy",2,Eyes="down")
                $ StayCount[1].change_stat("lust", 50, 10)
                $ StayCount[1].change_stat("lust", 70, 5)
                "[StayCount[1].name] seems really into this, and watches her do it."
            else:
                $ StayCount[1].change_face("sadside",Brows="confused")
                $ StayCount[1].change_stat("lust", 50, 5)
                "[StayCount[1].name] doesn't really seem to appreciate this."
                $ Line = 3
    if Line:
        menu:
            extend ""
            "Continue?":
                pass
            "Stop her." if len(StayCount) < 2:
                $ Line = 0
                call expression StayCount[0].Tag + "_Pos_Reset"
                "You take a step back, pulling away from her."
                $ StayCount[0].change_stat("love", 80, -2)
                $ StayCount[0].change_stat("obedience", 80, 5)
                $ StayCount[0].change_stat("inhibition", 80, -2)
                $ StayCount[0].change_face("sad")
                "She seems a bit disappointed."
            "Stop them." if len(StayCount) > 1:
                $ Line = 0
                call expression StayCount[1].Tag + "_Pos_Reset"
                call expression StayCount[0].Tag + "_Pos_Reset"
                "You take a step back, pulling away from them."
                $ StayCount[0].change_face("sad")
                $ StayCount[0].change_stat("love", 80, -2)
                $ StayCount[0].change_stat("obedience", 80, 5)
                $ StayCount[0].change_stat("inhibition", 80, -2)
                if Line == 3:
                    $ StayCount[1].change_stat("love", 80, 4)
                    $ StayCount[1].change_stat("obedience", 80, 5)
                    $ StayCount[1].change_face("bemused")
                    "[StayCount[0].name] seems a bit disappointed, but [StayCount[1].name] seems pleased."
                else:
                    $ StayCount[1].change_stat("love", 80, -1)
                    $ StayCount[1].change_stat("obedience", 80, 5)
                    $ StayCount[1].change_stat("inhibition", 80, -1)
                    $ StayCount[1].change_face("sad")
                    "They seem a bit disappointed."

    if Line:

        if len(StayCount) > 1 and Line != 3:
            $ StayCount[0].GLG(StayCount[1],600,4,1)
            $ StayCount[1].GLG(StayCount[0],600,4,1)
            $ StayCount[0].GLG(StayCount[1],800,3,1)
            $ StayCount[1].GLG(StayCount[0],800,3,1)
            $ StayCount[0].GLG(StayCount[1],900,1,1)
            $ StayCount[1].GLG(StayCount[0],900,1,1)
        if 2 <= Options[0] <= 3 and D20 >= 15:

            $ StayCount[1].GLG(StayCount[0],900,4,1)
            $ Player.change_stat("focus", 50, 10)
            $ Player.change_stat("focus", 80, 5)
            "After a few minutes of this, it looks like [StayCount[1].name] gets off."
            call Girl_Cumming (StayCount[1], 1)
            if Line == 4:
                $ StayCount[0].GLG(StayCount[1],900,3,1)
                "It looks like [StayCount[0].name] is reacting positively to it as well. . ."
                call Girl_Cumming (StayCount[0], 1)
            if len(StayCount) > 1:
                "The girls take a step back."
                call expression StayCount[1].Tag + "_Pos_Reset"
            else:
                "[StayCount[0].name] takes a step back."
            call expression StayCount[0].Tag + "_Pos_Reset"

        elif 4 <= Options[0] <= 5 and D20 >= 10:

            $ Player.focus = 15
            if Options[0] == 5:
                $ StayCount[0].Spunk.append("tits")

            if Line == 4:
                $ StayCount[0].change_stat("inhibition", 90, 7)
                $ StayCount[1].change_stat("inhibition", 90, 4)
                $ StayCount[0].GLG(StayCount[1],900,3,1)
                $ StayCount[1].GLG(StayCount[0],900,3,1)
                "After a few minutes of this, the two of them manage to get you off."
            else:
                $ StayCount[0].change_stat("inhibition", 90, 5)
                "After a few minutes of this, she manages to get you off."
            "A little more work is needed to clean up the mess."
            if Options[0] == 5:
                $ StayCount[0].Spunk = []
            if len(StayCount) > 1:
                "The girls take a step back."
                call expression StayCount[1].Tag + "_Pos_Reset"
            else:
                "[StayCount[0].name] takes a step back."
            call expression StayCount[0].Tag + "_Pos_Reset"

        elif 6 <= Options[0] <= 7 and D20 >= 15:

            $ StayCount[0].change_stat("inhibition", 90, 7)
            $ Player.change_stat("focus", 50, 15)
            $ Player.change_stat("focus", 80, 5)
            "After a few minutes of this, it looks like [StayCount[0].name] gets off."
            call Girl_Cumming (StayCount[0], 1)
            if Line == 4:
                $ StayCount[1].change_stat("inhibition", 90, 6)
                $ StayCount[0].GLG(StayCount[1],900,3,1)
                "It looks like [StayCount[1].name] is enjoying herself as well. . ."
                call Girl_Cumming (StayCount[1], 1)
            if len(StayCount) > 1:
                $ StayCount[1].GLG(StayCount[0],900,3,1)
                "The girls take a step back."
                call expression StayCount[1].Tag + "_Pos_Reset"
            else:
                "[StayCount[0].name] takes a step back."
            call expression StayCount[0].Tag + "_Pos_Reset"
        else:

            if len(StayCount) > 1:
                call expression StayCount[1].Tag + "_Pos_Reset"
            call expression StayCount[0].Tag + "_Pos_Reset"
            $ Player.change_stat("focus", 50, 15)
            $ Player.change_stat("focus", 80, 5)
            if D20 >= 15:
                "After a minute or two, it sounds like someone is coming, so you scramble apart."
                "Disappointing. . ."
            elif D20 >= 10:
                "After a minute or two, she seems satisfied with her efforts, and pulls back."
                if 4 <= Options[0] <= 5:
                    "You're left pretty hard."
            else:
                "After a minute or so of this, she draws back and finshes washing herself off."
                if 4 <= Options[0] <= 5:
                    "You're left pretty hard."
    call shift_focus (StayCount[0])
    return








label Study_Room_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
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
                    if "Sneakthief" in KittyX.Traits:
                        ch_k "No problem. . ."
                        jump Study_Room
                    elif "no_thief" in KittyX.recent_history:
                        ch_k "I told you, no."
                    elif approval_check(KittyX, 400, "I") or approval_check(KittyX, 1400):
                        $ KittyX.change_stat("love", 90, 3)
                        $ KittyX.change_stat("obedience", 50, 10)
                        $ KittyX.change_stat("inhibition", 60, 10)
                        ch_k "Heh, you have a wicked mind. . ."
                        $ KittyX.Traits.append("Sneakthief")
                        jump Study_Room
                    else:
                        $ KittyX.change_stat("love", 90, -3)
                        $ KittyX.change_stat("obedience", 50, 2)
                        $ KittyX.change_stat("inhibition", 60, 2)
                        ch_k "Um, I don't really feel comfortable doing that. . ."
                        $ KittyX.recent_history.append("no_thief")
                "Open the door.":
                    if "Sneakthief" in KittyX.Traits:
                        ch_k "No problem. . ."
                        jump Study_Room
                    elif "no_thief" in KittyX.recent_history:
                        ch_k "I told you, no."
                    elif approval_check(KittyX, 500, "O") or approval_check(KittyX, 1600):
                        $ KittyX.change_stat("obedience", 50, 15)
                        $ KittyX.change_stat("inhibition", 60, 10)
                        ch_k "Heh, if you say so. . ."
                        $ KittyX.Traits.append("Sneakthief")
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
                "Do you think you could pick that lock?" if "Sneakthief" not in StormX.Traits:
                    if "no_thief" in StormX.recent_history:
                        ch_s "I told you, I won't do that."
                    elif approval_check(StormX, 400, "I") or approval_check(StormX, 1400):
                        $ StormX.change_stat("love", 90, 3)
                        $ StormX.change_stat("obedience", 80, 10)
                        $ StormX.change_stat("inhibition", 60, 10)
                        $ StormX.change_face("sly")
                        ch_s "Oh, this should be interesting. . ."
                        "She pulls some picks from behind her ear."
                        ch_s "Ok, we've got a click on 1. . . 2 is binding. . ."
                        ch_s "Click on 3. . . 4. . . click on 5, back to 2. . . and we're in."
                        $ StormX.Traits.append("Sneakthief")
                        $ StormX.change_face("normal")
                        jump Study_Room
                    else:
                        $ StormX.change_stat("love", 90, -3)
                        $ StormX.change_stat("obedience", 50, 2)
                        $ StormX.change_stat("inhibition", 60, 2)
                        ch_s "I don't think that's really appropriate behavior. . ."
                        $ StormX.recent_history.append("no_thief")
                "Could you pick the lock again?" if "Sneakthief" in StormX.Traits:
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
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        if time_index >= 3:
            "It's late, you head back to your room."
            jump Player_Room
        else:
            call Wait
            call Girls_Location

    call GirlsAngry
    call XavierFace ("happy")


    if time_index >= 3:
        $ Line = "You are in Xavier's Study, but he isn't in at the moment. What would you like to do?"
    else:
        $ Line = "You are in Xavier's Study. What would you like to do?"
    menu:
        "[Line]"
        "Chat" if time_index >= 3:
            call Chat

        "Plan Omega!" if time_index < 3 and RogueX.location == bg_current and Player.Lvl >= 5:
            if approval_check(RogueX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (RogueX)
            else:
                ch_r "I don't want to do that. . ."
        "Plan Kappa!" if time_index < 3 and KittyX.location == bg_current and Player.Lvl >= 5:
            if "Xavier's photo" in Player.Inventory and approval_check(KittyX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (KittyX)
            elif "Xavier's photo" in Player.Inventory:
                ch_k "I don't really want to do that. . ."
            else:
                ch_k "What?"
        "Plan Psi!" if time_index < 3 and EmmaX.location == bg_current and Player.Lvl >= 5:
            if approval_check(EmmaX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (EmmaX)
            else:
                ch_e "I'd rather not. . ."
        "Plan Chi!" if time_index < 3 and LauraX.location == bg_current and Player.Lvl >= 5:
            if LauraX.Lvl >= 2 and approval_check(LauraX, 1500, TabM=1, Loc="No") and approval_check(LauraX, 750, "I"):
                call Xavier_Plan (LauraX)
            elif LauraX.Lvl < 2 or not approval_check(LauraX, 750, "I"):
                ch_l "I'm not ready for that."
            else:
                ch_l "Huh?"
        "Plan Alpha!" if time_index < 3 and JeanX.location == bg_current and Player.Lvl >= 5:
            if approval_check(JeanX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (JeanX)
            else:
                ch_j "You're on your own there."
        "Plan Rho!" if time_index < 3 and StormX.location == bg_current and Player.Lvl >= 5:
            if "Xavier's files" in Player.Inventory and approval_check(StormX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan (StormX)
            elif "Xavier's files" in Player.Inventory:
                ch_s "I do not believe that would be approrpriate."
            else:
                ch_s "What is that?"
        "Plan Zeta!" if time_index < 3 and JubesX.location == bg_current and Player.Lvl >= 5:
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
                jump Player_Room
            else:
                call Wait
                call Girls_Location
                ch_x "Not that I mind the company, but is there something I can do for you?"

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry
        "Return to Your Room" if TravelMode:
            jump Player_Room_Entry

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
        jump Player_Room_Entry
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
                                $ Player.Cash += 500
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
                                $ Player.Cash += 500
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
        if "Xavier's photo" not in Player.Inventory:
            if D20 >= 10:
                "Buried under a pile of documents, you find a printed out photo."
                "It appears to be a selfie of Mystique making out with Xavier."
                "She's reaching down to adjust his . . . oh, {i}that's{/i} interesting."
                if StormX.location == bg_current:
                    ch_s "You should probably put that back, it looks personal."
                else:
                    "[[Xavier's photo acquired.]"
                    $ Player.Inventory.append("Xavier's photo")
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
        if "Xavier's files" not in Player.Inventory:
            if D20 >= 10:
                "You search through some documents, but don't find anything."
                if StormX.location == bg_current:
                    ch_s "Hmm. . ."
                    "She reaches under some of the documents and finds a small notch."
                    "With a soft \"click\"a panel flips open in the drawer, revealing some file folders."
                    "Inside are some fairly. . . detailed reports on the girls at the school."
                    $ StormX.change_face("surprised",2)
                    "These include body measurements, sexual histories. . . masturbation habits?"
                    $ StormX.change_stat("obedience", 70, 5)
                    $ StormX.change_stat("inhibition", 70, 5)
                    $ StormX.change_face("angry")
                    ch_s "Well, I don't think Charles should be holding information like this. . ."
                    $ StormX.change_face("normal",1)
                    "[[Xavier's files acquired.]"
                    $ Player.Inventory.append("Xavier's files")
                    if "rho" in Player.history:
                        $ Player.history.remove("rho")
            else:
                "You search through some documents, but don't find anything."
                "It would probably take a more thorough search."
        else:
            "There doesn't seem to be anything more of interest in here."

    $ counter += 3
    jump Study_Room_Explore




label Rogue_Room_Entry:
    $ bg_current = RogueX.home
    call Girls_Room_Entry (RogueX)
    $ bg_current = "bg_campus"
    jump Misplaced
label Kitty_Room_Entry:
    $ bg_current = KittyX.home
    call Girls_Room_Entry (KittyX)
    $ bg_current = "bg_campus"
    jump Misplaced
label Emma_Room_Entry:
    $ bg_current = EmmaX.home
    call Girls_Room_Entry (EmmaX)
    $ bg_current = "bg_campus"
    jump Misplaced
label Laura_Room_Entry:
    $ bg_current = LauraX.home
    call Girls_Room_Entry (LauraX)
    $ bg_current = "bg_campus"
    jump Misplaced
label Jean_Room_Entry:
    $ bg_current = JeanX.home
    call Girls_Room_Entry (JeanX)
    $ bg_current = "bg_campus"
    jump Misplaced
label Storm_Room_Entry:
    $ bg_current = StormX.home
    call Girls_Room_Entry (StormX)
    $ bg_current = "bg_campus"
    jump Misplaced
label Jubes_Room_Entry:
    $ bg_current = JubesX.home
    call Girls_Room_Entry (JubesX)
    $ bg_current = "bg_campus"
    jump Misplaced

label Girls_Room_Entry(Chr=0):

    if Chr not in all_Girls:
        return
    $ Player.DrainWord("locked",0,0,1)
    call shift_focus (Chr)
    $ bg_current = Chr.home
    $ Nearby = []
    call Gym_Clothes_Off
    call set_the_scene (Entry=1)
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    $ D20 = renpy.random.randint(1, 20)

    $ Round -= 5 if Round >= 5 else Round

    if Chr in Party:
        if time_index >= 3 or (time_index == 2 and Round <= 10):
            if approval_check(Chr, 1000, "LI",Alt=[[JubesX],500]) or approval_check(Chr, 600, "OI",Alt=[[JubesX],300]):

                if Chr == RogueX:
                    ch_r "It's pretty late, [Chr.player_petname], but you can come in for a little bit."
                elif Chr == KittyX:
                    ch_k "It's kinda late, [Chr.player_petname], but you can have a minute."
                elif Chr == EmmaX:
                    ch_e "It's rather late, [Chr.player_petname], but I can spare you some time."
                elif Chr == LauraX:
                    ch_l "It's getting late, but come on in."
                elif Chr == JeanX:
                    ch_j "It's late, but whatever."
                elif Chr == StormX:
                    ch_s "You've come by fairly late, [Chr.player_petname], but come in."
                elif Chr == JubesX:
                    ch_v "Sure, come on in."
            elif Chr.addiction >= 50:
                if Chr == RogueX:
                    ch_r "Um, yeah, you'd better come in. . ."
                elif Chr == KittyX:
                    ch_k "I'd really like to see you. . ."
                elif Chr == EmmaX:
                    ch_e "Yes. . . I suppose you should. . ."
                elif Chr == LauraX:
                    ch_l "Um, yeah, you'd better come in. . ."
                elif Chr == JeanX:
                    ch_j "Oh, um, sure, come in."
                elif Chr == StormX:
                    ch_s "Oh, yes, come in."
                elif Chr == JubesX:
                    ch_v "Oh, yes, do come in. . ."
            elif approval_check(Chr, 500, "LI") or approval_check(Chr, 300, "OI"):

                if Chr == RogueX:
                    ch_r "It's a little late [Chr.player_petname]. See you tomorrow."
                elif Chr == KittyX:
                    ch_k "It's a little late [Chr.player_petname]. Tomorrow?"
                elif Chr == EmmaX:
                    ch_e "It's late [Chr.player_petname]. I'll see you tomorrow."
                elif Chr == LauraX:
                    ch_l "See you tomorrow."
                elif Chr == JeanX:
                    ch_j "It's late, see ya."
                elif Chr == StormX:
                    ch_s "You've come by fairly late, [Chr.player_petname], perhaps visit tomorrow."
                elif Chr == JubesX:
                    ch_v "No thanks. . ."
                $ Chr.recent_history.append("noentry")
                $ Chr.daily_history.append("noentry")
                if Chr in Party:
                    $ Party.remove(Chr)
                "She heads inside and closes the door behind her."
                return
        else:

            if Chr == RogueX:
                ch_r "Come on in, [Chr.player_petname]."
            elif Chr == KittyX:
                ch_k "Come on in!"
            elif Chr == EmmaX:
                ch_e "Don't just stand at the door."
            elif Chr == LauraX:
                ch_l "Come on in."
            elif Chr == JeanX:
                ch_j "Make yourself at home."
            elif Chr == StormX:
                ch_s "Make yourself welcome."
            elif Chr == JubesX:
                ch_v "Have a seat or whatever. . ."
        call EventCalls
        jump expression Chr.Tag + "_Room"



    if Round >= 10 and Chr.location == bg_current and "les" in Chr.recent_history:
        call Girls_Caught_Lesing (Chr)
        if not _return:
            jump expression Chr.Tag + "_Room"

    if bg_current == KittyX.home and "dress2" in LauraX.history and not Party:

        call Laura_Dressup3
        $ bg_current = "bg_campus"
        jump Misplaced

    if Round >= 10 and Chr.location == bg_current and "gonnafap" in Chr.daily_history and D20 >= 5:

        call Girl_Caught_Mastubating (Chr)
    else:

        if Chr in Keys:
            menu:
                "You have a key, what do you do?"
                "Knock politely":
                    $ Line = "knock"
                "Use the key to enter.":

                    call set_the_scene

        if Line != "knock" and Chr in Keys:
            if Chr.location == bg_current:

                if Round <= 10:
                    if "noentry" in Chr.recent_history or "angry" in Chr.recent_history:
                        $ Chr.change_face("angry")
                        if Chr == RogueX:
                            ch_r "Buzz off already."
                        elif Chr == KittyX:
                            ch_k "GTFO."
                        elif Chr == EmmaX:
                            ch_e "Out!"
                        elif Chr == LauraX:
                            ch_l "Get out of my face."
                        elif Chr == JeanX:
                            ch_j "Out!"
                        elif Chr == StormX:
                            ch_s "Get out."
                        elif Chr == JubesX:
                            ch_v "Out!"
                        "[Chr.name] shoves you back into the hall."
                        return
                    if time_index >= 3:
                        "She's asleep in bed. You slip out quietly."
                        return
                elif "gonnafap" in Chr.daily_history and D20 >= 5:

                    call Girl_Caught_Mastubating (Chr)
                elif D20 >=15 and (time_index >= 3 or time_index == 0):

                    call Girl_Caught_Changing (Chr)
                    jump expression Chr.Tag + "_Room"
        else:



            "You knock on [Chr.name]'s door."
            if Chr.location != bg_current:
                "Looks like she's not home right now."

                if Chr in Keys:
                    menu:
                        "Go in and wait for her?"
                        "Yes":
                            $ Line = 0
                            jump expression Chr.Tag + "_Room"
                        "No":
                            pass
                "You head back."
                $ bg_current = "bg_campus"
                call set_the_scene
                jump Misplaced

            if Round <= 10:
                if time_index >= 3:
                    "There's no answer, she's probably asleep."
                    $ bg_current = "bg_campus"
                    call set_the_scene
                    jump Misplaced

            if (D20 >=19 and Chr.lust >= 50) or (D20 >=15 and Chr.lust >= 70) or (D20 >=10 and Chr.lust >= 80):

                "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                "After several seconds and some more shuffling of clothing, [Chr.name] comes to the door."
                $ Chr.change_face("perplexed",2)
                call set_the_scene
                if Chr == RogueX:
                    ch_r "Sorry about that [Chr.player_petname], I was. . . working out."
                elif Chr == KittyX:
                    ch_k "Oh, hey, [Chr.player_petname], I was. . . never mind."
                elif Chr == EmmaX:
                    ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                elif Chr == LauraX:
                    ch_l "Um, hey [Chr.player_petname], just working off some stress."
                elif Chr == JeanX:
                    ch_j "Oh, um, hey."
                elif Chr == StormX:
                    ch_s "Ah, [Chr.player_petname], I was. . . preocupied."
                elif Chr == JubesX:
                    ch_v "Oh, um, [Chr.player_petname]. I was just. . . taking care of something."
                $ Chr.change_face("perplexed",1)
                $ approval_bonus += 10
            elif D20 >=15 and (time_index >= 3 or time_index == 0):

                "You hear the rustling of fabric and some knocking around, but after a few seconds [Chr.name] comes to the door."
                call set_the_scene
                if Chr == RogueX:
                    ch_r "Sorry about that [Chr.player_petname], I was just getting changed."
                elif Chr == KittyX:
                    ch_k "Oh, hi [Chr.player_petname], I was[KittyX.like]just getting changed."
                elif Chr == EmmaX:
                    ch_e "Oh, do come in [Chr.player_petname], don't mind that I was just getting changed."
                elif Chr == LauraX:
                    ch_l "Hey [Chr.player_petname], I was just getting dressed."
                elif Chr == JeanX:
                    ch_j "Hey [Chr.player_petname], I was getting dressed."
                elif Chr == StormX:
                    ch_s "Oh, hello, [Chr.player_petname]. I was just getting changed."
                elif Chr == JubesX:
                    ch_v "Oh, hey, [Chr.player_petname], I was getting dressed."
            elif "angry" in Chr.recent_history:
                $ Chr.change_face("angry")
                if Chr == RogueX:
                    ch_r "I don't want to deal with you right now."
                elif Chr == KittyX:
                    ch_k "Nooope."
                elif Chr == EmmaX:
                    ch_e "I haven't any time for this."
                elif Chr == LauraX:
                    ch_l "Nope."
                elif Chr == JeanX:
                    ch_j "Out!"
                elif Chr == StormX:
                    ch_s "Get out."
                elif Chr == JubesX:
                    ch_v "Out!"
                $ primary_action = 0
                "[Chr.name] knocks you back into the hall and slams the door."
                $ bg_current = "bg_campus"
                jump Misplaced
            else:
                call set_the_scene
                "[Chr.name] opens the door and leans out."
                "You ask if you can come inside."



        if Chr.location != bg_current:
            "Looks like she's not home right now."
            if Chr in Keys:
                menu:
                    "Go in and wait for her?"
                    "Yes":
                        $ Line = 0
                        jump expression Chr.Tag + "_Room"
                    "No":
                        pass
            "You head back."
            $ bg_current = "bg_campus"
            jump Misplaced
        elif time_index >= 3 and "noentry" in Chr.recent_history:
            if Chr == RogueX:
                ch_r "Hey, I told you you're not welcome. I'll see you tomorrow."
            elif Chr == KittyX:
                ch_k "Scram. I'll see you tomorrow."
            elif Chr == EmmaX:
                ch_e "Later, [Chr.player_petname]."
            elif Chr == LauraX:
                ch_l "Not tonight, [Chr.player_petname]."
            elif Chr == JeanX:
                ch_j "No, not tonight."
            elif Chr == StormX:
                ch_s "I made myself clear, [Chr.player_petname], not tonight."
            elif Chr == JubesX:
                ch_v "Don't mess with me at night, [Chr.player_petname]. Out!"
            $ bg_current = "bg_campus"
            jump Misplaced
        elif "noentry" in Chr.recent_history or "angry" in Chr.recent_history:
            $ Chr.change_face("angry")
            if Chr == RogueX:
                ch_r "Buzz off already."
            elif Chr == KittyX:
                ch_k "GTFO."
            elif Chr == EmmaX:
                ch_e "Out."
            elif Chr == LauraX:
                ch_l "Fuck off."
            elif Chr == JeanX:
                ch_j "Out!"
            elif Chr == StormX:
                ch_s "Get out."
            elif Chr == JubesX:
                ch_v "Out!"
            $ bg_current = "bg_campus"
            jump Misplaced
        elif time_index >= 3 and (Chr.event_counter["sleepover"] or Chr.SEXP >= 30 or Chr == JubesX):

            if Chr == RogueX:
                ch_r "It's pretty late, [Chr.player_petname], but it's always nice to see you."
            elif Chr == KittyX:
                ch_k "It's late, [Chr.player_petname], but you're so cute."
            elif Chr == EmmaX:
                ch_e "It is getting late, [Chr.player_petname]."
                ch_e "but you are so adorable."
            elif Chr == LauraX:
                ch_l "It's late, but I was hoping you'd stop by."
            elif Chr == JeanX:
                ch_j "Hey [Chr.player_petname], almost time for bed."
            elif Chr == StormX:
                ch_s "Hello, [Chr.player_petname], it's almost bedtime."
            elif Chr == JubesX:
                ch_v "Oh, hey, [Chr.player_petname] come on in."
        elif time_index >= 3 and (approval_check(Chr, 1000, "LI") or approval_check(Chr, 600, "OI") or Chr == JubesX):

            if Chr == RogueX:
                ch_r "It's pretty late, [Chr.player_petname], but you can come in for a little bit."
            elif Chr == KittyX:
                ch_k "It's late, [Chr.player_petname], but I could hang out a bit."
            elif Chr == EmmaX:
                ch_e "It is getting late, [Chr.player_petname], but I could make some time."
            elif Chr == LauraX:
                ch_l "It's late, [Chr.player_petname], but you can come in."
            elif Chr == JeanX:
                ch_j "It's kinda late."
            elif Chr == StormX:
                ch_s "You've come by fairly late, [Chr.player_petname], but come in."
            elif Chr == JubesX:
                ch_v "Oh, hey, [Chr.player_petname] come on in."
        elif Chr.addiction >= 50:
            $ Chr.change_face("manic")
            if Chr == RogueX:
                ch_r "Um, yeah, you'd better come in. . ."
            elif Chr == KittyX:
                ch_k "I could use some attention. . ."
            elif Chr == EmmaX:
                ch_e "I. . . suppose you should. . ."
            elif Chr == LauraX:
                ch_l "You should come in. . ."
            elif Chr == JeanX:
                ch_j "Oh, um. . . hey. . ."
            elif Chr == StormX:
                ch_s "Oh, yes, come in."
            elif Chr == JubesX:
                ch_v "Oh, yes, do come in. . ."
        elif time_index >= 3 and (approval_check(Chr, 500, "LI") or approval_check(Chr, 300, "OI")):
            if Chr == RogueX:
                ch_r "It's a little late [Chr.player_petname]. Maybe tomorrow."
            elif Chr == KittyX:
                ch_k "It's late [Chr.player_petname]. Tomorrow?"
            elif Chr == EmmaX:
                ch_e "It's late [Chr.player_petname]. I'll see you tomorrow."
            elif Chr == LauraX:
                ch_l "It's late [Chr.player_petname]. Come back tomorrow."
            elif Chr == JeanX:
                ch_j "It's late, see ya."
            elif Chr == StormX:
                ch_s "You've come by fairly late, [Chr.player_petname], perhaps tomorrow."
            elif Chr == JubesX:
                ch_v "Nope. . ."
            $ Chr.recent_history.append("noentry")
            $ Chr.daily_history.append("noentry")
            $ bg_current = "bg_campus"
            jump Misplaced
        elif approval_check(Chr, 600, "LI") or approval_check(Chr, 300, "OI"):

            if Chr == RogueX:
                ch_r "Sure, come on in [Chr.player_petname]."
            elif Chr == KittyX:
                ch_k "Sure, come on in [Chr.player_petname]."
            elif Chr == EmmaX:
                ch_e "Come in, [Chr.player_petname]."
            elif Chr == LauraX:
                ch_l "Make yourself at home, I guess."
            elif Chr == JeanX:
                ch_j "Hey, make yourself at home."
            elif Chr == StormX:
                ch_s "Oh, hello [Chr.player_petname], come in."
            elif Chr == JubesX:
                ch_v "Oh, hey, [Chr.player_petname] come on in."
        else:

            if Chr == RogueX:
                ch_r "I'd rather you didn't come in, thanks."
            elif Chr == KittyX:
                ch_k "Nah, you can stay out."
            elif Chr == EmmaX:
                ch_e "I don't think that would be appropriate."
            elif Chr == LauraX:
                ch_l "Nah."
            elif Chr == JeanX:
                ch_j "Nah, get going."
            elif Chr == StormX:
                ch_s "I would rather you didn't."
            elif Chr == JubesX:
                ch_v "Oh, no thanks."
            $ Chr.recent_history.append("noentry")
            $ Chr.daily_history.append("noentry")
            $ bg_current = "bg_campus"
            jump Misplaced


    call EventCalls
    if Chr.location == Chr.home and "angry" in Chr.recent_history:

        $ Line = 0
        $ primary_action = 0
        "[Chr.name] shoves you back into the hall and slams the door. You head back to your room."
        $ bg_current = "bg_player"
        jump Misplaced
    jump Misplaced






label Rogue_Room:
    $ bg_current = "bg_rogue"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls
    call GirlsAngry


    if RogueX.location == bg_current:
        $ Line = "You are in "+RogueX.name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+RogueX.name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        "Chat":

            call Chat
        "Would you like to study?":

            call Study_Session

        "Lock the door" if "locked" not in Player.Traits:
            if RogueX.location == bg_current and not approval_check(RogueX, 1000):
                ch_r "Hey, could you maybe keep that open, [RogueX.player_petname]?"
            else:
                "You lock the door"
                $ Player.Traits.append("locked")
                call Taboo_Level

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level

        "Sleep." if time_index >= 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Wait." if time_index < 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Return to Your Room" if TravelMode:
            jump Player_Room_Entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call Girls_Room_Entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call Girls_Room_Entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call Girls_Room_Entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call Girls_Room_Entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call Girls_Room_Entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call Girls_Room_Entry (JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    if "angry" in RogueX.recent_history:
        $ RogueX.change_face("angry")
        ch_r "I really think you should leave."
        "[RogueX.name] pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ primary_action = 0
        jump Player_Room
    jump Rogue_Room







label Kitty_Room:
    $ bg_current = "bg_kitty"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls
    call GirlsAngry


    if KittyX.location == bg_current:
        $ Line = "You are in "+KittyX.name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+KittyX.name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        "Chat":

            call Chat
        "Would you like to study?":

            call Study_Session

        "Lock the door" if "locked" not in Player.Traits:
            if KittyX.location == bg_current and not approval_check(KittyX, 1000):
                ch_k "Um, I'd[KittyX.like]rather you didn't lock my door, [KittyX.player_petname]?"
            else:
                "You lock the door"
                $ Player.Traits.append("locked")
                call Taboo_Level

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level

        "Sleep." if time_index >= 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Wait." if time_index < 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Return to Your Room" if TravelMode:
            jump Player_Room_Entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call Girls_Room_Entry (RogueX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call Girls_Room_Entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call Girls_Room_Entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call Girls_Room_Entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call Girls_Room_Entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call Girls_Room_Entry (JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    if "angry" in KittyX.recent_history:
        $ KittyX.change_face("angry")
        ch_k "Go. Now."
        "[KittyX.name] pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ primary_action = 0
        jump Player_Room
    jump Kitty_Room







label Emma_Room:
    $ bg_current = "bg_emma"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls
    call GirlsAngry


    if EmmaX.location == bg_current:
        $ Line = "You are in "+EmmaX.name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+EmmaX.name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        "Chat":

            call Chat
        "Would you like to study?":

            call Study_Session

        "Lock the door" if "locked" not in Player.Traits:
            if EmmaX.location == bg_current and not approval_check(EmmaX, 1000):
                ch_e "Do you really think it's appropriate for you to lock the door to my room?"
            else:
                "You lock the door"
                $ Player.Traits.append("locked")
                call Taboo_Level

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level

        "Sleep." if time_index >= 3 and EmmaX.location == bg_current:
            call Round10
            call Girls_Location
            call EventCalls

        "Wait." if time_index < 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Return to Your Room" if TravelMode:
            jump Player_Room_Entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call Girls_Room_Entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call Girls_Room_Entry (KittyX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call Girls_Room_Entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call Girls_Room_Entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call Girls_Room_Entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call Girls_Room_Entry (JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    if "angry" in EmmaX.recent_history:
        $ EmmaX.change_face("angry")
        ch_e "I think you should leave now."
        "[EmmaX.name] pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ primary_action = 0
        jump Player_Room
    jump Emma_Room







label Laura_Room:
    $ bg_current = "bg_laura"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls
    call GirlsAngry


    if LauraX.location == bg_current:
        $ Line = "You are in "+LauraX.name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+LauraX.name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        "Chat":

            call Chat
        "Would you like to study?":

            call Study_Session

        "Lock the door" if "locked" not in Player.Traits:
            if LauraX.location == bg_current and not approval_check(LauraX, 1200):
                ch_l "I don't want to feel caged up like that, [LauraX.player_petname]."
            else:
                "You lock the door"
                $ Player.Traits.append("locked")
                call Taboo_Level

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level

        "Sleep." if time_index >= 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Wait." if time_index < 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Return to Your Room" if TravelMode:
            jump Player_Room_Entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call Girls_Room_Entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call Girls_Room_Entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call Girls_Room_Entry (EmmaX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call Girls_Room_Entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call Girls_Room_Entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call Girls_Room_Entry (JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    if "angry" in LauraX.recent_history:
        $ LauraX.change_face("angry")
        $ Line = 0
        $ primary_action = 0
        ch_l "Get out before we both regret it."
        "[LauraX.name] shoves you back into the hall and slams the door. You head back to your room."
        jump Player_Room
    jump Laura_Room





label Jean_Room:
    $ bg_current = "bg_jean"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls
    call GirlsAngry


    if JeanX.location == bg_current:
        $ Line = "You are in "+JeanX.name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+JeanX.name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        "Chat":

            call Chat
        "Would you like to study?":

            call Study_Session

        "Lock the door" if "locked" not in Player.Traits:
            if JeanX.location == bg_current and not approval_check(JeanX, 1200):
                ch_j "Hey, don't lock that."
            else:
                "You lock the door"
                $ Player.Traits.append("locked")
                call Taboo_Level

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level

        "Sleep." if time_index >= 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Wait." if time_index < 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Return to Your Room" if TravelMode:
            jump Player_Room_Entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call Girls_Room_Entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call Girls_Room_Entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call Girls_Room_Entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call Girls_Room_Entry (LauraX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call Girls_Room_Entry (StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call Girls_Room_Entry (JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    if "angry" in JeanX.recent_history:
        $ JeanX.change_face("angry")
        $ Line = 0
        $ primary_action = 0
        ch_j "Out!"
        "[JeanX.name] shoves you back into the hall and slams the door. You head back to your room."
        jump Player_Room
    jump Jean_Room






label Storm_Room:
    $ bg_current = "bg_storm"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls
    call GirlsAngry


    if StormX.location == bg_current:
        $ Line = "You are in "+StormX.name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+StormX.name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        "Chat":

            call Chat
        "Would you like to study?":

            call Study_Session

        "Lock the door" if "locked" not in Player.Traits:
            if StormX.location == bg_current and not approval_check(StormX, 1000):
                ch_s "I would really prefer you didn't lock the door, [StormX.player_petname]."
            else:
                "You lock the door"
                $ Player.Traits.append("locked")
                call Taboo_Level

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level

        "Sleep." if time_index >= 3 and StormX.location == bg_current:
            call Round10
            call Girls_Location
            call EventCalls

        "Wait." if time_index < 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Return to Your Room" if TravelMode:
            jump Player_Room_Entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call Girls_Room_Entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call Girls_Room_Entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call Girls_Room_Entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call Girls_Room_Entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call Girls_Room_Entry (JeanX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call Girls_Room_Entry (JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    if "angry" in StormX.recent_history:
        $ StormX.change_face("angry")
        ch_s "Out. Now."
        "[StormX.name] pushes you to the top of the stairs and slams the door. You head back to your room."
        $ Line = 0
        $ primary_action = 0
        jump Player_Room
    jump Storm_Room







label Jubes_Room:
    $ bg_current = "bg_jubes"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene (Quiet=1)
    call QuickEvents
    call checkout (1)
    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls
    call GirlsAngry


    if JubesX.location == bg_current:
        $ Line = "You are in "+JubesX.name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+JubesX.name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        "Chat":

            call Chat
        "Would you like to study?":

            call Study_Session

        "Lock the door" if "locked" not in Player.Traits:
            if JubesX.location == bg_current and not approval_check(JubesX, 1000):
                ch_v "You really shouldn't lock -my- door, [JubesX.player_petname]."
            else:
                "You lock the door"
                $ Player.Traits.append("locked")
                call Taboo_Level

        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"
            $ Player.Traits.remove("locked")
            call Taboo_Level

        "Sleep." if time_index >= 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Wait." if time_index < 3:
            call Round10
            call Girls_Location
            call EventCalls

        "Return to Your Room" if TravelMode:
            jump Player_Room_Entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call Girls_Room_Entry (RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call Girls_Room_Entry (KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call Girls_Room_Entry (EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call Girls_Room_Entry (LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call Girls_Room_Entry (JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call Girls_Room_Entry (StormX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    if "angry" in JubesX.recent_history:
        $ JubesX.change_face("angry")
        ch_v "Out!"
        "[JubesX.name] pushes you back into the hall and slams the door. You head back to your room."
        $ Line = 0
        $ primary_action = 0
        jump Player_Room
    jump Jubes_Room
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
