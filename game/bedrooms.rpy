label bedroom_entry(Girl):
    $ bg_current = Girl.home

    call girls_room_entry(Girl)

    $ bg_current = "bg_campus"

    jump Misplaced

label girls_room_entry(Girl):
    $ bg_current = Girl.home
    $ door_locked = False

    call shift_focus(Girl)

    $ Nearby = []

    call Gym_Clothes_Off #call Gym_Clothes
    call set_the_scene(entering = 1)
    call Taboo_Level

    $ Player.recent_history.append("traveling")

    $ D20 = renpy.random.randint(1, 20)
    $ round -= 5 if round >= 5 else round

    if Girl in Party:
        if time_index >= 3 or (time_index == 2 and round <= 10):
            if approval_check(Girl, 1000, "LI", Alt = [[JubesX], 500]) or approval_check(Girl, 600, "OI",Alt = [[JubesX], 300]):
                if Girl == RogueX:
                    ch_r "It's pretty late, [Girl.player_petname], but you can come in for a little bit."
                elif Girl == KittyX:
                    ch_k "It's kinda late, [Girl.player_petname], but you can have a minute."
                elif Girl == EmmaX:
                    ch_e "It's rather late, [Girl.player_petname], but I can spare you some time."
                elif Girl == LauraX:
                    ch_l "It's getting late, but come on in."
                elif Girl == JeanX:
                    ch_j "It's late, but whatever."
                elif Girl == StormX:
                    ch_s "You've come by fairly late, [Girl.player_petname], but come in."
                elif Girl == JubesX:
                    ch_v "Sure, come on in."
            elif Girl.addiction >= 50:
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
            elif approval_check(Girl, 500, "LI") or approval_check(Girl, 300, "OI"):
                if Girl == RogueX:
                    ch_r "It's a little late [Girl.player_petname]. See you tomorrow."
                elif Girl == KittyX:
                    ch_k "It's a little late [Girl.player_petname]. Tomorrow?"
                elif Girl == EmmaX:
                    ch_e "It's late [Girl.player_petname]. I'll see you tomorrow."
                elif Girl == LauraX:
                    ch_l "See you tomorrow."
                elif Girl == JeanX:
                    ch_j "It's late, see ya."
                elif Girl == StormX:
                    ch_s "You've come by fairly late, [Girl.player_petname], perhaps visit tomorrow."
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
                ch_r "Come on in, [Girl.player_petname]."
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

        call event_calls

        call girls_room(Girl)

    if round >= 10 and Girl.location == bg_current and "lesbian" in Girl.recent_history:
        call Girls_Caught_Lesing(Girl)

        if not _return:
            call girls_room(Girl)

    if bg_current == KittyX.home and "dress2" in LauraX.history and not Party:
        call Laura_Dressup3

        $ bg_current = "bg_campus"

        jump Misplaced

    if round >= 10 and Girl.location == bg_current and "will_masturbate" in Girl.daily_history and D20 >= 5:
        call Girl_Caught_Mastubating(Girl)
    else:
        if Girl in Keys:
            menu:
                "You have a key, what do you do?"
                "Knock politely":
                    $ line = "knock"
                "Use the key to enter.":
                    $ line = None
                    call set_the_scene
        else:
            $ line = None

        if line != "knock" and Girl in Keys:
            if Girl.location == bg_current:
                if round <= 10:        #add "no" condtion here
                    if time_index >= 3: #night time
                        "She's asleep in bed. You slip out quietly." #fix add options here.

                        return
                elif "will_masturbate" in Girl.daily_history and D20 >= 5:
                    call Girl_Caught_Mastubating(Girl)
                elif D20 >=15 and (time_index >= 3 or time_index == 0):
                    call Girl_Caught_Changing(Girl)
                    call girls_room(Girl)
        else:
            "You knock on [Girl.name]'s door."
            if Girl.location == bg_current:
                if round <= 10:
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
                        ch_r "Sorry about that [Girl.player_petname], I was. . . working out."
                    elif Girl == KittyX:
                        ch_k "Oh, hey, [Girl.player_petname], I was. . . never mind."
                    elif Girl == EmmaX:
                        ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                    elif Girl == LauraX:
                        ch_l "Um, hey [Girl.player_petname], just working off some stress."
                    elif Girl == JeanX:
                        ch_j "Oh, um, hey."
                    elif Girl == StormX:
                        ch_s "Ah, [Girl.player_petname], I was. . . preocupied."
                    elif Girl == JubesX:
                        ch_v "Oh, um, [Girl.player_petname]. I was just. . . taking care of something."

                    $ Girl.change_face("perplexed",1)

                    $ temp_modifier += 10
                elif D20 >=15 and (time_index >= 3 or time_index == 0):
                    "You hear the rustling of fabric and some knocking around, but after a few seconds [Girl.name] comes to the door."

                    call set_the_scene

                    if Girl == RogueX:
                        ch_r "Sorry about that [Girl.player_petname], I was just getting changed."
                    elif Girl == KittyX:
                        ch_k "Oh, hi [Girl.player_petname], I was[KittyX.like]just getting changed."
                    elif Girl == EmmaX:
                        ch_e "Oh, do come in [Girl.player_petname], don't mind that I was just getting changed."
                    elif Girl == LauraX:
                        ch_l "Hey [Girl.player_petname], I was just getting dressed."
                    elif Girl == JeanX:
                        ch_j "Hey [Girl.player_petname], I was getting dressed."
                    elif Girl == StormX:
                        ch_s "Oh, hello, [Girl.player_petname]. I was just getting changed."
                    elif Girl == JubesX:
                        ch_v "Oh, hey, [Girl.player_petname], I was getting dressed."
                elif "angry" in Girl.recent_history:
                    $ Girl.change_face("angry")

                    $ primary_action = 0

                    call get_out_lines(Girl)

                    $ bg_current = "bg_campus"

                    jump Misplaced
                else:
                    call set_the_scene

                    "[Girl.name] opens the door and leans out."
                    "You ask if you can come inside."

        if Girl.location != bg_current:
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
                ch_e "Later, [Girl.player_petname]."
            elif Girl == LauraX:
                ch_l "Not tonight, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "No, not tonight."
            elif Girl == StormX:
                ch_s "I made myself clear, [Girl.player_petname], not tonight."
            elif Girl == JubesX:
                ch_v "Don't mess with me at night, [Girl.player_petname]. Out!"

            $ bg_current = "bg_campus"

            jump Misplaced
        elif "noentry" in Girl.recent_history or "angry" in Girl.recent_history:
            $ Girl.change_face("angry")

            call get_out_lines(Girl)

            $ bg_current = "bg_campus"

            jump Misplaced
        elif time_index >= 3 and (Girl.event_counter["sleepover"] or Girl.SEXP >= 30 or Girl == JubesX):
            if Girl == RogueX:
                ch_r "It's pretty late, [Girl.player_petname], but it's always nice to see you."
            elif Girl == KittyX:
                ch_k "It's late, [Girl.player_petname], but you're so cute."
            elif Girl == EmmaX:
                ch_e "It is getting late, [Girl.player_petname]."
                ch_e "but you are so adorable."
            elif Girl == LauraX:
                ch_l "It's late, but I was hoping you'd stop by."
            elif Girl == JeanX:
                ch_j "Hey [Girl.player_petname], almost time for bed."
            elif Girl == StormX:
                ch_s "Hello, [Girl.player_petname], it's almost bedtime."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.player_petname] come on in."
        elif time_index >= 3 and (approval_check(Girl, 1000, "LI") or approval_check(Girl, 600, "OI") or Girl == JubesX):
            if Girl == RogueX:
                ch_r "It's pretty late, [Girl.player_petname], but you can come in for a little bit."
            elif Girl == KittyX:
                ch_k "It's late, [Girl.player_petname], but I could hang out a bit."
            elif Girl == EmmaX:
                ch_e "It is getting late, [Girl.player_petname], but I could make some time."
            elif Girl == LauraX:
                ch_l "It's late, [Girl.player_petname], but you can come in."
            elif Girl == JeanX:
                ch_j "It's kinda late."
            elif Girl == StormX:
                ch_s "You've come by fairly late, [Girl.player_petname], but come in."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.player_petname] come on in."
        elif Girl.addiction >= 50:
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
        elif time_index >= 3 and (approval_check(Girl, 500, "LI") or approval_check(Girl, 300, "OI")):
            if Girl == RogueX:
                ch_r "It's a little late [Girl.player_petname]. Maybe tomorrow."
            elif Girl == KittyX:
                ch_k "It's late [Girl.player_petname]. Tomorrow?"
            elif Girl == EmmaX:
                ch_e "It's late [Girl.player_petname]. I'll see you tomorrow."
            elif Girl == LauraX:
                ch_l "It's late [Girl.player_petname]. Come back tomorrow."
            elif Girl == JeanX:
                ch_j "It's late, see ya."
            elif Girl == StormX:
                ch_s "You've come by fairly late, [Girl.player_petname], perhaps tomorrow."
            elif Girl == JubesX:
                ch_v "Nope. . ."

            $ Girl.recent_history.append("noentry")
            $ Girl.daily_history.append("noentry")

            $ bg_current = "bg_campus"

            jump Misplaced
        elif approval_check(Girl, 600, "LI") or approval_check(Girl, 300, "OI"):
            if Girl == RogueX:
                ch_r "Sure, come on in [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "Sure, come on in [Girl.player_petname]."
            elif Girl == EmmaX:
                ch_e "Come in, [Girl.player_petname]."
            elif Girl == LauraX:
                ch_l "Make yourself at home, I guess."
            elif Girl == JeanX:
                ch_j "Hey, make yourself at home."
            elif Girl == StormX:
                ch_s "Oh, hello [Girl.player_petname], come in."
            elif Girl == JubesX:
                ch_v "Oh, hey, [Girl.player_petname] come on in."
        else:
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

    call event_calls
    jump Misplaced

label girls_room(Girl):
    $ bg_current = Girl.home
    $ Player.drain_word("traveling", 1, 0)

    call Taboo_Level
    call set_the_scene(silent=1)
    call QuickEvents
    call checkout(1)

    if round <= 10:
        call round_10
        call girls_location
        call event_calls

    call GirlsAngry

    if Girl.location == bg_current:
        $ line = "You are in "+Girl.name+"'s room. What would you like to do?"
    else:
        $ line = "You are in "+Girl.name+"'s room, but she isn't here. What would you like to do?"

    menu:
        "[line]"
        "Chat":
            call Chat
        "Would you like to study?":
            call Study_Session
        "Lock the door" if not door_locked:
            if Girl.location == bg_current and not approval_check(Girl, 1000, Alt = [[LauraX, JeanX], 1200]):
                if Girl == RogueX:
                    ch_r "Hey, could you maybe keep that open, [RogueX.player_petname]?"
                elif Girl == KittyX:
                    ch_k "Um, I'd[KittyX.like]rather you didn't lock my door, [KittyX.player_petname]?"
                elif Girl == EmmaX:
                    ch_e "Do you really think it's appropriate for you to lock the door to my room?"
                elif Girl == LauraX:
                    ch_l "I don't want to feel caged up like that, [LauraX.player_petname]."
                elif Girl == JeanX:
                    ch_j "Hey, don't lock that."
                elif Girl == StormX:
                    ch_s "I would really prefer you didn't lock the door, [StormX.player_petname]."
                elif Girl == JubesX:
                    ch_v "You really shouldn't lock -my- door, [JubesX.player_petname]."
            else:
                "You lock the door"

                $ door_locked = True

                call Taboo_Level
        "Unlock the door" if door_locked:
            "You unlock the door"

            $ door_locked = False

            call Taboo_Level
        "Sleep" if time_index >= 3: #night time
            call round_10
            call girls_location
            call event_calls
        "wait" if time_index < 3: #not night time
            call round_10
            call girls_location
            call event_calls
        "Return to Your Room" if TravelMode:
            jump player_room_entry
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room" if bg_current is not RogueX.home and "met" in RogueX.history:
                    call girls_room_entry(RogueX)
                "[KittyX.name]'s Room" if bg_current is not KittyX.home and "met" in KittyX.history:
                    call girls_room_entry(KittyX)
                "[EmmaX.name]'s Room" if bg_current is not EmmaX.home and "met" in EmmaX.history:
                    call girls_room_entry(EmmaX)
                "[LauraX.name]'s Room" if bg_current is not LauraX.home and "met" in LauraX.history:
                    call girls_room_entry(LauraX)
                "[JeanX.name]'s Room" if bg_current is not JeanX.home and "met" in JeanX.history:
                    call girls_room_entry(JeanX)
                "[StormX.name]'s Room" if bg_current is not StormX.home and "met" in StormX.history:
                    call girls_room_entry(StormX)
                "[JubesX.name]'s Room" if bg_current is not JubesX.home and "met" in JubesX.history:
                    call girls_room_entry(JubesX)
                "Back":
                    pass

            return
        "Go to the Showers" if TravelMode:
            jump Shower_Room_entry
        "Leave" if not TravelMode:
            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
            jump Campus_entry

    if "angry" in Girl.recent_history:
        $ Girl.change_face("angry")

        call get_out_lines(Girl)

        $ line = 0
        $ primary_action = 0

        jump player_room

label player_room_entry:
    $ door_locked = False

    $ bg_current = "bg_player"

    call Gym_Clothes_Off

    $ Player.recent_history.append("traveling")

    $ Nearby = []
    $ round -= 5 if round >= 5 else round

    call event_calls
    call set_the_scene
    jump Clear_Stack

label player_room:
    $ bg_current = "bg_player"
    $ Player.drain_word("traveling", 1, 0)

    call Taboo_Level
    call set_the_scene(silent=1)
    call QuickEvents
    call checkout(1)

    if round <= 10:
        call round_10
        call girls_location
        call event_calls

    call GirlsAngry

    menu:
        "You are in your room. What would you like to do?"
        "Chat":
            call Chat
        "Study":
            call Study_Session
        "Lock the door" if not door_locked:
            "You lock the door"

            $ door_locked = True

            call Taboo_Level
        "Unlock the door" if door_locked:
            "You unlock the door"

            $ door_locked = False

            call Taboo_Level
        "Sleep" if time_index >= 3: #night time
            call round_10
            call girls_location
            call event_calls
        "wait" if time_index < 3: #not night time
            "You wait around a bit."

            call round_10
            call girls_location
            call event_calls
        "Shop":
            call Shop
        "Special Options":
            call SpecialMenu
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.name]'s Room":
                    call girls_room_entry(RogueX)
                "[KittyX.name]'s Room" if "met" in KittyX.history:
                    call girls_room_entry(KittyX)
                "[EmmaX.name]'s Room" if "met" in EmmaX.history:
                    call girls_room_entry(EmmaX)
                "[LauraX.name]'s Room" if "met" in LauraX.history:
                    call girls_room_entry(LauraX)
                "[JeanX.name]'s Room" if "met" in JeanX.history:
                    call girls_room_entry(JeanX)
                "[StormX.name]'s Room" if "met" in StormX.history:
                    call girls_room_entry(StormX)
                "[JubesX.name]'s Room" if "met" in JubesX.history:
                    call girls_room_entry(JubesX)
                "Back":
                    pass
        "Go to the Showers" if TravelMode:
            jump Shower_Room_entry
        "Attic" if TravelMode and "attic" in Player.history:
            jump StormMeet
        "Leave" if not TravelMode:
            call Worldmap
        "Leave [Go to Campus Square]" if TravelMode:
            jump Campus_entry

    jump player_room
