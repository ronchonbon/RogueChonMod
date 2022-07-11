label world_map:
    hide screen Girl_picker

    $ stack_depth = renpy.call_stack_depth()

    while True:
        $ Player.destination = None

        menu:
            "Where would you like to go?"
            "My room" if Player.location != "bg_player":
                $ Player.destination = "bg_player"
            "Girl's rooms":
                menu:
                    "[RogueX.name]'s room" if Player.location != "bg_rogue":
                        $ Player.destination = RogueX
                    "[KittyX.name]'s room" if Player.location != "bg_kitty":
                        $ Player.destination = KittyX
                    "[EmmaX.name]'s room" if Player.location != "bg_emma":
                        $ Player.destination = EmmaX
                    "[LauraX.name]'s room" if Player.location != "bg_laura":
                        $ Player.destination = LauraX
                    "[JeanX.name]'s room" if Player.location != "bg_jean":
                        $ Player.destination = JeanX
                    "[StormX.name]'s room" if Player.location != "bg_storm":
                        $ Player.destination = StormX
                    "[JubesX.name]'s room" if Player.location != "bg_jubes":
                        $ Player.destination = JubesX
                    "Back":
                        pass
            "University Square" if Player.location != "bg_campus":
                call check_sunshock

                $ Player.destination = "bg_campus"
            "Class" if Player.location != "bg_classroom":
                if time_index < 3:
                    $ Player.destination = "bg_classroom"
                elif "Xavier" in Player.Keys:
                    "The door is locked, but you were able to use Xavier's key to get in."

                    $ Player.destination = "bg_classroom"
                else:
                    "It's late for classes and the classrooms are locked down."

                    $ Player.destination = None
            "The Danger Room" if Player.location != "bg_dangerroom":
                $ Player.destination = "bg_dangerroom"
            "The showers" if Player.location != "bg_shower":
                $ Player.destination = "bg_shower"
            "The pool" if Player.location != "bg_pool":
                call check_sunshock

                $ Player.destination = "bg_pool"
            "Xavier's study" if Player.location != "bg_study":
                $ Player.destination = "bg_study"
            # "The mall" if time_index < 3 and Player.location != "bg_mall":#if "mall" in Player.history:
            #     call check_sunshock
            #
            #     $ Player.destination = "bg_mall"
            # "The attic" if "attic" in Player.history and Player.location != "bg_storm":
            #     jump meet_Storm
            "Stay where I am.":
                return

        if Player.destination:
            $ stack_depth = renpy.call_stack_depth()

            while stack_depth > 0:
                $ stack_depth -= 1

                $ renpy.pop_call()

            if Player.location == "bg_dangerroom":
                call exit_gym

            call hide_all

            $ Player.traveling = True

            if Player.destination == "bg_player":
                jump player_room
            elif Player.destination in all_Girls:
                $ Girl = Player.destination

                jump girls_room
            elif Player.destination == "bg_campus":
                jump campus
            elif Player.destination == "bg_classroom":
                jump classroom
            elif Player.destination == "bg_dangerroom":
                jump danger_room
            elif Player.destination == "bg_shower":
                jump shower_room
            elif Player.destination == "bg_pool":
                jump pool
            elif Player.destination == "bg_study":
                jump study_room
            elif Player.destination == "bg_mall":
                jump mall

label player_room:
    $ door_locked = False

    if Player.traveling:
        $ Player.traveling = False

        $ Nearby = []

        call set_the_scene(location = "bg_player", fade = True)
    else:
        call set_the_scene(location = "bg_player")

    if round <= 10:
        call tenth_round
        call set_the_scene

    while True:
        show screen Girl_picker()

        menu:
            "You are in your room. What would you like to do?"
            "Study":
                call study
            "Lock the door" if not door_locked:
                "You lock the door."

                $ door_locked = True
            "Unlock the door" if door_locked:
                "You unlock the door."

                $ door_locked = False
            "Sleep" if time_index > 2:
                call tenth_round
                call set_the_scene
            "Wait" if time_index < 3:
                "You wait around a bit."

                call tenth_round
                call set_the_scene
            "Special options":
                call SpecialMenu
            "Leave":
                call world_map

label girls_room_entry:
    $ D20 = renpy.random.randint(1, 20)

    if True:
        $ knocking = False

        if Girl in Player.Keys:
            menu:
                "You have a key, what do you do?"
                "Knock politely":
                    $ knocking = True
                "Use the key to enter":
                    call set_the_scene(location = Girl.home, fade = True)

                    if Girl.location == Girl.home:
                        if round <= 10:
                            if time_index > 2:
                                "She's asleep in bed. You slip out quietly."

                                $ Player.traveling = True

                                jump player_room

        if Girl not in Player.Keys or knocking:
            "You knock on [Girl.name]'s door."

            if Girl.location == Girl.home:
                if round <= 10:
                    if time_index > 2:
                        "There's no answer, she's probably asleep."

                        $ Player.traveling = True

                        jump player_room

                call add_Girls(Girl)

                "[Girl.name] opens the door and leans out."
                "You ask if you can come inside."
            else:
                "Looks like she's not home right now."

                if Girl in Player.Keys:
                    menu:
                        "Go in and wait for her?"
                        "Yes":
                            return
                        "No":
                            "You head back."

                $ Player.traveling = True

                jump player_room

    $ Girl.location = Girl.home

    return

label girls_room:
    if Player.traveling:
        $ Player.traveling = False

        $ door_locked = False

        $ Nearby = []

        call set_the_scene(location = "bg_door", fade = True)
        call girls_room_entry

    if Player.location != Girl.home:
        $ door_locked = False

        call set_the_scene(location = Girl.home, fade = True)

    if round <= 10:
        call tenth_round
        call set_the_scene

    while True:
        if Girl.location == Player.location:
            $ line = "You are in " + Girl.name + "'s room. What would you like to do?"
        else:
            $ line = "You are in + " + Girl.name + "'s room, but she isn't here. What would you like to do?"

        show screen Girl_picker()

        menu:
            "[line]"
            "Would you like to study?":
                call study
            "Lock the door" if not door_locked:
                if Girl.location == Player.location and not approval_check(Girl, 1000, alternate_thresholds = {LauraX: 1200, JeanX: 1200}):
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
                    "You lock the door."

                    $ door_locked = True
            "Unlock the door" if door_locked:
                "You unlock the door."

                $ door_locked = False
            "Sleep" if time_index > 2:
                call tenth_round
                call set_the_scene
            "Wait" if time_index < 3:
                "You wait around a bit."

                call tenth_round
                call set_the_scene
            "Leave":
                call world_map

label campus:
    $ door_locked = False

    if Player.traveling:
        $ Player.traveling = False

        $ Nearby = []

    call set_the_scene(location = "bg_campus", fade = True)

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.traveling = True

            jump player_room

        call tenth_round
        call set_the_scene

    while True:
        show screen Girl_picker()

        menu:
            "You are in the university square. What would you like to do?"
            "Wait" if time_index < 3:
                "You wait around a bit."

                call tenth_round
                call set_the_scene
            "Leave":
                call world_map

label classroom:
    if Player.traveling:
        $ Player.traveling = False

        $ door_locked = False

        $ Nearby = []

        if Player.location != "bg_classroom":
            call set_the_scene(location = "bg_classroom", fade = True)

        if time_index < 2 and weekday < 5:
            call classroom_seating
    else:
        $ door_locked = False

        call set_the_scene(location = "bg_classroom")

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.traveling = True

            jump player_room

        call tenth_round
        call set_the_scene

    while True:
        show screen Girl_picker()

        menu:
            "What would you like to do?"
            "Take the morning class" if weekday < 5 and time_index == 0 and round > 15:
                if round >= 30:
                    call take_class
                    call tenth_round
                    call set_the_scene
                else:
                    "Class is already letting out. You can hang out until the next one."
            "Take the morning class (locked)" if weekday < 5 and time_index == 0 and round <= 15:
                pass
            "Take the afternoon class" if weekday < 5 and time_index == 1 and round > 15:
                if round >= 30:
                    call take_class
                    call tenth_round
                    call set_the_scene
                else:
                    "Class is already letting out. You can hang out until they lock up for the night."
            "Take the morning class (locked)" if weekday < 5 and time_index == 1 and round <= 15:
                pass
            "Lock the door" if not door_locked:
                if weekday >= 5 or time_index >= 2:
                    "You lock the door."

                    $ door_locked = True
                else:
                    "You can't really do that during class."
            "Unlock the door" if door_locked:
                "You unlock the door."

                $ door_locked = False
            "Wait" if time_index < 3:
                "You hang out for a bit."

                call tenth_round
                call set_the_scene

                if time_index < 2:
                    "A new class is in session. What would you like to do?"
                else:
                    "Classes have let out for the day. What would you like to do?"
            "Leave":
                call world_map

label danger_room_entry:
    $ Changing = Player.Party[:]

    if True:
        show black_screen onlayer black

        python:
            for G in Changing:
                G.change_Outfit(G.Wardrobe.gym_Outfit.name, instant = True)

        hide black_screen onlayer black

    return

label danger_room:
    $ door_locked = False

    if Player.traveling:
        $ Player.traveling = False

        $ Nearby = []

        call set_the_scene(location = "bg_dangerroom", fade = True)
        call danger_room_entry
    else:
        call set_the_scene(location = "bg_dangerroom")

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.traveling = True

            jump player_room

        call tenth_round
        call set_the_scene

    while True:
        show screen Girl_picker()

        menu:
            "What would you like to do?"
            "Train":
                if time_index > 2:
                    "The Danger Room has been powered off for the night."
                elif round >= 30:
                    call training
                    call tenth_round
                    call set_the_scene
                else:
                    "There isn't time to do much before the next rotation."
            "Lock the door" if not door_locked:
                if time_index > 2:
                    "You lock the door."

                    $ door_locked = True
                else:
                    "You can't do that during free hours."
            "Unlock the door" if door_locked:
                "You unlock the door."

                $ door_locked = False
            "Wait" if time_index < 3:
                "You hang out for a bit."

                call tenth_round
                call set_the_scene
            "Leave":
                call world_map

label shower_entry:
    $ D20 = renpy.random.randint(1, 20)

    $ showering_Girls = []

    python:
        for G in active_Girls:
            if D20 < 5 and G not in Player.Party and (G.location == G.home or G.location == "bg_dangerroom"):
                showering_Girls.append(G)
            else:
                G.location = "nearby"

                Nearby.append(G)

        if showering_Girls:
            renpy.random.shuffle(showering_Girls)

    $ D20 = renpy.random.randint(1, 20)

    python:
        for G in showering_Girls:
            if G not in Player.Party:
                if D20 >= 10:
                    G.add_word(1, "showered", "showered", 0, 0)

                G.change_Outfit("shower")

            G.location = "bg_shower"

    call set_the_scene(location = "bg_shower", fade = True)

    if len(Player.Party) > 2:
        $ line = " and the girls"
    elif Player.Party:
        $ line = " and " + Player.Party[0].name
    else:
        $ line = ""

    if len(showering_Girls) > 2:
        "As you enter, you[line] see some others."
    elif len(showering_Girls) == 2:
        "As you enter, you[line] see [showering_Girls[0].name] and [showering_Girls[1].name]."
    elif showering_Girls:
        "As you enter, you[line] see [showering_Girls[0].name]."

    $ first = True
    $ someone_left = False

    $ temp_Girls = showering_Girls[:]

    while temp_Girls:
        call meeting_in_shower_lines(temp_Girls[0], approval = approval_check(temp_Girls[0], 900), first = first, someone_left = someone_left)

        if first:
            $ first = False

        if not approval:
            call remove_Girl(temp_Girls[0])

            if not someone_left:
                $ someone_left = True

        $ temp_Girls.remove(temp_Girls[0])

    return

label shower_room:
    if Player.traveling:
        $ Player.traveling = False

        $ door_locked = False

        $ Present = []
        $ Nearby = []

        call shower_entry

    if Player.location != "bg_shower":
        call set_the_scene(location = "bg_shower", fade = True)

    if round <= 10:
        if time_index == 3:
            "You're getting tired, you head back to your room."

            $ Player.traveling = True

            jump player_room

        call tenth_round
        call set_the_scene

    while True:
        show screen Girl_picker()

        menu:
            "You're in the showers. What would you like to do?"
            "Shower" if round >= 30:
                call showering
                call set_the_scene
            "Shower (locked)" if round < 30:
                pass
            "Wait" if time_index < 3:
                "You hang out for a bit."

                if round > 30:
                    "In the showers."
                    "Kinda weird."

                call tenth_round
                call set_the_scene

                python:
                    if renpy.random.randint(1, 20) < 5:
                        Nearby = []

                        for G in active_Girls:
                            if G.location != Player.location and (G.location == G.home or G.location == "bg_dangerroom"):
                                G.location = "nearby"

                                Nearby.append(G)
            "Leave":
                call world_map

label pool:
    $ door_locked = False

    if Player.traveling:
        $ Player.traveling = False

        $ Nearby = []

    call set_the_scene(location = "bg_pool", fade = True)

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.traveling = True

            jump player_room

        call tenth_round
        call set_the_scene

    while True:
        show screen Girl_picker()

        menu:
            "You're at the pool. What would you like to do?"
            "Want to swim?" if round >= 30:
                call check_who_is_present

                if time_index > 2 and not Present:
                    "It's a bit late for a swim."
                else:
                    call swim
            "Want to swim? (locked)" if round < 30:
                pass
            "Want to sunbathe?" if time_index < 2 and round >= 30:
                call sunbathe
            "Want to sunbathe? (locked)" if time_index > 1 or round < 30:
                pass
            "Want to skinnydip?" if round >= 30:
                call skinny_dip
            "Want to skinnydip? (locked)" if round < 30:
                pass
            "Wait" if time_index < 3:
                "You hang out for a bit."

                call tenth_round
                call set_the_scene
            "Leave":
                call world_map

label study_entry:
    while True:
        show screen Girl_picker()

        menu:
            "You're at the door, what do you do?"
            "Knock politely":
                $ decision = "knock"
            "Enter without knocking":
                if time_index > 2:
                    "The door is locked. It's not like you could just walk through it."
                else:
                    ch_x "You know, [Player.name], it is not polite to enter a room unannounced."

                    return
            "Use the key to enter" if time_index > 2 and "Xavier" in Player.Keys:
                "You use your key."
            "Leave":
                $ Player.traveling = True

                jump player_room

        if decision == "knock":
            if time_index > 2:
                "There's no answer, he's probably asleep."
            else:
                ch_x "Yes, enter. . ."

                "You enter the room."

                return

label study_room:
    if Player.traveling:
        $ Player.traveling = False

        $ door_locked = False

        $ Nearby = []

        call set_the_scene(location = "bg_door", fade = True)
        call study_entry

    if Player.location != "bg_study":
        $ door_locked = False

        call set_the_scene(location = "bg_study", fade = True)

        $ Xavier.change_face("happy")

    if round <= 10:
        if time_index > 2:
            "It's late, you head back to your room."

            $ Player.traveling = True

            jump player_room

        call tenth_round
        call set_the_scene

    while True:
        show screen Girl_picker()

        if time_index > 2:
            $ line = "You are in Xavier's study, but he isn't in at the moment. What would you like to do?"
        else:
            $ line = "You are in Xavier's study. What would you like to do?"

        menu:
            "[line]"
            "Wait":
                if time_index > 2:
                    "You probably don't want to be here when Xavier gets in."
                elif time_index == 2:
                    ch_x "If you don't mind, I would like to close up for the evening?"

                    $ Player.traveling = True

                    jump player_room
                else:
                    call tenth_round
                    call set_the_scene

                    ch_x "Not that I mind the company, but is there something I can do for you?"
            "Leave":
                call world_map

label mall:
    $ door_locked = False

    if Player.traveling:
        $ Player.traveling = False

        $ Nearby = []

        call set_the_scene(location = "bg_mall", fade = True)

        "You're at the Salem Centre Mall."
    else:
        call set_the_scene(location = "bg_mall")

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.traveling = True

            jump player_room

        call tenth_round
        call set_the_scene

    if len(Player.Party) > 1:
        "You wander the various stores with the girls, seeing what they have to offer. . ."
    elif Player.Party:
        "You wander the various stores with [Player.Party[0].name], seeing what they have to offer. . ."
    else:
        "You wander the various stores, seeing what they have to offer. . ."

    while True:
        if time_index > 2:
            ch_u "The mall is now closing, please head to the nearest exit. . ."

            $ Player.traveling = False

            jump campus

        show screen Girl_picker()

        menu:
            "Where would you like to go?"
            "Just wander and window shop" if Player.Party and round > 20:
                python:
                    if renpy.random.randint(1, 20) > 10:
                        for G in Player.Party:
                            G.change_stat("love", 80, 1)
                            G.change_stat("obedience", 50, 1)
                            G.change_stat("inhibition", 50, 1)

                if len(Player.Party) > 1:
                    "You wander around with the girls and see what they have available."
                elif Player.Party:
                    "You wander around with [Player.Party[0].name]and see what they have available."

                call tenth_round
                call set_the_scene
            "Head back to school":
                call world_map
