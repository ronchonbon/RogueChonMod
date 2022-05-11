init python:

    def Room_Full(Here = [],BO=[]):
            # Culls parties down to 2 max
            # if Room_Full(): do something to empty it.
            global Party
            Here = []
            while len(Party) > 2:
                    # If two or more members in the party
                    #Culls down party size to two
                    Party.remove(Party[2])

            # checks to see which girls are present at a given location
            # adds members who are not currently in the party

            BO = TotalGirls[:]
            while BO:
                    if BO[0].Loc == bg_current and BO[0] not in Party:
                                Here.append(BO[0])
                    BO.remove(BO[0])
            if len(Party) + len(Here) >= 2:
                return 1
            else:
                return 0

label Round10(BO=[],Occupant=0): #rkeljsv
        #Called when it's time to auto-wait/sleep
        if Time_Count >= 3: #night
                    call Sleepover
                    return
                    #End night time

        #if it's not night time, just wait
        if bg_current not in PersonalRooms or bg_current == "bg player":
                    #if you are in a public space
                    call Wait
                    return
        #else. . .

        $ BO = TotalGirls[:]
        while BO:
                #sets Occupant if this is in one of the girls' rooms
                if BO[0].Home == bg_current:
                        $ Occupant = BO[0]
                        $ BO = [1]
                $ BO.remove(BO[0])

        if not Occupant:
                #if nobody was found, do this
                call Wait
                return
        #else
        if Occupant.Loc == bg_current:
                #If they are home
                if Occupant == RogueX:
                        ch_r "Sure, you can wait around a bit."
                elif Occupant == KittyX:
                        ch_k "Sure, you can hang out for a bit."
                elif Occupant == EmmaX:
                        ch_e "You can stay for a while, if you'd like."
                elif Occupant == LauraX:
                        ch_l "You can stay."
                elif Occupant == JeanX:
                        pass
                elif Occupant == StormX:
                        ch_s "I do not mind your presence."
                elif Occupant == JubesX:
                        ch_v "Yeah, you can hang for a bit."
        else:
                #if nobody is home
                "You wait for [Occupant.Name] to return."

        call Wait

        call Girls_Location #new here

        if Time_Count < 3 or Occupant.Loc != bg_current:
                #if it's not nightime or the girl is not home. . .
                return

        if Occupant == JubesX:
                #Jubilee doesn't sleep, so doesn't kick you out
                pass
        elif Occupant.Sleep or Occupant.SEXP >= 30:
                #It's late but she really likes you
                if Occupant == RogueX:
                        ch_r "It's pretty late, [RogueX.Petname], but you're welcome to stick around. . ."
                elif Occupant == KittyX:
                        ch_k "It's kinda late, [KittyX.Petname], but you can stay if you like. . ."
                elif Occupant == EmmaX:
                        ch_e "It's getting a bit late, [EmmaX.Petname], but I'd like you to stay. . ."
                elif Occupant == LauraX:
                        ch_l "I'm going to sleep soon. You can stay."
                elif Occupant == JeanX:
                        ch_j "I'm going to sleep in a bit, did you want to join me?"
                elif Occupant == StormX:
                        ch_s "I am going to bed soon, care to join me?"

        elif ApprovalCheck(Occupant, 1000, "LI") or ApprovalCheck(Occupant, 600, "OI"):
                #It's late but she really likes you
                if Occupant == RogueX:
                        ch_r "It's pretty late, [Occupant.Petname], but you can stay for a little bit."
                elif Occupant == KittyX:
                        ch_k "It's kinda late, [KittyX.Petname], but you can stay for a bit."
                elif Occupant == EmmaX:
                        ch_e "It's getting a bit late, [EmmaX.Petname], but you can stay."
                elif Occupant == LauraX:
                        ch_l "It's late, you can stay though."
                elif Occupant == JeanX:
                        ch_j "It's getting late."
                elif Occupant == StormX:
                        ch_s "It is getting late, [StormX.Petname]."
        else:
                #she likes you well enough but it's late so you should go
                if Occupant == RogueX:
                        ch_r "It's getting a little late [Occupant.Petname]. You should head out."
                elif Occupant == KittyX:
                        ch_k "It's getting late [KittyX.Petname]. You should get some sleep."
                elif Occupant == EmmaX:
                        ch_e "It's getting late, [EmmaX.Petname]. I need to get some sleep."
                elif Occupant == LauraX:
                        ch_l "I'm going to sleep. You should leave."
                elif Occupant == JeanX:
                        ch_j "I'm going to sleep. You should go."
                elif Occupant == StormX:
                        ch_s "I am going to bed soon. You should go."
                $ bg_current == "bg campus"
                jump Misplaced
        return

label Checkout(Total = 0,BO=[]):
        $ BO = TotalGirls[:]
        while BO:
                $ BO[0].Love = 1000 if BO[0].Love > 1000 else BO[0].Love
                $ BO[0].Obed = 1000 if BO[0].Obed > 1000 else BO[0].Obed
                $ BO[0].Inbt = 1000 if BO[0].Inbt > 1000 else BO[0].Inbt
                $ BO[0].Lust = 99 if BO[0].Lust > 99 else BO[0].Lust

                $ BO[0].Love = 0 if BO[0].Love < 0 else BO[0].Love
                $ BO[0].Obed = 0 if BO[0].Obed < 0 else BO[0].Obed
                $ BO[0].Inbt = 0 if BO[0].Inbt < 0 else BO[0].Inbt
                $ BO[0].Lust = 0 if BO[0].Lust < 0 else BO[0].Lust

                $ BO[0].Action = BO[0].MaxAction if BO[0].Action > BO[0].MaxAction else BO[0].Action
                $ BO[0].Action = 0 if BO[0].Action < 0 else BO[0].Action

                $ BO[0].Addict = 100 if BO[0].Addict > 100 else BO[0].Addict
                $ BO[0].Addict = 0 if BO[0].Addict < 0 else BO[0].Addict
                $ BO[0].Addictionrate = 10 if BO[0].Addictionrate > 10 else BO[0].Addictionrate
                $ BO[0].Addictionrate = 0 if BO[0].Addictionrate < 0 else BO[0].Addictionrate
                $ BO[0].Thirst = 100 if BO[0].Thirst > 100 else BO[0].Thirst
                $ BO[0].Thirst = 0 if BO[0].Thirst < 0 else BO[0].Thirst

                if BO[0].Forced and BO[0].ForcedCount < 10:
                            $ BO[0].ForcedCount += 1
                if BO[0].Tag == "Laura":
                            $ LauraX.ScentTimer = 0
                $ BO.remove(BO[0])

        #Player
        $ Player.Focus = 99 if Player.Focus > 99 else Player.Focus
        $ Player.Focus = 0 if Player.Focus < 0 else Player.Focus
        $ Player.Semen = Player.Semen_Max if Player.Semen > Player.Semen_Max else Player.Semen
        $ Player.Semen = 0 if Player.Semen < 0 else Player.Semen

        if Total:
                $ MultiAction = 1
                $ Player.DrainWord("cockout")
                $ Player.DrainWord("nude")
                $ Trigger = 0
                $ Trigger2 = 0
                $ Trigger3 = 0
                $ Trigger4 = 0
                $ Trigger5 = 0
                $ ThreeCount = 100
                $ Partner = 0
                $ Player.FocusX = 0
        return

label Wait (Outfit = 1, Lights = 1, BO=[]):
    # If Outfit is 1, it changes her clothes to the scheduled default, otherwise it does not.
    # If Lights is 1, it removes the blackout screen, otherwise it does not.
    show blackscreen onlayer black

    call Checkout(1)
    $ Player.XP = 3330 if Player.XP > 3330 else Player.XP

    if Time_Count < 3:  #not sleep time
                $ Time_Count += 1
    else:
        # Things that happen when you sleep
                $ del Party[:]

                #Setting the time/date
                $ Time_Count = 0
                $ Day += 1
                if Weekday < 6:
                    $ Weekday += 1
                else:
                    $ Weekday = 0
                $ DayofWeek = Week[Weekday]

                if PunishmentX: #Event[3]:
                        #If you're under punishment
                        $ Player.Cash += int(Player.Income / 2)
                        if PunishmentX == 1:
                            "Your punishment from Xavier has expired."
                        $ PunishmentX -= 1
                else:
                        #otherwise, you make money
                        $ Player.Cash += Player.Income


        # Things about you when you sleep:
                $ Player.Semen = Player.Semen_Max
                $ Player.Spunk = 0
                $ Player.Rep = 0 if Player.Rep < 0 else Player.Rep
                $ Player.Rep += 10 if Player.Rep < 800 else 0
                $ Player.Rep = 1000 if Player.Rep > 1000 else Player.Rep

                $ TotalSEXP = 0 #zeros out so that next bit and add to it

                #Clearing colognes
                if "mandrill" in Player.Traits:
                        $ Player.Traits.remove("mandrill")
                if "purple" in Player.Traits:
                        $ Player.Traits.remove("purple")
                if "corruption" in Player.Traits:
                        $ Player.Traits.remove("corruption")
                call Favorite_Actions # Sets the girl's favorite activities once per day

        # Things about the girls when you sleep:

                if "halloween" in Player.DailyActions:
                        if RogueX.Hair == "cosplay":
                            if "evo" in RogueX.DailyActions:
                                $ RogueX.Hair = "evo"
                            elif "wet" in RogueX.DailyActions:
                                $ RogueX.Hair = "wet"
                        if JeanX.Hair == "pony":
                            if "short" in JeanX.DailyActions:
                                $ JeanX.Hair = "short"
                            elif "wet" in JeanX.DailyActions:
                                $ JeanX.Hair = "wet"
                        if EmmaX.Hair == "hat":
                                $ EmmaX.Hair = "wave"
                        elif EmmaX.Hair == "hat wet":
                                $ EmmaX.Hair = "wet"
                        if StormX.Hair == "short":
                            if "long" in StormX.DailyActions:
                                $ StormX.Hair = "long"
                            elif "mohawk" in StormX.DailyActions:
                                $ StormX.Hair = "mohawk"
                            elif "wet" in StormX.DailyActions:
                                $ StormX.Hair = "wet"
                            elif "wethawk" in StormX.DailyActions:
                                $ StormX.Hair = "wethawk"

                $ BO = TotalGirls[:]
                while BO:
                        #loops through and makes choices.
                        if BO[0] in ActiveGirls and BO[0].Loc != bg_current:
                                $ BO[0].Loc = BO[0].Home
                        if BO[0].Todo:
                                call Todo(BO[0])
                        $ BO[0].Outfit = "sleep"
                        $ BO[0].OutfitChange("sleep")

                        #Addiction
                        $ BO[0].Addict += BO[0].Addictionrate   #(0-10)
                        $ BO[0].Addict -= (3*BO[0].Resistance)  #(0,3,6, or 9)
                        if "nonaddictive" in Player.Traits:
                                    $ BO[0].Addictionrate -= 2
                                    $ BO[0].Addict -= 5
                        if "addictive" not in Player.Traits:
                                    $ BO[0].Addictionrate -= BO[0].Resistance
                                    if BO[0] != RogueX and BO[0].Addictionrate >= 3:
                                            # further bonus for anyone other than Rogue
                                            $ BO[0].Addictionrate -= BO[0].Resistance

                        $ BO[0].ForcedCount -= 1 if BO[0].ForcedCount > 0 else 0
                        if BO[0].ForcedCount > 0:
                                $ BO[0].ForcedCount -= 1 if ApprovalCheck(BO[0], 1000, "LO") else 0
                        $ BO[0].Action = BO[0].MaxAction

                        $ BO[0].Rep = 0 if BO[0].Rep < 0 else BO[0].Rep
                        $ BO[0].Rep += 10 if BO[0].Rep < 800 else 0
                        $ BO[0].Rep = 1000 if BO[0].Rep > 1000 else BO[0].Rep

                        $ BO[0].Lust -= 5 if BO[0].Lust >= 50 else 0
                        $ TotalSEXP += BO[0].SEXP #tabulates total based on combined score

                        if BO[0].SEXP >= 15:
                                #raises thirst if you've had sex before
                                if BO[0].SEXP >= 50:
                                    $ BO[0].Thirst += 8 if BO[0].Thirst <= 70 else 4
                                elif BO[0].SEXP >= 25:
                                    $ BO[0].Thirst += 5 if BO[0].Thirst <= 60 else 2
                                else:
                                    $ BO[0].Thirst += 3 if BO[0].Thirst <= 50 else 1

                                $ BO[0].Thirst -= 5 if BO[0].Break[0] else 0
                                $ BO[0].Thirst += 1 if BO[0].Lust >= 50 else 0

                        if "gonnafap" in BO[0].DailyActions and BO[0].Loc != bg_current:
                                #if it's morning and she wanted to fap yesterday, so she did. . .
                                $ BO[0].Lust = 25
                                $ BO[0].Thirst -= int(BO[0].Thirst/2) if BO[0].Thirst >= 50 else int(BO[0].Thirst/4)
                        elif "wannafap" in BO[0].DailyActions:
                                #if it's morning and she didn't get to fap yesterday. . .
                                $ BO[0].Thirst += 10 if BO[0].Thirst <= 50 else 5

                        $ BO[0].Break[0] -= 1 if BO[0].Break[0] > 0 else 0

                        $ del BO[0].Spunk[:]

                        if "lover" in BO[0].Petnames and BO[0].Love > 800:
                                $ BO[0].Love += 10
                        if "master" in BO[0].Petnames and BO[0].Obed > 600:
                                $ BO[0].Obed += 10
                        if "fuck buddy" in BO[0].Petnames:
                                $ BO[0].Inbt += 10

                        $ BO[0].SluttyClothes()   #checks to see if they want to change their default look

                        if BO[0].Tag == "Jean":
                                if BO[0].Love < 1000 and BO[0].StatStore > 0:
                                        #for Jean, after her obedience raises above 500, it starts filling her Love stat from her Stored stat
                                        if BO[0].Obed >= 900:
                                                $ BO[0].Love += 10
                                                $ BO[0].StatStore -= 10
                                        elif BO[0].Obed >= 700:
                                                $ BO[0].Love += 5
                                                $ BO[0].StatStore -= 5
                                        elif BO[0].Obed >= 500:
                                                $ BO[0].Love += 1
                                                $ BO[0].StatStore -= 1
                                if BO[0].Rep <= 800 and "nowhammy" not in JeanX.Traits:
                                        #she mindwipes students to reset her reputation
                                        $ BO[0].Rep = 800

                        if "Jeaned" in BO[0].Traits:
                                # fixes if the girl's like-stats have been whammied
                                $ BO[0].Traits.remove("Jeaned") #got whammied tag
                                $ BO[0].LikeJean = getattr(JeanX,"LikeS"+BO[0].Tag) #To restore to original values. . .

                        $ BO.remove(BO[0])
    #End of things when you sleep

    # Things that happen every time you wait
    #Things that are about you:
    $ Player.Semen += 1
    $ MultiAction = 1
    $ Player.Focus -= 5 if Player.Focus >= 10 else 0
    $ Situation = 0
    $ Current_Time = Time_Options[(Time_Count)]
    $ Round = 100
    # Clears out recent and daily actions
    $ del Player.RecentActions[:]
    if Time_Count == 0:
            $ del Player.DailyActions[:]
    call Taboo_Level(0)
    call GirlWaitUp #checks girls attraction based on who's in the room

    #Things that are about the girls:      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if Time_Count == 3:
            #if it was just Evening, check to see if they studied
            call Study_Time
    $ BO = TotalGirls[:]
    while BO:
            #cycles through each girl possible

            $ BO[0].Action += 1 if Time_Count != 0 else 0  #not morning

            $ BO[0].OCount = 0
            if BO[0].Lust >= 70 or BO[0].Thirst >= 30 or (renpy.random.randint(1, 40) + BO[0].Lust)>= 70:
                        # checks if she wants to fap
                        if "nofap" in BO[0].Traits:
                                $ BO[0].AddWord(1,0,"wannafap",0,0) #adds "wannafap" tag to daily
                        else:
                                $ BO[0].AddWord(1,0,"gonnafap",0,0) #adds "wannafap" tag to daily

            if "les" in BO[0].RecentActions: #if she had a lesbian encounter without you. . .
                        $ BO[0].Thirst -= int(BO[0].Thirst/2)
                        $ BO[0].Lust = 20

            #Resets her flirt  options
            $ BO[0].Chat[5] = 0
            #Resets her addiction fix attempts            :
            $ BO[0].Event[3] -= 1 if BO[0].Event[3] else 0 #resets her addiction fix, takes at least five turns before she hassles you again

            $ BO[0].Forced = 0
            if BO[0].Loc == "bg classroom" or BO[0].Loc == "bg dangerroom" or BO[0].Loc == "bg teacher":
                    $ BO[0].XP += 10
            elif (bg_current == "bg classroom" or bg_current == "bg dangerroom") and BO[0].Loc == "nearby":
                    $ BO[0].XP += 10
            elif BO[0].Loc == "bg showerroom":
                    call Remove_Girl(BO[0])

            if BO[0] in ActiveGirls and "met" not in BO[0].History:
                $ ActiveGirls.remove(BO[0])

            #Appearance clean-up
            $ BO[0].Blush = 0
            $ BO[0].Water = 0
            $ BO[0].Held = 0

            #Reduced addiction
            $ BO[0].Addict += BO[0].Addictionrate # +0-10
            $ BO[0].Addictionrate -= BO[0].Resistance if BO[0].Addictionrate > 3 else 0         #if rate is above 3, drop it by an extra Resistance

            #Adjusts shame rate
            if BO[0].Taboo and BO[0].Shame and BO[0] in ActiveGirls:
                        if BO[0].Loc == "bg dangerroom":
                                $ BO[0].Shame -= 10 if BO[0].Shame >=10 else BO[0].Shame
                        $ Count = int((BO[0].Taboo * BO[0].Shame) / 200)
                        $ BO[0].Statup("Obed", 90, Count)
                        $ BO[0].Statup("Inbt", 90, Count)
                        $ BO[0].Rep -= Count

            #subtracts BO[0].Love by 5* the number of recent unsatisfieds
            $ BO[0].Love -= 5 * BO[0].RecentActions.count("unsatisfied")

            # Clears out recent and daily actions
            $ del BO[0].RecentActions[:]
            if "angry" in BO[0].DailyActions:
                        $ BO[0].RecentActions.append("angry")
            if Time_Count == 0:
                        $ del BO[0].DailyActions[:]
            elif Time_Count == 3 and "yesdate" in BO[0].DailyActions and "stoodup" not in BO[0].Traits:
                        #if you stood her up for a date. . .
                        $ Player.DrainWord("yesdate",0,1)
                        $ BO[0].Traits.append("stoodup")

            if BO[0].Loose < 2:  #checks how tight the girl's asshole is
                        if (BO[0].Anal + BO[0].DildoA + BO[0].Plug) >= 15:
                                $ BO[0].Loose = 2
                        elif (BO[0].Anal + BO[0].DildoA + BO[0].Plug) >= 3:
                                $ BO[0].Loose = 1

            $ BO[0].XP = 3330 if BO[0].XP > 3330 else BO[0].XP #caps XP
            if BO[0].XP >= BO[0].XPgoal and BO[0].Lvl < 10:
                        $ BO[0].XPgoal = int((1.15 * BO[0].XPgoal) + 100)
                        $ BO[0].Lvl += 1
                        $ BO[0].StatPoints += 1
                        "[BO[0].Name]'s leveled up! I bet she has some new tricks to learn."
                        if BO[0].Lvl == 10:
                                "[BO[0].Name]'s reached max level!"
            if BO[0] == LauraX:
                        $ BO[0].Addictionrate -= (2 * BO[0].Resistance) if BO[0].Addictionrate > 5 else 0
            elif BO[0] == JubesX and "met" in JubesX.History:
                        $ BO[0].Addictionrate = 2 if BO[0].Addictionrate < 2 else BO[0].Addictionrate
                        if "sunshine" not in JubesX.History:
                                #keeps her getting too hungry before Sunshine event
                                $ BO[0].Addict = 40 if BO[0].Addict > 40 else BO[0].Addict

            $ BO[0].DefaultFaces()      #sets a default face based on conditions
            $ BO[0].FaceChange(5)       #resets face

            $ BO.remove(BO[0])
    #end loop

    call Girls_Schedule #schedules all the girls. . .

    if Outfit:
            $ BO = TotalGirls[:]
            while BO:
                    #loops through and makes choices.
                    $ BO[0].OutfitChange(BO[0].OutfitDay)
                    $ BO.remove(BO[0])

    #Player leveling check
    if Player.Lvl < 10 and Player.XP >= Player.XPgoal:
            $ Player.XPgoal = int((1.15 * Player.XPgoal) + 100)
            $ Player.Lvl += 1
            $ Player.StatPoints += 1
            if Player.Lvl <5:
                $ Count = 1
            elif Player.Lvl <9:
                $ Count = 2
            else:
                $ Count = 3
            $ Player.Income += Count
            "You've leveled up!"
            "Xavier has noticed your achievements and raised your stipend by $[Count] per day. It is now $[Player.Income]."
            if Player.Lvl == 10:
                "You've reached max level!"

    #End Hourly actions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    call LesCheck #checks to see if the girls hook up with each other. . .
    #end wait items:

    call Checkout
    if Time_Count < 3:
            hide NightMask onlayer nightmask
    if Lights:
            hide blackscreen onlayer black
    return

label Girls_Schedule(Girls = [], Clothes = 1, Location = 1, LocTemp = 0):
        # Set the girl's natural movements
        # If not Clothes, don't bother with her outfit in the schedule
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        if not Girls:
                #fills list unless a specific girl is sent
                $ Girls = ActiveGirls[:]
        elif Girls[0] not in TotalGirls:
                return
        while Girls:
                if Girls[0] in Party and Clothes != 2 or not Location:
                        #if she's in a party, never mind
                        pass
                elif Clothes != 2 and "sleepover" in Girls[0].Traits and Time_Count == 0:
                        #she slept over, so just forget this for now
                        pass
                else:
                        if (Time_Count == 0 and Clothes and Round >= 90) or Clothes == 2:
                                #In the morning, or if ordered to reschedule, pick an outfit for the day.
                                $ Girls[0].OutfitDay = 0
                                if Girls[0].Break[0]:
                                    pass #she won't pick clothes if she's mad at you
                                elif Girls[0].Clothing[Weekday] == 1:
                                        $ Girls[0].OutfitDay = "casual1"
                                elif Girls[0].Clothing[Weekday] == 2:
                                        $ Girls[0].OutfitDay = "casual2"
                                elif Girls[0].Clothing[Weekday] == 3 and Girls[0].Custom1[0]:
                                        $ Girls[0].OutfitDay = "custom1"
                                elif Girls[0].Clothing[Weekday] == 4:
                                        $ Girls[0].OutfitDay = "gym"
                                elif Girls[0].Clothing[Weekday] == 5 and Girls[0].Custom2[0]:
                                        $ Girls[0].OutfitDay = "custom2"
                                elif Girls[0].Clothing[Weekday] == 6 and Girls[0].Custom3[0]:
                                        $ Girls[0].OutfitDay = "custom3"
                                if not Girls[0].OutfitDay:
                                        $ Options = ["casual1", "casual2"]
                                        if not Girls[0].Break[0]:
                                                $ Options.append("custom1") if Girls[0].Custom1[0] == 2 else Options
                                                $ Options.append("custom2") if Girls[0].Custom2[0] == 2 else Options
                                                $ Options.append("custom3") if Girls[0].Custom3[0] == 2 else Options
                                        $ renpy.random.shuffle(Options)
                                        $ Girls[0].OutfitDay = Options[0]
                                        $ del Options[:]
                                $ Girls[0].Outfit = Girls[0].OutfitDay
                        #End clothing portion

                        #Location portion
                        $ LocTemp = Girls[0].Loc
                        if Girls[0] not in ActiveGirls:
                                $ LocTemp = "hold"
                                $ Girls[0].Loc = "hold"
                        elif Girls[0] in Party or Girls[0].Loc == "hold":
                                pass
                        else:
                                $ Girls[0].Loc = Girls[0].Schedule[Weekday][Time_Count]
                                if Girls[0] == JubesX and JubesX.Addict > 60:
                                                #Jubliee will not leave her room voluntarily if it's higher than 60
                                                $ JubesX.Loc = JubesX.Home

                        if Girls[0].Loc != LocTemp and Girls[0] not in Party:
                                #if she moved
                                if LocTemp == bg_current:
                                        if ApprovalCheck(Girls[0], 1200) and Girls[0].Loc not in ("bg classroom","bg teacher","bg dangerroom"):
                                                # if she's contented, then she just sticks around
                                                $ Girls[0].Loc = LocTemp
                                        else:
                                                #If she was where you were, but left
                                                $ Girls[0].RecentActions.append("leaving")
                                elif Girls[0].Loc == bg_current:
                                                #If she's showed up
                                                $ Girls[0].RecentActions.append("arriving")
                        if Girls[0] in Nearby:
                                                $ Nearby.remove(Girls[0])
                if Girls[0].Loc == "bg teacher":
                        call AltClothes(Girls[0],8) #Sets teaching outfit
                        $ Girls[0].OutfitChange()

                $ Girls.remove(Girls[0])
        #end while looping
        return

label Study_Time(BO=[],Studiers=[]):
    #this finds girls that are alone in their rooms and has them study together in the evenings.
    $ BO = TotalGirls[:]
    while BO:
            if BO[0].Loc != bg_current and BO[0].Loc in PersonalRooms:
                    #if they aren't with you, and are in a character room, they study
                    $ Studiers.append(BO[0])
            $ BO.remove(BO[0])
    if len(Studiers) < 2:
            #returns if there aren't enough available girls
            return

    $ renpy.random.shuffle(Studiers)
    $ Studiers[0].GLG(Studiers[1],800,5,1)
    $ Studiers[1].GLG(Studiers[0],800,5,1)

    $ Studiers[0].XP += 5
    $ Studiers[1].XP += 5
    return

label Todo(Chr=0): #rkeljs
        #Actions checked each night
        #causes her to grow her pubes out
        if Chr not in TotalGirls:
            return

        if Chr == LauraX:
                if "pubes" in Chr.Todo:
                        $ Chr.Pubes = 1
                        $ Chr.Todo.remove("pubes")

                if "mission" in Chr.Todo: #puts her on ice until a week after the first meeting
                        $ Chr.PubeC -= 1
                        if Chr.PubeC >= 1:
                                $ Chr.Loc = "hold"
                        else:
                                $ Chr.History.append("dress0") #starts dress event where you'll meet again
                                $ Chr.Todo.remove("mission")
                if "cleanhouse" in Chr.Todo:
                        #if you promised to break up with other girls, this counts it down
                        if LauraX in Player.Harem or not Player.Harem:
                                # mission complete
                                $ LauraX.Event[5] = 2
                                $ Chr.Todo.remove("cleanhouse")
                        $ LauraX.Event[5] -= 1 if LauraX.Event[5] > 1 else 0
        else:
                if "pubes" in Chr.Todo:
                        $ Chr.PubeC -= 1
                        if Chr.PubeC >= 1:
                                pass
                        else:
                                $ Chr.Pubes = 1
                                $ Chr.Todo.remove("pubes")
        #causes her to wax her pubes
        if "shave" in Chr.Todo:
                $ Chr.Pubes = 0
                $ Chr.Todo.remove("shave")

        if "hair" in Chr.Todo:
                if StormX.Hair == "long":
                        $ StormX.Hair = "mohawk"
                elif StormX.Hair == "wethawk":
                        $ StormX.Hair = "wet"
                elif StormX.Hair == "wet":
                        $ StormX.Hair = "wethawk"
                else:
                        $ StormX.Hair = "long"
                $ Chr.Todo.remove("hair")

        #causes her to put in piercings
        if "ring" in Chr.Todo:
                $ Chr.Pierce = "ring"
                $ Chr.Todo.remove("ring")
        if "barbell" in Chr.Todo:
                $ Chr.Pierce = "barbell"
                $ Chr.Todo.remove("barbell")
        return

label EventCalls(EGirls=[]): #rkeljs
        call Present_Check
        $ D20 = renpy.random.randint(1, 20)
        call Get_Dressed

        if Time_Count == 2 and "yesdate" in Player.DailyActions:
            if bg_current == "bg campus":
                    call DateNight
                    $ Player.DrainWord("yesdate",0,1)
                    return
            else:
                    menu:
                        "You have a date to get to, head for the square?"
                        "Yes":
                            $ renpy.pop_call()
                            jump Campus_Entry
                        "No":
                            "Suit yourself. . ."

        if Day < 3 or Round <= 10: #was day 5
                    #Disables events when it's too early in the game or the turn is about to end
                    return

    #Activates Jubes meet
        if JubesX in ActiveGirls:
                    #you haven't completed Jubes's intro, but have met Storm
                    if Time_Count < 3 and "sunshine" not in JubesX.History and "traveling" in Player.RecentActions and bg_current in ("bg classroom","bg dangerroom","bg campus","bg pool"):
                            jump Jubes_Sunshine
                            return
                    elif "mall" not in Player.History and "sunshine" in JubesX.History and Time_Count < 3 and JubesX.Addict < 50:
                            call Jubes_Mall
                            jump Misplaced
                    elif not JubesX.Event[1] and JubesX.Addict < 50:
                            #if she hasn't had her addiction event yet. . .
                            $ JubesX.Addict += 5
    #End Jubes meet

    #Activates Kitty meet
        if KittyX in ActiveGirls:
                if "Kate" not in KittyX.Names and KittyX.Inbt >= 500 and KittyX.Loc == bg_current:
                        #She calls herself Kate now.
                        call Kitty_Kate
                        return
        else:
                if "traveling" in Player.RecentActions and "met" not in KittyX.History and bg_current == "bg classroom":
                        jump KittyMeet
                        return

    #Activates Laura meet
        if LauraX in ActiveGirls:
                    pass
        elif "met" not in LauraX.History and "traveling" in Player.RecentActions:
                    if bg_current == "bg dangerroom":
                            if Day >= 7 and "dress0" not in LauraX.History and "mission" not in LauraX.Todo:
                                    call LauraMeet
                                    return

                    #Calls Kitty starting dressup event
                    if Time_Count < 3 and "met" in KittyX.History:
                            if "dress0" in LauraX.History:
                                    call Laura_Dressup
                                    return

    #Activates Emma meet and class stuff
        if EmmaX in ActiveGirls:
                if bg_current == "bg classroom" and Time_Count == 2 and Weekday in (0,2,4):
                        #If you've met Emma, it's evening on a school night, mon/tue/fri
                        if "traveling" in Player.RecentActions and not Party:
                                #if you are in motion,
                                if "classcaught" not in EmmaX.History:
                                        #if first time you catch her, 100% chance
                                        jump Emma_Caught_Classroom
                                        return
                                elif D20 <= 10 and "gonnafap" in EmmaX.DailyActions:
                                        #50/50 chance of catching Emma in class
                                        jump Emma_Caught_Classroom
                                        return

                        if "detention" in Player.Traits and not Party:
                                        jump Emma_Detention

                        if Round >= 70:
                                #if you are in class and not travelling. . .
                                $ EmmaX.Loc = "bg classroom"
        else:
                #Emma is not in ActiveGirls
                if Day >= 4 and "met" not in EmmaX.History and "traveling" in Player.RecentActions and bg_current == "bg classroom" and Weekday < 5:   #was day 6
                        jump EmmaMeet
                        return
    #End Emma meet

    #Activates Storm meet
        if StormX in ActiveGirls:
                    if bg_current == "bg classroom" and StormX.Loc == "bg teacher" and "Peter" in StormX.History and "traveling" in Player.RecentActions:
                            #if you told her your name was Peter Parker
                            call Storm_Peter
                            return
                    if bg_current == "bg classroom" and Time_Count == 2 and Weekday in (1,3):
                            if "mohawk" not in StormX.History and "traveling" not in Player.RecentActions and ApprovalCheck(StormX, 200, "I"):
                                    jump Storm_Hairtalk
                                    return
                            if Round >= 70:
                                    #if you are in class and not travelling. . .
                                    $ StormX.Loc = "bg classroom"
                    if Time_Count == 3 and bg_current == "bg pool" and "poolnight" in Player.History:
                            if "sex friend" not in StormX.Petnames or (D20 < 5 and "poolnight" not in Player.RecentActions):
                                    #call's Storm's skinny dipping thing at night if it's the first time or a 25% chance.
                                    call Storm_Poolnight
                                    return


        elif "met" not in StormX.History and "met" in JeanX.History:
                    if bg_current == "bg player" and "attic" not in Player.History and "noise" not in Player.History:
                            #You hadn't asked Emma yet
                            call StormMeetPrelude
                            return
                    elif bg_current == "bg classroom" and "noise" in Player.History and "traveling" in Player.RecentActions:
                            #You hadn't asked Emma yet
                            call StormMeetAsk
                            return
                    elif bg_current == "bg player" and Time_Count < 2 and 0 < StormX.Break[0] <= 101 and "traveling" in Player.RecentActions:
                            #Break is being used as a 3-day countdown to when you are forced to meet Storm.
                            call StormMeetWater
                            jump Misplaced
    #End Storm meet


    #skips events if you were just now following someone
        if "goto" in Player.RecentActions:
                $ Player.RecentActions.remove("goto")
                return

    #locked door check
        if "locked" in Player.Traits:
                #exits if the door is locked, but maybe open this up a bit later.
                return

        if "micro" not in Player.History and Day > 13:
                #this is to offer players microtransactions
                call Microtransactions_Intro

    #Start relationship checks

    #activates if you haven't done an addiction event today
        if "fix" not in Player.DailyActions:
                call AddictCheck

        if bg_current == "bg_player":
                #only activates while in player room
                $ EGirls = ActiveGirls[:]
                while EGirls and "asked meet" not in EGirls[0].DailyActions:
                    #loops through girls. If "asked meet" in her actions, it kicks that one girl out
                    if "asked meet" in EGirls[0].DailyActions:
                            $ EGirls = ["x",EGirls[0]]
                    $ EGirls.remove(EGirls[0])

        if not EGirls:
                #these events only play if you lack a prior commitment.

                #This scene has Girl A asks Girl B off camera if she wants to have a poly Relationship with you
                    call ShareCheck

                #Activates if any girl caught you cheating
                    #checks to see if any of the girls noticed you cheating on them
                    #returns if not
                    call CheatCheck

                #checks to see if a girl wants to jump you. . .
                    call JumperCheck

                #Checks to see if any girls want to fap.
                    #If they have "wannafap" in their daily, and "nofap" in their traits, and are not in the room, they will ask you
                    #otherwise, they will automatically fap. If you meet them after this, they will be fapping,
                    #if you keep them busy, they will do it overnight
                    if Time_Count >= 2 and "fapcall" not in Player.DailyActions:
                            #if it's evening or later and nobody has yet called you about fapping. . .
                            $ EGirls = ActiveGirls[:]
                            $ renpy.random.shuffle(EGirls)
                            while EGirls:
                                if "wannafap" in EGirls[0].DailyActions:
                                        #if she's wants to fap and is not in the room with you
                                        call CalltoFap(EGirls[0]) #checks to see if she's allowed
                                        if not EGirls:
                                                return
                                $ EGirls.remove(EGirls[0])
                    #end fap call check

        $ EGirls = ActiveGirls[:] if not EGirls else EGirls
        $ renpy.random.shuffle(EGirls)

        #fills list and then randomly shuffles it.
        while EGirls:
                if "relationship" not in EGirls[0].DailyActions:
                        if "stoodup" in EGirls[0].Traits: #you stood her up
                                        call Date_Stood_Up(EGirls[0])
                                        return
                        if EGirls[0].Break[0] or "angry" in EGirls[0].DailyActions:
                                        #skip all this if you're broken up
                                        pass
                        elif not EGirls[0].Event[0] and EGirls[0].Sleep >= 5:
                                if EGirls[0].Loc == bg_current or EGirls[0] in Party:
                                    call girl_key(EGirls[0])

                                    return
                        elif EGirls[0] == JubesX: #remove once she has scenes
                                    pass
                        elif EGirls[0] == JeanX:
                            if bg_current != "bg classroom":
                                if JeanX.Obed >= 500 and "sir" not in JeanX.History:
                                        call Jean_Sub
                                elif JeanX.Obed >= 800 and "master" not in JeanX.History:
                                        call Jean_Master
                                elif JeanX.Love >= 500 and "sexfriend" not in JeanX.History:
                                        call Jean_Like
                                elif JeanX.Love >= 800 and JeanX.Obed >= 600 and not JeanX.Event[5]:
                                        call Jean_Love
                                elif "daddy" not in JeanX.Petnames and ApprovalCheck(JeanX, 750, "L"):
                                        if (bg_current == EGirls[0].Home or bg_current == "bg player") and EGirls[0].Loc == bg_current:
                                            call girl_daddy(JeanX)
                                return
                        elif "boyfriend" not in EGirls[0].Petnames and EGirls[0].Love >= 800 and EGirls[0].Event[5] != 20 and EGirls[0].Tag + "No" not in Player.Traits: # EGirls[0].Event[5]
                                # EGirls[0].Event[5] is 20 if you refused due to other girlfriend
                                # if "RogueNo" it means you can't date her.
                                if EGirls[0] == LauraX and LauraX.Event[5] == 3:
                                        #This gets called when Laura asks you to break up with the other girls
                                        call Laura_Cleanhouse
                                elif Player.Harem and EGirls[0].Tag + "Yes" not in Player.Traits:
                                        call Poly_Start(EGirls[0])
                                elif bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call girl_boyfriend(EGirls[0])
                                else:
                                        call AskedMeet(EGirls[0],"bemused")
                                return
                        elif "lover" not in EGirls[0].Petnames and EGirls[0].Love >= 950 and EGirls[0].Event[6] < 15: # EGirls[0].Event[6]
                                # <15 is also != 20, but double check that there isn't more to that. . .K_Event[6] != 20? and E_Event[6] != 20:
                                if bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_Love"
                                else:
                                        call AskedMeet(EGirls[0],"bemused")
                                return
                        elif "sir" not in EGirls[0].History and "sir" not in EGirls[0].Petnames and EGirls[0].Obed >= 500: # EGirls[0].Event[7]
                                if bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_Sub"
                                else:
                                        call AskedMeet(EGirls[0],"bemused")
                                return
                        elif "master" not in EGirls[0].History and "master" not in EGirls[0].Petnames and EGirls[0].Obed >= 850 and EGirls[0].Event[8] < 2:
                                #and EGirls[0].Event[8] < 2, remove that bit when Rogue's scene is updated to not need it.
                                if bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_Master"
                                else:
                                        call AskedMeet(EGirls[0],"bemused")
                                return
                        elif "daddy" not in EGirls[0].Petnames and ApprovalCheck(EGirls[0], 750, "L") and ApprovalCheck(EGirls[0], 500, "O") and ApprovalCheck(EGirls[0], 500, "I"): # EGirls[0].Event[5]
                                if (bg_current == EGirls[0].Home or bg_current == "bg player") and EGirls[0].Loc == bg_current:
                                        call girl_daddy(EGirls[0])
                                return
                        elif "sex friend" not in EGirls[0].Petnames and EGirls[0].Inbt >= 500: # EGirls[0].Event[9]  Fix this one
                                if EGirls[0] == EmmaX:
                                    if bg_current == "bg classroom" and (EmmaX.Loc == "bg teacher" or EmmaX.Loc == "bg classroom") and Time_Count == 2:
                                            call Emma_Sexfriend
                                            return
                                elif EGirls[0] == StormX:
                                    if StormX.Event[9]:
                                            pass
                                    elif "traveling" in Player.RecentActions and Time_Count < 2:
                                            call Storm_Sexfriend
                                            return
                                elif bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_Sexfriend"
                                        return
                                elif EGirls[0] in Player.Harem and EGirls[0].Loc == bg_current:
                                        call expression EGirls[0].Tag + "_Sexfriend"
                                        return
                                elif EGirls[0] == LauraX:
                                        call expression EGirls[0].Tag + "_Sexfriend"
                                        return
                        elif "fuck buddy" not in EGirls[0].Petnames and EGirls[0].Inbt >= 800: # EGirls[0].Event[10]  Fix this one
                                if EGirls[0] == RogueX:
                                    if bg_current != EGirls[0].Loc:
                                        call expression EGirls[0].Tag + "_Fuckbuddy"
                                        return
                                elif EGirls[0] == LauraX:
                                    if bg_current == "bg player" and EGirls[0].Loc != bg_current:
                                        call expression EGirls[0].Tag + "_Fuckbuddy"
                                        return
                                elif EGirls[0] == StormX:
                                    if bg_current == "bg classroom" and Time_Count == 2 and Weekday in (1,3):
                                        call Storm_Fuckbuddy
                                        return
                                elif bg_current == EGirls[0].Home or bg_current == "bg player":
                                        call expression EGirls[0].Tag + "_Fuckbuddy"
                                        return
                                elif EGirls[0] in Player.Harem and EGirls[0].Loc == bg_current:
                                        call expression EGirls[0].Tag + "_Fuckbuddy"
                                        return
                $ EGirls.remove(EGirls[0])

        #activates if you have done an addiction event today
        if "fix" in Player.DailyActions:
                call AddictCheck
        # EndPrimary Event Calls / / / / / / / / / / / / / / / / / Drops down to. . .

label QuickEvents(EGirls=[]):
        #These events get checked every screen refresh
        $ Options = []
        call Present_Check

        $ EGirls = TotalGirls[:]
        $ renpy.random.shuffle(EGirls)
        while EGirls:
                if EGirls[0].Loc == bg_current:
                        if EGirls[0].Lust >= 90:
                                $ EGirls[0].Blush = 1
                                $ EGirls[0].Wet = 2
                        elif EGirls[0].Lust >= 60:
                                $ EGirls[0].Blush = 1
                                $ EGirls[0].Wet = 1
                        else:
                                $ EGirls[0].Wet = 0

                        #Girl reacts to getting horny
                        if Taboo and EGirls[0].Lust >= 75:
                                if EGirls[0].Inbt > 800 or "exhibitionist" in EGirls[0].Traits:
                                        "[EGirls[0].Name] gets a sly smile on her face and squirms a bit."
                                elif EGirls[0].Inbt > 500 and EGirls[0].Lust < 90:
                                        "[EGirls[0].Name] looks a bit flushed and uncomfortable."
                                elif bg_current != "bg showerroom":
                                        "[EGirls[0].Name] gets an embarrassed look on her face and suddenly leaves the room."
                                        #"gonnafap" in Chr.DailyActions
                                        call Remove_Girl(EGirls[0])
                                        call Set_The_Scene
                                        $ EGirls[0].Loc = EGirls[0].Home if bg_current != EGirls[0].Home else "bg campus"
                                        if "nofap" in EGirls[0].Traits:
                                                $ EGirls[0].AddWord(1,0,"wannafap",0,0) #adds "wannafap" tag to daily
                                                call CalltoFap(EGirls[0]) #checks to see if she's allowed
                                        else:
                                                $ EGirls[0].AddWord(1,0,"gonnafap",0,0) #adds "wannafap" tag to daily
                else:
                        #if Girl is not around
                        if EGirls[0].Loc == "bg showerroom" and "showered" in EGirls[0].DailyActions:
                                #if she's recently showered and still in the shower, send her elsewhere
                                $ EGirls[0].Loc = EGirls[0].Schedule[Weekday][Time_Count]
                                if EGirls[0] == JubesX and JubesX.Addict > 60:
                                                #Jubliee will not leave her room voluntarily if it's higher than 60
                                                $ JubesX.Loc = JubesX.Home
                                $ EGirls[0].Spunk = []
                                $ EGirls[0].OutfitChange()
                #End girl's Quick Events
                if EGirls:
                        $ EGirls.remove(EGirls[0])
        return

label AskedMeet(Girl = 0, Emotion = "bemused",Why=0): # Use AskedMeet(RogueX,"angry")
    #This asks the player to meet the chosen character later
    if "asked meet" not in Girl.DailyActions and Girl.Loc != bg_current:
                    $ Girl.FaceChange(Emotion)
                    "[Girl.Name] asks if you could meet her in your room later."
                    $ Girl.AddWord(1,"asked meet","asked meet",0,0) # adds "asked meet" to recent and daily
                    $ Player.AddWord(1,0,"meet girl",0,0)
                    if RTR_Toggle:
                            call ReturnToRoom
    return

label ReturnToRoom:
    #used when asked to meet up with a girl
    menu:
        "Return to your room and deal with that?"
        "Yes":
            $ renpy.pop_call() #removes call to this label
            $ renpy.pop_call() #removes call to Events
            jump player_room_entry
        "No":
            pass
    return

menu Tutorial:
    "What did you want to know about?"
    "UI":
        while True:
            menu:
                "Which UI element did you want to hear about?"
                "Relationship Bar":
                        "The bar covering the top left of the screen displays the stats of the primary girl in the scene. These stats are described elsewhere in the tutorial."
                        "If the bar is green, it represents Rogue's stats. If it's dark blue, it represents Kitty's."
                "Focus Button":
                        "You can switch between available girls by hitting the small blue icon to the right of the Relationship Bar."
                        "This changes which girl is currently the focus of your attention. You can do this as often as you like."
                "Inventory":
                        "The small backpack to the left of that is your inventory."
                "Time":
                        "The next panel shows the day since you started, the day of the week, and the time of day."
                        "There are four periods in the day, Morning, Midday, Evening, and Night, representing roughly 4 hours each (not counting sleep time"
                "Menus":
                        "Much of the gameplay choices are made via menus along the left side of the screen."
                        "Don't worry too much about making \"bad\" choices, they are only temporary setbacks."
                        "There are no absolute fail states, and even choices that upset a girl can have eventual payoffs."
                        "Play how you want to play, have fun."
                "Back":
                    jump Tutorial
    "Stats":
        menu Tutorial_Stats:
            "Which stat were you interested in?"
            "Relationship Stats":
                "Stats are what is used to track your progress with the various girls in the mansion."
                while True:
                    menu:
                        "Which Stat would you like to hear about?"
                        "Love Stat":
                                "If you look at the top-left of the screen, there is a red bar."
                                "This represents the girl's \"love level.\""
                                "You can raise this stat by doing things that make the girl happy. This produces a red +X number."
                                $ RogueX.Statup("Love", 200, 1)
                                "You can also lower this number if you do things that make the girl upset, which is represented by a red -X."
                                $ RogueX.Statup("Love", 200, -1)
                        "Obedience Stat":
                                "The blue bar to the right of that is the \"Obedience level.\""
                                "This represents the girl's willingness to do what you want, and raises when you convince her to do something."
                                $ RogueX.Statup("Obed", 200, 1)
                                "It lowers when you push her too far and she refuses."
                                $ RogueX.Statup("Obed", 200, -1)
                        "Inhibition Stat":
                                "The yellow bar to the right of that is the \"Inhibition level.\""
                                "This represent's the girl's own sexual interest, and raises when she decides to do something on her own, or something naughty for the first time."
                                $ RogueX.Statup("Inbt", 200, 1)
                                "It lowers when she becomes overly ashamed, like when caught doing something sexier than she's comfortable with."
                                $ RogueX.Statup("Inbt", 200, -1)
                                "These are the three core relationship stats, and most activities in the game are gated by how high each is, either alone or in combinations."
                                "If you can reach 1000 in all three stats, she will be up for just about anything, although some activities do require special conditions."
                        "Back":
                                jump Tutorial_Stats
            "Sexual stats":
                "There are several stats which are used in sexual encounters."
                while True:
                    menu:
                        "Which Stat would you like to hear about?"
                        "Lust":
                                "The bar underneath \"Love\" represents the girl's \"Lust.\""
                                "This stat raises as she becomes excited, and falls as she gets turned off or after she orgasms (at 100\%)."
                                $ RogueX.Statup("Lust", 200, 1)
                                $ RogueX.Lust -= 1
                        "Player Excitement":
                                "The rather \"suggestive\" bar to the right of Inhibitions represents your own excitement."
                                $ Player.Statup("Focus", 200, 1)
                                $ Player.Focus -= 1
                                "When it reaches 100\%, you orgasm. If you wish to delay this, you can learn to \"focus\" during sex and slow the progression."
                                "The better you get at each sexual activity, the faster these stats will rise."
                                "The bar underneath this represents the amount of times you can \"get it up\" before needing some time out. You can raise this stat when you level."
                                "It's also worth noting that each girl will only be up for doing a certain number of activities in a given time period."
                        "Back":
                                jump Tutorial_Stats
            "Player Stats":
                    "Aside from the sexual ones mentioned above, the player has a few stats of note."
                    "One is his XP. This raises as you study, attend classes, or attend training sessions."
                    "It represents your advancement as a mutant student of the academy. As you gain levels, you gain stat points."
                    "You can spend these to unlock new traits, either refining your powers or your sexual prowess."
                    "The girls also gain traits which unlock new abilities."
                    "You also have an income level, based on the stipend Xavier grants you. This rises as you level, but may be reduced for bad behavior."
            "Addiction":
                    "The Addiction stat is represented by the bar below Obedience. This stat rises as she begins to crave your touch."
                    "It lowers when she comes into physical contact with you, the more intense the contact, the lower the craving gets."
                    "At high Addiction levels, she is highly susceptible to your advances, but will not be happy about it if you press her."
                    "The Addiction Rate is represented by the bar to the right of it. This stat represents how quickly her cravings build, and falls off over time."
                    "There are various ways that you can increase or decrease how addictive your touch becomes to her. Use this capability at your own risk."
                    "If this aspect does not interest you, you can just choose the more benign options to satisfy her cravings until her interest dies down."
            "Back":
                    jump Tutorial
        jump Tutorial_Stats
    "Activities":
        while True:
            menu:
                "So what can you do with your time?"
                "Wait/Sleep":
                        "You can always just \"Wait.\" This causes you to waste time, but who knows, maybe something interesting will happen."
                        "Of course when it's night time, this becomes \"Sleep.\" You can only sleep in your own room at first, but maybe someone else would let you sleep in her room."
                "Shop":
                        "You can also access the school's fabricator store, where you can order various items to be delivered to your room."
                "Class":
                        "You can always attend classes. These are typically not that interesting, but will raise your XP, and various events might occur in class."
                        "Classes are open during weekday morning and midday periods. You might bump into Rogue there."
                        "You can access the classroom by using \"Leave [[Go to Campus Square].\""
                "Danger Room":
                        "You can also attend a Danger Room training session. These also raise your XP."
                        "The Danger Room is open any time except late at night (students need their sleep)."
                        "You can access the Danger Room by using \"Leave [[Go to Campus Square].\""
                "Shower":
                        "You can also take a shower, but don't worry, you'll do that off camera automatically if you don't get around to it."
                        "You can access the showers by using \"Leave [[Go to Campus Square].\""
                "Study":
                        "You can also choose to study with one of the other students. This will gain you XP, and who knows what else might happen?"
                "Dating":
                        "You can also go out on a date with one of the other students in the evenings. She will probably expect you to pay, so be prepared."
                "Chat":
                        "And of course you can just hang out with one of the other students, or talk to them on the phone if you have their number."
                "Back":
                        jump Tutorial

    "Never mind.":
        return
jump Tutorial

label SpecialMenu: #rkeljsv
    while True:
        menu:
            "Tutorial":
                    jump Tutorial
            "Statchecker" if False:
                    "This element will check all the stats and make sure that they work in your current savegame."
                    "This is a good idea if you're getting 'variable not found' syle errors."
                    menu:
                        "Do you want to do this?"
                        "Yes":
                                $ renpy.pop_call()
                                call Failsafe
                                jump player_room
                        "Never mind.":
                                pass
            "Halloween Party [[Evening Only] (locked)" if Time_Count != 2:
                    pass
            "Halloween Party" if Time_Count == 2:
                    if "halloween" in Player.History:
                            "Did you want to repeat the Halloween party?"
                            "Any girls you met the last time will not see stat changes from conversation,"
                            "but they can still gain stats from flirting and similar activities."
                    else:
                            "Looks like things are getting spooky around Xavier's Institute."
                            "You've recieved an invitation to attend a Halloween party being held in the campus square."
                            "You can do this now, or save it for later. You can always repeat it at a later date."
                    menu:
                        "Go to the party?"
                        "Yes":
                                "You change into your costume and head out to the party."
                                call Halloween_Party_Entry
                        "No":
                                return


            "Do some Microtransactions [[locked] (locked)" if "micro" not in Player.History:
                    call Microtransactions
            "Do some Microtransactions" if "micro" in Player.History:
                    call Microtransactions
            "Visit McCoy's lab to change things about myself.":
                    call Hanks_Lab
            "Reset Custom Outfits":
                    call Emergency_Clothing_Reset
            "Leveling Menu":
                while True:
                    menu:
                        "Level-up menu"
                        "Level Yourself" if Player.StatPoints > 0 or "addict control" in Player.Traits:
                                call Level_Up(Player)
                        "Level Yourself [[No points to spend] (locked)" if Player.StatPoints <= 0 and "addict control" not in Player.Traits:
                                pass
                        "Level [RogueX.Name]" if RogueX.StatPoints > 0:
                                call Level_Up(RogueX)
                        "Level [KittyX.Name]" if KittyX.StatPoints > 0 and "met" in KittyX.History:
                                call Level_Up(KittyX)
                        "Level [EmmaX.Name]" if EmmaX.StatPoints > 0 and "met" in EmmaX.History:
                                call Level_Up(EmmaX)
                        "Level [LauraX.Name]" if LauraX.StatPoints > 0 and "met" in LauraX.History:
                                call Level_Up(LauraX)
                        "Level [JeanX.Name]" if JeanX.StatPoints > 0 and "met" in JeanX.History:
                                call Level_Up(JeanX)
                        "Level [StormX.Name]" if StormX.StatPoints > 0 and "met" in StormX.History:
                                call Level_Up(StormX)
                        "Level [JubesX.Name]" if JubesX.StatPoints > 0 and "met" in JubesX.History:
                                call Level_Up(JubesX)
                        "Back":
                                jump SpecialMenu
                "You need to gain experience first by training or going to class."

            "Return to Room when asked?":
                        "If a girl says she needs to see you, by default you are asked if you'd like to return."
                        menu:
                            "Would you like the game to ask you this?"
                            "Yes [[current]" if RTR_Toggle:
                                    pass
                            "Yes" if not RTR_Toggle:
                                    $ RTR_Toggle = 1
                            "No [[current]" if not RTR_Toggle:
                                    pass
                            "No" if RTR_Toggle:
                                    $ RTR_Toggle = 0
            "Activate Travel Mode" if not TravelMode:
                    "This mode causes you to travel directly to adjacent areas, but not directly to more distant ones."
                    "If you would prefer to use the default, more \"world map\" style of travel, you can toggle this back off."
                    "You can use \"Leave\" to open the location directory."
                    $ TravelMode = 1
            "Deactivate Travel Mode" if TravelMode:
                    $ TravelMode = 0

            "Press the red button" if False:
                "Huh, wonder what that was about. . ."

            "Never mind.":
                return
    return

label Hanks_Lab(Line=0):
        "This is Professor McCoy's lab. You can do various self-modifications here."
        "The changes will be so seemless, it's almost like nobody will even notice!"
        while True:
            $ Line = 0
            menu:
                "What would you like to do?"
                "Alter skin color":
                        menu:
                            "What skin color would you like?"
                            "Green":
                                    $ Player.Color = "green"
                            "White":
                                    $ Player.Color = "pink"
                            "Black":
                                    $ Player.Color = "brown"
                            "Never mind":
                                    $ Line = 1
                        if not Line:
                                "You fiddle with some of McCoy's machinery and a glowing blue liquid pours into a flask."
                                "You down it in a single gulp, and within minutes your skin tone shifts to be more [Player.Color]ish."

                "Change my name.":
                            "You log in to McCoy's high end computer, this should allow you to change your name in all offical databases."
                            $ Player.Name = renpy.input("What name would you like?", default="Zero", length = 10)
                            $ Player.Name = Player.Name.strip()
                            if not Player.Name:
                                    $ Player.Name = "Zero"
                            if Player.Name in ("master", "sir", "lover", "boyfriend", "sex friend", "fuck buddy"):
                                    "Nice try, smartass."
                                    $ Player.Name = "Zero"
                            if "met" in KittyX.History:
                                    $ KittyX.Petnames.append(Player.Name[:1])
                            if "met" in EmmaX.History:
                                    call LastNamer
                                    $ EmmaX.Petnames.append(_return)
                            "That should do it, your name has been updated and an email has been sent out to everyone on campus about the change."
                "Red Button" if False:
                            if not Player.Harem:
                                "No harem"
                            elif len(Player.Harem) == 4:
                                "[Player.Harem[0].Tag],[Player.Harem[1].Tag],[Player.Harem[2].Tag],[Player.Harem[3].Tag]"
                            elif len(Player.Harem) == 3:
                                "[Player.Harem[0].Tag],[Player.Harem[1].Tag],[Player.Harem[2].Tag]"
                            elif len(Player.Harem) == 2:
                                "[Player.Harem[0].Tag],[Player.Harem[1].Tag]"
                            else:
                                "[Player.Harem[0].Tag]"
                "Blue Button":
                            $ Count = len(ActiveGirls)
                            "[Count]"
                            if len(ActiveGirls) == 8:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag],[ActiveGirls[5].Tag],[ActiveGirls[6].Tag],[ActiveGirls[7].Tag]"
                            elif len(ActiveGirls) == 7:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag],[ActiveGirls[5].Tag],[ActiveGirls[6].Tag]"
                            elif len(ActiveGirls) == 6:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag],[ActiveGirls[5].Tag]"
                            elif len(ActiveGirls) == 5:
                                "A-[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                                "B-[ActiveGirls[4].Tag]"
                            elif len(ActiveGirls) == 4:
                                "[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag],[ActiveGirls[3].Tag]"
                            elif len(ActiveGirls) == 3:
                                "[ActiveGirls[0].Tag],[ActiveGirls[1].Tag],[ActiveGirls[2].Tag]"
                            elif len(ActiveGirls) == 2:
                                "[ActiveGirls[0].Tag],[ActiveGirls[1].Tag]"
                            else:
                                "[ActiveGirls[0].Tag]"
                            $ Count = 0
                "Yellow Button":
                            $ Count = len(TotalGirls)
                            "[Count]"
                            if len(TotalGirls) == 8:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag],[TotalGirls[6].Tag],[TotalGirls[7].Tag]"
                            elif len(TotalGirls) == 7:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag],[TotalGirls[6].Tag]"
                            elif len(TotalGirls) == 6:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag],[TotalGirls[5].Tag]"
                            elif len(TotalGirls) == 5:
                                "A-[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                                "B-[TotalGirls[4].Tag]"
                            elif len(TotalGirls) == 4:
                                "[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag],[TotalGirls[3].Tag]"
                            elif len(TotalGirls) == 3:
                                "[TotalGirls[0].Tag],[TotalGirls[1].Tag],[TotalGirls[2].Tag]"
                            elif len(TotalGirls) == 2:
                                "[TotalGirls[0].Tag],[TotalGirls[1].Tag]"
                            else:
                                "[TotalGirls[0].Tag]"
                            $ Count = 0
                "Orange Button":
                            $ Line = "This is Halloween." if "halloween" in RogueX.History else "no"
                            "Rogue: [Line]"
                            $ Line = "This is Halloween." if "halloween" in KittyX.History else "no"
                            "Kitty: [Line]"
                            $ Line = "This is Halloween." if "halloween" in EmmaX.History else "no"
                            "Emma: [Line]"
                            $ Line = "This is Halloween." if "halloween" in LauraX.History else "no"
                            "Laura: [Line]"
                            $ Line = "This is Halloween." if "halloween" in JeanX.History else "no"
                            "Jean: [Line]"
                            $ Line = "This is Halloween." if "halloween" in StormX.History else "no"
                            "Storm: [Line]"
                            $ Line = 0
                "Leave.":
                            return

        return

label Level_Up(Chr=Player):
        if Chr != Player and Chr not in TotalGirls:
            return
        if Chr == Player:
            while Player.StatPoints > 0 or "addict control" in Player.Traits:
                menu:
                    "You have [Player.StatPoints] points to spend. How would you like to spend them?"
                    "Increase sexual stamina. [[Acquired] (locked)" if "focus" in Player.Traits:
                        pass
                    "Increase sexual stamina. [[One point]" if "focus" not in Player.Traits:
                        menu:
                            "This trait will unlock the \"Focus\" option during sex, giving you more time before you blow."
                            "Unlock Focus.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1
                                        $ Player.Traits.append("focus")
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass

                    "Increase your addictiveness. [[One point]" if "addict control" not in Player.Traits and "nonaddictive" not in Player.Traits and "addictive" not in Player.Traits:
                        menu:
                            "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                            "Increase addictiveness.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1
                                        $ Player.Traits.append("addictive")
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass

                    "Reduce your addictiveness. [[One point]" if "addict control" not in Player.Traits and "nonaddictive" not in Player.Traits and "addictive" not in Player.Traits:
                        menu:
                            "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                            "Reduce addictiveness.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1
                                        $ Player.Traits.append("nonaddictive")
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass

                    "Control your Addiction level. [[Two points]" if "addict control" not in Player.Traits and ("nonaddictive" in Player.Traits or "addictive" in Player.Traits):
                        menu:
                            "This trait will allow you to freely control the amount you addict girls to your touch."
                            "Gain addiction control.":
                                if Player.StatPoints >= 2:
                                        $ Player.StatPoints -= 2
                                        $ Player.Traits.append("addict control")
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass

                    "Increase your addictiveness. [[Free]" if "addict control" in Player.Traits: #If you have Addict-control
                        menu:
                            "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                            "Increase addictiveness, no cost.":
                                if "nonaddictive" in Player.Traits:
                                        $ Player.Traits.remove("nonaddictive")
                                        "You are now at the baseline addictiveness level."
                                elif "addictive" not in Player.Traits:
                                        $ Player.Traits.append("addictive")
                                        "You are now at the enhanced addictiveness level."
                                else:
                                        "You are already at the max addictiveness level."
                            "Cancel.":
                                        pass
                    "Reduce your addictiveness. [[Free]" if "addict control" in Player.Traits:
                        menu:
                            "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                            "Reduce addictiveness.":
                                if "addictive" in Player.Traits:
                                        $ Player.Traits.remove("addictive")
                                        "You are now at the baseline addictiveness level."
                                elif "nonaddictive" not in Player.Traits:
                                        $ Player.Traits.append("nonaddictive")
                                        "You are now at the reduced addictiveness level."
                                else:
                                        "You are already at the minimum addictiveness level."

                                if "addictive" in Player.Traits:
                                        $ Player.Traits.remove("addictive")
                                        $ Player.Traits.append("nonaddictive")
                                        $ Player.Traits.append("addict control")
                                else:
                                        $ Player.Traits.append("nonaddictive")
                            "Cancel.":
                                        pass

                    "Increase semen production. [[Maxed] (locked)" if Player.Semen_Max >= 5:
                        pass
                    "Increase semen production. [[One point]" if Player.Semen_Max < 5:
                        menu:
                            "This trait will increase by 1 the number of times you can climax before needing a break."
                            "Increase max semen.":
                                if Player.StatPoints > 0:
                                        $ Player.StatPoints -= 1
                                        $ Player.Semen_Max += 1
                                else:
                                        "You don't have enough points for that."
                                if Player.Semen_Max >= 5:
                                        "You're already at the max level."
                            "Cancel.":
                                        pass

                    "Never Mind, I'll come back later.":
                                        return
        else:
            #Girls leveling system
            while Chr.StatPoints > 0:
                menu:
                    "[Chr.Name] is Level [Chr.Lvl] and has [Chr.StatPoints] points to spend. How would you like to spend them?"
                    "Increase sexual focus. [[Acquired] (locked)" if "focus" in Chr.Traits:
                        pass
                    "Increase sexual focus. [[One point]" if "focus" not in Chr.Traits:
                        menu:
                            "This trait will unlock the \"Focus\" option during sex, giving [Chr.Name] more time before she orgasms."
                            "Unlock Focus.":
                                if Chr.StatPoints:
                                        $ Chr.StatPoints -= 1
                                        $ Chr.Traits.append("focus")
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                pass

                    "Increase [Chr.Name]'s resistance. [[Maxed] (locked)" if Chr.Resistance >= 3:
                        pass
                    "Increase [Chr.Name]'s resistance. [[One point]" if 0 < Chr.Resistance < 3:
                        menu:
                            "This trait will increase [Chr.Name]'s resistance to your touch's addictive properties."
                            "Increase Resistance.":
                                if Chr.StatPoints:
                                        $ Chr.StatPoints -= 1
                                        $ Chr.Resistance += 1
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass


                    "Increase stamina. [[Maxed] (locked)" if Chr.MaxAction >= 10:
                        pass
                    "Increase stamina. [[One point]" if Chr.MaxAction < 10:
                        "This trait will increase by 2 the number of sex actions [Chr.Name] can take before needing a break."
                        menu:
                            "She currently has [Chr.MaxAction] actions."
                            "Increase sex actions.":
                                if Chr.StatPoints:
                                    $ Chr.StatPoints -= 1
                                    $ Chr.MaxAction += 2
                                    if Chr.MaxAction > 10:
                                        $ Chr.MaxAction = 10
                                        "[Chr.Name] has reached her maximum actions."
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass

                    "Allow [Chr.Name] to touch. [[Acquired] (locked)" if Chr == RogueX and "touch" in Chr.Traits:
                        pass
                    "Allow [Chr.Name] to touch. [[One point]" if Chr == RogueX and "touch" not in Chr.Traits and Chr.Lvl >= 5:
                        "This trait will allow [Chr.Name] to touch other people, not just you, without harming them."
                        menu:
                            "She can still borrow their abilities if they have any."
                            "Unlock touch ability.":
                                if Chr.StatPoints:
                                        $ Chr.StatPoints -= 1
                                        $ Chr.Traits.append("touch")
                                else:
                                        "You don't have enough points for that."
                            "Cancel.":
                                        pass
                    "Never Mind, I'll come back later.":
                                        return

        return

label Remove_Girl(Girl = 0, HideGirl = 1, Hold=0,BO=[]):
        # Girl is the girl being removed, this is for putting girls in a safe location if they run.
        # "Hold" is sent by Present_Check/Girls_Arrive, if active, and you are in public, it sets the girl nearby

        if Girl == "All":
                $ Party = []
                $ Nearby = []
                $ Partner = 0
                $ BO = TotalGirls[:]
        else:
                while Girl in Party:
                        $ Party.remove(Girl)
                while Girl in Present:
                        $ Present.remove(Girl)
                while Girl in Nearby:
                        $ Nearby.remove(Girl)
                if Partner == Girl:
                        $ Partner = 0
                $ BO = [Girl]

        while BO:
                $ BO[0].DrainWord("leaving",1,0,0)
                $ BO[0].DrainWord("arriving",1,0,0)

                if BO[0].Loc == bg_current or (bg_current == "bg classroom" and BO[0].Loc == "bg teacher"):
                    if Hold and bg_current in ("bg campus","bg classroom","bg dangerroom","bg pool"):
                            # "Hold" is sent by Present_Check/Girls_Arrive, if active, and you are in public, it sets the girl nearby
                            if BO[0] not in Nearby:
                                    $ Nearby.append(BO[0])
                            $ BO[0].Loc = "nearby"
                    elif bg_current == BO[0].Home:
                            #if you are in the girl's room, send her to the campus
                            if BO[0] == JubesX and JubesX.Addict >= 60:
                                        $ BO[0].Loc = "bg showerroom"
                            $ BO[0].Loc = "bg campus"
                            $ Player.DrainWord("locked",0,0,1)
                    else:
                            #if you are not in the girl's room, send her home
                            $ BO[0].Loc = BO[0].Home
                            $ Player.DrainWord("locked",0,0,1)

                #below portion visually removes girls.
                if HideGirl:
                            call hide_girl(BO[0], sprite = True)
                $ BO.remove(BO[0])
        return

label CleartheRoom(Character = 0, Passive = 0, Silent = 0, Girls=[],BO=[]): #rkeljsv
        #This is intended to clear the room of non-essential characters
        #the named character is the one who stays, everyone else is kicked out.
        #Character is the one asking to clear the room.
        #Passive is when the second person leaves on their own.
        #Silent removes dialog
        # call CleartheRoom(RogueX,1,1)

        #this populates a list of other girls at the current location

        $ BO = TotalGirls[:]
        $ BO.remove(Character) if Character in TotalGirls else BO
        while BO:
                if BO[0].Loc == bg_current or BO[0] in Party:
                        #if she is at current location, or in your Party
                        $ Girls.append(BO[0])
                elif BO[0].Loc == "bg teacher" and bg_current == "bg classroom":
                        #or is not the character asking people to leave, but is in a teacher role in class. . .
                        $ Girls.append(BO[0])

                $ BO.remove(BO[0])

        $ Nearby = [] #empties the nearby list

        if not Silent and not Passive:
                #this section asks a question that a later phase will answer
                if Character.Loc != bg_current:
                        "[Character.Name] enters the room."
                        $ Character.Loc = bg_current
                if not Girls:
                        #if there is no other girl. . .
                        if Character in TotalGirls:
                                call Display_Girl(Character)
                        return
                if Character == RogueX:
                        # if the clearing character is Rogue
                        if len(Girls) > 1:
                            #if there is at least two other girls. . .
                            ch_r "Ladies, could I talk to [Player.Name] alone for a minute?"
                        elif Girls:
                            #if there is at least one other girl. . .
                            ch_r "[Girls[0].Name], could I talk to [Player.Name] alone for a minute?"
                elif Character == KittyX:
                        if len(Girls) > 1:
                            ch_k "Girls, could I talk to [Player.Name] alone for a sec?"
                        elif Girls:
                            ch_k "[Girls[0].Name], could I talk to [Player.Name] alone for a sec?"
                elif Character == EmmaX:
                        if len(Girls) > 1:
                            ch_e "Girls, would you mind if I had a word alone with [Player.Name]?"
                        elif Girls:
                            ch_e "[Girls[0].Name], would you mind if I had a word alone with [Player.Name]?"
                elif Character == LauraX:
                        if len(Girls) > 1:
                            ch_l "Hey, clear out, I need to talk with [Player.Name]."
                        elif Girls:
                            ch_l "[Girls[0].Name], clear out, I need to talk with [Player.Name]."
                elif Character == JeanX:
                        if len(Girls) > 1:
                            ch_j "Let me have the room, ladies."
                        elif Girls:
                            ch_j "You there, clear out."
                elif Character == StormX:
                        if len(Girls) > 1:
                            ch_s "If I could have the room, ladies?"
                        elif Girls:
                            ch_s "If you could give me the room, [Girls[0].Name], I need to speak with [Player.Name]."
                elif Character == JubesX:
                        if len(Girls) > 1:
                            ch_v "Hey, could you gals check out? I've gotta talk to [Player.Name]."
                        elif Girls:
                            ch_v "Hey, could you check out, [Girls[0].Name]? I've gotta talk to [Player.Name]."
        #end portion asking about each girl

        $ renpy.random.shuffle(Girls)
        while Girls:
                if Girls[0] in Party:
                        $ Party.remove(Girls[0])
                $ Girls[0].DrainWord("leaving",1,0,0)
                $ Girls[0].DrainWord("arriving",1,0,0)

                if Silent:
                        pass
                elif not Passive and Character != "All":
                        #if there are other girls. . .
                        if Girls[0] == RogueX:
                                ch_r "No problem, I'll see you later then."
                        elif Girls[0] == KittyX:
                                ch_k "[KittyX.Like]sure, I'll see you later."
                        elif Girls[0] == EmmaX:
                                ch_e "Fine, I'll see you later then."
                        elif Girls[0] == LauraX:
                                ch_l "Ok. I'm leaving."
                        elif Girls[0] == JeanX:
                                ch_j "I'll pretend you were less rude. . ."
                        elif Girls[0] == StormX:
                                ch_s "I will see you all later. . ."
                        elif Girls[0] == JubesX:
                                ch_v "I'm gonna peace out. . ."
                else:
                        if Girls[0] == RogueX:
                                ch_r "I should get going, see you later, [RogueX.Petname]."
                        elif Girls[0] == KittyX:
                                ch_k "I think I'll head out, I'll see you later."
                        elif Girls[0] == EmmaX:
                                ch_e "I think I should be going now."
                        elif Girls[0] == LauraX:
                                ch_l "I'm leaving."
                        elif Girls[0] == JeanX:
                                "[JeanX.Name] wanders off."
                        elif Girls[0] == StormX:
                                ch_s "I should go. . ."
                        elif Girls[0] == JubesX:
                                ch_v "I'm gonna peace out. . ."

                if bg_current == Girls[0].Home:
                        if Character != "All": #if it's not clearing all girls. . .
                                #if the girl is not Rogue but you're in Rogue's room, the girl takes you to her room
                                $ bg_current = Character.Home
                                $ Character.Loc = Character.Home
                                call Set_The_Scene
                                call CleartheRoom(Character)
                                call Taboo_Level
                                if not Silent:
                                    "[Character.Name] brings you back to her room. . ."
                                jump Misplaced
                                return
                        else:
                                $ Girls[0].Loc = "bg campus"
                else:
                                $ Girls[0].Loc = Girls[0].Home

                if Girls[0] == RogueX:
                        hide Rogue_Sprite with easeoutright
                elif Girls[0] == KittyX:
                        hide Kitty_Sprite with easeoutbottom
                elif Girls[0] == EmmaX:
                        hide Emma_Sprite with easeoutright
                elif Girls[0] == LauraX:
                        hide Laura_Sprite with easeoutright
                elif Girls[0] == JeanX:
                        hide Jean_Sprite with easeoutright
                elif Girls[0] == StormX:
                        hide Storm_Sprite with easeoutright
                elif Girls[0] == JubesX:
                        hide Jubes_Sprite with easeoutright
                $ Girls.remove(Girls[0])
        if Character in TotalGirls:
                call Display_Girl(Character)
        call Taboo_Level
        return

label Girls_Location(GirlsNum = 0, Change=0, BOptions=[]):
        #this figures out where girls are and where to put spares.
        #it's called most often by Locations, after Waits
        #Girlsnum sets the number of girls that have already talked
        #"arriving" is set by the "Schedule" code, and will not be applied unless
        # the girl in questions was someplace else, and just showed up here on their own.

        $ BOptions = TotalGirls[:]
        $ renpy.random.shuffle(BOptions)
        while BOptions:
                #cycles through each girl possible, adds them to the local area if possible
                if "leaving" in BOptions[0].RecentActions:
                        if "sleepover" in BOptions[0].Traits:
                                $ BOptions[0].DrainWord("sleepover",0,0,1)  #remove from Traits
                        call leave(BOptions[0])
                        if BOptions[0].Loc != bg_current:
                                if BOptions[0] in Present:
                                        $ Present.remove(BOptions[0])
                                $ Change = 1
                        $ GirlsNum += 1
                #if Girl was in Nearby, but was moved to a new location
                if BOptions[0] in Nearby and BOptions[0].Loc != "nearby": #and BOptions[0].Loc != bg_current
                                $ Nearby.remove(BOptions[0])
                $ BOptions.remove(BOptions[0])

        if Change:
            #if there are any fewer girls than there were, Set the Scene
            call Set_The_Scene(Dress=0)

        $ BOptions = TotalGirls[:]
        while BOptions:
                        if "arriving" in BOptions[0].RecentActions:
                                call Girls_Arrive
                                return
                        $ BOptions.remove(BOptions[0])
        return

label Girls_Arrive(Primary = 0, Secondary = 0, GirlsNum = 0,BO=[]): #rkeljsv
        # Called by Girls_Location after a Wait period
        #"arriving" is set by the "Schedule" code, and will not be applied unless
        # the girl in questions was someplace else, and just showed up here on their own.
        # Present contains all girls already local

        $ Options = []

        call Present_Check
        $ BO = Present[:]
        while BO:
                #Each girl trying to arrive is added to the Options
                if "arriving" in BO[0].RecentActions and BO[0] not in Party:
                        $ GirlsNum += 1
                        $ Options.append(BO[0])
                $ BO[0].DrainWord("arriving")
                $ BO.remove(BO[0])

        if not Options:
                #If there are no incoming girl options, then no point to the rest
                return

        $ renpy.random.shuffle(Options)
        $ Primary = Options[0]
        if len(Options) >= 2:
                #if 2+ people are arriving
                if bg_current == Options[1].Home:       #if you're in Options[0]'s room,
                        $ Primary = Options[1]
                        $ Secondary = Options[0]
                else:
                        $ Secondary = Options[1]

        if Secondary not in TotalGirls:
                $ Secondary = 0
        $ Options = []

        if "locked" in Player.Traits:
                if Primary == KittyX:
                        call Locked_Door(KittyX)
                        if KittyX.Loc != bg_current:
                            $ Primary = 0
                        elif Secondary:
                            #since Kitty can just barg right in, if she does so,
                            "You hear a \"thump\" as if someone was trying to follow Kitty."
                            call Locked_Door(Secondary)
                            if Secondary.Loc != bg_current:
                                    $ Secondary = 0
                elif Primary.Home == bg_current:
                        #if it's the girl's room. . .
                        "You hear a key jiggling in the lock."
                else:
                        call Locked_Door(Primary)
                        if Primary.Loc != bg_current:
                            $ Primary = 0
        #End "if the door was locked."

        if not Primary:
                return

        #This sequence sets the pecking order, more important once there are more girls
        #girls left out of this are put into "Nearby" for the current space

        call Shift_Focus(Primary)
        if bg_current == "bg dangerroom":
                    #call Gym_Clothes("auto")
                    #puts incoming girls into gym clothes
                    $ Primary.Outfit = "gym"
                    $ Primary.OutfitChange()
                    if Secondary:
                            $ Secondary.Outfit = "gym"
                            $ Secondary.OutfitChange()

        call Set_The_Scene #causes the girls to display
        if bg_current == "bg player":
                    if Secondary:
                            #if there's a second girl
                            "[Primary.Name] and [Secondary.Name] just entered your room."
                    else:
                            #if there's no second girl,
                            "[Primary.Name] just entered your room."

                    if Primary == RogueX:
                                if Secondary:
                                    ch_r "Hey, [RogueX.Petname], can we come in?"
                                else:
                                    ch_r "Hey, [RogueX.Petname], can I come in?"
                    elif Primary == KittyX:
                                if Secondary:
                                    ch_k "Hey[KittyX.like]can we come in?"
                                else:
                                    ch_k "Hey[KittyX.like]can I come in?"
                    elif Primary == EmmaX:
                                if Secondary:
                                    ch_e "Ah, good, you're here. May we come in?"
                                else:
                                    ch_e "Ah, good, you're here. May I come in?"
                    elif Primary == LauraX:
                                    ch_l "Hey."
                                    ch_p ". . . [[She seems to want to stay]."
                    elif Primary == JeanX:
                                    ch_j "Hey, [JeanX.Petname]."
                                    ch_p ". . . [[Ok, she's here now]."
                    elif Primary == StormX:
                                if Secondary:
                                    ch_s "Excellent, you're in. May we come in?"
                                else:
                                    ch_s "Excellent, you're in. May I come in?"
                    elif Primary == JubesX:
                                if Secondary:
                                    ch_v "Oh, hey, mind us coming in?"
                                else:
                                    ch_v "Oh, hey, mind me coming in?"
                    menu:
                        extend ""
                        "Sure.":
                            $ Line = "sure"
                        "Not right now, maybe later.":
                            $ Line = "later"
                        "Nope.":
                            $ Line = "no"

                    if Line == "sure":
                            $ Primary.Statup("Love", 80, 1)
                            $ Primary.Statup("Obed", 50, 2)
                            $ Primary.Statup("Inbt", 50, 2)
                            if Primary == RogueX:
                                    ch_r "Thanks."
                            elif Primary == KittyX:
                                    $ KittyX.Statup("Inbt", 50, 1)
                                    ch_k "Cool."
                            elif Primary == EmmaX:
                                    ch_e "Good."
                            elif Primary == LauraX:
                                    $ LauraX.Statup("Love", 50, 1)
                                    $ LauraX.Statup("Obed", 60, 1)
                                    "She doesn't leave."
                            elif Primary == JeanX:
                                    "She doesn't leave."
                            elif Primary == StormX:
                                    ch_s "Good."
                            elif Primary == JubesX:
                                    ch_v "Nice."
                            if Secondary:
                                    $ Secondary.Statup("Love", 80, 1)
                                    $ Secondary.Statup("Obed", 50, 2)
                                    $ Secondary.Statup("Inbt", 50, 2)
                            #end "sure"
                    if Line == "later":
                            $ Primary.Statup("Love", 60, -1, 1)
                            $ Primary.Statup("Obed", 70, 5)
                            $ Primary.FaceChange("confused")
                            if Secondary and Secondary != JeanX:
                                    $ Secondary.Statup("Love", 60, -1, 1)
                                    $ Secondary.Statup("Obed", 70, 5)
                                    $ Secondary.FaceChange("confused")
                                    if Primary == RogueX:
                                            ch_r "Um, ok, we'll go then."
                                    elif Primary == KittyX:
                                            $ KittyX.Statup("Love", 60, -1, 1)
                                            $ KittyX.Statup("Obed", 70, 2)
                                            ch_k "Oh[KittyX.like]we'll get going then."
                                    elif Primary == EmmaX:
                                            $ EmmaX.Statup("Love", 90, -2)
                                            $ EmmaX.Statup("Obed", 30, -7)
                                            ch_e "If that's how you wish to play it. . ."
                                    elif Primary == LauraX:
                                            $ LauraX.Statup("Love", 90, -2)
                                            $ LauraX.Statup("Obed", 30, -7)
                                            ch_l "Ok, later."
                                    elif Primary == StormX:
                                            ch_s "Ah, then we'll leave you to it."
                                    elif Primary == JubesX:
                                            ch_v "Oh. Ok. . ."
                                    call Remove_Girl(Secondary)
                            elif Primary == RogueX:
                                    ch_r "Um, ok."
                            elif Primary == KittyX:
                                    $ KittyX.Statup("Love", 60, -1, 1)
                                    $ KittyX.Statup("Obed", 70, 2)
                                    ch_k "Oh[KittyX.like]I'll get going then."
                            elif Primary == EmmaX:
                                    $ EmmaX.Statup("Love", 90, -2)
                                    $ EmmaX.Statup("Obed", 30, -7)
                                    ch_e "If that's how you wish to play it. . ."
                            elif Primary == LauraX:
                                    $ LauraX.Statup("Love", 90, -2)
                                    $ LauraX.Statup("Obed", 30, -7)
                                    ch_l "Ok, later."
                            elif Primary == StormX:
                                    ch_s "Ah, then I'll leave you to it."
                            elif Primary == JubesX:
                                    ch_v "Oh. Ok. . ."
                            if Primary == JeanX or Secondary == JeanX:
                                    ch_j "Uh-huh."
                                    "She doesn't leave."
                            if Primary != JeanX:
                                    call Remove_Girl(Primary)
                            #end "later"
                    if Line == "no":
                            $ Primary.Statup("Obed", 50, 5)
                            if ApprovalCheck(Primary, 1800) or ApprovalCheck(Primary, 500, "O"):
                                # She accepts it
                                $ Primary.Statup("Obed", 80, 2)
                                if Primary == RogueX:
                                        ch_r "I guess that's ok. See you later then."
                                elif Primary == KittyX:
                                        ch_k "If you want some alone time. . ."
                                elif Primary == EmmaX:
                                        $ EmmaX.Statup("Obed", 50, 2)
                                        ch_e "I suppose you can have your personal space. . ."
                                elif Primary == LauraX:
                                        ch_l "Not a problem."
                                elif Primary == StormX:
                                        ch_s ". . . very well. . ."
                                elif Primary == JubesX:
                                        ch_v "Oh. Ok. . ."
                            else:
                                $ Primary.FaceChange("angry")
                                $ Primary.Statup("Love", 60, -5, 1)
                                $ Primary.Statup("Love", 80, -2)
                                $ Primary.Statup("Obed", 80, 3)
                                $ Primary.Statup("Inbt", 50, 1)
                                if Primary == RogueX:
                                        ch_r "Well fine!"
                                elif Primary == KittyX:
                                        $ KittyX.Statup("Love", 80, -2)
                                        $ KittyX.Statup("Obed", 80, 2)
                                        ch_k "Jerk!"
                                elif Primary == EmmaX:
                                        $ EmmaX.Statup("Love", 90, -2)
                                        $ EmmaX.Statup("Obed", 80, 3)
                                        ch_e "We'll see how long that attitude lasts. . ."
                                elif Primary == LauraX:
                                        $ LauraX.Statup("Love", 90, -2)
                                        "She seems upset."
                                elif Primary == StormX:
                                        ch_s ". . . I see. . ."
                                elif Primary == JubesX:
                                        ch_v "Oh, so you're going to be like -that-. . ."
                            if Primary == JeanX or Secondary == JeanX:
                                    ch_j "Uh-huh."
                                    "She doesn't leave."
                            if Primary != JeanX:
                                    call Remove_Girl(Primary)
                            if Secondary and Secondary != JeanX:
                                    $ Secondary.Statup("Obed", 50, 5)
                                    if ApprovalCheck(Secondary, 1800) or ApprovalCheck(Secondary, 500, "O"):
                                        $ Secondary.Statup("Obed", 80, 2)
                                        if Secondary == RogueX:
                                                ch_r "I guess that's ok. See you later then."
                                        elif Secondary == KittyX:
                                                ch_k "If you want some alone time. . ."
                                        elif Secondary == EmmaX:
                                                $ EmmaX.Statup("Obed", 50, 2)
                                                ch_e "I suppose you can have your personal space. . ."
                                        elif Secondary == LauraX:
                                                ch_l "Not a problem."
                                        elif Primary == StormX:
                                                ch_s ". . . very well. . ."
                                        elif Primary == JubesX:
                                                ch_v "Oh. Ok. . ."
                                    else:
                                        $ Secondary.FaceChange("angry")
                                        $ Secondary.Statup("Love", 60, -5, 1)
                                        $ Secondary.Statup("Love", 80, -2)
                                        $ Secondary.Statup("Obed", 80, 3)
                                        $ Secondary.Statup("Inbt", 50, 1)
                                        if Secondary == RogueX:
                                                ch_r "Well fine!"
                                        elif Secondary == KittyX:
                                                $ KittyX.Statup("Love", 80, -2)
                                                $ KittyX.Statup("Obed", 80, 2)
                                                ch_k "Jerk!"
                                        elif Secondary == EmmaX:
                                                $ EmmaX.Statup("Love", 90, -2)
                                                $ EmmaX.Statup("Obed", 80, 3)
                                                ch_e "We'll see how long that attitude lasts. . ."
                                        elif Secondary == LauraX:
                                                $ LauraX.Statup("Love", 90, -2)
                                                "She seems upset."
                                        elif Primary == StormX:
                                                ch_s ". . . I see. . ."
                                        elif Primary == JubesX:
                                                ch_v "Oh, so you're going to be like -that-. . ."
                                    call Remove_Girl(Secondary)
                                    if Primary == JeanX:
                                            "[Secondary.Name] storms out."
                                    else:
                                            "The girls storm out."
                                            if Primary == StormX or Secondary == StormX:
                                                    "-so to speak."
                        #end "nope"
                    #end girls showed up to player's room.

        elif bg_current in PersonalRooms:
                    #if you show up at one of the girls' rooms
                    if Secondary:
                            #if there's a second girl
                            "[Primary.Name] and [Secondary.Name] just entered the room."
                    else:
                            #if there's no second girl,
                            "[Primary.Name] just entered the room."
                    if bg_current == Primary.Home:
                                    if "angry" in Primary.DailyActions:
                                            #She's angry
                                            $ Primary.FaceChange("bemused", 1,Brows="angry")
                                            if Primary == RogueX:
                                                            ch_r "I'm kinda pissed at you right now, get out of here."
                                            elif Primary == KittyX:
                                                            ch_k "You shouldn't be here right now."
                                            elif Primary == EmmaX:
                                                            ch_e "I don't think you should be here."
                                            elif Primary == LauraX:
                                                            ch_l "You should get away while you can."
                                            elif Primary == JeanX:
                                                            ch_j "I'm not in the mood."
                                            elif Primary == StormX:
                                                            ch_s "This would not be a safe place for you to be. . ."
                                            elif Primary == JubesX:
                                                            ch_v "\"Tread not into my lair\". . ."

                                    elif Time_Count >= 3 and ApprovalCheck(Primary, 1000, "LI") and ApprovalCheck(Primary, 600, "OI"):
                                            #it's night and she likes you
                                            if Primary == RogueX:
                                                            ch_r "Oh, hey, [RogueX.Petname], it's pretty late, but I guess you can stick around for a bit."
                                            elif Primary == KittyX:
                                                            ch_k "Oh, hey, it's kinds late, but you can stay for a bit."
                                            elif Primary == EmmaX:
                                                            ch_e "Oh, it's a bit late, but you're welcome."
                                            elif Primary == LauraX:
                                                            ch_l "It's late."
                                            elif Primary == JeanX:
                                                            ch_j "Oh, you know what time it is, right?"
                                            elif Primary == StormX:
                                                            ch_s "Delightful to see you, but the hour is late. . ."
                                            elif Primary == JubesX:
                                                            ch_v "Kinda late, [JubesX.Petname], s'up?"
                                            $ Line = "stay"
                                    elif ApprovalCheck(Primary, 1300) or ApprovalCheck(Primary, 500, "O") or Primary == JubesX:
                                            #it's not night and she likes you
                                            if Primary == RogueX:
                                                            ch_r "Oh, hey, [RogueX.Petname], nice to see you here."
                                            elif Primary == KittyX:
                                                            ch_k "Oh, hey, nice to see you."
                                            elif Primary == EmmaX:
                                                            ch_e "Oh, nice to see you."
                                            elif Primary == LauraX:
                                                            ch_l "Oh, hey."
                                            elif Primary == JeanX:
                                                            ch_j "Oh, hello?"
                                            elif Primary == StormX:
                                                            ch_s "It is good to see you."
                                            elif Primary == JubesX:
                                                            ch_v "Hey, [JubesX.Petname], s'up?"
                                            $ Line = "stay"
                                    elif Time_Count >= 3:
                                            #it's night and she wants you gone
                                            if Primary == RogueX:
                                                            ch_r "Oh, hey, [RogueX.Petname], it's kind late, could you head out of here?"
                                            elif Primary == KittyX:
                                                            ch_k "Oh, hey, [KittyX.Petname]. It's kind of late, could you come back tomorrow?"
                                            elif Primary == EmmaX:
                                                            ch_e "Oh, hello, [EmmaX.Petname]. It's a bit late, could you come back tomorrow?"
                                            elif Primary == LauraX:
                                                            ch_l "Oh, hey, it's late."
                                            elif Primary == JeanX:
                                                            ch_j "You -can- tell time, right?"
                                            elif Primary == StormX:
                                                            ch_s "I'm afraid that the hour is a bit late for visits. . ."
                                            #elif Primary == JubesX:
                                                            #not a factor since she does not sleep
                                    elif ApprovalCheck(Primary, 600, "LI") or ApprovalCheck(Primary, 300, "OI"):
                                            #it's not night and she's neutral
                                            if Primary == RogueX:
                                                            ch_r "Oh, hey, [RogueX.Petname]. You can stick around, I guess."
                                            elif Primary == KittyX:
                                                            ch_k "Oh, hey, [KittyX.Petname], what's up?"
                                            elif Primary == EmmaX:
                                                            ch_e "Oh, hello, [EmmaX.Petname], can I help you with anything?"
                                            elif Primary == LauraX:
                                                            ch_l "Oh, hey, [LauraX.Petname]."
                                            elif Primary == JeanX:
                                                            ch_j "Um, hello?"
                                            elif Primary == StormX:
                                                            ch_s "Oh, yes? Did you need something?"
                                            elif Primary == JubesX:
                                                            ch_v "Hey, [JubesX.Petname], s'up?"
                                            $ Line = "stay"
                                    else:
                                            #she wants you gone
                                            if Primary == RogueX:
                                                            ch_r "Hey, [RogueX.Petname], I'm not sure why you're here, but I'd rather you leave."
                                            elif Primary == KittyX:
                                                            ch_k "Hey, [KittyX.Petname], what are you even doing here?"
                                                            ch_k "Could you[KittyX.like]get out?"
                                            elif Primary == EmmaX:
                                                            ch_e "Oh, hello, [EmmaX.Petname]?"
                                                            ch_e "Did you have a reason to be visiting me?"
                                            elif Primary == LauraX:
                                                            $ Primary.FaceChange("confused")
                                                            ch_l "Hey, [LauraX.Petname], why are you here?"
                                            elif Primary == JeanX:
                                                            $ Primary.FaceChange("confused")
                                                            ch_j "I didn't invite you here."
                                            elif Primary == StormX:
                                                            ch_s "I'm afraid that this is not a good time."
                                            elif Primary == JubesX:
                                                            ch_v "Hey, [JubesX.Petname]? Not a good time."
                                    if Line != "stay":
                                        #if she asked you to leave. . .
                                        menu:
                                            extend ""
                                            "Sure, ok. [[you go]":
                                                        $ Primary.Statup("Love", 80, 1)
                                                        $ Primary.Statup("Obed", 50, 2)
                                                        $ Primary.Statup("Inbt", 50, 2)
                                                        call AnyLine(Primary,"Thanks.")
                                                        "You head back to your room."
                                            "Sorry, I'll go.":
                                                        $ Primary.Statup("Love", 90, 2)
                                                        $ Primary.Statup("Obed", 50, 3)
                                                        $ Primary.FaceChange("smile")
                                                        call AnyLine(Primary,"Thanks.")
                                                        "You head back to your room."
                                            "Are you sure I can't stay?":
                                                        if "angry" in Primary.DailyActions:
                                                                $ Primary.FaceChange("angry")
                                                                if Primary == RogueX:
                                                                                ch_r "What part of \"no\" don't ya get?"
                                                                elif Primary == KittyX:
                                                                                ch_k "I think I said {i}NO!{/i}"
                                                                elif Primary == EmmaX:
                                                                                ch_e "I believe I said {i}no.{/i}"
                                                                elif Primary == LauraX:
                                                                                ch_l "[[growls] . . .You probably shouldn't."
                                                                elif Primary == JeanX:
                                                                                ch_j "Oh, bad call, [Primary.Petname]"
                                                                elif Primary == StormX:
                                                                                ch_s "Quite certain."
                                                                elif Primary == JubesX:
                                                                                ch_v "Oh, let me check. . ."
                                                                                $ Primary.FaceChange("angry",Eyes="side")
                                                                                ch_v ". . ."
                                                                                $ Primary.FaceChange("angry",Mouth="open")
                                                                                ch_v "-YES.-"
                                                                                $ Primary.FaceChange("angry")
                                                        elif Time_Count >= 3 and ApprovalCheck(Primary, 800, "LI") and ApprovalCheck(Primary, 400, "OI"):
                                                                $ Primary.FaceChange("sadside")
                                                                if Primary == RogueX:
                                                                                ch_r "I suppose I can make an exception this once."
                                                                elif Primary == KittyX:
                                                                                ch_k "Maybe just this once. . ."
                                                                elif Primary == EmmaX:
                                                                                ch_e "Perhaps just this once. . ."
                                                                elif Primary == LauraX:
                                                                                ch_l "I guess. . ."
                                                                elif Primary == JeanX:
                                                                                ch_j "Oh, whatever, make it quick."
                                                                elif Primary == StormX:
                                                                                ch_s "If it is really so important. . ."
                                                                elif Primary == JubesX:
                                                                                ch_v "Sure."
                                                                $ Line = "stay"
                                                        elif Time_Count >= 3:
                                                                if Primary == RogueX:
                                                                                ch_r "No way, [RogueX.Petname]. Try again tomorrow."
                                                                elif Primary == KittyX:
                                                                                ch_k "Noooope. Try again tomorrow."
                                                                elif Primary == EmmaX:
                                                                                ch_e "I'm afraid not. Try again tomorrow."
                                                                elif Primary == LauraX:
                                                                                ch_l "No. Maybe tomorrow."
                                                                elif Primary == JeanX:
                                                                                ch_j "Um, no? Get out."
                                                                elif Primary == StormX:
                                                                                ch_s "Not tonight, perhaps during class."
                                                                elif Primary == JubesX:
                                                                                ch_v "Sure."
                                                                                $ Line = "stay"
                                                        elif ApprovalCheck(Primary, 750):
                                                                if Primary == RogueX:
                                                                                ch_r "Oh, fine. For a little bit."
                                                                elif Primary == KittyX:
                                                                                ch_k "Oh, fiiiine."
                                                                                ch_k "Just for a little bit."
                                                                elif Primary == EmmaX:
                                                                                ch_e "Oh, very well. . ."
                                                                                ch_e "Just for a little bit."
                                                                elif Primary == LauraX:
                                                                                ch_l "Ok."
                                                                                ch_l "Just for a minute."
                                                                elif Primary == JeanX:
                                                                                ch_j "I guess? Whatever."
                                                                elif Primary == StormX:
                                                                                ch_s "If it is really so important. . ."
                                                                elif Primary == JubesX:
                                                                                ch_v "Sure."
                                                                $ Line = "stay"
                                                        else:
                                                                $ Primary.FaceChange("angry")
                                                                if Primary == RogueX:
                                                                                ch_r "No, seriously, get."
                                                                elif Primary == KittyX:
                                                                                ch_k "Noooope."
                                                                elif Primary == EmmaX:
                                                                                ch_e "Definitely not."
                                                                elif Primary == LauraX:
                                                                                ch_l "No."
                                                                elif Primary == JeanX:
                                                                                ch_j "Um, no?"
                                                                elif Primary == StormX:
                                                                                ch_s "Definitely not."
                                                                elif Primary == JubesX:
                                                                                ch_v "Nope."
                                                        if Line != "stay":
                                                                $ Primary.Statup("Love", 80, -1)
                                                                $ Primary.Statup("Inbt", 50, 3)
                                                                "[Primary.Name] kicks you out of the room."

                                            "I'm sticking around, thanks.":
                                                        if "angry" in Primary.DailyActions or (not ApprovalCheck(Primary, 1800) and not ApprovalCheck(Primary, 500, "O")):
                                                                $ Primary.FaceChange("angry")
                                                                if Primary == RogueX:
                                                                                ch_r "No way, buster! Out!"
                                                                elif Primary == KittyX:
                                                                                ch_k "Nooope, out!"
                                                                elif Primary == EmmaX:
                                                                                ch_e "You must be joking."
                                                                elif Primary == LauraX:
                                                                                ch_l "You really shouldn't."
                                                                elif Primary == JeanX:
                                                                                ch_j "Um, no you aren't."
                                                                elif Primary == StormX:
                                                                                ch_s "You most certainly are not."
                                                                elif Primary == JubesX:
                                                                                ch_v "Well, it's easier than calling -out- for dinner. . ."
                                                        else:
                                                                $ Primary.Statup("Obed", 80, 5)
                                                                $ Primary.FaceChange("sad")
                                                                if Primary == RogueX:
                                                                                ch_r ". . ."
                                                                                ch_r "I guess that's ok."
                                                                elif Primary == KittyX:
                                                                                ch_k ". . ."
                                                                                ch_k "Fine."
                                                                elif Primary == EmmaX:
                                                                                ch_e ". . ."
                                                                                ch_e "Fine."
                                                                elif Primary == LauraX:
                                                                                ch_l ". . ."
                                                                elif Primary == JeanX:
                                                                                ch_j "Fine, whatever."
                                                                elif Primary == StormX:
                                                                                ch_s "We will have to discuss boundaries later."
                                                                elif Primary == JubesX:
                                                                                ch_v "Uh-huh. . ."
                                                                $ Line = "stay"
                                                        if Line != "stay":
                                                                $ Primary.Statup("Love", 60, -5, 1)
                                                                $ Primary.Statup("Love", 80, -5)
                                                                $ Primary.Statup("Obed", 50, 2)
                                                                $ Primary.Statup("Inbt", 60, 5)
                                                                "[Primary.Name] kicks you out of the room."

                                    if Line != "stay":
                                            $ bg_current = "bg player"
                                            jump Misplaced
                                    #End the girl tells you to leave.
                    elif Primary == RogueX:
                                    ch_r "Sorry, I wasn't expecting to bump into you here."
                    elif Primary == KittyX:
                                    ch_k "Hey[KittyX.like]funny meeting you here."
                    elif Primary == EmmaX:
                                    ch_e "I didn't expect to run into you here."
                    elif Primary == LauraX:
                                    ch_l "Oh, hey."
                    elif Primary == JeanX:
                                    ch_j "Oh, you. . ."
                    elif Primary == StormX:
                                    ch_s "Ah, [StormX.Petname]."
                    elif Primary == JubesX:
                                    ch_v "Oh, hey. . ."
        #end girls showed up to Primary's room.

        elif bg_current == "bg classroom":
                #if this is triggered, Adjacent should never be higher than 1.
                #adjacent characters who are neither Primary nor secondary should have been removed from adjacency

                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] and [Secondary.Name] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary.Name] just entered the room."

                if Primary == RogueX or Secondary == RogueX:
                                ch_r "Hey, [RogueX.Petname]."
                if Primary == KittyX or Secondary == KittyX:
                                ch_k "Oh, hey."
                if Primary == EmmaX or Secondary == EmmaX:
                                ch_e "Oh, hello, [EmmaX.Petname]."
                if Primary == LauraX or Secondary == LauraX:
                                ch_l "Hey."
                if Primary == StormX or Secondary == StormX:
                                ch_s "Hello, [StormX.Petname]."
                if Primary == JubesX or Secondary == JubesX:
                                ch_v "Hey!"

                $ Line = 0
                $ D20 = renpy.random.randint(1, 20)

                if Primary == EmmaX or Primary == StormX:
                        #if the Primary is one of the teachers, swap the Secondary in
                        if Secondary:
                                $ Primary = Secondary
                                $ Secondary = 0
                        else:
                                $ Primary = 0
                if Primary:
                        #Determines who sits next to you
                        if ApprovalCheck(Primary, 1000):
                                if len(Present) < 2 and D20 >= 10:
                                        $ Line = Primary.Name + " takes the seat next to you"
                                        $ Present.append(Primary)
                                else:
                                        $ Line = Primary.Name + " sits across the room from you"
                                        $ Nearby.append(Primary)
                        else:
                                        $ Line = Primary.Name + " sits across the room from you"
                                        $ Nearby.append(Primary)

                if Secondary:
                        if ApprovalCheck(Secondary, 1000):
                            if len(Present) < 2 and D20 >= 10:
                                        #changes dialog based on whether she does the same or differently than the last person
                                        if Primary in Present:
                                                $ Line = Primary.Name + " and " + Secondary.Name + " sit down next to you"
                                        else:
                                                $ Line = Line + ", while " + Secondary.Name + " takes the seat next to you"
                                        $ Present.append(Secondary)
                            else:
                                        if Primary in Nearby:
                                                $ Line = Primary.Name + " and " + Secondary.Name + " sit across the room from you"
                                        else:
                                                $ Line = Line + ", while " + Secondary.Name + " sits across the room from you"
                                        $ Nearby.append(Secondary)
                        else:
                                        if Primary in Nearby:
                                                $ Line = Primary.Name + " and " + Secondary.Name + " sit across the room from you"
                                        else:
                                                $ Line = Line + ", while " + Secondary.Name + " sits across the room from you"
                                        $ Nearby.append(Secondary)
                if Line:
                    "[Line]."

                if EmmaX.Loc == "bg teacher":
                        "[EmmaX.Name] takes her position behind the podium."
                elif StormX.Loc == "bg teacher":
                        "[StormX.Name] takes her position behind the podium."
                #end girls showed up to class
        elif bg_current == "bg dangerroom":
                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] and [Secondary.Name] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary.Name] just entered the room."
                #end girls showed up to the Danger Room
        elif bg_current == "bg campus":
                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] and [Secondary.Name] just entered the square."
                else:
                        #if there's no second girl,
                        "[Primary.Name] just entered the square."
                #end girls showed up to the campus
        elif bg_current == "bg pool":
                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] and [Secondary.Name] just entered the pool area."
                else:
                        #if there's no second girl,
                        "[Primary.Name] just entered the pool area."
                #end girls showed up to the campus
        else: #if it's anywhere else,
                if Secondary:
                        #if there's a second girl
                        "[Primary.Name] and [Secondary.Name] just entered the room."
                else:
                        #if there's no second girl,
                        "[Primary.Name] just entered the room."
                #end girls showed up someplace

        if bg_current in ("bg campus","bg dangerroom","bg pool"):
                if Primary == RogueX or Secondary == RogueX:
                            ch_r "Hey, [RogueX.Petname]."
                if Primary == KittyX or Secondary == KittyX:
                            ch_k "Oh, hey."
                if Primary == EmmaX or Secondary == EmmaX:
                            ch_e "Oh, hello, [EmmaX.Petname]."
                if Primary == LauraX or Secondary == LauraX:
                            ch_l "Hey."
                if Primary == StormX or Secondary == StormX:
                            ch_s "Hello, [StormX.Petname]."
                if Primary == JubesX or Secondary == JubesX:
                            ch_v "Hey!"
        #end "girls showed up"

        $ BO = TotalGirls[:]
        while BO:
                if BO[0] in Nearby:
                        $ BO[0].Loc = "nearby"
                elif BO[0].Loc == bg_current:
                        $ Present.append(BO[0])
                $ BO.remove(BO[0])
        if Nearby:
                "There were some others as well, but they kept their distance."
        return

label ReturnToSender:
        #Set's girl's location back to where she's meant to be if she was "nearby"
        #Set's girl's location back to where she's meant to be if she stuck around in an area you've since left
        $ BO = ActiveGirls[:]
        while BO:
            #if BO[0].Loc != bg_current and BO[0].Loc == "nearby":
            #if BO[0].Loc != bg_current and BO[0] not in Party:

            if BO[0] not in Party and BO[0].Schedule[Weekday][Time_Count] != bg_current:
                    # so long as she is not scehduled to be in the current location,
                    $ BO[0].Loc = BO[0].Schedule[Weekday][Time_Count]
                    if BO[0] == JubesX and JubesX.Addict > 60:
                                    #Jubliee will not leave her room voluntarily if it's higher than 60
                                    $ JubesX.Loc = JubesX.Home
            $ BO.remove(BO[0])
        return

label Swap_Nearby(Girl=0): #rkeljsv
        #allows you to bring nearby girls in.
        # girl is the girl in question, here is a counter for locals
        if Girl not in Nearby:
            return
        if bg_current not in ("bg campus","bg classroom","bg dangerroom"):
            #if you aren't in a space that supports this. . .
            "There's no room for that here."
            return

        if len(Present) >= 2:
            #if two or more girls are adjacent so there is no room. . .
            call AnyLine(Girl,"It's a little crowded over there.")
            menu:
                "Move away from an adjacent girl?"
                "[RogueX.Name]" if RogueX.Loc == bg_current:
                        "You shift away from [RogueX.Name]"
                        call Remove_Girl(RogueX,1,1)    #Hide+moveto nearby
                "[KittyX.Name]" if KittyX.Loc == bg_current:
                        "You shift away from [KittyX.Name]"
                        call Remove_Girl(KittyX,1,1)    #Hide+moveto nearby
                "[EmmaX.Name]" if EmmaX.Loc == bg_current:
                        "You shift away from [EmmaX.Name]"
                        call Remove_Girl(EmmaX,1,1)     #Hide+moveto nearby
                "[LauraX.Name]" if LauraX.Loc == bg_current:
                        "You shift away from [LauraX.Name]"
                        call Remove_Girl(LauraX,1,1)    #Hide+moveto nearby
                "[JeanX.Name]" if JeanX.Loc == bg_current:
                        "You shift away from [JeanX.Name]"
                        call Remove_Girl(JeanX,1,1)    #Hide+moveto nearby
                "[StormX.Name]" if StormX.Loc == bg_current:
                        "You shift away from [StormX.Name]"
                        call Remove_Girl(StormX,1,1)    #Hide+moveto nearby
                "[JubesX.Name]" if JubesX.Loc == bg_current:
                        "You shift away from [JubesX.Name]"
                        call Remove_Girl(JubesX,1,1)    #Hide+moveto nearby
                "No, never mind.":
                    return
        "[Girl.Name] comes over and joins you."
        $ Nearby.remove(Girl)
        $ Present.append(Girl)
        call Shift_Focus(Girl)
        $ Girl.Loc = bg_current
        call Set_The_Scene(1,0,0,0)
        return

label Dismissed:  #rkeljsv
        # this is called to dismiss any girl in the local area.
        menu:
            "Did you want to ask someone to leave?"
            "[RogueX.Name]" if RogueX.Loc == bg_current or RogueX in Party:
                call Girl_Dismissed(RogueX)
            "[KittyX.Name]" if KittyX.Loc == bg_current or KittyX in Party:
                call Girl_Dismissed(KittyX)
            "[EmmaX.Name]" if EmmaX.Loc == bg_current or EmmaX in Party:
                call Girl_Dismissed(EmmaX)
            "[LauraX.Name]" if LauraX.Loc == bg_current or LauraX in Party:
                call Girl_Dismissed(LauraX)
            "[JeanX.Name]" if JeanX.Loc == bg_current or JeanX in Party:
                call Girl_Dismissed(JeanX)
            "[StormX.Name]" if StormX.Loc == bg_current or StormX in Party:
                call Girl_Dismissed(StormX)
            "[JubesX.Name]" if JubesX.Loc == bg_current or JubesX in Party:
                call Girl_Dismissed(JubesX)
            "Nevermind.":
                pass
        return

label Locked_Door(Girl=0,Entry=0,Current=0): #rkeljsv
        # called when a girl tries to enter a locked room, mainly from the summon function
        # Girl is the indicated girl, Entry is True if you want to always have her enter with dialog
        # Current is a girl you are currently with
        if Girl not in TotalGirls:
                return
        if Current not in TotalGirls:
                $ Current = 0
        $ Player.AddWord(1,"interruption") #adds to Recent
        if not Trigger:
                #resets the scene if not during a sex act
                call Set_The_Scene
        if Girl == KittyX:
                if bg_current == "bg campus" or bg_current == "bg pool":
                        "Suddently, [Girl.Name] rounds a corner."
                else:
                        "You look to the door just as [KittyX.Name] phases into the room."
                $ KittyX.Loc = bg_current
                call Taboo_Level
                $ KittyX.OutfitChange()
                call Display_Girl(KittyX,TrigReset=0)
                ch_k "Hi, [KittyX.Petname]!"
                return 1
        if "locked" not in Player.Traits:
                $ Girl.Loc = bg_current
                if Entry:
                        call Display_Girl(Girl,TrigReset=0)
                        if bg_current == "bg campus" or bg_current == "bg pool":
                                "Suddently, [Girl.Name] rounds a corner."
                        else:
                                "Suddently, [Girl.Name] enters the room, apparently without knocking."
                        if Girl == RogueX:
                                ch_r "Hey, got a minute, [Girl.Petname]?"
                        elif Girl == EmmaX:
                                ch_e "[Girl.Petname], I had something I wanted to discuss. . ."
                        elif Girl == LauraX:
                                ch_l "Hey, [Girl.Petname]."
                        elif Girl == JeanX:
                                ch_j "Hey, [Girl.Petname]."
                        elif Girl == StormX:
                                ch_s "May I come in, [Girl.Petname]?"
                        elif Girl == JubesX:
                                ch_v "Hey, [Girl.Petname]."
                return 1
        if Girl.Loc == Girl.Home:
                "You hear a key in the lock, and [Girl.Name] enters the room."
        elif Girl == JeanX:
                "You hear a rattle at the door."
                "After a moment, and some clicking in the lock, the door pops open."
                "[JeanX.Name] walks into the room."
                $ JeanX.Loc = bg_current
                call Taboo_Level
                $ JeanX.OutfitChange()
                call Display_Girl(JeanX,TrigReset=0)
                ch_j "Hey, [JeanX.Petname]!"
                return 1
        else:
            "The doorknob jiggles. A moment later, you hear a knock."
            if Girl == RogueX:
                    ch_r "Could I come in, [Girl.Petname]?"
            elif Girl == EmmaX:
                    ch_e "[Girl.Petname], I'm waiting."
            elif Girl == LauraX:
                    ch_l "It's me."
            elif Girl == StormX:
                    ch_s "[Girl.Petname], may I come in?"
            elif Girl == JubesX:
                    ch_v "Hey, it's [Girl.Name]."
            menu:
                extend ""
                "Open door":
                        ch_p "Hold on, [Girl.Name]!"
                        "You unlock the door and let her in."
                        $ Girl.Loc = bg_current
                        $ Girl.OutfitChange()
                "Open door [[but stop fucking first]" if Trigger:
                        ch_p "Hold on, [Girl.Name]!"
                        call Sex_Over(1,Primary) #Cleans up after the sex stuff
                        "You unlock the door and let her in."
                        $ Girl.Loc = bg_current
                        $ Girl.OutfitChange()
                        call Display_Girl(Girl,TrigReset=0)
                        if Girl == RogueX:
                                ch_r "Hey, got a minute, [Girl.Petname]?"
                        elif Girl == EmmaX:
                                ch_e "[Girl.Petname], I had something I wanted to discuss. . ."
                        elif Girl == LauraX:
                                ch_l "Hey, [Girl.Petname]."
                        elif Girl == StormX:
                                ch_s "Hello, I wanted to talk with you. . ."
                        elif Girl == JubesX:
                                ch_v "Hey, [Girl.Petname]."
                        jump Misplaced
                "Send her away":
                        ch_p "Er, sorry, could you come back later?"
                        $ Girl.Statup("Love", 80, -2)
                        if Girl == RogueX:
                                ch_r "C'mon, [Girl.Petname], don't yank my chain like this!"
                                if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                                return 0
                        elif Girl == EmmaX:
                                $ Girl.Statup("Obed", 80, -2)
                                ch_e "I have to say, [EmmaX.Petname], I understand the appeal of having someone at your beck and call. . ."
                                ch_e "but I don't appreciate being on the receiving end!"
                                if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                                return 0
                        elif Girl in (LauraX,JubesX):
                            "[Girl.Name] goes quiet."
                            if ApprovalCheck(Girl, 500,"I") and not ApprovalCheck(Girl, 500,"O"):
                                    $ Girl.Loc = bg_current
                                    $ Girl.OutfitChange()
                                    if Girl == LauraX:
                                            $ LauraX.ArmPose = 2
                                            $ LauraX.Claws = 1
                                            "snickt"
                                            call Display_Girl(Girl,TrigReset=0) #fix, make a misty animation?
                                            "The door swings open."
                                            $ LauraX.Claws = 0
                                            ch_l "Hey, so I don't like being jerked around, so don't do that, okay?"
                                    else:
                                            "A thin mist passes under the door, and forms into a human shape."
                                            call Display_Girl(Girl,TrigReset=0)
                                            ch_v "Well, I wanted to talk."
                                    $ Girl.Statup("Obed", 80, -4)
                            else:
                                    $ Girl.Statup("Love", 80, -1)
                                    $ Girl.Statup("Obed", 80, 3)
                                    call AnyLine(Girl,"Ok.")
                                    "You hear her shuffling off."
                                    if Girl.Loc == bg_current:
                                        call Remove_Girl(Girl)
                                    return 0
                        elif Girl == StormX:
                            if ApprovalCheck(Girl, 800,"LI") and not ApprovalCheck(Girl, 500,"O"):
                                    $ Girl.Loc = bg_current
                                    $ Girl.OutfitChange()
                                    call Display_Girl(Girl,TrigReset=0)
                                    "You hear some clicking from the door."
                                    "The door swings open."
                                    $ Girl.Statup("Obed", 80, -4)
                                    ch_s "That was not a quality lock."
                            else:
                                    $ Girl.Statup("Love", 80, -1)
                                    $ Girl.Statup("Obed", 80, 3)
                                    ch_s ". . ."
                                    ch_s "Very well, I can respect that."
                                    if Girl.Loc == bg_current:
                                        call Remove_Girl(Girl)
                                    return 0
        if Current:
            if Current == EmmaX and ("three" not in EmmaX.History or "classcaught" not in EmmaX.History):
                    #Emma-specific code
                    $ Girl.AddWord(1,0,0,"saw with " + Current.Tag) #adds to Traits.
                    if bg_current == EmmaX.Home:
                            #if you're in her room. . .
                            ch_e "I. . . This isn't what it looks like. . ."
                            "She shoves the two of you out of her room and slams the door."
                            $ Girl.Loc = "bg player"
                            call Remove_Girl(EmmaX)
                    else:
                            ch_e "I. . . This isn't what it looks like. . ."
                            call Remove_Girl(EmmaX)
                            "She seems uncomfortable with the situation and leaves the room."
                            "Perhaps you should ask her about it later."
                    jump Misplaced

            if "poly " + Current.Tag in Girl.Traits or (Current in Player.Harem and Girl in Player.Harem):
                    #if they already have a relationship. . .
                    pass
            else:
                    #if they don't have a relationship. . .
                    if ApprovalCheck(Current, 1500, TabM=2, Bonus = (Girl.GirlLikeCheck(Current) - 500)):
                            #if the current girl approves of starting something. . .
                            $ Current.FaceChange("sexy", 1)
                            $ Current.Statup("Obed", 90, 5)
                            $ Current.Statup("Inbt", 90, 5)
                            $ Current.Statup("Lust", 90, 3)
                    else:
                            #the current girl isn't on board with this
                            $ Current.FaceChange("angry", 1)
                            if Current == RogueX:
                                    ch_r "Hey, [Girl.Tag], we're a little busy here?"
                            elif Current == KittyX:
                                    ch_k "Um, [Girl.Tag]? Read the room?"
                            elif Current == EmmaX:
                                    ch_e "[Girl.Tag], could you please leave?"
                            elif Current == LauraX:
                                    ch_l "Scram, [Girl.Tag]."
                            elif Current == JeanX:
                                    ch_j "Leave, [Girl.Tag]."
                            elif Current == StormX:
                                    ch_s "Would you mind give us some space?"
                            elif Current == JubesX:
                                    ch_v "Yeah, we were. . . busy."
                            $ Girl.AddWord(1,0,0,"saw with " + Current.Tag)
                            if Girl == RogueX:
                                    $ Girl.FaceChange("perplexed", 2)
                                    ch_r "Oh, sorry about that! I'll head out."
                            elif Girl == KittyX:
                                    $ Girl.FaceChange("perplexed", 2)
                                    ch_k "Oh! Sorrysorrysorry!"
                            elif Girl == EmmaX:
                                    $ Girl.FaceChange("bemused", 2)
                                    ch_e "I wouldn't want to spoil the mood. . ."
                            elif Girl == LauraX:
                                    ch_l "Oh, sure. Whatever."
                            elif Girl == JeanX:
                                    $ Girl.FaceChange("bemused", 1)
                                    ch_j "Fine."
                            elif Girl == StormX:
                                    $ Girl.FaceChange("bemused", 1)
                                    ch_s "Yes. . ."
                            elif Girl == JubesX:
                                    $ Girl.FaceChange("perplexed", 2)
                                    ch_v "Oh, yes! Sorry!"
                            $ Girl.FaceChange("sad", 1)
                            $ Current.FaceChange("sexy", 1)
                            if Girl.Loc == bg_current:
                                    call Remove_Girl(Girl)
                            return 0
            if Current == RogueX:
                    ch_r "Oh, [Girl.Tag], did you want to join in?"
            elif Current == KittyX:
                    ch_k "Um, [Girl.Tag]? Did you want something?"
            elif Current == EmmaX:
                    ch_e "Oh, [Girl.Tag]. . . care to join us?"
            elif Current == LauraX:
                    ch_l "Oh, hey, [Girl.Tag]."
            elif Current == JeanX:
                    ch_j "Hey."
            elif Current == StormX:
                    ch_s "Oh, hello [Girl.Tag], did you want to join in?"
            elif Current == JubesX:
                    ch_v "Hey, [Girl.Tag], did you need something?"
        #end current stuff
        $ Girl.Loc = bg_current
        call Taboo_Level
        $ Girl.OutfitChange(5)
        $ Player.DrainWord("locked",0,0,1)
        call Set_The_Scene(1,0,0,0)#characters, no entry, no clothes changes, no triggers

        if Partner == Girl:
                #if this is already a Partner, skip this dialog
                $ Silent = 1
        $ Partner = Girl
        $ Line = 0
        return 1

label Taboo_Level(Taboo_Loc=1,Teach=0,BO=[]): #rkeljsv
        #cycles through each girl, setting their taboo level.
        # if Taboo_Loc, will only work on local characters.
        #Set your taboo level

        if EmmaX.Loc == "bg teacher":
                $ EmmaX.Loc = "bg classroom" #Sets Emma to being in class if she's teaching
                $ Teach = 1
        elif StormX.Loc == "bg teacher":
                $ StormX.Loc = "bg classroom" #Sets Storm to being in class if she's teaching
                $ Teach = 2

        call CheckTaboo(Player,bg_current)

        $ BO = TotalGirls[:]
        if JeanX in BO and "nowhammy" not in JeanX.Traits:
                # So long as Jean is allowed to whammy students, she does not care about location.
                $ JeanX.Taboo = 0
                $ BO.remove(JeanX)
        while BO:
                #cycles through each girl possible, setting them to local if they are in the party
                #Then it checks their taboo level
                if BO[0] in Party:
                        $ BO[0].Loc = bg_current
                if BO[0].Loc == "nearby":
                        $ Taboo_Check = bg_current
                else:
                        $ Taboo_Check = BO[0].Loc
                if not Taboo_Loc or Taboo_Check == bg_current:
                        #only checks if they are local if it's not a general check
                        call CheckTaboo(BO[0],Taboo_Check)
                $ BO.remove(BO[0])

        if Teach == 2:
                $ StormX.Loc = "bg teacher" #Sets Storm to being a teacher again
        elif Teach:
                $ EmmaX.Loc = "bg teacher" #Sets Emma to being a teacher again
        return
        #end taboo level

label Speed_Shift(S=0):
        #adjusts the speed of animations to S, uses fade to hide glitches
        # call Speed_Shift(2)
        $ Speed = S
        show blackscreen onlayer black
        pause 0.01
        hide blackscreen onlayer black
        return

label Shop: #rkeljs
    menu:
        "You are logged into the store. You have [Player.Cash] dollars."
        "Buy dildo for $20.":
                if Player.Inventory.count("dildo") >= 10:
                    "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
                elif Player.Cash >= 20:
                    "You purchase one dildo."
                    $ Player.Inventory.append("dildo")
                    $ Player.Cash -= 20
                else:
                    "You don't have enough for that."
        "Buy \"Shocker\" vibrator for $25.":
                if Player.Inventory.count("vibrator") >= 10:
                    "If you bought one more vibrator, you would risk a geological event."
                elif Player.Cash >= 25:
                    "You purchase one vibrator."
                    $ Player.Inventory.append("vibrator")
                    $ Player.Cash -= 25
                else:
                    "You don't have enough for that."
        "Gifts for [RogueX.Name]":
            menu:
                "Buy green lace nighty for $75." if "nighty" not in RogueX.Inventory and "Rogue nighty" not in Player.Inventory:
                    if Player.Cash >= 75:
                        "You purchase the nighty, this will look nice on [RogueX.Name]."
                        $ Player.Inventory.append("Rogue nighty")
                        $ Player.Cash -= 75
                    else:
                        "You don't have enough for that."
                "Buy black lace bra for $90." if "lace bra" not in RogueX.Inventory and "Rogue lace bra" not in Player.Inventory:
                    if Player.Cash >= 90:
                        "You purchase the lace bra, this will look nice on [RogueX.Name]."
                        $ Player.Inventory.append("Rogue lace bra")
                        $ Player.Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "lace panties" not in RogueX.Inventory and "Rogue lace panties" not in Player.Inventory:
                    if Player.Cash >= 110:
                        "You purchase the lace panties, these will look nice on [RogueX.Name]."
                        $ Player.Inventory.append("Rogue lace panties")
                        $ Player.Cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in RogueX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(RogueX, 1500):
                    if Player.Cash >= 100:
                        "You purchase the stockings, these will look nice on [RogueX.Name]."
                        $ Player.Inventory.append("stockings and garterbelt")
                        $ Player.Cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy yellow bikini top for $50." if "bikini top" not in RogueX.Inventory and "Rogue bikini top" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "You purchase the bikini top, this will look nice on [RogueX.Name]."
                            $ Player.Inventory.append("Rogue bikini top")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."
                "Buy green bikini bottoms for $50." if "bikini bottoms" not in RogueX.Inventory and "Rogue bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "You purchase the bikini bottoms, these will look nice on [RogueX.Name]."
                            $ Player.Inventory.append("Rogue bikini bottoms")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [KittyX.Name]" if "met" in KittyX.History:
            menu:
                "Buy white lace bra for $90." if "lace bra" not in KittyX.Inventory and "Kitty lace bra" not in Player.Inventory:
                    if Player.Cash >= 90:
                        "You purchase the lace bra, this will look nice on [KittyX.Name]."
                        $ Player.Inventory.append("Kitty lace bra")
                        $ Player.Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "lace panties" not in KittyX.Inventory and "Kitty lace panties" not in Player.Inventory:
                    if Player.Cash >= 110:
                        "You purchase the lace panties, these will look nice on [KittyX.Name]."
                        $ Player.Inventory.append("Kitty lace panties")
                        $ Player.Cash -= 110
                    else:
                        "You don't have enough for that."

                "Buy pantyhose for $50." if "pantyhose" not in KittyX.Inventory and "Kitty pantyhose" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "You purchase the hose, these will look nice on [KittyX.Name]."
                        $ Player.Inventory.append("Kitty pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in KittyX.Inventory and "stockings and garterbelt" not in Player.Inventory:
                    if Player.Cash >= 100:
                        "You purchase the stockings, these will look nice on [KittyX.Name]."
                        $ Player.Inventory.append("stockings and garterbelt")
                        $ Player.Cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy knee-stockings for $50." if "knee" not in KittyX.Inventory and "knee" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "You purchase the stockings, these will look nice on [KittyX.Name]."
                        $ Player.Inventory.append("knee")
                        $ Player.Cash -= 50
                    else:
                        "You don't have enough for that."

                "Buy blue cat bikini top for $60." if "bikini top" not in KittyX.Inventory and "Kitty bikini top" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "You purchase the bikini top, this will look nice on [KittyX.Name]."
                            $ Player.Inventory.append("Kitty bikini top")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."
                "Buy blue bikini bottoms for $60." if "bikini bottoms" not in KittyX.Inventory and "Kitty bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "You purchase the bikini bottoms, these will look nice on [KittyX.Name]."
                            $ Player.Inventory.append("Kitty bikini bottoms")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."
                "Buy blue miniskirt for $50." if "blue skirt" not in KittyX.Inventory and "Kitty blue skirt" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "You purchase the blue skirt, this will look nice on [KittyX.Name]."
                            $ Player.Inventory.append("Kitty blue skirt")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [EmmaX.Name]" if "met" in EmmaX.History:
            menu:
                "Buy white lace bra for $90." if "lace bra" not in EmmaX.Inventory and "Emma lace bra" not in Player.Inventory:
                        if Player.Cash >= 90:
                            "You purchase the lace bra, this will look nice on [EmmaX.Name]."
                            $ Player.Inventory.append("Emma lace bra")
                            $ Player.Cash -= 90
                        else:
                            "You don't have enough for that."
                "Buy white lace panties for $110." if "lace panties" not in EmmaX.Inventory and "Emma lace panties" not in Player.Inventory:
                        if Player.Cash >= 110:
                            "You purchase the lace panties, these will look nice on [EmmaX.Name]."
                            $ Player.Inventory.append("Emma lace panties")
                            $ Player.Cash -= 110
                        else:
                            "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in EmmaX.Inventory and "Emma pantyhose" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "You purchase the hose, these will look nice on [EmmaX.Name]."
                        $ Player.Inventory.append("Emma pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in EmmaX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(EmmaX, 1500):
                    if Player.Cash >= 100:
                        "You purchase the stockings, these will look nice on [EmmaX.Name]."
                        $ Player.Inventory.append("stockings and garterbelt")
                        $ Player.Cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy white bikini top for $60." if "bikini top" not in EmmaX.Inventory and "Emma bikini top" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "You purchase the bikini top, this will look nice on [EmmaX.Name]."
                            $ Player.Inventory.append("Emma bikini top")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."
                "Buy white bikini bottoms for $60." if "bikini bottoms" not in EmmaX.Inventory and "Emma bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "You purchase the bikini bottoms, these will look nice on [EmmaX.Name]."
                            $ Player.Inventory.append("Emma bikini bottoms")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [LauraX.Name]" if "met" in LauraX.History:
            menu:
                "Buy red corset for $70." if "corset" not in LauraX.Inventory and "Laura corset" not in Player.Inventory:
                    if Player.Cash >= 70:
                        "You purchase the corset, this will look nice on [LauraX.Name]."
                        $ Player.Inventory.append("Laura corset")
                        $ Player.Cash -= 70
                    else:
                        "You don't have enough for that."
                "Buy red lace corset for $90." if "lace corset" not in LauraX.Inventory and "Laura lace corset" not in Player.Inventory:
                    if Player.Cash >= 90:
                        "You purchase the lace corset, this will look nice on [LauraX.Name]."
                        $ Player.Inventory.append("Laura lace corset")
                        $ Player.Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy red lace panties for $110." if "lace panties" not in LauraX.Inventory and "Laura lace panties" not in Player.Inventory:
                    if Player.Cash >= 110:
                        "You purchase the lace panties, these will look nice on [LauraX.Name]."
                        $ Player.Inventory.append("Laura lace panties")
                        $ Player.Cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy black bikini top for $50." if "bikini top" not in LauraX.Inventory and "Laura bikini top" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "You purchase the bikini top, this will look nice on [LauraX.Name]."
                            $ Player.Inventory.append("Laura bikini top")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "bikini bottoms" not in LauraX.Inventory and "Laura bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "You purchase the bikini bottoms, these will look nice on [LauraX.Name]."
                            $ Player.Inventory.append("Laura bikini bottoms")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."
                "Never mind.":
                    pass

        "Gifts for [JeanX.Name]" if "met" in JeanX.History:
            menu:
                "Buy black corset for $70." if "corset" not in JeanX.Inventory and "Jean corset" not in Player.Inventory:
                    if Player.Cash >= 70:
                        "You purchase the corset, this will look nice on [JeanX.Name]."
                        $ Player.Inventory.append("Jean corset")
                        $ Player.Cash -= 70
                    else:
                        "You don't have enough for that."
                "Buy green lace bra for $90." if "lace bra" not in JeanX.Inventory and "Jean lace bra" not in Player.Inventory:
                    if Player.Cash >= 90:
                        "You purchase the lace bra, this will look nice on [JeanX.Name]."
                        $ Player.Inventory.append("Jean lace bra")
                        $ Player.Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy green lace panties for $110." if "lace panties" not in JeanX.Inventory and "Jean lace panties" not in Player.Inventory:
                    if Player.Cash >= 110:
                        "You purchase the lace panties, these will look nice on [JeanX.Name]."
                        $ Player.Inventory.append("Jean lace panties")
                        $ Player.Cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy \"X\" bikini top for $50." if "bikini top" not in JeanX.Inventory and "Jean bikini top" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "You purchase the bikini top, this will look nice on [JeanX.Name]."
                            $ Player.Inventory.append("Jean bikini top")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "bikini bottoms" not in JeanX.Inventory and "Jean bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 50:
                            "You purchase the bikini bottoms, these will look nice on [JeanX.Name]."
                            $ Player.Inventory.append("Jean bikini bottoms")
                            $ Player.Cash -= 50
                        else:
                            "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in JeanX.Inventory and "Jean pantyhose" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "You purchase the hose, these will look nice on [JeanX.Name]."
                        $ Player.Inventory.append("Jean pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in JeanX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(JeanX, 800):
                    if Player.Cash >= 100:
                        "You purchase the stockings, these will look nice on [JeanX.Name]."
                        $ Player.Inventory.append("stockings and garterbelt")
                        $ Player.Cash -= 100
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [StormX.Name]" if "met" in StormX.History:
            menu:
                "Buy black lace bra for $90." if "lace bra" not in StormX.Inventory and "Storm lace bra" not in Player.Inventory:
                        if Player.Cash >= 90:
                            "You purchase the lace bra, this will look nice on [StormX.Name]."
                            $ Player.Inventory.append("Storm lace bra")
                            $ Player.Cash -= 90
                        else:
                            "You don't have enough for that."
                "Buy black lace panties for $110." if "lace panties" not in StormX.Inventory and "Storm lace panties" not in Player.Inventory:
                        if Player.Cash >= 110:
                            "You purchase the lace panties, these will look nice on [StormX.Name]."
                            $ Player.Inventory.append("Storm lace panties")
                            $ Player.Cash -= 110
                        else:
                            "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in StormX.Inventory and "Storm pantyhose" not in Player.Inventory:
                    if Player.Cash >= 50:
                        "You purchase the hose, these will look nice on [StormX.Name]."
                        $ Player.Inventory.append("Storm pantyhose")
                        $ Player.Cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in StormX.Inventory and "stockings and garterbelt" not in Player.Inventory and ApprovalCheck(StormX, 1500):
                    if Player.Cash >= 100:
                        "You purchase the stockings, these will look nice on [StormX.Name]."
                        $ Player.Inventory.append("stockings and garterbelt")
                        $ Player.Cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy black bikini top for $60." if "bikini top" not in StormX.Inventory and "Storm bikini top" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "You purchase the bikini top, this will look nice on [StormX.Name]."
                            $ Player.Inventory.append("Storm bikini top")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."
                "Buy black bikini bottoms for $60." if "bikini bottoms" not in StormX.Inventory and "Storm bikini bottoms" not in Player.Inventory:
                        if Player.Cash >= 60:
                            "You purchase the bikini bottoms, these will look nice on [StormX.Name]."
                            $ Player.Inventory.append("Storm bikini bottoms")
                            $ Player.Cash -= 60
                        else:
                            "You don't have enough for that."
                "Never mind.":
                    pass

        "Buy books":
            menu Shop_Books:
                "Buy \"Dazzler and Longshot\" for $20.":
                    "A sappy romantic novel about two starcrossed lovers."
                    if "DL" not in Shop_Inventory: #if Inventory_Check("Dazzler and Longshot") >= 4:
                        "They seem to be out of stock at the moment."
                    elif Player.Cash >= 20:
                        "You purchase the book."
                        $ Shop_Inventory.remove("DL")
                        $ Player.Inventory.append("Dazzler and Longshot")
                        $ Player.Cash -= 20
                    else:
                        "You don't have enough for that."
                "Buy \"256 Shades of Grey\" for $20.":
                    "A gripping sexual thriller about a stern red-headed \"goblin queen\" and her subject."
                    if "G" not in Shop_Inventory: #if "256 Shades of Grey" in Player.Inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.Cash >= 20:
                        "You purchase the book."
                        $ Shop_Inventory.remove("G")
                        $ Player.Inventory.append("256 Shades of Grey")
                        $ Player.Cash -= 20
                    else:
                        "You don't have enough for that."
                "Buy \"Avengers Tower Penthouse\" for $20.":
                    "A book filled with nude pictures of various Avengers, sexy."
                    if "A" not in Shop_Inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.Cash >= 20:
                        "You purchase the book."
                        $ Shop_Inventory.remove("A")
                        $ Player.Inventory.append("Avengers Tower Penthouse")
                        $ Player.Cash -= 20
                    else:
                        "You don't have enough for that."
                "Back":
                    jump Shop
            jump Shop_Books
        "Buy Cologne":
            if Day < 50:
                "These are currently out of stock, check back later."
                jump Shop
            menu:
                "Examine the Mandrill Cologne (\"Nothin says lovin like a shiny red butt\").":
                    menu:
                        "This cologne is guaranteed to make women love you more [[+Love]."
                        "Buy Mandrill Cologne for $150":
                            pass
                        "Never mind.":
                            jump Shop
                    if "Mandrill Cologne" in Player.Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.Cash >= 150:
                        "You purchase one bottle of Mandrill Cologne."
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Inventory.append("Mandrill Cologne")
                        $ Player.Cash -= 150
                    else:
                        "You don't have enough for that."
                "Examine the Purple Rain Cologne (\"They can't resist your charms\").":
                    menu:
                        "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]."
                        "Buy Purple Rain Cologne for $200":
                            pass
                        "Never mind.":
                            jump Shop
                    if "Purple Rain Cologne" in Player.Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.Cash >= 200:
                        "You purchase one bottle of Purple Rain Cologne."
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Inventory.append("Purple Rain Cologne")
                        $ Player.Cash -= 200
                    else:
                        "You don't have enough for that."
                "Examine the Corruption Cologne (\"Let the wild out\").":
                    menu:
                        "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]."
                        "Buy Corruption Cologne for $250":
                            pass
                        "Never mind.":
                            jump Shop
                    if "Corruption Cologne" in Player.Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.Cash >= 250:
                        "You purchase one bottle of Corruption Cologne."
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Inventory.append("Corruption Cologne")
                        $ Player.Cash -= 250
                    else:
                        "You don't have enough for that."
                "Back":
                    pass
        "Exit Store":
            return
    jump Shop
    return

label Set_The_Scene(Chr = 1, Entry = 0, Dress = 1, TrigReset = 1, Quiet=0,BO=[]): #rkeljsv
        # If Chr, then display the characters in the room
        # If Entry, then show the "entry" version of a room, such as a closed door, does not display characters
        # If Dress, then check whether the character is underdressed when displaying her
        # Trigreset resets triggers
        # if Quiet, no fade to black

        if not Quiet:
                show blackscreen onlayer black

        if Entry:
                $ Chr = 0
                call AllHide

        call display_background(entering = Entry)

        if Time_Count >= 3:
                show NightMask onlayer nightmask
        else:
                hide NightMask onlayer nightmask

        if TrigReset:
                # resets triggers
                $ Trigger = 0
                $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
                $ Trigger3 = 0
                $ Trigger4 = 0
                $ Trigger5 = 0
                $ TrigReset = 0

        if Chr:
                call Present_Check  #culls out Party to 2,
                #sets location to bg_current, removes extra girls, sets Focus to a girl in the room

                $ BO = TotalGirls[:]

                while BO:
                        #loops through and makes choices.
                        if Ch_Focus != BO[0]:
                                #moves all other girls to Stage Right, 75 layer
                                $ BO[0].sprite_location = StageRight
                                $ BO[0].Layer = 75
                        call Display_Girl(BO[0],Dress,TrigReset)
                        $ BO.remove(BO[0])
                # set and display primary girl
                if Ch_Focus.Loc == bg_current:
                        $ Ch_Focus.sprite_location = StageCenter
                        $ Ch_Focus.Layer = 100
                        call Display_Girl(Ch_Focus,Dress,TrigReset)

                if bg_current == "bg study" and Time_Count < 3:
                        show Professor at sprite_location(StageLeft) zorder 25
                else:
                        hide Professor

        else:
                call AllHide(1) #removes all girls that aren't there.
        show Chibi_UI
        hide Cellphone

        if bg_current == "bg classroom":
            if EmmaX.Loc == "bg teacher":
                    #if Emma is teaching, sets teaching outfit
                    #call AltClothes(EmmaX,8)
                    $ EmmaX.OutfitChange()
            if StormX.Loc == "bg teacher":
                    #if Storm is teaching, sets teaching outfit
                    #call AltClothes(StormX,8)
                    $ StormX.OutfitChange()

        if bg_current != "bg pool":
                #hides pool overlay if not in the pool area
                hide FullPool
        if TrigReset and Dress:
                #resets your clothing if nude
                call Get_Dressed

        hide DressScreen
        if "Historia" in Player.Traits: #Simulation haze
                show BlueScreen onlayer black
        else:
                hide BlueScreen onlayer black
        hide blackscreen onlayer black

        return

label Shift_Focus(Chr = RogueX, Second = 0,BO=[],Return=0):
        #When used like Shift_Focus(KittyX), changes the focus character and relative default positions
        if Chr not in TotalGirls:
                "Tell Oni [Chr]"
                "Then Tell Oni [Chr.Tag]"
        if Chr == Ch_Focus == Partner:
                #if somehow the partner and chosen girl are the same. . .
                $ BO = TotalGirls[:]
                if Partner in TotalGirls:
                        $ BO.remove(Partner)
                else:
                        "Tell Oni, in Shift Focus, P:[Partner]"
                while BO:
                        #loops through and makes choices.
                        if BO[0].Loc == bg_current:
                                $ Partner = BO[0]
                        $ BO.remove(BO[0])
                #if anyone else is in the room, make her the partner. Do I want this?
        if Chr.Loc == bg_current:
                #If she is where you're at. . .
                $ BO = TotalGirls[:]
                if Chr in TotalGirls:
                        $ BO.remove(Chr)
                else:
                        "Tell Oni, in Shift Focus, C:[Chr]"
                while BO:
                        #loops through and makes choices.
                        if BO[0].Loc == bg_current:
                                #if other girl is in the room, shift her to second position
                                $ BO[0].sprite_location = StageRight
                                $ BO[0].Layer = 75
                                $ BO = [1]
                        $ BO.remove(BO[0])
                #and move Girl to first position
                $ Chr.sprite_location = StageCenter
                $ Chr.Layer = 100
        if Ch_Focus == Chr:
                #If Girl was already the focal character, return
                pass
        elif Second and Second != Chr:
                #if a deliberate partner was offered to the call, use it
                $ Partner = Second
        elif Partner == Chr:
                #If Chr was the Partner in a scene, make the existing focal character the Partner
                $ Partner = Ch_Focus
        $ Ch_Focus = Chr
        if Partner == Chr:
                $ Partner = 0

        $ renpy.restart_interaction()
        return

transform sprite_location(x_location = StageRight, y_location = 50):
    pos (x_location, y_location)

label Display_Girl(Chr=0,Dress = 1, TrigReset = 1, DLoc = 0, YLoc=50): #rkeljsv
                # If Dress, then check whether the character is underdressed when displaying her
                # call Display_Girl(RogueX,0,0)
                if Chr not in TotalGirls:
                        "Tell Oni that in Display_Girl, Chr is [Chr]"
                        return

                if Chr not in Party and Chr.Loc != bg_current:
                        # If girl isn't there, put her away
                        call hide_girl(Chr, sprite = True)
                        $ Chr.OutfitChange(Changed=1)
                        return

                if Dress:
                        if Chr.Outfit == "swimwear":
                                if Chr.Loc == "bg pool":
                                        $ Chr.OutfitChange(Changed=1)
                                elif Chr.OutfitDay != "swimwear":
                                        $ Chr.Outfit = Chr.OutfitDay
                                        $ Chr.OutfitChange(Changed=1)
                        elif Taboo: #If not in the showers, get dressed and dry off
                                $ Chr.OutfitChange(Changed=1)
                        elif Chr.Loc != "bg dangerroom" and Chr.OutfitDay != "gym":
                                #if she's not in the gym and arw wearing gym clothes. . .
                                $ Chr.Outfit = Chr.OutfitDay
                                $ Chr.OutfitChange(Changed=1)

                elif Chr.Loc != "bg showerroom" and Chr.Loc != "bg pool":
                        $ Chr.Water = 0

                if TrigReset:
                        # resets triggers
                        $ Trigger = 0
                        $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
                        $ Trigger3 = 0
                        $ Trigger4 = 0
                        $ Trigger5 = 0

                if Partner == Chr:
                        $ DLoc = StageRight #Moves Girl over if she's secondary

                if DLoc: #if sent a pre-location, use that, otherwise, accept the existing one.
                        $ Chr.sprite_location = DLoc
                else:
                        $ DLoc = Chr.sprite_location

                call hide_girl(Chr)

                #displays girl if present, Sets her as local if in a party
                $ Chr.Loc = bg_current

                if Dress:
                        #If in public, check to see if clothes are too sexy, and change them if necessary
                        call OutfitShame(Chr)

                if bg_current == "bg movies" or bg_current == "bg restaurant":
                        #shifts them downward if on a date
                        $ YLoc = 250

                #Display Girl
                if Chr == RogueX:
                        show Rogue_Sprite at sprite_location(DLoc,YLoc) zorder Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)
                elif Chr == KittyX:
                        show Kitty_Sprite at sprite_location(DLoc,YLoc) zorder Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)
                elif Chr == EmmaX:
                        show Emma_Sprite at sprite_location(DLoc,YLoc) zorder Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)
                elif Chr == LauraX:
                        $ Chr.Claws = 0 # Resets her claws
                        show Laura_Sprite at sprite_location(DLoc,YLoc) zorder Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)
                elif Chr == JeanX:
                        show Jean_Sprite at sprite_location(DLoc,YLoc) zorder Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)
                elif Chr == StormX:
                        show Storm_Sprite at sprite_location(DLoc,YLoc) zorder Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)
                elif Chr == JubesX:
                        show Jubes_Sprite at sprite_location(DLoc,YLoc) zorder Chr.Layer:
                                alpha 1
                                zoom 1
                                offset (0,0)
                                anchor (0.5, 0.0)
                #End show Chr
                return

label ViewShift(Girl=0,View=0,ShouldHide=1,ViewTrig=Trigger):
    # Allows you to shift the viewpoint of a girl in fondling modes
    # call ViewShift(RogueX,"breasts")
    if Girl not in TotalGirls:
            return
    if View == "menu":
            if not renpy.showing(Girl.Tag+"_Sprite") and not renpy.showing(Girl.Tag+"_Doggy_Animation") and not renpy.showing(Girl.Tag+"_SexSprite"):
                    #if she's not already visible, this should not work
                    return
            menu:
                    "Full Body":
                            call reset_position(Girl, trigger = ViewTrig, set = True)
                    "Upper half":
                            call breasts_launch(Girl, trigger = ViewTrig)
                    "Middle View":
                            call expression Girl.Tag + "_Middle_Launch" pass (ViewTrig)
                    "Lower half":
                            call pussy_launch(Girl, trigger = ViewTrig)
                    "Rear view" if Girl in (RogueX,KittyX,EmmaX,LauraX,JeanX):
                            $ Girl.Pose = "doggy"
                            call expression Girl.Tag + "_Sex_Launch" pass (ViewTrig)
                    "On top of you" if Girl in (EmmaX,JeanX,StormX):
                            $ Girl.Pose = "sex"
                            call expression Girl.Tag + "_Sex_Launch" pass (ViewTrig)
                    "Laying down" if Girl in (RogueX,KittyX,LauraX):
                            $ Girl.Pose = "sex"
                            call expression Girl.Tag + "_Sex_Launch" pass (ViewTrig)
                    "Never mind":
                            pass
    else:
                    if ShouldHide:
                            call hide_girl(Girl)
                    if View == "full":
                            call reset_position(Girl, trigger = ViewTrig, set = True)
                    elif View == "breasts":
                            call breasts_launch(Girl, trigger = ViewTrig)
                    elif View == "mid":
                            call expression Girl.Tag + "_Middle_Launch" pass (ViewTrig)
                    elif View == "pussy":
                            call pussy_launch(Girl, trigger = ViewTrig)
                    elif View == "doggy" or View == "sex":
                            call expression Girl.Tag + "_Sex_Launch" pass (ViewTrig)
                    elif View == "kiss":
                            call kissing_launch(Girl, trigger = ViewTrig)
    return

image Punchout:
    Null(0,0)

label Punch:
    #causes the screen to shake a bit
    show Punchout with vpunch
    hide Punchout
    return

label AllReset(Chr = 0,BO=[]): #rkeljsv
    #resets all the sex animation poses
    #call AllReset("all")
    if Chr in TotalGirls:
            $ BO = [Chr]
    else:
            $ BO = TotalGirls[:]

    while BO:
            call expression BO[0].Tag + "_BJ_Reset"
            call expression BO[0].Tag + "_TJ_Reset"
            call expression BO[0].Tag + "_HJ_Reset"
            call expression BO[0].Tag + "_Sex_Reset"
            call expression BO[0].Tag + "_Doggy_Reset"
            call hide_girl(BO[0])
            if BO[0] == RogueX:
                if RogueX.Loc == bg_current:
                        show Rogue_Sprite at sprite_location(RogueX.sprite_location,50) zorder RogueX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0)
                        show Rogue_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0) pos (RogueX.sprite_location,50)
                else:
                        hide Rogue_Sprite
            elif BO[0] == KittyX:
                if KittyX.Loc == bg_current:
                        show Kitty_Sprite at sprite_location(KittyX.sprite_location,50) zorder KittyX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                        show Kitty_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (KittyX.sprite_location,50)
                else:
                        hide Kitty_Sprite
            elif BO[0] == EmmaX:
                if EmmaX.Loc == bg_current:
                        show Emma_Sprite at sprite_location(EmmaX.sprite_location,50) zorder EmmaX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                        show Emma_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (EmmaX.sprite_location,50)
                else:
                        hide Emma_Sprite
            elif BO[0] == LauraX:
                if LauraX.Loc == bg_current:
                        show Laura_Sprite at sprite_location(LauraX.sprite_location,50) zorder LauraX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                        show Laura_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (LauraX.sprite_location,50)
                else:
                        hide Laura_Sprite
            elif BO[0] == JeanX:
                if JeanX.Loc == bg_current:
                        show Jean_Sprite at sprite_location(JeanX.sprite_location,50) zorder JeanX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                        show Jean_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (JeanX.sprite_location,50)
                else:
                        hide Jean_Sprite
            elif BO[0] == StormX:
                if StormX.Loc == bg_current:
                        show Storm_Sprite at sprite_location(StormX.sprite_location,50) zorder StormX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                        show Storm_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (StormX.sprite_location,50)
                else:
                        hide Storm_Sprite
            elif BO[0] == JubesX:
                if JubesX.Loc == bg_current:
                        show Jubes_Sprite at sprite_location(JubesX.sprite_location,50) zorder JubesX.Layer:
                                ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                        show Jubes_Sprite:
                                zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (JubesX.sprite_location,50)
                else:
                        hide Jubes_Sprite
            $ BO.remove(BO[0])
    return

label AllHide(Cull=0): #rkeljsv
        if Cull or RogueX.Loc != bg_current:
            call hide_girl(RogueX, sprite = True)
        if Cull or KittyX.Loc != bg_current:
            call hide_girl(KittyX, sprite = True)
        if Cull or EmmaX.Loc != bg_current:
            call hide_girl(EmmaX, sprite = True)
        if Cull or LauraX.Loc != bg_current:
            call hide_girl(LauraX, sprite = True)
        if Cull or JeanX.Loc != bg_current:
            call hide_girl(JeanX, sprite = True)
        if Cull or StormX.Loc != bg_current:
            call hide_girl(StormX, sprite = True)
        if Cull or JubesX.Loc != bg_current:
            call hide_girl(JubesX, sprite = True)
        if Cull or "bg study" != bg_current:
                hide Professor
        return

label Sex_Menu_Threesome(Girl=0): #rkeljsv
        if not Girl or Girl not in TotalGirls:
            return

        menu:
            "Do you want to join us [RogueX.Name]?" if RogueX.Loc == bg_current and Girl != RogueX:
                    if Partner == RogueX:
                        #if she's already involved
                        ch_r "If I'd been do'in it right you wouldn't hafta ask. . ."
                    else:
                        if Girl == JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(RogueX)
                        call Girls_Noticed(Girl,RogueX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_r "Oh, well. . . I'm still game. . ."
                            call Rogue_SexAct("switch")
                        elif RogueX.Loc == bg_current:
                            ch_r "I s'pose I could lend a hand . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room."

            "Do you want to join us [KittyX.Name]?" if KittyX.Loc == bg_current and Girl != KittyX:
                    if Partner == KittyX:
                        #if she's already involved
                        ch_k "Lol, what are you even talking about?"
                    else:
                        if Girl == JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(KittyX)
                        call Girls_Noticed(Girl,KittyX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_k "Whoa, drama much? . ."
                            call Kitty_SexAct("switch")
                        elif KittyX.Loc == bg_current:
                            ch_k "I could[KittyX.like]give it a try. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room."

            "Do you want to join us [EmmaX.Name]?" if EmmaX.Loc == bg_current and Girl != EmmaX:
                    if Partner == EmmaX:
                        #if she's already involved
                        ch_e "Have I not been keeping up?"
                    else:
                        if Girl == JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(EmmaX)
                        call Girls_Noticed(Girl,EmmaX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_e "Pity. . ."
                            call Emma_SexAct("switch")
                        elif EmmaX.Loc == bg_current:
                            ch_e "So what did you have in mind for us. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room."

            "Do you want to join us [LauraX.Name]?" if LauraX.Loc == bg_current and Girl != LauraX:
                    if Partner == LauraX:
                        #if she's already involved
                        ch_l "I already am."
                    else:
                        if Girl == JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(LauraX)
                        call Girls_Noticed(Girl,LauraX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_l "Her loss. . ."
                            call Laura_SexAct("switch")
                        elif LauraX.Loc == bg_current:
                            ch_l "Hm, ok. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room."

            "Do you want to join us [JeanX.Name]?" if JeanX.Loc == bg_current and Girl != JeanX:
                    if Partner == JeanX:
                        #if she's already involved
                        ch_j "I've been here the entire time. . ."
                    else:
                        call Girls_Noticed(Girl,JeanX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_j "Huh. Her loss. . ."
                            call Jean_SexAct("switch")
                        elif JeanX.Loc == bg_current:
                            ch_j "Sure."
                        else:
                            "She seems annoyed with this whole situation and leaves the room."

            "Do you want to join us [StormX.Name]?" if StormX.Loc == bg_current and Girl != StormX:
                    if Partner == StormX:
                        #if she's already involved
                        ch_s "You hadn't noticed?"
                    else:
                        if Girl == JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(StormX)
                        call Girls_Noticed(Girl,StormX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_s "Oh, that's too bad. . ."
                            call Storm_SexAct("switch")
                        elif StormX.Loc == bg_current:
                            ch_s "Delighted. . ."
                        else:
                            "She seems uncomfortable with this situation and leaves the room."

            "Do you want to join us [JubesX.Name]?" if JubesX.Loc == bg_current and Girl != JubesX:
                    if Partner == JubesX:
                        #if she's already involved
                        ch_v "I thought I already was!"
                    else:
                        if Girl == JeanX:
                                #this raises a girl's like-Jean stat if Jean wants to sleep with her
                                call Girl_Whammy(JubesX)
                        call Girls_Noticed(Girl,JubesX,1)
                        if Girl.Loc != bg_current:
                            # if the lead ran away
                            ch_v "Oh, well. . ."
                            call Jubes_SexAct("switch")
                        elif JubesX.Loc == bg_current:
                            ch_v "Sure!"
                        else:
                            "She seems uncomfortable with this situation and leaves the room."

            "Never mind [[something else]":
                    pass
        if AloneCheck(Girl) and Girl.Taboo == 20:
                $ Girl.Taboo = 0
                $ Taboo = 0
        return

label Partner_Like(Girl=0,Value=1,AltValue=1,Measure=800,Partner=Partner):
        # This raises a partner's "like" stat by an amount
        # call Partner_Like(RogueX,2)
        # Girl is the lead, Partner is the second girl
        # Value is the amount it changes if Measure is met, otherwise AltValue
        if Girl not in TotalGirls or Partner not in TotalGirls: #should remove "character don't exist" errors
                return

        if Trigger4:
                # if the Partner is doing a secondary action. . .
                if Trigger4 == "watch":
                        pass
                elif Trigger4 in ("hand","blow"):
                        $ Value += 1
                elif Trigger4 in ("lick pussy","lick ass"):
                        $ Value += 3
                else:
                        $ Value += 2
        #End Trigger4 bonuses

        $ Partner.GLG(Girl,Measure,Value,1)
        $ Girl.GLG(Partner,Measure,Value,1)
        return

label GirlWaitUp(Local=0,Check=70,D20=0,Teach=0,BOA=[],BOB=[]):  #rkeljsv
        #This adjusts girl's liking each other based on shared activities
        #Local =1 only checks if they are in the room with you.
        #it goes R+K, R+E, R+L, K+E, K+L, E+L, etc.
        # was call GirlWaitAttract()
        # now call GirlWaitUp

        $ D20 = renpy.random.randint(0,1) if not D20 else D20

        if EmmaX.Loc == "bg teacher":
                $ EmmaX.Loc = "bg classroom" #Sets Emma to being in class if she's teaching
                $ Teach = 1
        elif StormX.Loc == "bg teacher":
                $ StormX.Loc = "bg classroom" #Sets Storm to being in class if she's teaching
                $ Teach = 2
        $ BOA = TotalGirls[:]
        #$ BOA.extend(TotalGirls)
        while BOA:
            #loops through the girls in an outer loop
            $ BOB = TotalGirls[:]
            while BOB:
                    #loops through the girls in an inner loop
                    if BOA[0] != BOB[0] and BOA[0].Loc == BOB[0].Loc:
                            #if the two girls are not identical, and are in the same location. . .
                            if BOA[0].Loc == "bg classroom":
                                            $ BOA[0].GLG(BOB[0],700,1,1)
                                            #R_LikeKitty += 1
                            elif BOA[0].Loc == "bg dangerroom":
                                            $ BOA[0].GLG(BOB[0],700,(1+D20),1)
                                            #R_LikeKitty += 1+D20
                            elif BOA[0].Loc == "bg showerroom":
                                    if BOA[0] == EmmaX:
                                            #if it's EmmaX. . .
                                            $ BOA[0].GLG(BOB[0],900,3,1)
                                            #EmmaX.LikeKitty += 3
                                    elif BOB[0] in (EmmaX,StormX) and BOA[0] != LauraX:
                                            #If it's anyone other than Laura seeing Emma's body. . .
                                            $ BOA[0].GLG(BOB[0],900,3,1)
                                            #RogueX.LikeEmma += 3
                                    else:
                                            $ BOA[0].GLG(BOB[0],900,2,1)
                                            #RogueX.LikeKitty += 2
                            else:
                                    $ BOA[0].GLG(BOB[0],Check, D20,1)
                                    #RogueX.LikeKitty += D20

                            #RogueX.LikeKitty += (int(KittyX.Shame/5)) #Rogue likes Kitty based on how slutty Kitty looks
                            if BOA[0] == EmmaX:
                                    #if it's Emma. . .
                                    #raise Emma's like by 1/4 other girl's shame
                                    $ BOA[0].GLG(BOB[0],1000,(int(BOB[0].Shame/4)),1)
                            elif BOB[0] in (EmmaX,StormX) and BOA[0] != LauraX:
                                    #If it's anyone other than Laura seeing Emma's body. . .
                                    #raise girl's like by 1/4 other girl's shame
                                    $ BOA[0].GLG(BOB[0],1000, (int(BOB[0].Shame/4)),1)
                            else:
                                    #raise girls's like by 1/5 other girl's shame
                                    $ BOA[0].GLG(BOB[0],1000, (int(BOB[0].Shame/5)),1)

                    $ BOB.remove(BOB[0])
            $ BOA.remove(BOA[0])

        if Teach == 2:
                $ StormX.Loc = "bg teacher" #Sets Storm to being a teacher again
        elif Teach:
                $ EmmaX.Loc = "bg teacher" #Sets Emma to being a teacher again
        return

label Jumped(Act=0): #rkeljsv
        # called by JumperCheck if a girl jumps you
        # Girls[0] is the girl
        # make sure that this puts people in the right rooms after they do stuff. . .

        if Girls[0] == EmmaX and Partner and "three" not in EmmaX.History:
                    #if lead is Emma, there is a partner, but she doesn't share. . .
                    $ Girls.remove(Partner)
                    $ Partner = 0
        elif EmmaX in Girls and ((Taboo and "taboo" not in EmmaX.History) or "three" not in EmmaX.History):
                    #if partner is Emma and she doesn't share. . .
                    $ Girls.remove(EmmaX)
                    $ Partner = 0

        if not Girls:
                return

        if Girls[0].Loc != bg_current and "locked" in Player.Traits:
            #if the girl is not in the room with you, and your door is locked. . .
            call Locked_Door(Girls[0])
            if not Girls or Girls[0].Loc != bg_current:
                    #if you refused her entry. . .
                    $ Player.RecentActions.append("nope")
                    return

        #sets their location
        $ BO = Girls[:]
        while BO:
                $ BO[0].Loc = bg_current
                $ BO.remove(BO[0])
        $ Girls[0].AddWord(1,"jumped","jumped")

        call Taboo_Level #makes sure Taboo level is accurate

        if Taboo and (not ApprovalCheck(Girls[0], 1500, TabM=3) or (Girls[0] == EmmaX and Taboo and "taboo" not in EmmaX.History)):
                #causes you to leave if the girl is not ready for public stuff
                $ Act = "leave"

        if bg_current in PersonalRooms:
                #Causes the girl to pull you out if she doesn't live in the room you're in
                if bg_current == "bg player":
                                pass
                elif Girls[0].Home != bg_current and not (Partner and Partner.Home == bg_current):
                                #if it's not the first girl's room, and also not the second's
                                $ Act = "leave"

        if Room_Full(): #if the room is full. . .
                $ Act = "leave"

        call Shift_Focus(Girls[0]) #this is not working, sometimes?
        call Set_The_Scene

        $ Player.RecentActions.append("jumped")
        $ Girls[0].FaceChange("sly",1)
        if Act == "leave":
                #if she's not supercool with public stuff. . .
                "Suddenly, [Girls[0].Name] grabs your arm with a miscevious smile, and starts to lead you back towards your room."
                menu:
                    "Go along with it":
                        $ Girls[0].Statup("Inbt", 95, 3)
                        "You follow after her."
                    "Pull away from her and head back.":
                        $ Girls[0].Statup("Love", 90, -10)
                        $ Girls[0].Statup("Obed", 50, 10)
                        $ Girls[0].Statup("Obed", 95, 5)
                        $ Girls[0].Statup("Inbt", 95, -5)
                        $ Girls[0].FaceChange("sad",1)
                        "You tell her to cut it out, and head back to what you were doing."
                        $ Player.RecentActions.append("nope")
                        $ Girls[0].AddWord(1,"refused","refused")
                        if not ApprovalCheck(Girls[0], 500, "O"):
                                $ Girls[0].AddWord(1,"angry","angry")
                        return

                if Partner:
                        "[Partner.Name] also follows along behind you."

                $ bg_current = "bg player"
                call CleartheRoom(Girls[0],1,1)

                #call Taboo_Level #makes sure Taboo level is accurate, moved lower in chain
        else:
            if Partner in TotalGirls:
                    $ Girls[1].FaceChange("sly",1)
                    "Suddenly, [Girls[0].Name] pulls you aside and [Partner.Name] follows along."
            else:
                    "Suddenly, [Girls[0].Name] pulls you aside."
            menu:
                    "See where this is going":
                        $ Girls[0].Statup("Inbt", 95, 2)
                    "Not here [[head to your room]":
                        $ Girls[0].Statup("Inbt", 95, 1)
                        "You head to your room first."
                        $ bg_current = "bg player"
                        call CleartheRoom(Girls[0],1,1)
                    "Pull away from her and head back.":
                        $ Girls[0].Statup("Love", 90, -10)
                        $ Girls[0].Statup("Obed", 50, 10)
                        $ Girls[0].Statup("Obed", 95, 5)
                        $ Girls[0].Statup("Inbt", 95, -5)
                        $ Girls[0].FaceChange("sad",1)
                        "You tell her to cut it out, and head back to what you were doing."
                        $ Player.RecentActions.append("nope")
                        $ Girls[0].AddWord(1,"refused","refused")
                        if not ApprovalCheck(Girls[0], 500, "O"):
                                $ Girls[0].AddWord(1,"angry","angry")
                        return

        $ BO = Girls[:]
        while BO:
                $ BO[0].Loc = bg_current
                $ BO.remove(BO[0])

        call Taboo_Level #makes sure Taboo level is accurate
        call Set_The_Scene(Dress=0)

        $ Girls[0].AddWord(1,"jumped","jumped",0,"jumped") #adds jumped to recent, daily, and history

        if Girls[0] == RogueX:
                ch_r "You've been dodge'in me lately."
                ch_r "Figured it was about time we did something about that."
        elif Girls[0] == KittyX:
                ch_k "Why haven't you been coming by?"
                ch_k "Wouldn't you enjoy some \"Kitty\" time?"
        elif Girls[0] == EmmaX:
                ch_e "You haven't been coming around to visit lately."
                ch_e "Is there any way I could tempt you?"
        elif Girls[0] == LauraX:
                ch_l "I'm horny, let's fuck."
        elif Girls[0] == JeanX:
                ch_j "Hey, I'm kinda horny, let's fuck."
        elif Girls[0] == StormX:
                ch_s "You haven't been taking care of your duties. . ."
        elif Girls[0] == JubesX:
                ch_v "I wouldn't mind some attention here. . ."
        else:
                return

        call Favorite_Actions(Girls[0],1) #returns a string of the action
        $ Act = _return
        $ Situation = Girls[0]

        if Act in ("anal","sex","blow","tit","hand","hotdog"):
                # if cock needs to be out. . .
                "[Girls[0].Name] reaches down and unzips your fly. . ."
                if not Player.Semen:
                    "You wish you weren't already drained. . . you stop her hands."
                    ch_p "I could actually use a break right now. . "
                    $ Act = "fondle breasts"
                else:
                    call Seen_First_Peen(Girls[0],Partner,1)

        if Partner:
                call Girls_Noticed(Girls[0],1) #calls the "noticed check" for this girl.

        # launches the appropriate scene based on the sex act in question.
        if Act == "anal":
                call expression Girls[0].Tag + "_AnalPrep" #call R_AnalPrep
        elif Act == "sex":
                call expression Girls[0].Tag + "_SexPrep" #call R_SexPrep
        elif Act ==  "lick pussy":
                call expression Girls[0].Tag + "_LP_Prep" #call R_LPlayer.Prep
        elif Act == "fondle pussy":
                call expression Girls[0].Tag + "_FP_Prep" #call R_FPlayer.Prep
        elif Act == "blow":
                call expression Girls[0].Tag + "_BJ_Prep" #call R_BJ_Prep
        elif Act == "tit":
                call expression Girls[0].Tag + "_TJ_Prep" #call R_TJ_Prep
        elif Act == "hand":
                call expression Girls[0].Tag + "_HJ_Prep" #call R_HJ_Prep
        elif Act == "hotdog":
                call expression Girls[0].Tag + "_HotdogPrep" #call R_HotdogPrep
        elif Act == "suck breasts":
                call expression Girls[0].Tag + "_SB_Prep" #call R_SB_Prep
        elif Act == "fondle breasts":
                call expression Girls[0].Tag + "_FB_Prep" #call R_FB_Prep
        elif Act == "insert ass" or Act == "lick ass":
                call expression Girls[0].Tag + "_IA_Prep" #call R_IA_Prep
        else: #Act == "kiss you"
                call KissPrep(Girls[0]) #call R_KissPrep
        return

label Quick_Sex(Girl=Ch_Focus,Act=0): #rkeljsv
        # called by Chitchat if a girl is horny

        $ Girl.FaceChange("sly",1)
        $ Girl.AddWord(1,"quicksex","quicksex")
        menu:
            extend ""
            "Sure":
                    $ Girl.Statup("Love", 95, 4)
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Inbt", 70, 2)
                    $ Girl.Statup("Inbt", 90, 3)
            "No thanks":
                    $ Line = 0
                    $ Girl.Statup("Love", 80, -2)
                    if (2*Girl.Obed) >= (Girl.Love + Girl.Inbt + (5*Girl.Thirst)):
                            #she's more obedient than horny
                            $ Girl.FaceChange("sadside",1)
                            $ Girl.Statup("Obed", 90, 7)
                            if Girl == RogueX:
                                    ch_r "Ok, fine. . ."
                            elif Girl == KittyX:
                                    ch_k "Fine, whatever. . ."
                            elif Girl == EmmaX:
                                    ch_e "I can accept this. . ."
                            elif Girl == LauraX:
                                    ch_l "Ok. . ."
                            elif Girl == JeanX:
                                    ch_j ". . . Ok. . ."
                            elif Girl == StormX:
                                    ch_s "Very well. . ."
                            elif Girl == JubesX:
                                    ch_v "What-ever. . ."
                            menu:
                                "Wait, on second thought. . .":
                                        $ Girl.Statup("Love", 80, -2)
                                        $ Girl.Statup("Obed", 80, -8)
                                        $ Line = "ask"
                                ". . . [[say nothing, still no].":
                                        pass
                    elif (ApprovalCheck(Girl, 600, "I") and Girl.Thirst >= 30) or Girl.Thirst >= 50:
                                        #she's pretty horny
                                        $ Girl.FaceChange("confused",1,Eyes="surprised")
                                        $ Girl.Statup("Love", 80, -1)
                                        $ Girl.Statup("Obed", 70, 4)
                                        $ Girl.Statup("Inbt", 60, 5)
                                        $ Girl.Statup("Inbt", 90, 3)
                                        if Girl == RogueX:
                                                ch_r "You're sure about that?"
                                        elif Girl == KittyX:
                                                ch_k "Seriously"
                                        elif Girl == EmmaX:
                                                ch_e "Have you thought this through?"
                                        elif Girl == LauraX:
                                                ch_l "Seriously, free sex here."
                                        elif Girl == JeanX:
                                                ch_j "Seriously? . ."
                                        elif Girl == StormX:
                                                ch_s "Are you quite sure? . ."
                                        elif Girl == JubesX:
                                                ch_v "I can make it worth your while. . ."
                                        $ Line = "ask"
                    #above stack falls through to here.
                    if Line == "ask":
                            $ Line = 0
                            $ Count = 2
                            $ Cnt = 0
                            while Count:
                                    #loops at least twice, more if she starts begging
                                    $ Count -= 1
                                    menu:
                                        extend ""
                                        "Ok, fine.":
                                                $ Act = 1
                                                $ Count = 0
                                                $ Girl.FaceChange("sly",1)
                                                $ Girl.Statup("Love", 80, 2)
                                                $ Girl.Statup("Love", 95, 3)
                                                $ Girl.Statup("Obed", 70, 2)
                                                $ Girl.Statup("Inbt", 90, 3)

                                        "Beg me." if Cnt < 100:
                                                $ Girl.Statup("Obed", 80, 2)
                                                $ Line = "beg"
                                        "Beg me again." if Cnt >= 100:
                                                $ Girl.Statup("Obed", 90, 2)
                                                $ Line = "beg"

                                        "Only if I get to choose.":
                                                $ Girl.FaceChange("smile",1,Brows="confused")
                                                $ Girl.Statup("Love", 90, 2)
                                                $ Girl.Statup("Obed", 80, 3)
                                                $ Girl.Statup("Obed", 95, 3)
                                                $ Girl.Statup("Inbt", 85, 2)
                                                if Girl == RogueX:
                                                        ch_r "Ok, fine."
                                                elif Girl == KittyX:
                                                        ch_k "Yeah, whatever."
                                                elif Girl == EmmaX:
                                                        ch_e "I suppose."
                                                elif Girl == LauraX:
                                                        ch_l "Fair."
                                                elif Girl == JeanX:
                                                        ch_j "Ok, whatever. . ."
                                                elif Girl == StormX:
                                                        ch_s "That can be arranged. . ."
                                                elif Girl == JubesX:
                                                        ch_v "Hmmm. ok. . ."
                                                call expression Girl.Tag + "_SexMenu"
                                                return

                                        "Still no.":
                                                $ Girl.Statup("Love", 85, -2)
                                                $ Girl.Statup("Obed", 90, 3)
                                                if ApprovalCheck(Girl, 1500+(5*Cnt)-(10*Girl.Thirst), "LI"):
                                                            #if she's obedient, or her horniness is higher than her Inhibition
                                                            $ Line = "beg"
                                                elif not Cnt and Count:
                                                            #if you've never refused before
                                                            $ Girl.Uptop = 1 #Uptop up
                                                            pause 1
                                                            call expression Girl.Tag + "_First_Topless" pass (1)
                                                            $ Girl.Uptop = 0 #Uptop up
                                                            $ Girl.FaceChange("confused",1,Mouth="smile")
                                                            $ Girl.Statup("Inbt", 70, 3)
                                                            $ Girl.Statup("Inbt", 95, 3)
                                                            if Girl == RogueX:
                                                                    ch_r "You -really- sure about that?"
                                                            elif Girl == KittyX:
                                                                    ch_k "Reaaaaally?"
                                                            elif Girl == EmmaX:
                                                                    ch_e "-No- second thoughts, [Girl.Petname]?"
                                                            elif Girl == LauraX:
                                                                    ch_l "I mean, come on."
                                                            elif Girl == JeanX:
                                                                    ch_j "You -know- you want it. . ."
                                                            elif Girl == StormX:
                                                                    ch_s "Are you -that- sure of yourself?"
                                                            elif Girl == JubesX:
                                                                    ch_v "Bummer. . ."
                                                            $ Cnt += 25
                                    if Line == "beg":
                                            if ApprovalCheck(Girl, 600+Cnt, "O") or ApprovalCheck(Girl, 1500+(5*Cnt)-(10*Girl.Thirst)):
                                                    #if she's obedient, or her horniness is higher than her Inhibition
                                                    if Cnt < 50:
                                                            #first time
                                                            $ Girl.FaceChange("sad",2)
                                                            $ Girl.Statup("Love", 90, -2)
                                                            $ Girl.Statup("Obed", 50, 5)
                                                            $ Girl.Statup("Obed", 95, 3)
                                                            $ Girl.Statup("Inbt", 90, 3)
                                                            if Girl == RogueX:
                                                                    ch_r "Please?"
                                                            elif Girl == KittyX:
                                                                    ch_k "Pretty please?"
                                                            elif Girl == EmmaX:
                                                                    ch_e ". . ."
                                                                    $ Girl.Statup("Love", 90, -2)
                                                                    $ Girl.Statup("Obed", 200, 3)
                                                                    ch_e ". . .Please?"
                                                            elif Girl == LauraX:
                                                                    ch_l "Um. . . Please?"
                                                            elif Girl == JeanX:
                                                                    ch_j "Huh. . ."
                                                                    $ Girl.Statup("Obed", 90, 3)
                                                                    ch_j "Ok. . . please? . ."
                                                            elif Girl == StormX:
                                                                    ch_s "No? You're that certain?"
                                                            elif Girl == JubesX:
                                                                    ch_v "Ya'sure?"
                                                    else:
                                                            #second time
                                                            $ Girl.FaceChange("sad",2,Eyes="surprised")
                                                            $ Girl.Statup("Love", 90, -4)
                                                            $ Girl.Statup("Obed", 70, 6)
                                                            $ Girl.Statup("Obed", 200, 3)
                                                            $ Girl.Statup("Inbt", 90, 5)
                                                            if Girl == RogueX:
                                                                    ch_r "Come on, I really need it. . ."
                                                            elif Girl == KittyX:
                                                                    ch_k "I need you, [Girl.Petname]!"
                                                            elif Girl == EmmaX:
                                                                    $ Girl.Statup("Love", 90, -2)
                                                                    $ Girl.Statup("Obed", 200, 1)
                                                                    ch_e "I. . . really need you here, [Girl.Petname]. . ."
                                                            elif Girl == LauraX:
                                                                    $ Girl.Statup("Obed", 80, 1)
                                                                    ch_l "I've got a fevah, and the only prescription is your dick. . ."
                                                            elif Girl == JeanX:
                                                                    ch_j "I. . ."
                                                                    ch_j "Come on, man. . ."
                                                                    $ Girl.Statup("Obed", 90, 5)
                                                                    ch_j "Please?"
                                                            elif Girl == StormX:
                                                                    ch_s ". . ."
                                                            elif Girl == JubesX:
                                                                    ch_v "Pretty Please?"
                                                    $ Count = 1 if Count <= 0 else Count #allows it to cycle one more time
                                                    $ Cnt += 100
                                            elif Cnt > 50:
                                                            #she refuses on second time
                                                            $ Girl.FaceChange("angry",1)
                                                            $ Girl.Statup("Love", 70, -3)
                                                            $ Girl.Statup("Love", 85, -5)
                                                            $ Girl.Statup("Obed", 80, -2)
                                                            $ Girl.Statup("Inbt", 90, 4)
                                                            if Girl == RogueX:
                                                                    ch_r "I'm not going to beg again."
                                                            elif Girl == KittyX:
                                                                    ch_k "Not even!"
                                                            elif Girl == EmmaX:
                                                                    $ Girl.Statup("Love", 90, -3)
                                                                    $ Girl.Statup("Obed", 70, -3)
                                                                    $ Girl.Statup("Obed", 200, 2)
                                                                    ch_e "I. . . Once was too much!"
                                                            elif Girl == LauraX:
                                                                    ch_l "Ooooh, you are pushing it, [Player.Name]."
                                                            elif Girl == JeanX:
                                                                    $ Girl.Statup("Obed", 90, 4)
                                                                    ch_j "Whatever. . ."
                                                            elif Girl == StormX:
                                                                    ch_s "So be it."
                                                            elif Girl == JubesX:
                                                                    ch_v "Boooo."
                                            else:
                                                            #she refuses
                                                            $ Girl.FaceChange("sad",2,Brows="confused")
                                                            $ Girl.Statup("Love", 95, -2)
                                                            $ Girl.Statup("Obed", 50, -2)
                                                            $ Girl.Statup("Obed", 90, -2)
                                                            $ Girl.Statup("Inbt", 90, 5)
                                                            if Girl == RogueX:
                                                                    ch_r "I'm not going to beg."
                                                            elif Girl == KittyX:
                                                                    ch_k "That's. . . rude."
                                                            elif Girl == EmmaX:
                                                                    $ Girl.Statup("Obed", 70, -2)
                                                                    ch_e "That is so beneath me."
                                                            elif Girl == LauraX:
                                                                    ch_l "Not worth it. ."
                                                            elif Girl == JeanX:
                                                                    $ Girl.Statup("Obed", 90, 4)
                                                                    ch_j "Yeah, not worth it. . ."
                                                            elif Girl == StormX:
                                                                    ch_s "So be it."
                                                            elif Girl == JubesX:
                                                                    ch_v "Booo."
                                    #end of "beg" chain
                            #end of loop, if not Act, return disappointed
                    $ Line = 0
                    if not Act:
                            #she accepts your refusal
                            $ Girl.Statup("Love", 80, -2)
                            if Girl == RogueX:
                                    ch_r "Ok, your loss, I guess. . ."
                            elif Girl == KittyX:
                                    ch_k "Too bad . ."
                            elif Girl == EmmaX:
                                    ch_e "Fine. . . I'll handle my own arrangements. . ."
                            elif Girl == LauraX:
                                    ch_l "Your loss. . ."
                            elif Girl == JeanX:
                                    ch_j "Your loss. . ."
                            elif Girl == StormX:
                                    ch_s "Well, your loss then. . ."
                            elif Girl == JubesX:
                                    ch_v "Lame."
                            return

        call Favorite_Actions(Girl,1) #returns a string of the action
        $ Act = _return

        if Act in ("anal","sex","blow","tit","hand","hotdog"):
                # if cock needs to be out. . .
                "[Girl.Name] reaches down and unzips your fly. . ."
                if not Player.Semen:
                    "You wish you weren't already drained. . . you stop her hands."
                    ch_p "I could actually use a break right now. . "
                    $ Act = "fondle breasts"
                else:
                    call Seen_First_Peen(Girl,Partner,1)

        $ Situation = Girl

        # launches the appropriate scene based on the sex act in question.
        if Act == "anal":
                call expression Girl.Tag + "_AnalPrep" #call R_AnalPrep
        elif Act == "sex":
                call expression Girl.Tag + "_SexPrep" #call R_SexPrep
        elif Act ==  "lick pussy":
                call expression Girl.Tag + "_LP_Prep" #call R_LPlayer.Prep
        elif Act == "fondle pussy":
                call expression Girl.Tag + "_FP_Prep" #call R_FPlayer.Prep
        elif Act == "blow":
                call expression Girl.Tag + "_BJ_Prep" #call R_BJ_Prep
        elif Act == "tit":
                call expression Girl.Tag + "_TJ_Prep" #call R_TJ_Prep
        elif Act == "hand":
                call expression Girl.Tag + "_HJ_Prep" #call R_HJ_Prep
        elif Act == "hotdog":
                call expression Girl.Tag + "_HotdogPrep" #call R_HotdogPrep
        elif Act == "suck breasts":
                call expression Girl.Tag + "_SB_Prep" #call R_SB_Prep
        elif Act == "fondle breasts":
                call expression Girl.Tag + "_FB_Prep" #call R_FB_Prep
        elif Act == "insert ass" or Act == "lick ass":
                call expression Girl.Tag + "_IA_Prep" #call R_IA_Prep
        else: #Act == "kiss you"
                call KissPrep(Girl) #call R_KissPrep
        return

label Escalation(Girl=0): #rkeljsv
        #call Escalation("Rogue","R")
        # raises the level of the sexual activity if the girl would like that.
        if Cnt < 10 or ThreeCount <= Round or Girl.Forced:
                #if things just started, or you recently made a change, return
                return

        $ Situation = Girl

        if Trigger == "fondle breast" and ApprovalCheck(Girl,1050,TabM=4,Alt=[[JeanX],800]) and Girl.Lust >= 30 and Girl.SuckB:
                    #if you're fondling her breasts, she has over 30 Lust, and she's had her breasts sucked before. . .
                    if Trigger2 == "suck breasts":
                            $ Trigger2 = 0
                    $ Girl.Statup("Inbt", 80, 2)
                    call expression Girl.Tag + "_SB_Prep" #call Rogue_SB_Prep
                    if "suck breasts" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger == "fondle thighs" and ApprovalCheck(Girl,1050,TabM=4,Alt=[[JeanX],800]) and Girl.Lust >= 30 and Girl.FondleP:
                    #if you're fondling her thighs, she has over 30 Lust, and she's had her pussy fondled before. . .
                    if Trigger2 == "fondle thighs":
                            $ Trigger2 = 0
                    $ Girl.Statup("Inbt", 80, 4)
                    call expression Girl.Tag + "_FP_Prep" #call Rogue_FPlayer.Prep
                    if "fondle pussy" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif not Player.Semen:
                    #can't do the rest if you're tapped out
                    pass
        elif Trigger == "handjob" and ApprovalCheck(Girl,1200,TabM=4) and Girl.Lust >= 30 and Girl.Blow:
                    #if she's giving a handy, she has over 30 Lust, and she's sucked cock before. . .
                    $ Girl.Statup("Inbt", 80, 3)
                    call expression Girl.Tag + "_BJ_Prep" #call Rogue_BJ_Prep
                    if "blow" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger not in ("sex","anal") and ApprovalCheck(Girl,1400,TabM=5,Alt=[[JeanX],1200]) and Girl.Lust >= 60 and Girl.Sex >= 3:
                    #if you're not having sex, she has over 60 Lust, and she's had sex before. . .
                    $ Girl.Statup("Inbt", 80, 4)
                    call expression Girl.Tag + "_SexPrep" #call Rogue_SexPrep
                    if "sex" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()
        elif Trigger != "anal" and ApprovalCheck(Girl,1400,TabM=5,Alt=[[JeanX],1200]) and Girl.Lust >= 70 and Girl.Anal >= 5:
                    #if you're not having anal, she has over 70 Lust, and she's had anal before. . .
                    $ Girl.Statup("Inbt", 80, 5)
                    call expression Girl.Tag + "_AnalPrep" #call Rogue_AnalPrep
                    if "anal" in Girl.RecentActions:
                            # If you went through with it, drop one phase back when returning to this point
                            $ renpy.pop_call()

        #if it falls through the options
        $ ThreeCount = 0
        $ Situation = 0
        return

label Sex_Dialog(Primary=Ch_Focus,Secondary=0,TempFocus=0,PrimaryLust=0,SecondaryLust=0,Line1=0,Line2=0,Line3=0,Line4=0,D20S=0):  #rkeljsv
        # call Sex_Dialog(RogueX,Partner)
        # Primary is main female, secondary is supporting female, action is what they are doing.

        # If the seed is 0-5, only offhands will play. If it's 15-20, only trigger3's will play. If it's 5-10, offhand and Secondaries will play.
        # If it's 10-15 all things will play.

        $ D20S = renpy.random.randint(1, 20) if not D20S else D20S
        $ Line = 0

        # Checks for Taboo, and if it passes through, calls the first sex dialog
        call Girls_Taboo(Primary)
        if not Trigger:
                return

        $ Secondary = Partner

        call Primary_SexDialog
        $ Line1 = Line #Set Line1 to the current state of the Line variable
        #End Primary Dialog

        #Trigger 2
        if Trigger2 and D20S <= 15:
                    # If there is a player offhand Trigger set and the random value is 1-15, add an Offhand dialog
                    $ Line = ""
                    call Offhand_Dialog
                    $ Line1 = Line1 + Line
        #End Offhand

        #Trigger 3
        if D20S >= 7 and Trigger not in ("masturbation", "lesbian"):
                    # If there is a Primary offhand Trigger set and the random value is 1-10, add a self-directed dialog
                    $ Line = 0
                    call Girl_Self_Lines(Primary,"T3",Trigger3,D20X=D20S)
                    if Line:
                            $ Line3 = Line + "."
        #End Primary girl offhand

        #Trigger 4
        if Secondary and (not Trigger4 or 7 <= D20S <= 17 or Trigger4 == "watch"):
                    # If there is a Secondary character and the random value is 5-15, add a threeway dialog
                    $ Line = 0
                    call SexDialog_Threeway
                    if Line:
                            $ Line4 = Line + "."
        #End Secondary Dialog

        #Applying player's satisfaction
        $ Player.Statup("Focus", 200, TempFocus)

        #Applying primary girl's satisfaction
        $ Primary.Statup("Lust", 200, PrimaryLust)
        $ Primary.LustFace()

        #Applying secondary girl's satisfaction
        if Secondary:
                $ SecondaryLust += (int(PrimaryLust/10)) if Secondary.GirlLikeCheck(Primary) >= 700 else 0
                $ Secondary.Statup("Lust", 200, SecondaryLust)
                $ Secondary.LustFace()

        # Dialog begins to play out. . .
        "[Line1]"
        if Line3:
                #If there's a secondary line, play it
                call Seen_First_Peen(Primary,Secondary,Passive=3)
                "[Line3]"
        if Line4:
                #add call to First Les here."
                #If there's a third person line, play it
                call Seen_First_Peen(Primary,Secondary,Passive=4)
                "[Line4]"
                if Trigger4 == "suck breasts" or Trigger4 == "fondle breasts":
                    #if breastplay is involved. . .
                    if ApprovalCheck(Primary,500,"I",TabM=2) and Primary.Lust >= 50 and (Primary.ChestNum() > 1 or Primary.OverNum() > 1):
                            # if the girl is horny and her top is on. . .
                            $ Primary.Uptop = 1
                            "[Primary.Name] seems frustrated and pulls her top open."

        call Activity_Check(Primary,Secondary,0)
        if not _return:
                #sees if girl is cool with what's happening, if not, removes her.
                if Primary.Forced:
                        #if you're coercing her, it just reverts to the previous tier
                        #$ renpy.pop_call() #negates call to Sex Dialog
                        return
                if Secondary and Secondary.Loc == bg_current:
                        #if the first girl leaves, but there is another,
                        $ Trigger = Secondary
                        $ Partner = 0
                        $ Trigger4 = 0
                        $ Trigger5 = 0
                        #$ renpy.pop_call() #negates call to Sex Dialog
                        #$ renpy.pop_call() #negates call to sexaction in progress
                        #$ renpy.pop_call() #negates call to sex menu
                else:
                        call Trig_Reset
                jump Misplaced   #moved out of previous column

        call Dirty_Talk

        return

label Trig_Reset(Visual=0):
        # Resets all triggers, and sprites if Visual
        $ Trigger = 0
        $ Trigger2 = 0
        $ Trigger3 = 0
        $ Trigger4 = 0
        $ Trigger5 = 0
        $ Situation = 0
        if Visual:
                call AllReset
        return

label Trigger_Swap(Active = 0, TriggerX1 = Trigger, TriggerX3 = Trigger3, Primary = Partner): #rkeljsv
    #this would switch primary character triggers over to secondary characters.
    # call Trigger_Swap("Rogue")
    # TriggerX1 and TriggerX3 store the primary girl's actions
    # Active is the old lead girl
    # Primary is the new lead girl

    $ Trigger2 = 0 if Trigger2 != "jackin" else Trigger2
    $ temp_modifier = 0

    if Trigger4:
            #if the second girl is already doing something
            if Trigger4 == "masturbation":
                    $ Trigger = "masturbation"
                    $ Trigger3 = Trigger5
                    $ Trigger4 = 0
                    #"hand","fondle breasts","suck breasts","fondle pussy","dildo pussy",
                    #"vibrator pussy","fondle ass","dildo anal"
            elif TriggerX1 == "lesbian":
                    $ Trigger = "lesbian"
                    $ Trigger3 = Trigger4
                    $ Trigger4 = 0
            elif Trigger4 in ("hand","blow","kiss you"):
                    $ Trigger = Trigger4
                    $ Trigger3 = 0
                    $ Trigger4 = 0
            else:
                    $ Trigger = 0
                    $ Trigger3 = 0
                    $ Trigger4 = 0
                    #"fondle breasts","suck breasts","fondle pussy","lick pussy",
                    #"fondle ass","lick ass",
    else:
                    #if the second girl is not already doing anything
                    $ Trigger = 0
                    $ Trigger3 = 0

    call Shift_Focus(Primary)
    if not Active:
            #if no girl is sent to this system, cycle active girls and place any locals into the Partner role
            $ BO = ActiveGirls[:]
            $ BO.remove(Primary) if Primary in BO else BO
            while BO:
                    if BO[0].Loc == bg_current:
                            $ Partner = BO[0]
                            $ BO = [1]
                    $ BO.remove(BO[0])
    else:
                    $ Partner = Active

    #if the primary girl was doing something
    if TriggerX1 == "masturbation":
                $ Trigger4 = "masturbation"
                $ Trigger5 = TriggerX3
                #"hand","fondle breasts","suck breasts","fondle pussy","dildo pussy",
                #"vibrator pussy","fondle ass","dildo anal"
    elif TriggerX1 == "lesbian":
                $ Trigger4 = TriggerX3
    else:
            if TriggerX1 in ("hand","blow","kiss you"):
                $ Trigger4 = TriggerX1
                $ Trigger5 = 0
            else:
                $ Trigger4 = "masturbation"
                if TriggerX1 in ("fondle thighs","fondle ass","insert ass","lick ass"):
                        $ Trigger5 = "fondle ass"
                        "You pull back from [Partner.Name]."
                elif TriggerX1 in ("dildo pussy","dildo anal"):
                        $ Trigger5 = TriggerX1
                        "You pull back from [Partner.Name]."
                elif TriggerX1 in ("titjob","hotdog","fondle breasts","suck breasts"):
                        $ Trigger5 = "fondle breasts"
                        "You pull back from [Partner.Name]."
                elif TriggerX1 in ("fondle pussy","lick pussy"):
                        $ Trigger5 = "fondle pussy"
                        "You pull back from [Partner.Name]."
                elif TriggerX1 == "sex":
                        $ Trigger5 = "fondle pussy"
                        "You pull out of [Partner.Name] and shift your attention to [Primary.Name]."
                elif TriggerX1 == "anal":
                        $ Trigger5 = "fondle ass"
                        "You pull out of [Partner.Name] and shift your attention to [Primary.Name]."
                else:
                        $ Trigger5 = 0
    call AllReset(Partner)

    if not Trigger:
            if Primary == RogueX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Rogue_SMenu
            if Primary == KittyX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Kitty_SMenu
            if Primary == EmmaX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Emma_SMenu
            if Primary == LauraX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Laura_SMenu
            if Primary == JeanX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Jean_SMenu
            if Primary == StormX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Storm_SMenu
            if Primary == JubesX:
                    $ renpy.pop_call() #causes it to skip past the cycle you were in before
                    $ renpy.pop_call() #causes it to skip past the sex menu you were in before that
                    jump Jubes_SMenu
    else:
                    call Set_The_Scene(Dress = 0, TrigReset = 0, Quiet=1)
                    call expression Primary.Tag + "_SexAct" pass ("SkipTo") #call Kitty_SexAct("SkipTo")
    return

label Seen_First_Peen(Primary=0, Secondary=0, Silent=0, Undress=0, Passive=0, GirlsNum=0, React=0, BOptions=[]):
    # call Seen_First_Peen(Primary,Secondary,Silent,Undress)
    # Primary is the first girl, Secondary the second, if there is one
    # _return will be 0 if other girl didn't comment,
    # 1 = if the other girl commented, 2 = didn't like it
    # Girlsnum will pass Second to the next girl, and keep track of whether anyone acted
    # Passive will be 3 or 4 if linked to Sex dialog acts 3 or 4
    if not Primary:
            #if this is not during a sex act
            $ BOptions = Present[:]  #loads up all local girls
            $ renpy.random.shuffle(BOptions)
            while BOptions:
                    #cycles through each girl possible,
                    #If girl is around, check to see if she noticed your cock yet
                    if (Ch_Focus == BOptions[0] or D20 >= 10) and "peen" not in BOptions[0].RecentActions:
                            #If BOptions[0] is the prinary or secondary character, and hasn't seen your cock yet, call the thing
                            #call expression BOptions[0].Tag + "_First_Peen" pass (Silent,Undress)
                            call Girl_First_Peen(BOptions[0],Silent,Undress)
                            $ GirlsNum = _return
                    $ BOptions.remove(BOptions[0])

            if not GirlsNum:
                #if no girls are present
                if "naked" not in Player.RecentActions and Undress:
                        "You strip nude."
                        $ Player.AddWord(1,"naked",0,0,0)
                elif "cockout" in Player.RecentActions:
                        return
                else:
                        "You whip your cock out."
                $ Player.AddWord(1,"cockout",0,0,0)
    #end if not during a sex act
    else:
            #It's during a sex act
            if Passive:
                    #if in Passive mode, during sex dialog, it only activates if cock is already out.
                    if Approval == Passive and "cockout" not in Player.RecentActions:
                        #if both are 3 or both are 4, meaning the activities matched up,
                        call CockOut
                    if "cockout" not in Player.RecentActions:
                        return

            #call expression Primary.Tag + "_First_Peen" pass (Silent,Undress,React=React)
            call Girl_First_Peen(Primary,Silent,Undress,React=React)

            if Secondary:
                    #call expression Secondary.Tag + "_First_Peen" pass (Silent,Undress,Second = _return)
                    call Girl_First_Peen(Secondary,Silent,Undress,Second = _return)
    return

label CockOut:
        # Passive and therefore Approval will be 3 or 4 if linked to Sex dialog acts 3 or 4
        if Approval == 3:
                    #if attached to line 3, use the Primary girl
                    #call expression Primary.Tag + "_First_Peen" pass (React=1)
                    call Girl_First_Peen(Primary,React=1)
        elif Approval == 4:
                    #if attached to line 4, use the Secondary girl
                    #call expression Secondary.Tag + "_First_Peen" pass (React=1)
                    call Girl_First_Peen(Secondary,React=1)
        $ Approval = 0
        return

label Get_Dressed: #checked each time she sees your cock
        #if no girls are present
        if "naked" in Player.RecentActions:
                "You get dressed."
                $ Player.DrainWord("naked")
                $ Player.DrainWord("cockout")
        elif "cockout" in Player.RecentActions:
                "You put your cock away."
                $ Player.DrainWord("cockout")
        return

label Girls_Noticed(Girl=Primary,Other=0,Silent=0,B=0,BO=[]): #rkeljsv
        # Called by Sex_Dialog or Girls_Taboo
        # Girl is lead girl, Other is a girl who notices you
        # if Silent, no dialog plays, B is a carried bonus value.
        if not Girl or Girl not in TotalGirls:
                        "Tell Oni that in noticed, no primary is set."
                        return
        $ BO = TotalGirls[:]
        $ BO.remove(Girl)
        while BO:
                if BO[0].Loc == bg_current and BO[0] != Girl:
                        # if there is a girl who is not primary, but is in the location
                        # set her as the one being noticed by the primary girl
                        $ Other = BO[0]
                        $ BO = [1]
                $ BO.remove(BO[0])
        if Other not in TotalGirls or Other == Girl:
                return
        if "threesome" in Other.RecentActions:
                return
        if Partner == Other and "noticed " + Girl.Tag in Other.RecentActions:
                return

        if not Silent:
            if Partner != Other:
                    #if there has been no connection yet. . .
                    $ Other.FaceChange("surprised", 1)
                    "[Other.Name] noticed what you and [Girl.Name] are up to."
            else:
                    #if there has been some noticing already. . .
                    $ Other.FaceChange("sly", 1)
                    if Other == KittyX:
                            "[Other.Name] is glancing at you and [Girl.Name] carefully. . ."
                    elif Other == EmmaX:
                            "[Other.Name] is carefully appraising you and [Girl.Name]. . ."
                    else:
                            "[Other.Name] is staring at you and [Girl.Name]. . ."

        if "cockout" in Player.RecentActions:
                    #call Girl_First_Peen(Other)
                    call Seen_First_Peen(Other,Girl)

        $ Girl.RecentActions.append("noticed " + Other.Tag)
        $ Other.RecentActions.append("noticed " + Girl.Tag)
        if Other == EmmaX and ("three" not in EmmaX.History or "classcaught" not in EmmaX.History):
                    #Emma-specific code
                    $ Other.AddWord(1,0,0,"saw with " + Girl.Tag) #adds to Traits.
                    if bg_current == EmmaX.Home:
                            #if you're in her room. . .
                            ch_e "If the two of you cannot keep your hands off each other, please do so elsewhere. . ."
                            "She shoves the two of you out of her room and slams the door."
                            $ Girl.Loc = "bg player"
                            jump Misplaced
                    call Remove_Girl(EmmaX)
                    if not Silent:
                            "She seems uncomfortable with the situation and leaves the room."
                            "Perhaps you should ask her about it later."
                    return

        if "poly " + Girl.Tag in Other.Traits or (Girl in Player.Harem and Other in Player.Harem):
                #if they already have a relationship. . .
                $ B = (1000-(20*Taboo))
        else:
                #if they don't have a relationship. . .
                $ B = (Other.GirlLikeCheck(Girl) - 500) #RogueX.LikeLaura - 500
                if Other in Player.Harem:
                        #if you and the other girl have a relationship. . .
                        $ B -= 200

        $ Other.sprite_location = StageFarRight
        call Display_Girl(Other,0,0)
        if Partner == Other:
                #if this is already a Partner, skip this dialog
                $ Silent = 1
        $ Partner = Other
        $ Line = 0
        if ApprovalCheck(Other, 2000, TabM=2, Bonus = B) or ApprovalCheck(Other, 950, "L", TabM=2, Bonus = (B/3)):
                    #if she's very loose or really likes you
                    $ Other.FaceChange("sexy", 1)
                    if not Silent:
                            "She decides to join you."
                    $ Other.Statup("Obed", 90, 5)
                    $ Other.Statup("Inbt", 90, 5)
                    $ Other.Statup("Lust", 90, 3)
                    $ Other.AddWord(1,0,0,"poly " + Girl.Tag)
                    call Threeway_Set(Other,Mode="start",GirlB=Girl)
        elif ApprovalCheck(Other, 650, "O", TabM=2) and ApprovalCheck(Other, 450, "L", TabM=1) or ApprovalCheck(Other, 800, "O", TabM=2, Bonus = (B/3)):
                    #if she likes you, but is very obedient
                    $ Other.FaceChange("sexy")
                    if not Silent:
                            "She sits down patiently off to the side and watches."
                    $ Other.Statup("Love", 90, 5)
                    $ Other.Statup("Inbt", 90, 5)
                    $ Other.Statup("Lust", 90, 2)
                    $ Other.AddWord(1,0,0,"poly " + Girl.Tag)
                    call Threeway_Set(Other,"watch",Mode="start",GirlB=Girl)
        elif ApprovalCheck(Other, 650, "I", TabM=2) and ApprovalCheck(Other, 450, "L", TabM=1) or ApprovalCheck(Other, 800, "I", TabM=2, Bonus = (B/3)):
                    #if she likes you, but is very uninhibited
                    $ Other.FaceChange("sexy")
                    if not Silent:
                            "She sits down and watches you with a hungry look."
                    $ Other.Statup("Love", 90, 5)
                    $ Other.Statup("Obed", 90, 2)
                    $ Other.Statup("Inbt", 90, 2)
                    $ Other.Statup("Lust", 90, 5)
                    $ Other.AddWord(1,0,0,"poly " + Girl.Tag)
                    call Threeway_Set(Other,"watch",Mode="start",GirlB=Girl)
        elif ApprovalCheck(Other, 1500, TabM=2, Bonus = B):
                    $ Other.FaceChange("perplexed", 1)
                    if not Silent:
                            "She looks a little confused at what's happening, but she stays put and watches."
                    if Other.Love >= Other.Obed and Other.Love >= Other.Inbt:
                        $ Other.Statup("Obed", 90, 2)
                        $ Other.Statup("Inbt", 90, 2)
                    elif Other.Obed >= Other.Inbt:
                        $ Other.Statup("Love", 90, 2)
                        $ Other.Statup("Inbt", 90, 2)
                    else:
                        $ Other.Statup("Love", 90, 2)
                        $ Other.Statup("Obed", 90, 1)
                        $ Other.Statup("Inbt", 90, 1)
                    $ Other.Statup("Lust", 90, 5)
                    call Threeway_Set(Other,"watch",Mode="start",GirlB=Girl)
        elif ApprovalCheck(Other, 650, "L", TabM=1) or ApprovalCheck(Other, 400, "O", TabM=2):
                    #if she likes you or is obedient, but not enough
                    $ Other.FaceChange("angry", 2)
                    if bg_current == Other.Home:
                            if Other in (LauraX,JeanX):
                                "She looks annoyed, and kicks you both out of the room."
                            else:
                                "She looks betrayed, and kicks you both out of the room."
                    else:
                            if Other in (LauraX,JeanX):
                                "She looks annoyed, and storms out of the room."
                            else:
                                "She looks betrayed, and storms out of the room."
                    $ Other.Statup("Love", 200, -5)
                    $ Other.Statup("Love", 80, -5)
                    $ Other.Statup("Love", 70, -5)
                    $ Other.Statup("Obed", 90, -5)
                    $ Other.Statup("Lust", 89, 10)
                    $ Partner = 0
                    $ Other.AddWord(1,0,0,"saw with " + Girl.Tag)
                    if bg_current == Other.Home: #Kicks you out if in Rogue's room
                            $ Other.RecentActions.append("angry")
                            call GirlsAngry
                    call Remove_Girl(Other)
        else:
                    #if she doesn't like you much
                    $ Other.FaceChange("surprised", 2)
                    $ Other.Statup("Inbt", 90, 2)
                    $ Other.Statup("Lust", 40, 20)
                    if Trigger != "kiss you":
                            $ Other.Statup("Love", 90, -10)
                            $ Other.Statup("Obed", 90, -5)
                            $ Other.Statup("Lust", 80, 10)
                    if bg_current == Other.Home:
                            $ Other.Statup("Love", 90, -5)
                            $ Other.Statup("Obed", 90, -5)
                            if Other in (LauraX,JeanX):
                                    "She looks uncomfortable with this, and shoves you both out of the room."
                            else:
                                    "She looks embarrassed, and shoves you both out of the room."
                    elif Trigger != "kiss you":
                            if Other in (LauraX,JeanX):
                                    "She looks uncomfortable with this, and stalks out of the room."
                            else:
                                    "She looks embarrassed, and bolts from the room."
                    else:
                                    "She looks a bit disgusted and walks away."
                    $ Partner = 0
                    if bg_current == Other.Home: #Kicks you out if in Rogue's room
                            $ Other.RecentActions.append("angry")
                            call GirlsAngry
                    call Remove_Girl(Other)
        if AloneCheck(Girl) and Girl.Taboo == 20:
                #if the second girl ran away, it removes the taboo factor she added.
                $ Girl.Taboo = 0
                $ Taboo = 0
        if Line:
            # This plays a line from a threesome action, if there is one.
            "[Line]."
            $ Line = 0
        return

label CloseOut(Chr = Ch_Focus): #rkeljsv
        # This exits out of the current sex act, whichever it might be, then returns
        $ Chr = GirlCheck(Chr)
        if Trigger == "blow":
            call expression Chr.Tag + "_BJ_After"
        elif Trigger == "hand":
            call expression Chr.Tag + "_HJ_After"
        elif Trigger == "titjob":
            call expression Chr.Tag + "_TJ_After"
        elif Trigger == "kiss you":
            call Kiss_After
        elif Trigger == "fondle breasts":
            call expression Chr.Tag + "_FB_After"
        elif Trigger == "suck breasts":
            call expression Chr.Tag + "_SB_After"
        elif Trigger == "fondle thighs":
            call expression Chr.Tag + "_FT_After"
        elif Trigger == "fondle pussy":
            call expression Chr.Tag + "_FP_After"
        elif Trigger == "lick pussy":
            call expression Chr.Tag + "_LP_After"
        elif Trigger == "fondle ass":
            call expression Chr.Tag + "_FA_After"
        elif Trigger == "insert ass":
            call expression Chr.Tag + "_IA_After"
        elif Trigger == "lick ass":
            call expression Chr.Tag + "_LA_After"
        elif Trigger == "sex":
            call expression Chr.Tag + "_SexAfter"
        elif Trigger == "hotdog":
            call expression Chr.Tag + "_HotdogAfter"
        elif Trigger == "anal":
            call expression Chr.Tag + "_AnalAfter"
        elif Trigger == "dildo pussy":
            call expression Chr.Tag + "_DP_After"
        elif Trigger == "dildo anal":
            call expression Chr.Tag + "_DA_After"
        elif Trigger == "strip":
            call Group_Strip_End
        elif Trigger == "masturbation":
            $ Chr.Action -= 1
            $ Chr.Mast += 1
        elif Trigger == "lesbian":
            call Les_After
        else:
            "That's odd, tell Oni how you got here, Close [Chr.Name] [Trigger]."
        return

label Sex_Over(Clothes=1,Girls=0,BO=[]): #rkeljsv
        #this routine plays out at the end of any sex menu session
        #it cleans them up and puts their clothes on, only returning a line of dialog if they were undressed
        # call Sex_Over(1,Girl)
        $ Line = 0
        call Trig_Reset
        if Girls in TotalGirls:
                # in this case, "Girls" would be a single girl, ie RogueX
                $ BO = [Girls]
        else:
                $ BO = TotalGirls[:]
                $ renpy.random.shuffle(BO)
        while BO:
                if BO[0].Loc == bg_current:
                        # if this girl is present
                        $ BO[0].OCount = 0
                        call Girl_Cleanup(BO[0],"after")
                        if Player.Spunk:
                                if BO[0] == RogueX:
                                        ch_r "Let me take care of that for you. . ."
                                elif BO[0] == KittyX:
                                        ch_k "You've got a little something. . ."
                                        ch_k "just let me get that."
                                elif BO[0] == EmmaX:
                                        ch_e "[EmmaX.Petname], let's get you presentable. . ."
                                elif BO[0] == LauraX:
                                        ch_l "[LauraX.Petname], you've got a little something. . ."
                                elif BO[0] == JeanX:
                                        ch_j "[JeanX.Petname], you might want to clean up. . ."
                                elif BO[0] == StormX:
                                        ch_s "Allow me to take care of that, [StormX.Petname]. . ."
                                elif BO[0] == JubesX:
                                        ch_v "Oh, I can clean that up for you, [JubesX.Petname]. . ."
                                call Girl_CleanCock(BO[0])

                if "nowhammy" not in JeanX.Traits and "saw with Jean" in BO[0].Traits:
                                #if a girl saw you with Jean and got pissed, she forgets. . .
                                $ BO[0].Traits.remove("saw with Jean")
                                $ BO[0].Traits.append("sawJeanW") #got whammied tag
                $ BO.remove(BO[0])

        if Girls == Partner and Girls in TotalGirls:
                #swaps lead back to original
                call Shift_Focus(Girls)
        $ Girls = 0
        call AllReset("all") #resets all sex positions.

        if Clothes:
                #if asked to put their clothes back on.
                $ BO = TotalGirls[:]
                while BO:
                        if BO[0].Loc == bg_current:
                                if BO[0].OutfitChange(Changed=1) == 2:
                                        if Line:
                                            $ Line = Line + " and " + BO[0].Name
                                        else:
                                            $ Line = BO[0].Name
                                        $ Girls += 1
                        $ BO.remove(BO[0])
                if Girls > 1:
                    "[Line] throw their clothes back on."
                elif Girls:
                    "[Line] throws her clothes back on."
        call Get_Dressed
        call Checkout(1)
        return

label SkipTo(Chr = Ch_Focus): #rkeljsv
        # This jumps to the chosen sex act, called from the sex menu
        $ Chr = GirlCheck(Chr)
        if Trigger == "blow":
            call expression Chr.Tag + "_BJ_Cycle"
        elif Trigger == "hand":
            call expression Chr.Tag + "_HJ_Cycle"
        elif Trigger == "titjob":
            call expression Chr.Tag + "_TJ_Cycle"
        elif Trigger == "kiss you":
            call KissCycle(Chr)
        elif Trigger == "fondle breasts":
            call expression Chr.Tag + "_FB_Cycle"
        elif Trigger == "suck breasts":
            call expression Chr.Tag + "_SB_Cycle"
        elif Trigger == "fondle thighs":
            call expression Chr.Tag + "_FT_Cycle"
        elif Trigger == "fondle pussy":
            call expression Chr.Tag + "_FP_Cycle"
        elif Trigger == "lick pussy":
            call expression Chr.Tag + "_LP_Cycle"
        elif Trigger == "fondle ass":
            call expression Chr.Tag + "_FA_Cycle"
        elif Trigger == "insert ass":
            call expression Chr.Tag + "_IA_Cycle"
        elif Trigger == "lick ass":
            call expression Chr.Tag + "_LA_Cycle"
        elif Trigger == "sex":
            call expression Chr.Tag + "_SexCycle"
        elif Trigger == "hotdog":
            call expression Chr.Tag + "_HotdogCycle"
        elif Trigger == "anal":
            call expression Chr.Tag + "_AnalCycle"
        elif Trigger == "dildo pussy":
            call expression Chr.Tag + "_DP_Cycle"
        elif Trigger == "dildo anal":
            call expression Chr.Tag + "_DA_Cycle"
        elif Trigger == "strip":
            call Group_Strip_End
        elif Trigger == "masturbation":
            $ Chr.Action -= 1
            $ Chr.Mast += 1
        elif Trigger == "lesbian":
            call Les_Cycle(Chr)
        else:
            "That's odd, tell Oni how you got here, Close [Chr.Name] [Trigger]."
        return

label Clear_Stack:
    #this empties the call stack of stray items, and is called when the player goes to his room
    $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
    while StackDepth > 0:
        $ StackDepth -= 1
        $ renpy.pop_call()
    jump player_room

label Girl_TightsRipped(Girl=0,Count = 0):
        #Called if a girl's cloths get ripped
        if Girl not in TotalGirls:
                return
        if Girl.Hose == "tights":
                $ Count = 1
                $ Girl.Hose = "ripped tights"
                $ Girl.FaceChange("angry")
        elif Girl.Hose == "pantyhose":
                $ Count = 1
                $ Girl.Hose = "ripped pantyhose"
                $ Girl.FaceChange("angry")
        else:
                #if she wasn't wearing tights or hose
                return

        if "ripped tights" in Girl.Inventory or "ripped pantyhose" in Girl.Inventory:
            #if she'd already torn a pair
            if Girl == RogueX:
                    ch_r "Damnation, that's another pair ruined!"
            elif Girl == KittyX:
                    ch_k "Dammit! Not again!"
            elif Girl == EmmaX:
                    ch_e "Well, add another pair to my budget. . ."
            elif Girl == LauraX:
                    ch_l "I need to find stronger ones."
            elif Girl == JeanX:
                    ch_j "Well, who has a pair I could take. . ."
            elif Girl == StormX:
                    ch_s "I need to invest in more of these."

        else:
            $ Count = 2
            if Girl == RogueX:
                    ch_r "I hate getting a run in these things."
            elif Girl == KittyX:
                    ch_k "Ouch, I guess I missed a dodge. . ."
            elif Girl == EmmaX:
                    ch_e "Well that's unfortunate. . ."
            elif Girl == LauraX:
                    ch_l "What?"
                    ch_l ". . ."
                    $ Girl.Eyes = "down"
                    ch_l "Oh, they got torn."
                    $ Girl.Eyes = "normal"
            elif Girl == JeanX:
                    ch_j "Ugh, new ones will be a pain to find."
            elif Girl == StormX:
                    ch_s "It appears these are not fit for combat."

        if Count:
                #If they ripped
                if not Girl.Legs and Girl.Panties != "shorts":
                        if Girl == StormX and StormX in Rules:
                            #Storm don't care
                            pass
                        elif Girl.Panties:
                            if Girl.SeenPanties:
                                $ Count = 3 if not ApprovalCheck(Girl, 600) else Count
                            else:
                                $ Girl.SeenPanties = 1
                                $ Count = 3 if not ApprovalCheck(Girl, 900) else Count
                            $ Girl.Statup("Lust", 60, 2)
                        else:
                            if Girl.SeenPussy:
                                $ Count = 3 if not ApprovalCheck(Girl, 900) else Count
                            else:
                                call Rogue_First_Bottomless
                                $ Count = 3 if not ApprovalCheck(Girl, 1400) else Count

                if Count != 3:
                        $ Girl.AddWord(1,"ripped","ripped")

                if Count == 2:
                        #first time
                        menu:
                            extend ""
                            "I think those look really good on you.":
                                $ Girl.FaceChange("smile", 1)
                                $ Girl.Inventory.append(Girl.Hose)
                                if Girl == RogueX:
                                        ch_r "You think so? That's sweet, maybe I'll keep them on hand."
                                elif Girl == KittyX:
                                        ch_k "Oh, you think? I guess I could keep them."
                                elif Girl == EmmaX:
                                        ch_e "Oh, you enjoy the rugged look?"
                                elif Girl == LauraX:
                                        ch_l "I quess."
                                elif Girl == JeanX:
                                        ch_j "Oh, you like to see me roughed up?"
                                elif Girl == StormX:
                                        ch_s "I suppose so. . ."

                            "Yeah, too bad.":
                                $ Girl.FaceChange("bemused")
                                if Girl == RogueX:
                                        ch_r ". . ."
                                elif Girl == KittyX:
                                        ch_k ". . . rude. . ."
                                elif Girl == EmmaX:
                                        ch_e ". . . yes. . ."
                                elif Girl == LauraX:
                                        pass
                                elif Girl == JeanX:
                                        ch_j "Right?"
                                elif Girl == StormX:
                                        ch_s "I see you."

                            "Ha! Those don't leave much to the imagination!":
                                if Girl == RogueX:
                                        ch_r "Thanks for that. . ."
                                elif Girl == KittyX:
                                        ch_k "You aren't kidding."
                                elif Girl == EmmaX:
                                        ch_e "I imagine you do enjoy that. . ."
                                elif Girl == LauraX:
                                        ch_l "I guess not."
                                elif Girl == JeanX:
                                        ch_j "Oh, I guess."
                                elif Girl == StormX:
                                        ch_s "You may be right about that. . ."


                elif Count == 3: #She is embarassed and takes off
                    $ Girl.FaceChange("startled", 2)
                    if Girl == RogueX:
                            ch_r "I, um, I should get out of here."
                    elif Girl == KittyX:
                            ch_k "This is. . . a bit breazy for me. . ."
                    elif Girl == EmmaX:
                            $ Girl.FaceChange("sexy", 1)
                            ch_e "This might cause a bit of a stir, I should probably change. . ."
                    elif Girl == LauraX:
                            $ Girl.FaceChange("perplexed", 0)
                            ch_l "I guess I should change into something else."
                    elif Girl == JeanX:
                            ch_j "I'm going to get changed though. . ."
                    elif Girl == StormX:
                            $ Girl.FaceChange("bemused", 0)
                            ch_s "I really probably should change."
                    $ Girl.Blush = 1
                    call Remove_Girl(Girl)
                    $ Girl.OutfitChange()
                #end "if they ripped"
        return
