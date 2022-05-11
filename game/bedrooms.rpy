label bedroom_entry(character):
    $ bg_current = character.Home

    call girls_room_entry(character)

    $ bg_current = "bg_campus"

    jump Misplaced

label girls_room_entry(character):
    $ bg_current = character.Home
    $ Player.DrainWord("locked", 0, 0, 1)

    call Shift_Focus(character)

    $ Nearby = []

    call Gym_Clothes_Off #call Gym_Clothes
    call Set_The_Scene(Entry = 1)
    call Taboo_Level

    $ Player.RecentActions.append("traveling")
    $ D20 = renpy.random.randint(1, 20)

    $ Round -= 5 if Round >= 5 else Round

    if character in Party:
        if Time_Count >= 3 or (Time_Count == 2 and Round <= 10):
            if ApprovalCheck(character, 1000, "LI", Alt = [[JubesX], 500]) or ApprovalCheck(character, 600, "OI",Alt = [[JubesX], 300]):
                if character == RogueX:
                    ch_r "It's pretty late, [character.Petname], but you can come in for a little bit."
                elif character == KittyX:
                    ch_k "It's kinda late, [character.Petname], but you can have a minute."
                elif character == EmmaX:
                    ch_e "It's rather late, [character.Petname], but I can spare you some time."
                elif character == LauraX:
                    ch_l "It's getting late, but come on in."
                elif character == JeanX:
                    ch_j "It's late, but whatever."
                elif character == StormX:
                    ch_s "You've come by fairly late, [character.Petname], but come in."
                elif character == JubesX:
                    ch_v "Sure, come on in."
            elif character.Addict >= 50:
                if character == RogueX:
                    ch_r "Um, yeah, you'd better come in. . ."
                elif character == KittyX:
                    ch_k "I'd really like to see you. . ."
                elif character == EmmaX:
                    ch_e "Yes. . . I suppose you should. . ."
                elif character == LauraX:
                    ch_l "Um, yeah, you'd better come in. . ."
                elif character == JeanX:
                    ch_j "Oh, um, sure, come in."
                elif character == StormX:
                    ch_s "Oh, yes, come in."
                elif character == JubesX:
                    ch_v "Oh, yes, do come in. . ."
            elif ApprovalCheck(character, 500, "LI") or ApprovalCheck(character, 300, "OI"):
                if character == RogueX:
                    ch_r "It's a little late [character.Petname]. See you tomorrow."
                elif character == KittyX:
                    ch_k "It's a little late [character.Petname]. Tomorrow?"
                elif character == EmmaX:
                    ch_e "It's late [character.Petname]. I'll see you tomorrow."
                elif character == LauraX:
                    ch_l "See you tomorrow."
                elif character == JeanX:
                    ch_j "It's late, see ya."
                elif character == StormX:
                    ch_s "You've come by fairly late, [character.Petname], perhaps visit tomorrow."
                elif character == JubesX:
                    ch_v "No thanks. . ."

                $ character.RecentActions.append("noentry")
                $ character.DailyActions.append("noentry")

                if character in Party:
                        $ Party.remove(character)

                "She heads inside and closes the door behind her."

                return
        else:
            if character == RogueX:
                ch_r "Come on in, [character.Petname]."
            elif character == KittyX:
                ch_k "Come on in!"
            elif character == EmmaX:
                ch_e "Don't just stand at the door."
            elif character == LauraX:
                ch_l "Come on in."
            elif character == JeanX:
                ch_j "Make yourself at home."
            elif character == StormX:
                ch_s "Make yourself welcome."
            elif character == JubesX:
                ch_v "Have a seat or whatever. . ."

        call EventCalls

        call girls_room(character)

    if Round >= 10 and character.Loc == bg_current and "les" in character.RecentActions:
        call Girls_Caught_Lesing(character)

        if not _return:
            call girls_room(character)

    if bg_current == KittyX.Home and "dress2" in LauraX.History and not Party:
        call Laura_Dressup3
        $ bg_current = "bg campus"
        jump Misplaced

    if Round >= 10 and character.Loc == bg_current and "gonnafap" in character.DailyActions and D20 >= 5:
        call Girl_Caught_Mastubating(character)
    else:
        if character in Keys:
            menu:
                "You have a key, what do you do?"
                "Knock politely":
                    $ Line = "knock"
                "Use the key to enter.":
                    call Set_The_Scene

        if Line != "knock" and character in Keys:
            if character.Loc == bg_current:
                if Round <= 10:        #add "no" condtion here
                    if Time_Count >= 3: #night time
                        "She's asleep in bed. You slip out quietly." #fix add options here.

                        return
                elif "gonnafap" in character.DailyActions and D20 >= 5:
                    call Girl_Caught_Mastubating(character)
                elif D20 >=15 and (Time_Count >= 3 or Time_Count == 0):
                    call Girl_Caught_Changing(character)

                    call girls_room(character)
        else:
            "You knock on [character.Name]'s door."
            if character.Loc == bg_current:
                if Round <= 10:
                    if Time_Count >= 3: #night time
                        "There's no answer, she's probably asleep."

                        $ bg_current = "bg campus"
                        call Set_The_Scene
                        jump Misplaced
                if (D20 >=19 and character.Lust >= 50) or (D20 >=15 and character.Lust >= 70) or (D20 >=10 and character.Lust >= 80):
                    "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                    "After several seconds and some more shuffling of clothing, [character.Name] comes to the door."

                    $ character.FaceChange("perplexed",2)
                    call Set_The_Scene

                    if character == RogueX:
                        ch_r "Sorry about that [character.Petname], I was. . . working out."
                    elif character == KittyX:
                        ch_k "Oh, hey, [character.Petname], I was. . . never mind."
                    elif character == EmmaX:
                        ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                    elif character == LauraX:
                        ch_l "Um, hey [character.Petname], just working off some stress."
                    elif character == JeanX:
                        ch_j "Oh, um, hey."
                    elif character == StormX:
                        ch_s "Ah, [character.Petname], I was. . . preocupied."
                    elif character == JubesX:
                        ch_v "Oh, um, [character.Petname]. I was just. . . taking care of something."

                    $ character.FaceChange("perplexed",1)
                    $ temp_modifier += 10
                elif D20 >=15 and (Time_Count >= 3 or Time_Count == 0):
                    "You hear the rustling of fabric and some knocking around, but after a few seconds [character.Name] comes to the door."

                    call Set_The_Scene

                    if character == RogueX:
                        ch_r "Sorry about that [character.Petname], I was just getting changed."
                    elif character == KittyX:
                        ch_k "Oh, hi [character.Petname], I was[KittyX.like]just getting changed."
                    elif character == EmmaX:
                        ch_e "Oh, do come in [character.Petname], don't mind that I was just getting changed."
                    elif character == LauraX:
                        ch_l "Hey [character.Petname], I was just getting dressed."
                    elif character == JeanX:
                        ch_j "Hey [character.Petname], I was getting dressed."
                    elif character == StormX:
                        ch_s "Oh, hello, [character.Petname]. I was just getting changed."
                    elif character == JubesX:
                        ch_v "Oh, hey, [character.Petname], I was getting dressed."
                elif "angry" in character.RecentActions:
                    $ character.FaceChange("angry")

                    $ Trigger = 0

                    call get_out_dialog(character)

                    $ bg_current = "bg campus"
                    jump Misplaced
                else:
                    call Set_The_Scene

                    "[character.Name] opens the door and leans out."
                    "You ask if you can come inside."

        if character.Loc != bg_current:
            "Looks like she's not home right now."
            if character in Keys:
                menu:
                    "Go in and wait for her?"
                    "Yes":
                        $ Line = 0
                        call girls_room(character)
                    "No":
                        pass

            "You head back."

            $ bg_current = "bg campus"
            jump Misplaced
        elif Time_Count >= 3 and "noentry" in character.RecentActions:
            if character == RogueX:
                ch_r "Hey, I told you you're not welcome. I'll see you tomorrow."
            elif character == KittyX:
                ch_k "Scram. I'll see you tomorrow."
            elif character == EmmaX:
                ch_e "Later, [character.Petname]."
            elif character == LauraX:
                ch_l "Not tonight, [character.Petname]."
            elif character == JeanX:
                ch_j "No, not tonight."
            elif character == StormX:
                ch_s "I made myself clear, [character.Petname], not tonight."
            elif character == JubesX:
                ch_v "Don't mess with me at night, [character.Petname]. Out!"

            $ bg_current = "bg campus"
            jump Misplaced
        elif "noentry" in character.RecentActions or "angry" in character.RecentActions:
            $ character.FaceChange("angry")

            call get_out_dialog(character)

            $ bg_current = "bg campus"
            jump Misplaced
        elif Time_Count >= 3 and (character.Sleep or character.SEXP >= 30 or character == JubesX):
            if character == RogueX:
                ch_r "It's pretty late, [character.Petname], but it's always nice to see you."
            elif character == KittyX:
                ch_k "It's late, [character.Petname], but you're so cute."
            elif character == EmmaX:
                ch_e "It is getting late, [character.Petname]."
                ch_e "but you are so adorable."
            elif character == LauraX:
                ch_l "It's late, but I was hoping you'd stop by."
            elif character == JeanX:
                ch_j "Hey [character.Petname], almost time for bed."
            elif character == StormX:
                ch_s "Hello, [character.Petname], it's almost bedtime."
            elif character == JubesX:
                ch_v "Oh, hey, [character.Petname] come on in."
        elif Time_Count >= 3 and (ApprovalCheck(character, 1000, "LI") or ApprovalCheck(character, 600, "OI") or character == JubesX):
            if character == RogueX:
                ch_r "It's pretty late, [character.Petname], but you can come in for a little bit."
            elif character == KittyX:
                ch_k "It's late, [character.Petname], but I could hang out a bit."
            elif character == EmmaX:
                ch_e "It is getting late, [character.Petname], but I could make some time."
            elif character == LauraX:
                ch_l "It's late, [character.Petname], but you can come in."
            elif character == JeanX:
                ch_j "It's kinda late."
            elif character == StormX:
                ch_s "You've come by fairly late, [character.Petname], but come in."
            elif character == JubesX:
                ch_v "Oh, hey, [character.Petname] come on in."
        elif character.Addict >= 50:
            $ character.FaceChange("manic")

            if character == RogueX:
                ch_r "Um, yeah, you'd better come in. . ."
            elif character == KittyX:
                ch_k "I could use some attention. . ."
            elif character == EmmaX:
                ch_e "I. . . suppose you should. . ."
            elif character == LauraX:
                ch_l "You should come in. . ."
            elif character == JeanX:
                ch_j "Oh, um. . . hey. . ."
            elif character == StormX:
                ch_s "Oh, yes, come in."
            elif character == JubesX:
                ch_v "Oh, yes, do come in. . ."
        elif Time_Count >= 3 and (ApprovalCheck(character, 500, "LI") or ApprovalCheck(character, 300, "OI")):
            if character == RogueX:
                ch_r "It's a little late [character.Petname]. Maybe tomorrow."
            elif character == KittyX:
                ch_k "It's late [character.Petname]. Tomorrow?"
            elif character == EmmaX:
                ch_e "It's late [character.Petname]. I'll see you tomorrow."
            elif character == LauraX:
                ch_l "It's late [character.Petname]. Come back tomorrow."
            elif character == JeanX:
                ch_j "It's late, see ya."
            elif character == StormX:
                ch_s "You've come by fairly late, [character.Petname], perhaps tomorrow."
            elif character == JubesX:
                ch_v "Nope. . ."

            $ character.RecentActions.append("noentry")
            $ character.DailyActions.append("noentry")

            $ bg_current = "bg campus"
            jump Misplaced
        elif ApprovalCheck(character, 600, "LI") or ApprovalCheck(character, 300, "OI"):
            if character == RogueX:
                ch_r "Sure, come on in [character.Petname]."
            elif character == KittyX:
                ch_k "Sure, come on in [character.Petname]."
            elif character == EmmaX:
                ch_e "Come in, [character.Petname]."
            elif character == LauraX:
                ch_l "Make yourself at home, I guess."
            elif character == JeanX:
                ch_j "Hey, make yourself at home."
            elif character == StormX:
                ch_s "Oh, hello [character.Petname], come in."
            elif character == JubesX:
                ch_v "Oh, hey, [character.Petname] come on in."
        else:
            #She doesn't like you
            if character == RogueX:
                ch_r "I'd rather you didn't come in, thanks."
            elif character == KittyX:
                ch_k "Nah, you can stay out."
            elif character == EmmaX:
                ch_e "I don't think that would be appropriate."
            elif character == LauraX:
                ch_l "Nah."
            elif character == JeanX:
                ch_j "Nah, get going."
            elif character == StormX:
                ch_s "I would rather you didn't."
            elif character == JubesX:
                ch_v "Oh, no thanks."

            $ character.RecentActions.append("noentry")
            $ character.DailyActions.append("noentry")

            $ bg_current = "bg campus"
            jump Misplaced

    call EventCalls
    jump Misplaced

label girls_room(character):
    $ bg_current = character.Home
    $ Player.DrainWord("traveling", 1, 0)

    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)

    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls

    call GirlsAngry

    if character.Loc == bg_current:
        $ Line = "You are in "+character.Name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+character.Name+"'s room, but she isn't here. What would you like to do?"

    menu:
        "[Line]"

        "Chat":
            call Chat
        "Would you like to study?":
            call Study_Session
        "Lock the door" if "locked" not in Player.Traits:
            if character.Loc == bg_current and not ApprovalCheck(character, 1000, Alt = [[LauraX, JeanX], 1200]):
                if character == RogueX:
                    ch_r "Hey, could you maybe keep that open, [RogueX.Petname]?"
                elif character == KittyX:
                    ch_k "Um, I'd[KittyX.like]rather you didn't lock my door, [KittyX.Petname]?"
                elif character == EmmaX:
                    ch_e "Do you really think it's appropriate for you to lock the door to my room?"
                elif character == LauraX:
                    ch_l "I don't want to feel caged up like that, [LauraX.Petname]."
                elif character == JeanX:
                    ch_j "Hey, don't lock that."
                elif character == StormX:
                    ch_s "I would really prefer you didn't lock the door, [StormX.Petname]."
                elif character == JubesX:
                    ch_v "You really shouldn't lock -my- door, [JubesX.Petname]."
            else:
                "You lock the door"

                $ Player.Traits.append("locked")

                call Taboo_Level
        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"

            $ Player.Traits.remove("locked")

            call Taboo_Level
        "Sleep" if Time_Count >= 3: #night time
            call Round10
            call Girls_Location
            call EventCalls
        "Wait" if Time_Count < 3: #not night time
            call Round10
            call Girls_Location
            call EventCalls
        "Return to Your Room" if TravelMode:
            jump player_room_entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.Name]'s Room" if bg_current is not RogueX.Home and "met" in RogueX.History:
                    call girls_room_entry(RogueX)
                "[KittyX.Name]'s Room" if bg_current is not KittyX.Home and "met" in KittyX.History:
                    call girls_room_entry(KittyX)
                "[EmmaX.Name]'s Room" if bg_current is not EmmaX.Home and "met" in EmmaX.History:
                    call girls_room_entry(EmmaX)
                "[LauraX.Name]'s Room" if bg_current is not LauraX.Home and "met" in LauraX.History:
                    call girls_room_entry(LauraX)
                "[JeanX.Name]'s Room" if bg_current is not JeanX.Home and "met" in JeanX.History:
                    call girls_room_entry(JeanX)
                "[StormX.Name]'s Room" if bg_current is not StormX.Home and "met" in StormX.History:
                    call girls_room_entry(StormX)
                "[JubesX.Name]'s Room" if bg_current is not JubesX.Home and "met" in JubesX.History:
                    call girls_room_entry(JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry
        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    if "angry" in character.RecentActions:
        $ character.FaceChange("angry")

        call get_out_dialog(character)

        $ Line = 0
        $ Trigger = 0

        jump player_room

    call girls_room(character)

label player_room_entry:
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg player"

    call Gym_Clothes_Off

    $ Player.RecentActions.append("traveling")

    $ Nearby = []
    $ Round -= 5 if Round >= 5 else Round

    call EventCalls
    call Set_The_Scene

    jump Clear_Stack

label player_room:
    $ bg_current = "bg player"
    $ Player.DrainWord("traveling", 1, 0)

    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)

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
        "Sleep" if Time_Count >= 3: #night time
            call Round10
            call Girls_Location
            call EventCalls
        "Wait" if Time_Count < 3: #not night time
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
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry
        "Attic" if TravelMode and "attic" in Player.History:
            jump StormMeet
        "Leave" if not TravelMode:
            call Worldmap
        "Leave [Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    jump player_room
