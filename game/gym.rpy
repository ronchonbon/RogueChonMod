label Gym_Entry(BO=[],GirlsNum = 0):  #rkeljsv
        if Taboo == 0 and bg_current == "bg dangerroom":
            menu:
                "Is this visit for work or for play?"
                "Work [[get geared up]":
                        pass
                "Play [[keep on this outfit]":
                        return
        $ BO = TotalGirls[:]
        while BO:
                #while there are still girls to do or the Mode is exit. . .
                if BO[0].Loc != "bg dangerroom" and BO[0].Outfit == "gym":
                                #If she isn't in the dangerroom, switch to her day clothes
                                $ BO[0].Outfit = BO[0].OutfitDay
                elif BO[0].Outfit == "gym":
                                #If she's already in gym clothes, skip this
                                pass
                elif BO[0].Loc == "bg dangerroom" and BO[0] not in Party:
                                #If she was already here
                                $ BO[0].Outfit = "gym"
                $ BO.remove(BO[0])
        call Set_The_Scene
        $ BO = Present[:]
        while BO:
                if BO[0].Outfit != "gym":
                        #If girl is in the gym, see if she'll change clothes
                        if ApprovalCheck(BO[0], 1300, "LO") or "passive" in BO[0].Traits:
                            pass
                        elif ApprovalCheck(BO[0], 800, "LO") and BO[0].Custom1[0]:
                            pass
                        elif ApprovalCheck(BO[0], 600, "LO") and BO[0].Gym[0] != 1:
                            pass
                        else:
                            $ Line = "no"

                        if Line == "no" or "asked gym" in BO[0].DailyActions or "no ask gym" in BO[0].Traits:
                                #If she decides not to ask you
                                show blackscreen onlayer black
                                if BO[0] == EmmaX:
                                        ch_e "I should change too."
                                elif BO[0] == LauraX:
                                        ch_l "I'll be right back. . ."
                                elif BO[0] == StormX:
                                        ch_s "I should change as well. . ."
                                else:
                                    if GirlsNum:
                                            call AnyLine(BO[0],"I'll be right back too.")
                                    else:
                                            call AnyLine(BO[0],"I'll be back soon, gotta change.")
                                $ BO[0].Outfit = "gym"
                        else:
                                # She asks to change outfits
                                $ BO[0].DailyActions.append("asked gym")
                                if GirlsNum:
                                    #if the second girl to ask. . .
                                    if BO[0] == EmmaX:
                                            $ Line = "Do you think I should change as well?"
                                    elif BO[0] == LauraX:
                                            $ Line = "Did you want me to change into my gym clothes?"
                                    elif BO[0] == StormX:
                                            $ Line = "Do you think I should change as well?"
                                    else:
                                            $ Line = "Should I change too?"
                                else:
                                    if BO[0] == EmmaX:
                                            $ Line = "Did you want me to change into my gear?"
                                    elif BO[0] == LauraX:
                                            $ Line = "Did you want me to change into my gym clothes?"
                                    elif BO[0] == StormX:
                                            $ Line = "Do you think I should change into my gym clothes?"
                                    else:
                                            $ Line = "Would you like me to change into my gym clothes?"
                                call AnyLine(BO[0],Line)
                                menu:
                                        extend ""
                                        "Yeah, they look great.":
                                                    $ BO[0].FaceChange("smile")
                                                    $ BO[0].Statup("Love", 80, 2)
                                                    $ BO[0].Statup("Obed", 40, 1)
                                                    $ BO[0].Statup("Inbt", 30, 1)
                                                    $ Line = 1
                                        "No, stay in that.":
                                                    $ BO[0].FaceChange("confused")
                                                    $ BO[0].Statup("Obed", 50, 5)
                                                    $ Line = 0
                                        "Whichever you like.":
                                                    $ BO[0].FaceChange("confused")
                                                    $ BO[0].Statup("Inbt", 50, 1)
                                                    $ Line = renpy.random.randint(0, 3)
                                        "I don't care.":
                                                    $ BO[0].FaceChange("angry")
                                                    $ BO[0].Statup("Love", 50, -3, 1)
                                                    $ BO[0].Statup("Obed", 50, 4)
                                                    $ BO[0].Statup("Inbt", 50, 2)
                                                    $ Line = renpy.random.randint(0, 1)
                                if Line:
                                        #If she decided to change
                                        if BO[0] == RogueX:
                                                ch_r "Ok, be right back."
                                        elif BO[0] == KittyX:
                                                ch_k "Ok, back in a bit."
                                        elif BO[0] == EmmaX:
                                                ch_e "Fine, I'll be right back."
                                        elif BO[0] == LauraX:
                                                ch_l "I'll be right back then."
                                        elif BO[0] == StormX:
                                                ch_s "Then I will return shortly."
                                        elif BO[0] == JubesX:
                                                ch_v "K, be right back."
                                        $ BO[0].Outfit = "gym"
                                # End She asks to change outfits
                        if BO[0].Outfit == "gym":
                                $ GirlsNum += 1
                        $ Line = 0
                        # End She isn't already in gym clothes
                $ BO.remove(BO[0])
                # End if BO[0].Outfit != "gym":

        $ BO = TotalGirls[:]
        while BO:
                #loops through and makes choices.
                $ BO[0].OutfitChange()
                $ BO.remove(BO[0])
        hide blackscreen onlayer black
        return

label Gym_Exit(BO=[]):  #rkeljsv
        #Called when you leave the gym, puts girls in their day clothes
        # call with "call Gym_Exit([RogueX]) " for a specific girl only
        if BO and BO[0] in TotalGirls:
                pass
        else:
                $ BO = Party[:]
        while BO:
                if BO[0].Outfit == "gym":
                        #if they are in gym clothes, they tell you they'll change
                        if len(Party) > 1:
                                $ Line = "We should change out of these if we're leaving. . ."
                        else:
                                $ Line = "I should change out of these if we're leaving. . ."
                        $ BO[0].Outfit = BO[0].OutfitDay
                $ BO.remove(BO[0])
        if Party:
                call AnyLine(Party[0],Line)
        if Line:
            show blackscreen onlayer black with dissolve
            $ BO = Party[:]
            while BO:
                    #then they will change
                    $ BO[0].OutfitChange()
                    $ BO.remove(BO[0])
            $ Line = 0
            hide blackscreen onlayer black
        return

label Gym_Clothes_Off(BO=[]):  #rkeljsv
        #Called when time changes and girls leave the Gym, puts girls in their day clothes
        if BO and BO[0] in TotalGirls:
                pass
        else:
                $ BO = TotalGirls[:]
        while BO: #or Mode == "exit"?
                #while there are still girls to do or the Mode is exit. . .
                if BO[0] not in Party:
                    if BO[0].Outfit == "gym" and BO[0].Loc != "bg dangerroom":
                            $ BO[0].Outfit = BO[0].OutfitDay
                    elif BO[0].Loc == "bg dangerroom":
                            $ BO[0].Outfit = "gym"
                $ BO.remove(BO[0])
        return

label Danger_Room_Entry:
    call Jubes_Entry_Check
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg dangerroom"
    $ Nearby = []
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    $ Round -= 5 if Round >= 5 else Round
    call EventCalls
    call Gym_Entry #call Gym_Clothes("pre")#Automatically puts them in gym clothes if they've been here
    call Set_The_Scene

label Danger_Room:
    $ bg_current = "bg dangerroom"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                "Looks like shifts are changing. . ."
                if Time_Count >=3: # night time
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait
                call EventCalls
                call Girls_Location
                call Gym_Clothes_Off #call Gym_Clothes
    call GirlsAngry
    #End Room Set-up

    menu:
        "This is the Danger Room. What would you like to do?"
        "Train":
                if Time_Count >= 3: #night time
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
                    #call Danger_Room_Historia

        "Lock the door" if "locked" not in Player.Traits:
                    if Time_Count >= 3: #night time
                            "You lock the door"
                            $ Player.Traits.append("locked")
                            call Taboo_Level
                    else:
                            "You can't really do that during free hours."

        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Wait. (locked)" if Time_Count >= 3: #night time
                    pass
        "Wait." if Time_Count < 3: #not night time
                    "You hang out for a bit."
                    call Wait
                    call EventCalls
                    call Girls_Location
                    call Gym_Clothes_Off #call Gym_Clothes

        "Leave" if not TravelMode:
                    call Gym_Exit  #call Gym_Clothes("change")
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    call Gym_Exit  #call Gym_Clothes("change")
                    jump Campus_Entry

        "Go to the showers" if TravelMode:
                    call Gym_Exit  #call Gym_Clothes("change")
                    jump Shower_Room_Entry
    jump Danger_Room

label Training:
    $ D20 = renpy.random.randint(1, 20)

    $ Player.XP += (5 + (int(Round / 10)))
    $ Player.DailyActions.append("dangerroom")
    call Set_The_Scene

    if Round >= 80:
            $ Line = "You have a long session in the Danger Room."
    elif Round >= 50:
            $ Line = "You have a short workout in the Danger Room."
    else:
            $ Line = "You squeeze in a quick session in the Danger Room."

    $ Trigger = 0
    if D20 >= 18:
            #if "cyclops":
            "[Line] During the exercise, Cyclops accidentally shoots you."
            "Luckily you're immune to the beams, but your clothes weren't so lucky."
            call RoomStatboost("Love",80,2)
            call RoomStatboost("Lust",80,5)
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

    $ Options = ActiveGirls[:]
    while Options:
            #Runs through all active girls, if they are in the room, checks to see if their hose were ripped.
            if Options[0].Loc == bg_current:
                    call Girl_TightsRipped(Options[0])
            $ Options.remove(Options[0])
    call Wait
    call Girls_Location
    call Set_The_Scene
    $ Line = "The training session has ended, what would you like to do next?"

    jump Danger_Room

label Rogue_TightsRipped(Count = 0):
        if RogueX.Hose == "tights":
                $ Count = 1
                $ RogueX.Hose = "ripped tights"
                $ RogueX.FaceChange("angry")
                if "ripped tights" in RogueX.Inventory:
                    ch_r "Damnation, that's another pair ruined!"
                else:
                    $ Count = 2
                    ch_r "Well that's a good pair of tights down the chute."
        elif RogueX.Hose == "pantyhose":
                $ Count = 1
                $ RogueX.Hose = "ripped pantyhose"
                $ RogueX.FaceChange("angry")
                if "ripped pantyhose" in RogueX.Inventory:
                    ch_r "Tsk, another pair ruined!"
                else:
                    $ Count = 2
                    ch_r "I hate getting a run in these things."
        if Count:
                #If they ripped
                if not RogueX.Legs and RogueX.Panties != "shorts":
                        if RogueX.Panties:
                            if RogueX.SeenPanties:
                                $ Count = 3 if not ApprovalCheck(RogueX, 600) else Count
                            else:
                                $ RogueX.SeenPanties = 1
                                $ Count = 3 if not ApprovalCheck(RogueX, 900) else Count
                            $ RogueX.Statup("Lust", 60, 2)
                        else:
                            if RogueX.SeenPussy:
                                $ Count = 3 if not ApprovalCheck(RogueX, 900) else Count
                            else:
                                call Rogue_First_Bottomless
                                $ Count = 3 if not ApprovalCheck(RogueX, 1400) else Count

                if Count == 2:
                        #first time
                        menu:
                            extend ""
                            "I think those look really good on you.":
                                $ RogueX.FaceChange("smile", 1)
                                $ RogueX.Inventory.append(RogueX.Hose)
                                ch_r "You think so? That's sweet, maybe I'll keep them on hand."
                            "Yeah, too bad.":
                                $ RogueX.FaceChange("bemused")
                                ch_r ". . ."
                            "Ha! Those don't leave much to the imagination!":
                                ch_r "Thanks for that. . ."

                elif Count == 3: #She is embarassed and takes off
                    $ RogueX.FaceChange("startled", 2)
                    ch_r "I, um, I should get out of here."
                    $ RogueX.Blush = 1
                    call Remove_Girl(RogueX)
                    $ RogueX.OutfitChange()
                #end "if they ripped"
        return
