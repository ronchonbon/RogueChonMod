label world_map:
    $ stack_depth = renpy.call_stack_depth()

    $ taboo = 0

    $ bg_current = "bg_campus"

    call set_the_scene(silent = True)

    while True:
        menu world_map_menu:
            "Where would you like to go?"
            "My room":# if bg_current != "bg_player":
                jump player_room_entry
            "Girl's rooms":
                menu:
                    "[RogueX.name]'s room":# if bg_current != "bg_rogue":
                        $ Girl = RogueX

                        jump girls_room_entry
                    "[KittyX.name]'s room" if "met" in KittyX.history:# and bg_current != "bg_kitty":
                        $ Girl = KittyX

                        jump girls_room_entry
                    "[EmmaX.name]'s room" if "met" in EmmaX.history:# and bg_current != "bg_emma":
                        $ Girl = EmmaX

                        jump girls_room_entry
                    "[LauraX.name]'s room" if "met" in LauraX.history:# and bg_current != "bg_laura":
                        $ Girl = LauraX

                        jump girls_room_entry
                    "[JeanX.name]'s room" if "met" in JeanX.history:# and bg_current != "bg_jean":
                        $ Girl = JeanX

                        jump girls_room_entry
                    "[StormX.name]'s room" if "met" in StormX.history:# and bg_current != "bg_storm":
                        $ Girl = StormX

                        jump girls_room_entry
                    "[JubesX.name]'s room" if "met" in JubesX.history:# and bg_current != "bg_jubes":
                        $ Girl = JubesX

                        jump girls_room_entry
                    "Back":
                        pass
            "University Square":# if bg_current != "bg_campus":
                jump campus_entry
            "Class":# if bg_current != "bg_classroom":
                if time_index < 3:
                    jump classroom_entry
                elif "Xavier" in keys:
                    "The door is locked, but you were able to use Xavier's key to get in."

                    jump classroom_entry
                else:
                    "It's late for classes and the classrooms are locked down."

                    jump world_map
            "The Danger Room":# if bg_current != "bg_dangerroom":
                jump danger_room_entry
            "The showers":# if bg_current != "bg_showerroom":
                jump shower_entry
            "The pool":# if bg_current != "bg_pool":
                jump pool_entry
            "Xavier's study":# if bg_current != "bg_study":
                jump study_entry
            "Go to the mall" if "mall" in Player.history and time_index < 3:# and bg_current != "bg_mall":
                jump Mall_entry
            "Attic" if "attic" in Player.history:# and bg_current != "bg_storm":
                jump StormMeet
            "Stay where I am.":
                return

label player_room_entry:
    $ stack_depth = renpy.call_stack_depth()

    while stack_depth > 0:
        $ stack_depth -= 1

        $ renpy.pop_call()

    $ Player.recent_history.append("traveling")

    $ Nearby = []

    call set_the_scene(character = False)
    call taboo_level
    call event_calls

label player_room:
    $ Player.drain_word("traveling", 1, 0)

    $ bg_current = "bg_player"

    $ door_locked = False

    call set_the_scene(silent = True)
    call taboo_level
    call quick_event
    call event_calls

    if round <= 10:
        call tenth_round
        call girls_location
        call event_calls

    call are_girls_angry

    while True:
        $ bg_current = "bg_player"

        menu:
            "You are in your room. What would you like to do?"
            "Chat":
                call chat
            "Study":
                call study
            "Lock the door" if not door_locked:
                "You lock the door."

                $ door_locked = True

                call taboo_level
            "Unlock the door" if door_locked:
                "You unlock the door."

                $ door_locked = False

                call taboo_level
            "Sleep" if time_index >= 3: #night time
                call tenth_round
                call girls_location
                call event_calls
            "Wait" if time_index < 3: #not night time
                "You wait around a bit."

                if round > 10:
                    call wait
                else:
                    call tenth_round

                call girls_location
                call event_calls
            "Shop":
                call shop
            "Special Options":
                call SpecialMenu
            "Leave":
                call world_map

label girls_room_entry:
    $ Player.recent_history.append("traveling")

    $ Nearby = []

    $ bg_current = "bg_entry"

    $ door_locked = False

    call shift_focus(Girl)
    call set_the_scene(entering = True)
    call taboo_level

    $ D20 = renpy.random.randint(1, 20)

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

                $ Girl.recent_history.append("no_entry")
                $ Girl.daily_history.append("no_entry")

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
        jump girls_room

    if round >= 10 and Girl.location == bg_current and "lesbian" in Girl.recent_history:
        call Girls_Caught_Lesing(Girl)

        if not _return:
            jump girls_room

    if bg_current == KittyX.home and "dress2" in LauraX.history and not Party:
        call Laura_Dressup3

        return

    if round >= 10 and Girl.location == bg_current and "will_masturbate" in Girl.daily_history and D20 >= 5:
        call caught_masturbating(Girl)
    else:
        $ knocking = False

        if Girl in keys:
            menu:
                "You have a key, what do you do?"
                "Knock politely":
                    $ knocking = True
                "Use the key to enter.":
                    call set_the_scene

        if not knocking and Girl in keys:
            if Girl.location == bg_current:
                if round <= 10:        #add "no" condtion here
                    if time_index >= 3: #night time
                        "She's asleep in bed. You slip out quietly." #fix add options here.

                        return
                elif "will_masturbate" in Girl.daily_history and D20 >= 5:
                    call caught_masturbating(Girl)
                elif D20 >=15 and (time_index >= 3 or time_index == 0):
                    call Girl_Caught_Changing(Girl)
                    jump girls_room
        else:
            "You knock on [Girl.name]'s door."

            if Girl.location == bg_current:
                if round <= 10:
                    if time_index >= 3: #night time
                        "There's no answer, she's probably asleep."

                        jump reset_location
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

                    $ approval_bonus += 10
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
                elif "_angry" in Girl.recent_history:
                    $ Girl.change_face("_angry")

                    call get_out_lines(Girl)
                    jump reset_location
                else:
                    call set_the_scene

                    "[Girl.name] opens the door and leans out."
                    "You ask if you can come inside."

        if Girl.location != bg_current:
            "Looks like she's not home right now."

            if Girl in keys:
                menu:
                    "Go in and wait for her?"
                    "Yes":
                        jump girls_room
                    "No":
                        pass

            "You head back."

            jump reset_location
        elif time_index >= 3 and "no_entry" in Girl.recent_history:
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

    call event_calls

label girls_room:
    $ Player.drain_word("traveling", 1, 0)

    $ bg_current = Girl.home

    call set_the_scene(silent = True)
    call taboo_level
    call quick_event
    call event_calls

    if round <= 10:
        call tenth_round
        call girls_location
        call event_calls

    call are_girls_angry

    while True:
        $ bg_current = Girl.home

        if Girl.location == bg_current:
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
                    "You lock the door."

                    $ door_locked = True

                    call taboo_level
            "Unlock the door" if door_locked:
                "You unlock the door."

                $ door_locked = False

                call taboo_level
            "Sleep" if time_index >= 3: #night time
                call tenth_round
                call girls_location
                call event_calls
            "Wait" if time_index < 3: #not night time
                "You wait around a bit."

                if round > 10:
                    call wait
                else:
                    call tenth_round

                call girls_location
                call event_calls
            "Leave":
                call world_map

        if "_angry" in Girl.recent_history:
            $ Girl.change_face("_angry")

            call get_out_lines(Girl)

            $ bg_current = "bg_campus"

            jump reset_location

label campus_entry:
    call check_on_Jubes_sunshock

    $ Player.recent_history.append("traveling")

    $ Nearby = []

    $ bg_current = "bg_campus"

    $ door_locked = False

    call set_the_scene
    call taboo_level
    call event_calls

label campus:
    $ Player.drain_word("traveling", 1, 0)

    $ bg_current = "bg_campus"

    call set_the_scene(silent = True)
    call taboo_level
    call quick_event
    call event_calls

    if time_index == 2 and "going_on_date" in Player.daily_history:
        menu:
            "Ready to go on that date?"
            "Yes":
                call DateNight

                if "going_on_date" in Player.daily_history:
                    $ Player.daily_history.remove("going_on_date")
            "One moment. . .":
                pass

    if round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."

            jump player_room

        call tenth_round
        call girls_location
        call event_calls

    call are_girls_angry

    while True:
        $ bg_current = "bg_campus"

        menu:
            "You are in the university square. What would you like to do?"
            "Chat":
                call chat
            "Wait" if time_index < 3:
                "You wait around a bit."

                if round > 10:
                    call wait
                else:
                    call tenth_round

                call girls_location
                call event_calls
            "Leave":
                call world_map

label classroom_entry:
    $ Player.recent_history.append("traveling")

    $ Present = []
    $ Nearby = []

    $ bg_current = "bg_classroom"

    $ door_locked = False

    call set_the_scene(character = False)
    call taboo_level
    call event_calls

label classroom:
    $ bg_current = "bg_classroom"

    if "goto" in Player.recent_history or "traveling" in Player.recent_history:
        $ Present = []

        if time_index < 2 and weekday < 5:
            call classroom_seating

        $ Player.drain_word("goto",1,0)
        $ Player.drain_word("traveling",1,0)

    if EmmaX.location == "bg_teacher":
        "As you sit down, you see [EmmaX.name] at the podium."
    elif StormX.location == "bg_teacher":
        "As you sit down, you see [StormX.name] at the podium."
    elif time_index == 2 or weekday > 5:
        "You enter the classroom."

    call set_the_scene(silent = True)
    call taboo_level
    call quick_event
    call event_calls

    if round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."

            jump player_room

        call tenth_round
        call girls_location
        call event_calls

    call are_girls_angry

    while True:
        $ bg_current = "bg_classroom"

        menu:
            extend ""
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
                if weekday >=5 or time_index >= 2:
                    "You lock the door."

                    $ door_locked = True

                    call taboo_level
                else:
                    "You can't really do that during class."
            "Unlock the door" if door_locked:
                "You unlock the door."

                $ door_locked = False

                call taboo_level
            "Wait" if time_index < 3:
                "You hang out for a bit."

                if round > 10:
                    call wait
                else:
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
    $ Player.recent_history.append("traveling")

    $ Nearby = []

    $ bg_current = "bg_dangerroom"

    $ door_locked = False

    call set_the_scene
    call gym_entry
    call taboo_level
    call event_calls

label danger_room:
    $ bg_current = "bg_dangerroom"

    $ Player.drain_word("traveling", 1, 0)

    call set_the_scene(silent = True)
    call taboo_level
    call quick_event

    if round <= 10:
        "Looks like shifts are changing. . ."

        if time_index >=3:
            "You're getting tired, you head back to your room."

            $ bg_current = "bg_player"

            jump reset_location

        call tenth_round
        call girls_location
        call event_calls

    call are_girls_angry

    "This is the Danger Room. What would you like to do?"

    while True:
        $ bg_current = "bg_dangerroom"

        menu:
            extend ""
            "Train":
                if time_index >= 3:
                    "The Danger Room has been powered off for the night, maybe take a break."
                elif round >= 30:
                    call training
                else:
                    "There really isn't time to do much before the next rotation, maybe wait a bit."
            "Chat":
                call chat
            "Lock the door" if not door_locked:
                if time_index >= 3:
                    "You lock the door."

                    $ door_locked = True

                    call taboo_level
                else:
                    "You can't really do that during free hours."
            "Unlock the door" if door_locked:
                "You unlock the door."

                $ door_locked = False

                call taboo_level
            "Wait" if time_index < 3:
                "You hang out for a bit."

                if round > 10:
                    call wait
                else:
                    call tenth_round

                call girls_location
                call event_calls
            "Leave":
                call exit_gym
                call world_map

label gym_entry(number_of_girls = 0):
    # if taboo == 0:
    #     menu:
    #         "Is this visit for work or for play?"
    #         "Work [[get geared up]":
    #             pass
    #         "Play [[keep on this outfit]":
    #             return

    $ temp_Girls = Present[:]

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
                if temp_Girls[0] == EmmaX:
                    ch_e "I should change too."
                elif temp_Girls[0] == LauraX:
                    ch_l "I'll be right back. . ."
                elif temp_Girls[0] == StormX:
                    ch_s "I should change as well. . ."
                else:
                    if number_of_girls:
                        temp_Girls[0].voice "I'll be right back too."
                    else:
                        temp_Girls[0].voice "I'll be back soon, gotta change."

                $ temp_Girls[0].outfit_name = "gym_clothes"
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

                call gym_clothes_menu

                if _return:
                    if temp_Girls[0] == RogueX:
                        ch_r "Ok, be right back."
                    elif temp_Girls[0] == KittyX:
                        ch_k "Ok, back in a bit."
                    elif temp_Girls[0] == EmmaX:
                        ch_e "Fine, I'll be right back."
                    elif temp_Girls[0] == LauraX:
                        ch_l "I'll be right back then."
                    elif temp_Girls[0] == StormX:
                        ch_s "Then I will return shortly."
                    elif temp_Girls[0] == JubesX:
                        ch_v "K, be right back."

                    $ temp_Girls[0].outfit_name = "gym_clothes"

            show black_screen onlayer black

            $ temp_Girls[0].change_outfit()

            if temp_Girls[0].outfit_name == "gym_clothes":
                $ number_of_girls += 1

        $ temp_Girls.remove(temp_Girls[0])

    hide black_screen onlayer black

    return

label shower_entry:
    $ Nearby = []
    $ Present = []

    $ bg_current = "bg_entry"

    $ door_locked = False

    call set_the_scene (0, 1, 0)
    call taboo_level

    if round <= 10 or len(Party) >= 2:
        jump shower_room

    #if day >= 15 and "met" not in JeanX.history and "met" in EmmaX.history:
    if day >= 1 and "met" not in JeanX.history and "met" in EmmaX.history:
        call JeanMeet
        jump shower_room

    $ potential_Girls = []

    python:
        for G in active_Girls:
            if G not in Party and "showered" not in G.daily_history and (G.location == G.home or G.location == "bg_dangerroom"):
                potential_Girls.append(G)

    if potential_Girls:
        $ renpy.random.shuffle(potential_Girls)

    $ D20 = renpy.random.randint(1, 20)

    if D20 < 5 or (len(potential_Girls) + len(Party) > 2):
        while potential_Girls and (D20 < 5 or len(potential_Girls) + len(Party) > 2):
            $ Nearby.append(potential_Girls[0])

            $ potential_Girls[0].location = "nearby"

            $ potential_Girls.remove(potential_Girls[0])

    if not Party and potential_Girls and potential_Girls[0] in all_Girls:
        if D20 > 15:
            call caught_showering(potential_Girls[0])
            jump shower_room
        elif D20 > 13:
            $ potential_Girls[0].add_word(1,"showered","showered",0,0)

            $ bg_current = "bg_showerroom"

            call Girl_Caught_Changing(potential_Girls[0])
            jump shower_room

    $ bg_current = "bg_showerroom"

    python:
        for G in potential_Girls:
            G.location = bg_current

    call check_who_is_present(0)

    python:
        for G in potential_Girls:
            if G.location == bg_current and G not in Party:
                if D20 >= 10:
                    G.add_word(1,"showered","showered",0,0)

                G.change_outfit("shower")

    call set_the_scene(check_if_dressed = False)

    if Party:
        $ line = " and " + Party[0].name
    else:
        $ line = ""

    if len(potential_Girls) >= 2:
        "As you enter, you[line] see [potential_Girls[0].name] and [potential_Girls[1].name] standing there."
    elif potential_Girls:
        "As you enter, you[line] see [potential_Girls[0].name] standing there."

    if potential_Girls:
        if potential_Girls[0] == RogueX:
            ch_r "Hey, [RogueX.player_petname]."

            if "showered" in RogueX.recent_history:
                ch_r "I was just getting ready to head out."
            if not approval_check(potential_Girls[0], 900):
                ch_r "See ya later."
        if potential_Girls[0]  == KittyX:
            ch_k "Hey, [KittyX.player_petname]."

            if "showered" in KittyX.recent_history:
                ch_k "I just got finished."
            if not approval_check(potential_Girls[0], 900):
                ch_k "Oh, um, I should get out of your way. . ."
        if potential_Girls[0]  == EmmaX:
            ch_e "Oh, hello, [EmmaX.player_petname]."
            if "showered" in EmmaX.recent_history:
                ch_e "I was about finished here."
            if not approval_check(potential_Girls[0], 900):
                ch_e "I should get going."
        if potential_Girls[0]  == LauraX:
            ch_l "Oh, hey."

            if "showered" in LauraX.recent_history:
                ch_l "I'm done here."
            if not approval_check(potential_Girls[0], 900):
                ch_l "See you later."
        if potential_Girls[0]  == JeanX:
            ch_j "Oh, hey. . . you."

            if "showered" in JeanX.recent_history:
                ch_j "I'm wrapping up here."
            if not approval_check(potential_Girls[0], 900):
                ch_j "Later."
        if potential_Girls[0]  == StormX:
            ch_s "Oh, hello, [StormX.player_petname]."

            if "showered" in StormX.recent_history:
                ch_s "I was finishing up here."
            if not approval_check(potential_Girls[0], 600):
                ch_s "I am heading out at the moment."
        if potential_Girls[0]  == JubesX:
            ch_v "Yo, [JubesX.player_petname]."

            if "showered" in JubesX.recent_history:
                ch_v "I just finished up here."
            if not approval_check(potential_Girls[0], 900):
                ch_v "I should, uh, get going. . ."

        if len(potential_Girls) >= 2:
            if potential_Girls[1] == RogueX:
                if not approval_check(potential_Girls[0], 900) and not approval_check(potential_Girls[1], 900):
                    ch_r "Yeah, I'll see you too."
                elif not approval_check(potential_Girls[1], 900):

                    ch_r "Yeah, I should get going though."
                else:
                    ch_r "Yeah, hey."
            if potential_Girls[1] == KittyX:
                if not approval_check(potential_Girls[0], 900) and not approval_check(potential_Girls[1], 900):
                    ch_k "Yeah, see ya."
                elif not approval_check(potential_Girls[1], 900):
                    ch_k "Oh, well. . . I should get going."
                else:
                    ch_k "Yeah, hi."
            if potential_Girls[1] == EmmaX:
                if not approval_check(potential_Girls[0], 900) and not approval_check(potential_Girls[1], 900):
                    ch_e "Yes, I should also get going."
                elif not approval_check(potential_Girls[1], 900):
                    ch_e "You two look like you have some business. . ."
                else:
                    ch_e "Yes, hello."
            if potential_Girls[1] == LauraX:
                if not approval_check(potential_Girls[0], 900) and not approval_check(potential_Girls[1], 900):
                    ch_l "Yeah, I'm heading out too."
                elif not approval_check(potential_Girls[1], 900):
                    ch_l "I'll get out of your way."
                else:
                    ch_l "Hey."
            if potential_Girls[1] == JeanX:
                if not approval_check(potential_Girls[0], 900) and not approval_check(potential_Girls[1], 900):
                    ch_j "Yeah, I'm done too."
                elif not approval_check(potential_Girls[1], 900):
                    ch_j "I'm headed out."
                else:
                    ch_j "Hey."
            if potential_Girls[1] == StormX:
                if not approval_check(potential_Girls[0], 900) and not approval_check(potential_Girls[1], 600):
                    ch_s "Yes, I am also leaving."
                elif not approval_check(potential_Girls[1], 900):
                    ch_s "I wouldn't want to be a bother. . ."
                else:
                    ch_s "Yes, hello."
            if potential_Girls[1] == JubesX:
                if not approval_check(potential_Girls[0], 900) and not approval_check(potential_Girls[1], 900):
                    ch_v "Yeah, see ya."
                elif not approval_check(potential_Girls[1], 900):
                    ch_v "Oh, so. . . I should head out."
                else:
                    ch_v "Yeah, hey."

            if not approval_check(potential_Girls[1], 900):
                call remove_girl(potential_Girls[1])

        if not approval_check(potential_Girls[0], 900):
            call remove_girl(potential_Girls[0])

        if potential_Girls:
            if RogueX in Party:
                ch_r "Hey, [potential_Girls[0].name]."
            if KittyX in Party:
                ch_k "Hi, [potential_Girls[0].name]."
            if EmmaX in Party:
                ch_e "Oh, hello, [potential_Girls[0].name]."
            if LauraX in Party:
                ch_l "Hey."
            if JeanX in Party:
                ch_j "Yeah, hey."
            if StormX in Party:
                ch_s "Hello, [potential_Girls[0].name]."
            if JubesX in Party:
                ch_v "Hey, [potential_Girls[0].name]."

label shower_room:
    $ bg_current = "bg_showerroom"

    $ Player.drain_word("traveling", 1, 0)

    call set_the_scene(check_if_dressed = False)
    call taboo_level
    call quick_event

    if round <= 10:
        if time_index == 3:
            "You're getting tired, you head back to your room."

            jump player_room

        call tenth_round
        call event_calls
        call girls_location

    call are_girls_angry

    while True:
        $ bg_current = "bg_showerroom"

        menu:
            "You're in the showers. What would you like to do?"
            "Shower" if round > 30:
                call showering
            "Chat":
                call chat
            "Wait" if time_index < 3:
                "You hang out for a bit."

                if round > 30:
                    "In the showers."
                    "Not gonna lie, kinda weird."

                if round > 10:
                    call wait
                else:
                    call tenth_round

                call girls_location
                call event_calls

                if renpy.random.randint(1, 20) < 5:
                    $ Nearby = []
                    $ temp_Girls = active_Girls[:]

                    while temp_Girls:
                        if temp_Girls[0].location != bg_current and "showered" not in temp_Girls[0].daily_history and (temp_Girls[0].location == temp_Girls[0].home or temp_Girls[0].location == "bg_dangerroom"):
                            $ Nearby.append(line[0])

                        $ temp_Girls.remove(line[0])

                    if Nearby:
                        $ renpy.random.shuffle(Nearby)

                        while len(Nearby) > 2:
                            $ Nearby.remove(Nearby[0])

                        if len(Nearby) > 1:
                            $ Nearby[1].location = "nearby"

                        $ Nearby[0].location = "nearby"
            "Leave":
                call quick_event
                call change_out_of_towels
                call world_map

label pool_entry:
    call check_on_Jubes_sunshock

    $ Player.recent_history.append("traveling")

    $ Nearby = []

    $ bg_current = "bg_pool"

    $ door_locked = False

    call SwimSuit
    call set_the_scene
    call taboo_level
    call event_calls

label pool:
    $ Player.drain_word("traveling", 1, 0)

    $ bg_current = "bg_pool"

    call set_the_scene(silent = True, check_if_dressed = False)
    call taboo_level
    call quick_event

    if round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."

            jump player_room

        call wait
        call event_calls
        call girls_location

    call are_girls_angry

    while True:
        $ bg_current = "bg_pool"

        menu:
            "You're at the pool. What would you like to do?"
            "Chat":
                call chat
            "Want to sunbathe?" if time_index < 2:
                call Pool_Sunbathe

                $ round -= 20 if round >= 20 else round

                "You just hang out for a little while."
            "Want to swim?":
                if time_index >= 3 and AloneCheck():
                    "It's a bit late for a swim."
                else:
                    call Pool_Swim
            "Want to skinnydip?":
                call Pool_Skinnydip
            "Wait" if time_index < 3:
                "You hang out for a bit."

                if round > 10:
                    call wait
                else:
                    call tenth_round

                call girls_location
                call event_calls
            "Leave":
                call world_map

label study_entry:
    $ Player.recent_history.append("traveling")

    $ Nearby = []

    $ bg_current = "bg_entry"

    $ door_locked = False

    call set_the_scene(entering = True)
    call taboo_level

    $ decision = None

    while True:
        $ decision = None

        menu:
            "You're at the door, what do you do?"
            "Knock politely":
                $ decision = "knock"
            "Enter without knocking":
                if time_index >= 3:
                    "The door is locked. It's not like you could just walk through it."
                else:
                    ch_x "You know, [Player.name], it is not polite to enter a room unannounced."

                    jump study_room
            "Use the key to enter" if time_index >= 3 and "Xavier" in keys:
                "You use your key."
            "Ask [KittyX.name]" if time_index >= 3 and KittyX in Party:
                $ decision = "kitty"
            "Ask [StormX.name]" if time_index >= 3 and StormX in Party:
                $ decision = "storm"
            "Leave":
                jump misplaced

        if decision == "knock":
            if time_index >= 3:
                "There's no answer, he's probably asleep."
            else:
                ch_x "Yes, enter. . ."

                "You enter the room."

                jump study_room
        elif decision == "kitty":
            ch_k "Yeah?"

            $ talking_to_Kitty = True

            while talking_to_Kitty:
                menu:
                    extend ""
                    "Could you phase through the door and open it for me?":
                        if "Sneakthief" in KittyX.traits:
                            ch_k "No problem. . ."

                            jump study_room
                        elif "no_thief" in KittyX.recent_history:
                            ch_k "I told you, no."
                        elif approval_check(KittyX, 400, "I") or approval_check(KittyX, 1400):
                            $ KittyX.change_stat("love", 90, 3)
                            $ KittyX.change_stat("obedience", 50, 10)
                            $ KittyX.change_stat("inhibition", 60, 10)

                            ch_k "Heh, you have a wicked mind. . ."

                            $ KittyX.traits.append("Sneakthief")

                            jump study_room
                        else:
                            $ KittyX.change_stat("love", 90, -3)
                            $ KittyX.change_stat("obedience", 50, 2)
                            $ KittyX.change_stat("inhibition", 60, 2)

                            ch_k "Um, I don't really feel comfortable doing that. . ."

                            $ KittyX.recent_history.append("no_thief")
                    "Open the door.":
                        if "Sneakthief" in KittyX.traits:
                            ch_k "No problem. . ."

                            jump study_room
                        elif "no_thief" in KittyX.recent_history:
                            ch_k "I told you, no."
                        elif approval_check(KittyX, 500, "O") or approval_check(KittyX, 1600):
                            $ KittyX.change_stat("obedience", 50, 15)
                            $ KittyX.change_stat("inhibition", 60, 10)

                            ch_k "Heh, if you say so. . ."

                            $ KittyX.traits.append("Sneakthief")

                            jump study_room
                        else:
                            $ KittyX.change_stat("love", 90, -5)
                            $ KittyX.change_stat("obedience", 50, 2)
                            $ KittyX.change_stat("inhibition", 60, 2)

                            ch_k "Um, no."

                            $ KittyX.recent_history.append("no_thief")
                    "Never mind. [[Leave]":
                        $ talking_to_Kitty = False
        elif decision == "storm":
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

                            jump study_room
                        else:
                            $ StormX.change_stat("love", 90, -3)
                            $ StormX.change_stat("obedience", 50, 2)
                            $ StormX.change_stat("inhibition", 60, 2)

                            ch_s "I don't think that's really appropriate behavior. . ."

                            $ StormX.recent_history.append("no_thief")
                    "Could you pick the lock again?" if "Sneakthief" in StormX.traits:
                        ch_s "No problem. . ."

                        jump study_room
                    "Never mind. [[Leave]":
                        $ talking_to_Storm = False

label study_room:
    $ Player.drain_word("traveling",1,0)

    $ bg_current = "bg_study"

    call change_Xavier_face("_happy")

    call set_the_scene(silent = True)
    call taboo_level
    call quick_event

    if round <= 10:
        if time_index >= 3:
            "It's late, you head back to your room."

            jump player_room
        else:
            call tenth_round
            call girls_location

    call are_girls_angry

    while True:
        $ bg_current = "bg_study"

        if time_index >= 3:
            "You are in Xavier's study, but he isn't in at the moment. What would you like to do?"
        else:
            "You are in Xavier's study. What would you like to do?"

        menu:
            extend ""
            "Chat" if time_index >= 3:
                call chat
            "Plan Omega!" if time_index < 3 and RogueX.location == bg_current and Player.level >= 5:
                if approval_check(RogueX, 1500, taboo_modifier=1, Loc="No"):
                    call Xavier_Plan(RogueX)
                else:
                    ch_r "I don't want to do that. . ."
            "Plan Kappa!" if time_index < 3 and KittyX.location == bg_current and Player.level >= 5:
                if "Xavier's photo" in Player.inventory and approval_check(KittyX, 1500, taboo_modifier=1, Loc="No"):
                    call Xavier_Plan(KittyX)
                elif "Xavier's photo" in Player.inventory:
                    ch_k "I don't really want to do that. . ."
                else:
                    ch_k "What?"
            "Plan Psi!" if time_index < 3 and EmmaX.location == bg_current and Player.level >= 5:
                if approval_check(EmmaX, 1500, taboo_modifier=1, Loc="No"):
                    call Xavier_Plan(EmmaX)
                else:
                    ch_e "I'd rather not. . ."
            "Plan Chi!" if time_index < 3 and LauraX.location == bg_current and Player.level >= 5:
                if LauraX.level >= 2 and approval_check(LauraX, 1500, taboo_modifier=1, Loc="No") and approval_check(LauraX, 750, "I"):
                    call Xavier_Plan(LauraX)
                elif LauraX.level < 2 or not approval_check(LauraX, 750, "I"):
                    ch_l "I'm not ready for that."
                else:
                    ch_l "Huh?"
            "Plan Alpha!" if time_index < 3 and JeanX.location == bg_current and Player.level >= 5:
                if approval_check(JeanX, 1500, taboo_modifier=1, Loc="No"):
                    call Xavier_Plan(JeanX)
                else:
                    ch_j "You're on your own there."
            "Plan Rho!" if time_index < 3 and StormX.location == bg_current and Player.level >= 5:
                if "Xavier's files" in Player.inventory and approval_check(StormX, 1500, taboo_modifier=1, Loc="No"):
                    call Xavier_Plan(StormX)
                elif "Xavier's files" in Player.inventory:
                    ch_s "I do not believe that would be approrpriate."
                else:
                    ch_s "What is that?"
            "Plan Zeta!" if time_index < 3 and JubesX.location == bg_current and Player.level >= 5:
                if approval_check(JubesX, 1500, taboo_modifier=1, Loc="No"):
                    call Xavier_Plan(JubesX)
                else:
                    ch_v "What's a \"Zeta?\""
            "Explore" if time_index >= 3 and "explore" not in Player.recent_history:
                $ counter = 0

                $ Player.recent_history.append("explore")

                call study_Explore
            "Wait":
                if time_index >= 3:
                    "You probably don't want to be here when Xavier gets in."
                elif time_index >=2:
                    ch_x "If you don't mind, I would like to close up for the evening?"

                    $ bg_current = "bg_campus"

                    jump misplaced
                else:
                    if round > 10:
                        call wait
                    else:
                        call tenth_round

                    call girls_location

                    ch_x "Not that I mind the company, but is there something I can do for you?"
            "Leave":
                call world_map

label reset_location:
    $ door_locked = False

    $ stack_depth = renpy.call_stack_depth()

    while stack_depth > 0:
        $ stack_depth -= 1

        $ renpy.pop_call()

    if bg_current == "bg_player":
        jump player_room
    elif bg_current == "bg_rogue":
        $ Girl = RogueX

        jump girls_room
    elif bg_current == "bg_kitty":
        $ Girl = KittyX

        jump girls_room
    elif bg_current == "bg_emma":
        $ Girl = EmmaX

        jump girls_room
    elif bg_current == "bg_laura":
        $ Girl = LauraX

        jump girls_room
    elif bg_current == "bg_jean":
        $ Girl = JeanX

        jump girls_room
    elif bg_current == "bg_storm":
        $ Girl = StormX

        jump girls_room
    elif bg_current == "bg_jubes":
        $ Girl = JubesX

        jump girls_room
    elif bg_current == "bg_dangerroom":
        jump danger_room
    elif bg_current == "bg_classroom":
        jump classroom
    elif bg_current == "bg_showerroom":
        jump shower_room
    elif bg_current == "bg_study":
        jump study_room
    elif bg_current == "bg_pool":
        jump pool_entry
    elif bg_current in ["bg_mall", "bg_shop", "bg_dressing"]:
        jump mall
    else:
        jump campus
