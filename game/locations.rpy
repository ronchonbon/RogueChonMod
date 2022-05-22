

label Worldmap:
    $ Taboo = 0
    menu:
        "Where would you like to go?"
        "My Room":
            $ renpy.pop_call()
            jump player_room_entry
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
            jump Campus_entry
        "Class":
            if time_index < 3:
                $ renpy.pop_call()
                jump Class_Room_entry
            elif "Xavier" in Keys:
                "The door is locked, but you were able to use Xavier's key to get in."
                $ renpy.pop_call()
                jump Class_Room_entry
            else:
                "It's late for classes and the classrooms are locked down."
                jump Worldmap
        "The Danger Room":
            $ renpy.pop_call()
            jump Danger_Room_entry
        "The showers":
            $ renpy.pop_call()
            jump Shower_Room_entry
        "The pool":
            $ renpy.pop_call()
            jump Pool_entry
        "Xavier's Study":
            $ renpy.pop_call()
            jump Study_Room_entry

        "Go to the mall" if "mall" in Player.history and time_index < 3:
            call Mall_entry
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
        jump Pool_entry
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
    call Jubes_entry_Check
    $ Player.drain_word("locked",0,0,1)
    $ bg_current = "bg_campus"
    $ Nearby = []
    call Gym_Clothes_Off
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    call event_calls
    call set_the_scene

label Campus:
    $ bg_current = "bg_campus"
    $ Player.drain_word("traveling",1,0)
    call Taboo_Level
    call set_the_scene (silent=1)
    call QuickEvents
    call checkout (1)
    call GirlsAngry
    if time_index == 2 and "going_on_date" in Player.daily_history:

        menu:
            "Ready to go on that date?"
            "Yes":
                call DateNight
                if "going_on_date" in Player.daily_history:
                    $ Player.daily_history.remove("going_on_date")
            "One moment. . .":
                pass
    if round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."
            jump player_room
        call wait
        call event_calls
        call girls_location



    menu:
        "You are in the university square. What would you like to do?"
        "Chat":

            call Chat

        "wait." if time_index < 3:
            "You wait around a bit."
            call wait
            call event_calls
            call girls_location

        "Go to my Room" if TravelMode:
            jump player_room_entry
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
                jump Class_Room_entry
            elif "Xavier" in Keys:
                "The door is locked, but you were able to use Xavier's key to get in."
                jump Class_Room_entry
            else:
                "It's late for classes and the classrooms are locked down."
        "Go to the Danger Room" if TravelMode:
            jump Danger_Room_entry
        "Go to the showers" if TravelMode:
            jump Shower_Room_entry
        "Go to the pool" if TravelMode:
            jump Pool_entry
        "Xavier's Study" if TravelMode:
            jump Study_Room_entry
        "Go to the mall" if TravelMode and "mall" in Player.history:
            call Mall_entry

        "Leave" if not TravelMode:
            call Worldmap

    jump Campus










label Danger_Room_entering:
    call Jubes_entry_Check
    $ Player.drain_word("locked",0,0,1)
    $ bg_current = "bg_dangerroom"
    $ Nearby = []
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    $ round -= 5 if round >= 5 else round
    call event_calls
    call Gym_entry
    call set_the_scene

label Danger_Room:
    $ bg_current = "bg_dangerroom"
    $ Player.drain_word("traveling",1,0)
    call Taboo_Level
    call set_the_scene (silent=1)
    call QuickEvents
    call checkout (1)
    if round <= 10:
        "Looks like shifts are changing. . ."
        if time_index >=3:
            "You're getting tired, you head back to your room."
            jump player_room
        call wait
        call event_calls
        call girls_location
        call Gym_Clothes_Off
    call GirlsAngry



    menu:
        "This is the Danger Room. What would you like to do?"
        "Train":

            if time_index >= 3:
                "The Danger Room has been powered off for the night, maybe take a break."
            elif round >= 30:
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

        "wait. (locked)" if time_index >= 3:
            pass
        "wait." if time_index < 3:
            "You hang out for a bit."
            call wait
            call event_calls
            call girls_location
            call Gym_Clothes_Off

        "Leave" if not TravelMode:
            call Gym_Exit
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            call Gym_Exit
            jump Campus_entry

        "Go to the showers" if TravelMode:
            call Gym_Exit
            jump Shower_Room_entry
    jump Danger_Room

label Training:
    $ D20 = renpy.random.randint(1, 20)



    $ Player.XP += (5 + (int(round / 10)))
    $ Player.daily_history.append("dangerroom")
    call set_the_scene

    if round >= 80:
        $ Line = "You have a long session in the Danger Room."
    elif round >= 50:
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
    call wait
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
            call remove_girl (RogueX)
            $ RogueX.change_outfit()

    return











label Study_Room_entering:
    call Jubes_entry_Check
    $ Player.drain_word("locked",0,0,1)
    $ Nearby = []
    $ bg_current = "bg_study"
    call Gym_Clothes_Off
    call Taboo_Level
    call set_the_scene (Entry=1)
    $ round -= 5 if round >= 5 else round
    menu:
        "You're at the door, what do you do?"
        "Knock politely":
            $ Line = "knock"
        "Enter without knocking":

            if time_index >= 3:
                "The door is locked. It's not like you could just walk through it."
                jump Study_Room_entry

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
            jump Study_Room_entry
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
        jump Study_Room_entry
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
        jump Study_Room_entry

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
    if round <= 10:
        if time_index >= 3:
            "It's late, you head back to your room."
            jump player_room
        else:
            call wait
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
        "wait":

            if time_index >= 3:
                "You probably don't want to be here when Xavier gets in."
            elif time_index >=2:
                ch_x "If you don't mind, I would like to close up for the evening?"
                "You return to your room."
                jump player_room
            else:
                call wait
                call girls_location
                ch_x "Not that I mind the company, but is there something I can do for you?"

        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_entry
        "Return to Your Room" if TravelMode:
            jump player_room_entry

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
        jump player_room_entry
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
