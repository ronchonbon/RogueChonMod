label world_map:
    $ taboo = 0

    menu:
        "Where would you like to go?"
        "My room":
            jump player_room_entry
        "Girl's rooms":
            menu:
                "[RogueX.name]'s room":
                    call girls_room_entry(RogueX)
                "[KittyX.name]'s room" if "met" in KittyX.history:
                    call girls_room_entry(KittyX)
                "[EmmaX.name]'s room" if "met" in EmmaX.history:
                    call girls_room_entry(EmmaX)
                "[LauraX.name]'s room" if "met" in LauraX.history:
                    call girls_room_entry(LauraX)
                "[JeanX.name]'s room" if "met" in JeanX.history:
                    call girls_room_entry(JeanX)
                "[StormX.name]'s room" if "met" in StormX.history:
                    call girls_room_entry(StormX)
                "[JubesX.name]'s room" if "met" in JubesX.history:
                    call girls_room_entry(JubesX)
                "Back":
                    jump world_map
        "University Square":
            jump campus_entry
        "Class":
            if time_index < 3:
                jump classroom_entry
            elif "Xavier" in keys:
                "The door is locked, but you were able to use Xavier's key to get in."

                jump classroom_entry
            else:
                "It's late for classes and the classrooms are locked down."

                jump world_map
        "The Danger Room":
            jump danger_room_entry
        "The showers":
            jump shower_entry
        "The pool":
            jump pool_entry
        "Xavier's study":
            jump study_entry
        "Go to the mall" if "mall" in Player.history and time_index < 3:
            call Mall_entry
            jump campus
        "Attic" if "attic" in Player.history:
            jump StormMeet
        "Stay where I am.":
            return

    return

label player_room_entry:
    $ door_locked = False

    $ bg_current = "bg_player"

    $ Player.recent_history.append("traveling")

    $ Nearby = []

    call change_out_of_gym_clothes
    call event_calls
    call set_the_scene

label player_room:
    $ bg_current = "bg_player"

    $ Player.drain_word("traveling", 1, 0)

    call taboo_level
    call set_the_scene(silent = True)
    call quick_event
    call checkout(total = True)

    if round <= 10:
        call tenth_round
        call girls_location
        call event_calls

    call are_girls_angry

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

            call tenth_round
            call girls_location
            call event_calls
        "Shop":
            call Shop
        "Special Options":
            call SpecialMenu
        "Leave":
            call world_map

    jump player_room

label girls_room_entry(Girl):
    $ bg_current = Girl.home
    $ door_locked = False

    call shift_focus(Girl)

    $ Nearby = []

    call change_out_of_gym_clothes #call Gym_Clothes
    call set_the_scene(entering = 1)
    call taboo_level

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

        return

    if round >= 10 and Girl.location == bg_current and "will_masturbate" in Girl.daily_history and D20 >= 5:
        call caught_masturbating(Girl)
    else:
        if Girl in keys:
            menu:
                "You have a key, what do you do?"
                "Knock politely":
                    $ knocking = True
                "Use the key to enter.":
                    $ knocking = False

                    call set_the_scene
        else:
            $ knocking = False

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
                    call girls_room(Girl)
        else:
            "You knock on [Girl.name]'s door."
            if Girl.location == bg_current:
                if round <= 10:
                    if time_index >= 3: #night time
                        "There's no answer, she's probably asleep."

                        jump campus
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
                elif "angry" in Girl.recent_history:
                    $ Girl.change_face("angry")

                    call get_out_lines(Girl)
                    jump campus
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
                        call girls_room(Girl)
                    "No":
                        pass

            "You head back."

            jump campus
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

            jump campus
        elif "noentry" in Girl.recent_history or "angry" in Girl.recent_history:
            $ Girl.change_face("angry")

            call get_out_lines(Girl)
            jump campus
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

            jump campus
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

            jump campus

    call event_calls

    return

label girls_room(Girl):
    $ bg_current = Girl.home

    $ Player.drain_word("traveling", 1, 0)

    call taboo_level
    call set_the_scene(silent = True)
    call quick_event
    call checkout(total = True)

    if round <= 10:
        call tenth_round
        call girls_location
        call event_calls

    call are_girls_angry

    label girls_room_menu:

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

            call tenth_round
            call girls_location
            call event_calls
        "Leave":
            call world_map

    if "angry" in Girl.recent_history:
        $ Girl.change_face("angry")

        call get_out_lines(Girl)
        jump player_room

    jump girls_room_menu

label campus_entry:
    call check_on_Jubes_sunshock

    $ bg_current = "bg_campus"

    $ Player.drain_word("locked",0,0,1)
    $ Player.recent_history.append("traveling")

    $ Nearby = []

    call change_out_of_gym_clothes
    call taboo_level
    call event_calls
    call set_the_scene

label campus:
    $ bg_current = "bg_campus"

    $ Player.drain_word("traveling",1,0)

    call taboo_level
    call set_the_scene(silent = True)
    call quick_event
    call checkout(total = True)

    call are_girls_angry

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

        call wait
        call event_calls
        call girls_location

    menu:
        "You are in the university square. What would you like to do?"
        "Chat":
            call chat
        "Wait" if time_index < 3:
            "You wait around a bit."

            call wait
            call girls_location
            call event_calls
        "Leave":
            call world_map

    jump campus

label campus_map:
    $ primary_action = None
    $ offhand_action = None
    $ girl_offhand_action = None
    $ second_girl_primary_action = None
    $ second_girl_offhand_action = None

    $ bg_current = "bg_campus"

    $ Player.drain_word("locked",0,0,1)

    call set_the_scene
    call world_map

    jump campus

label classroom_entry:
    call check_on_Jubes_sunshock

    $ bg_current = "bg_classroom"

    $ Player.drain_word("locked",0,0,1)
    $ Player.recent_history.append("traveling")

    $ Present = []
    $ Nearby = []

    call change_out_of_gym_clothes
    call taboo_level
    call event_calls
    call set_the_scene(0)

label classroom:
    $ bg_current = "bg_classroom"

    if "goto" in Player.recent_history or "traveling" in Player.recent_history:
        $ Present = []

        if time_index < 2 and weekday < 5:
            call classroom_Seating

        $ Player.drain_word("goto",1,0)
        $ Player.drain_word("traveling",1,0)

    call taboo_level
    call set_the_scene(silent = True)
    call quick_event
    call checkout(total = True)

    if round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."

            jump player_room

        call wait
        call event_calls
        call girls_location

    call are_girls_angry

    if EmmaX.location == "bg_teacher":
        "As you sit down, you see [EmmaX.name] at the podium. What would you like to do?"
    elif StormX.location == "bg_teacher":
        "As you sit down, you see [StormX.name] at the podium. What would you like to do?"
    elif time_index == 2 or weekday > 5:
        "You enter the classroom. What would you like to do?"
    else:
        "You sit down at a desk. What would you like to do?"

    menu classroom_menu:
        extend ""
        "Take the morning class" if weekday < 5 and time_index == 0:
            if round >= 30:
                jump take_class
            else:
                "Class is already letting out. You can hang out until the next one."
        "Take the afternoon class" if weekday < 5 and time_index == 1:
            if round >= 30:
                jump take_class
            else:
                "Class is already letting out. You can hang out until they lock up for the night."
        "Chat":
            call chat
        "Lock the door" if "locked" not in Player.traits:
            if weekday >=5 or time_index >= 2:
                "You lock the door."

                $ Player.traits.append("locked")

                call taboo_level
            else:
                "You can't really do that during class."
        "Unlock the door" if "locked" in Player.traits:
            "You unlock the door."

            $ Player.traits.remove("locked")

            call taboo_level
        "Wait" if time_index < 3:
            "You hang out for a bit."

            call wait
            call girls_location
            call event_calls

            if time_index < 2:
                $ line = "A new class is in session. What would you like to do?"
            else:
                $ line = "Classes have let out for the day. What would you like to do?"
        "Leave":
            call world_map

    jump classroom_menu

label danger_room_entry:
    call check_on_Jubes_sunshock

    $ bg_current = "bg_dangerroom"

    $ Player.drain_word("locked",0,0,1)
    $ Player.recent_history.append("traveling")

    $ Nearby = []

    call gym_entry
    call taboo_level
    call event_calls
    call set_the_scene

label danger_room:
    $ bg_current = "bg_dangerroom"

    $ Player.drain_word("traveling",1,0)

    call taboo_level
    call set_the_scene(silent = True)
    call quick_event
    call checkout(total = True)

    if round <= 10:
        "Looks like shifts are changing. . ."

        if time_index >=3:
            "You're getting tired, you head back to your room."

            jump player_room

        call wait
        call girls_location
        call event_calls
        call change_out_of_gym_clothes

    call are_girls_angry

    menu:
        "This is the Danger Room. What would you like to do?"
        "Train":
            if time_index >= 3:
                "The Danger Room has been powered off for the night, maybe take a break."
            elif round >= 30:
                jump training
            else:
                "There really isn't time to do much before the next rotation, maybe wait a bit."
        "Chat":
            call chat
        "Lock the door" if "locked" not in Player.traits:
            if time_index >= 3:
                "You lock the door."

                $ Player.traits.append("locked")

                call taboo_level
            else:
                "You can't really do that during free hours."
        "Unlock the door" if "locked" in Player.traits:
            "You unlock the door."

            $ Player.traits.remove("locked")

            call taboo_level
        "Wait" if time_index < 3:
            "You hang out for a bit."

            call wait
            call girls_location
            call event_calls
            call change_out_of_gym_clothes
        "Leave":
            call exit_gym
            jump campus_map

    jump danger_room

label shower_entry:
    call check_on_Jubes_sunshock

    $ bg_current = "bg_showerroom"

    $ Player.drain_word("locked",0,0,1)

    $ Nearby = []
    $ Present = []

    call taboo_level
    call set_the_scene (0, 1, 0)

    if round <= 10 or len(Party) >= 2:
        jump shower_room

    if day >= 9 and "met" not in JeanX.history and "met" in EmmaX.history:
        call JeanMeet
        jump shower_room

    $ potential_Girls = []
    $ Girls = active_Girls[:]

    while Girls:
        if Girls[0] not in Party and "showered" not in Girls[0].daily_history and (Girls[0].location == Girls[0].home or Girls[0].location == "bg_dangerroom"):
            $ potential_Girls.append(Girls[0])

        $ Girls.remove(Girls[0])

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
            call girl_caught_showering(potential_Girls[0])
            jump shower_room
        elif D20 > 13:
            $ potential_Girls[0].add_word(1,"showered","showered",0,0)

            call Girl_Caught_Changing(potential_Girls[0])
            jump shower_room

    $ temp_Girls = potential_Girls[:]
    while temp_Girls:
        $ temp_Girls[0].location = bg_current
        $ temp_Girls.remove(temp_Girls[0])

    call Present_Check (0)

    $ temp_Girls = potential_Girls[:]

    while temp_Girls:
        if temp_Girls[0].location == bg_current and temp_Girls[0] not in Party:
            if D20 >= 10:
                $ temp_Girls[0].add_word(1,"showered","showered",0,0)

            $ temp_Girls[0].change_outfit("_towel")

        $ temp_Girls.remove(temp_Girls[0])

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

    $ Player.drain_word("traveling",1,0)

    call taboo_level
    call set_the_scene(check_if_dressed = False)
    call quick_event
    call checkout(total = True)

    if round <= 10:
        if time_index == 3:
            "You're getting tired, you head back to your room."
            jump player_room

        call wait
        call event_calls
        call girls_location

    call are_girls_angry

    menu:
        "You're in the showers. What would you like to do?"
        "Chat":
            call chat
        "Shower" if round > 30:
            call showering
        "Wait" if time_index < 3:
            "You hang out for a bit."

            if round > 30:
                "In the showers."
                "Not gonna lie, kinda weird."

            call wait
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
            call world_map
            call change_out_of_towels

    jump shower_room

label pool_entry:
    call check_on_Jubes_sunshock

    $ bg_current = "bg_pool"

    $ Player.drain_word("locked",0,0,1)
    $ Player.recent_history.append("traveling")

    $ Nearby = []

    call change_out_of_gym_clothes
    call taboo_level
    call event_calls
    call SwimSuit
    call set_the_scene

label pool:
    $ bg_current = "bg_pool"

    $ Player.drain_word("traveling",1,0)

    call taboo_level
    call set_the_scene(silent = True, Dress=0)
    call quick_event
    call checkout(total = True)

    if round <= 10:
        if time_index >= 3:
            "You're getting tired, you head back to your room."

            jump player_room

        call wait
        call event_calls
        call girls_location

    call are_girls_angry

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
        "Wait (locked)" if time_index >= 3:
            pass
        "Wait" if time_index < 3:
            "You hang out for a bit."

            call wait
            call girls_location
            call event_calls
        "Leave":
            call world_map

    jump pool

label study_entry:
    call check_on_Jubes_sunshock
    $ bg_current = "bg_study"

    $ Player.drain_word("locked",0,0,1)

    $ Nearby = []

    call change_out_of_gym_clothes
    call taboo_level
    call set_the_scene(entering = True)

    menu:
        "You're at the door, what do you do?"
        "Knock politely":
            $ decision = "knock"
        "Enter without knocking":
            if time_index >= 3:
                "The door is locked. It's not like you could just walk through it."

                jump study_entry
        "Use the key to enter" if time_index >= 3 and "Xavier" in keys:
            "You use your key."

            $ decision = None
        "Ask [KittyX.name]" if time_index >= 3 and KittyX in Party:
            $ decision = "kitty"
        "Ask [StormX.name]" if time_index >= 3 and StormX in Party:
            $ decision = "storm"
        "Leave":
            "You head back."

            jump campus_map

    if decision == "knock":
        if time_index >= 3:
            "There's no answer, he's probably asleep."

            jump study_entry
        else:
            ch_x "Yes, enter. . ."

            "You enter the room."
    elif decision == "kitty":
        ch_k "Yeah?"

        while True:
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
                    "You head back."

                    jump campus_map

        jump study_entry
    elif decision == "storm":
        ch_s "What is it?"

        while True:
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
                    "You head back."

                    jump campus_map

        jump study_entry

    elif time_index < 3:
        ch_x "You know, [Player.name], it is not polite to enter a room unannounced."

label study_room:
    $ bg_current = "bg_study"

    $ Player.drain_word("traveling",1,0)

    call taboo_level
    call set_the_scene(silent = True)
    call quick_event
    call checkout(total = True)

    if round <= 10:
        if time_index >= 3:
            "It's late, you head back to your room."

            jump player_room
        else:
            call wait
            call girls_location

    call are_girls_angry
    call change_Xavier_face ("_happy")

    if time_index >= 3:
        "You are in Xavier's study, but he isn't in at the moment. What would you like to do?"
    else:
        "You are in Xavier's study. What would you like to do?"

    menu:
        extend ""
        "Chat" if time_index >= 3:
            call chat
        "Plan Omega!" if time_index < 3 and RogueX.location == bg_current and Player.level >= 5:
            if approval_check(RogueX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan(RogueX)
            else:
                ch_r "I don't want to do that. . ."
        "Plan Kappa!" if time_index < 3 and KittyX.location == bg_current and Player.level >= 5:
            if "Xavier's photo" in Player.inventory and approval_check(KittyX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan(KittyX)
            elif "Xavier's photo" in Player.inventory:
                ch_k "I don't really want to do that. . ."
            else:
                ch_k "What?"
        "Plan Psi!" if time_index < 3 and EmmaX.location == bg_current and Player.level >= 5:
            if approval_check(EmmaX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan(EmmaX)
            else:
                ch_e "I'd rather not. . ."
        "Plan Chi!" if time_index < 3 and LauraX.location == bg_current and Player.level >= 5:
            if LauraX.level >= 2 and approval_check(LauraX, 1500, TabM=1, Loc="No") and approval_check(LauraX, 750, "I"):
                call Xavier_Plan(LauraX)
            elif LauraX.level < 2 or not approval_check(LauraX, 750, "I"):
                ch_l "I'm not ready for that."
            else:
                ch_l "Huh?"
        "Plan Alpha!" if time_index < 3 and JeanX.location == bg_current and Player.level >= 5:
            if approval_check(JeanX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan(JeanX)
            else:
                ch_j "You're on your own there."
        "Plan Rho!" if time_index < 3 and StormX.location == bg_current and Player.level >= 5:
            if "Xavier's files" in Player.inventory and approval_check(StormX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan(StormX)
            elif "Xavier's files" in Player.inventory:
                ch_s "I do not believe that would be approrpriate."
            else:
                ch_s "What is that?"
        "Plan Zeta!" if time_index < 3 and JubesX.location == bg_current and Player.level >= 5:
            if approval_check(JubesX, 1500, TabM=1, Loc="No"):
                call Xavier_Plan(JubesX)
            else:
                ch_v "What's a \"Zeta?\""
        "Explore" if time_index >= 3 and "explore" not in Player.recent_history:
            $ counter = 0

            $ Player.recent_history.append("explore")

            jump study_Explore
        "Wait":
            if time_index >= 3:
                "You probably don't want to be here when Xavier gets in."
            elif time_index >=2:
                ch_x "If you don't mind, I would like to close up for the evening?"
                "You return to your room."

                jump player_room
            else:
                call wait
                call girls_location

                ch_x "Not that I mind the company, but is there something I can do for you?"
        "Leave":
            call world_map

    jump study_room
