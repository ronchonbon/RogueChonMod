label bedroom_entry(Girl):
    $ bg_current = Girl.Home

    call girls_room_entry(Girl)

    $ bg_current = "bg_campus"

    jump Misplaced

label girls_room_entry(Girl):
    $ bg_current = Girl.Home
    $ Player.DrainWord("locked", 0, 0, 1)

    call Shift_Focus(Girl)

    $ Nearby = []

    call Gym_Clothes_Off #call Gym_Clothes
    call set_the_scene(Entry = 1)
    call Taboo_Level

    $ Player.recent_history.append("traveling")
    $ D20 = renpy.random.randint(1, 20)

    $ Round -= 5 if Round >= 5 else Round

    if Girl in Party:
        if time_index >= 3 or (time_index == 2 and Round <= 10):
            if ApprovalCheck(Girl, 1000, "LI", Alt = [[JubesX], 500]) or ApprovalCheck(Girl, 600, "OI",Alt = [[JubesX], 300]):
                if Girl == RogueX:
                    ch_r "It's pretty late, [Girl.Petname], but you can come in for a little bit."
                elif Girl == KittyX:
                    ch_k "It's kinda late, [Girl.Petname], but you can have a minute."
                elif Girl == EmmaX:
                    ch_e "It's rather late, [Girl.Petname], but I can spare you some time."
                elif Girl == LauraX:
                    ch_l "It's getting late, but come on in."
                elif Girl == JeanX:
                    ch_j "It's late, but whatever."
                elif Girl == StormX:
                    ch_s "You've come by fairly late, [Girl.Petname], but come in."
                elif Girl == JubesX:
                    ch_v "Sure, come on in."
            elif Girl.Addict >= 50:
                if Girl == RogueX:
                    ch_r "Um, yeah, you'd better come in. . ."
                elif Girl == KittyX:
                    ch_k "I'd really like to see you. . ."
                elif Girl == EmmaX:
                    ch_e "Yes. . . I suppose you should. . ."
                elif Girl == LauraX:
                    ch_l "Um, yeah, you'd better come in. . ."
                elif Girl == JeanX:
                    ch_j "Oh, um, sure, come in."
                elif Girl == StormX:
                    ch_s "Oh, yes, come in."
                elif Girl == JubesX:
                    ch_v "Oh, yes, do come in. . ."
            elif ApprovalCheck(Girl, 500, "LI") or ApprovalCheck(Girl, 300, "OI"):
                if Girl == RogueX:
                    ch_r "It's a little late [Girl.Petname]. See you tomorrow."
                elif Girl == KittyX:
                    ch_k "It's a little late [Girl.Petname]. Tomorrow?"
                elif Girl == EmmaX:
                    ch_e "It's late [Girl.Petname]. I'll see you tomorrow."
                elif Girl == LauraX:
                    ch_l "See you tomorrow."
                elif Girl == JeanX:
                    ch_j "It's late, see ya."
                elif Girl == StormX:
                    ch_s "You've come by fairly late, [Girl.Petname], perhaps visit tomorrow."
                elif Girl == JubesX:
                    ch_v "No thanks. . ."

                $ Girl.recent_history.append("noentry")
                $ Girl.daily_history.append("noentry")

                if Girl in Party:
                        $ Party.remove(Girl)

                "She heads inside and closes the door behind her."

                return
        else:
            if Girl == RogueX:
                ch_r "Come on in, [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "Come on in!"
            elif Girl == EmmaX:
                ch_e "Don't just stand at the door."
            elif Girl == LauraX:
                ch_l "Come on in."
            elif Girl == JeanX:
                ch_j "Make yourself at home."
            elif Girl == StormX:
                ch_s "Make yourself welcome."
            elif Girl == JubesX:
                ch_v "Have a seat or whatever. . ."

        call EventCalls

        call girls_room(Girl)

    if Round >= 10 and Girl.Loc == bg_current and "les" in Girl.recent_history:
        call Girls_Caught_Lesing(Girl)

        if not _return:
            call girls_room(Girl)

    if bg_current == KittyX.Home and "dress2" in LauraX.History and not Party:
        call Laura_Dressup3
        $ bg_current = "bg_campus"
        jump Misplaced

    if Round >= 10 and Girl.Loc == bg_current and "gonnafap" in Girl.daily_history and D20 >= 5:
        call Girl_Caught_Mastubating(Girl)
    else:
        if Girl in Keys:
            menu:
                "You have a key, what do you do?"
                "Knock politely":
                    $ line = "knock"
                "Use the key to enter.":
                    call set_the_scene

        if line != "knock" and Girl in Keys:
            if Girl.Loc == bg_current:
                if Round <= 10:        #add "no" condtion here
                    if time_index >= 3: #night time
                        "She's asleep in bed. You slip out quietly." #fix add options here.

                        return
                elif "gonnafap" in Girl.daily_history and D20 >= 5:
                    call Girl_Caught_Mastubating(Girl)
                elif D20 >=15 and (time_index >= 3 or time_index == 0):
                    call Girl_Caught_Changing(Girl)

                    call girls_room(Girl)
        else:
            "You knock on [Girl.name]'s door."
            if Girl.Loc == bg_current:
                if Round <= 10:
                    if time_index >= 3: #night time
                        "There's no answer, she's probably asleep."

                        $ bg_current = "bg_campus"
                        call set_the_scene
                        jump Misplaced
                if (D20 >=19 and Girl.lust >= 50) or (D20 >=15 and Girl.lust >= 70) or (D20 >=10 and Girl.lust >= 80):
                    "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                    "After several seconds and some more shuffling of clothing, [Girl.name] comes to the door."

                    $ Girl.change_face("perplexed",2)
                    call set_the_scene

                    if Girl == RogueX:
                        ch_r "Sorry about that [Girl.Petname], I was. . . working out."
                    elif Girl == KittyX:
                        ch_k "Oh, hey, [Girl.Petname], I was. . . never mind."
                    elif Girl == EmmaX:
                        ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                    elif Girl == LauraX:
                        ch_l "Um, hey [Girl.Petname], just working off some stress."
                    elif Girl == JeanX:
                        ch_j "Oh, um, hey."
                    elif Girl == StormX:
                        ch_s "Ah, [Girl.Petname], I was. . . preocupied."
                    elif Girl == JubesX:
                        ch_v "Oh, um, [Girl.Petname]. I was just. . . taking care of something."

                    $ Girl.change_face("perplexed",1)
                    $ temp_modifier += 10
                elif D20 >=15 and (time_index >= 3 or time_index == 0):
                    "You hear the rustling of fabric and some knocking around, but after a few seconds [Girl.name] comes to the door."

                    call set_the_scene

                    if Girl == RogueX:
                        ch_r "Sorry about that [Girl.Petname], I was just getting changed."
                    elif Girl == KittyX:
                        ch_k "Oh, hi [Girl.Petname], I was[KittyX.like]just getting changed."
                    elif Girl == EmmaX:
                        ch_e "Oh, do come in [Girl.Petname], don't mind that I was just getting changed."
                    elif Girl == LauraX:
                        ch_l "Hey [Girl.Petname], I was just getting dressed."
                    elif Girl == JeanX:
                        ch_j "Hey [Girl.Petname], I was getting dressed."
                    elif Girl == StormX:
                        ch_s "Oh, hello, [Girl.Petname]. I was just getting changed."
                    elif Girl == JubesX:
                        ch_v "Oh, hey, [Girl.Petname], I was getting dressed."
                elif "angry" in Girl.recent_history:
                    $ Girl.change_face("angry")

                    $ primary_action = 0

                    call get_out_dialog(Girl)

                    $ bg_current = "bg_campus"
                    jump Misplaced
                else:
                    call set_the_scene

                    "[Girl.name] opens the door and leans out."
                    "You ask if you can come inside."

        if Girl.Loc != bg_current:
            "Looks like she's not home right now."
            if Girl in Keys:
                menu:
                    "Go in and wait for her?"
                    "Yes":
                        $ line = 0
                        call girls_room(Girl)
                    "No":
                        pass

            "You head back."

            $ bg_current = "bg_campus"
            jump Misplaced
        elif time_index >= 3 and "noentry" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Hey, I told you you're not welcome. I'll see you tomorrow."
            elif Girl == KittyX:
                ch_k "Scram. I'll see you tomorrow."
            elif Girl == EmmaX:
                ch_e "Later, [Girl.Petname]."
            elif Girl == LauraX:
                ch_l "Not tonight, [Girl.Petname]."
            elif Girl == JeanX:
                ch_j "No, not tonight."
            elif Girl == StormX:
                ch_s "I made myself clear, [Girl.Petname], not tonight."
            elif Girl == JubesX:
                ch_v "Don't mess with me at night, [Girl.Petname]. Out!"

            $ bg_current = "bg_campus"
            jump Misplaced
        elif "noentry" in Girl.recent_history or "angry" in Girl.recent_history:
            $ Girl.change_face("angry")

            call get_out_dialog(Girl)

            $ bg_current = "bg_campus"
            jump Misplaced
        elif time_index >= 3 and (Girl.Sleep or Girl.SEXP >= 30 or Girl == JubesX):
            if Girl == RogueX:
                ch_r "It's pretty late, [Girl.Petname], but it's always nice to see you."
            elif Girl == KittyX:
                ch_k "It's late, [Girl.Petname], but you're so cute."
            elif Girl == EmmaX:
                ch_e "It is getting late, [Girl.Petname]."
                ch_e "but you are so adorable."
            elif Girl == LauraX:
                ch_l "It's late, but I was hoping you'd stop by."
            elif Girl == JeanX:
                ch_j "Hey [Girl.Petname], almost time for bed."
            elif Girl == StormX:
                ch_s "Hello, [Girl.Petname], it's almost bedtime."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.Petname] come on in."
        elif time_index >= 3 and (ApprovalCheck(Girl, 1000, "LI") or ApprovalCheck(Girl, 600, "OI") or Girl == JubesX):
            if Girl == RogueX:
                ch_r "It's pretty late, [Girl.Petname], but you can come in for a little bit."
            elif Girl == KittyX:
                ch_k "It's late, [Girl.Petname], but I could hang out a bit."
            elif Girl == EmmaX:
                ch_e "It is getting late, [Girl.Petname], but I could make some time."
            elif Girl == LauraX:
                ch_l "It's late, [Girl.Petname], but you can come in."
            elif Girl == JeanX:
                ch_j "It's kinda late."
            elif Girl == StormX:
                ch_s "You've come by fairly late, [Girl.Petname], but come in."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.Petname] come on in."
        elif Girl.Addict >= 50:
            $ Girl.change_face("manic")

            if Girl == RogueX:
                ch_r "Um, yeah, you'd better come in. . ."
            elif Girl == KittyX:
                ch_k "I could use some attention. . ."
            elif Girl == EmmaX:
                ch_e "I. . . suppose you should. . ."
            elif Girl == LauraX:
                ch_l "You should come in. . ."
            elif Girl == JeanX:
                ch_j "Oh, um. . . hey. . ."
            elif Girl == StormX:
                ch_s "Oh, yes, come in."
            elif Girl == JubesX:
                ch_v "Oh, yes, do come in. . ."
        elif time_index >= 3 and (ApprovalCheck(Girl, 500, "LI") or ApprovalCheck(Girl, 300, "OI")):
            if Girl == RogueX:
                ch_r "It's a little late [Girl.Petname]. Maybe tomorrow."
            elif Girl == KittyX:
                ch_k "It's late [Girl.Petname]. Tomorrow?"
            elif Girl == EmmaX:
                ch_e "It's late [Girl.Petname]. I'll see you tomorrow."
            elif Girl == LauraX:
                ch_l "It's late [Girl.Petname]. Come back tomorrow."
            elif Girl == JeanX:
                ch_j "It's late, see ya."
            elif Girl == StormX:
                ch_s "You've come by fairly late, [Girl.Petname], perhaps tomorrow."
            elif Girl == JubesX:
                ch_v "Nope. . ."

            $ Girl.recent_history.append("noentry")
            $ Girl.daily_history.append("noentry")

            $ bg_current = "bg_campus"
            jump Misplaced
        elif ApprovalCheck(Girl, 600, "LI") or ApprovalCheck(Girl, 300, "OI"):
            if Girl == RogueX:
                ch_r "Sure, come on in [Girl.Petname]."
            elif Girl == KittyX:
                ch_k "Sure, come on in [Girl.Petname]."
            elif Girl == EmmaX:
                ch_e "Come in, [Girl.Petname]."
            elif Girl == LauraX:
                ch_l "Make yourself at home, I guess."
            elif Girl == JeanX:
                ch_j "Hey, make yourself at home."
            elif Girl == StormX:
                ch_s "Oh, hello [Girl.Petname], come in."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.Petname] come on in."
        else:
            #She doesn't like you
            if Girl == RogueX:
                ch_r "I'd rather you didn't come in, thanks."
            elif Girl == KittyX:
                ch_k "Nah, you can stay out."
            elif Girl == EmmaX:
                ch_e "I don't think that would be appropriate."
            elif Girl == LauraX:
                ch_l "Nah."
            elif Girl == JeanX:
                ch_j "Nah, get going."
            elif Girl == StormX:
                ch_s "I would rather you didn't."
            elif Girl == JubesX:
                ch_v "Oh, no thanks."

            $ Girl.recent_history.append("noentry")
            $ Girl.daily_history.append("noentry")

            $ bg_current = "bg_campus"
            jump Misplaced

    call EventCalls
    jump Misplaced

label girls_room(Girl):
    $ bg_current = Girl.Home
    $ Player.DrainWord("traveling", 1, 0)

    call Taboo_Level
    call set_the_scene(Quiet=1)
    call QuickEvents
    call Checkout(1)

    if Round <= 10:
        call Round10
        call Girls_Location
        call EventCalls

    call GirlsAngry

    if Girl.Loc == bg_current:
        $ line = "You are in "+Girl.name+"'s room. What would you like to do?"
    else:
        $ line = "You are in "+Girl.name+"'s room, but she isn't here. What would you like to do?"

    menu:
        "[line]"

        "Chat":
            call Chat
        "Would you like to study?":
            call Study_Session
        "Lock the door" if "locked" not in Player.Traits:
            if Girl.Loc == bg_current and not ApprovalCheck(Girl, 1000, Alt = [[LauraX, JeanX], 1200]):
                if Girl == RogueX:
                    ch_r "Hey, could you maybe keep that open, [RogueX.Petname]?"
                elif Girl == KittyX:
                    ch_k "Um, I'd[KittyX.like]rather you didn't lock my door, [KittyX.Petname]?"
                elif Girl == EmmaX:
                    ch_e "Do you really think it's appropriate for you to lock the door to my room?"
                elif Girl == LauraX:
                    ch_l "I don't want to feel caged up like that, [LauraX.Petname]."
                elif Girl == JeanX:
                    ch_j "Hey, don't lock that."
                elif Girl == StormX:
                    ch_s "I would really prefer you didn't lock the door, [StormX.Petname]."
                elif Girl == JubesX:
                    ch_v "You really shouldn't lock -my- door, [JubesX.Petname]."
            else:
                "You lock the door"

                $ Player.Traits.append("locked")

                call Taboo_Level
        "Unlock the door" if "locked" in Player.Traits:
            "You unlock the door"

            $ Player.Traits.remove("locked")

            call Taboo_Level
        "Sleep" if time_index >= 3: #night time
            call Round10
            call Girls_Location
            call EventCalls
        "Wait" if time_index < 3: #not night time
            call Round10
            call Girls_Location
            call EventCalls
        "Return to Your Room" if TravelMode:
            jump player_room_entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room" if bg_current is not RogueX.Home and "met" in RogueX.History:
                    call girls_room_entry(RogueX)
                "[KittyX.name]'s Room" if bg_current is not KittyX.Home and "met" in KittyX.History:
                    call girls_room_entry(KittyX)
                "[EmmaX.name]'s Room" if bg_current is not EmmaX.Home and "met" in EmmaX.History:
                    call girls_room_entry(EmmaX)
                "[LauraX.name]'s Room" if bg_current is not LauraX.Home and "met" in LauraX.History:
                    call girls_room_entry(LauraX)
                "[JeanX.name]'s Room" if bg_current is not JeanX.Home and "met" in JeanX.History:
                    call girls_room_entry(JeanX)
                "[StormX.name]'s Room" if bg_current is not StormX.Home and "met" in StormX.History:
                    call girls_room_entry(StormX)
                "[JubesX.name]'s Room" if bg_current is not JubesX.Home and "met" in JubesX.History:
                    call girls_room_entry(JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry
        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    if "angry" in Girl.recent_history:
        $ Girl.change_face("angry")

        call get_out_dialog(Girl)

        $ line = 0
        $ primary_action = 0

        jump player_room

    call girls_room(Girl)

label player_room_entry:
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg_player"

    call Gym_Clothes_Off

    $ Player.recent_history.append("traveling")

    $ Nearby = []
    $ Round -= 5 if Round >= 5 else Round

    call EventCalls
    call set_the_scene

    jump Clear_Stack

label player_room:
    $ bg_current = "bg_player"
    $ Player.DrainWord("traveling", 1, 0)

    call Taboo_Level
    call set_the_scene(Quiet=1)
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
        "Sleep" if time_index >= 3: #night time
            call Round10
            call Girls_Location
            call EventCalls
        "Wait" if time_index < 3: #not night time
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
        "Go to the Showers" if TravelMode:
            jump Shower_Room_Entry
        "Attic" if TravelMode and "attic" in Player.History:
            jump StormMeet
        "Leave" if not TravelMode:
            call Worldmap
        "Leave [Go to Campus Square]" if TravelMode:
            jump Campus_Entry

    jump player_room
