label Shower_Room_Entry:
    call Jubes_Entry_Check
    $ bg_current = "bg_showerroom"
    $ door_locked = False
    $ Nearby = []
    $ Present = []
    call Taboo_Level
    call set_the_scene(0,1,0)
    $ Round -= 5 if Round >= 5 else Round
    if Round <= 10 or len(Party) >= 2:
            jump Shower_Room

    #Activates Jean meet
    if Day >= 9 and "met" not in JeanX.History and "met" in EmmaX.History:
            call JeanMeet
            jump Shower_Room

    $ Options = []
    $ line = active_Girls[:]   #make sure this is initialized
    while line:
            #loops through and adds populates Occupants with locals
            if line[0] not in Party and "showered" not in line[0].daily_history and (line[0].location == line[0].Home or line[0].location == "bg_dangerroom"):
                    #Checks if girl is in the shower
                    $ Options.append(line[0])
            $ line.remove(line[0])
    $ line = 0

    if Options:
                $ renpy.random.shuffle(Options)

    $ D20 = renpy.random.randint(1, 20)
    # <5 is they show up late, 5-9 is they haven't showered yet, 10+ is they finished,
    # 13-15 is they are changing, 16+ is you walk in on them nude, 17+ they might be masturbating

    if D20 < 5 or (len(Options) + len(Party) > 2):  #not Options or
                # if < 5, they show up late, or if there are more potential girls than room for them
                while Options and (D20 < 5 or len(Options) + len(Party) > 2):
                        #Loops through while Options and Party are more than 2
                        $ Nearby.append(Options[0])     #adds this girl to the nearby roster
                        $ Options[0].location = "nearby"     #adds this girl to the nearby roster
                        $ Options.remove(Options[0])    #subs this girl from Options

    if not Party and Options and Options[0] in all_Girls:
            if D20 > 15:
                    call Girl_Caught_Shower(Options[0])
                    jump Shower_Room
            elif D20 > 13:
                    $ Options[0].AddWord(1,"showered","showered",0,0)
                    call Girl_Caught_Changing(Options[0])
                    jump Shower_Room
    #End Caught Check

    # If none of the caught dialogs plays, checks to see if anyone is in the room, and allows them to be there if they are.
    $ line = Options[:]
    while line:
            #loops through and adds populates nearby with locals
            $ line[0].location = bg_current
            $ line.remove(line[0])
    $ line = 0

    call Present_Check(0)

    $ line = Options[:]
    while line:
            #loops through and puts towels on them, maybe the "showered" trait
            if line[0].location == bg_current and line[0] not in Party:
                    if D20 >= 10:
                            $ line[0].AddWord(1,"showered","showered",0,0)
                    $ line[0].OutfitChange("towel")
            $ line.remove(line[0])
    $ line = 0
    #End Count set-up

    call set_the_scene(Dress=0)
    if Party:
        $ line = " and " + Party[0].name
    else:
        $ line = ""
    if len(Options) >= 2:
        "As you enter, you[line] see [Options[0].name] and [Options[1].name] standing there."
    elif Options:
        "As you enter, you[line] see [Options[0].name] standing there."
    $ line = 0

    if Options:
            $ line = 0
            if Options[0] == RogueX:
                    ch_r "Hey, [RogueX.Petname]."
                    if "showered" in RogueX.recent_history:
                            ch_r "I was just getting ready to head out."
                    if not ApprovalCheck(Options[0], 900):
                            ch_r "See ya later."
            if Options[0]  == KittyX:
                    ch_k "Hey, [KittyX.Petname]."
                    if "showered" in KittyX.recent_history:
                            ch_k "I just got finished."
                    if not ApprovalCheck(Options[0], 900):
                            ch_k "Oh, um, I should get out of your way. . ."
            if Options[0]  == EmmaX:
                    ch_e "Oh, hello, [EmmaX.Petname]."
                    if "showered" in EmmaX.recent_history:
                            ch_e "I was about finished here."
                    if not ApprovalCheck(Options[0], 900):
                            ch_e "I should get going."
            if Options[0]  == LauraX:
                    ch_l "Oh, hey."
                    if "showered" in LauraX.recent_history:
                            ch_l "I'm done here."
                    if not ApprovalCheck(Options[0], 900):
                            ch_l "See you later."
            if Options[0]  == JeanX:
                    ch_j "Oh, hey. . . you."
                    if "showered" in JeanX.recent_history:
                            ch_j "I'm wrapping up here."
                    if not ApprovalCheck(Options[0], 900):
                            ch_j "Later."
            if Options[0]  == StormX:
                    ch_s "Oh, hello, [StormX.Petname]."
                    if "showered" in StormX.recent_history:
                            ch_s "I was finishing up here."
                    if not ApprovalCheck(Options[0], 600):
                            ch_s "I am heading out at the moment."
            if Options[0]  == JubesX:
                    ch_v "Yo, [JubesX.Petname]."
                    if "showered" in JubesX.recent_history:
                            ch_v "I just finished up here."
                    if not ApprovalCheck(Options[0], 900):
                            ch_v "I should, uh, get going. . ."
            if len(Options) >= 2:
                    if Options[1] == RogueX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    #if both decide to leave
                                    ch_r "Yeah, I'll see you too."
                            elif not ApprovalCheck(Options[1], 900):
                                    #if only person 2 decides to leave
                                    ch_r "Yeah, I should get going though."
                            else:
                                    #if both stay
                                    ch_r "Yeah, hey."
                    if Options[1] == KittyX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_k "Yeah, see ya."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_k "Oh, well. . . I should get going."
                            else:
                                    ch_k "Yeah, hi."
                    if Options[1] == EmmaX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_e "Yes, I should also get going."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_e "You two look like you have some business. . ."
                            else:
                                    ch_e "Yes, hello."
                    if Options[1] == LauraX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_l "Yeah, I'm heading out too."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_l "I'll get out of your way."
                            else:
                                    ch_l "Hey."
                    if Options[1] == JeanX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_j "Yeah, I'm done too."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_j "I'm headed out."
                            else:
                                    ch_j "Hey."
                    if Options[1] == StormX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 600):
                                    ch_s "Yes, I am also leaving."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_s "I wouldn't want to be a bother. . ."
                            else:
                                    ch_s "Yes, hello."
                    if Options[1] == JubesX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_v "Yeah, see ya."
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_v "Oh, so. . . I should head out."
                            else:
                                    ch_v "Yeah, hey."

                    if not ApprovalCheck(Options[1], 900):
                            call remove_girl(Options[1])
            if not ApprovalCheck(Options[0], 900):
                            call remove_girl(Options[0])
            # End welcomes
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
    $ line = 0
    # End Reply portion
    $ Options = []

label Shower_Room:
    $ bg_current = "bg_showerroom"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call set_the_scene(Dress=0)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if time_index == 3: #night time
                        "You're getting tired, you head back to your room."
                        jump player_room
                call Wait
                call EventCalls
                call Girls_Location
    call GirlsAngry
    #End Room Set-up

    menu:
        "You're in the showers. What would you like to do?"

        "Chat":
                call Chat

        "Shower" if Round > 30:
                call Showering
        "Shower [[no time](locked)" if Round <= 30:
                pass

        "Wait." if time_index < 3: #not night time
                "You hang out for a bit."
                if Round > 30:
                        "In the showers."
                        "Not gonna lie, kinda weird."
                call Wait
                call EventCalls
                call Girls_Location

                #this bit sets up drop-in Girls
                if renpy.random.randint(1, 20) < 5:
                        $ Nearby = []
                        $ line = active_Girls[:]   #make sure this is initialized
                        while line:
                                #loops through and adds populates Occupants with locals
                                if line[0].location != bg_current and "showered" not in line[0].daily_history and (line[0].location == line[0].Home or line[0].location == "bg_dangerroom"):
                                        #Checks if girl is in the shower
                                        $ Nearby.append(line[0])
                                $ line.remove(line[0])
                        $ line = 0
                        if Nearby:
                                $ renpy.random.shuffle(Nearby)
                                while len(Nearby) > 2:
                                            # culls out list to 2 if there is a party
                                            $ Nearby.remove(Nearby[0])
                                if len(Nearby) > 1:
                                        $ Nearby[1].location = "nearby"
                                $ Nearby[0].location = "nearby"
        "Wait.  [[no time](locked)" if time_index >= 3: # night time
                pass

        "Go to the Danger Room" if TravelMode:
                call No_Towels
                jump Danger_Room_Entry
        "Return to Your Room" if TravelMode:
                call No_Towels
                jump player_room_entry
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                            call No_Towels
                            call girls_room_entry(RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.History:
                            call No_Towels
                            call girls_room_entry(KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.History:
                            call No_Towels
                            call girls_room_entry(EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.History:
                            call No_Towels
                            call girls_room_entry(LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.History:
                            call No_Towels
                            call girls_room_entry(JeanX)
                "[StormX.name]'s Room" if "met" in StormX.History:
                            call No_Towels
                            call girls_room_entry(StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.History:
                            call No_Towels
                            call girls_room_entry(JubesX)

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
    #Removes their towels if player is leaving the showers
    $ Girls = all_Girls[:]
    while Girls:
            #loops through and adds populates Occupants with locals
            if Girls[0].location == "bg_showerroom":
                    $ Girls[0].AddWord(1,"showered","showered")
            if "met" in Girls[0].History and Girls[0] not in Party:
                    $ Girls[0].location = Girls[0].Schedule[Weekday][time_index]
            $ Girls[0].OutfitChange(Girls[0].OutfitDay)
            $ Girls.remove(Girls[0])
    return

label Showering(Occupants = [], StayCount=[] , Showered = 0, line = 0, Girls=[]):
    # Occupants tallies how many girls are here.
    # StayCount tallies how many girls are willing to stick around.
    $ Girls = all_Girls[:]
    while Girls:
            #loops through and adds populates Occupants with locals
            if Girls[0] not in active_Girls:
                    $ Girls[0].location = "hold"
            if Girls[0].location == "bg_showerroom" and Girls[0] not in Occupants:
                    $ Occupants.append(Girls[0])
            $ Girls.remove(Girls[0])
    if Occupants:
            ch_p "I'm taking a shower, care to join me?"
            if Occupants[0] == RogueX and "showered" in RogueX.recent_history:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_r "We actually just finished up, so we'll head out."
                    else:
                        ch_r "I actually just finished up, so I'll head out."
                    $ Showered = 1
            elif Occupants[0] == KittyX and "showered" in KittyX.recent_history:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_k "We actually just showered, so we're heading out."
                    else:
                        ch_k "I actually just showered, so I'm heading out."
                    $ Showered = 1
            elif Occupants[0] == EmmaX and "showered" in EmmaX.recent_history:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_e "We were actually finishing up, so we're heading out."
                    else:
                        ch_e "I was actually finishing up, so I'm heading out."
                    $ Showered = 1
            elif Occupants[0] == LauraX and "showered" in LauraX.recent_history:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_l "We were done, actually."
                    else:
                        ch_l "I'm heading out now."
                    $ Showered = 1
            elif Occupants[0] == JeanX and "showered" in JeanX.recent_history:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_j "We were done."
                    else:
                        ch_j "I'm heading out."
                    $ Showered = 1
            elif Occupants[0] == StormX and "showered" in StormX.recent_history:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_s "I think we're about finished and heading out now."
                    else:
                        ch_s "I was about finished and heading out now."
                    $ Showered = 1
            elif Occupants[0] == JubesX and "showered" in JubesX.recent_history:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_v "We finished getting showered, so we're taking off."
                    else:
                        ch_v "I finished getting showered, so I'm taking off."
                    $ Showered = 1
            else:
                #None of them have showered yet
                if Occupants[0] == RogueX:
                        if ApprovalCheck(RogueX, 1200) or (ApprovalCheck(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy):
                                    # Rogue says yes
                                    ch_r "I suppose I could stick around. . ."
                                    $ StayCount.append(RogueX)
                        else:
                                    # Rogue says no
                                    ch_r "Nah, I should probably get going."
                elif Occupants[0] == KittyX:
                        if ApprovalCheck(KittyX, 1400) or (ApprovalCheck(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy):
                                    ch_k "Yeah, I could stick around."
                                    $ StayCount.append(KittyX)
                        else:
                                    ch_k "I've got to get going."
                elif Occupants[0] == EmmaX:
                        if not "classcaught" in EmmaX.History or "three" not in EmmaX.History:
                                ch_e "I really should be going. . ."
                        elif ApprovalCheck(EmmaX, 1400) or (ApprovalCheck(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy):
                                    ch_e "I suppose I could stay, for a bit."
                                    $ StayCount.append(EmmaX)
                        else:
                                    ch_e "I'm afraid I really must be going."
                elif Occupants[0] == LauraX:
                        if ApprovalCheck(LauraX, 1400) or (ApprovalCheck(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy):
                                    ch_l "I got nothing better to do."
                                    $ StayCount.append(LauraX)
                        else:
                                    ch_l "I gotta get going."
                elif Occupants[0] == JeanX:
                        if ApprovalCheck(JeanX, 1400) or (ApprovalCheck(JeanX, 700) and JeanX.SeenChest and JeanX.SeenPussy):
                                    ch_j "Sure, why not."
                                    $ StayCount.append(JeanX)
                        else:
                                    ch_j "Nah, lol."
                elif Occupants[0] == StormX:
                        if ApprovalCheck(StormX, 700):
                                    ch_s "I could stay, I suppose."
                                    $ StayCount.append(StormX)
                        else:
                                    ch_s "I really do have things to do, [StormX.Petname]."
                elif Occupants[0] == JubesX:
                        if ApprovalCheck(JubesX, 1400) or (ApprovalCheck(JubesX, 700) and JubesX.SeenChest and JubesX.SeenPussy):
                                    ch_v "I guess I could stay a minute. . ."
                                    $ StayCount.append(JubesX)
                        else:
                                    ch_v "I'm kinda busy, [JubesX.Petname]."
                #end first girls

                if len(Occupants) >= 2:
                    #seond girls
                    if Occupants[1] == RogueX:
                        if ApprovalCheck(RogueX, 1200) or (ApprovalCheck(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy):
                                if StayCount:
                                    #If Rogue said yes
                                    ch_r "I could stick around too. . ."
                                else:
                                    #If Rogue said no
                                    ch_r "Well, I could probably stay."
                                $ StayCount.append(RogueX)
                        else:
                                if StayCount:#RogueCount > 1:
                                    #If Rogue said yes
                                    ch_r "I can't though . ."
                                else:
                                    #If Rogue said no
                                    ch_r "I should get going too."

                    elif Occupants[1] == KittyX:
                        if ApprovalCheck(KittyX, 1400) or (ApprovalCheck(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy):
                                if StayCount:
                                    #If Kitty said yes
                                    ch_k "I guess I could stay too. . ."
                                else:
                                    #If Kitty said no
                                    ch_k "Well, I could stay though."
                                $ StayCount.append(KittyX)
                        else:
                                if StayCount:#RogueCount > 1:
                                    #If Kitty said yes
                                    ch_k "I've really got to go though. . ."
                                else:
                                    #If Kitty said no
                                    ch_k "Yeah, I should head out too."

                    elif Occupants[1] == EmmaX:
                        if not "classcaught" in EmmaX.History or "three" not in EmmaX.History:
                                    ch_e "I really should be going. . ."
                        elif ApprovalCheck(EmmaX, 1400) or (ApprovalCheck(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy):
                                if StayCount:
                                    #If Emma said yes
                                    ch_e "I suppose I could also stay. . ."
                                else:
                                    #If Emma said no
                                    ch_e "But {i}I{/i} could stick around. . ."
                                $ StayCount.append(EmmaX)
                        else:
                                if StayCount:
                                    #If Emma said yes
                                    ch_e "But I really must be going. . ."
                                else:
                                    #If Emma said no
                                    ch_e "Yes, let's go."

                    elif Occupants[1] == LauraX:
                        if ApprovalCheck(LauraX, 1400) or (ApprovalCheck(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy):
                                if StayCount:
                                    #If Laura said yes
                                    ch_l "I could stay too. . ."
                                else:
                                    #If Laura said no
                                    ch_l "I could stick around."
                                $ StayCount.append(LauraX)
                        else:
                                if StayCount:
                                    #If Laura said yes
                                    ch_l "I gotta get going though. . ."
                                else:
                                    #If Laura said no
                                    ch_l "Yeah, me too."

                    elif Occupants[1] == JeanX:
                        if ApprovalCheck(JeanX, 1000) or (ApprovalCheck(JeanX, 600) and JeanX.SeenChest and JeanX.SeenPussy):
                                if StayCount:
                                    #If Jean said yes
                                    ch_j "I guess I could stay too. . ."
                                else:
                                    #If Jean said no
                                    ch_j "I could stick around."
                                $ StayCount.append(JeanX)
                        else:
                                if StayCount:
                                    #If Jean said yes
                                    ch_j "I'm heading out though. . ."
                                else:
                                    #If Jean said no
                                    ch_j "Yeah."

                    elif Occupants[1] == StormX:
                        if ApprovalCheck(StormX, 700):
                                if StayCount:
                                    #If Storm said yes
                                    ch_s "I could also stay. . ."
                                else:
                                    #If Storm said no
                                    ch_s "I could stay for a moment though. . ."
                                $ StayCount.append(StormX)
                        else:
                                if StayCount:
                                    #If Storm said yes
                                    ch_s "Well I'm afraid I must be going. . ."
                                else:
                                    #If Storm said no
                                    ch_s "Yes, let's."

                    elif Occupants[1] == JubesX:
                        if ApprovalCheck(JubesX, 1400) or (ApprovalCheck(JubesX, 700) and JubesX.SeenChest and JubesX.SeenPussy):
                                if StayCount:
                                    #If Jubes said yes
                                    ch_k "I could kinda stay too. . ."
                                else:
                                    #If Jubes said no
                                    ch_k "Well, -I'm- not that busy. . ."
                                $ StayCount.append(JubesX)
                        else:
                                if StayCount:#RogueCount > 1:
                                    #If Jubes said yes
                                    ch_k "I'm really busy right now though. . ."
                                else:
                                    #If Jubes said no
                                    ch_k "Oh, yeah, I gotta go too. . ."

                #end none have showered yet
            if len(Occupants) > len(StayCount):
                    #if either said no. If they're at StayCount = 2 here, they have already agreed.
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
                                $ line = "spot"

                        #fix Add "Take off your own clothes" option.

                        "Maybe you could stay and watch?":
                                $ line = "watch me"

                        "But I didn't get to watch." if Showered:
                                $ line = "watch you"
                    if line:
                        $ Girls = Occupants[:]
                        while Girls:
                                #loops through and adds populates Occupants with locals
                                if Girls[0].location == bg_current and Girls[0] not in StayCount:
                                        if Girls[0] == EmmaX and (not "classcaught" in EmmaX.History or (StayCount and "three" not in EmmaX.History)):
                                            #if it's Emma, and she isn't comfortable with threesomes or public stuff, skip her
                                            pass
                                        elif Girls[0] == JeanX and ApprovalCheck(Girls[0], 600):
                                            $ StayCount.append(Girls[0])
                                        elif Girls[0] == StormX:
                                            if ApprovalCheck(Girls[0], 700, "LO"):
                                                $ StayCount.append(Girls[0])
                                        elif ApprovalCheck(Girls[0], 1200,Alt=[[KittyX],1400]) or (ApprovalCheck(Girls[0], 600,Alt=[[KittyX],700]) and Girls[0].SeenChest and Girls[0].SeenPussy): #1400/700 for Kitty?
                                            $ StayCount.append(Girls[0])
                                        elif line == "spot" and ApprovalCheck(Girls[0], 1000, "LI",Alt=[[KittyX],1200]):   #1200 for Kitty?
                                            $ StayCount.append(Girls[0])
                                        elif line == "watch you" and ApprovalCheck(Girls[0], 600, "O",Alt=[[EmmaX],500]):   #500 for Emma?
                                            $ StayCount.append(Girls[0])
                                        #else, she doesn't agree
                                $ Girls.remove(Girls[0])

                        if line == "spot":
                                #"Sure you got every spot?"
                                if StayCount:
                                        #if at least one girl agreed to stay
                                        if StayCount[0] == RogueX: #RogueCount == 2:
                                            #Rogue agreed
                                            ch_r "Fine, I could use another scrub."
                                        elif StayCount[0] == KittyX:
                                            #Kitty agreed
                                            ch_k "Oh, I guess I could take another pass at it."
                                        elif StayCount[0] == EmmaX:
                                            #Emma agreed
                                            ch_e "I suppose we could take a look. . ."
                                        elif StayCount[0] == LauraX:
                                            #Laura agreed
                                            ch_l "Well, maybe. . ."
                                        elif StayCount[0] == JeanX:
                                            #Jean agreed
                                            ch_j "Well. . ."
                                        elif StayCount[0] == StormX:
                                            #Storm agreed
                                            ch_s "Well, another pass couldn't hurt. . ."
                                        elif StayCount[0] == JubesX:
                                            #Jubes agreed
                                            ch_v "I mean, you can never be -too- clean. . ."
                                if RogueX.location == bg_current and RogueX not in StayCount: #RogueCount == 1:
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Well, [RogueX.Petname], I think I'm fine."
                                    else:
                                            ch_r "No, [RogueX.Petname], I think I'm covered."
                                if KittyX.location == bg_current and KittyX not in StayCount: # KittyCount == 1:
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Oh, well I think I[KittyX.like]got it?"
                                            ch_k "See you later, [KittyX.Petname]."
                                    else:
                                            ch_k "Ha, I'm squeaky clean, [KittyX.Petname], see you later."
                                if EmmaX.location == bg_current and EmmaX not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "Well it appears you'll be taken care of."
                                            ch_e "I'll be going, [EmmaX.Petname]."
                                    else:
                                            ch_e "I'm afraid not, [EmmaX.Petname], I'll be going."
                                if LauraX.location == bg_current and LauraX not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "Looks like you got this handled."
                                            ch_l "I'm out, [LauraX.Petname]."
                                    else:
                                            ch_l "I'm out."
                                if JeanX.location == bg_current and JeanX not in StayCount:
                                    #Jean refused
                                    if StayCount:
                                            ch_j "Well, looks like you guys are going to have fun."
                                            ch_j "I'll head out, [JeanX.Petname]."
                                    else:
                                            ch_j "I'll head out."
                                if StormX.location == bg_current and StormX not in StayCount:
                                    #Storm refused
                                    if StayCount:
                                            ch_s "It looks like you'll be occupied."
                                            ch_s "I'll be going, [StormX.Petname]."
                                    else:
                                            ch_s "I really doubt that I could have, [StormX.Petname], I'll be going."
                                if JubesX.location == bg_current and JubesX not in StayCount: # JubesCount == 1:
                                    #Jubes refused
                                    if StayCount:
                                            ch_v "Nah, I think you'll be fine."
                                            ch_v "Later, guys."
                                    else:
                                            ch_v "Nah, I'm good. Later, [JubesX.Petname]."
                                #end "missed a spot?"

                        elif line == "watch me":
                                #"Maybe you could stay and watch?"
                                if StayCount:
                                        if StayCount[0] == RogueX:
                                            #Rogue agreed
                                            ch_r "Yeah, I guess I do enjoy the view."
                                        elif StayCount[0] == KittyX:
                                            #Kitty agreed
                                            ch_k "I. . . guess I wouldn't mind that. . ."
                                        elif StayCount[0] == LauraX:
                                            #Laura agreed
                                            ch_l "Ok, let's see what you got."
                                        elif StayCount[0] == JeanX:
                                            #Jean agreed
                                            ch_j "Ohh, this should be good. . ."
                                        elif StayCount[0] == StormX:
                                            #Storm agreed
                                            ch_s "I suppose that I could. . ."
                                        elif StayCount[0] == JubesX:
                                            #Jubes agreed
                                            ch_v ". . . Yeah, ok."

                                if RogueX.location == bg_current and RogueX not in StayCount: #RogueCount == 1:
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Oh, well, I'm gonna pass on that, [RogueX.Petname]."
                                    else:
                                            ch_r "Yeah, I'm gonna pass on that, [RogueX.Petname]."
                                if KittyX.location == bg_current and KittyX not in StayCount: # KittyCount == 1:
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Well, [KittyX.like]I don't need to see that."
                                            ch_k "See you later, [KittyX.Petname]."
                                    else:
                                            ch_k "[KittyX.Like]I don't need to see that."
                                if EmmaX.location == bg_current and EmmaX not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "You appear to have enough of an audience."
                                            ch_e "I'll be going, [EmmaX.Petname]."
                                    else:
                                            ch_e "I think I'll be fine, [EmmaX.Petname], I'll be going."
                                if LauraX.location == bg_current and LauraX not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "She's got you covered."
                                            ch_l "I'm out, [LauraX.Petname]."
                                    else:
                                            ch_l "I'm out."
                                if JeanX.location == bg_current and JeanX not in StayCount:
                                    #Jean refused
                                    if StayCount:
                                            ch_j "Well, looks like you guys are going to have fun."
                                            ch_j "I'll head out, [JeanX.Petname]."
                                    else:
                                            ch_j "I'll head out."
                                if StormX.location == bg_current and StormX not in StayCount:
                                    #Storm refused
                                    if StayCount:
                                            ch_s "Oh, I think someone else wants the show."
                                            ch_s "I'll be going, [StormX.Petname]."
                                    else:
                                            ch_s "I don't see why I would, [StormX.Petname]. I'll be going."
                                if JubesX.location == bg_current and JubesX not in StayCount: # JubesCount == 1:
                                    #Jubes refused
                                    if StayCount:
                                            ch_v "Um, no thanks. . ."
                                            ch_v "See you later, [JubesX.Petname]."
                                    else:
                                            ch_v "Um, no thanks."
                                #end "Watch me"

                        elif line == "watch you":
                                #"But I didn't get to watch."
                                if StayCount:
                                        if StayCount[0] == RogueX:
                                            #Rogue agreed
                                            ch_r "Well, I don't mind putting on a show."
                                        elif StayCount[0] == KittyX:
                                            #Kitty agreed
                                            ch_k "You want to watch me. . ."
                                            ch_k "Ok."
                                        elif StayCount[0] == EmmaX:
                                            #Emma agreed
                                            ch_e "I suppose I can't blame you for that. . ."
                                        elif StayCount[0] == LauraX:
                                            #Laura agreed
                                            ch_l "Huh. Suit yourself."
                                        elif StayCount[0] == JeanX:
                                            #Jean agreed
                                            ch_j "Well, we can't have that. . ."
                                        elif StayCount[0] == StormX:
                                            #Storm agreed
                                            ch_s ". . ."
                                        elif StayCount[0] == JubesX:
                                            #Jubes agreed
                                            ch_v "Well. . . I guess we should make up for that. . ."

                                if RogueX.location == bg_current and RogueX not in StayCount: #RogueCount == 1:
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Really? Well not me."
                                            ch_r "Have fun, [RogueX.Petname]."
                                    else:
                                            ch_r "Keep dreaming, [RogueX.Petname]."
                                if KittyX.location == bg_current and KittyX not in StayCount: # KittyCount == 1:
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Seriously?! Well I'm not into that."
                                            ch_k "Later, [KittyX.Petname]."
                                    else:
                                            ch_k "[KittyX.Like]no way!"
                                if EmmaX.location == bg_current and EmmaX not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "I wouldn't want to intrude."
                                            ch_e "I'll be going."
                                    else:
                                            ch_e "Hmm, I doubt you could handle it."
                                            ch_e "I'll be going."
                                if LauraX.location == bg_current and LauraX not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "She's got you covered."
                                            ch_l "I'm out, [LauraX.Petname]."
                                    else:
                                            ch_l "I'm out."
                                if JeanX.location == bg_current and JeanX not in StayCount:
                                    #Jean refused
                                    if StayCount:
                                            ch_j "Well, looks like you guys are going to have fun."
                                            ch_j "I'll head out, [JeanX.Petname]."
                                    else:
                                            ch_j "I'll head out."
                                if StormX.location == bg_current and StormX not in StayCount:
                                    #Storm refused
                                    if StayCount:
                                            ch_s "Well, you two enjoy yourselves."
                                            ch_s "I'll be going."
                                    else:
                                            ch_s "I'm flattered, but no."
                                            ch_s "I'll be going."
                                if JubesX.location == bg_current and JubesX not in StayCount: # JubesCount == 1:
                                    #Jubes refused
                                    if StayCount:
                                            ch_v "Ok, looks like you two can have fun with that."
                                            ch_v "Later, [JubesX.Petname]."
                                    else:
                                            ch_v "Yeah, no way."
                                #end "Watch you?"

                    if len(StayCount) > 1:
                            #if there are multiple girls
                            if StayCount[1].GirlLikeCheck(StayCount[0]) > 500:
                                    #if she likes the other girl. . .
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
                    #end "if you asked then a question"
            $ Girls = Occupants[:]
            while Girls:
                    #loops through and adds populates Occupants with locals
                    if Girls[0].location == bg_current:
                            if Girls[0] in StayCount:
                                    #If the girl Stays
                                    $ Girls[0].OutfitChange("nude")
                                    $ Girls[0].Water = 1
                                    $ Girls[0].Spunk = []
                                    $ Girls[0].recent_history.append("showered")
                                    $ Girls[0].daily_history.append("showered")
                                    call expression Girls[0].Tag + "_First_Bottomless" pass (1)
                                    call first_topless(Girls[0], silent = 1)
                            else:
                                    #If the girl leaves
                                    call remove_girl(Girls[0])
                            while Girls[0] in Nearby:
                                    $ Nearby.remove(Girls[0])
                    $ Girls.remove(Girls[0])

    call Seen_First_Peen(0,0,0,1) #You get naked

    while len(StayCount) >= 2 and StayCount[1] in Nearby:
            # removes any staying Girls from Nearby
            $ Nearby.remove(StayCount[1])
    while StayCount and StayCount[0] in Nearby:
            # removes any staying Girls from Nearby
            $ Nearby.remove(StayCount[0])

    if Nearby and len(StayCount) < 2:
            # This value carries over from the Entry scene if there are girls who show up late
            $ renpy.random.shuffle(Nearby)

            while Nearby and (len(Nearby) + len(StayCount)) > 2:
                        # while Nearby is more than 2-Staying Girls
                        $ Nearby.remove(Nearby[0]) #culls it to 1

            if len(Nearby) >= 2:
                "As you finish getting undressed, [Nearby[0].name] and [Nearby[1].name] enter the room."
                $ Nearby[1].location = bg_current
            else:
                "As you finish getting undressed, [Nearby[0].name] enters the room."
            $ Nearby[0].location = bg_current

            $ Girls = Nearby[:]

            #call Present_Check ?
            call set_the_scene(Dress=0)

            call Seen_First_Peen(0,0,1,1) #You get naked, silent reactions

            if RogueX in Girls:# in Nearby:
                    if RogueX.SeenPeen == 1:
                            $ RogueX.change_face("surprised",2,Eyes="down")
                            ch_r "Oh!"
                            $ RogueX.change_face("bemused",1,Eyes="side")
                            ch_r "I am so sorry, I should {i}not{/i} have just barged in like that."
                    else:
                            $ RogueX.change_face("bemused",1,Eyes="side")
                            ch_r "I simply {i}must{/i} be more careful. . ."
            if KittyX in Girls:
                    $ KittyX.change_face("bemused",2,Eyes="side")
                    if KittyX.SeenPeen == 1:
                            ch_k "Sorry! Sorry! I need to stop just casually phasing into places!"
                    else:
                            ch_k "I have {i}got{/i} to knock more. . ."
            if EmmaX in Girls:
                    if EmmaX.SeenPeen == 1:
                            $ EmmaX.change_face("surprised")
                            ch_e "Oh! Dreadfully sorry."
                            $ EmmaX.change_face("sexy",Eyes="down")
                            ch_e "I hope we can meet again under. . . different circumstances."
                    else:
                            $ EmmaX.change_face("sexy",Eyes="down")
                            ch_e "I really should pay closer attention. . ."
                    if "classcaught" not in EmmaX.History or ((StayCount or len(Nearby) >= 2) and "three" not in EmmaX.History):
                            #if Emma just showed up, but there are other girls around and she's not ok with that
                            "[EmmaX.name] decides to leave immediately."
                            call remove_girl(EmmaX)
                            $ Girls.remove(EmmaX)
                            $ EmmaX.OutfitChange()
            if LauraX in Girls:
                    if LauraX.SeenPeen == 1:
                            $ LauraX.change_face("surprised",Eyes="down")
                            ch_l "Hey. That's interesting. . ."
                    else:
                            $ LauraX.change_face("normal",Eyes="down")
                            ch_l ". . ."
                            $ LauraX.change_face("normal")
                            ch_l "I'm supposed to knock, aren't I."
            if JeanX in Girls:
                    if JeanX.SeenPeen == 1:
                            $ JeanX.change_face("surprised",Eyes="down")
                            ch_j "Well what do we have here? . ."
                    else:
                            $ JeanX.change_face("normal",Eyes="down")
                            ch_j ". . ."
                            $ JeanX.change_face("normal")
                            ch_j "Oh, nice to catch you. . . like this. . ."
            if StormX in Girls:
                    if StormX.SeenPeen == 1:
                            $ StormX.change_face("surprised")
                            ch_s "Oh! Hello there."
                            $ StormX.change_face("sexy",Eyes="down")
                            ch_s "And hello to you as well. . ."
                    else:
                            $ StormX.change_face("sexy",Eyes="down")
                            ch_s "I'm sorry to intrude. . ."
                    $ StormX.change_face("sexy")
            if JubesX in Girls:
                    $ JubesX.change_face("bemused",2,Eyes="side")
                    if JubesX.SeenPeen == 1:
                            ch_v "Oh, sorry! I wasn't paying attention."
                            $ JubesX.Eyes = "down"
                            pause 1
                            $ JubesX.Eyes = "side"
                            ch_v "um. . . hey. . ."
                    else:
                            ch_v "Oh, sorry! I wasn't paying attention."

            if EmmaX in StayCount and "three" not in EmmaX.History:
                            #if Emma was already here, but there are other girls around and she's not ok with that
                            if len(Girls) >= 2:
                                    "Seeing the other girls arrive, [EmmaX.name] quickly excuses herself."
                            else:
                                    "Seeing [Girls[0].name] arrive, [EmmaX.name] quickly excuses herself."
                            $ StayCount.remove(EmmaX)
                            call remove_girl(EmmaX)
                            $ EmmaX.OutfitChange()

            if Girls:
                #if there are still girls around to join in. . .
                if ApprovalCheck(Girls[0], 1200):
                        $ StayCount.append(Girls[0])
                if len(Girls) >=2 and ApprovalCheck(Girls[1], 1200) and len(StayCount) < 2:
                        $ StayCount.append(Girls[1])

                if len(Girls) >=2:
                        if Girls[0] not in StayCount and Girls[1] not in StayCount:
                                "They both turn right back around."
                                call remove_girl(Girls[0])
                                call remove_girl(Girls[1])
                                $ Girls = []
                        elif Girls[0] not in StayCount:
                                "[Girls[0].name] turns right back around, but [Girls[1].name] stays."
                                call remove_girl(Girls[0])
                                $ Girls.remove(Girls[0])
                        elif Girls[1] not in StayCount:
                                "[Girls[1].name] turns right back around, but [Girls[0].name] stays."
                                call remove_girl(Girls[1])
                                $ Girls.remove(Girls[1])
                elif Girls[0] not in StayCount:
                                "She turns right back around."
                                call remove_girl(Girls[0])
                                $ Girls.remove(Girls[0])

                while Girls:
                        #loops deals with "Nearby"s joining the party, removes others
                        #If Rogue Stays
                        $ Girls[0].OutfitChange("nude")
                        $ Girls[0].Water = 1
                        $ Girls[0].Spunk = []
                        $ Girls[0].recent_history.append("showered")
                        $ Girls[0].daily_history.append("showered")
                        call expression Girls[0].Tag + "_First_Bottomless" pass (1)
                        call first_topless(Girls[0], silent = 1)
                        if Girls[0] == RogueX:
                                    ch_r "I wouldn't mind stick'in around though."
                        elif Girls[0] == KittyX:
                                    ch_k "I {i}could{/i} get in on this."
                        elif Girls[0] == EmmaX:
                                    ch_e "But, I could use some face time."
                        elif Girls[0] == LauraX:
                                    ch_l "Scoot over."
                        elif Girls[0] == JeanX:
                                    ch_j "You're hogging the water."
                        elif Girls[0] == StormX:
                                    ch_s "Oh, goodbye then. . ."
                        elif Girls[0] == JubesX:
                                    ch_v "Well, I could always join ya."
                        $ Girls.remove(Girls[0])

    #End "girl crashes in"

    $ Round -= 30 if Round >= 30 else Round
    $ primary_action = 0

    if StayCount:
                #If at least one stays
                if len(StayCount) > 1 and StayCount[0] == StayCount[1]:
                        $ StayCount.remove(StayCount[0])
                if len(StayCount) > 1:
                        #If both stay
                        call shift_focus(StayCount[0], StayCount[1])
                        "You take a quick shower with [StayCount[0].name] and [StayCount[1].name]."
                else:
                        call shift_focus(StayCount[0])
                        "You take a quick shower with [StayCount[0].name]."

                call Shower_Sex

                if StayCount[0] == RogueX:
                        #Rogue agreed
                        ch_r "That was real nice, [RogueX.Petname]."
                elif StayCount[0] == KittyX:
                        #Kitty agreed
                        ch_k "That was. . . nice."
                elif StayCount[0] == EmmaX:
                        #Emma agreed
                        ch_e "That was. . . distracting."
                elif StayCount[0] == LauraX:
                        #Laura agreed
                        ch_l "Well that was fun."
                elif StayCount[0] == JeanX:
                        #Jean agreed
                        ch_j "That was fun."
                elif StayCount[0] == StormX:
                        #Storm agreed
                        ch_s "Ah, that was relaxing."
                elif StayCount[0] == JubesX:
                        #Jubes agreed
                        ch_v "That was fun, [JubesX.Petname]."

                if len(StayCount) > 1:
                        #if there are multiple girls
                        if StayCount[1] == RogueX:
                                #Rogue too
                                ch_r "Yeah."
                        elif StayCount[1] == KittyX:
                                #Kitty too
                                ch_k "Yeah, I had fun."
                        elif StayCount[1] == EmmaX:
                                #Emma too
                                ch_e "Indeed."
                        elif StayCount[1] == LauraX:
                                #Laura too
                                ch_l "Yup."
                        elif StayCount[1] == JeanX:
                                #Jean agreed
                                ch_j "Yeah, it was."
                        elif StayCount[1] == StormX:
                                #Storm too
                                ch_s "Certainly."
                        elif StayCount[1] == JubesX:
                                #Jubes too
                                ch_v "Yeah, totally."

    else:
                #solo shower
                $ line = "You take a quick shower" + renpy.random.choice([". It was fairly uneventful.",
                        ". A few people came and went as you did so.",
                        ". That was refreshing."])
                "[line]"
    #insert random events here
    $ Player.recent_history.append("showered")
    $ Player.daily_history.append("showered")
    if "scent" in Player.daily_history:
            $ Player.daily_history.remove("scent")

    call Get_Dressed
    if RogueX.location == bg_current:
            $ RogueX.OutfitChange("towel")
    if KittyX.location == bg_current:
            $ KittyX.OutfitChange("towel")
    if EmmaX.location == bg_current:
            $ EmmaX.OutfitChange("towel")
    if LauraX.location == bg_current:
            $ LauraX.OutfitChange("towel")
    if JeanX.location == bg_current:
            $ JeanX.OutfitChange("towel")
    if JubesX.location == bg_current:
            $ JubesX.OutfitChange("towel")

    $ Options = []

    return

label Shower_Sex(Options=0,line=0):
        #called from showering if sex is on the table.
        if len(StayCount) > 1 and (ApprovalCheck(StayCount[1], 1800,Check=1) > ApprovalCheck(StayCount[0], 1800,Check=1)):
                $ renpy.random.shuffle(StayCount) #swaps girls if second girl likes you more
        call shift_focus(StayCount[0])

        $ D20 = renpy.random.randint(1,20)
        $ D20 += 5 if ApprovalCheck(StayCount[0], 1800) else 0 #bonus if girl really likes you

        if "showered" in Player.recent_history:
                $ D20 = 0

        $ StayCount[0].change_face("sly")
        #A set
        if len(StayCount) > 1 and D20 >= 10:
                "As you do so, both girls press their bodies body up against yours."
                $ line = StayCount[0].name
                call Close_Launch(StayCount[0],StayCount[1])
        elif D20 >= 5:
                "As you do so, [StayCount[0].name] presses her body up against you."
                $ line = "She"
                call Close_Launch(StayCount[0])
        else:
                $ line = renpy.random.choice(["It was fairly uneventful.",
                    "A few people came and went as you did so.",
                    "That was refreshing."])
                "[line]"
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

        if line:
            if len(StayCount) > 1:
                    $ StayCount[0].change_stat("lust", 50, 5)
                    $ StayCount[0].change_stat("lust", 70, 3)
                    $ StayCount[1].change_stat("lust", 50, 5)
                    $ StayCount[1].change_stat("lust", 70, 3)
            else:
                    $ StayCount[0].change_stat("lust", 50, 6)
                    $ StayCount[0].change_stat("lust", 70, 3)
            $ Player.change_stat("Focus", 50, 5)
            $ Player.change_stat("Focus", 80, 2)
            menu:
                extend ""
                "Continue?":
                        pass
                "Stop her." if len(StayCount) < 2: #if one
                        $line = 0
                        call reset_position(StayCount[0])
                        "You take a step back, pulling away from her."
                        $ StayCount[0].change_stat("love", 80, -1)
                        $ StayCount[0].change_stat("obedience", 80, 5)
                        $ StayCount[0].change_stat("inhibition", 80, -1)
                        $ StayCount[0].change_face("sad")
                        "She seems a bit disappointed."
                "Stop them." if len(StayCount) > 1: #if both
                        $line = 0
                        call reset_position(StayCount[1])
                        call reset_position(StayCount[0])
                        "You take a step back, pulling away from them."
                        $ StayCount[0].change_stat("love", 80, -1)
                        $ StayCount[0].change_stat("obedience", 80, 5)
                        $ StayCount[0].change_stat("inhibition", 80, -1)
                        $ StayCount[1].change_stat("obedience", 80, 5)
                        $ StayCount[1].change_stat("inhibition", 80, -1)
                        $ StayCount[0].change_face("sad")
                        $ StayCount[1].change_face("sad")
                        "They seem a bit disappointed."
        if line:
            #B set
            $ Options = [1]
            if len(StayCount) > 1:
                    if ApprovalCheck(StayCount[0], 1300) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 800:
                        $ Options.append(2)     #"She reaches over to [StayCount[1]] and begins soaping up her pussy."
                    if ApprovalCheck(StayCount[0], 1200) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 700:
                        $ Options.append(3)     #"She reaches over to [StayCount[1]] and begins soaping up her chest."

            if ApprovalCheck(StayCount[0], 1300):
                $ Options.append(4)     #"She reaches down and takes your cock in her hand, soaping it up."
            if ApprovalCheck(StayCount[0], 1400):
                $ Options.append(5)     #"She kneels down and wraps her breasts around your cock, soaping it up."

            if ApprovalCheck(StayCount[0], 1300):
                $ Options.append(6)     #"She reaches down and begins fondling her own pussy, building a nice lather."
            if ApprovalCheck(StayCount[0], 1200):
                $ Options.append(7)     #"She begins rubbing her own breasts in circles, building a nice lather."

            if not ApprovalCheck(StayCount[0], 1400):
                #only adds these if there's not much in there.
                if ApprovalCheck(StayCount[0], 1000):
                    $ Options.append(8)         #"She draws her breasts up and down your arm, the soap bubbles squirting out."
                if ApprovalCheck(StayCount[0], 1100):
                    $ Options.append(9)         #"She kneels down and rubs her breasts against your leg, soaping it up."
                if ApprovalCheck(StayCount[0], 1000):
                    $ Options.append(10)        #"She presses against your back, her soapy breasts rubbing back and forth against it."
                if ApprovalCheck(StayCount[0], 1100):
                    $ Options.append(11)        #"She presses against your chest, her soapy breasts rubbing back and forth against it."

            $ renpy.random.shuffle(Options)

            #"line" will be either the first girl's name, or "She"
            #lesbian
            if Options[0] == 2:
                    $ StayCount[0].change_stat("lust", 50, 5)
                    $ StayCount[0].change_stat("lust", 70, 2)
                    $ StayCount[1].change_stat("lust", 50, 7)
                    $ StayCount[1].change_stat("lust", 70, 3)
                    $ Player.change_stat("Focus", 50, 8)
                    $ Player.change_stat("Focus", 80, 4)
                    "[line] reaches over to [StayCount[1].name] and begins soaping up her chest."
            elif Options[0] == 3:
                    $ StayCount[0].change_stat("lust", 50, 7)
                    $ StayCount[0].change_stat("lust", 70, 3)
                    $ StayCount[1].change_stat("lust", 50, 8)
                    $ StayCount[1].change_stat("lust", 70, 4)
                    $ Player.change_stat("Focus", 50, 8)
                    $ Player.change_stat("Focus", 80, 5)
                    "[line] reaches over to [StayCount[1].name] and begins soaping up her pussy."

            #fondling you
            elif Options[0] == 4:
                    if len(StayCount) > 1:
                            $ StayCount[0].change_stat("lust", 50, 10)
                            $ StayCount[0].change_stat("lust", 70, 7)
                    else:
                            $ StayCount[0].change_stat("lust", 50, 8)
                            $ StayCount[0].change_stat("lust", 70, 5)
                    $ Player.change_stat("Focus", 50, 10)
                    $ Player.change_stat("Focus", 80, 6)
                    "[line] reaches down and takes your cock in her hand, soaping it up."
            elif Options[0] == 5:
                    if len(StayCount) > 1:
                            $ StayCount[0].change_stat("lust", 50, 12)
                            $ StayCount[0].change_stat("lust", 70, 8)
                    else:
                            $ StayCount[0].change_stat("lust", 50, 9)
                            $ StayCount[0].change_stat("lust", 70, 6)
                    $ Player.change_stat("Focus", 50, 10)
                    $ Player.change_stat("Focus", 80, 4)
                    "[line] kneels down and wraps her breasts around your cock, soaping it up."

            #msturbation
            elif Options[0] == 6:
                    if len(StayCount) > 1:
                            $ StayCount[0].change_stat("lust", 50, 11)
                            $ StayCount[0].change_stat("lust", 70, 6)
                    else:
                            $ StayCount[0].change_stat("lust", 50, 9)
                            $ StayCount[0].change_stat("lust", 70, 5)
                    $ Player.change_stat("Focus", 50, 9)
                    $ Player.change_stat("Focus", 80, 4)
                    "[line] reaches down and begins fondling her own pussy, building a nice lather."
            elif Options[0] == 7:
                    if len(StayCount) > 1:
                            $ StayCount[0].change_stat("lust", 50, 10)
                            $ StayCount[0].change_stat("lust", 70, 5)
                    else:
                            $ StayCount[0].change_stat("lust", 50, 9)
                            $ StayCount[0].change_stat("lust", 70, 4)
                    $ Player.change_stat("Focus", 50, 8)
                    $ Player.change_stat("Focus", 80, 3)
                    "[line] begins rubbing her own breasts in circles, building a nice lather."

            #gentle tease
            elif Options[0] == 8:
                    $ StayCount[0].change_stat("lust", 50, 6)
                    $ StayCount[0].change_stat("lust", 70, 3)
                    $ Player.change_stat("Focus", 50, 7)
                    $ Player.change_stat("Focus", 80, 3)
                    "[line] draws her breasts up and down your arm, the soap bubbles squirting out."
            elif Options[0] == 9:
                    $ StayCount[0].change_stat("lust", 50, 8)
                    $ StayCount[0].change_stat("lust", 70, 3)
                    $ Player.change_stat("Focus", 50, 8)
                    $ Player.change_stat("Focus", 80, 3)
                    "[line] kneels down and rubs her breasts against your leg, soaping it up."
            elif Options[0] == 10:
                    $ StayCount[0].change_stat("lust", 50, 7)
                    $ StayCount[0].change_stat("lust", 70, 3)
                    $ Player.change_stat("Focus", 50, 6)
                    $ Player.change_stat("Focus", 80, 3)
                    "[line] presses against your back, her soapy breasts rubbing back and forth against it."
            elif Options[0] == 11:
                    $ StayCount[0].change_stat("lust", 50, 7)
                    $ StayCount[0].change_stat("lust", 70, 3)
                    $ Player.change_stat("Focus", 50, 8)
                    $ Player.change_stat("Focus", 80, 4)
                    "[line] presses against your chest, her soapy breasts rubbing back and forth against it."
            elif Options[0] == 1:
                    $ StayCount[0].change_stat("lust", 50, 5)
                    $ StayCount[0].change_stat("lust", 70, 2)
                    $ Player.change_stat("Focus", 50, 6)
                    $ Player.change_stat("Focus", 80, 3)
                    "[line] stares silently at you as she moves her hands along her soapy body. . ."
                    $ line = 0

        if line and len(StayCount) > 1:
            #C Set, check what the other girl thinks. . .
            $ D20 += 5 if ApprovalCheck(StayCount[1], 1800) else 0
            if StayCount[1].GirlLikeCheck(StayCount[0]) <= 800 and 2 <= Options[0] <=3:
                $ D20 -= 5
            if StayCount[1].GirlLikeCheck(StayCount[0]) <= 600:
                $ D20 -= 5

            if 2 <= Options[0] <= 3:
                # if it's lesbian stuff. . .
                if ApprovalCheck(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 800:
                        $ StayCount[1].change_face("sexy",1)
                        $ StayCount[0].change_stat("lust", 50, 5)
                        $ StayCount[0].change_stat("lust", 70, 5)
                        $ StayCount[1].change_stat("lust", 50, 12)
                        $ StayCount[1].change_stat("lust", 70, 12)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].name] seems really into this, and returns the favor."
                        $ Player.change_stat("Focus", 50, 7)
                        $ Player.change_stat("Focus", 80, 3)
                        $ line = 4
                elif ApprovalCheck(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700:
                        $ StayCount[1].change_face("sexy",2,Eyes="closed")
                        $ StayCount[1].change_stat("lust", 50, 10)
                        $ StayCount[1].change_stat("lust", 70, 10)
                        $ Player.change_stat("Focus", 50, 5)
                        $ Player.change_stat("Focus", 80, 3)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].name] seems really into this, and leans into it."
                else:
                        $ StayCount[1].change_stat("lust", 50, 10)
                        $ StayCount[1].change_face("sadside",Brows="confused")
                        "[StayCount[1].name] doesn't really seem to appreciate this."
                        "She pulls away."
                        $ line = 3
            else:
                # if it's not lesbian stuff. . .
                if (ApprovalCheck(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700) or ApprovalCheck(StayCount[1], 2000):
                    if Options[0] == 5: #titjob
                        $ StayCount[1].change_stat("lust", 50, 10)
                        $ StayCount[1].change_stat("lust", 70, 5)
                        $ Player.change_stat("Focus", 50, 6)
                        $ Player.change_stat("Focus", 80, 3)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].name] seems really into this, slowly rubbing against you as she watches."
                    else:
                        $ StayCount[1].change_stat("lust", 50, 10)
                        $ StayCount[1].change_stat("lust", 70, 5)
                        $ Player.change_stat("Focus", 50, 5)
                        $ Player.change_stat("Focus", 80, 3)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].name] seems really into this, and joins her on the other side."
                    $ line = 4
                elif ((ApprovalCheck(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 600)) or ApprovalCheck(StayCount[1], 1600):
                        $ StayCount[1].change_face("sexy",2,Eyes="down")
                        $ StayCount[1].change_stat("lust", 50, 10)
                        $ StayCount[1].change_stat("lust", 70, 5)
                        "[StayCount[1].name] seems really into this, and watches her do it."
                else:
                        $ StayCount[1].change_face("sadside",Brows="confused")
                        $ StayCount[1].change_stat("lust", 50, 5)
                        "[StayCount[1].name] doesn't really seem to appreciate this."
                        $ line = 3
        if line:
            menu:
                extend ""
                "Continue?":
                    pass
                "Stop her." if len(StayCount) < 2: #if one
                    $ line = 0
                    call reset_position(StayCount[0])
                    "You take a step back, pulling away from her."
                    $ StayCount[0].change_stat("love", 80, -2)
                    $ StayCount[0].change_stat("obedience", 80, 5)
                    $ StayCount[0].change_stat("inhibition", 80, -2)
                    $ StayCount[0].change_face("sad")
                    "She seems a bit disappointed."
                "Stop them." if len(StayCount) > 1: #if both
                    $line = 0
                    call reset_position(StayCount[1])
                    call reset_position(StayCount[0])
                    "You take a step back, pulling away from them."
                    $ StayCount[0].change_face("sad")
                    $ StayCount[0].change_stat("love", 80, -2)
                    $ StayCount[0].change_stat("obedience", 80, 5)
                    $ StayCount[0].change_stat("inhibition", 80, -2)
                    if line == 3:
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

        if line:
            #D set, wrap-up
            if len(StayCount) > 1 and line != 3: #if second didn't disapprove
                    $ StayCount[0].GLG(StayCount[1],600,4,1)
                    $ StayCount[1].GLG(StayCount[0],600,4,1)
                    $ StayCount[0].GLG(StayCount[1],800,3,1)
                    $ StayCount[1].GLG(StayCount[0],800,3,1)
                    $ StayCount[0].GLG(StayCount[1],900,1,1)
                    $ StayCount[1].GLG(StayCount[0],900,1,1)
            if 2 <= Options[0] <= 3 and D20 >= 15:
                    #if it's lesbian. . .
                    $ StayCount[1].GLG(StayCount[0],900,4,1)
                    $ Player.change_stat("Focus", 50, 10)
                    $ Player.change_stat("Focus", 80, 5)
                    "After a few minutes of this, it looks like [StayCount[1].name] gets off."
                    call Girl_Cumming(StayCount[1],1)
                    if line == 4:
                            $ StayCount[0].GLG(StayCount[1],900,3,1)
                            "It looks like [StayCount[0].name] is reacting positively to it as well. . ."
                            call Girl_Cumming(StayCount[0],1)
                    if len(StayCount) > 1:
                            "The girls take a step back."
                            call reset_position(StayCount[1])
                    else:
                            "[StayCount[0].name] takes a step back."
                    call reset_position(StayCount[0])

            elif 4 <= Options[0] <= 5 and D20 >= 10:
                    #if it's her fondling you
                    $ Player.Focus = 15
                    if Options[0] == 5: #if it was titjob
                            $ StayCount[0].Spunk.append("tits")

                    if line == 4:
                            $ StayCount[0].change_stat("inhibition", 90, 7)
                            $ StayCount[1].change_stat("inhibition", 90, 4)
                            $ StayCount[0].GLG(StayCount[1],900,3,1)
                            $ StayCount[1].GLG(StayCount[0],900,3,1)
                            "After a few minutes of this, the two of them manage to get you off."
                    else:
                            $ StayCount[0].change_stat("inhibition", 90, 5)
                            "After a few minutes of this, she manages to get you off."
                    "A little more work is needed to clean up the mess."
                    if Options[0] == 5: #if it was titjob
                            $ StayCount[0].Spunk = []
                    if len(StayCount) > 1:
                            "The girls take a step back."
                            call reset_position(StayCount[1])
                    else:
                            "[StayCount[0].name] takes a step back."
                    call reset_position(StayCount[0])

            elif 6 <= Options[0] <= 7 and D20 >= 15:
                    #if it's her masturbation. . .
                    $ StayCount[0].change_stat("inhibition", 90, 7)
                    $ Player.change_stat("Focus", 50, 15)
                    $ Player.change_stat("Focus", 80, 5)
                    "After a few minutes of this, it looks like [StayCount[0].name] gets off."
                    call Girl_Cumming(StayCount[0],1)
                    if line == 4:
                            $ StayCount[1].change_stat("inhibition", 90, 6)
                            $ StayCount[0].GLG(StayCount[1],900,3,1)
                            "It looks like [StayCount[1].name] is enjoying herself as well. . ."
                            call Girl_Cumming(StayCount[1],1)
                    if len(StayCount) > 1:
                            $ StayCount[1].GLG(StayCount[0],900,3,1)
                            "The girls take a step back."
                            call reset_position(StayCount[1])
                    else:
                            "[StayCount[0].name] takes a step back."
                    call reset_position(StayCount[0])
            else:
                #nobody got off
                if len(StayCount) > 1:
                        call reset_position(StayCount[1])
                call reset_position(StayCount[0])
                $ Player.change_stat("Focus", 50, 15)
                $ Player.change_stat("Focus", 80, 5)
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
        call shift_focus(StayCount[0])
        return
