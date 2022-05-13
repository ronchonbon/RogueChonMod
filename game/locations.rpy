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
                "[RogueX.Name]'s Room":
                            call girls_room_entry(RogueX)
                "[KittyX.Name]'s Room" if "met" in KittyX.History:
                            call girls_room_entry(KittyX)
                "[EmmaX.Name]'s Room" if "met" in EmmaX.History:
                            call girls_room_entry(EmmaX)
                "[LauraX.Name]'s Room" if "met" in LauraX.History:
                            call girls_room_entry(LauraX)
                "[JeanX.Name]'s Room" if "met" in JeanX.History:
                            call girls_room_entry(JeanX)
                "[StormX.Name]'s Room" if "met" in StormX.History:
                            call girls_room_entry(StormX)
                "[JubesX.Name]'s Room" if "met" in JubesX.History:
                            call girls_room_entry(JubesX)
                "Back":
                            jump Worldmap
        "University Square":
                    $ renpy.pop_call()
                    jump Campus_Entry
        "Class":
            if Time_Count < 3: #not nighttime
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

        "Go to the mall" if "mall" in Player.History and Time_Count < 3:
                    call Mall_Entry
                    jump Campus

        "Attic" if "attic" in Player.History:
                    jump StormMeet
        "Stay where I am.":
                    return
    return

label Misplaced:
        if Trigger and Trigger in TotalGirls:
                #sent here by a broken sex action, Trigger should be girl's name
                call expression  Trigger.Tag + "_SexMenu"
        #if "Historia" in Player.Traits:
                #call Historia_Clear
        scene onlayer black #removes MindFuck and black screen
        $ Player.DrainWord("locked",0,0,1)
        $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
        while StackDepth > 0:
                $ StackDepth -= 1
                $ renpy.pop_call()
        if bg_current == "bg player":
                jump player_room
        if bg_current == "bg rogue":
                call girls_room(RogueX)
        if bg_current == "bg kitty":
                call girls_room(KittyX)
        if bg_current == "bg emma":
                call girls_room(EmmaX)
        if bg_current == "bg laura":
                call girls_room(LauraX)
        if bg_current == "bg jean":
                call girls_room(JeanX)
        if bg_current == "bg storm":
                call girls_room(StormX)
        if bg_current == "bg jubes":
                call girls_room(JubesX)
        if bg_current == "bg dangerroom":
                jump Danger_Room
        if bg_current == "bg classroom":
                jump Class_Room
        if bg_current == "bg showerroom":
                jump Shower_Room
        if bg_current == "bg study":
                jump Study_Room
        if bg_current == "bg pool":
                jump Pool_Entry
        if bg_current in ("bg mall","bg shop","bg dressing"):
                call Shopping_Mall
                return
        jump Campus

        return

label Campus_Map:
    $ Line = 0
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    $ bg_current = "bg campus"
    $ Player.DrainWord("locked",0,0,1)
    call Set_The_Scene
    if not TravelMode:
        call Worldmap
    jump Campus

label Campus_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg campus"
    $ Nearby = []
    call Gym_Clothes_Off #call Gym_Clothes
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    call EventCalls
    call Set_The_Scene

label Campus:
    $ bg_current = "bg campus"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    call GirlsAngry
    if Time_Count == 2 and "yesdate" in Player.DailyActions: #evening
            #if it's evening and you have a date lined up. . .
            menu:
                "Ready to go on that date?"
                "Yes":
                        call DateNight
                        if "yesdate" in Player.DailyActions:
                                $ Player.DailyActions.remove("yesdate")
                "One moment. . .":
                        pass
    if Round <= 10:
                if Time_Count >= 3: #night time
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
        "Wait." if Time_Count < 3: #not night time
            "You wait around a bit."
            call Wait
            call EventCalls
            call Girls_Location
        "Go to my Room" if TravelMode:
                    jump player_room_entry
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.Name]'s Room":
                            call girls_room_entry(RogueX)
                "[KittyX.Name]'s Room" if "met" in KittyX.History:
                            call girls_room_entry(KittyX)
                "[EmmaX.Name]'s Room" if "met" in EmmaX.History:
                            call girls_room_entry(EmmaX)
                "[LauraX.Name]'s Room" if "met" in LauraX.History:
                            call girls_room_entry(LauraX)
                "[JeanX.Name]'s Room" if "met" in JeanX.History:
                            call girls_room_entry(JeanX)
                "[StormX.Name]'s Room" if "met" in StormX.History:
                            call girls_room_entry(StormX)
                "[JubesX.Name]'s Room" if "met" in JubesX.History:
                            call girls_room_entry(JubesX)
                "Back":
                            pass
        "Go to the classroom" if TravelMode:
                    if Time_Count < 3: #not night time
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
    $ Player.DrainWord("locked",0,0,1)
    $ Nearby = []
    $ bg_current = "bg study"
    call Gym_Clothes_Off #call Gym_Clothes
    call Taboo_Level
    call Set_The_Scene(Entry = 1)
    $ Round -= 5 if Round >= 5 else Round
    menu:
            "You're at the door, what do you do?"
            "Knock politely":
                    $ Line = "knock"

            "Enter without knocking":
                 if Time_Count >= 3: #night time
                         "The door is locked. It's not like you could just walk through it."
                         jump Study_Room_Entry

            "Use the key to enter" if Time_Count >= 3 and "Xavier" in Keys: #night
                    "You use your key."
                    $ Line = 0

            "Ask [KittyX.Name]" if Time_Count >= 3 and KittyX in Party: #night
                    $ Line = "kitty"
            "Ask [StormX.Name]" if Time_Count >= 3 and StormX in Party: #night
                    $ Line = "storm"

            "Leave":
                    "You head back."
                    jump Campus_Map

    if Line == "knock":
        if Time_Count >= 3: #night time
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
                            elif "no thief" in KittyX.RecentActions:
                                ch_k "I told you, no."
                            elif ApprovalCheck(KittyX, 400, "I") or ApprovalCheck(KittyX, 1400):
                                $ KittyX.Statup("Love", 90, 3)
                                $ KittyX.Statup("Obed", 50, 10)
                                $ KittyX.Statup("Inbt", 60, 10)
                                ch_k "Heh, you have a wicked mind. . ."
                                $ KittyX.Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                $ KittyX.Statup("Love", 90, -3)
                                $ KittyX.Statup("Obed", 50, 2)
                                $ KittyX.Statup("Inbt", 60, 2)
                                ch_k "Um, I don't really feel comfortable doing that. . ."
                                $ KittyX.RecentActions.append("no thief")
                    "Open the door.":
                            if "Sneakthief" in KittyX.Traits:
                                ch_k "No problem. . ."
                                jump Study_Room
                            elif "no thief" in KittyX.RecentActions:
                                ch_k "I told you, no."
                            elif ApprovalCheck(KittyX, 500, "O") or ApprovalCheck(KittyX, 1600):
                                $ KittyX.Statup("Obed", 50, 15)
                                $ KittyX.Statup("Inbt", 60, 10)
                                ch_k "Heh, if you say so. . ."
                                $ KittyX.Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                $ KittyX.Statup("Love", 90, -5)
                                $ KittyX.Statup("Obed", 50, 2)
                                $ KittyX.Statup("Inbt", 60, 2)
                                ch_k "Um, no."
                                $ KittyX.RecentActions.append("no thief")
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
                            if "no thief" in StormX.RecentActions:
                                ch_s "I told you, I won't do that."
                            elif ApprovalCheck(StormX, 400, "I") or ApprovalCheck(StormX, 1400):
                                $ StormX.Statup("Love", 90, 3)
                                $ StormX.Statup("Obed", 80, 10)
                                $ StormX.Statup("Inbt", 60, 10)
                                $ StormX.FaceChange("sly")
                                ch_s "Oh, this should be interesting. . ."
                                "She pulls some picks from behind her ear."
                                ch_s "Ok, we've got a click on 1. . . 2 is binding. . ."
                                ch_s "Click on 3. . . 4. . . click on 5, back to 2. . . and we're in."
                                $ StormX.Traits.append("Sneakthief")
                                $ StormX.FaceChange("normal")
                                jump Study_Room
                            else:
                                $ StormX.Statup("Love", 90, -3)
                                $ StormX.Statup("Obed", 50, 2)
                                $ StormX.Statup("Inbt", 60, 2)
                                ch_s "I don't think that's really appropriate behavior. . ."
                                $ StormX.RecentActions.append("no thief")
                    "Could you pick the lock again?" if "Sneakthief" in StormX.Traits:
                                ch_s "No problem. . ."
                                jump Study_Room
                    "Never mind. [[Leave]":
                            "You head back."
                            jump Campus_Map
            jump Study_Room_Entry

    elif Time_Count < 3: #not night time
            ch_x "You know, [Player.Name], it is not polite to enter a room unannounced."
    $ Cnt = 0

label Study_Room:
    $ bg_current = "bg study"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
            if Time_Count >= 3: #night time
                "It's late, you head back to your room."
                jump player_room
            else:
                call Wait
                call Girls_Location

    call GirlsAngry
    call XavierFace("happy")

    if Time_Count >= 3: # night time
        $ Line = "You are in Xavier's Study, but he isn't in at the moment. What would you like to do?"
    else:
        $ Line = "You are in Xavier's Study. What would you like to do?"
    menu:
        "[Line]"
        "Chat" if Time_Count >= 3: #night time #fix, open up once sex while in office is fine
                    call Chat

        "Plan Omega!" if Time_Count < 3 and RogueX.Loc == bg_current and Player.Lvl >= 5:
                    if ApprovalCheck(RogueX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(RogueX) #Plan_Omega
                    else:
                        ch_r "I don't want to do that. . ."
        "Plan Kappa!" if Time_Count < 3 and KittyX.Loc == bg_current and Player.Lvl >= 5:
                    if "Xavier's photo" in Player.Inventory and ApprovalCheck(KittyX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(KittyX) #Plan_Kappa
                    elif "Xavier's photo" in Player.Inventory:
                        ch_k "I don't really want to do that. . ."
                    else:
                        ch_k "What?"
        "Plan Psi!" if Time_Count < 3 and EmmaX.Loc == bg_current and Player.Lvl >= 5:
                    if ApprovalCheck(EmmaX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(EmmaX) #Plan_Psi
                    else:
                        ch_e "I'd rather not. . ."
        "Plan Chi!" if Time_Count < 3 and LauraX.Loc == bg_current and Player.Lvl >= 5:
                    if LauraX.Lvl >= 2 and ApprovalCheck(LauraX, 1500, TabM=1, Loc="No") and ApprovalCheck(LauraX, 750, "I"):
                        call Xavier_Plan(LauraX) #Plan_Chi
                    elif LauraX.Lvl < 2 or not ApprovalCheck(LauraX, 750, "I"):
                        ch_l "I'm not ready for that."
                    else:
                        ch_l "Huh?"
        "Plan Alpha!" if Time_Count < 3 and JeanX.Loc == bg_current and Player.Lvl >= 5:
                    if ApprovalCheck(JeanX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(JeanX) #Plan_Chi
                    else:
                        ch_j "You're on your own there."
        "Plan Rho!" if Time_Count < 3 and StormX.Loc == bg_current and Player.Lvl >= 5:
                    if "Xavier's files" in Player.Inventory and ApprovalCheck(StormX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(StormX) #Plan_Rho
                    elif "Xavier's files" in Player.Inventory:
                        ch_s "I do not believe that would be approrpriate."
                    else:
                        ch_s "What is that?"
        "Plan Zeta!" if Time_Count < 3 and JubesX.Loc == bg_current and Player.Lvl >= 5:
                    if ApprovalCheck(JubesX, 1500, TabM=1, Loc="No"):
                        call Xavier_Plan(JubesX) #Plan_Zeta
                    else:
                        ch_v "What's a \"Zeta?\""
        "Explore" if Time_Count >= 3 and "explore" not in Player.RecentActions:
                    $ Cnt = 0
                    $ Player.RecentActions.append("explore")
                    jump Study_Room_Explore

        "Wait":
                    if Time_Count >= 3: #night time
                            "You probably don't want to be here when Xavier gets in."
                    elif Time_Count >=2: #evening time
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
    $ Line = 0
    $ D20 = renpy.random.randint(1, 20)
    menu:
        "Where would you like to look?"
        "Bookshelf":
            if D20 >= 5 + Cnt:
                    $ Line = "book"
            else:
                    "As you search the bookshelf, you accidentally knock one of the books off."
                    "It hammers against the floor, and a little light blinks on the desk."
        "Left Desk Drawer":
            if KittyX.Loc != bg_current and StormX.Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 10 + Cnt:
                    $ Line = "left"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Middle Desk Drawer":
            if KittyX.Loc != bg_current and StormX.Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 15 + Cnt:
                    $ Line = "mid"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Right Desk Drawer":
            if KittyX.Loc != bg_current and StormX.Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 5 + Cnt:
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
                if KittyX.Loc == bg_current:
                    menu:
                        "Since [KittyX.Name] is around, have her check inside?"
                        "Check in the box":
                            if ApprovalCheck(KittyX, 700, "I") or ApprovalCheck(KittyX, 1800):
                                if "Well Studied" not in Achievements:
                                        $ KittyX.Statup("Obed", 50, 10)
                                        $ KittyX.Statup("Inbt", 60, 15)
                                        ch_k "Sounds like a plan."
                                        "[KittyX.Name] swipes her hand through the box, and pulls out a stack of bills."
                                        "Looks like Xavier was hiding a rainy day fund in here."
                                        $ Player.Cash += 500
                                        "[[$500 acquired.]"
                                        $ Achievements.append("Well Studied")
                                else:
                                        "Looks like this has been thoroughly looted."
                            else:#Kitty doesn't approve
                                $ KittyX.Statup("Love", 90, -3)
                                $ KittyX.Statup("Obed", 50, 1)
                                $ KittyX.Statup("Inbt", 60, 2)
                                ch_k "I really don't think we should do that."
                        "Put it back.":
                            "You place the box back on the shelf."
                elif StormX.Loc == bg_current:
                    menu:
                        "Since [StormX.Name] is around, have her check inside?"
                        "Check in the box":
                            if ApprovalCheck(StormX, 700, "I") or ApprovalCheck(StormX, 1800):
                                if "Well Studied" not in Achievements:
                                        $ StormX.Statup("Obed", 50, 10)
                                        $ StormX.Statup("Inbt", 60, 15)
                                        ch_s "I suppose I could. . ."
                                        "[StormX.Name] picks the lock on the box, and pulls out a stack of bills."
                                        "Looks like Charles had some money set aside. . ."
                                        $ Player.Cash += 500
                                        "[[$500 acquired.]"
                                        $ Achievements.append("Well Studied")
                                else:
                                        "Looks like this has been thoroughly looted."
                            else:#Storm doesn't approve
                                $ StormX.Statup("Love", 90, -3)
                                $ StormX.Statup("Obed", 50, 1)
                                $ StormX.Statup("Inbt", 60, 2)
                                ch_s "I really don't think we should do that."
                        "Put it back.":
                            "You place the box back on the shelf."
                else:#[KittyX.Name]'s not there
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
                        if StormX.Loc == bg_current:
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
                        if StormX.Loc == bg_current:
                                ch_s "Hmm. . ."
                                "She reaches under some of the documents and finds a small notch."
                                "With a soft \"click\"a panel flips open in the drawer, revealing some file folders."
                                "Inside are some fairly. . . detailed reports on the girls at the school."
                                $ StormX.FaceChange("surprised",2)
                                "These include body measurements, sexual histories. . . masturbation habits?"
                                $ StormX.Statup("Obed", 70, 5)
                                $ StormX.Statup("Inbt", 70, 5)
                                $ StormX.FaceChange("angry")
                                ch_s "Well, I don't think Charles should be holding information like this. . ."
                                $ StormX.FaceChange("normal",1)
                                "[[Xavier's files acquired.]"
                                $ Player.Inventory.append("Xavier's files")
                                if "rho" in Player.History:
                                        $ Player.History.remove("rho")
                else:
                        "You search through some documents, but don't find anything."
                        "It would probably take a more thorough search."
            else:
                        "There doesn't seem to be anything more of interest in here."

    $ Cnt += 3
    jump Study_Room_Explore
