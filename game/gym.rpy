label Gym_Entry(Girls=[],GirlsNum = 0):  #rkeljsv
        if Taboo == 0 and bg_current == "bg_dangerroom":
            menu:
                "Is this visit for work or for play?"
                "Work [[get geared up]":
                        pass
                "Play [[keep on this outfit]":
                        return
        $ Girls = all_Girls[:]
        while Girls:
                #while there are still girls to do or the Mode is exit. . .
                if Girls[0].Loc != "bg_dangerroom" and Girls[0].Outfit == "gym":
                                #If she isn't in the dangerroom, switch to her day clothes
                                $ Girls[0].Outfit = Girls[0].OutfitDay
                elif Girls[0].Outfit == "gym":
                                #If she's already in gym clothes, skip this
                                pass
                elif Girls[0].Loc == "bg_dangerroom" and Girls[0] not in Party:
                                #If she was already here
                                $ Girls[0].Outfit = "gym"
                $ Girls.remove(Girls[0])
        call set_the_scene
        $ Girls = Present[:]
        while Girls:
                if Girls[0].Outfit != "gym":
                        #If girl is in the gym, see if she'll change clothes
                        if ApprovalCheck(Girls[0], 1300, "LO") or "passive" in Girls[0].Traits:
                            pass
                        elif ApprovalCheck(Girls[0], 800, "LO") and Girls[0].Custom1[0]:
                            pass
                        elif ApprovalCheck(Girls[0], 600, "LO") and Girls[0].Gym[0] != 1:
                            pass
                        else:
                            $ line = "no"

                        if line == "no" or "asked gym" in Girls[0].daily_history or "no ask gym" in Girls[0].Traits:
                                #If she decides not to ask you
                                show blackscreen onlayer black
                                if Girls[0] == EmmaX:
                                        ch_e "I should change too."
                                elif Girls[0] == LauraX:
                                        ch_l "I'll be right back. . ."
                                elif Girls[0] == StormX:
                                        ch_s "I should change as well. . ."
                                else:
                                    if GirlsNum:
                                            call Anyline(Girls[0],"I'll be right back too.")
                                    else:
                                            call Anyline(Girls[0],"I'll be back soon, gotta change.")
                                $ Girls[0].Outfit = "gym"
                        else:
                                # She asks to change outfits
                                $ Girls[0].daily_history.append("asked gym")
                                if GirlsNum:
                                    #if the second girl to ask. . .
                                    if Girls[0] == EmmaX:
                                            $ line = "Do you think I should change as well?"
                                    elif Girls[0] == LauraX:
                                            $ line = "Did you want me to change into my gym clothes?"
                                    elif Girls[0] == StormX:
                                            $ line = "Do you think I should change as well?"
                                    else:
                                            $ line = "Should I change too?"
                                else:
                                    if Girls[0] == EmmaX:
                                            $ line = "Did you want me to change into my gear?"
                                    elif Girls[0] == LauraX:
                                            $ line = "Did you want me to change into my gym clothes?"
                                    elif Girls[0] == StormX:
                                            $ line = "Do you think I should change into my gym clothes?"
                                    else:
                                            $ line = "Would you like me to change into my gym clothes?"
                                call Anyline(Girls[0],line)
                                menu:
                                        extend ""
                                        "Yeah, they look great.":
                                                    $ Girls[0].change_face("smile")
                                                    $ Girls[0].change_stat("love", 80, 2)
                                                    $ Girls[0].change_stat("obedience", 40, 1)
                                                    $ Girls[0].change_stat("inhibition", 30, 1)
                                                    $ line = 1
                                        "No, stay in that.":
                                                    $ Girls[0].change_face("confused")
                                                    $ Girls[0].change_stat("obedience", 50, 5)
                                                    $ line = 0
                                        "Whichever you like.":
                                                    $ Girls[0].change_face("confused")
                                                    $ Girls[0].change_stat("inhibition", 50, 1)
                                                    $ line = renpy.random.randint(0, 3)
                                        "I don't care.":
                                                    $ Girls[0].change_face("angry")
                                                    $ Girls[0].change_stat("love", 50, -3, 1)
                                                    $ Girls[0].change_stat("obedience", 50, 4)
                                                    $ Girls[0].change_stat("inhibition", 50, 2)
                                                    $ line = renpy.random.randint(0, 1)
                                if line:
                                        #If she decided to change
                                        if Girls[0] == RogueX:
                                                ch_r "Ok, be right back."
                                        elif Girls[0] == KittyX:
                                                ch_k "Ok, back in a bit."
                                        elif Girls[0] == EmmaX:
                                                ch_e "Fine, I'll be right back."
                                        elif Girls[0] == LauraX:
                                                ch_l "I'll be right back then."
                                        elif Girls[0] == StormX:
                                                ch_s "Then I will return shortly."
                                        elif Girls[0] == JubesX:
                                                ch_v "K, be right back."
                                        $ Girls[0].Outfit = "gym"
                                # End She asks to change outfits
                        if Girls[0].Outfit == "gym":
                                $ GirlsNum += 1
                        $ line = 0
                        # End She isn't already in gym clothes
                $ Girls.remove(Girls[0])
                # End if Girls[0].Outfit != "gym":

        $ Girls = all_Girls[:]
        while Girls:
                #loops through and makes choices.
                $ Girls[0].OutfitChange()
                $ Girls.remove(Girls[0])
        hide blackscreen onlayer black
        return

label Gym_Exit(Girls=[]):  #rkeljsv
        #Called when you leave the gym, puts girls in their day clothes
        # call with "call Gym_Exit([RogueX]) " for a specific girl only
        if Girls and Girls[0] in all_Girls:
                pass
        else:
                $ Girls = Party[:]
        while Girls:
                if Girls[0].Outfit == "gym":
                        #if they are in gym clothes, they tell you they'll change
                        if len(Party) > 1:
                                $ line = "We should change out of these if we're leaving. . ."
                        else:
                                $ line = "I should change out of these if we're leaving. . ."
                        $ Girls[0].Outfit = Girls[0].OutfitDay
                $ Girls.remove(Girls[0])
        if Party:
                call Anyline(Party[0],line)
        if line:
            show blackscreen onlayer black with dissolve
            $ Girls = Party[:]
            while Girls:
                    #then they will change
                    $ Girls[0].OutfitChange()
                    $ Girls.remove(Girls[0])
            $ line = 0
            hide blackscreen onlayer black
        return

label Gym_Clothes_Off(Girls=[]):  #rkeljsv
        #Called when time changes and girls leave the Gym, puts girls in their day clothes
        if Girls and Girls[0] in all_Girls:
                pass
        else:
                $ Girls = all_Girls[:]
        while Girls: #or Mode == "exit"?
                #while there are still girls to do or the Mode is exit. . .
                if Girls[0] not in Party:
                    if Girls[0].Outfit == "gym" and Girls[0].Loc != "bg_dangerroom":
                            $ Girls[0].Outfit = Girls[0].OutfitDay
                    elif Girls[0].Loc == "bg_dangerroom":
                            $ Girls[0].Outfit = "gym"
                $ Girls.remove(Girls[0])
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
    call Gym_Entry #call Gym_Clothes("pre")#Automatically puts them in gym clothes if they've been here
    call set_the_scene

label Danger_Room:
    $ bg_current = "bg_dangerroom"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                "Looks like shifts are changing. . ."
                if time_index >=3: # night time
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
                if time_index >= 3: #night time
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
                    if time_index >= 3: #night time
                            "You lock the door"
                            $ Player.Traits.append("locked")
                            call Taboo_Level
                    else:
                            "You can't really do that during free hours."

        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level

        "Wait. (locked)" if time_index >= 3: #night time
                    pass
        "Wait." if time_index < 3: #not night time
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
    $ Player.daily_history.append("dangerroom")
    call set_the_scene

    if Round >= 80:
            $ line = "You have a long session in the Danger Room."
    elif Round >= 50:
            $ line = "You have a short workout in the Danger Room."
    else:
            $ line = "You squeeze in a quick session in the Danger Room."

    $ primary_action = 0
    if D20 >= 18:
            #if "cyclops":
            "[line] During the exercise, Cyclops accidentally shoots you."
            "Luckily you're immune to the beams, but your clothes weren't so lucky."
            call RoomStatboost("love",80,2)
            call RoomStatboost("lust",80,5)
    elif D20 >= 17:
            "[line] You participate in a hand-to-hand combat class."
            "Before you begin, Cyclops explains that it’s always good to know how to defend yourself when you can’t rely on your powers."
            "It sounds like there’s a story there."
    elif D20 >= 16:
            "Some of the senior students walk over to talk about your powers."
            "Nightcrawler wonders aloud what would happen if he grabbed you and tried to teleport while you tried to disable his powers."
            "You succeed in freaking each other out."
    else:
            $ line = line + renpy.random.choice([" It was fairly boring.",
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
            "[line]"

    $ Options = active_Girls[:]
    while Options:
            #Runs through all active girls, if they are in the room, checks to see if their hose were ripped.
            if Options[0].Loc == bg_current:
                    call Girl_TightsRipped(Options[0])
            $ Options.remove(Options[0])
    call Wait
    call Girls_Location
    call set_the_scene
    $ line = "The training session has ended, what would you like to do next?"

    jump Danger_Room

label Rogue_TightsRipped(Count = 0):
        if RogueX.Hose == "tights":
                $ Count = 1
                $ RogueX.Hose = "ripped tights"
                $ RogueX.change_face("angry")
                if "ripped tights" in RogueX.Inventory:
                    ch_r "Damnation, that's another pair ruined!"
                else:
                    $ Count = 2
                    ch_r "Well that's a good pair of tights down the chute."
        elif RogueX.Hose == "pantyhose":
                $ Count = 1
                $ RogueX.Hose = "ripped pantyhose"
                $ RogueX.change_face("angry")
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
                            $ RogueX.change_stat("lust", 60, 2)
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
                                $ RogueX.change_face("smile", 1)
                                $ RogueX.Inventory.append(RogueX.Hose)
                                ch_r "You think so? That's sweet, maybe I'll keep them on hand."
                            "Yeah, too bad.":
                                $ RogueX.change_face("bemused")
                                ch_r ". . ."
                            "Ha! Those don't leave much to the imagination!":
                                ch_r "Thanks for that. . ."

                elif Count == 3: #She is embarassed and takes off
                    $ RogueX.change_face("startled", 2)
                    ch_r "I, um, I should get out of here."
                    $ RogueX.Blush = 1
                    call Remove_Girl(RogueX)
                    $ RogueX.OutfitChange()
                #end "if they ripped"
        return
