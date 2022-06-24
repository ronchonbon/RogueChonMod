label world_map:
    $ stack_depth = renpy.call_stack_depth()

    while True:
        menu:
            "Where would you like to go?"
            "My room" if Player.location != "bg_player":
                $ destination = "bg_player"
            "Girl's rooms":
                menu:
                    "[RogueX.name]'s room" if Player.location != "bg_rogue":
                        $ destination = RogueX
                    "[KittyX.name]'s room" if "met" in KittyX.history and Player.location != "bg_kitty":
                        $ destination = KittyX
                    "[EmmaX.name]'s room" if "met" in EmmaX.history and Player.location != "bg_emma":
                        $ destination = EmmaX
                    "[LauraX.name]'s room" if "met" in LauraX.history and Player.location != "bg_laura":
                        $ destination = LauraX
                    "[JeanX.name]'s room" if "met" in JeanX.history and Player.location != "bg_jean":
                        $ destination = JeanX
                    "[StormX.name]'s room" if "met" in StormX.history and Player.location != "bg_storm":
                        $ destination = StormX
                    "[JubesX.name]'s room" if "met" in JubesX.history and Player.location != "bg_jubes":
                        $ destination = JubesX
                    "Back":
                        pass
            "University Square" if Player.location != "bg_campus":
                call check_sunshock

                $ destination = "bg_campus"
            "Class" if Player.location != "bg_classroom":
                if time_index < 3:
                    $ destination = "bg_classroom"
                elif "Xavier" in Player.Keys:
                    "The door is locked, but you were able to use Xavier's key to get in."

                    $ destination = "bg_classroom"
                else:
                    "It's late for classes and the classrooms are locked down."

                    $ destination = None
            "The Danger Room" if Player.location != "bg_dangerroom":
                $ destination = "bg_dangerroom"
            "The showers" if Player.location != "bg_showerroom":
                $ destination = "bg_showerroom"
            "The pool" if Player.location != "bg_pool":
                call check_sunshock

                $ destination = "bg_pool"
            "Xavier's study" if Player.location != "bg_study":
                $ destination = "bg_study"
            "The mall" if time_index < 3 and Player.location != "bg_mall":#if "mall" in Player.history:
                call check_sunshock

                $ destination = "bg_mall"
            "The attic" if "attic" in Player.history and Player.location != "bg_storm":
                jump meet_Storm
            "Stay where I am.":
                return

        if destination:
            if Player.location == "bg_dangerroom":
                call exit_gym

            call hide_all

            $ Player.traveling = True

            if destination == "bg_player":
                jump player_room
            elif destination in all_Girls:
                $ Girl = destination

                jump girls_room
            elif destination == "bg_classroom":
                jump classroom
            elif destination == "bg_dangerroom":
                jump danger_room
            elif destination == "bg_showerroom":
                jump shower
            elif destination == "bg_pool":
                jump pool
            elif destination == "bg_study":
                jump study
            elif destination == "bg_mall":
                jump mall

label player_room:
    $ Player.location = "bg_player"

    $ door_locked = False

    call check_who_is_present
    call set_Character_taboos
    call set_the_scene(fade = True)

    if Player.traveling:
        $ Nearby = []

        call traveling_event_calls

        $ Player.traveling = False

    call quick_event_calls

    if round <= 10:
        call tenth_round
        call girls_location

    call event_calls

    while True:
        call are_girls_angry
        call set_Character_taboos

        menu:
            "You are in your room. What would you like to do?"
            "Chat":
                call chat
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
                call girls_location
                call event_calls
            "Wait" if time_index < 3:
                "You wait around a bit."

                call tenth_round
                call girls_location
                call event_calls
            "Special options":
                call SpecialMenu
            "Leave":
                call world_map

label girls_room_entry:
    $ D20 = renpy.random.randint(1, 20)

    if Girl in Player.Party:
        if time_index > 2 or (time_index == 2 and round <= 10):
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

                $ Girl.recent_history.append("no_entry")
                $ Girl.daily_history.append("no_entry")

                call remove_Girl(Girl)

                "She heads inside and closes the door behind her."

                jump reset_location
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

        return

    if round >= 10 and Girl.location == Girl.home and "lesbian" in Girl.recent_history:
        python:
            GirlB = None

            for G in active_Girls:
                if G.location == Girl.home and "lesbian" in G.recent_history:
                    GirlB = G

                    break

        if GirlB:
            call caught_lesbian(Girl, GirlB)

    if Girl == KittyX and "dress2" in LauraX.history and not Player.Party:
        call Laura_Dressup3

    if round >= 10 and Girl.location == Girl.home and "will_masturbate" in Girl.daily_history and D20 >= 5:
        call caught_masturbating(Girl)
    else:
        $ knocking = False

        if Girl in Player.Keys:
            menu:
                "You have a key, what do you do?"
                "Knock politely":
                    $ knocking = True
                "Use the key to enter.":
                    $ Player.location = Girl.home

                    call check_who_is_present
                    call set_Character_taboos
                    call set_the_scene(fade = True)

                    if Girl.location == Girl.home:
                        if round <= 10:
                            if time_index > 2:
                                "She's asleep in bed. You slip out quietly."

                                $ Player.location = "bg_campus"

                                jump reset_location
                        elif "will_masturbate" in Girl.daily_history and D20 >= 5:
                            $ girl_secondary_action = "fondle_pussy"
                            $ second_girl_secondary_action = "fondle_breasts"

                            $ Girl.daily_history.append("unseen")
                            $ Girl.recent_history.append("unseen")

                            $ Girl.drain_word("no_masturbation")
                            $ Girl.recent_history.append("masturbation")
                            $ Girl.daily_history.append("masturbation")

                            "You see [Girl.name] laying back on her bed with her eyes closed, fingers tracing circles around her clit."

                            call masturbation_cycle(Girl)
                        elif D20 >= 15 and (time_index > 2 or time_index == 0):
                            call caught_changing(Girl)

        if Girl not in Player.Keys or knocking:
            "You knock on [Girl.name]'s door."

            if Girl.location == Girl.home:
                if round <= 10:
                    if time_index > 2: #night time
                        "There's no answer, she's probably asleep."

                        jump reset_location
                if (D20 >= 19 and Girl.lust >= 50) or (D20 >=15 and Girl.lust >= 70) or (D20 >=10 and Girl.lust >= 80):
                    "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                    "After several seconds and some more shuffling of clothing, [Girl.name] comes to the door."

                    $ Girl.change_face("perplexed",2)

                    call add_Girl(Girl)

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

                    $ Girl.change_face("perplexed", 1)

                    $ approval_bonus += 10
                elif D20 >= 15 and (time_index > 2 or time_index == 0):
                    "You hear the rustling of fabric and some knocking around, but after a few seconds [Girl.name] comes to the door."

                    call add_Girl(Girl)

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
                elif "_angry" in Girl.recent_history:
                    $ Girl.change_face("_angry")

                    call get_out_lines(Girl)
                    jump reset_location
                else:
                    call add_Girl(Girl)

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

                            jump reset_location

        if time_index > 2 and "no_entry" in Girl.recent_history:
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

            jump reset_location
        elif "no_entry" in Girl.recent_history or "_angry" in Girl.recent_history:
            $ Girl.change_face("_angry")

            call get_out_lines(Girl)
            jump reset_location
        elif time_index > 2 and (Girl.event_counter["sleepover"] or Girl.SEXP >= 30 or Girl == JubesX):
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
        elif time_index > 2 and (approval_check(Girl, 1000, "LI") or approval_check(Girl, 600, "OI") or Girl == JubesX):
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
        elif time_index > 2 and (approval_check(Girl, 500, "LI") or approval_check(Girl, 300, "OI")):
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

            $ Girl.recent_history.append("no_entry")
            $ Girl.daily_history.append("no_entry")

            jump reset_location
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

            $ Girl.recent_history.append("no_entry")
            $ Girl.daily_history.append("no_entry")

            jump reset_location

    if Girl.location == "bg_entry":
        $ Girl.location = Girl.home

    return

label girls_room:
    if Player.traveling:
        $ Player.location = "bg_entry"

        $ door_locked = False

        call check_who_is_present
        call set_Character_taboos
        call set_the_scene(fade = True)

        $ Nearby = []

        call girls_room_entry
        call traveling_event_calls

        $ Player.traveling = False

    if Player.location != Girl.home:
        $ Player.location = Girl.home

        $ door_locked = False

        call check_who_is_present
        call set_Character_taboos
        call set_the_scene(fade = True)

    call quick_event_calls

    if round <= 10:
        call tenth_round
        call girls_location

    call event_calls

    while True:
        call are_girls_angry
        call set_Character_taboos

        if Girl.location == Player.location:
            "You are in [Girl.name]'s room. What would you like to do?"
        else:
            "You are in [Girl.name]'s room, but she isn't here. What would you like to do?"

        menu:
            extend ""
            "Chat":
                call chat
            "Would you like to study?":
                call study
            "Lock the door" if not door_locked:
                if Girl.location == Player.location and not approval_check(Girl, 1000, Alt = [[LauraX, JeanX], 1200]):
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
                call girls_location
                call event_calls
            "Wait" if time_index < 3:
                "You wait around a bit."

                call tenth_round
                call girls_location
                call event_calls
            "Leave":
                call world_map

label campus:
    $ Player.location = "bg_campus"

    $ door_locked = False

    call check_who_is_present
    call set_Character_taboos
    call set_the_scene(fade = True)

    if Player.traveling:
        $ Nearby = []

        call traveling_event_calls

        $ Player.traveling = False

    call quick_event_calls

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            jump player_room

        call tenth_round
        call girls_location

    call event_calls

    while True:
        call are_girls_angry
        call set_Character_taboos

        menu:
            "You are in the university square. What would you like to do?"
            "Chat":
                call chat
            "Wait" if time_index < 3:
                "You wait around a bit."

                call tenth_round
                call girls_location
                call event_calls
            "Leave":
                call world_map

label classroom:
    if Player.traveling:
        $ Player.location = "bg_classroom"

        $ door_locked = False

        call check_who_is_present
        call set_Character_taboos

        $ Nearby = []

        call traveling_event_calls

        if time_index < 2 and weekday < 5:
            call classroom_seating

        $ Player.traveling = False
    else:
        $ Player.location = "bg_classroom"

        $ door_locked = False

        call check_who_is_present
        call set_Character_taboos
        call set_the_scene(fade = True)

    call quick_event_calls

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.location = "bg_player"

            jump reset_location

        call tenth_round
        call girls_location

    call event_calls

    while True:
        call are_girls_angry
        call set_Character_taboos

        menu:
            "What would you like to do?"
            "Take the morning class" if weekday < 5 and time_index == 0:
                if round >= 30:
                    call take_class
                else:
                    "Class is already letting out. You can hang out until the next one."
            "Take the afternoon class" if weekday < 5 and time_index == 1:
                if round >= 30:
                    call take_class
                else:
                    "Class is already letting out. You can hang out until they lock up for the night."
            "Chat":
                call chat
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
                call girls_location
                call event_calls

                if time_index < 2:
                    "A new class is in session. What would you like to do?"
                else:
                    "Classes have let out for the day. What would you like to do?"
            "Leave":
                call world_map

label danger_room_entry:
    $ number_of_girls = 0

    $ temp_Girls = Player.Party[:]

    while temp_Girls:
        if temp_Girls[0].outfit_name != "gym_clothes":
            if approval_check(temp_Girls[0], 1300, "LO") or "passive" in temp_Girls[0].traits:
                $ approval_passed = True
            elif approval_check(temp_Girls[0], 800, "LO") and temp_Girls[0].first_custom_outfit["outfit_active"]:
                $ approval_passed = True
            elif approval_check(temp_Girls[0], 600, "LO") and temp_Girls[0].gym_clothes["outfit_active"] != 1:
                $ approval_passed = True
            else:
                $ approval_passed = False

            if not approval_passed or "asked gym" in temp_Girls[0].daily_history or "no_ask gym" in temp_Girls[0].traits:
                if number_of_girls:
                    if temp_Girls[0] == EmmaX:
                        $ line = "I should change too."
                    elif temp_Girls[0] == LauraX:
                        $ line = "I'll be right back. . ."
                    elif temp_Girls[0] == StormX:
                        $ line = "I should change as well. . ."
                    else:
                        $ line = "I'll be right back too."
                else:
                    $ line = "I'll be back soon, gotta change."

                temp_Girls[0].voice "[line]"

                $ temp_Girls[0].outfit_name = "gym_clothes"

                $ number_of_girls += 1
            else:
                $ temp_Girls[0].daily_history.append("asked gym")

                if number_of_girls:
                    if temp_Girls[0] == EmmaX:
                        $ line = "Do you think I should change as well?"
                    elif temp_Girls[0] == LauraX:
                        $ line = "Did you want me to change into my gym clothes?"
                    elif temp_Girls[0] == StormX:
                        $ line = "Do you think I should change as well?"
                    else:
                        $ line = "Should I change too?"
                else:
                    if temp_Girls[0] == EmmaX:
                        $ line = "Did you want me to change into my gear?"
                    elif temp_Girls[0] == LauraX:
                        $ line = "Did you want me to change into my gym clothes?"
                    elif temp_Girls[0] == StormX:
                        $ line = "Do you think I should change into my gym clothes?"
                    else:
                        $ line = "Would you like me to change into my gym clothes?"

                temp_Girls[0].voice "[line]"

                menu:
                    extend ""
                    "Yeah, they look great.":
                        $ G.change_face("_smile")
                        $ G.change_stat("love", 80, 2)
                        $ G.change_stat("obedience", 40, 1)
                        $ G.change_stat("inhibition", 30, 1)

                        $ change = 1
                    "No, stay in that.":
                        $ G.change_face("_confused")
                        $ G.change_stat("obedience", 50, 5)

                        $ change = 0
                    "Whichever you like.":
                        $ G.change_face("_confused")
                        $ G.change_stat("inhibition", 50, 1)

                        $ change =  renpy.random.randint(0, 3)
                    "I don't care.":
                        $ G.change_face("_angry")
                        $ G.change_stat("love", 50, -3, 1)
                        $ G.change_stat("obedience", 50, 4)
                        $ G.change_stat("inhibition", 50, 2)

                        $ change = renpy.random.randint(0, 1)

                if change:
                    if temp_Girls[0] == RogueX:
                        $ line = "Ok, be right back."
                    elif temp_Girls[0] == KittyX:
                        $ line = "Ok, back in a bit."
                    elif temp_Girls[0] == EmmaX:
                        $ line = "Fine, I'll be right back."
                    elif temp_Girls[0] == LauraX:
                        $ line = "I'll be right back then."
                    elif temp_Girls[0] == StormX:
                        $ line = "Then I will return shortly."
                    elif temp_Girls[0] == JubesX:
                        $ line = "K, be right back."

                    temp_Girls[0].voice "[line]"

                    $ temp_Girls[0].outfit_name = "gym_clothes"

                    $ number_of_girls += 1

        $ temp_Girls.remove(temp_Girls[0])

    if number_of_girls:
        show black_screen onlayer black

        python:
            for G in Player.Party:
                G.change_outfit()

        hide black_screen onlayer black

    return

label danger_room:
    $ Player.location = "bg_dangerroom"

    $ door_locked = False

    call check_who_is_present
    call set_Character_taboos
    call set_the_scene(fade = True)

    if Player.traveling:
        $ Nearby = []

        call danger_room_entry
        call traveling_event_calls

        $ Player.traveling = False

    call quick_event_calls

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.location = "bg_player"

            jump reset_location

        call tenth_round
        call girls_location

    call event_calls

    while True:
        call are_girls_angry
        call set_Character_taboos

        menu:
            "This is the Danger Room. What would you like to do?"
            "Train":
                if time_index > 2:
                    "The Danger Room has been powered off for the night, maybe take a break."
                elif round >= 30:
                    call training
                else:
                    "There really isn't time to do much before the next rotation, maybe wait a bit."
            "Chat":
                call chat
            "Lock the door" if not door_locked:
                if time_index > 2:
                    "You lock the door."

                    $ door_locked = True
                else:
                    "You can't really do that during free hours."
            "Unlock the door" if door_locked:
                "You unlock the door."

                $ door_locked = False
            "Wait" if time_index < 3:
                "You hang out for a bit."

                call tenth_round
                call girls_location
                call event_calls
            "Leave":
                call world_map

label shower_entry:
    $ D20 = renpy.random.randint(1, 20)

    $ showering_Girls = []

    python:
        for G in active_Girls:
            if D20 < 5 and G not in Player.Party and "showered" not in G.daily_history and (G.location == G.home or G.location == "bg_dangerroom"):
                showering_Girls.append(G)
            else:
                G.location = "nearby"

                Nearby.append(G)

        if showering_Girls:
            renpy.random.shuffle(showering_Girls)

    $ D20 = renpy.random.randint(1, 20)

    if not Player.Party and showering_Girls:
        if D20 > 15:
            call caught_showering(showering_Girls[0])
        elif D20 > 13:
            $ showering_Girls[0].add_word(1,"showered","showered", 0, 0)

            $ Player.location = "bg_showerroom"

            call check_who_is_present
            call set_Character_taboos
            call set_the_scene(fade = True)

            call caught_changing(showering_Girls[0])

    python:
        for G in showering_Girls:
            if G not in Player.Party:
                if D20 >= 10:
                    G.add_word(1,"showered","showered", 0, 0)

                G.change_outfit("shower")

            G.location = "bg_showerroom"

    $ Player.location = "bg_showerroom"

    call set_the_scene(fade = True)

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
        $ approval = approval_check(temp_Girls[0], 900)

        call meeting_in_shower_lines(temp_Girls[0], approval = approval, first = first, someone_left = someone_left)

        if first:
            $ first = False

        if not approval:
            call remove_Girl(temp_Girls[0])

            if not someone_left:
                $ someone_left = True

        $ temp_Girls.remove(temp_Girls[0])

    $ showering_Girls = temp_Girls[:]

    if len(showering_Girls) > 1:
        if RogueX in Player.Party:
            ch_r "Hey."

        if KittyX in Player.Party:
            ch_k "Hi."

        if EmmaX in Player.Party:
            ch_e "Oh, hello."

        if LauraX in Player.Party:
            ch_l "Hey."

        if JeanX in Player.Party:
            ch_j "Yeah, hey."

        if StormX in Player.Party:
            ch_s "Hello."

        if JubesX in Player.Party:
            ch_v "Hey."
    elif showering_Girls:
        if RogueX in Player.Party:
            ch_r "Hey, [showering_Girls[0].name]."

        if KittyX in Player.Party:
            ch_k "Hi, [showering_Girls[0].name]."

        if EmmaX in Player.Party:
            ch_e "Oh, hello, [showering_Girls[0].name]."

        if LauraX in Player.Party:
            ch_l "Hey."

        if JeanX in Player.Party:
            ch_j "Yeah, hey."

        if StormX in Player.Party:
            ch_s "Hello, [showering_Girls[0].name]."

        if JubesX in Player.Party:
            ch_v "Hey, [showering_Girls[0].name]."

label shower_room:
    if Player.traveling:
        $ Player.location = "bg_entry"

        $ door_locked = False

        call check_who_is_present
        call set_Character_taboos
        call set_the_scene(fade = True)

        $ Present = []
        $ Nearby = []

        call traveling_event_calls

        if round > 10:
            call shower_entry

        $ Player.traveling = False

    if Player.location != "bg_showerroom":
        $ Player.location = "bg_showerroom"

        $ door_locked = False

        call check_who_is_present
        call set_Character_taboos
        call set_the_scene(fade = True)

    call quick_event_calls

    if round <= 10:
        if time_index == 3:
            "You're getting tired, you head back to your room."

            jump player_room

        call tenth_round
        call girls_location

    call event_calls

    while True:
        call are_girls_angry
        call set_Character_taboos

        menu:
            "You're in the showers. What would you like to do?"
            "Shower" if round >= 30:
                call showering
            "Shower (locked)" if round < 30:
                call showering
            "Chat":
                call chat
            "Wait" if time_index < 3:
                "You hang out for a bit."

                if round > 30:
                    "In the showers."
                    "Not gonna lie, kinda weird."

                call tenth_round
                call girls_location
                call event_calls

                python:
                    if renpy.random.randint(1, 20) < 5:
                        Nearby = []

                        for G in active_Girls:
                            if G.location != Player.location and "showered" not in G.daily_history and (G.location == G.home or G.location == "bg_dangerroom"):
                                Nearby.append(G)

                                G.location = "nearby"
            "Leave":
                call world_map

label pool:
    $ Player.location = "bg_pool"

    $ door_locked = False

    call check_who_is_present
    call set_Character_taboos
    call set_the_scene(fade = True)

    if Player.traveling:
        $ Nearby = []

        call traveling_event_calls

        $ Player.traveling = False

    call quick_event_calls

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            jump player_room

        call tenth_round
        call girls_location

    call event_calls

    while True:
        call are_girls_angry
        call set_Character_taboos

        menu:
            "You're at the pool. What would you like to do?"
            "Chat":
                call chat
            "Want to sunbathe?" if time_index < 2 and round >= 30:
                call Pool_Sunbathe

                "You just hang out for a little while."
            "Want to sunbathe? (locked)" if round < 30:
                pass
            "Want to swim?" if round >= 30:
                if time_index > 2 and AloneCheck(focused_Girl):
                    "It's a bit late for a swim."
                else:
                    call Pool_Swim
            "Want to swim? (locked)" if round < 30:
                pass
            "Want to skinnydip?" if round >= 30:
                call Pool_Skinnydip
            "Want to skinnydip? (locked)" if round < 30:
                pass
            "Wait" if time_index < 3:
                "You hang out for a bit."

                call tenth_round
                call girls_location
                call event_calls
            "Leave":
                call world_map

label study_entry:
    $ decision = None

    while True:
        $ decision = None

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
            "Ask [KittyX.name]" if time_index > 2 and KittyX in Player.Party:
                $ decision = KittyX
            "Ask [StormX.name]" if time_index > 2 and StormX in Player.Party:
                $ decision = StormX
            "Leave":
                jump reset_location

        if decision == "knock":
            if time_index > 2:
                "There's no answer, he's probably asleep."
            else:
                ch_x "Yes, enter. . ."

                "You enter the room."

                return
        elif decision == KittyX:
            ch_k "Yeah?"

            $ talking_to_Kitty = True

            while talking_to_Kitty:
                menu:
                    extend ""
                    "Could you phase through the door and open it for me?":
                        if "Sneakthief" in KittyX.traits:
                            ch_k "No problem. . ."

                            return
                        elif "no_thief" in KittyX.recent_history:
                            ch_k "I told you, no."
                        elif approval_check(KittyX, 400, "I") or approval_check(KittyX, 1400):
                            $ KittyX.change_stat("love", 90, 3)
                            $ KittyX.change_stat("obedience", 50, 10)
                            $ KittyX.change_stat("inhibition", 60, 10)

                            ch_k "Heh, you have a wicked mind. . ."

                            $ KittyX.traits.append("Sneakthief")

                            return
                        else:
                            $ KittyX.change_stat("love", 90, -3)
                            $ KittyX.change_stat("obedience", 50, 2)
                            $ KittyX.change_stat("inhibition", 60, 2)

                            ch_k "Um, I don't really feel comfortable doing that. . ."

                            $ KittyX.recent_history.append("no_thief")
                    "Open the door.":
                        if "Sneakthief" in KittyX.traits:
                            ch_k "No problem. . ."

                            return
                        elif "no_thief" in KittyX.recent_history:
                            ch_k "I told you, no."
                        elif approval_check(KittyX, 500, "O") or approval_check(KittyX, 1600):
                            $ KittyX.change_stat("obedience", 50, 15)
                            $ KittyX.change_stat("inhibition", 60, 10)

                            ch_k "Heh, if you say so. . ."

                            $ KittyX.traits.append("Sneakthief")

                            return
                        else:
                            $ KittyX.change_stat("love", 90, -5)
                            $ KittyX.change_stat("obedience", 50, 2)
                            $ KittyX.change_stat("inhibition", 60, 2)

                            ch_k "Um, no."

                            $ KittyX.recent_history.append("no_thief")
                    "Never mind.":
                        $ talking_to_Kitty = False
        elif decision == StormX:
            ch_s "What is it?"

            $ talking_to_Storm = True

            while talking_to_Storm:
                menu:
                    extend ""
                    "Do you think you could pick that lock?" if "Sneakthief" not in StormX.traits:
                        if "no_thief" in StormX.recent_history:
                            ch_s "I told you, I won't do that."
                        elif approval_check(StormX, 400, "I") or approval_check(StormX, 1400):
                            $ StormX.change_stat("love", 90, 3)
                            $ StormX.change_stat("obedience", 80, 10)
                            $ StormX.change_stat("inhibition", 60, 10)
                            $ StormX.change_face("_sly")

                            ch_s "Oh, this should be interesting. . ."
                            "She pulls some picks from behind her ear."
                            ch_s "Ok, we've got a click on 1. . . 2 is binding. . ."
                            ch_s "Click on 3. . . 4. . . click on 5, back to 2. . . and we're in."

                            $ StormX.traits.append("Sneakthief")
                            $ StormX.change_face("_normal")

                            return
                        else:
                            $ StormX.change_stat("love", 90, -3)
                            $ StormX.change_stat("obedience", 50, 2)
                            $ StormX.change_stat("inhibition", 60, 2)

                            ch_s "I don't think that's really appropriate behavior. . ."

                            $ StormX.recent_history.append("no_thief")
                    "Could you pick the lock again?" if "Sneakthief" in StormX.traits:
                        ch_s "No problem. . ."

                        return
                    "Never mind.":
                        $ talking_to_Storm = False

label study_room:
    if Player.traveling:
        $ Player.location = "bg_entry"

        $ door_locked = False

        call check_who_is_present
        call set_Character_taboos
        call set_the_scene(fade = True)

        $ Nearby = []

        call study_entry
        call traveling_event_calls

        $ Player.traveling = False

    if Player.location != "bg_study":
        $ Player.location = "bg_study"

        $ door_locked = False

        call check_who_is_present
        call set_Character_taboos
        call change_Xavier_face("_happy")
        call set_the_scene(fade = True)

    call quick_event_calls

    if round <= 10:
        if time_index > 2:
            "It's late, you head back to your room."

            jump player_room

        call tenth_round
        call girls_location

    call event_calls

    while True:
        call are_girls_angry
        call set_Character_taboos

        if time_index > 2:
            "You are in Xavier's study, but he isn't in at the moment. What would you like to do?"
        else:
            "You are in Xavier's study. What would you like to do?"

        menu:
            extend ""
            "Chat" if time_index > 2:
                call chat
            "Plan Omega!" if time_index < 3 and RogueX.location == Player.location and Player.level >= 5:
                if approval_check(RogueX, 1500, taboo_modifier=1, Loc="No"):
                    call execute_plan(RogueX)
                else:
                    ch_r "I don't want to do that. . ."
            "Plan Kappa!" if time_index < 3 and KittyX.location == Player.location and Player.level >= 5:
                if "Xavier's photo" in Player.inventory and approval_check(KittyX, 1500, taboo_modifier=1, Loc="No"):
                    call execute_plan(KittyX)
                elif "Xavier's photo" in Player.inventory:
                    ch_k "I don't really want to do that. . ."
                else:
                    ch_k "What?"
            "Plan Psi!" if time_index < 3 and EmmaX.location == Player.location and Player.level >= 5:
                if approval_check(EmmaX, 1500, taboo_modifier=1, Loc="No"):
                    call execute_plan(EmmaX)
                else:
                    ch_e "I'd rather not. . ."
            "Plan Chi!" if time_index < 3 and LauraX.location == Player.location and Player.level >= 5:
                if LauraX.level >= 2 and approval_check(LauraX, 1500, taboo_modifier=1, Loc="No") and approval_check(LauraX, 750, "I"):
                    call execute_plan(LauraX)
                elif LauraX.level < 2 or not approval_check(LauraX, 750, "I"):
                    ch_l "I'm not ready for that."
                else:
                    ch_l "Huh?"
            "Plan Alpha!" if time_index < 3 and JeanX.location == Player.location and Player.level >= 5:
                if approval_check(JeanX, 1500, taboo_modifier=1, Loc="No"):
                    call execute_plan(JeanX)
                else:
                    ch_j "You're on your own there."
            "Plan Rho!" if time_index < 3 and StormX.location == Player.location and Player.level >= 5:
                if "Xavier's files" in Player.inventory and approval_check(StormX, 1500, taboo_modifier=1, Loc="No"):
                    call execute_plan(StormX)
                elif "Xavier's files" in Player.inventory:
                    ch_s "I do not believe that would be approrpriate."
                else:
                    ch_s "What is that?"
            "Plan Zeta!" if time_index < 3 and JubesX.location == Player.location and Player.level >= 5:
                if approval_check(JubesX, 1500, taboo_modifier=1, Loc="No"):
                    call execute_plan(JubesX)
                else:
                    ch_v "What's a \"Zeta?\""
            "Explore" if time_index > 2 and "explore" not in Player.recent_history:
                $ counter = 0

                $ Player.recent_history.append("explore")

                call study_Explore
            "Wait":
                if time_index > 2:
                    "You probably don't want to be here when Xavier gets in."
                elif time_index == 2:
                    ch_x "If you don't mind, I would like to close up for the evening?"

                    $ Player.location = "bg_campus"

                    jump reset_location
                else:
                    call tenth_round
                    call girls_location
                    call event_calls

                    ch_x "Not that I mind the company, but is there something I can do for you?"
            "Leave":
                call world_map

label mall_entry:
    call check_sunshock

    $ Nearby = []

    $ Player.location = "bg_mall"

    $ door_locked = False

    call set_the_scene
    call set_Character_taboos
    call event_calls

label mall:
    $ Player.location = "bg_mall"

    $ door_locked = False

    call check_who_is_present
    call set_Character_taboos
    call set_the_scene(fade = True)

    if Player.traveling:
        $ Nearby = []

        call traveling_event_calls

        $ Player.traveling = False

    call quick_event_calls

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            jump player_room

        call tenth_round
        call girls_location

    call event_calls

    "You're at the Salem Centre Mall."

    if len(Player.Party) > 1:
        "You wander the various stores with the girls, seeing what they have to offer. . ."
    elif Player.Party:
        "You wander the various stores with [Player.Party[0].name], seeing what they have to offer. . ."
    else:
        "You wander the various stores, seeing what they have to offer. . ."

    while True:
        call are_girls_angry
        call set_Character_taboos

        if time_index > 2:
            if "date" in Player.recent_history:
                "It's getting late, you head back to the dorms. . ."

                jump Date_End

            ch_u "The mall is now closing, please head to the nearest exit. . ."

            $ Player.location = "bg_campus"

            jump reset_location

        menu:
            "Where would you like to go?"
            "Enter clothing shop" if round > 20:
                call clothing_shop
            "Enter swimwear shop" if round > 20:
                call swimsuit_shop
            "Enter lingerie shop" if round > 20:
                call lingerie_shop
            "Enter the sex shop" if round > 20:
                call sex_shop
            "Wait around a bit" if "date" not in Player.recent_history:
                "You wait around a bit."

                call tenth_round
                call girls_location
                call event_calls
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
                call girls_location
                call event_calls
            "Do something else" if "date" in Player.recent_history and round > 20:
                jump Date_Location
            "Head back to school" if "date" in Player.recent_history:
                if "movie" in Player.recent_history or "dinner" in Player.recent_history or round < 30 or not Player.Party:
                    "It's getting late, you head back to the dorms. . ."

                    jump Date_End
                else:
                    if Player.Party[0] in [EmmaX, StormX]:
                        Player.Party[0].voice "Oh, I was expecting more. . ."
                    elif Player.Party[0] in [JeanX, LauraX]:
                        Player.Party[0].voice "Is that it?"
                    else:
                        Player.Party[0].voice "Aw. . . we aren't doing anything else?"

                    menu:
                        "Continue shopping":
                            pass
                        "Do something else":
                            jump Date_Location
                        "Head back to school [[seriously this time]":
                            ch_p "Yeah, let's head back."

                            Player.Party[0].voice "Fine. . ."

                            "It's getting late, you head back to the dorms. . ."

                            jump Date_End
            "Head back to school" if "date" not in Player.recent_history:
                call world_map

label reset_location:
    $ door_locked = False

    $ stack_depth = renpy.call_stack_depth()

    while stack_depth > 0:
        $ stack_depth -= 1

        $ renpy.pop_call()

    if Player.location == "bg_player":
        jump player_room
    elif Player.location == "bg_rogue":
        $ Girl = RogueX

        jump girls_room
    elif Player.location == "bg_kitty":
        $ Girl = KittyX

        jump girls_room
    elif Player.location == "bg_emma":
        $ Girl = EmmaX

        jump girls_room
    elif Player.location == "bg_laura":
        $ Girl = LauraX

        jump girls_room
    elif Player.location == "bg_jean":
        $ Girl = JeanX

        jump girls_room
    elif Player.location == "bg_storm":
        $ Girl = StormX

        jump girls_room
    elif Player.location == "bg_jubes":
        $ Girl = JubesX

        jump girls_room
    elif Player.location == "bg_dangerroom":
        jump danger_room
    elif Player.location == "bg_classroom":
        jump classroom
    elif Player.location == "bg_showerroom":
        jump shower_room
    elif Player.location == "bg_study":
        jump study_room
    elif Player.location == "bg_pool":
        jump pool
    elif Player.location in ["bg_mall", "bg_shop", "bg_dressing"]:
        jump mall
    else:
        $ Player.traveling = True

        jump campus
