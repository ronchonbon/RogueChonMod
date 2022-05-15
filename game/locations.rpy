label Worldmap:
    scene bg_campus onlayer backdrop
    scene
    $ Taboo = 0
    menu:
        "Where would you like to go?"
        "My Room":
                    $ renpy.pop_call()
                    jump player_room_entry
        "Testbed" if config.developer:
                    $ renpy.pop_call()
                    jump Rogue_Room_Test
        "Girl's Rooms":
            menu:
                "[RogueX.name]'s Room":
                            call girls_room_entry(RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.History:
                            call girls_room_entry(KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.History:
                            call girls_room_entry(EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.History:
                            call girls_room_entry(LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.History:
                            call girls_room_entry(JeanX)
                "[StormX.name]'s Room" if "met" in StormX.History:
                            call girls_room_entry(StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.History:
                            call girls_room_entry(JubesX)
                "Back":
                            jump Worldmap
        "University Square":
                    $ renpy.pop_call()
                    jump Campus_Entry
        "Class":
            if time_index < 3: #not nighttime
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

        "Go to the mall" if "mall" in Player.History and time_index < 3:
                    call Mall_Entry
                    jump Campus

        "Attic" if "attic" in Player.History:
                    jump StormMeet
        "Stay where I am.":
                    return
    return

label Misplaced:
        if primary_action and primary_action in all_Girls:
                #sent here by a broken sex action, primary_action should be girl's name
                call expression  primary_action.Tag + "_SexMenu"
        #if simulation:
                #call clear_simulation
        scene onlayer black #removes MindFuck and black screen
        $ door_locked = False
        $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
        while StackDepth > 0:
                $ StackDepth -= 1
                $ renpy.pop_call()
        if bg_current == "bg_player":
                jump player_room
        if bg_current == "bg_rogue":
                call girls_room(RogueX)
        if bg_current == "bg_kitty":
                call girls_room(KittyX)
        if bg_current == "bg_emma":
                call girls_room(EmmaX)
        if bg_current == "bg_laura":
                call girls_room(LauraX)
        if bg_current == "bg_jean":
                call girls_room(JeanX)
        if bg_current == "bg_storm":
                call girls_room(StormX)
        if bg_current == "bg_jubes":
                call girls_room(JubesX)
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
    $ line = 0
    $ primary_action = 0
    $ offhand_action = 0
    $ girl_offhand_action = 0
    $ Partner_primary_action = 0
    $ Partner_offhand_action = 0
    $ bg_current = "bg_campus"
    $ door_locked = False
    call set_the_scene
    if not TravelMode:
        call Worldmap
    jump Campus

label Campus_Entry:
    call Jubes_Entry_Check
    $ door_locked = False
    $ bg_current = "bg_campus"
    $ Nearby = []
    call Gym_Clothes_Off #call Gym_Clothes
    call Taboo_Level
    $ Player.recent_history.append("traveling")
    call EventCalls
    call set_the_scene

label Campus:
    $ bg_current = "bg_campus"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    call GirlsAngry
    if time_index == 2 and "yesdate" in Player.daily_history: #evening
            #if it's evening and you have a date lined up. . .
            menu:
                "Ready to go on that date?"
                "Yes":
                        call DateNight
                        if "yesdate" in Player.daily_history:
                                $ Player.daily_history.remove("yesdate")
                "One moment. . .":
                        pass
    if Round <= 10:
                if time_index >= 3: #night time
                    "You're getting tired, you head back to your room."
                    jump player_room
                call Wait
                call EventCalls
                call Girls_Location
    #End date code

    menu:
        "You are in the university square. What would you like to do?"

        "Chat":
            call Chat
        "Wait." if time_index < 3: #not night time
            "You wait around a bit."
            call Wait
            call EventCalls
            call Girls_Location
        "Go to my Room" if TravelMode:
                    jump player_room_entry
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                            call girls_room_entry(RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.History:
                            call girls_room_entry(KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.History:
                            call girls_room_entry(EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.History:
                            call girls_room_entry(LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.History:
                            call girls_room_entry(JeanX)
                "[StormX.name]'s Room" if "met" in StormX.History:
                            call girls_room_entry(StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.History:
                            call girls_room_entry(JubesX)
                "Back":
                            pass
        "Go to the classroom" if TravelMode:
                    if time_index < 3: #not night time
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
        "Go to the mall" if TravelMode and "mall" in Player.History:
                    call Mall_Entry

        "Leave" if not TravelMode:
                    call Worldmap

    jump Campus

label Study_Room_Entry:
    call Jubes_Entry_Check
    $ door_locked = False
    $ Nearby = []
    $ bg_current = "bg_study"
    call Gym_Clothes_Off #call Gym_Clothes
    call Taboo_Level
    call set_the_scene(Entry = 1)
    $ Round -= 5 if Round >= 5 else Round
    menu:
            "You're at the door, what do you do?"
            "Knock politely":
                    $ line = "knock"

            "Enter without knocking":
                 if time_index >= 3: #night time
                         "The door is locked. It's not like you could just walk through it."
                         jump Study_Room_Entry

            "Use the key to enter" if time_index >= 3 and "Xavier" in Keys: #night
                    "You use your key."
                    $ line = 0

            "Ask [KittyX.name]" if time_index >= 3 and KittyX in Party: #night
                    $ line = "kitty"
            "Ask [StormX.name]" if time_index >= 3 and StormX in Party: #night
                    $ line = "storm"

            "Leave":
                    "You head back."
                    jump Campus_Map

    if line == "knock":
        if time_index >= 3: #night time
            "There's no answer, he's probably asleep."
            jump Study_Room_Entry
        else:
            ch_x "Yes, enter. . ."
            "You enter the room."
    elif line == "kitty":
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
                            elif ApprovalCheck(KittyX, 400, "I") or ApprovalCheck(KittyX, 1400):
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
                            elif ApprovalCheck(KittyX, 500, "O") or ApprovalCheck(KittyX, 1600):
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
    elif line == "storm":
            ch_s "What is it?"
            while True:
                menu:
                    extend ""
                    "Do you think you could pick that lock?" if "Sneakthief" not in StormX.Traits:
                            if "no_thief" in StormX.recent_history:
                                ch_s "I told you, I won't do that."
                            elif ApprovalCheck(StormX, 400, "I") or ApprovalCheck(StormX, 1400):
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

    elif time_index < 3: #not night time
            ch_x "You know, [Player.name], it is not polite to enter a room unannounced."
    $ counter = 0

label Study_Room:
    $ bg_current = "bg_study"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
            if time_index >= 3: #night time
                "It's late, you head back to your room."
                jump player_room
            else:
                call Wait
                call Girls_Location

    call GirlsAngry
    call XavierFace("happy")

    if time_index >= 3: # night time
        $ line = "You are in Xavier's Study, but he isn't in at the moment. What would you like to do?"
    else:
        $ line = "You are in Xavier's Study. What would you like to do?"
    menu:
        "[line]"
        "Chat" if time_index >= 3: #night time #fix, open up once sex while in office is fine
                    call Chat

        "Plan Omega!" if time_index < 3 and RogueX.location == bg_current and Player.Lvl >= 5:
                    if ApprovalCheck(RogueX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(RogueX) #Plan_Omega
                    else:
                        ch_r "I don't want to do that. . ."
        "Plan Kappa!" if time_index < 3 and KittyX.location == bg_current and Player.Lvl >= 5:
                    if "Xavier's photo" in Player.Inventory and ApprovalCheck(KittyX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(KittyX) #Plan_Kappa
                    elif "Xavier's photo" in Player.Inventory:
                        ch_k "I don't really want to do that. . ."
                    else:
                        ch_k "What?"
        "Plan Psi!" if time_index < 3 and EmmaX.location == bg_current and Player.Lvl >= 5:
                    if ApprovalCheck(EmmaX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(EmmaX) #Plan_Psi
                    else:
                        ch_e "I'd rather not. . ."
        "Plan Chi!" if time_index < 3 and LauraX.location == bg_current and Player.Lvl >= 5:
                    if LauraX.Lvl >= 2 and ApprovalCheck(LauraX, 1500, TabM=1, Loc="No") and ApprovalCheck(LauraX, 750, "I"):
                        call Xavier_Plan(LauraX) #Plan_Chi
                    elif LauraX.Lvl < 2 or not ApprovalCheck(LauraX, 750, "I"):
                        ch_l "I'm not ready for that."
                    else:
                        ch_l "Huh?"
        "Plan Alpha!" if time_index < 3 and JeanX.location == bg_current and Player.Lvl >= 5:
                    if ApprovalCheck(JeanX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(JeanX) #Plan_Chi
                    else:
                        ch_j "You're on your own there."
        "Plan Rho!" if time_index < 3 and StormX.location == bg_current and Player.Lvl >= 5:
                    if "Xavier's files" in Player.Inventory and ApprovalCheck(StormX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(StormX) #Plan_Rho
                    elif "Xavier's files" in Player.Inventory:
                        ch_s "I do not believe that would be approrpriate."
                    else:
                        ch_s "What is that?"
        "Plan Zeta!" if time_index < 3 and JubesX.location == bg_current and Player.Lvl >= 5:
                    if ApprovalCheck(JubesX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(JubesX) #Plan_Zeta
                    else:
                        ch_v "What's a \"Zeta?\""
        "Explore" if time_index >= 3 and "explore" not in Player.recent_history:
                    $ counter = 0
                    $ Player.recent_history.append("explore")
                    jump Study_Room_Explore

        "Wait":
                    if time_index >= 3: #night time
                            "You probably don't want to be here when Xavier gets in."
                    elif time_index >=2: #evening time
                            ch_x "If you don't mind, I would like to close up for the evening?"
                            "You return to your room."
                            jump player_room
                    else:
                            call Wait
                            call Girls_Location
                            ch_x "Not that I mind the company, but is there something I can do for you?"

        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
        "Return to Your Room" if TravelMode:
                    jump player_room_entry

    jump Study_Room

label Study_Room_Explore:
    $ line = 0
    $ D20 = renpy.random.randint(1, 20)
    menu:
        "Where would you like to look?"
        "Bookshelf":
            if D20 >= 5 + counter:
                    $ line = "book"
            else:
                    "As you search the bookshelf, you accidentally knock one of the books off."
                    "It hammers against the floor, and a little light blinks on the desk."
        "Left Desk Drawer":
            if KittyX.location != bg_current and StormX.location != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 10 + counter:
                    $ line = "left"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Middle Desk Drawer":
            if KittyX.location != bg_current and StormX.location != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 15 + counter:
                    $ line = "mid"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Right Desk Drawer":
            if KittyX.location != bg_current and StormX.location != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 5 + counter:
                    $ line = "right"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Never mind [[back]":
                    jump Study_Room

    $ D20 = renpy.random.randint(1, 20)
    if not line:
                "Probably best to get out of here."
                "You slip out and head back to your room."
                jump player_room_entry
    elif line == "book":
            if D20 >= 15 and "Well Studied" not in Achievements:
                "As you check the books on the shelf, you notice that one of them is actually a disguised lockbox."
                if KittyX.location == bg_current:
                    menu:
                        "Since [KittyX.name] is around, have her check inside?"
                        "Check in the box":
                            if ApprovalCheck(KittyX, 700, "I") or ApprovalCheck(KittyX, 1800):
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
                            else:#Kitty doesn't approve
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
                            if ApprovalCheck(StormX, 700, "I") or ApprovalCheck(StormX, 1800):
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
                            else:#Storm doesn't approve
                                $ StormX.change_stat("love", 90, -3)
                                $ StormX.change_stat("obedience", 50, 1)
                                $ StormX.change_stat("inhibition", 60, 2)
                                ch_s "I really don't think we should do that."
                        "Put it back.":
                            "You place the box back on the shelf."
                else:#[KittyX.name]'s not there
                            "You can't think of any way to get it open, too bad you aren't a ghost or something."
                            "You place the box back on the shelf."
            elif D20 >= 15:
                "There doesn't seem to be anything more of interest in here."
            else:
                "You search through the books for a few minutes, but don't find anything."
                "It would probably take a more thorough search."
    elif line == "left":
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
                                if "kappa" in Player.History:
                                        $ Player.History.remove("kappa")
                else:
                        "You search through some documents, but don't find anything."
                        "It would probably take a more thorough search."
            else:
                        "There doesn't seem to be anything more of interest in here."
    elif line == "mid":
            if "all" not in Keys:
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
                if "all" not in Keys:
                        $ Keys.append("all")
            else:
                "There doesn't seem to be anything interesting in here."
    elif line == "right":
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
                                if "rho" in Player.History:
                                        $ Player.History.remove("rho")
                else:
                        "You search through some documents, but don't find anything."
                        "It would probably take a more thorough search."
            else:
                        "There doesn't seem to be anything more of interest in here."

    $ counter += 3
    jump Study_Room_Explore
