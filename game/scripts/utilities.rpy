init python:

    def get_last_name(character):
        split_name = character.name.split()

        return split_name[character.name.count(" ")]

    def sort_Girls_by_approval(Girls):
        sorted_Girls = [Girls[0]]

        Girls.remove(Girls[0])

        while Girls:
            for g in range(len(sorted_Girls)):
                if approval_check(Girls[0], report_value = True) > approval_check(sorted_Girls[g], report_value = True):
                    sorted_Girls.insert(g, Girls[0])

            if Girls[0] not in sorted_Girls:
                sorted_Girls.append(Girls[0])

            Girls.remove(Girls[0])

        return sorted_Girls

label change_Player_stat(flavor, update):
    $ stat = getattr(Player, flavor)

    $ stat += update

    $ stat = 100 if stat > 100 else stat

    $ setattr(Player, flavor, stat)

    if update > 0:
        show expression Text(" +[update]", size = 40, color = "#FFFFFF") at stat_rising(0.75) onlayer screens
    elif update < 0:
        show expression Text("[update]", size = 40, color = "#FFFFFF") at stat_falling(0.75) onlayer screens

    return

label change_Girl_stat(Girl, flavor, update, alternate_values = {}):
    if Girl in alternate_values.keys():
        $ check = alternate_values[Girl][0]
        $ update = alternate_values[Girl][1]

    $ stat = getattr(Girl, flavor)

    $ stat += update

    if update:
        if flavor == "love":
            $ shade = "#c11b17"
        elif flavor == "obedience":
            $ shade = "#2554c7"
        elif flavor == "inhibition":
            $ shade = "#FFF380"
        elif flavor == "lust":
            $ shade = "#FAAFBE"

            if update > 0:
                show expression Text(" +[update]", size = 40, color = shade) at stat_rising(Girl.sprite_location) onlayer screens
            elif update < 0:
                show expression Text("[update]", size = 40, color = shade) at stat_falling(Girl.sprite_location) onlayer screens

            $ stat = 100 if stat > 100 else stat

            $ setattr(Girl, flavor, stat)

            return

        if update > 0:
            show expression Text(" +[update]", size = 40, color = shade) at stat_rising(Girl.sprite_location) onlayer screens
        elif update < 0:
            show expression Text("[update]", size = 40, color = shade) at stat_falling(Girl.sprite_location) onlayer screens

        $ stat = 1000 if stat > 1000 else stat

        $ setattr(Girl, flavor, stat)

    return

label change_Present_stat(flavor, update):
    call check_who_is_present

    $ temp_Girls = Present[:]

    while temp_Girls:
        call change_Girl_stat(temp_Girls[0], flavor, update)

        $ temp_Girls.remove(temp_Girls[0])

    return

label set_the_scene(location = None, show_Characters = True, fade = False, static = False):
    if fade:
        show black_screen onlayer black

    if location:
        $ Player.location = location
    else:
        $ location = Player.location

    python:
        for G in active_Girls:
            if G in Player.Party:
                G.location = Player.location

    if show_Characters:
        call check_who_is_present(location = Player.location)

        if Present:
            if Player.focused_Girl not in Present:
                call shift_focus(Present[0])

            $ offset = (stage_far_far_right - stage_far_left)/len(Present)
            $ total_offset = offset

            call get_color_transform
            $ color_transform = _return

            if not fade and not static:
                call get_transition
                $ transition = _return[0]
            else:
                $ transition = False

            $ number_of_Girls = len(Present)

            $ temp_Girls = all_Girls[:]
            $ temp_Girls.remove(Player.focused_Girl)
            $ renpy.random.shuffle(temp_Girls)

            while temp_Girls:
                if temp_Girls[0].teaching and Player.location == "bg_classroom":
                    if renpy.showing(temp_Girls[0].tag + "_sprite"):
                        call hide_Girl(temp_Girls[0], transition = False)
                        call show_Girl(temp_Girls[0], sprite_layer = 1, color_transform = color_transform, animation_transform = teaching, transition = False)
                    else:
                        call show_Girl(temp_Girls[0], sprite_layer = 1, color_transform = color_transform, animation_transform = teaching, transition = transition)

                    $ number_of_Girls -= 1
                elif temp_Girls[0].location == Player.location:
                    if Player.location == "bg_restaurant" and renpy.showing(temp_Girls[0].tag + "_sprite"):
                        call hide_Girl(temp_Girls[0], transition = False)
                        call show_Girl(temp_Girls[0], x_position = stage_center + total_offset, sprite_layer = 1, color_transform = color_transform, animation_transform = dining, transition = False)
                    elif Player.location == "bg_restaurant":
                        call show_Girl(temp_Girls[0], x_position = stage_center + total_offset, sprite_layer = 1, color_transform = color_transform, animation_transform = dining, transition = transition)
                    elif renpy.showing(temp_Girls[0].tag + "_sprite"):
                        call hide_Girl(temp_Girls[0], transition = False)
                        call show_Girl(temp_Girls[0], x_position = stage_center + total_offset, sprite_layer = 5, color_transform = color_transform, transition = False)
                    else:
                        call show_Girl(temp_Girls[0], x_position = stage_center + total_offset, sprite_layer = 5, color_transform = color_transform, transition = transition)

                    $ number_of_Girls -= 1

                    if stage_center + total_offset + offset >= stage_far_far_right:
                        $ total_offset = -offset*(number_of_Girls - 1)
                    else:
                        $ total_offset += offset
                elif renpy.showing(temp_Girls[0].tag + "_sprite"):
                    call hide_Girl(temp_Girls[0])

                $ temp_Girls.remove(temp_Girls[0])

            if Player.focused_Girl.teaching and Player.location == "bg_classroom":
                if renpy.showing(Player.focused_Girl.tag + "_sprite"):
                    call hide_Girl(Player.focused_Girl, transition = False)
                    call show_Girl(Player.focused_Girl, sprite_layer = 1, color_transform = color_transform, animation_transform = teaching, transition = False)
                else:
                    call show_Girl(Player.focused_Girl, sprite_layer = 1, color_transform = color_transform, animation_transform = teaching, transition = transition)
            elif Player.focused_Girl.location == Player.location:
                if Player.location == "bg_restaurant" and renpy.showing(Player.focused_Girl.tag + "_sprite"):
                    call hide_Girl(Player.focused_Girl, transition = False)
                    call show_Girl(Player.focused_Girl, x_position = stage_center, sprite_layer = 1, color_transform = color_transform, animation_transform = dining, transition = False)
                elif Player.location == "bg_restaurant":
                    call show_Girl(Player.focused_Girl, x_position = stage_center, sprite_layer = 1, color_transform = color_transform, animation_transform = dining, transition = transition)
                elif renpy.showing(Player.focused_Girl.tag + "_sprite"):
                    call hide_Girl(Player.focused_Girl, transition = False)
                    call show_Girl(Player.focused_Girl, x_position = stage_center, sprite_layer = 6, color_transform = color_transform, transition = False)
                else:
                    call show_Girl(Player.focused_Girl, x_position = stage_center, sprite_layer = 6, color_transform = color_transform, transition = transition)
            elif renpy.showing(Player.focused_Girl.tag + "_sprite"):
                call hide_Girl(Player.focused_Girl)

        if Player.location == "bg_study" and time_index < 3:
            show Xavier_sprite zorder 3 at sprite_location(stage_left)
    else:
        call hide_all

    hide black_screen onlayer black

    return

label event_calls:

    return

label traveling_event_calls(location):
    # if location == "bg_classroom" and "met" not in KittyX.history:
    #     call meet_Kitty
    #
    #     return
    #
    # if EmmaX in active_Girls:
    #     if location == "bg_classroom":
    #         if "noise" in Player.history and "attic" not in Player.history and EmmaX.teaching and EmmaX.location == "bg_classroom" and time_index < 2 and weekday < 5:
    #             call meet_Storm_ask_Emma
    #
    #             return
    #
    #         if time_index == 2 and weekday in [0, 2, 4]:
    #             if not Player.Party:
    #                 if "classcaught" not in EmmaX.history:
    #                     call Emma_Caught_Classroom
    #
    #                     return
    #                 elif D20 <= 10 and "will_masturbate" in EmmaX.daily_history:
    #                     call Emma_Caught_Classroom
    #
    #                     return
    #
    #             if "detention" in Player.traits and not Player.Party:
    #                 call Emma_Detention
    #
    #                 return

    # if "met" not in LauraX.history:
    #     if location == "bg_dangerroom":
    #         call meet_Laura
    #
    #         return
    # else:
    #     if location == "bg_campus" and KittyX in active_Girls and time_index < 3 and "dress0" in LauraX.history:
    #         call Laura_Dressup
    #
    #         return

    # if "met" not in JeanX.history:
    #     if location == "bg_shower":
    #         call meet_Jean
    #
    #         return

    # if "met" not in StormX.history:
    #     if location == "bg_player":
    #         if "noise" not in Player.history and "attic" not in Player.history and day >= 1:
    #             call meet_Storm_prelude
    #
    #             return
    #         elif "attic" in Player.history and "water" not in Player.history and day >= 5:
    #             call meet_StormWater
    #
    #             return
    # else:
    #     if location == "bg_classroom":
    #         if StormX.teaching and "Peter" in StormX.history:
    #             call Storm_Peter
    #
    #             return
    #
    #         if StormX.location == "bg_classroom" and time_index == 2 and "mohawk" not in StormX.history and approval_check(StormX, 200, "I"):
    #             call Storm_Hairtalk
    #
    #             return
    #
    #     if location == "bg_pool":
    #         if time_index == 3 and "poolnight" in Player.history:
    #             if "sex friend" not in StormX.player_petnames or (D20 < 5 and "poolnight" not in Player.recent_history):
    #                 call Storm_Poolnight
    #
    #                 return

    # if JubesX in active_Girls:
    #     if location in ["bg_classroom", "bg_dangerroom", "bg_campus", "bg_pool"]:
    #         if time_index < 3 and "sunshine" not in JubesX.history:
    #             call Jubes_Sunshine
    #
    #             return
    #
    #         if "sunshine" in JubesX.history and "mall" not in Player.history and time_index < 3 and JubesX.addiction < 50:
    #             call Jubes_Mall
    #
    #             return

    return

label quick_event_calls:

    return

label tenth_round:
    if Player.location not in bedrooms:
        call wait

        return

    if time_index > 2:
        call sleepover

        return

    python:
        Occupant = None

        for G in all_Girls:
            if G.home == Player.location:
                Occupant = G

                break

    if not Occupant:
        call wait

        return

    if Occupant.location == Player.location:
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
        "You wait for [Occupant.name] to return."

    call wait
    call set_Girls_locations

    if time_index < 3 or Occupant.location != Player.location:
        return

    if Occupant == JubesX:
        pass
    elif Occupant.event_counter["sleepover"] or Occupant.SEXP >= 30:
        if Occupant == RogueX:
            ch_r "It's pretty late, [RogueX.player_petname], but you're welcome to stick around. . ."
        elif Occupant == KittyX:
            ch_k "It's kinda late, [KittyX.player_petname], but you can stay if you like. . ."
        elif Occupant == EmmaX:
            ch_e "It's getting a bit late, [EmmaX.player_petname], but I'd like you to stay. . ."
        elif Occupant == LauraX:
            ch_l "I'm going to sleep soon. You can stay."
        elif Occupant == JeanX:
            ch_j "I'm going to sleep in a bit, did you want to join me?"
        elif Occupant == StormX:
            ch_s "I am going to bed soon, care to join me?"
    elif approval_check(Occupant, 1000, "L") or approval_check(Occupant, 600, "OI"):
        if Occupant == RogueX:
            ch_r "It's pretty late, [Occupant.player_petname], but you can stay for a little bit."
        elif Occupant == KittyX:
            ch_k "It's kinda late, [KittyX.player_petname], but you can stay for a bit."
        elif Occupant == EmmaX:
            ch_e "It's getting a bit late, [EmmaX.player_petname], but you can stay."
        elif Occupant == LauraX:
            ch_l "It's late, you can stay though."
        elif Occupant == JeanX:
            ch_j "It's getting late."
        elif Occupant == StormX:
            ch_s "It is getting late, [StormX.player_petname]."
    else:
        if Occupant == RogueX:
            ch_r "It's getting a little late [Occupant.player_petname]. You should head out."
        elif Occupant == KittyX:
            ch_k "It's getting late [KittyX.player_petname]. You should get some sleep."
        elif Occupant == EmmaX:
            ch_e "It's getting late, [EmmaX.player_petname]. I need to get some sleep."
        elif Occupant == LauraX:
            ch_l "I'm going to sleep. You should leave."
        elif Occupant == JeanX:
            ch_j "I'm going to sleep. You should go."
        elif Occupant == StormX:
            ch_s "I am going to bed soon. You should go."

        $ Player.location = "bg_campus"

        jump reset_location

    return

label set_Girls_locations:
    $ Nearby = []

    $ temp_Girls = active_Girls[:]
    $ renpy.random.shuffle(temp_Girls)

    python:
        leaving_Girls = []
        arriving_Girls = []

        for G in temp_Girls:
            if G not in Player.Party:
                previous_location = G.location

                if G.location == "nearby":
                    G.location = Player.location

                if G == JubesX and G.addiction > 60:
                    G.location = G.home
                else:
                    G.location = G.weekly_schedule[weekday][time_index]

                if G.location == "bg_teacher":
                    G.location = "bg_classroom"
                    G.teaching = True
                elif G.teaching:
                    G.teaching = False

                if previous_location == Player.location and G.location != previous_location:
                    leaving_Girls.append(G)
                elif G.location == Player.location and G.location != previous_location:
                    arriving_Girls.append(G)
            else:
                G.location = Player.location

    hide black_screen onlayer black

    while leaving_Girls:
        call expression leaving_Girls[0].tag + "_leaving"

        $ leaving_Girls.remove(leaving_Girls[0])

    call change_clothes

    if arriving_Girls:
        call Girls_arrive(arriving_Girls)

    return

label change_clothes:
    python:
        for G in active_Girls:
            if G not in Player.Party:
                Outfit_name = None

                if G.location == "bg_dangerroom":
                    Outfit_name = "gym_clothes"
                elif G.location == "bg_pool" and "swimwear" in G.Wardrobe.Outfits.keys():
                    Outfit_name = "swimwear"
                elif G.location == "bg_shower":
                    Outfit_name = "shower"
                elif G.teaching:
                    Outfit_name = "teacher"

                G.change_Outfit(Outfit_name, instant = True)

    return

label wait:
    show black_screen onlayer black

    $ stack_depth = renpy.call_stack_depth()

    call checkout
    call reset_player

    if time_index < 3:
        $ time_index += 1
        $ current_time = time_options[time_index]

        $ round = 100

        call set_Girls_locations
    else:
        $ time_index = 0
        $ current_time = time_options[time_index]

        $ round = 100

        $ day += 1

        if weekday < 6:
            $ weekday += 1
        else:
            $ weekday = 0

        $ day_of_week = week[weekday]

        $ Player.Party = []

        $ Player.cash += Player.income

        $ Player.semen = Player.max_semen
        $ Player.spunk = False
        $ Player.reputation += 10 if Player.reputation < 800 else 0

        call reset_all_Girls_at_end
        call change_clothes

    call reset_all_Girls_at_beginning

    $ Player.semen += 1
    $ Player.focus -= 5 if Player.focus >= 10 else 0

    if Player.level < 10 and Player.XP >= Player.XP_goal:
        $ Player.XP_goal = int(1.15*Player.XP_goal + 100)
        $ Player.level += 1
        $ Player.stat_points += 1

        if Player.level < 5:
            $ increase = 1
        elif Player.level < 9:
            $ increase = 2
        else:
            $ increase = 3

        $ Player.income += increase

        "You've leveled up!"
        "Xavier has noticed your achievements and raised your stipend by $[increase] per day. It is now $[Player.income]."

        if Player.level == 10:
            "You've reached max level!"

    call checkout

    hide black_screen onlayer black

    return

label checkout:
    python:
        Player.focus = 99 if Player.focus > 99 else Player.focus
        Player.focus = 0 if Player.focus < 0 else Player.focus

        Player.semen = Player.max_semen if Player.semen > Player.max_semen else Player.semen
        Player.semen = 0 if Player.semen < 0 else Player.semen

        Player.reputation = 1000 if Player.reputation > 1000 else Player.reputation
        Player.reputation = 0 if Player.reputation < 0 else Player.reputation

        Player.XP = 3330 if Player.XP > 3330 else Player.XP

        for G in all_Girls:
            G.love = 1000 if G.love > 1000 else G.love
            G.love = 0 if G.love < 0 else G.love

            G.obedience = 1000 if G.obedience > 1000 else G.obedience
            G.obedience = 0 if G.obedience < 0 else G.obedience

            G.inhibition = 1000 if G.inhibition > 1000 else G.inhibition
            G.inhibition = 0 if G.inhibition < 0 else G.inhibition

            G.lust = 99 if G.lust > 99 else G.lust
            G.lust = 0 if G.lust < 0 else G.lust

            G.mood = 9 if G.mood > 9 else G.mood
            G.mood = 0 if G.mood < 0 else G.mood

            G.remaining_Actions = G.max_Actions if G.remaining_Actions > G.max_Actions else G.remaining_Actions
            G.remaining_Actions = 0 if G.remaining_Actions < 0 else G.remaining_Actions

            for GB in all_Girls:
                if GB != G:
                    G.likes[GB.tag] = 1000 if G.likes[GB.tag] > 1000 else G.likes[GB.tag]
                    G.likes[GB.tag] = 0 if G.likes[GB.tag] < 0 else G.likes[GB.tag]

    return

label reset_player:
    call get_dressed
    call stop_all_Actions

    return

label reset_all_Girls_at_end:
    python:
        total_SEXP = 0

        for G in all_Girls:
            total_SEXP += G.SEXP

            if G in active_Girls and G.location != Player.location:
                G.location = G.home

            G.remaining_Actions = G.max_Actions

            G.lust -= 5 if G.lust >= 50 else 0

            for key in G.spunk.keys():
                G.spunk[key] = False

            G.todays_Outfit_name = G.Outfit_schedule[weekday]

    return

label reset_all_Girls_at_beginning:
    python:
        for G in active_Girls:
            G.remaining_Actions += 1 if time_index != 0 else 0

            if G.location == "bg_classroom" or G.location == "bg_dangerroom" or G.teaching:
                G.XP += 10

            G.blushing = ""
            G.wet = False
            G.held_item = None

            if G.Clothes["buttplug"]:
                bonus = 1
            else:
                bonus = 0

            if G.used_to_anal < 2:
                if G.Action_counter["anal"] + G.Action_counter["dildo_ass"] + bonus >= 15:
                    G.used_to_anal = 2
                elif G.Action_counter["anal"] + G.Action_counter["dildo_ass"] + bonus >= 3:
                    G.used_to_anal = 1

            G.XP = 3330 if G.XP > 3330 else G.XP

            if G.XP >= G.XP_goal and G.level < 10:
                G.XP_goal = int((1.15*G.XP_goal) + 100)
                G.level += 1
                G.stat_points += 1

                renpy.say(None, "[G.name]'s leveled up! I bet she has some new tricks to learn.")

                if G.level == 10:
                    renpy.say(None, "[G.name]'s reached max level!")

            G.set_default_faces()
            G.change_face()

    return

label clear_the_room(Girl, passive = False, silent = False):
    $ Girls = []
    $ hosted = False

    python:
        for G in all_Girls:
            if G != Girl:
                if G.location == Player.location or G in Player.Party:
                    Girls.append(G)

                    if Player.location == G.home:
                        hosted = True

    if Girl.location != Player.location:
        call add_Girls(Girl)
    else:
        call shift_focus(Girl)

    if not passive and not silent:
        if hosted:
            if len(Girls) > 1:
                if Girl == RogueX:
                    ch_r "Ladies, could I talk to [Player.name] alone for a minute?"
                elif Girl == KittyX:
                    ch_k "Girls, could I talk to [Player.name] alone for a sec?"
                elif Girl == EmmaX:
                    ch_e "Girls, would you mind if I had a word alone with [Player.name]?"
                elif Girl == LauraX:
                    ch_l "Hey, I need to talk with [Player.name]."
                elif Girl == JeanX:
                    ch_j "Let me have [Player.name]], ladies."
                elif Girl == StormX:
                    ch_s "If I could speak to [Player.name], ladies?"
                elif Girl == JubesX:
                    ch_v "Hey, I've gotta talk to [Player.name]."
            elif Girls:
                if Girl == RogueX:
                    ch_r "[Girls[0].name], could I talk to [Player.name] alone for a minute?"
                elif Girl == KittyX:
                    ch_k "[Girls[0].name], could I talk to [Player.name] alone for a sec?"
                elif Girl == EmmaX:
                    ch_e "[Girls[0].name], would you mind if I had a word alone with [Player.name]?"
                elif Girl == LauraX:
                    ch_l "[Girls[0].name], I need to talk with [Player.name]."
                elif Girl == JeanX:
                    ch_j "You there, I need [Player.name]."
                elif Girl == StormX:
                    ch_s "I need to speak with [Player.name]."
                elif Girl == JubesX:
                    ch_v "Hey, I've gotta talk to [Player.name]."
        else:
            if len(Girls) > 1:
                if Girl == RogueX:
                    ch_r "Ladies, could I talk to [Player.name] alone for a minute?"
                elif Girl == KittyX:
                    ch_k "Girls, could I talk to [Player.name] alone for a sec?"
                elif Girl == EmmaX:
                    ch_e "Girls, would you mind if I had a word alone with [Player.name]?"
                elif Girl == LauraX:
                    ch_l "Hey, clear out, I need to talk with [Player.name]."
                elif Girl == JeanX:
                    ch_j "Let me have the room, ladies."
                elif Girl == StormX:
                    ch_s "If I could have the room, ladies?"
                elif Girl == JubesX:
                    ch_v "Hey, could you gals check out? I've gotta talk to [Player.name]."
            elif Girls:
                if Girl == RogueX:
                    ch_r "[Girls[0].name], could I talk to [Player.name] alone for a minute?"
                elif Girl == KittyX:
                    ch_k "[Girls[0].name], could I talk to [Player.name] alone for a sec?"
                elif Girl == EmmaX:
                    ch_e "[Girls[0].name], would you mind if I had a word alone with [Player.name]?"
                elif Girl == LauraX:
                    ch_l "[Girls[0].name], clear out, I need to talk with [Player.name]."
                elif Girl == JeanX:
                    ch_j "You there, clear out."
                elif Girl == StormX:
                    ch_s "If you could give me the room, [Girls[0].name], I need to speak with [Player.name]."
                elif Girl == JubesX:
                    ch_v "Hey, could you check out, [Girls[0].name]? I've gotta talk to [Player.name]."

    call stop_all_Actions

    $ renpy.random.shuffle(Girls)

    if hosted:
        while Girls:
            if silent:
                pass
            elif not passive:
                if Girls[0] == RogueX:
                    ch_r "No problem, I'll see you later then."
                elif Girls[0] == KittyX:
                    ch_k "[KittyX.Like]sure, I'll see you later."
                elif Girls[0] == EmmaX:
                    ch_e "Fine, I'll see you later then."
                elif Girls[0] == LauraX:
                    ch_l "Ok. see ya."
                elif Girls[0] == JeanX:
                    ch_j "I'll pretend you were less rude. . ."
                elif Girls[0] == StormX:
                    ch_s "I will see you later. . ."
                elif Girls[0] == JubesX:
                    ch_v "Peace. . ."

            $ Girls.remove(Girls[0])

        $ Girl.location = Girl.home

        if not silent:
            "[Girl.name] brings you back to her room."

        jump Girls_room
    else:
        while Girls:
            if silent:
                pass
            elif not passive:
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
                    ch_r "I should get going, see you later, [RogueX.player_petname]."
                elif Girls[0] == KittyX:
                    ch_k "I think I'll head out, I'll see you later."
                elif Girls[0] == EmmaX:
                    ch_e "I think I should be going now."
                elif Girls[0] == LauraX:
                    ch_l "I'm leaving."
                elif Girls[0] == JeanX:
                    "[JeanX.name] wanders off."
                elif Girls[0] == StormX:
                    ch_s "I should go. . ."
                elif Girls[0] == JubesX:
                    ch_v "I'm gonna peace out. . ."

            if passive and silent:
                call remove_Girl(Girls[0], transition = False)
            else:
                call remove_Girl(Girls[0])

            $ Girls.remove(Girls[0])

    call set_the_scene

    return

label stop_all_Actions(visual = False):
    $ Player.primary_Action = ActionClass(None, Target = None)
    $ Player.secondary_Action = ActionClass(None, Target = None)

    $ temp_Girls = Present[:]

    while temp_Girls:
        $ temp_Girls[0].main_action = ActionClass(None, Target = None)
        $ temp_Girls[0].secondary_Action = ActionClass(None, Target = None)

        if visual:
            call show_full_body(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    return

label ask_to_meet(Girl):
    "[Girl.name] asks if you could meet her in your room later."

    if always_return_to_room:
        call return_to_room

    return

label return_to_room:
    menu:
        "Return to your room and deal with that?"
        "Yes":
            $ Player.traveling = True

            show black_screen onlayer black

            call hide_all
            jump player_room
        "No":
            pass

    return

label Girls_arrive(arriving_Girls):
    if arriving_Girls in all_Girls:
        $ arriving_Girls = [arriving_Girls]

    $ arriving_Girls = sort_Girls_by_approval(arriving_Girls)

    call add_Girls(arriving_Girls)

    python:
        for G in all_Girls:
            if G in Nearby:
                G.location = "nearby"

    return True

label exit_gym:
    python:
        line = None

        for G in Player.Party:
            if G.Outfit.name == "gym_clothes":
                if len(Player.Party) > 1:
                    line = "We should change out of these if we're leaving. . ."
                else:
                    line = "I should change out of these if we're leaving. . ."

    if line:
        Player.Party[0].voice "[line]"

        show black_screen onlayer black

        python:
            for G in Player.Party:
                G.change_Outfit(instant = True)

        hide black_screen onlayer black

    return

label dismiss_menu:
    menu:
        "Did you want to ask someone to leave?"
        "[RogueX.name]" if RogueX.location == Player.location or RogueX in Player.Party:
            call dismiss_Girl(RogueX)
        "[KittyX.name]" if KittyX.location == Player.location or KittyX in Player.Party:
            call dismiss_Girl(KittyX)
        "[EmmaX.name]" if EmmaX.location == Player.location or EmmaX in Player.Party:
            call dismiss_Girl(EmmaX)
        "[LauraX.name]" if LauraX.location == Player.location or LauraX in Player.Party:
            call dismiss_Girl(LauraX)
        "[JeanX.name]" if JeanX.location == Player.location or JeanX in Player.Party:
            call dismiss_Girl(JeanX)
        "[StormX.name]" if StormX.location == Player.location or StormX in Player.Party:
            call dismiss_Girl(StormX)
        "[JubesX.name]" if JubesX.location == Player.location or JubesX in Player.Party:
            call dismiss_Girl(JubesX)
        "Never mind.":
            pass

    return

label get_dressed:
    if Player.naked:
        "You get dressed."

        $ Player.naked = False
    elif Player.cock_out:
        "You put your cock away."

        $ Player.cock_out = False
    return

label shift_focus(Girl):
    if Player.focused_Girl == Girl:
        return

    $ Player.focused_Girl = Girl

    $ renpy.restart_interaction()

    return
