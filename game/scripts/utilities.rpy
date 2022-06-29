init python:

    def get_last_name(character):
        split_name = character.name.split()

        return split_name[character.name.count(" ")]

label change_Player_stat(flavor, check, update, greater_than = False):
    $ stat = getattr(Player, flavor)

    if greater_than:
        if stat >= check:
            $ stat += update
        else:
            $ update = 0
    else:
        if stat <= check:
            $ stat += update
        else:
            $ update = 0

    $ stat = 100 if stat > 100 else stat

    $ setattr(Player, flavor, stat)

    if update > 0:
        show expression Text("+[update]", size = 40, color = "#FFFFFF") at stat_rising(0.75) onlayer screens
    elif update < 0:
        show expression Text("[update]", size = 40, color = "#FFFFFF") at stat_falling(0.75) onlayer screens

    return

label change_Girl_stat(Girl, flavor, check, update, greater_than = False, Alt = [[], 0, 0]):
    if Girl in Alt[0]:
        $ check = Alt[1] if Alt[1] else check
        $ update = Alt[2] if Alt[2] else update

    if flavor in ["love", "obedience", "inhibition"]:
        $ check *= 10

    $ stat = getattr(Girl, flavor)

    $ Overflow = Girl.had_chat[4]

    if Girl == JeanX and flavor == "inhibition" and Girl.IX > 0:
        $ stat -= Girl.IX

    if greater_than:
        if stat >= check:
            $ stat += update
        else:
            $ update = 0
    else:
        if stat <= check:
            $ stat += update
        else:
            $ update = 0

    if Girl == JeanX and flavor == "inhibition" and Girl.IX > 0:
        $ stat += Girl.IX

    if update:
        if Girl == JeanX and update > 0:
            if flavor == "obedience" and Girl.obedience <= 800 and check < 800:
                $ update = int(update/2)
                $ stat -= update
            elif flavor == "inhibition" and Girl.IX > 0:
                if Girl.taboo >= 40:
                    $ update += update
                    $ stat += update
                if stat > 1000:
                    $ Girl.IX -= (stat - 1000)

                    $ stat = 1000
                    $ update = 0
                elif stat > 700:
                    $ Girl.IX -= int(update/2)

                $ Girl.IX = 0 if Girl.IX < 0 else Girl.IX
            elif flavor == "love" and stat >= 500 and Girl.obedience < 700:
                if Girl.love < 500:
                    $ Girl.love = 500

                    $ update = stat - 500

                $ Girl.stored_stats += update

                if check > Girl.obedience:
                    $ flavor = "obedience"
                    $ update = int(update/5)
                    $ stat = Girl.obedience + update
                else:
                    $ update = 0

        if flavor == "love":
            $ shade = "#c11b17"
        elif flavor == "obedience":
            $ shade = "#2554c7"
        elif flavor == "inhibition":
            $ shade = "#FFF380"
        elif flavor == "lust":
            $ shade = "#FAAFBE"

            if update > 0:
                show expression Text("+[update]", size = 40, color = shade) at stat_rising(Girl.sprite_location) onlayer screens
            elif update < 0:
                show expression Text("[update]", size = 40, color = shade) at stat_falling(Girl.sprite_location) onlayer screens

            $ stat = 100 if stat > 100 else stat

            $ setattr(Girl, flavor, stat)

            return

        if stat > 1000:
            $ line = stat - 1000 - update

            if line > 0:
                show expression Text("+[line]", size = 40, color = "#FFFFFF") at stat_rising(Girl.sprite_location) onlayer screens
            elif line < 0:
                show expression Text("[line]", size = 40, color = "#FFFFFF") at stat_falling(Girl.sprite_location) onlayer screens

            if not Girl.had_chat[4]:
                $ update = 0
            else:
                $ update = stat - 1000

                $ setattr(Girl, flavor, 1000)

                if flavor == "love":
                    if Girl.had_chat[4] == 1:
                        $ flavor = "obedience"
                    elif Girl.had_chat[4] == 2:
                        $ flavor = "inhibition"
                    else:
                        $ update = 0
                elif flavor == "obedience":
                    if Girl.had_chat[4] == 3:
                        $ flavor = "inhibition"
                    elif Girl.had_chat[4] == 4:
                        $ flavor = "love"
                    else:
                        $ update = 0
                elif flavor == "inhibition":
                    if Girl.had_chat[4] == 5:
                        $ flavor = "obedience"
                    elif Girl.had_chat[4] == 6:
                        $ flavor = "love"
                    else:
                        $ update = 0

                $ stat = getattr(Girl, flavor)
                $ stat += update

                if flavor == "love":
                    $ shade = "#c11b17"
                elif flavor == "obedience":
                    $ shade = "#2554c7"
                elif flavor == "inhibition":
                    $ shade = "#FFF380"
                else:
                    $ shade = "#FFFFFF"

        if update > 0:
            show expression Text("+[update]", size = 40, color = shade) at stat_rising(Girl.sprite_location) onlayer screens
        elif update < 0:
            show expression Text("[update]", size = 40, color = shade) at stat_falling(Girl.sprite_location) onlayer screens

    $ stat = 1000 if stat > 1000 else stat

    $ setattr(Girl, flavor, stat)

    return

label set_Character_taboos:
    call check_taboo(Player)
    call check_who_is_present

    $ temp_Girls = Present[:]

    while temp_Girls:
        if temp_Girls[0] == JeanX and "nowhammy" not in JeanX.traits:
            $ temp_Girls[0].taboo = 0
        else:
            call check_taboo(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    return

label set_the_scene(location = None, show_Characters = True, fade = False, static = False):
    if fade:
        show black_screen onlayer black

        pause 0.4

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
            if focused_Girl not in Present:
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
            $ temp_Girls.remove(focused_Girl)
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

            if focused_Girl.teaching and Player.location == "bg_classroom":
                if renpy.showing(focused_Girl.tag + "_sprite"):
                    call hide_Girl(focused_Girl, transition = False)
                    call show_Girl(focused_Girl, sprite_layer = 1, color_transform = color_transform, animation_transform = teaching, transition = False)
                else:
                    call show_Girl(focused_Girl, sprite_layer = 1, color_transform = color_transform, animation_transform = teaching, transition = transition)
            elif focused_Girl.location == Player.location:
                if Player.location == "bg_restaurant" and renpy.showing(focused_Girl.tag + "_sprite"):
                    call hide_Girl(focused_Girl, transition = False)
                    call show_Girl(focused_Girl, x_position = stage_center, sprite_layer = 1, color_transform = color_transform, animation_transform = dining, transition = False)
                elif Player.location == "bg_restaurant":
                    call show_Girl(focused_Girl, x_position = stage_center, sprite_layer = 1, color_transform = color_transform, animation_transform = dining, transition = transition)
                elif renpy.showing(focused_Girl.tag + "_sprite"):
                    call hide_Girl(focused_Girl, transition = False)
                    call show_Girl(focused_Girl, x_position = stage_center, sprite_layer = 6, color_transform = color_transform, transition = False)
                else:
                    call show_Girl(focused_Girl, x_position = stage_center, sprite_layer = 6, color_transform = color_transform, transition = transition)
            elif renpy.showing(focused_Girl.tag + "_sprite"):
                call hide_Girl(focused_Girl)

        if Player.location == "bg_study" and time_index < 3:
            show Xavier_sprite zorder 3 at sprite_location(stage_left)
    else:
        call hide_all

    if fade:
        hide black_screen onlayer black

    return

label event_calls:
    if time_index == 2 and "going_on_date" in Player.daily_history and Player.location != "bg_campus":
        menu:
            "You have a date to get to, head for the square?"
            "Yes":
                $ entering = True

                jump campus
            "No":
                "Suit yourself. . ."

    if round <= 10:
        return

    if KittyX in active_Girls:
        if "Kate" not in KittyX.names and KittyX.location == Player.location and KittyX.inhibition >= 500:
            call Kitty_Kate

            return

    if "fix" not in Player.daily_history:
        call check_addiction

    if Player.location == "bg_player":
        $ event_Girls = active_Girls[:]

        while event_Girls and "asked_to_meet" not in event_Girls[0].daily_history:
            if "asked_to_meet" in event_Girls[0].daily_history:
                $ event_Girls = [event_Girls[0]]
            else:
                $ event_Girls.remove(event_Girls[0])
    else:
        $ event_Girls = []

    if not event_Girls:
        call check_if_shared
        call check_if_cheated
        call JumperCheck

        if time_index >= 2 and "fapcall" not in Player.daily_history:
            $ event_Girls = active_Girls[:]

            $ renpy.random.shuffle(event_Girls)

            while event_Girls:
                if "wants_to_masturbate" in event_Girls[0].daily_history:
                    call CalltoFap (event_Girls[0])

                    if not event_Girls:
                        return

                $ event_Girls.remove(event_Girls[0])

    $ event_Girls = active_Girls[:] if not event_Girls else event_Girls
    $ renpy.random.shuffle(event_Girls)

    while event_Girls:
        if "relationship" not in event_Girls[0].daily_history:
            if "stoodup" in event_Girls[0].traits:
                call Date_Stood_Up (event_Girls[0])

                return

            if event_Girls[0].broken_up[0] or "angry" in event_Girls[0].daily_history:
                pass
            elif not event_Girls[0].event_happened[0] and event_Girls[0].event_counter["sleepover"] >= 5:
                if event_Girls[0].location == Player.location or event_Girls[0] in Player.Party:
                    call expression event_Girls[0].tag + "_Key"
                    return
            elif event_Girls[0] == JeanX:
                if Player.location != "bg_classroom":
                    if JeanX.obedience >= 500 and "sir" not in JeanX.history:
                        call Jean_Sub
                    elif JeanX.obedience >= 800 and "master" not in JeanX.history:
                        call Jean_Master
                    elif JeanX.love >= 500 and "sexfriend" not in JeanX.history:
                        call Jean_Like
                    elif JeanX.love >= 800 and JeanX.obedience >= 600 and not JeanX.event_happened[5]:
                        call Jean_Love
                    elif "daddy" not in JeanX.player_petnames and approval_check(JeanX, 750, "L"):
                        if (Player.location == event_Girls[0].home or Player.location == "bg_player") and event_Girls[0].location == Player.location:
                            call Jean_Daddy

                    return
            elif event_Girls[0] == JubesX:
                pass
            elif "boyfriend" not in event_Girls[0].player_petnames and event_Girls[0].love >= 800 and event_Girls[0].event_happened[5] != 20 and event_Girls[0].tag + "_No" not in Player.traits:
                if event_Girls[0] == LauraX and LauraX.event_happened[5] == 3:
                    call Laura_Cleanhouse
                elif Player.Harem and event_Girls[0].tag + "_Yes" not in Player.traits:
                    call Poly_Start (event_Girls[0])
                elif Player.location == event_Girls[0].home or Player.location == "bg_player":
                    call expression event_Girls[0].tag + "_BF"
                else:
                    call ask_to_meet (event_Girls[0])

                return
            elif "lover" not in event_Girls[0].player_petnames and event_Girls[0].love >= 950 and event_Girls[0].event_happened[6] < 15:
                if Player.location == event_Girls[0].home or Player.location == "bg_player":
                    call expression event_Girls[0].tag + "_Love"
                else:
                    call ask_to_meet (event_Girls[0])

                return
            elif "sir" not in event_Girls[0].history and "sir" not in event_Girls[0].player_petnames and event_Girls[0].obedience >= 500:
                if Player.location == event_Girls[0].home or Player.location == "bg_player":
                    call expression event_Girls[0].tag + "_Sub"
                else:
                    call ask_to_meet (event_Girls[0])
                return
            elif "master" not in event_Girls[0].history and "master" not in event_Girls[0].player_petnames and event_Girls[0].obedience >= 850 and event_Girls[0].event_happened[8] < 2:
                if Player.location == event_Girls[0].home or Player.location == "bg_player":
                    call expression event_Girls[0].tag + "_Master"
                else:
                    call ask_to_meet (event_Girls[0])

                return
            elif "daddy" not in event_Girls[0].player_petnames and approval_check(event_Girls[0], 750, "L") and approval_check(event_Girls[0], 500, "O") and approval_check(event_Girls[0], 500, "I"):
                if (Player.location == event_Girls[0].home or Player.location == "bg_player") and event_Girls[0].location == Player.location:
                    call expression event_Girls[0].tag + "_Daddy"

                return
            elif "sex friend" not in event_Girls[0].player_petnames and event_Girls[0].inhibition >= 500:
                if event_Girls[0] == EmmaX:
                    if Player.location == "bg_classroom" and (EmmaX.teaching or EmmaX.location == "bg_classroom") and time_index == 2:
                        call Emma_Sexfriend
                        return
                elif event_Girls[0] == StormX:
                    if StormX.event_happened[9]:
                        pass
                    elif "traveling" in Player.recent_history and time_index < 2:
                        call Storm_Sexfriend

                        return
                elif Player.location == event_Girls[0].home or Player.location == "bg_player":
                    call expression event_Girls[0].tag + "_Sexfriend"

                    return
                elif event_Girls[0] in Player.Harem and event_Girls[0].location == Player.location:
                    call expression event_Girls[0].tag + "_Sexfriend"

                    return
                elif event_Girls[0] == LauraX:
                    call expression event_Girls[0].tag + "_Sexfriend"

                    return
            elif "fuck buddy" not in event_Girls[0].player_petnames and event_Girls[0].inhibition >= 800:
                if event_Girls[0] == RogueX:
                    if Player.location != event_Girls[0].location:
                        call expression event_Girls[0].tag + "_Fuckbuddy"

                        return
                elif event_Girls[0] == LauraX:
                    if Player.location == "bg_player" and event_Girls[0].location != Player.location:
                        call expression event_Girls[0].tag + "_Fuckbuddy"

                        return
                elif event_Girls[0] == StormX:
                    if Player.location == "bg_classroom" and time_index == 2 and weekday in (1,3):
                        call Storm_Fuckbuddy

                        return
                elif Player.location == event_Girls[0].home or Player.location == "bg_player":
                    call expression event_Girls[0].tag + "_Fuckbuddy"

                    return
                elif event_Girls[0] in Player.Harem and event_Girls[0].location == Player.location:
                    call expression event_Girls[0].tag + "_Fuckbuddy"

                    return

        $ event_Girls.remove(event_Girls[0])

    if "fix" in Player.daily_history:
        call check_addiction

    return

label traveling_event_calls(location):
    if location == "bg_campus":
        if "going_on_date" in Player.daily_history and time_index == 2:
            $ Player.drain_word("going_on_date", 0, 1)

            call DateNight

            return

    if location == "bg_classroom" and "met" not in KittyX.history:
        call meet_Kitty

        return

    if EmmaX in active_Girls:
        if location == "bg_classroom":
            if "noise" in Player.history and "attic" not in Player.history and EmmaX.teaching and EmmaX.location == "bg_classroom" and time_index < 2 and weekday < 5:
                call meet_Storm_ask_Emma

                return

            if time_index == 2 and weekday in [0, 2, 4]:
                if not Player.Party:
                    if "classcaught" not in EmmaX.history:
                        call Emma_Caught_Classroom

                        return
                    elif D20 <= 10 and "will_masturbate" in EmmaX.daily_history:
                        call Emma_Caught_Classroom

                        return

                if "detention" in Player.traits and not Player.Party:
                    call Emma_Detention

                    return

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
    #     if location == "bg_showerroom":
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

    if JubesX in active_Girls:
        if location in ["bg_classroom", "bg_dangerroom", "bg_campus", "bg_pool"]:
            if time_index < 3 and "sunshine" not in JubesX.history:
                call Jubes_Sunshine

                return

            if "sunshine" in JubesX.history and "mall" not in Player.history and time_index < 3 and JubesX.addiction < 50:
                call Jubes_Mall

                return

    return

label quick_event_calls:
    $ event_Girls = active_Girls[:]
    $ renpy.random.shuffle(event_Girls)

    while event_Girls:
        if event_Girls[0].location == Player.location:
            if event_Girls[0].lust >= 90:
                $ event_Girls[0].blushing = "_blush1"
                $ event_Girls[0].grool = 2
            elif event_Girls[0].lust >= 60:
                $ event_Girls[0].blushing = "_blush1"
                $ event_Girls[0].grool = 1
            else:
                $ event_Girls[0].grool = 0

            if taboo and event_Girls[0].lust >= 75:
                if event_Girls[0].inhibition > 800 or "exhibitionist" in event_Girls[0].traits:
                    "[event_Girls[0].name] gets a sly smile on her face and squirms a bit."
                elif event_Girls[0].inhibition > 500 and event_Girls[0].lust < 90:
                    "[event_Girls[0].name] looks a bit flushed and uncomfortable."
                elif Player.location != "bg_showerroom":
                    "[event_Girls[0].name] gets an embarrassed look on her face and suddenly leaves the room."

                    call remove_Girl(event_Girls[0])

                    if "no_masturbating" in event_Girls[0].traits:
                        $ event_Girls[0].add_word(1, 0,"wants_to_masturbate", 0, 0)

                        call CalltoFap(event_Girls[0])
                    else:
                        $ event_Girls[0].add_word(1, 0,"will_masturbate", 0, 0)
        else:
            if event_Girls[0].location == "bg_showerroom" and "showered" in event_Girls[0].daily_history:
                python:
                    for key in event_Girls[0].spunk.keys():
                        event_Girls[0].spunk[key] = False

                if event_Girls[0] == JubesX and JubesX.addiction > 60:
                    $ event_Girls[0].location = event_Girls[0].home
                else:
                    $ event_Girls[0].location = event_Girls[0].weekly_schedule[weekday][time_index]

                $ event_Girls[0].change_outfit()

        $ event_Girls.remove(event_Girls[0])

    return

label tenth_round:
    if Player.location not in bedrooms or Player.location != "bg_player":
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
    elif approval_check(Occupant, 1000, "LI") or approval_check(Occupant, 600, "OI"):
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
                elif G.location != Player.location or "lockedtravels" not in G.traits:
                    G.location = G.weekly_schedule[weekday][time_index]

                if G.location == "bg_teacher":
                    G.location = "bg_classroom"
                    G.teaching = True
                elif G.teaching:
                    G.teaching = False

                if G.location == "bg_showerroom":
                    G.add_word(1, "showered", "showered")

                if previous_location == Player.location and G.location != previous_location:
                    if "sleepover" in G.traits:
                        G.drain_word("sleepover", 0, 0, 1)

                    leaving_Girls.append(G)
                elif G.location == Player.location and G.location != previous_location:
                    arriving_Girls.append(G)
            else:
                G.location = Player.location

    while leaving_Girls:
        call expression leaving_Girls[0].tag + "_Leave"

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
                elif G.location == "bg_pool" and G.swimwear["outfit_active"]:
                    Outfit_name = "swimwear"
                elif G.location == "bg_showerroom":
                    Outfit_name = "shower"
                elif G.teaching:
                    Outfit_name = "teacher"

                G.change_Outfit(Outfit_name, instant = True)

    return

label wait:
    show black_screen onlayer black

    pause 0.4

    $ stack_depth = renpy.call_stack_depth()

    call checkout
    call reset_player

    if time_index < 3:
        $ time_index += 1

        $ Player.recent_history = []

        call set_Girls_locations
    else:
        $ time_index = 0
        $ day += 1

        if weekday < 6:
            $ weekday += 1
        else:
            $ weekday = 0

        $ day_of_week = week[weekday]

        $ Player.recent_history = []
        $ Player.daily_history = []
        $ Player.Party = []

        if being_punished:
            $ Player.cash += int(Player.income/2)

            if being_punished == 1:
                "Your punishment from Xavier has expired."

            $ being_punished -= 1
        else:
            $ Player.cash += Player.income

        $ Player.semen = Player.max_semen
        $ Player.spunk = False
        $ Player.reputation += 10 if Player.reputation < 800 else 0

        if "mandrill" in Player.traits:
            $ Player.traits.remove("mandrill")
        if "purple" in Player.traits:
            $ Player.traits.remove("purple")
        if "corruption" in Player.traits:
            $ Player.traits.remove("corruption")

        call check_favorite_actions
        call reset_all_girls_at_end
        call change_clothes

    $ multi_action = True

    $ current_time = time_options[(time_index)]

    $ round = 100

    call set_Character_taboos
    call who_likes_who

    if time_index == 3:
        call offscreen_studying

    call reset_all_girls_at_beginning

    $ Player.semen += 1
    $ Player.focus -= 5 if Player.focus >= 10 else 0

    if Player.level < 10 and Player.XP >= Player.XP_goal:
        $ Player.XP_goal = int((1.15*Player.XP_goal) + 100)
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

    call offscreen_lesbian
    call checkout

    pause 0.5

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

            G.addiction = 100 if G.addiction > 100 else G.addiction
            G.addiction = 0 if G.addiction < 0 else G.addiction

            G.addiction_rate = 10 if G.addiction_rate > 10 else G.addiction_rate
            G.addiction_rate = 0 if G.addiction_rate < 0 else G.addiction_rate

            G.thirst = 100 if G.thirst > 100 else G.thirst
            G.thirst = 0 if G.thirst < 0 else G.thirst

            G.remaining_actions = G.max_actions if G.remaining_actions > G.max_actions else G.remaining_actions
            G.remaining_actions = 0 if G.remaining_actions < 0 else G.remaining_actions

            if G.forced and G.event_counter["forced"] < 10:
                G.event_counter["forced"] += 1

            if G == LauraX:
                G.scent_timer = 0

    return

label reset_player:
    call get_dressed
    call stop_all_actions

    $ Player.focusing = False

    $ multi_action = True

    $ position_timer = 100

    $ Partner = None

    return

label reset_all_girls_at_end:
    python:
        total_SEXP = 0

        for G in all_Girls:
            total_SEXP += G.SEXP

            if G in active_Girls and G.location != Player.location:
                G.location = G.home

            if G.to_do:
                if G == LauraX:
                    if "pubes" in G.to_do:
                        G.pubes = "_hairy"
                        G.to_do.remove("pubes")

                    if "mission" in G.to_do:
                        G.pubes_counter -= 1

                        if G.pubes_counter >= 1:
                            G.location = "hold"
                        else:
                            G.history.append("dress0")
                            G.to_do.remove("mission")

                    if "cleanhouse" in G.to_do:
                        if LauraX in Player.Harem or not Player.Harem:
                            G.event_happened[5] = 2
                            G.to_do.remove("cleanhouse")

                        G.event_happened[5] -= 1 if G.event_happened[5] > 1 else 0
                else:
                    if "pubes" in G.to_do:
                        G.pubes_counter -= 1

                        if not G.pubes_counter:
                            G.pubes = "_hairy"
                            G.to_do.remove("pubes")

                if "shave" in G.to_do:
                    G.pubes = ""
                    G.to_do.remove("shave")

                if "ring" in G.to_do:
                    G.change_into(ring_body_piercings())
                    G.to_do.remove("ring")

                if "barbell" in G.to_do:
                    G.change_into(barbell_body_piercings())
                    G.to_do.remove("barbell")

            G.change_Outfit("sleepwear")

            G.addiction += G.addiction_rate
            G.addiction -= 3*G.resistance

            if "nonaddictive" in Player.traits:
                G.addiction_rate -= 2
                G.addiction -= 5
            elif "addictive" not in Player.traits:
                G.addiction_rate -= G.resistance

            G.remaining_actions = G.max_actions
            G.reputation = 0 if G.reputation < 0 else G.reputation
            G.reputation += 10 if G.reputation < 800 else 0
            G.reputation = 1000 if G.reputation > 1000 else G.reputation
            G.lust -= 5 if G.lust >= 50 else 0

            if G.SEXP >= 15:
                if G.SEXP >= 50:
                    G.thirst += 8 if G.thirst <= 70 else 4
                elif G.SEXP >= 25:
                    G.thirst += 5 if G.thirst <= 60 else 2
                else:
                    G.thirst += 3 if G.thirst <= 50 else 1

                G.thirst += 1 if G.lust >= 50 else 0

            if "will_masturbate" in G.daily_history and G.location != Player.location:
                G.lust = 25
                G.thirst -= int(G.thirst/2) if G.thirst >= 50 else int(G.thirst/4)
            elif "wants_to_masturbate" in G.daily_history:
                G.thirst += 10 if G.thirst <= 50 else 5

            for key in G.spunk.keys():
                G.spunk[key] = False

            if "lover" in G.player_petnames and G.love > 800:
                G.love += 10

            if "master" in G.player_petnames and G.obedience > 600:
                G.obedience += 10

            if "fuck buddy" in G.player_petnames:
                G.inhibition += 10

            G.todays_Outfit_name = G.Outfit_schedule[weekday]

    return

label offscreen_studying:
    python:
        Studiers = []

        for G in active_Girls:
            if G.location != Player.location and G.location in bedrooms:
                Studiers.append(G)

    if len(Studiers) < 2:
        return

    $ renpy.random.shuffle(Studiers)

    for GA in Studiers:
        for GB in Studiers:
            if GA != GB:
                GA.check_if_likes(GB, 800, 5, 1)
                GB.check_if_likes(GA, 800, 5, 1)

        GA.XP += 5

    return

label reset_all_girls_at_beginning:
    python:
        for G in all_Girls:
            G.remaining_actions += 1 if time_index != 0 else 0
            G.session_orgasms = 0

            if G.lust >= 70 or G.thirst >= 30 or (renpy.random.randint(1, 40) + G.lust)>= 70:
                if "no_masturbating" in G.traits:
                    G.add_word(1, 0, "wants_to_masturbate", 0, 0)
                else:
                    G.add_word(1, 0, "will_masturbate", 0, 0)

            if "lesbian" in G.recent_history:
                G.thirst -= int(G.thirst/2)
                G.lust = 20

            G.forced = False

            if G.location == "bg_classroom" or G.location == "bg_dangerroom" or G.teaching:
                G.XP += 10

            G.blushing = ""
            G.wet = False
            G.held_item = None

            G.addiction += G.addiction_rate
            G.addiction_rate -= G.resistance if G.addiction_rate > 3 else 0

            if G.taboo and G.Wardrobe.current_Outfit.shame and G in active_Girls:
                stat_change = int((G.taboo*G.Wardrobe.current_Outfit.shame)/200)

                G.change_stat("obedience", 90, stat_change)
                G.change_stat("inhibition", 90, stat_change)
                G.reputation -= stat_change

            G.love -= 5*G.recent_history.count("unsatisfied")

            G.recent_history = []

            if "angry" in G.daily_history:
                G.recent_history.append("angry")

            if time_index == 0:
                G.daily_history = []
            elif time_index == 3 and "going_on_date" in G.daily_history and "stoodup" not in G.traits:
                Player.drain_word("going_on_date", 0, 1)

                G.traits.append("stoodup")

            if G.Wardrobe.current_Outfit.Clothes["buttplug"]:
                bonus = 1
            else:
                bonus = 0

            if G.used_to_anal < 2:
                if G.action_counter["anal"] + G.action_counter["dildo_ass"] + bonus >= 15:
                    G.used_to_anal = 2
                elif G.action_counter["anal"] + G.action_counter["dildo_ass"] + bonus >= 3:
                    G.used_to_anal = 1

            G.XP = 3330 if G.XP > 3330 else G.XP

            if G.XP >= G.XP_goal and G.level < 10:
                G.XP_goal = int((1.15*G.XP_goal) + 100)
                G.level += 1
                G.stat_points += 1

                renpy.say(None, "[G.name]'s leveled up! I bet she has some new tricks to learn.")

                if G.level == 10:
                    renpy.say(None, "[G.name]'s reached max level!")

            if G == LauraX:
                G.addiction_rate -= (2*G.resistance) if G.addiction_rate > 5 else 0
            elif G == JubesX and "met" in JubesX.history:
                G.addiction_rate = 2 if G.addiction_rate < 2 else G.addiction_rate

                if "sunshine" not in JubesX.history:
                    G.addiction = 40 if G.addiction > 40 else G.addiction

            G.set_default_faces()
            G.change_face()

    return

label offscreen_lesbian:
    if "threesome" not in EmmaX.history:
        if EmmaX.thirst >= 30 and approval_check(EmmaX, 800, "I"):
            $ EmmaX.history.append("threesome")

    python:
        Girls = []

        for G in active_Girls:
            if G not in Player.Party or G.location != Player.location:
                if G == RogueX and "touch" not in RogueX.traits:
                    pass
                elif G == EmmaX and "threesome" not in EmmaX.history:
                    pass
                elif approval_check(G, 500, "I", Alt = [[EmmaX, JeanX], 300]) and G.thirst >= 60:
                    if "monogamous" not in G.traits or G.broken_up:
                        Girls.append(G)

    if not Girls:
        return

    python:
        renpy.random.shuffle(Girls)

        partner_found = False

        while not partner_found:
            if Girls[0] == JeanX and G.likes[Girls[0].tag] >= 500:
                partner_found = True
            elif Girls[0] in Player.Harem and G in Player.Harem and Girls[0].likes[G.tag] >= 600:
                partner_found = True
            elif G.likes[Girls[0].tag] >= 800 and Girls[0].likes[G.tag] >= 800:
                partner_found = True
            elif G.thirst >= 90 and Girls[0].likes[G.tag] >= 600:
                partner_found = True
            else:
                Girls.remove(G)

    if not partner_found:
        return

    $ Girls = [Girls[0], Girls[1]]

    if Player.location != Girls[0].home:
        $ Girls[0].location = Girls[0].home
        $ Girls[1].location = Girls[0].home
    elif Player.location != Girls[1].home:
        $ Girls[0].location = Girls[1].home
        $ Girls[1].location = Girls[1].home

    python:
        for GA in Girls:
            GA.add_word(1, "lesbian", 0, 0, 0)

            for GB in Girls:
                if GA != GB:
                    GA.check_if_likes(GB, 700, 15, 1)
                    GA.check_if_likes(GB, 900, 10, 1)
                    GA.check_if_likes(GB, 1000, 5, 1)

            GA.change_stat("lust", 60, 20)
            GA.thirst -= 5

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

    call stop_all_actions

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

        jump girls_room
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
                call remove_Girl(Girls[0], transition = None)
            else:
                call remove_Girl(Girls[0])

            $ Girls.remove(Girls[0])

    return

label stop_all_actions(visual = False):
    $ Player.primary_action = None
    $ Player.secondary_action = None
    $ girl_secondary_action = None
    $ second_girl_main_action = None
    $ second_girl_secondary_action = None

    $ temp_Girls = Present[:]

    while temp_Girls:
        $ temp_Girls[0].main_action = None
        $ temp_Girls[0].secondary_action = None

        if visual:
            call show_full_body(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    return

label ask_to_meet(Girl):
    if "asked_to_meet" not in Girl.daily_history and Girl.location != Player.location:
        "[Girl.name] asks if you could meet her in your room later."

        $ Girl.add_word(1, "asked_to_meet", "asked_to_meet", 0, 0)

        $ Player.add_word(1, 0, "meet girl", 0, 0)

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

label coitus_interruptus(Partners, Interrupters):
    if Partners in all_Girls:
        $ Partners = [Partners]

    if Interrupters in all_Girls:
        $ Interrupters = [Interrupters]

    if EmmaX in Partners and "threesome" not in EmmaX.history:
        python:
            for G in Interrupters:
                G.add_word(1, 0, 0, "saw with " + EmmaX.tag)

        ch_e "I. . . This isn't what it looks like. . ."

        if Player.location == EmmaX.home:
            $ Player.location = "bg_door"

            call hide_Girl(EmmaX, transition == False)

            $ number = len(Partners) + len(Interrupters)

            "She shoves the [number] of you out of her room and slams the door."

            jump reset_location
        else:
            call remove_Girl(EmmaX)

            "She seems uncomfortable with the situation and leaves the room."
            "Perhaps you should ask her about it later."

            $ door_locked = False

            return True

    $ Partner = Partners[0]
    $ Interrupter = Interrupters[0]

    if len(Partners) + len(Interrupters) == 2:
        if "poly " + Partner.tag in Interrupter.traits or (Partner in Player.Harem and Interrupter in Player.Harem):
            pass
        else:
            if approval_check(Partner, 1500, taboo_modifier=2, Bonus = (Interrupter.likes[Partner.tag] - 500)):
                $ Partner.change_face("sexy", 1)
                call change_Girl_stat(Partner, "obedience", 90, 5)
                call change_Girl_stat(Partner, "inhibition", 90, 5)
                call change_Girl_stat(Partner, "lust", 90, 3)
            else:
                $ Partner.change_face("angry", 1)

                if Partner == RogueX:
                    ch_r "Hey, [Interrupter.tag], we're a little busy here?"
                elif Partner == KittyX:
                    ch_k "Um, [Interrupter.tag]? Read the room?"
                elif Partner == EmmaX:
                    ch_e "[Interrupter.tag], could you please leave?"
                elif Partner == LauraX:
                    ch_l "Scram, [Interrupter.tag]."
                elif Partner == JeanX:
                    ch_j "Leave, [Interrupter.tag]."
                elif Partner == StormX:
                    ch_s "Would you mind give us some space?"
                elif Partner == JubesX:
                    ch_v "Yeah, we were. . . busy."

                $ Interrupter.add_word(1, 0, 0,"saw with " + Partner.tag)

                if Interrupter == RogueX:
                    $ Interrupter.change_face("perplexed", 2)

                    ch_r "Oh, sorry about that! I'll head out."
                elif Interrupter == KittyX:
                    $ Interrupter.change_face("perplexed", 2)

                    ch_k "Oh! Sorrysorrysorry!"
                elif Interrupter == EmmaX:
                    $ Interrupter.change_face("bemused", 2)

                    ch_e "I wouldn't want to spoil the mood. . ."
                elif Interrupter == LauraX:
                    ch_l "Oh, sure. Whatever."
                elif Interrupter == JeanX:
                    $ Interrupter.change_face("bemused", 1)

                    ch_j "Fine."
                elif Interrupter == StormX:
                    $ Interrupter.change_face("bemused", 1)

                    ch_s "Yes. . ."
                elif Interrupter == JubesX:
                    $ Interrupter.change_face("perplexed", 2)

                    ch_v "Oh, yes! Sorry!"

                $ Partner.change_face("sexy", 1)

                $ Interrupter.change_face("sad", 1)

                call remove_Girl(Interrupter)

                return False

        if Partner == RogueX:
            ch_r "Oh, [Interrupter.tag], did you want to join in?"
        elif Partner == KittyX:
            ch_k "Um, [Interrupter.tag]? Did you want something?"
        elif Partner == EmmaX:
            ch_e "Oh, [Interrupter.tag]. . . care to join us?"
        elif Partner == LauraX:
            ch_l "Oh, hey, [Interrupter.tag]."
        elif Partner == JeanX:
            ch_j "Hey."
        elif Partner == StormX:
            ch_s "Oh, hello [Interrupter.tag], did you want to join in?"
        elif Partner == JubesX:
            ch_v "Hey, [Interrupter.tag], did you need something?"
    elif len(Partners) > 1 and len(Interrupters) == 1:
        $ temp_Girls = Partners[:]

        while temp_Girls:
            if "poly " + temp_Girls[0].tag in Interrupter.traits or (temp_Girls[0] in Player.Harem and Interrupter in Player.Harem):
                pass
            else:
                if approval_check(temp_Girls[0], 1500, taboo_modifier=2, Bonus = (Interrupter.likes[temp_Girls[0].tag] - 500)):
                    $ temp_Girls[0].change_face("sexy", 1)
                    call change_Girl_stat(temp_Girls[0], "obedience", 90, 5)
                    call change_Girl_stat(temp_Girls[0], "inhibition", 90, 5)
                    call change_Girl_stat(temp_Girls[0], "lust", 90, 3)
                else:
                    $ temp_Girls[0].change_face("angry", 1)

                    if temp_Girls[0] == RogueX:
                        ch_r "Hey, [Interrupter.tag], we're a little busy here?"
                    elif temp_Girls[0] == KittyX:
                        ch_k "Um, [Interrupter.tag]? Read the room?"
                    elif temp_Girls[0] == EmmaX:
                        ch_e "[Interrupter.tag], could you please leave?"
                    elif temp_Girls[0] == LauraX:
                        ch_l "Scram, [Interrupter.tag]."
                    elif temp_Girls[0] == JeanX:
                        ch_j "Leave, [Interrupter.tag]."
                    elif temp_Girls[0] == StormX:
                        ch_s "Would you mind give us some space?"
                    elif temp_Girls[0] == JubesX:
                        ch_v "Yeah, we were. . . busy."

                    $ Interrupter.add_word(1, 0, 0,"saw with " + temp_Girls[0].tag)

                    if Interrupter == RogueX:
                        $ Interrupter.change_face("perplexed", 2)

                        ch_r "Oh, sorry about that! I'll head out."
                    elif Interrupter == KittyX:
                        $ Interrupter.change_face("perplexed", 2)

                        ch_k "Oh! Sorrysorrysorry!"
                    elif Interrupter == EmmaX:
                        $ Interrupter.change_face("bemused", 2)

                        ch_e "I wouldn't want to spoil the mood. . ."
                    elif Interrupter == LauraX:
                        ch_l "Oh, sure. Whatever."
                    elif Interrupter == JeanX:
                        $ Interrupter.change_face("bemused", 1)

                        ch_j "Fine."
                    elif Interrupter == StormX:
                        $ Interrupter.change_face("bemused", 1)

                        ch_s "Yes. . ."
                    elif Interrupter == JubesX:
                        $ Interrupter.change_face("perplexed", 2)

                        ch_v "Oh, yes! Sorry!"

                    $ temp_Girls[0].change_face("sexy", 1)

                    $ Interrupter.change_face("sad", 1)

                    call remove_Girl(Interrupter)

                    return False

            if temp_Girls[0] == RogueX:
                ch_r "Oh, [Interrupter.tag], did you want to join in?"
            elif temp_Girls[0] == KittyX:
                ch_k "Um, [Interrupter.tag]? Did you want something?"
            elif temp_Girls[0] == EmmaX:
                ch_e "Oh, [Interrupter.tag]. . . care to join us?"
            elif temp_Girls[0] == LauraX:
                ch_l "Oh, hey, [Interrupter.tag]."
            elif temp_Girls[0] == JeanX:
                ch_j "Hey."
            elif temp_Girls[0] == StormX:
                ch_s "Oh, hello [Interrupter.tag], did you want to join in?"
            elif temp_Girls[0] == JubesX:
                ch_v "Hey, [Interrupter.tag], did you need something?"

            $ temp_Girls.remove(temp_Girls[0])
    elif len(Partners) == 1 and len(Interrupters) > 1:
        $ temp_Girls = Interrupters[:]

        while temp_Girls:
            if "poly " + Partner.tag in temp_Girls[0].traits or (Partner in Player.Harem and temp_Girls[0] in Player.Harem):
                if Partner == RogueX:
                    ch_r "Oh, [temp_Girls[0].tag], did you want to join in?"
                elif Partner == KittyX:
                    ch_k "Um, [temp_Girls[0].tag]? Did you want something?"
                elif Partner == EmmaX:
                    ch_e "Oh, [temp_Girls[0].tag]. . . care to join us?"
                elif Partner == LauraX:
                    ch_l "Oh, hey, [temp_Girls[0].tag]."
                elif Partner == JeanX:
                    ch_j "Hey."
                elif Partner == StormX:
                    ch_s "Oh, hello [temp_Girls[0].tag], did you want to join in?"
                elif Partner == JubesX:
                    ch_v "Hey, [temp_Girls[0].tag], did you need something?"

                $ temp_Girls.remove(temp_Girls[0])
            else:
                if approval_check(Partner, 1500, taboo_modifier=2, Bonus = (temp_Girls[0].likes[Partner.tag] - 500)):
                    $ Partner.change_face("sexy", 1)
                    call change_Girl_stat(Partner, "obedience", 90, 5)
                    call change_Girl_stat(Partner, "inhibition", 90, 5)
                    call change_Girl_stat(Partner, "lust", 90, 3)

                    if Partner == RogueX:
                        ch_r "Oh, [temp_Girls[0].tag], did you want to join in?"
                    elif Partner == KittyX:
                        ch_k "Um, [temp_Girls[0].tag]? Did you want something?"
                    elif Partner == EmmaX:
                        ch_e "Oh, [temp_Girls[0].tag]. . . care to join us?"
                    elif Partner == LauraX:
                        ch_l "Oh, hey, [temp_Girls[0].tag]."
                    elif Partner == JeanX:
                        ch_j "Hey."
                    elif Partner == StormX:
                        ch_s "Oh, hello [temp_Girls[0].tag], did you want to join in?"
                    elif Partner == JubesX:
                        ch_v "Hey, [temp_Girls[0].tag], did you need something?"

                    $ temp_Girls.remove(temp_Girls[0])
                else:
                    $ Partner.change_face("angry", 1)

                    if Partner == RogueX:
                        ch_r "Hey, [temp_Girls[0].tag], we're a little busy here?"
                    elif Partner == KittyX:
                        ch_k "Um, [temp_Girls[0].tag]? Read the room?"
                    elif Partner == EmmaX:
                        ch_e "[temp_Girls[0].tag], could you please leave?"
                    elif Partner == LauraX:
                        ch_l "Scram, [temp_Girls[0].tag]."
                    elif Partner == JeanX:
                        ch_j "Leave, [temp_Girls[0].tag]."
                    elif Partner == StormX:
                        ch_s "Would you mind give us some space, [temp_Girls[0].tag]?"
                    elif Partner == JubesX:
                        ch_v "Yeah, we were. . . busy."

                    $ temp_Girls[0].add_word(1, 0, 0,"saw with " + Partner.tag)

                    if temp_Girls[0] == RogueX:
                        $ temp_Girls[0].change_face("perplexed", 2)

                        ch_r "Oh, sorry about that! I'll head out."
                    elif temp_Girls[0] == KittyX:
                        $ temp_Girls[0].change_face("perplexed", 2)

                        ch_k "Oh! Sorrysorrysorry!"
                    elif temp_Girls[0] == EmmaX:
                        $ temp_Girls[0].change_face("bemused", 2)

                        ch_e "I wouldn't want to spoil the mood. . ."
                    elif temp_Girls[0] == LauraX:
                        ch_l "Oh, sure. Whatever."
                    elif temp_Girls[0] == JeanX:
                        $ temp_Girls[0].change_face("bemused", 1)

                        ch_j "Fine."
                    elif temp_Girls[0] == StormX:
                        $ temp_Girls[0].change_face("bemused", 1)

                        ch_s "Yes. . ."
                    elif temp_Girls[0] == JubesX:
                        $ temp_Girls[0].change_face("perplexed", 2)

                        ch_v "Oh, yes! Sorry!"

                    $ Partner.change_face("sexy", 1)

                    $ temp_Girls[0].change_face("sad", 1)

                    call remove_Girl(temp_Girls[0])

                    $ temp_Girls.remove(temp_Girls[0])

                    if not temp_Girls:
                        return False

    return

label Girls_arrive(arriving_Girls):
    if arriving_Girls in all_Girls:
        $ arriving_Girls = [arriving_Girls]

    while len(arriving_Girls) > 2:
        $ arriving_Girls.remove(arriving_Girls[-1])

    python:
        Primary = None

        for G in arriving_Girls:
            if Player.location == G.home:
                Primary = G

                break
            elif G == JeanX:
                Primary = JeanX

    if not Primary:
        $ Primary = arriving_Girls[0]

    if len(arriving_Girls) > 1:
        $ Secondary = arriving_Girls[0] if Primary != arriving_Girls[0] else arriving_Girls[1]

        if len(arriving_Girls) > 3:
            $ line = Primary.name + " and a few others"
        elif len(arriving_Girls) > 2:
            $ line = Primary.name + " and a couple others"
        else:
            $ line = Primary.name + " and " + Secondary.name
    else:
        $ Secondary = None

        $ line = Primary.name

    if Player.primary_action:
        $ Partners = focused_Girl

    if door_locked and KittyX not in arriving_Girls:
        $ Player.add_word(1, "interruption")

        call locked_door(arriving_Girls)

        if not _return:
            return False
    else:
        if Player.location == "bg_campus" or Player.location == "bg_pool":
            if len(arriving_Girls) > 1:
                "Suddenly, [line] round a corner."
            else:
                "Suddenly, [line] rounds a corner."
        elif Player.location == "bg_classroom":
            if len(arriving_Girls) > 1:
                "[line] walk into the room."
            else:
                "[line] walks into the room."
        else:
            if Primary == KittyX:
                "You look to the door just as [Primary.name] phases into the room."

                if Secondary and door_locked:
                    "You hear a \"thump\" as if someone was trying to follow her."
                    ch_k "Oops!"
                    "[Primary.name] turns back and unlocks the door."

                    $ door_locked = False
            else:
                if len(arriving_Girls) > 1:
                    "[line] enter the room."
                else:
                    "[line] enters the room."

        call add_Girls(arriving_Girls)

        if Player.primary_action:
            call coitus_interruptus(Partners, arriving_Girls)

            if not _return:
                return False

        if Player.location == "bg_player":
            if Primary == RogueX:
                if Secondary:
                    ch_r "Hey, [RogueX.player_petname], can we come in?"
                else:
                    ch_r "Hey, [RogueX.player_petname], can I come in?"
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
                ch_j "Hey, [JeanX.player_petname]."
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
                    $ line = "sure"
                "Not right now, maybe later.":
                    $ line = "later"
                "No.":
                    $ line = "no"

            if line == "sure":
                call change_Girl_stat(Primary, "love", 80, 1)
                call change_Girl_stat(Primary, "obedience", 50, 2)
                call change_Girl_stat(Primary, "inhibition", 50, 2)

                if Primary == RogueX:
                    ch_r "Thanks."
                elif Primary == KittyX:
                    call change_Girl_stat(Primary, "inhibition", 50, 1)

                    ch_k "Cool."
                elif Primary == EmmaX:
                    ch_e "Good."
                elif Primary == LauraX:
                    call change_Girl_stat(Primary, "love", 50, 1)
                    call change_Girl_stat(Primary, "obedience", 60, 1)
                elif Primary == StormX:
                    ch_s "Good."
                elif Primary == JubesX:
                    ch_v "Nice."

                if Secondary:
                    call change_Girl_stat(Secondary, "love", 80, 1)
                    call change_Girl_stat(Secondary, "obedience", 50, 2)
                    call change_Girl_stat(Secondary, "inhibition", 50, 2)
            elif line == "later":
                $ Primary.change_face("confused")
                call change_Girl_stat(Primary, "love", 60, -1, 1)
                call change_Girl_stat(Primary, "obedience", 70, 5)

                if Secondary and Secondary != JeanX:
                    $ Secondary.change_face("confused")
                    call change_Girl_stat(Secondary, "love", 60, -1, 1)
                    call change_Girl_stat(Secondary, "obedience", 70, 5)

                    if Primary == RogueX:
                        ch_r "Um, ok, we'll go then."
                    elif Primary == KittyX:
                        call change_Girl_stat(KittyX, "love", 60, -1, 1)
                        call change_Girl_stat(KittyX, "obedience", 70, 2)

                        ch_k "Oh[KittyX.like]we'll get going then."
                    elif Primary == EmmaX:
                        call change_Girl_stat(EmmaX, "love", 90, -2)
                        call change_Girl_stat(EmmaX, "obedience", 30, -7)

                        ch_e "If that's how you wish to play it. . ."
                    elif Primary == LauraX:
                        call change_Girl_stat(LauraX, "love", 90, -2)
                        call change_Girl_stat(LauraX, "obedience", 30, -7)

                        ch_l "Ok, later."
                    elif Primary == StormX:
                        ch_s "Ah, then we'll leave you to it."
                    elif Primary == JubesX:
                        ch_v "Oh. Ok. . ."
                elif Primary == RogueX:
                    ch_r "Um, ok."
                elif Primary == KittyX:
                    call change_Girl_stat(KittyX, "love", 60, -1, 1)
                    call change_Girl_stat(KittyX, "obedience", 70, 2)

                    ch_k "Oh[KittyX.like]I'll get going then."
                elif Primary == EmmaX:
                    call change_Girl_stat(EmmaX, "love", 90, -2)
                    call change_Girl_stat(EmmaX, "obedience", 30, -7)

                    ch_e "If that's how you wish to play it. . ."
                elif Primary == LauraX:
                    call change_Girl_stat(LauraX, "love", 90, -2)
                    call change_Girl_stat(LauraX, "obedience", 30, -7)

                    ch_l "Ok, later."
                elif Primary == StormX:
                    ch_s "Ah, then I'll leave you to it."
                elif Primary == JubesX:
                    ch_v "Oh. Ok. . ."

                if JeanX in arriving_Girls:
                    $ arriving_Girls.remove(JeanX)

                    $ Primary = JeanX
                    $ Secondary = None

                call remove_Girl(arriving_Girls)

                if JeanX == Primary:
                    ch_j "Uh-huh."

                    "She doesn't leave."
            elif line == "no":
                call change_Girl_stat(Primary, "obedience", 50, 5)

                if approval_check(Primary, 1800) or approval_check(Primary, 500, "O"):
                    call change_Girl_stat(Primary, "obedience", 80, 2)

                    if Primary == RogueX:
                        ch_r "I guess that's ok. See you later then."
                    elif Primary == KittyX:
                        ch_k "If you want some alone time. . ."
                    elif Primary == EmmaX:
                        call change_Girl_stat(EmmaX, "obedience", 50, 2)

                        ch_e "I suppose you can have your personal space. . ."
                    elif Primary == LauraX:
                        ch_l "Not a problem."
                    elif Primary == StormX:
                        ch_s ". . . very well. . ."
                    elif Primary == JubesX:
                        ch_v "Oh. Ok. . ."
                else:
                    $ Primary.change_face("angry")
                    call change_Girl_stat(Primary, "love", 60, -5, 1)
                    call change_Girl_stat(Primary, "love", 80, -2)
                    call change_Girl_stat(Primary, "obedience", 80, 3)
                    call change_Girl_stat(Primary, "inhibition", 50, 1)

                    if Primary == RogueX:
                        ch_r "Well fine!"
                    elif Primary == KittyX:
                        call change_Girl_stat(KittyX, "love", 80, -2)
                        call change_Girl_stat(KittyX, "obedience", 80, 2)

                        ch_k "Jerk!"
                    elif Primary == EmmaX:
                        call change_Girl_stat(EmmaX, "love", 90, -2)
                        call change_Girl_stat(EmmaX, "obedience", 80, 3)

                        ch_e "We'll see how long that attitude lasts. . ."
                    elif Primary == LauraX:
                        call change_Girl_stat(LauraX, "love", 90, -2)

                        "She seems upset."
                    elif Primary == StormX:
                        ch_s ". . . I see. . ."
                    elif Primary == JubesX:
                        ch_v "Oh, so you're going to be like -that-. . ."

                if Secondary and Secondary != JeanX:
                    call change_Girl_stat(Secondary, "obedience", 50, 5)

                    if approval_check(Secondary, 1800) or approval_check(Secondary, 500, "O"):
                        call change_Girl_stat(Secondary, "obedience", 80, 2)

                        if Secondary == RogueX:
                            ch_r "I guess that's ok. See you later then."
                        elif Secondary == KittyX:
                            ch_k "If you want some alone time. . ."
                        elif Secondary == EmmaX:
                            call change_Girl_stat(EmmaX, "obedience", 50, 2)

                            ch_e "I suppose you can have your personal space. . ."
                        elif Secondary == LauraX:
                            ch_l "Not a problem."
                        elif Primary == StormX:
                            ch_s ". . . very well. . ."
                        elif Primary == JubesX:
                            ch_v "Oh. Ok. . ."
                    else:
                        $ Secondary.change_face("angry")
                        call change_Girl_stat(Secondary, "love", 60, -5, 1)
                        call change_Girl_stat(Secondary, "love", 80, -2)
                        call change_Girl_stat(Secondary, "obedience", 80, 3)
                        call change_Girl_stat(Secondary, "inhibition", 50, 1)

                        if Secondary == RogueX:
                            ch_r "Well fine!"
                        elif Secondary == KittyX:
                            call change_Girl_stat(KittyX, "love", 80, -2)
                            call change_Girl_stat(KittyX, "obedience", 80, 2)

                            ch_k "Jerk!"
                        elif Secondary == EmmaX:
                            call change_Girl_stat(EmmaX, "love", 90, -2)
                            call change_Girl_stat(EmmaX, "obedience", 80, 3)

                            ch_e "We'll see how long that attitude lasts. . ."
                        elif Secondary == LauraX:
                            call change_Girl_stat(LauraX, "love", 90, -2)

                            "She seems upset."
                        elif Primary == StormX:
                            ch_s ". . . I see. . ."
                        elif Primary == JubesX:
                            ch_v "Oh, so you're going to be like -that-. . ."

                if JeanX in arriving_Girls:
                    $ arriving_Girls.remove(JeanX)

                    $ Primary = JeanX
                    $ Secondary = None

                if len(arriving_Girls) == 1:
                    "[arriving_Girls[0].name] storms out."
                else:
                    "The girls storm out."

                    if StormX in arriving_Girls:
                        "-so to speak."

                    if Primary == JeanX:
                        ch_j "Uh-huh."

                        "[Primary.name] doesn't leave."
        elif Player.location in bedrooms:
            if Player.location == Primary.home:
                if "angry" in Primary.daily_history:
                    $ Primary.change_face("bemused", 1,brows = "angry")

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
                elif time_index > 2 and approval_check(Primary, 1000, "LI") and approval_check(Primary, 600, "OI"):
                    if Primary == RogueX:
                        ch_r "Oh, hey, [RogueX.player_petname], it's pretty late, but I guess you can stick around for a bit."
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
                        ch_v "Kinda late, [JubesX.player_petname], s'up?"

                    $ line = "stay"
                elif approval_check(Primary, 1300) or approval_check(Primary, 500, "O") or Primary == JubesX:
                    if Primary == RogueX:
                        ch_r "Oh, hey, [RogueX.player_petname], nice to see you here."
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
                        ch_v "Hey, [JubesX.player_petname], s'up?"

                    $ line = "stay"
                elif time_index > 2:
                    if Primary == RogueX:
                        ch_r "Oh, hey, [RogueX.player_petname], it's kind late, could you head out of here?"
                    elif Primary == KittyX:
                        ch_k "Oh, hey, [KittyX.player_petname]. It's kind of late, could you come back tomorrow?"
                    elif Primary == EmmaX:
                        ch_e "Oh, hello, [EmmaX.player_petname]. It's a bit late, could you come back tomorrow?"
                    elif Primary == LauraX:
                        ch_l "Oh, hey, it's late."
                    elif Primary == JeanX:
                        ch_j "You -can- tell time, right?"
                    elif Primary == StormX:
                        ch_s "I'm afraid that the hour is a bit late for visits. . ."
                elif approval_check(Primary, 600, "LI") or approval_check(Primary, 300, "OI"):
                    if Primary == RogueX:
                        ch_r "Oh, hey, [RogueX.player_petname]. You can stick around, I guess."
                    elif Primary == KittyX:
                        ch_k "Oh, hey, [KittyX.player_petname], what's up?"
                    elif Primary == EmmaX:
                        ch_e "Oh, hello, [EmmaX.player_petname], can I help you with anything?"
                    elif Primary == LauraX:
                        ch_l "Oh, hey, [LauraX.player_petname]."
                    elif Primary == JeanX:
                        ch_j "Um, hello?"
                    elif Primary == StormX:
                        ch_s "Oh, yes? Did you need something?"
                    elif Primary == JubesX:
                        ch_v "Hey, [JubesX.player_petname], s'up?"

                    $ line = "stay"
                else:
                    if Primary == RogueX:
                        ch_r "Hey, [RogueX.player_petname], I'm not sure why you're here, but I'd rather you leave."
                    elif Primary == KittyX:
                        ch_k "Hey, [KittyX.player_petname], what are you even doing here?"
                        ch_k "Could you[KittyX.like]get out?"
                    elif Primary == EmmaX:
                        ch_e "Oh, hello, [EmmaX.player_petname]?"
                        ch_e "Did you have a reason to be visiting me?"
                    elif Primary == LauraX:
                        $ Primary.change_face("confused")

                        ch_l "Hey, [LauraX.player_petname], why are you here?"
                    elif Primary == JeanX:
                        $ Primary.change_face("confused")

                        ch_j "I didn't invite you here."
                    elif Primary == StormX:
                        ch_s "I'm afraid that this is not a good time."
                    elif Primary == JubesX:
                        ch_v "Hey, [JubesX.player_petname]? Not a good time."

                if line != "stay":
                    menu:
                        extend ""
                        "Sure, ok.":
                            call change_Girl_stat(Primary, "love", 80, 1)
                            call change_Girl_stat(Primary, "obedience", 50, 2)
                            call change_Girl_stat(Primary, "inhibition", 50, 2)

                            Primary.voice "Thanks."

                            "You head back to your room."
                        "Sorry, I'll go.":
                            $ Primary.change_face("smile")
                            call change_Girl_stat(Primary, "love", 90, 2)
                            call change_Girl_stat(Primary, "obedience", 50, 3)

                            Primary.voice "Thanks."

                            "You head back to your room."
                        "Are you sure I can't stay?":
                            if "angry" in Primary.daily_history:
                                $ Primary.change_face("angry")

                                if Primary == RogueX:
                                    ch_r "What part of \"no\" don't ya get?"
                                elif Primary == KittyX:
                                    ch_k "I think I said {i}NO!{/i}"
                                elif Primary == EmmaX:
                                    ch_e "I believe I said {i}no.{/i}"
                                elif Primary == LauraX:
                                    ch_l "[[growls] 0. . .You probably shouldn't."
                                elif Primary == JeanX:
                                    ch_j "Oh, bad call, [Primary.player_petname]"
                                elif Primary == StormX:
                                    ch_s "Quite certain."
                                elif Primary == JubesX:
                                    ch_v "Oh, let me check. . ."

                                    $ Primary.change_face("angry", eyes = "side")

                                    ch_v ". . ."

                                    $ Primary.change_face("angry", mouth = "open")

                                    ch_v "-YES.-"

                                    $ Primary.change_face("angry")
                            elif time_index > 2 and approval_check(Primary, 800, "LI") and approval_check(Primary, 400, "OI"):
                                $ Primary.change_face("sadside")

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

                                $ line = "stay"
                            elif time_index > 2:
                                if Primary == RogueX:
                                    ch_r "No way, [RogueX.player_petname]. Try again tomorrow."
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

                                    $ line = "stay"
                            elif approval_check(Primary, 750):
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

                                $ line = "stay"
                            else:
                                $ Primary.change_face("angry")
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

                            if line != "stay":
                                call change_Girl_stat(Primary, "love", 80, -1)
                                call change_Girl_stat(Primary, "inhibition", 50, 3)

                                "[Primary.name] kicks you out of the room."
                        "I'm sticking around, thanks.":
                            if "angry" in Primary.daily_history or (not approval_check(Primary, 1800) and not approval_check(Primary, 500, "O")):
                                $ Primary.change_face("angry")

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
                                $ Primary.change_face("sad")
                                call change_Girl_stat(Primary, "obedience", 80, 5)

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

                                $ line = "stay"

                            if line != "stay":
                                call change_Girl_stat(Primary, "love", 60, -5, 1)
                                call change_Girl_stat(Primary, "love", 80, -5)
                                call change_Girl_stat(Primary, "obedience", 50, 2)
                                call change_Girl_stat(Primary, "inhibition", 60, 5)

                                "[Primary.name] kicks you out of the room."

                if line != "stay":
                    $ Player.location = "bg_campus"

                    jump reset_location

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
                ch_s "Ah, [StormX.player_petname]."
            elif Primary == JubesX:
                ch_v "Oh, hey. . ."
        elif Player.location == "bg_classroom":
            if Primary == RogueX or Secondary == RogueX:
                ch_r "Hey, [RogueX.player_petname]."

            if Primary == KittyX or Secondary == KittyX:
                ch_k "Oh, hey."

            if Primary == EmmaX or Secondary == EmmaX:
                ch_e "Oh, hello, [EmmaX.player_petname]."

            if Primary == LauraX or Secondary == LauraX:
                ch_l "Hey."

            if Primary == StormX or Secondary == StormX:
                ch_s "Hello, [StormX.player_petname]."

            if Primary == JubesX or Secondary == JubesX:
                ch_v "Hey!"

            $ D20 = renpy.random.randint(1, 20)

            if Primary in [EmmaX, StormX]:
                if Secondary:
                    $ Primary = Secondary
                    $ Secondary = None
                else:
                    $ Primary = None

            $ line = None

            if Primary:
                if approval_check(Primary, 1000):
                    if D20 >= 10:
                        $ line = Primary.name + " takes a seat next to you"

                        $ Present.append(Primary)
                    else:
                        $ line = Primary.name + " sits across the room from you"

                        $ Nearby.append(Primary)

                        call hide_Girl(Primary)
                else:
                    $ line = Primary.name + " sits across the room from you"

                    $ Nearby.append(Primary)

                    call hide_Girl(Primary)

            if Secondary:
                if approval_check(Secondary, 1000):
                    if D20 >= 10:
                        if Primary in Present:
                            $ line = Primary.name + " and " + Secondary.name + " sit down next to you"
                        else:
                            $ line = line + "_, while " + Secondary.name + " takes the seat next to you"

                        $ Present.append(Secondary)
                    else:
                        if Primary in Nearby:
                            $ line = Primary.name + " and " + Secondary.name + " sit across the room from you"
                        else:
                            $ line = line + "_, while " + Secondary.name + " sits across the room from you"

                        $ Nearby.append(Secondary)

                        call hide_Girl(Secondary)
                else:
                    if Primary in Nearby:
                        $ line = Primary.name + " and " + Secondary.name + " sit across the room from you"
                    else:
                        $ line = line + "_, while " + Secondary.name + " sits across the room from you"

                    $ Nearby.append(Secondary)

                    call hide_Girl(Secondary)

            if line:
                "[line]."

            if EmmaX.teaching:
                "[EmmaX.name] takes her position behind the podium."
            elif StormX.teaching:
                "[StormX.name] takes her position behind the podium."
        elif Player.location in ["bg_campus", "bg_dangerroom", "bg_pool"]:
            if Primary == RogueX or Secondary == RogueX:
                ch_r "Hey, [RogueX.player_petname]."

            if Primary == KittyX or Secondary == KittyX:
                ch_k "Oh, hey."

            if Primary == EmmaX or Secondary == EmmaX:
                ch_e "Oh, hello, [EmmaX.player_petname]."

            if Primary == LauraX or Secondary == LauraX:
                ch_l "Hey."

            if Primary == StormX or Secondary == StormX:
                ch_s "Hello, [StormX.player_petname]."

            if Primary == JubesX or Secondary == JubesX:
                ch_v "Hey!"

    python:
        for G in all_Girls:
            if G in Nearby:
                G.location = "nearby"

    return True

label exit_gym:
    $ temp_Girls = Player.Party[:]

    $ line = None

    while temp_Girls:
        if temp_Girls[0].Wardrobe.current_Outfit.name == "gym_clothes":
            if len(Player.Party) > 1:
                $ line = "We should change out of these if we're leaving. . ."
            else:
                $ line = "I should change out of these if we're leaving. . ."

        $ temp_Girls.remove(temp_Girls[0])

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
            call dismiss_girl(RogueX)
        "[KittyX.name]" if KittyX.location == Player.location or KittyX in Player.Party:
            call dismiss_girl(KittyX)
        "[EmmaX.name]" if EmmaX.location == Player.location or EmmaX in Player.Party:
            call dismiss_girl(EmmaX)
        "[LauraX.name]" if LauraX.location == Player.location or LauraX in Player.Party:
            call dismiss_girl(LauraX)
        "[JeanX.name]" if JeanX.location == Player.location or JeanX in Player.Party:
            call dismiss_girl(JeanX)
        "[StormX.name]" if StormX.location == Player.location or StormX in Player.Party:
            call dismiss_girl(StormX)
        "[JubesX.name]" if JubesX.location == Player.location or JubesX in Player.Party:
            call dismiss_girl(JubesX)
        "Never mind.":
            pass

    return

label locked_door(arriving_Girls):
    if arriving_Girls in all_Girls:
        $ arriving_Girls = [arriving_Girls]

    python:
        Primary = None

        for G in arriving_Girls:
            if Player.location == G.home:
                Primary = G

                break
            elif G == JeanX:
                Primary = G

    if not Primary:
        $ Primary = arriving_Girls[0]

    if len(arriving_Girls) > 1:
        $ Secondary = arriving_Girls[0] if Primary != arriving_Girls[0] else arriving_Girls[1]

        if len(arriving_Girls) > 3:
            $ line = Primary.name + " and a few others"
        elif len(arriving_Girls) > 2:
            $ line = Primary.name + " and a couple others"
        else:
            $ line = Primary.name + " and " + Secondary.name
    else:
        $ Secondary = None

        $ line = Primary.name

    if Player.location == Primary.home:
        if len(arriving_Girls) > 1:
            "You hear a key in the lock, and [line] enter the room."
        else:
            "You hear a key in the lock, and [line] enters the room."
    elif Primary == JeanX:
        "You hear a rattle at the door."
        "After a moment, and some clicking in the lock, the door pops open."

        if len(arriving_Girls) > 1:
            "[line] walk into the room."
        else:
            "[line] walks into the room."

        call add_Girls(arriving_Girls)

        ch_j "Hey, [Girl.player_petname]!"
    else:
        "The doorknob jiggles. A moment later, you hear a knock."

        if len(arriving_Girls) > 1:
            if Primary == RogueX:
                ch_r "Could we come in, [Primary.player_petname]?"
            elif Primary == EmmaX:
                ch_e "[Primary.player_petname], we're waiting."
            elif Primary == LauraX:
                ch_l "It's me."

                if len(arriving_Girls) > 2:
                    ch_l ". . . and some friends."
                else:
                    ch_l ". . . and [Secondary.name]."
            elif Primary == StormX:
                ch_s "[Primary.player_petname], may we come in?"
            elif Primary == JubesX:
                if len(arriving_Girls) > 2:
                    ch_v "Hey, it's [Primary.name]."
                else:
                    ch_l "Hey, it's [Primary.name] and [Secondary.name]."
        else:
            if Primary == RogueX:
                ch_r "Could I come in, [Primary.player_petname]?"
            elif Primary == EmmaX:
                ch_e "[Primary.player_petname], I'm waiting."
            elif Primary == LauraX:
                ch_l "It's me."
            elif Primary == StormX:
                ch_s "[Primary.player_petname], may I come in?"
            elif Primary == JubesX:
                ch_v "Hey, it's [Primary.name]."

        menu:
            extend ""
            "Open door.":
                ch_p "Hold on, [Primary.name]!"
                "You unlock the door and let her in."

                call add_Girls(arriving_Girls)
            "Open door. [[Stop fucking first]" if Player.primary_action:
                ch_p "Hold on, [Primary.name]!"

                call sex_over

                "You unlock the door and let her in."

                call add_Girls(arriving_Girls)

                if Primary == RogueX:
                    ch_r "Hey, got a minute, [Primary.player_petname]?"
                elif Primary == EmmaX:
                    ch_e "[Primary.player_petname], I had something I wanted to discuss. . ."
                elif Primary == LauraX:
                    ch_l "Hey, [Primary.player_petname]."
                elif Primary == StormX:
                    ch_s "Hello, I wanted to talk with you. . ."
                elif Primary == JubesX:
                    ch_v "Hey, [Primary.player_petname]."
            "Send her away." if not Secondary:
                ch_p "Sorry, could you come back later?"

                call change_Girl_stat(Primary, "love", 80, -2)

                if Primary == RogueX:
                    ch_r "C'mon, [Primary.player_petname], don't yank my chain like this!"

                    return False
                elif Primary == EmmaX:
                    call change_Girl_stat(Primary, "obedience", 80, -2)

                    ch_e "I have to say, [EmmaX.player_petname], I understand the appeal of having someone at your beck and call. . ."
                    ch_e ". . . but I don't appreciate being on the receiving end!"

                    return False
                elif Primary in [LauraX, JubesX]:
                    "[Primary.name] goes quiet."

                    if approval_check(Primary, 500, "I") and not approval_check(Primary, 500, "O"):
                        if Primary == LauraX:
                            $ LauraX.arm_pose = 2
                            $ LauraX.claws = 1

                            "snickt"

                            call add_Girls(arriving_Girls)

                            "The door swings open."

                            $ LauraX.claws = 0

                            ch_l "Hey, I don't like being jerked around, so don't do that, okay?"
                        elif Primary == JubesX:
                            "A thin mist passes under the door, and forms into a human shape."

                            call add_Girls(arriving_Girls)

                            ch_v "Well, I wanted to talk."

                        call change_Girl_stat(Primary, "obedience", 80, -4)
                    else:
                        call change_Girl_stat(Primary, "love", 80, -1)
                        call change_Girl_stat(Primary, "obedience", 80, 3)

                        Primary.voice "Ok."

                        "You hear her shuffling off."

                        return False
                elif Primary == StormX:
                    if approval_check(Primary, 800,"LI") and not approval_check(Primary, 500,"O"):
                        $ Primary.change_outfit()

                        "You hear some clicking from the door."
                        "The door swings open."

                        call add_Girls(arriving_Girls)

                        call change_Girl_stat(Primary, "obedience", 80, -4)

                        ch_s "That was not a quality lock."
                    else:
                        call change_Girl_stat(Primary, "love", 80, -1)
                        call change_Girl_stat(Primary, "obedience", 80, 3)

                        ch_s ". . ."
                        ch_s "Very well, I can respect that."

                        return False
            "Send them away." if Secondary:
                ch_p "Sorry, could you come back later?"

                call change_Girl_stat(Primary, "love", 80, -2)

                if Primary == RogueX:
                    ch_r "C'mon, [Primary.player_petname], don't yank our chains like this!"

                    return False
                elif Primary == EmmaX:
                    call change_Girl_stat(Primary, "obedience", 80, -2)

                    ch_e "I have to say, [EmmaX.player_petname], I understand the appeal of having someone at your beck and call. . ."
                    ch_e ". . . but I don't appreciate being on the receiving end!"

                    return False
                elif Primary in [LauraX, JubesX]:
                    "[Primary.name] goes quiet."

                    if approval_check(Primary, 500, "I") and not approval_check(Primary, 500, "O"):
                        if Primary == LauraX:
                            $ LauraX.arm_pose = 2
                            $ LauraX.claws = 1

                            "snickt"

                            call add_Girls(arriving_Girls)

                            "The door swings open."

                            $ LauraX.claws = 0

                            ch_l "Hey, I don't like being jerked around, so don't do that, okay?"
                        elif Primary == JubesX:
                            "A thin mist passes under the door, and forms into a human shape."

                            call add_Girls(arriving_Girls)

                            ch_v "Well, we wanted to talk."

                        call change_Girl_stat(Primary, "obedience", 80, -4)
                    else:
                        call change_Girl_stat(Primary, "love", 80, -1)
                        call change_Girl_stat(Primary, "obedience", 80, 3)

                        Primary.voice "Ok."

                        "You hear footsteps wandering off."

                        return False
                elif Primary == StormX:
                    if approval_check(Primary, 800,"LI") and not approval_check(Primary, 500,"O"):
                        $ Primary.change_outfit()

                        "You hear some clicking from the door."
                        "The door swings open."

                        call add_Girls(arriving_Girls)

                        call change_Girl_stat(Primary, "obedience", 80, -4)

                        ch_s "That was not a quality lock."
                    else:
                        call change_Girl_stat(Primary, "love", 80, -1)
                        call change_Girl_stat(Primary, "obedience", 80, 3)

                        ch_s ". . ."
                        ch_s "Very well, we can respect that."

                        return False

    $ door_locked = False

    return True

label get_dressed:
    if "naked" in Player.recent_history:
        "You get dressed."

        $ Player.drain_word("naked")
        $ Player.drain_word("cockout")
    elif "cockout" in Player.recent_history:
        "You put your cock away."

        $ Player.drain_word("cockout")
    return





label SpecialMenu:
    while True:
        menu:
            "Meet Dr. Darkholme":
                jump meet_Mystique
            "Discover Mystique":
                jump discover_Mystique
            "Halloween Player.Party [[Evening Only] (locked)" if time_index != 2:
                pass
            "Halloween Player.Party" if time_index == 2:
                if "halloween" in Player.history:
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
                        call Halloween_Party_entry
                    "No":
                        return
            "Leveling Menu":
                while True:
                    menu:
                        "Level-up menu"
                        "Level Yourself" if Player.stat_points > 0 or "addict control" in Player.traits:
                            call Level_Up (Player)
                        "Level Yourself [[No points to spend] (locked)" if Player.stat_points <= 0 and "addict control" not in Player.traits:
                            pass
                        "Level [RogueX.name]" if RogueX.stat_points > 0:
                            call Level_Up (RogueX)
                        "Level [KittyX.name]" if KittyX.stat_points > 0 and "met" in KittyX.history:
                            call Level_Up (KittyX)
                        "Level [EmmaX.name]" if EmmaX.stat_points > 0 and "met" in EmmaX.history:
                            call Level_Up (EmmaX)
                        "Level [LauraX.name]" if LauraX.stat_points > 0 and "met" in LauraX.history:
                            call Level_Up (LauraX)
                        "Level [JeanX.name]" if JeanX.stat_points > 0 and "met" in JeanX.history:
                            call Level_Up (JeanX)
                        "Level [StormX.name]" if StormX.stat_points > 0 and "met" in StormX.history:
                            call Level_Up (StormX)
                        "Level [JubesX.name]" if JubesX.stat_points > 0 and "met" in JubesX.history:
                            call Level_Up (JubesX)
                        "Back":
                            jump SpecialMenu
                "You need to gain experience first by training or going to class."
            "Return to Room when asked?":
                "If a girl says she needs to see you, by default you are asked if you'd like to return."
                menu:
                    "Would you like the game to ask you this?"
                    "Yes [[current]" if always_return_to_room:
                        pass
                    "Yes" if not always_return_to_room:
                        $ always_return_to_room = True
                    "No [[current]" if not always_return_to_room:
                        pass
                    "No" if always_return_to_room:
                        $ always_return_to_room = False
            "Done.":
                return


label Level_Up(Chr=Player):
    if Chr != Player and Chr not in all_Girls:
        return
    if Chr == Player:
        while Player.stat_points > 0 or "addict control" in Player.traits:
            menu:
                "You have [Player.stat_points] points to spend. How would you like to spend them?"
                "Increase sexual stamina. [[Acquired] (locked)" if "focus" in Player.traits:
                    pass
                "Increase sexual stamina. [[One point]" if "focus" not in Player.traits:
                    menu:
                        "This trait will unlock the \"Focus\" option during sex, giving you more time before you blow."
                        "Unlock Focus.":
                            if Player.stat_points > 0:
                                $ Player.stat_points -= 1
                                $ Player.traits.append("focus")
                            else:
                                "You don't have enough points for that."
                        "Cancel.":
                            pass

                "Increase your addictiveness. [[One point]" if "addict control" not in Player.traits and "nonaddictive" not in Player.traits and "addictive" not in Player.traits:
                    menu:
                        "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                        "Increase addictiveness.":
                            if Player.stat_points > 0:
                                $ Player.stat_points -= 1
                                $ Player.traits.append("addictive")
                            else:
                                "You don't have enough points for that."
                        "Cancel.":
                            pass

                "Reduce your addictiveness. [[One point]" if "addict control" not in Player.traits and "nonaddictive" not in Player.traits and "addictive" not in Player.traits:
                    menu:
                        "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                        "Reduce addictiveness.":
                            if Player.stat_points > 0:
                                $ Player.stat_points -= 1
                                $ Player.traits.append("nonaddictive")
                            else:
                                "You don't have enough points for that."
                        "Cancel.":
                            pass

                "Control your Addiction level. [[Two points]" if "addict control" not in Player.traits and ("nonaddictive" in Player.traits or "addictive" in Player.traits):
                    menu:
                        "This trait will allow you to freely control the amount you addict girls to your touch."
                        "Gain addiction control.":
                            if Player.stat_points >= 2:
                                $ Player.stat_points -= 2
                                $ Player.traits.append("addict control")
                            else:
                                "You don't have enough points for that."
                        "Cancel.":
                            pass

                "Increase your addictiveness. [[Free]" if "addict control" in Player.traits:
                    menu:
                        "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                        "Increase addictiveness, no cost.":
                            if "nonaddictive" in Player.traits:
                                $ Player.traits.remove("nonaddictive")
                                "You are now at the baseline addictiveness level."
                            elif "addictive" not in Player.traits:
                                $ Player.traits.append("addictive")
                                "You are now at the enhanced addictiveness level."
                            else:
                                "You are already at the max addictiveness level."
                        "Cancel.":
                            pass
                "Reduce your addictiveness. [[Free]" if "addict control" in Player.traits:
                    menu:
                        "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                        "Reduce addictiveness.":
                            if "addictive" in Player.traits:
                                $ Player.traits.remove("addictive")
                                "You are now at the baseline addictiveness level."
                            elif "nonaddictive" not in Player.traits:
                                $ Player.traits.append("nonaddictive")
                                "You are now at the reduced addictiveness level."
                            else:
                                "You are already at the minimum addictiveness level."

                            if "addictive" in Player.traits:
                                $ Player.traits.remove("addictive")
                                $ Player.traits.append("nonaddictive")
                                $ Player.traits.append("addict control")
                            else:
                                $ Player.traits.append("nonaddictive")
                        "Cancel.":
                            pass

                "Increase semen production. [[Maxed] (locked)" if Player.max_semen >= 5:
                    pass
                "Increase semen production. [[One point]" if Player.max_semen < 5:
                    menu:
                        "This trait will increase by 1 the number of times you can climax before needing a break."
                        "Increase max semen.":
                            if Player.stat_points > 0:
                                $ Player.stat_points -= 1
                                $ Player.max_semen += 1
                            else:
                                "You don't have enough points for that."
                            if Player.max_semen >= 5:
                                "You're already at the max level."
                        "Cancel.":
                            pass
                "Never mind, I'll come back later.":

                    return
    else:

        while Chr.stat_points > 0:
            menu:
                "[Chr.name] is Level [Chr.level] and has [Chr.stat_points] points to spend. How would you like to spend them?"
                "Increase sexual focus. [[Acquired] (locked)" if "focus" in Chr.traits:
                    pass
                "Increase sexual focus. [[One point]" if "focus" not in Chr.traits:
                    menu:
                        "This trait will unlock the \"Focus\" option during sex, giving [Chr.name] more time before she orgasms."
                        "Unlock Focus.":
                            if Chr.stat_points:
                                $ Chr.stat_points -= 1
                                $ Chr.traits.append("focus")
                            else:
                                "You don't have enough points for that."
                        "Cancel.":
                            pass

                "Increase [Chr.name]'s resistance. [[Maxed] (locked)" if Chr.resistance >= 3:
                    pass
                "Increase [Chr.name]'s resistance. [[One point]" if 0 < Chr.resistance < 3:
                    menu:
                        "This trait will increase [Chr.name]'s resistance to your touch's addictive properties."
                        "Increase Resistance.":
                            if Chr.stat_points:
                                $ Chr.stat_points -= 1
                                $ Chr.resistance += 1
                            else:
                                "You don't have enough points for that."
                        "Cancel.":
                            pass


                "Increase stamina. [[Maxed] (locked)" if Chr.max_actions >= 10:
                    pass
                "Increase stamina. [[One point]" if Chr.max_actions < 10:
                    "This trait will increase by 2 the number of sex actions [Chr.name] can take before needing a break."
                    menu:
                        "She currently has [Chr.max_actions] actions."
                        "Increase sex actions.":
                            if Chr.stat_points:
                                $ Chr.stat_points -= 1
                                $ Chr.max_actions += 2
                                if Chr.max_actions > 10:
                                    $ Chr.max_actions = 10
                                    "[Chr.name] has reached her maximum actions."
                            else:
                                "You don't have enough points for that."
                        "Cancel.":
                            pass

                "Allow [Chr.name] to touch. [[Acquired] (locked)" if Chr == RogueX and "touch" in Chr.traits:
                    pass
                "Allow [Chr.name] to touch. [[One point]" if Chr == RogueX and "touch" not in Chr.traits and Chr.level >= 5:
                    "This trait will allow [Chr.name] to touch other people, not just you, without harming them."
                    menu:
                        "She can still borrow their abilities if they have any."
                        "Unlock touch ability.":
                            if Chr.stat_points:
                                $ Chr.stat_points -= 1
                                $ Chr.traits.append("touch")
                            else:
                                "You don't have enough points for that."
                        "Cancel.":
                            pass
                "Never mind, I'll come back later.":













                    return

    return













label shift_focus(Girl, Second = None):
    if focused_Girl == Girl:
        pass
    elif Second and Second != Girl:
        $ Partner = Second
    elif Partner == Girl:
        $ Partner = focused_Girl

    $ focused_Girl = Girl

    if Partner == Girl:
        $ Partner = None

    $ renpy.restart_interaction()

    return


label Sex_Menu_Threesome(Girl=0):
    if not Girl or Girl not in all_Girls:
        return

    menu:
        "Do you want to join us [RogueX.name]?" if RogueX.location == Player.location and Girl != RogueX:
            if Partner == RogueX:

                ch_r "If I'd been do'in it right you wouldn't hafta ask. . ."
            else:
                if Girl == JeanX:

                    call Girl_Whammy (RogueX)
                call Girls_Noticed (Girl, RogueX, 1)
                if Girl.location != Player.location:

                    ch_r "Oh, well. . . I'm still game. . ."
                    call shift_focus(RogueX)
                    $ renpy.pop_call()
                elif RogueX.location == Player.location:
                    ch_r "I s'pose I could lend a hand 0. ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [KittyX.name]?" if KittyX.location == Player.location and Girl != KittyX:
            if Partner == KittyX:

                ch_k "Lol, what are you even talking about?"
            else:
                if Girl == JeanX:

                    call Girl_Whammy (KittyX)
                call Girls_Noticed (Girl, KittyX, 1)
                if Girl.location != Player.location:

                    ch_k "Whoa, drama much? 0. ."
                    call shift_focus(KittyX)
                    $ renpy.pop_call()
                elif KittyX.location == Player.location:
                    ch_k "I could[KittyX.like]give it a try. . ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [EmmaX.name]?" if EmmaX.location == Player.location and Girl != EmmaX:
            if Partner == EmmaX:

                ch_e "Have I not been keeping up?"
            else:
                if Girl == JeanX:

                    call Girl_Whammy (EmmaX)
                call Girls_Noticed (Girl, EmmaX, 1)
                if Girl.location != Player.location:

                    ch_e "Pity. . ."
                    call shift_focus(EmmaX)
                    $ renpy.pop_call()
                elif EmmaX.location == Player.location:
                    ch_e "So what did you have in mind for us. . ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [LauraX.name]?" if LauraX.location == Player.location and Girl != LauraX:
            if Partner == LauraX:

                ch_l "I already am."
            else:
                if Girl == JeanX:

                    call Girl_Whammy (LauraX)
                call Girls_Noticed (Girl, LauraX, 1)
                if Girl.location != Player.location:

                    ch_l "Her loss. . ."
                    call shift_focus(LauraX)
                    $ renpy.pop_call()
                elif LauraX.location == Player.location:
                    ch_l "Hm, ok. . ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [JeanX.name]?" if JeanX.location == Player.location and Girl != JeanX:
            if Partner == JeanX:

                ch_j "I've been here the entire time. . ."
            else:
                call Girls_Noticed (Girl, JeanX, 1)
                if Girl.location != Player.location:

                    ch_j "Huh. Her loss. . ."
                    call shift_focus(JeanX)
                    $ renpy.pop_call()
                elif JeanX.location == Player.location:
                    ch_j "Sure."
                else:
                    "She seems annoyed with this whole situation and leaves the room."

        "Do you want to join us [StormX.name]?" if StormX.location == Player.location and Girl != StormX:
            if Partner == StormX:

                ch_s "You hadn't noticed?"
            else:
                if Girl == JeanX:

                    call Girl_Whammy (StormX)
                call Girls_Noticed (Girl, StormX, 1)
                if Girl.location != Player.location:

                    ch_s "Oh, that's too bad. . ."
                    call shift_focus(StormX)
                    $ renpy.pop_call()

                elif StormX.location == Player.location:
                    ch_s "Delighted. . ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [JubesX.name]?" if JubesX.location == Player.location and Girl != JubesX:
            if Partner == JubesX:

                ch_v "I thought I already was!"
            else:
                if Girl == JeanX:

                    call Girl_Whammy (JubesX)
                call Girls_Noticed (Girl, JubesX, 1)
                if Girl.location != Player.location:

                    ch_v "Oh, well. . ."
                    call shift_focus(JubesX)
                    $ renpy.pop_call()
                elif JubesX.location == Player.location:
                    ch_v "Sure!"
                else:
                    "She seems uncomfortable with this situation and leaves the room."
        "Never mind [[something else]":

            pass
    if AloneCheck(Girl) and Girl.taboo == 20:
        $ Girl.taboo = 0
        $ taboo = 0
    return

label Partner_Like(Girl=0, value=1, Altvalue=1, Measure=800, Partner=Partner):

    if Partner:
        if second_girl_main_action:

            if second_girl_main_action == "watch":
                pass
            elif second_girl_main_action in ("handjob", "blowjob"):
                $ value += 1
            elif second_girl_main_action in ("eat_pussy", "eat_ass"):
                $ value += 3
            else:
                $ value += 2


        $ Partner.check_if_likes(Girl,Measure,value, 1)
        $ Girl.check_if_likes(Partner,Measure,value, 1)

    return

label RoomStatboost(Type=0, Check=0, Amount=0):


    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == Player.location or temp_Girls[0] in Nearby:
            call change_Girl_stat(temp_Girls[0], Type, Check, Amount)
        $ temp_Girls.remove(temp_Girls[0])
    return



label Haremchange_stat(Girl=0, Check=1000, value=0, Greater=0, temp_GirlsA=[], temp_GirlsB=[]):



    if simulation:
        return
    if Girl == "all" or Girl == 0:
        $ temp_GirlsA = Player.Harem[:]
    elif Girl in all_Girls:
        $ temp_GirlsA = [Girl]
    else:
        return
    while temp_GirlsA:

        $ temp_GirlsB = Player.Harem[:]
        if temp_GirlsA[0] in temp_GirlsB:

            $ temp_GirlsB.remove(temp_GirlsA[0])
        while temp_GirlsB:

            $ temp_GirlsA[0].check_if_likes(temp_GirlsB[0],Check,value, 1)
            $ temp_GirlsB.remove(temp_GirlsB[0])
        $ temp_GirlsA.remove(temp_GirlsA[0])
    return

label JumperCheck(Girls=[]):

    if "nope" in Player.recent_history or Player.Party:

        return

    $ temp_Girls = active_Girls[:]
    while temp_Girls:
        if "lesbian" in temp_Girls[0].recent_history and "no_les" not in Player.recent_history and approval_check(temp_Girls[0], 1600 - temp_Girls[0].SEXP, taboo_modifier=0):

            call Call_For_Les (temp_Girls[0])

        if "locked" in Player.traits and temp_Girls[0].location != Player.location:

            pass
        elif temp_Girls[0].remaining_actions and temp_Girls[0].thirst >= 30 and approval_check(temp_Girls[0], 500, "I") and "refused" not in temp_Girls[0].daily_history and "met" in temp_Girls[0].history:
            if "chill" not in temp_Girls[0].traits and temp_Girls[0].tag not in Player.daily_history and "jumped" not in temp_Girls[0].daily_history and not temp_Girls[0].teaching:

                if renpy.random.randint(0,3) > 1:
                    $ Girls.append(temp_Girls[0])
                if temp_Girls[0].thirst >= 60:
                    $ Girls.append(temp_Girls[0])
            if temp_Girls[0].thirst >= 90:
                $ Girls.append(temp_Girls[0])
        $ temp_Girls.remove(temp_Girls[0])

    if not Girls:
        return

    if len(Girls) >= 2:
        $ renpy.random.shuffle(Girls)
        while len(Girls) >= 2 and Girls[0] == Girls[1]:
            $ Girls.remove(Girls[1])
        while len(Girls) > 2:
            $ Girls.remove(Girls[2])

    $ Partner = 0
    if len(Girls) >= 2:

        if Girls[0] in Player.Harem and Girls[1] in Player.Harem:
            $ Partner = Girls[1]
        elif Girls[0].likes[Girls[1].tag] >= 800 and Girls[1].likes[Girls[0].tag] >= 800:
            $ Partner = Girls[1]

    call Jumped

    if "nope" in Player.recent_history:

        while Girls:
            call remove_Girl(Girls[0])
            $ Girls.remove(Girls[0])
        jump reset_location
    elif Girls:

        if Girls[0].location == Player.location:
            call enter_main_sex_menu(Girls[0])

    if Player.location == "bg_player":

        jump player_room
    return

label Jumped(Act=0):
    if Girls[0] == EmmaX and Partner and "threesome" not in EmmaX.history:
        $ Girls.remove(Partner)
        $ Partner = 0
    elif EmmaX in Girls and ((taboo and "taboo" not in EmmaX.history) or "threesome" not in EmmaX.history):
        $ Girls.remove(EmmaX)
        $ Partner = 0

    if not Girls:
        return

    if Girls[0].location != Player.location and "locked" in Player.traits:

        call Girls_arrive(Girls[0])

        if not _return:
            $ Player.recent_history.append("nope")

            return

    python:
        for G in Girls:
            G.location = Player.location

    $ Girls[0].add_word(1,"jumped", "jumped")

    call set_Character_taboos

    if taboo and (not approval_check(Girls[0], 1500, taboo_modifier=3) or (Girls[0] == EmmaX and taboo and "taboo" not in EmmaX.history)):

        $ Act = "leave"

    if Player.location in bedrooms:

        if Player.location == "bg_player":
            pass
        elif Girls[0].home != Player.location and not (Partner and Partner.home == Player.location):

            $ Act = "leave"

    call shift_focus (Girls[0])
    call set_the_scene

    $ Player.recent_history.append("jumped")
    $ Girls[0].change_face("sly", 1)
    if Act == "leave":

        "Suddenly, [Girls[0].name] grabs your arm with a miscevious smile, and starts to lead you back towards your room."
        menu:
            "Go along with it":
                call change_Girl_stat(Girls[0], "inhibition", 95, 3)
                "You follow after her."
            "Pull away from her and head back.":
                call change_Girl_stat(Girls[0], "love", 90, -10)
                call change_Girl_stat(Girls[0], "obedience", 50, 10)
                call change_Girl_stat(Girls[0], "obedience", 95, 5)
                call change_Girl_stat(Girls[0], "inhibition", 95, -5)
                $ Girls[0].change_face("sad", 1)
                "You tell her to cut it out, and head back to what you were doing."
                $ Player.recent_history.append("nope")
                $ Girls[0].add_word(1,"refused", "refused")
                if not approval_check(Girls[0], 500, "O"):
                    $ Girls[0].add_word(1,"angry", "angry")
                return

        if Partner:
            "[Partner.name] also follows along behind you."

        $ Player.location = "bg_player"

        call clear_the_room(Girls[0], passive = True, silent = True)
    else:


        if Partner in all_Girls:
            $ Girls[1].change_face("sly", 1)
            "Suddenly, [Girls[0].name] pulls you aside and [Partner.name] follows along."
        else:
            "Suddenly, [Girls[0].name] pulls you aside."
        menu:
            "See where this is going":
                call change_Girl_stat(Girls[0], "inhibition", 95, 2)
            "Not here [[head to your room]":
                call change_Girl_stat(Girls[0], "inhibition", 95, 1)
                "You head to your room first."
                $ Player.location = "bg_player"
                call clear_the_room(Girls[0], passive = True, silent = True)
            "Pull away from her and head back.":
                call change_Girl_stat(Girls[0], "love", 90, -10)
                call change_Girl_stat(Girls[0], "obedience", 50, 10)
                call change_Girl_stat(Girls[0], "obedience", 95, 5)
                call change_Girl_stat(Girls[0], "inhibition", 95, -5)
                $ Girls[0].change_face("sad", 1)
                "You tell her to cut it out, and head back to what you were doing."
                $ Player.recent_history.append("nope")
                $ Girls[0].add_word(1,"refused", "refused")
                if not approval_check(Girls[0], 500, "O"):
                    $ Girls[0].add_word(1,"angry", "angry")
                return

    python:
        for G in Girls:
            G.location = Player.location

    call set_Character_taboos
    call set_the_scene

    $ Girls[0].add_word(1,"jumped", "jumped", 0,"jumped")

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

    call check_favorite_actions (Girls[0])
    $ Act = Girls[0].favorite_action

    if Act in ("anal", "sex", "blowjob", "titjob", "handjob", "hotdog"):

        "[Girls[0].name] reaches down and unzips your fly. . ."
        if not Player.semen:
            "You wish you weren't already drained. . . you stop her hands."
            ch_p "I could actually use a break right now. . "
            $ Act = "fondle_breasts"
        else:
            call Seen_First_Peen (Girls[0], Partner, 1)

    if Partner:
        call Girls_Noticed (Girls[0], Partner, 1)

    call before_action(Girls[0], Act, Girls[0])

label Quick_Sex(Girl=focused_Girl, Act=0):


    $ Girl.change_face("sly", 1)
    $ Girl.add_word(1,"quicksex", "quicksex")
    menu:
        extend ""
        "Sure":
            call change_Girl_stat(Girl, "love", 95, 4)
            call change_Girl_stat(Girl, "obedience", 50, 1)
            call change_Girl_stat(Girl, "inhibition", 70, 2)
            call change_Girl_stat(Girl, "inhibition", 90, 3)
        "No thanks":
            $ line = 0
            call change_Girl_stat(Girl, "love", 80, -2)
            if (2*Girl.obedience) >= (Girl.love + Girl.inhibition + (5*Girl.thirst)):

                $ Girl.change_face("sadside", 1)
                call change_Girl_stat(Girl, "obedience", 90, 7)
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
                        call change_Girl_stat(Girl, "love", 80, -2)
                        call change_Girl_stat(Girl, "obedience", 80, -8)
                        $ line = "ask"
                    ". . . [[say nothing, still no].":
                        pass
            elif (approval_check(Girl, 600, "I") and Girl.thirst >= 30) or Girl.thirst >= 50:

                $ Girl.change_face("confused", 1,eyes = "surprised")
                call change_Girl_stat(Girl, "love", 80, -1)
                call change_Girl_stat(Girl, "obedience", 70, 4)
                call change_Girl_stat(Girl, "inhibition", 60, 5)
                call change_Girl_stat(Girl, "inhibition", 90, 3)
                if Girl == RogueX:
                    ch_r "You're sure about that?"
                elif Girl == KittyX:
                    ch_k "Seriously"
                elif Girl == EmmaX:
                    ch_e "Have you thought this through?"
                elif Girl == LauraX:
                    ch_l "Seriously, free sex here."
                elif Girl == JeanX:
                    ch_j "Seriously? 0. ."
                elif Girl == StormX:
                    ch_s "Are you quite sure? 0. ."
                elif Girl == JubesX:
                    ch_v "I can make it worth your while. . ."
                $ line = "ask"

            if line == "ask":
                $ line = 0
                $ Count = 2
                $ counter = 0
                while Count:

                    $ Count -= 1
                    menu:
                        extend ""
                        "Ok, fine.":
                            $ Act = 1
                            $ Count = 0
                            $ Girl.change_face("sly", 1)
                            call change_Girl_stat(Girl, "love", 80, 2)
                            call change_Girl_stat(Girl, "love", 95, 3)
                            call change_Girl_stat(Girl, "obedience", 70, 2)
                            call change_Girl_stat(Girl, "inhibition", 90, 3)

                        "Beg me." if counter < 100:
                            call change_Girl_stat(Girl, "obedience", 80, 2)
                            $ line = "beg"
                        "Beg me again." if counter >= 100:
                            call change_Girl_stat(Girl, "obedience", 90, 2)
                            $ line = "beg"
                        "Only if I get to choose.":

                            $ Girl.change_face("smile", 1,brows = "confused")
                            call change_Girl_stat(Girl, "love", 90, 2)
                            call change_Girl_stat(Girl, "obedience", 80, 3)
                            call change_Girl_stat(Girl, "obedience", 95, 3)
                            call change_Girl_stat(Girl, "inhibition", 85, 2)
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
                            call enter_main_sex_menu(Girl)
                            return
                        "Still no.":

                            call change_Girl_stat(Girl, "love", 85, -2)
                            call change_Girl_stat(Girl, "obedience", 90, 3)
                            if approval_check(Girl, 1500+(5*counter)-(10*Girl.thirst), "LI"):

                                $ line = "beg"
                            elif not counter and Count:

                                $ Girl.top_pulled_up = 1
                                pause 1
                                call expression Girl.tag + "_First_Topless" pass (1)
                                $ Girl.top_pulled_up = 0
                                $ Girl.change_face("confused", 1,mouth = "smile")
                                call change_Girl_stat(Girl, "inhibition", 70, 3)
                                call change_Girl_stat(Girl, "inhibition", 95, 3)
                                if Girl == RogueX:
                                    ch_r "You -really- sure about that?"
                                elif Girl == KittyX:
                                    ch_k "Reaaaaally?"
                                elif Girl == EmmaX:
                                    ch_e "-No- second thoughts, [Girl.player_petname]?"
                                elif Girl == LauraX:
                                    ch_l "I mean, come on."
                                elif Girl == JeanX:
                                    ch_j "You -know- you want it. . ."
                                elif Girl == StormX:
                                    ch_s "Are you -that- sure of yourself?"
                                elif Girl == JubesX:
                                    ch_v "Bummer. . ."
                                $ counter += 25
                    if line == "beg":
                        if approval_check(Girl, 600+counter, "O") or approval_check(Girl, 1500+(5*counter)-(10*Girl.thirst)):

                            if counter < 50:

                                $ Girl.change_face("sad", 2)
                                call change_Girl_stat(Girl, "love", 90, -2)
                                call change_Girl_stat(Girl, "obedience", 50, 5)
                                call change_Girl_stat(Girl, "obedience", 95, 3)
                                call change_Girl_stat(Girl, "inhibition", 90, 3)
                                if Girl == RogueX:
                                    ch_r "Please?"
                                elif Girl == KittyX:
                                    ch_k "Pretty please?"
                                elif Girl == EmmaX:
                                    ch_e ". . ."
                                    call change_Girl_stat(Girl, "love", 90, -2)
                                    call change_Girl_stat(Girl, "obedience", 200, 3)
                                    ch_e ". . .Please?"
                                elif Girl == LauraX:
                                    ch_l "Um. . . Please?"
                                elif Girl == JeanX:
                                    ch_j "Huh. . ."
                                    call change_Girl_stat(Girl, "obedience", 90, 3)
                                    ch_j "Ok. . . please? 0. ."
                                elif Girl == StormX:
                                    ch_s "No? You're that certain?"
                                elif Girl == JubesX:
                                    ch_v "Ya'sure?"
                            else:

                                $ Girl.change_face("sad", 2,eyes = "surprised")
                                call change_Girl_stat(Girl, "love", 90, -4)
                                call change_Girl_stat(Girl, "obedience", 70, 6)
                                call change_Girl_stat(Girl, "obedience", 200, 3)
                                call change_Girl_stat(Girl, "inhibition", 90, 5)
                                if Girl == RogueX:
                                    ch_r "Come on, I really need it. . ."
                                elif Girl == KittyX:
                                    ch_k "I need you, [Girl.player_petname]!"
                                elif Girl == EmmaX:
                                    call change_Girl_stat(Girl, "love", 90, -2)
                                    call change_Girl_stat(Girl, "obedience", 200, 1)
                                    ch_e "I. . . really need you here, [Girl.player_petname]. . ."
                                elif Girl == LauraX:
                                    call change_Girl_stat(Girl, "obedience", 80, 1)
                                    ch_l "I've got a fevah, and the only prescription is your dick. . ."
                                elif Girl == JeanX:
                                    ch_j "I. . ."
                                    ch_j "Come on, man. . ."
                                    call change_Girl_stat(Girl, "obedience", 90, 5)
                                    ch_j "Please?"
                                elif Girl == StormX:
                                    ch_s ". . ."
                                elif Girl == JubesX:
                                    ch_v "Pretty Please?"
                            $ Count = 1 if Count <= 0 else Count
                            $ counter += 100
                        elif counter > 50:

                            $ Girl.change_face("angry", 1)
                            call change_Girl_stat(Girl, "love", 70, -3)
                            call change_Girl_stat(Girl, "love", 85, -5)
                            call change_Girl_stat(Girl, "obedience", 80, -2)
                            call change_Girl_stat(Girl, "inhibition", 90, 4)
                            if Girl == RogueX:
                                ch_r "I'm not going to beg again."
                            elif Girl == KittyX:
                                ch_k "Not even!"
                            elif Girl == EmmaX:
                                call change_Girl_stat(Girl, "love", 90, -3)
                                call change_Girl_stat(Girl, "obedience", 70, -3)
                                call change_Girl_stat(Girl, "obedience", 200, 2)
                                ch_e "I. . . Once was too much!"
                            elif Girl == LauraX:
                                ch_l "Ooooh, you are pushing it, [Player.name]."
                            elif Girl == JeanX:
                                call change_Girl_stat(Girl, "obedience", 90, 4)
                                ch_j "Whatever. . ."
                            elif Girl == StormX:
                                ch_s "So be it."
                            elif Girl == JubesX:
                                ch_v "Boooo."
                        else:

                            $ Girl.change_face("sad", 2,brows = "confused")
                            call change_Girl_stat(Girl, "love", 95, -2)
                            call change_Girl_stat(Girl, "obedience", 50, -2)
                            call change_Girl_stat(Girl, "obedience", 90, -2)
                            call change_Girl_stat(Girl, "inhibition", 90, 5)
                            if Girl == RogueX:
                                ch_r "I'm not going to beg."
                            elif Girl == KittyX:
                                ch_k "That's. . . rude."
                            elif Girl == EmmaX:
                                call change_Girl_stat(Girl, "obedience", 70, -2)
                                ch_e "That is so beneath me."
                            elif Girl == LauraX:
                                ch_l "Not worth it. ."
                            elif Girl == JeanX:
                                call change_Girl_stat(Girl, "obedience", 90, 4)
                                ch_j "Yeah, not worth it. . ."
                            elif Girl == StormX:
                                ch_s "So be it."
                            elif Girl == JubesX:
                                ch_v "Booo."


            $ line = 0
            if not Act:

                call change_Girl_stat(Girl, "love", 80, -2)
                if Girl == RogueX:
                    ch_r "Ok, your loss, I guess. . ."
                elif Girl == KittyX:
                    ch_k "Too bad 0. ."
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

    call check_favorite_actions (Girl)
    $ Act = Girl.favorite_action

    if Act in ("anal", "sex", "blowjob", "titjob", "handjob", "hotdog"):

        "[Girl.name] reaches down and unzips your fly. . ."
        if not Player.semen:
            "You wish you weren't already drained. . . you stop her hands."
            ch_p "I could actually use a break right now. . "
            $ Act = "fondle_breasts"
        else:
            call Seen_First_Peen (Girl, Partner, 1)

    call before_action(Girl, Act, context = Girl)

label Escalation(Girl=0):


    if counter < 10 or position_timer <= round or Girl.forced:

        return

    if Player.primary_action == "fondle_breast" and approval_check(Girl, 1050,taboo_modifier=4,Alt=[[JeanX],800]) and Girl.lust >= 30 and Girl.action_counter["suck_breasts"]:

        if Player.secondary_action == "suck_breasts":
            $ Player.secondary_action = None
        call change_Girl_stat(Girl, "inhibition", 80, 2)

        call before_action(Girl, "suck_breasts", Girl)

        if "suck_breasts" in Girl.recent_history:

            $ renpy.pop_call()
    elif Player.primary_action == "fondle_thighs" and approval_check(Girl, 1050,taboo_modifier=4,Alt=[[JeanX],800]) and Girl.lust >= 30 and Girl.action_counter["fondle_pussy"]:

        if Player.secondary_action == "fondle_thighs":
            $ Player.secondary_action = None
        call change_Girl_stat(Girl, "inhibition", 80, 4)

        call before_action(Girl, "fondle_thighs", Girl)

        if "fondle_pussy" in Girl.recent_history:

            $ renpy.pop_call()
    elif not Player.semen:

        pass
    elif Player.primary_action == "handjob" and approval_check(Girl, 1200,taboo_modifier=4) and Girl.lust >= 30 and Girl.action_counter["blowjob"]:

        call change_Girl_stat(Girl, "inhibition", 80, 3)

        call before_action(Girl, "blowjob", Girl)
        if "blowjob" in Girl.recent_history:

            $ renpy.pop_call()
    elif Player.primary_action not in ("sex", "anal") and approval_check(Girl, 1400,taboo_modifier=5,Alt=[[JeanX], 1200]) and Girl.lust >= 60 and Girl.action_counter["sex"] >= 3:

        call change_Girl_stat(Girl, "inhibition", 80, 4)

        call before_action(Girl, "sex", Girl)
        if "sex" in Girl.recent_history:

            $ renpy.pop_call()
    elif Player.primary_action != "anal" and approval_check(Girl, 1400,taboo_modifier=5,Alt=[[JeanX], 1200]) and Girl.lust >= 70 and Girl.action_counter["anal"] >= 5:

        call change_Girl_stat(Girl, "inhibition", 80, 5)

        call before_action(Girl, "anal", Girl)
        if "anal" in Girl.recent_history:

            $ renpy.pop_call()


    $ position_timer = 0

    return

label Sex_Dialog(Primary, Secondary):
    $ TempFocus=0
    $ PrimaryLust=0
    $ SecondaryLust=0
    $ line2=0
    $ line3=0
    $ line4=0
    $ D20S=0




    $ D20S = renpy.random.randint(1, 20) if not D20S else D20S
    $ line = 0







    call Girls_taboo (Primary)

    call Primary_SexDialog
    $ line1 = line



    if Player.secondary_action and D20S <= 15:

        $ line = ""
        call Offhand_Dialog
        $ line1 = line1 + line



    if D20S >= 7 and Player.primary_action not in ("masturbation", "lesbian"):

        $ line = 0
        call Girl_Self_lines (Primary, "T3", Primary.secondary_action, D20X=D20S)
        if line:
            $ line3 = line + "_."



    if Secondary and (not second_girl_main_action or 7 <= D20S <= 17 or second_girl_main_action == "watch"):

        $ line = 0
        call SexDialog_Threeway
        if line:
            $ line4 = line + "_."



    call change_Player_stat("focus", 200, TempFocus)


    call change_Girl_stat(Primary, "lust", 200, PrimaryLust)
    $ Primary.lust_face()


    if Secondary:
        $ SecondaryLust += (int(PrimaryLust/10)) if Secondary.likes[Primary.tag] >= 700 else 0
        call change_Girl_stat(Secondary, "lust", 200, SecondaryLust)
        $ Secondary.lust_face()


    "[line1]"
    if line3:

        call Seen_First_Peen (Primary, Secondary, Passive=3)
        "[line3]"
    if line4:


        call Seen_First_Peen (Primary, Secondary, Passive=4)
        "[line4]"
        if second_girl_main_action == "suck_breasts" or second_girl_main_action == "fondle_breasts":

            if approval_check(Primary,500,"I",taboo_modifier=2) and Primary.lust >= 50 and (Primary.Wardrobe.current_Outfit.Clothes["bra"] or Primary.top_number() > 1):

                $ Primary.top_pulled_up = 1
                "[Primary.name] seems frustrated and pulls her top open."

    call Activity_Check (Primary, Secondary, 0)
    if not _return:

        if Primary.forced:


            return
        if Secondary and Secondary.location == Player.location:
            $ Partner = None
            $ second_girl_main_action = None
            $ second_girl_secondary_action = None
        else:



            call stop_all_actions
        jump reset_location

    call Dirty_Talk

    return



label Activity_Check(Girl=0, Girl2=0, Silent=0, Removal=1, ClothesCheck=1, Mod=0, approval=1, Tempshame=0, tabooM=1):






    if Girl == Girl2:
        "Tell oni that the activity check failed after [Player.primary_action]."
        $ Girl.NotAStat = 5


    if "unseen" in Girl.recent_history or "classcaught" in Girl.recent_history:
        return 2

    $ Mod += 200 if Girl.forced else 0
    $ Mod += (Girl.lust*5) if Girl.lust >= 50 else 0

    if Girl2 and ClothesCheck != 2:

        $ Mod = int(Mod/2) if Mod > 0 else Mod

        $ Mod = (Girl.likes[Girl2.tag]-600)

        if Girl in Player.Harem and Girl2 in Player.Harem:
            $ Mod += 500

    if ClothesCheck and Girl2:


        call outfitShame (Girl2, 20)
        $ Tempshame = Girl2.Wardrobe.current_Outfit.Clothes["shame"]

        if Girl == StormX:

            $ approval = 2
        elif Tempshame <= 15 and (approval_check(Girl, 600,Bonus=Mod) or approval_check(Girl, 350, "I")):

            if approval_check(Girl, 900,Bonus=Mod) or approval_check(Girl, 450, "I"):
                $ approval = 2
        elif Tempshame <= 20 and (approval_check(Girl, 900,Bonus=Mod) or approval_check(Girl, 450, "I")):

            if approval_check(Girl, 1100,Bonus=Mod) or approval_check(Girl, 550, "I"):
                $ approval = 2
        elif Tempshame <= 25 and (approval_check(Girl, 1100,Bonus=Mod) or approval_check(Girl, 550, "I")):

            if approval_check(Girl, 1400,Bonus=Mod) or approval_check(Girl, 650, "I"):
                $ approval = 2
        elif (approval_check(Girl, 1400,Bonus=Mod) or approval_check(Girl, 650, "I")):

            if approval_check(Girl, 1600,Bonus=Mod) or approval_check(Girl, 850, "I"):
                $ approval = 2
        else:
            $ approval = 0

    if "exhibitionist" in Girl.traits or approval_check(Girl,900,"I"):

        $ tabooM = 0
    elif approval_check(Girl,50,"X") or approval_check(Girl,800,"I"):
        $ tabooM = 0.5

    if not approval:

        pass
    elif Player.primary_action == "striptease" and Player.secondary_action != "jerking_off":
        pass
    elif not Player.primary_action:
        pass
    elif Player.primary_action == "eat_ass":
        $ approval = approval_check(Girl, 1550,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "anal":
        $ approval = approval_check(Girl, 1550,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "sex":
        $ approval = approval_check(Girl, 1400,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "eat_pussy":
        $ approval = approval_check(Girl, 1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.secondary_action == "jerking_off":
        $ approval = approval_check(Girl, 1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "blowjob":
        $ approval = approval_check(Girl, 1300,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "titjob":
        $ approval = approval_check(Girl, 1200,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "hotdog":
        $ approval = approval_check(Girl, 1000,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "handjob" or girl_secondary_action == "handjob":
        $ approval = approval_check(Girl, 1100,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "footjob":
        $ approval = approval_check(Girl, 1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "dildo_ass":
        $ approval = approval_check(Girl, 1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "dildo_pussy":
        $ approval = approval_check(Girl, 1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "finger_ass":
        $ approval = approval_check(Girl, 1300,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "fondle_pussy" or Player.primary_action == "finger_pussy":
        $ approval = approval_check(Girl, 1050,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "suck_breasts":
        $ approval = approval_check(Girl, 1050,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "fondle_breasts":
        $ approval = approval_check(Girl,950,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "fondle_ass":
        $ approval = approval_check(Girl,850,Bonus=Mod, taboo_modifier = (tabooM* 1 ))

    elif Player.primary_action == "masturbation":
        $ approval = approval_check(Girl, 1200,Bonus=Mod, taboo_modifier = (tabooM* 2 ))

    elif Player.primary_action == "kiss":
        $ approval = approval_check(Girl,500,Bonus=Mod, taboo_modifier = 0)
    elif Player.primary_action == "fondle_thighs":
        $ approval = approval_check(Girl,750,Bonus=Mod, taboo_modifier = 0)

    elif Player.primary_action == "lesbian":
        $ approval = approval_check(Girl, 1350,Bonus=Mod, taboo_modifier = (tabooM* 2 ))


    if not approval:

        pass
    elif not second_girl_main_action:
        pass
    elif second_girl_main_action == "eat_ass":
        $ approval = approval_check(Girl, 1750,Bonus=(Mod+200), taboo_modifier = (tabooM* 3 ))
    elif second_girl_main_action == "eat_pussy":
        $ approval = approval_check(Girl, 1450,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "blowjob":
        $ approval = approval_check(Girl, 1300,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "handjob":
        $ approval = approval_check(Girl, 1200,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "finger_ass":
        $ approval = approval_check(Girl, 1500,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "fondle_pussy":
        $ approval = approval_check(Girl, 1250,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "suck_breasts":
        $ approval = approval_check(Girl, 1250,Bonus=(Mod+200), taboo_modifier = (tabooM* 3 ))
    elif second_girl_main_action == "fondle_breasts":
        $ approval = approval_check(Girl, 1150,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "kiss girl":
        $ approval = approval_check(Girl, 1050,Bonus=(Mod+200), taboo_modifier = 0)
    elif second_girl_main_action == "kiss both":
        $ approval = approval_check(Girl, 1050,Bonus=(Mod+200), taboo_modifier = 0)
    elif second_girl_main_action == "fondle_ass":
        $ approval = approval_check(Girl, 1050,Bonus=(Mod+200), taboo_modifier = (tabooM* 1 ))
    elif second_girl_main_action == "masturbation":
        $ approval = approval_check(Girl, 1400,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "watch":
        $ approval = approval_check(Girl, 1000,Bonus=(Mod+200), taboo_modifier = 0)
    elif second_girl_main_action == "kiss":
        $ approval = approval_check(Girl,600,Bonus=Mod, taboo_modifier = 0)

    if not Silent and not approval and not Girl.forced:
        $ Girl.change_face("sadside", 1)
        if Girl == RogueX:
            if Girl2:
                ch_r "I don't know, with [Girl2.name] here and all."
            ch_r "Ain't none a this right, [Girl.player_petname]."
        elif Girl == KittyX:
            if Girl2:
                ch_k "I don't know, with [Girl2.name] being here."
            ch_k "I'm[KittyX.like]not really comfortable with this?"
        elif Girl == EmmaX:
            if Girl2:
                ch_e "I'm unsure that I'm comfortable doing this with [Girl2.name] here."
            ch_e "This has become a bit too. . . scandalous for my tastes."
        elif Girl == LauraX:
            if Girl2:
                ch_l "[Girl2.name]'s weirding me out."
            else:
                ch_l "This is getting weird."
            ch_l "I'll see you later."
        elif Girl == JeanX:
            if Girl2:
                ch_j "I'd rather not be here with [Girl2.name]."
            ch_j "I'm gonna leave it here."
        elif Girl == StormX:
            if Girl2:
                ch_s "I do not want to do this with [Girl2.name] around."
            ch_s "This has become a bit much for me, I am sorry."
        elif Girl == JubesX:
            if Girl2:
                ch_v "Not around [Girl2.name], [Girl.player_petname]."
            ch_v "This is totally not cool. Sorry."

    if Removal and not approval and not Girl.forced:
        call remove_Girl(Girl, 2)
        "[Girl.name] takes off."

    return approval

label Seen_First_Peen(Primary=0, Secondary=0, Silent=0, Undress=0, Passive=0, GirlsNum=0, React=0, temp_Girls=[]):






    if not Primary:

        $ temp_Girls = Present[:]
        $ renpy.random.shuffle(temp_Girls)
        while temp_Girls:


            if (focused_Girl == temp_Girls[0] or D20 >= 10) and "peen" not in temp_Girls[0].recent_history:


                call Girl_First_Peen (temp_Girls[0], Silent, Undress)
                $ GirlsNum = _return
            $ temp_Girls.remove(temp_Girls[0])

        if not GirlsNum:

            if "naked" not in Player.recent_history and Undress:
                "You strip nude."
                $ Player.add_word(1,"naked", 0, 0, 0)
            elif "cockout" in Player.recent_history:
                return
            else:
                "You whip your cock out."

            $ Player.add_word(1,"cockout", 0, 0, 0)
    else:


        if Passive:

            if approval == Passive and "cockout" not in Player.recent_history:

                if approval == 3:


                    call Girl_First_Peen (Primary, React=1)
                elif approval == 4:


                    call Girl_First_Peen (Secondary, React=1)
                $ approval = 0
            if "cockout" not in Player.recent_history:
                return


        call Girl_First_Peen (Primary, Silent, Undress, React=React)

        if Secondary:

            call Girl_First_Peen (Secondary, Silent, Undress, Second=_return)
    return



label Girl_First_Peen(Girl=0, Silent=0, Undress=0, Second=0, React=0):







    if Girl.location != Player.location:
        if Partner == Girl:
            $ Partner = 0
        return
    if "cockout" in Player.recent_history and "peen" in Girl.recent_history:

        return

    if "unseen" in Girl.recent_history:

        return

    $ Girl.recent_history.append("peen")
    $ Girl.daily_history.append("peen")
    $ Girl.seen_peen += 1
    call change_Girl_stat(Girl, "inhibition", 30, 2)
    call change_Girl_stat(Girl, "inhibition", 80, 1)

    if Second:

        if Girl.seen_peen == 1:
            $ Girl.change_face("surprised", 2)
            if Girl == RogueX:
                ch_r "Wow, yeah, that's pretty nice. . ."
            elif Girl == KittyX:
                ch_k "Oh, wow, you aren't kidding. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("smirk", 2, eyes = "down")
                ch_e "My, that certainly is an impressive specimen. . ."
            elif Girl == LauraX:
                $ Girl.change_face("smirk", 2, eyes = "down")
                ch_l "Huh, that's a pretty good one you got there. . ."
            elif Girl == JeanX:
                $ Girl.change_face("smirk", 2, eyes = "down")
                ch_j "Yeah, looking good. . ."
            elif Girl == StormX:
                $ Girl.change_face("smirk", 2, eyes = "down")
                ch_s "Yes, that is impressive. . ."
            elif Girl == JubesX:
                $ Girl.change_face("smirk", 2, eyes = "down")
                ch_v "Oh, wow, yeah. . ."
            $ Girl.change_face("bemused", 1)
        elif Second == 1:

            if not approval_check(Girl, 800) and not approval_check(Girl, 500, "I"):
                $ Girl.change_face("sad", 1)
                if Girl == RogueX:
                    ch_r "If you're inta that sorta thing. . ."
                elif Girl == KittyX:
                    ch_k "I mean I guess. . ."
                elif Girl == EmmaX:
                    ch_e "I suppose you haven't had a lot of experience. . ."
                elif Girl == LauraX:
                    ch_l "I guess 0. ."
                elif Girl == JeanX:
                    ch_j "Yeah, it's ok. . ."
                elif Girl == StormX:
                    ch_s "I suppose it could be. . ."
                elif Girl == JubesX:
                    ch_v "I guess. . ."
            else:
                $ Girl.change_face("bemused", 1)
                if Girl == RogueX:
                    ch_r "Yeah, it really is a beauty. . ."
                elif Girl == KittyX:
                    ch_k "I know, right?!"
                elif Girl == EmmaX:
                    ch_e "Yes, it caught me off guard as well. . ."
                elif Girl == LauraX:
                    ch_l "Yeah, nice, isn't it. . ."
                elif Girl == JeanX:
                    ch_j "Right?"
                elif Girl == StormX:
                    ch_s "I thought so as well."
                elif Girl == JubesX:
                    ch_v "Right?"
        elif Second == 2:

            if not approval_check(Girl, 800) and not approval_check(Girl, 500, "I"):
                $ Girl.change_face("sad", 1)
                if Girl == RogueX:
                    ch_r "Right, whatever. . ."
                elif Girl == KittyX:
                    ch_k "So over it. . ."
                elif Girl == EmmaX:
                    ch_e "A fine judge of quality. . ."
                elif Girl == LauraX:
                    ch_l "I guess. . ."
                elif Girl == JeanX:
                    ch_j "Yeah. . ."
                elif Girl == StormX:
                    ch_s "True. . ."
                elif Girl == JubesX:
                    ch_v "I guess. . ."
            else:
                $ Girl.change_face("confused", 1)
                if Girl == RogueX:
                    ch_r "Well I liked it. . ."
                    $ Girl.change_face("sexy", 1)
                elif Girl == KittyX:
                    ch_k "Come on, it's really cute!"
                    $ Girl.change_face("smile", 1)
                elif Girl == EmmaX:
                    ch_e "You just don't appreciate the finer things. . ."
                    $ Girl.change_face("sly", 0)
                elif Girl == LauraX:
                    ch_l "Aw, come on, it's not that bad. . ."
                    $ Girl.change_face("sly", 0)
                elif Girl == JeanX:
                    ch_j "I mean, I've seen worse. . ."
                    $ Girl.change_face("sly", 0)
                elif Girl == StormX:
                    ch_s "It's far from the worst I've seen. . ."
                    $ Girl.change_face("sly", 0)
                elif Girl == JubesX:
                    ch_v "More for me, I guess. . ."
                    $ Girl.change_face("sly", 0)
        $ Silent = 1

    if Undress:
        $ Player.add_word(1,"naked")
    if not Silent:
        if "cockout" in Player.recent_history:
            $ Girl.change_face("down", 2)
            "[Girl.name] glances down at your exposed cock."
        elif React:

            "[Girl.name] reaches for your pants and pulls out your cock."
        elif Undress:
            "You strip nude."
        else:
            "You whip your cock out."
        $ Player.add_word(1,"cockout")
        if not Girl.forced and not React and taboo > 20 and (not approval_check(Girl, 1500) or Girl.SEXP < 10) and Player.location != "bg_showerroom" and Girl not in (JeanX,StormX):

            if not approval_check(Girl, 800) and not approval_check(Girl, 500, "I"):

                if Girl == EmmaX and ("detention" in Girl.recent_history or "classcaught" in Girl.recent_history):

                    $ Girl.change_face("confused", eyes = "down")
                    ch_e "Mmm?"
                    $ Girl.change_face("surprised", eyes = "squint")
                    if Girl.seen_peen == 1:
                        call change_Girl_stat(Girl, "love", 30, 10)
                        call change_Girl_stat(Girl, "love", 90, 5)
                        call change_Girl_stat(Girl, "obedience", 50, 20)
                        call change_Girl_stat(Girl, "inhibition", 60, 30)
                    else:
                        call change_Girl_stat(Girl, "love", 90, 2)
                        call change_Girl_stat(Girl, "obedience", 50, 3)
                        call change_Girl_stat(Girl, "inhibition", 60, 5)
                    ch_e "Well I suppose I can make an exception in this case."
                    $ React = 1
                else:

                    $ Girl.change_face("surprised", 2)
                    if Girl == RogueX:
                        ch_r "What the hell?"
                    elif Girl == KittyX:
                        ch_k "Huh?!"
                    elif Girl == EmmaX:
                        $ Girl.eyes = "down"
                        ch_e "Mmm?"
                    elif Girl == LauraX:
                        $ Girl.eyes = "down"
                        ch_l "Mmm?"
                    elif Girl == JubesX:
                        $ Girl.eyes = "down"
                        ch_v "Hey. . ."
                        $ Girl.eyes = "squint"
                        ch_v "What's that about?"
                    $ Girl.change_face("angry", 1)
                    $ Girl.recent_history.append("angry")
                    $ Girl.daily_history.append("angry")
                    $ React = 2
                    if Girl.seen_peen == 1:
                        call change_Girl_stat(Girl, "love", 90, -20)
                        call change_Girl_stat(Girl, "obedience", 50, 30)
                        call change_Girl_stat(Girl, "inhibition", 60, 20)
                    else:

                        if Girl == RogueX:
                            ch_r "What is {i}wrong{/i} with you?"
                        elif Girl == KittyX:
                            ch_k "Dude, seriously, you've got a problem!"
                        elif Girl == EmmaX:
                            ch_e "[Girl.player_petname]! We are going to have to work through this. . . problem of yours."
                        elif Girl == LauraX:
                            ch_l "Dude, not cool."
                        elif Girl == JubesX:
                            ch_v "Keep it in your pants. . ."
                        if Girl.daily_history.count("peen") >= 2:

                            call change_Girl_stat(Girl, "love", 90, -1)
                            call change_Girl_stat(Girl, "obedience", 50, 1)
                            call change_Girl_stat(Girl, "inhibition", 60, 2)
                        else:
                            call change_Girl_stat(Girl, "love", 90, -5)
                            call change_Girl_stat(Girl, "obedience", 50, 10)
                            call change_Girl_stat(Girl, "inhibition", 60, 10)
            else:


                $ Girl.change_face("surprised", 2)
                if Girl == RogueX:
                    ch_r "What are you- you should really put that thing away!"
                elif Girl == KittyX:
                    ch_k "Um, you should[Girl.like]put that away in public."
                elif Girl == EmmaX:
                    ch_e "You really should be careful where you display that thing."
                elif Girl == LauraX:
                    ch_l "I think there's a time and place for that sort of thing."
                elif Girl == JubesX:
                    ch_v "Um, maybe you should put that away?"
                $ Girl.change_face("bemused", 1)
                if Girl.seen_peen == 1:
                    if Girl == RogueX:
                        ch_r "I mean. . . no, definitely put that away!"
                    elif Girl == KittyX:
                        ch_k "Or[Girl.like]maybe. . ."
                    elif Girl == EmmaX:
                        $ Girl.eyes = "down"
                        ch_e ". . . impressive though it may be. . ."
                    elif Girl == LauraX:
                        ch_l ". . . not that I mind, myself. . ."
                    elif Girl == JubesX:
                        ch_v "Or. . . not. . ."
                    call change_Girl_stat(Girl, "love", 90, 20)
                    call change_Girl_stat(Girl, "obedience", 50, 20)
                    call change_Girl_stat(Girl, "inhibition", 60, 30)
                $ React = 2


        elif Girl.seen_peen > 10:

            return False
        elif approval_check(Girl, 1200) or approval_check(Girl, 500, "L"):

            $ Girl.change_face("sly", 1)
            if Girl.seen_peen == 1:
                $ Girl.change_face("surprised", 2)
                if Girl == RogueX:
                    ch_r "Whoa, I didn't know they looked so big up close."
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "love", 90, 5)
                elif Girl == KittyX:
                    $ Girl.change_face("surprised", 2)
                    ch_k "That's. . . impressive."
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "love", 90, 3)
                elif Girl == EmmaX:
                    $ Girl.change_face("surprised", 1, eyes = "down")
                    ch_e "Well that's certainly an interesting specimen."
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "love", 50, 5)
                    call change_Girl_stat(Girl, "love", 90, 10)
                elif Girl == LauraX:
                    $ Girl.change_face("surprised", 1, eyes = "down")
                    ch_l "Huh, that's a pretty good one you got there. . ."
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "love", 50, 5)
                    call change_Girl_stat(Girl, "love", 90, 10)
                elif Girl == JeanX:
                    $ Girl.change_face("confused", 1, eyes = "down", mouth = "smile")
                    ch_j "Well, what do we have here. . ."
                    $ Girl.change_face("bemused", 1)
                    ch_j "Preeety nice there, [Girl.player_petname]."
                    call change_Girl_stat(Girl, "love", 50, 5)
                    call change_Girl_stat(Girl, "love", 90, 10)
                    call change_Girl_stat(Girl, "obedience", 80, 3)
                elif Girl == StormX:
                    $ Girl.change_face("confused", 1, eyes = "down")
                    ch_s "Hmm. . . that is a lovely one."
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "love", 50, 5)
                    call change_Girl_stat(Girl, "love", 90, 5)
                    call change_Girl_stat(Girl, "inhibition", 60, 2)
                elif Girl == JubesX:
                    $ Girl.change_face("surprised", 2, eyes = "down")
                    ch_v "Oh. . . nice."
                    $ Girl.change_face("sly", 1)
                    call change_Girl_stat(Girl, "love", 80, 3)
                    call change_Girl_stat(Girl, "obedience", 80, 1)
                    call change_Girl_stat(Girl, "inhibition", 60, 4)
            elif Girl.seen_peen == 2:
                if Girl == RogueX:
                    ch_r "That thing sure is impressive."
                    call change_Girl_stat(Girl, "obedience", 50, 5)
                elif Girl == KittyX:
                    ch_k "I can't get over that."
                    call change_Girl_stat(Girl, "obedience", 50, 7)
                elif Girl == EmmaX:
                    $ Girl.eyes = "down"
                    ch_e "Oh, hello again."
                    call change_Girl_stat(Girl, "inhibition", 50, 5)
                elif Girl == LauraX:
                    $ Girl.eyes = "down"
                    ch_l "Oh, there it is."
                    call change_Girl_stat(Girl, "obedience", 50, 2)
                    call change_Girl_stat(Girl, "inhibition", 50, 3)
                elif Girl == JeanX:
                    $ Girl.eyes = "down"
                    ch_j "Still pretty impressive. . ."
                    call change_Girl_stat(Girl, "love", 90, 3)
                    call change_Girl_stat(Girl, "obedience", 80, 3)
                elif Girl == StormX:
                    $ Girl.eyes = "down"
                    ch_s "Hmm. . ."
                    call change_Girl_stat(Girl, "inhibition", 50, 2)
                elif Girl == JubesX:
                    $ Girl.change_face("sly", 1, eyes = "down")
                    ch_v "Hello again."
                    $ Girl.change_face("sly", 1)
                    call change_Girl_stat(Girl, "obedience", 80, 1)
                    call change_Girl_stat(Girl, "inhibition", 60, 1)
            elif Girl.seen_peen == 5:
                if Girl == RogueX:
                    ch_r "I certainly appreciate that guy."
                    call change_Girl_stat(Girl, "inhibition", 60, 5)
                elif Girl == KittyX:
                    ch_k "There it is."
                    call change_Girl_stat(Girl, "inhibition", 60, 5)
                elif Girl == EmmaX:
                    ch_e "Yes, we've seen that before."
                    call change_Girl_stat(Girl, "obedience", 60, 7)
                elif Girl == LauraX:
                    ch_l "Yeah, I've seen that one."
                    call change_Girl_stat(Girl, "obedience", 60, 4)
                    call change_Girl_stat(Girl, "inhibition", 60, 3)
                elif Girl == JeanX:
                    $ Girl.eyes = "down"
                    ch_j "Nice. . ."
                    call change_Girl_stat(Girl, "love", 90, 3)
                    call change_Girl_stat(Girl, "obedience", 80, 2)
                elif Girl == StormX:
                    ch_s ". . ."
                    call change_Girl_stat(Girl, "inhibition", 60, 5)
                elif Girl == JubesX:
                    $ Girl.change_face("sly", 1, eyes = "down")
                    ch_v "Hey there. . ."
                    $ Girl.change_face("sly", 1)
                    call change_Girl_stat(Girl, "love", 80, 1)
                    call change_Girl_stat(Girl, "obedience", 80, 2)
                    call change_Girl_stat(Girl, "inhibition", 60, 2)
            elif Girl.seen_peen == 10:
                if Girl == RogueX:
                    ch_r "I never get tired of seeing that."
                    call change_Girl_stat(Girl, "love", 90, 10)
                elif Girl == KittyX:
                    ch_k "So beautiful."
                    call change_Girl_stat(Girl, "obedience", 80, 10)
                    call change_Girl_stat(Girl, "inhibition", 60, 3)
                elif Girl == EmmaX:
                    $ Girl.eyes = "down"
                    ch_e "I do appreciate some of your features."
                    call change_Girl_stat(Girl, "obedience", 80, 5)
                    call change_Girl_stat(Girl, "inhibition", 60, 10)
                elif Girl == LauraX:
                    $ Girl.eyes = "down"
                    ch_l "I don't get tired of that view."
                    call change_Girl_stat(Girl, "obedience", 80, 8)
                    call change_Girl_stat(Girl, "inhibition", 60, 7)
                elif Girl == JeanX:
                    $ Girl.eyes = "down"
                    ch_j "Thanks for that. . ."
                    call change_Girl_stat(Girl, "love", 90, 10)
                    call change_Girl_stat(Girl, "obedience", 80, 8)
                elif Girl == StormX:
                    $ Girl.eyes = "down"
                    ch_s "Well, I do enjoy that one."
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "love", 90, 5)
                    call change_Girl_stat(Girl, "inhibition", 60, 2)
                elif Girl == JubesX:
                    $ Girl.change_face("confused", 1, eyes = "down")
                    ch_v "Kinda. . . hypnotic. . ."
                    $ Girl.change_face("sly", 1)
                    call change_Girl_stat(Girl, "love", 80, 1)
                    call change_Girl_stat(Girl, "obedience", 80, 3)
                    call change_Girl_stat(Girl, "inhibition", 60, 2)
            $ React = 1
        else:

            $ Girl.change_face("sad", 1)
            if Girl.seen_peen == 1:
                $ Girl.change_face("perplexed", 1 )
                $ Girl.eyes = "down"
                if Girl == RogueX:
                    ch_r "Well, I guess that's impressive. What do you plan to do with it?"
                    call change_Girl_stat(Girl, "obedience", 50, 5)
                    call change_Girl_stat(Girl, "inhibition", 60, 5)
                elif Girl == KittyX:
                    ch_k "Well that happened. . ."
                elif Girl == EmmaX:
                    ch_e "Are you aware that your dick is out?"
                    call change_Girl_stat(Girl, "obedience", 50, 2)
                elif Girl == LauraX:
                    ch_l "Your dick is out."
                    call change_Girl_stat(Girl, "inhibition", 60, 2)
                elif Girl == JeanX:
                    ch_j "Hey, you're penis is out."
                    call change_Girl_stat(Girl, "obedience", 80, 4)
                    call change_Girl_stat(Girl, "inhibition", 70, 4)
                elif Girl == StormX:
                    ch_s "Apparently you enjoy a nice breeze as well. . ."
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "inhibition", 60, 5)
                elif Girl == JubesX:
                    ch_v "Hmm, ok. . ."
                    call change_Girl_stat(Girl, "obedience", 80, 2)
                    call change_Girl_stat(Girl, "inhibition", 60, 2)
                call change_Girl_stat(Girl, "obedience", 50, 5)
                call change_Girl_stat(Girl, "inhibition", 60, 5)
            elif Girl.seen_peen < 5:
                $ Girl.change_face("sad", 0)
                if Girl == RogueX:
                    ch_r "Yeah, I've seen it."
                elif Girl == KittyX:
                    ch_k "Huh."
                elif Girl == EmmaX:
                    ch_e "You might want to put that away, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "Hey. . ."
                    ch_l "You might want to put that away, [Girl.player_petname]."
                elif Girl == JeanX:
                    ch_j "I've seen that one before."
                elif Girl == StormX:
                    ch_s ". . ."
                elif Girl == JubesX:
                    ch_v "That's. . . inappropriate. . ."
                    call change_Girl_stat(Girl, "obedience", 80, 2)
                call change_Girl_stat(Girl, "inhibition", 60, 2)
            elif Girl.seen_peen == 10:
                if Girl == RogueX:
                    ch_r "I'm getting tired of seeing that."
                    call change_Girl_stat(Girl, "obedience", 50, 5)
                    call change_Girl_stat(Girl, "inhibition", 60, 5)
                elif Girl == KittyX:
                    ch_k "[Girl.Like]put that away."
                    call change_Girl_stat(Girl, "obedience", 50, 7)
                    call change_Girl_stat(Girl, "inhibition", 60, 3)
                elif Girl == EmmaX:
                    ch_e "Yes, we've all seen that before."
                    call change_Girl_stat(Girl, "obedience", 50, 7)
                    call change_Girl_stat(Girl, "inhibition", 60, 5)
                elif Girl == LauraX:
                    ch_l "Yeah, yeah, waving your cock around again."
                    call change_Girl_stat(Girl, "obedience", 50, 8)
                    call change_Girl_stat(Girl, "inhibition", 60, 4)
                elif Girl == JeanX:
                    ch_j "Oh, Penis. So original."
                    call change_Girl_stat(Girl, "obedience", 50, 8)
                    call change_Girl_stat(Girl, "inhibition", 60, 4)
                elif Girl == StormX:
                    ch_s ". . ."
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "obedience", 50, 2)
                    call change_Girl_stat(Girl, "inhibition", 60, 4)
                elif Girl == JubesX:
                    ch_v ". . ."
                    call change_Girl_stat(Girl, "obedience", 80, 2)
                    call change_Girl_stat(Girl, "inhibition", 60, 2)
            $ React = 2
    else:

        $ Player.recent_history.append("cockout")
        if Girl.seen_peen > 10:
            return
        elif approval_check(Girl, 1200) or approval_check(Girl, 500, "L"):
            if Girl.seen_peen == 1:
                call change_Girl_stat(Girl, "love", 90, 5)
            elif Girl.seen_peen == 2:
                call change_Girl_stat(Girl, "obedience", 50, 5)
            elif Girl.seen_peen == 5:
                call change_Girl_stat(Girl, "inhibition", 60, 5)
            elif Girl.seen_peen == 10:
                call change_Girl_stat(Girl, "love", 90, 10)
        else:
            if Girl.seen_peen == 1:
                call change_Girl_stat(Girl, "obedience", 50, 5)
                call change_Girl_stat(Girl, "inhibition", 60, 5)
                $ Girl.add_word(1, 0, 0, 0,"seenpeen")
            elif Girl.seen_peen < 5:
                call change_Girl_stat(Girl, "inhibition", 60, 2)
            elif Girl.seen_peen == 10:
                call change_Girl_stat(Girl, "obedience", 50, 5)
                call change_Girl_stat(Girl, "inhibition", 60, 5)
        if Girl == JubesX:
            call change_Girl_stat(Girl, "obedience", 80, 1)
    if Girl.seen_peen == 1:
        if Girl == JeanX:
            call change_Girl_stat(Girl, "love", 90, 10)
            call change_Girl_stat(Girl, "obedience", 30, 20)
            call change_Girl_stat(Girl, "obedience", 50, 10)
            call change_Girl_stat(Girl, "obedience", 80, 5)
        elif Girl == JubesX:
            call change_Girl_stat(Girl, "obedience", 80, 3)
        call change_Girl_stat(Girl, "love", 90, 15)
        call change_Girl_stat(Girl, "obedience", 90, 20,Alt=[[StormX],900, 0])
        call change_Girl_stat(Girl, "inhibition", 60, 20)
        call change_Girl_stat(Girl, "lust", 200, 5)
    $ Girl.change_face("sly", 1)
    return React

label Girls_taboo(Girl, Choice=0):
    if Player.location in bedrooms or door_locked:
        return

    $ Player.add_word(1, 0,Girl.tag)
    $ Player.add_word(1, 0,"scent")

    if "uninterrupted" in Girl.recent_history:
        return
    elif "MindFuck" in Player.recent_history:
        return
    $ counter = Girl.recent_history.count("spotted") if "spotted" in Girl.recent_history else 1
    $ counter = 4 if counter > 4 else counter

    $ D20 = renpy.random.randint(1, 20)

    if "screen" in Girl.traits or (Partner and "screen" in Partner.traits):
        $ D20 += 8

    if D20 < 10:

        if taboo > 20:
            if (Player.primary_action == "kiss" and not Player.secondary_action and not girl_secondary_action):

                pass
            elif Girl not in Rules:

                $ Girl.change_face("surprised", 1)
                if Player.primary_action == "blowjob" or Player.primary_action == "handjob" or Player.primary_action == "titjob":
                    "[Girl.name] stops what she's doing with a startled look."
                else:
                    "You feel a slight buzzing in your head and stop what you're doing."
                ch_x "Cease that behavior at once! Come to my office immediately!"
                call show_full_body(Girl)
                call caught_having_sex(Girl)
                return
            else:

                ch_x "Hmmm. . ."
                call change_Girl_stat(Girl, "inhibition", 90, 2)
                call change_Girl_stat(Girl, "lust", 200, 3)
        if Player.location == "bg_classroom" and EmmaX.teaching and Girl != EmmaX:

            call Emma_Teacher_Caught (Girl)
        elif Player.location == "bg_classroom" and StormX.teaching and Girl != StormX:

            call Storm_Teacher_Caught (Girl)
        elif "interruption" in Player.recent_history:

            pass
        elif D20 == 1 and AloneCheck(Girl) and time_index < 3:
            python:
                shuffled_Girls = active_Girls[:]
                renpy.random.shuffle(shuffled_Girls)

                interrupting_Girl = None

                for G in shuffled_Girls:
                    if G != Girl:
                        if G.location != Player.location and "lockedout" not in Girl.traits:
                            interrupting_Girl = G

                            break

            if interrupting_Girl:
                call Girls_arrive(interrupting_Girl)

        python:
            Other = None

            for G in all_Girls:
                if G != Girl and G.location == Player.location:
                    Other = G

                    break

        if Other:
            call Girls_Noticed(Girl, Other)

    if taboo <= 20:
        python:
            Other = None

            for G in all_Girls:
                if G != Girl and G.location == Player.location:
                    Other = G

                    break

        if Other:
            call Girls_Noticed (Girl, Other)
        return
    elif (Player.primary_action == "kiss" and not Player.secondary_action and not girl_secondary_action):

        pass
    elif counter < 4:


        if Girl in (EmmaX,StormX) and "public" not in Girl.history:
            $ Girl.history.append("public")

        if "spotted" not in Girl.recent_history:
            "Some of the other students notice you and [Girl.name]."
            call change_Girl_stat(Girl, "inhibition", 200, 2)
            $ Girl.reputation -= 2
            $ Player.reputation -= 2
        elif counter < 3:
            "A few more students notice you and [Girl.name]."
            call change_Girl_stat(Girl, "inhibition", 200, 2)
            $ Girl.reputation -= 1
            $ Player.reputation -= 1
        elif counter == 3:
            "You've got quite an audience."
            call change_Girl_stat(Girl, "inhibition", 200, 3)
            $ Girl.reputation -= 1
            $ Player.reputation -= 1
        if Partner:
            $ Partner.reputation -= 1


        if "exhibitionist" in Girl.traits:
            $ Girl.change_face("sexy", 0)
            if "spotted" not in Girl.recent_history:
                if Girl == RogueX:
                    ch_r "Let'em watch, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "I think we can give'em a show, [Girl.player_petname]."
                elif Girl == EmmaX:
                    ch_e "Hmm, perhaps they can learn a few things, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "Well, let's give'em what they want."
                elif Girl == JeanX:
                    ch_j "Well of course they want this."
                elif Girl == StormX:
                    ch_s "Let them worship us. . ."
                elif Girl == JubesX:
                    ch_v "I'm good if you are. . ."
            call change_Girl_stat(Girl, "lust", 200, 4)
            $ Choice = "A"
        elif approval_check(Girl, 650, "I", taboo_modifier=counter):

            $ Girl.change_face("sexy", 1, brows = "sad")
            if "spotted" not in Girl.recent_history:
                if Girl == RogueX:
                    ch_r "Hmm, what should we do about this, [Girl.player_petname]?"
                elif Girl == KittyX:
                    ch_k "What should we do?"
                elif Girl == EmmaX:
                    ch_e "Well, this is something of a situation."
                elif Girl == LauraX:
                    ch_l "How do you want to play this?"
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "obedience", 80, 3)
                    call change_Girl_stat(Girl, "inhibition", 80, 3)
                    ch_j "Looks like we have an audience. . ."
                elif Girl == StormX:
                    ch_s "We seem to have attracted some attention. . ."
                elif Girl == JubesX:
                    ch_v "Oh, um, they're looking. . ."
            call change_Girl_stat(Girl, "lust", 200, 3)
            $ Choice = "B"
        elif approval_check(Girl, 1000, "OI", taboo_modifier=counter):

            $ Girl.change_face("surprised", 2)
            if Girl in (EmmaX,StormX):
                "[Girl.name] looks a bit concerned."
            elif Girl == LauraX:
                "[Girl.name] looks a bit uncomfortable."
            else:
                "[Girl.name] looks a bit panicked."
            call change_Girl_stat(Girl, "lust", 200, 3)
            $ Choice = "C"
        else:

            $ Girl.change_face("surprised", 2)
            if "spotted" not in Girl.recent_history:
                if Girl == KittyX:
                    "[Girl.name] bolts up with an embarassed look. She grabs her clothes and flings herself through the nearest wall."
                elif Girl in (EmmaX,StormX):
                    "[Girl.name] bolts up with an embarassed look. She grabs her clothes and stalks off."
                else:
                    "[Girl.name] bolts up with an embarassed look. She runs off while putting her clothes back on."
                $ Girl.reputation -= 3 if Girl.reputation >= 30 else Girl.reputation
            else:
                if Girl == KittyX:
                    call change_Girl_stat(Girl, "love", 90, -15)
                    "With a sudden embarrassed start, [Girl.name] panics. She dives through the nearest wall."
                elif Girl in (EmmaX,StormX):
                    call change_Girl_stat(Girl, "love", 90, -15)
                    "With a sudden embarrassed start, [Girl.name] stop what she's doing. She grabs her clothes and stalks off."
                else:
                    "With a sudden embarrassed start, [Girl.name] panics. She takes off while throwing her clothes together."
            "You head back to your room."
            $ Choice = "stop"

        if Choice != "stop":
            menu:
                "What would you like to do?"
                "Let them watch. . ." if "spotted" not in Girl.recent_history:
                    if Choice == "A":
                        $ Girl.change_face("sexy", 0)
                        if Girl == RogueX:
                            ch_r "That's what I'm talking about."
                        elif Girl == KittyX:
                            ch_k "I'll bring my \"A\" game."
                        elif Girl == EmmaX:
                            ch_e "It's only fair."
                        elif Girl == LauraX:
                            ch_l "I can handle that."
                        elif Girl == JeanX:
                            ch_j "Yeeeaah."
                        elif Girl == StormX:
                            ch_s "Yes. . ."
                        elif Girl == JubesX:
                            ch_v "Let's move it!"
                    elif Choice == "B":

                        $ Girl.change_face("sexy", 1,brows = "sad")
                        if Girl == RogueX:
                            ch_r "Uh, ok."
                        elif Girl == KittyX:
                            ch_k "Hehe, um, yeah."
                        elif Girl == EmmaX:
                            ch_e "I do suppose we can show them how it's done."
                        elif Girl == LauraX:
                            ch_l "Ok."
                        elif Girl == JeanX:
                            ch_j "Sure, whatever."
                        elif Girl == StormX:
                            ch_s "I suppose. . ."
                        elif Girl == JubesX:
                            ch_v "Um, yeah. . ."
                    elif Choice == "C":
                        $ Girl.change_face("sexy", 2)
                        if Girl.obedience > Girl.inhibition:
                            $ Girl.eyes = "side"
                            if Girl == RogueX:
                                ch_r "If you say so, [Girl.player_petname]."
                            elif Girl == KittyX:
                                ch_k "If you insist, [KittyX.player_petname]."
                            elif Girl == EmmaX:
                                ch_e "I won't back down if you won't, [EmmaX.player_petname]."
                            elif Girl == LauraX:
                                ch_l "I guess."
                            elif Girl == JeanX:
                                ch_j "I suppose we could. . ."
                            elif Girl == StormX:
                                ch_s "Certainly. . ."
                            elif Girl == JubesX:
                                ch_v ". . . Right."
                        else:
                            $ Girl.mouth = "smile"
                            $ Girl.brows = "sad"
                            if Girl == RogueX:
                                ch_r "Uh, I guess. . ."
                            elif Girl == KittyX:
                                ch_k "Yeah[KittyX.like]sure. . ."
                            elif Girl == EmmaX:
                                ch_e "Not that I mind, of course."
                            elif Girl == LauraX:
                                ch_l "Whatever. . ."
                            elif Girl == JeanX:
                                call change_Girl_stat(Girl, "obedience", 80, 3)
                                call change_Girl_stat(Girl, "inhibition", 80, 3)
                                ch_j "Yeah. . ."
                            elif Girl == StormX:
                                ch_s "Very well. . ."
                            elif Girl == JubesX:
                                ch_v "I guess."
                        call change_Girl_stat(Girl, "obedience", 200, 5)
                    "You get back to it."
                    $ Girl.blushing = "_blush1"
                "Continue" if "spotted" in Girl.recent_history:
                    if Choice == "C":
                        call change_Girl_stat(Girl, "obedience", 200, 4)
                "Ok, let's stop.":
                    if Choice == "A":
                        $ Girl.change_face("sad")
                        if Girl == KittyX:
                            ch_k "Booo."
                        elif Girl == LauraX:
                            ch_l "Sissy."
                        elif Girl == StormX:
                            ch_s "Oh, if you insist. . ."
                        else:
                            Girl.voice "Spoilsport."
                    elif Choice == "B":
                        $ Girl.change_face("sad")
                        if Girl == RogueX:
                            ch_r "Yeah, probably."
                        elif Girl == KittyX:
                            ch_k "Um, yeah."
                        elif Girl == EmmaX:
                            ch_e "I suppose."
                        elif Girl == LauraX:
                            ch_l "Probably a good call."
                        elif Girl == JeanX:
                            call change_Girl_stat(Girl, "love", 80, 3)
                            call change_Girl_stat(Girl, "obedience", 80, 3)
                            ch_j "Yeah. . . wouldn't want to cause a riot."
                        elif Girl == StormX:
                            ch_s "I suppose it's for the best. . ."
                        elif Girl == JubesX:
                            ch_v "Yeah, I guess so. . ."
                    elif Choice == "C":
                        call change_Girl_stat(Girl, "love", 90, 5)
                        $ Girl.change_face("smile")
                        if Girl == RogueX:
                            ch_r "Heh, thanks [Girl.player_petname]"
                        elif Girl == KittyX:
                            ch_k "Heh, thanks [Girl.player_petname]."
                            call change_Girl_stat(Girl, "love", 90, 5)
                        elif Girl == EmmaX:
                            ch_e "That probably would be for the best. . ."
                        elif Girl == LauraX:
                            ch_l "Yeah, thanks."
                            call change_Girl_stat(Girl, "love", 90, 5)
                        elif Girl == JeanX:
                            call change_Girl_stat(Girl, "love", 80, 3)
                            call change_Girl_stat(Girl, "obedience", 80, 3)
                            ch_j "Yeah. . ."
                        elif Girl == StormX:
                            ch_s "Yes, that makes sense. . ."
                        elif Girl == JubesX:
                            ch_v "Heh, thanks."
                    "You both run back to your rooms."
                    $ Choice = "stop"

        if Choice == "stop":
            $ Girl.recent_history.append("caught")
            $ Girl.daily_history.append("caught")
            show black_screen onlayer black
            call show_full_body(Girl)
            call remove_Girl(Girl)
            $ Girl.change_outfit()
            hide black_screen onlayer black
            $ Player.location = "bg_player"
            jump player_room
    elif "exhibitionist" not in Girl.traits:
        $ Girl.change_face("sly")
        if Girl == JeanX and "nowhammy" not in JeanX.traits:

            pass
        else:
            $ Girl.traits.append("exhibitionist")
            "[Girl.name] seems to have become something of an exhibitionist."
    elif D20 > 15:
        $ Girl.change_face("sexy")
        "The crowd cheers."

    $ Girl.recent_history.append("spotted") if counter < 4 else Girl.recent_history
    $ Girl.daily_history.append("spotted")  if "spotted" not in Girl.daily_history else Girl.daily_history
    return

label Girls_Noticed(Girl, Other, Silent=0):
    if "threesome" in Other.recent_history:
        return
    if Partner == Other and "noticed " + Girl.tag in Other.recent_history:
        return

    if not Silent:
        if Partner != Other:

            $ Other.change_face("surprised", 1)
            "[Other.name] noticed what you and [Girl.name] are up to."
        else:

            $ Other.change_face("sly", 1)
            if Other == KittyX:
                "[Other.name] is glancing at you and [Girl.name] carefully. . ."
            elif Other == EmmaX:
                "[Other.name] is carefully appraising you and [Girl.name]. . ."
            else:
                "[Other.name] is staring at you and [Girl.name]. . ."

    if "cockout" in Player.recent_history:

        call Seen_First_Peen (Other, Girl)

    $ Girl.recent_history.append("noticed " + Other.tag)
    $ Other.recent_history.append("noticed " + Girl.tag)
    if Other == EmmaX and ("threesome" not in EmmaX.history or "classcaught" not in EmmaX.history):

        $ Other.add_word(1, 0, 0,"saw with " + Girl.tag)
        if Player.location == EmmaX.home:

            ch_e "If the two of you cannot keep your hands off each other, please do so elsewhere. . ."
            "She shoves the two of you out of her room and slams the door."
            $ Girl.location = "bg_player"
            jump player_room
        call remove_Girl(EmmaX)
        if not Silent:
            "She seems uncomfortable with the situation and leaves the room."
            "Perhaps you should ask her about it later."
        return

    if "poly " + Girl.tag in Other.traits or (Girl in Player.Harem and Other in Player.Harem):

        $ B = (1000-(20*taboo))
    else:

        $ B = (Other.likes[Girl.tag] - 500)
        if Other in Player.Harem:

            $ B -= 200

    call add_Girls(Other, x_position = stage_far_right)

    if Partner == Other:

        $ Silent = 1
    $ Partner = Other
    $ line = 0
    if approval_check(Other, 2000, taboo_modifier=2, Bonus = B) or approval_check(Other, 950, "L", taboo_modifier=2, Bonus = (B/3)):

        $ Other.change_face("sexy", 1)
        if not Silent:
            "She decides to join you."
        call change_Girl_stat(Other, "obedience", 90, 5)
        call change_Girl_stat(Other, "inhibition", 90, 5)
        call change_Girl_stat(Other, "lust", 90, 3)
        $ Other.add_word(1, 0, 0,"poly " + Girl.tag)
        call Threeway_Set (Other, Mode="start", GirlB=Girl)
    elif approval_check(Other, 650, "O", taboo_modifier=2) and approval_check(Other, 450, "L", taboo_modifier=1) or approval_check(Other, 800, "O", taboo_modifier=2, Bonus = (B/3)):

        $ Other.change_face("sexy")
        if not Silent:
            "She sits down patiently off to the side and watches."
        call change_Girl_stat(Other, "love", 90, 5)
        call change_Girl_stat(Other, "inhibition", 90, 5)
        call change_Girl_stat(Other, "lust", 90, 2)
        $ Other.add_word(1, 0, 0,"poly " + Girl.tag)
        call Threeway_Set (Other, "watch", Mode="start", GirlB=Girl)
    elif approval_check(Other, 650, "I", taboo_modifier=2) and approval_check(Other, 450, "L", taboo_modifier=1) or approval_check(Other, 800, "I", taboo_modifier=2, Bonus = (B/3)):

        $ Other.change_face("sexy")
        if not Silent:
            "She sits down and watches you with a hungry look."
        call change_Girl_stat(Other, "love", 90, 5)
        call change_Girl_stat(Other, "obedience", 90, 2)
        call change_Girl_stat(Other, "inhibition", 90, 2)
        call change_Girl_stat(Other, "lust", 90, 5)
        $ Other.add_word(1, 0, 0,"poly " + Girl.tag)
        call Threeway_Set (Other, "watch", Mode="start", GirlB=Girl)
    elif approval_check(Other, 1500, taboo_modifier=2, Bonus = B):
        $ Other.change_face("perplexed", 1)
        if not Silent:
            "She looks a little confused at what's happening, but she stays put and watches."
        if Other.love >= Other.obedience and Other.love >= Other.inhibition:
            call change_Girl_stat(Other, "obedience", 90, 2)
            call change_Girl_stat(Other, "inhibition", 90, 2)
        elif Other.obedience >= Other.inhibition:
            call change_Girl_stat(Other, "love", 90, 2)
            call change_Girl_stat(Other, "inhibition", 90, 2)
        else:
            call change_Girl_stat(Other, "love", 90, 2)
            call change_Girl_stat(Other, "obedience", 90, 1)
            call change_Girl_stat(Other, "inhibition", 90, 1)
        call change_Girl_stat(Other, "lust", 90, 5)
        call Threeway_Set (Other, "watch", Mode="start", GirlB=Girl)
    elif approval_check(Other, 650, "L", taboo_modifier=1) or approval_check(Other, 400, "O", taboo_modifier=2):

        $ Other.change_face("angry", 2)
        if Player.location == Other.home:
            if Other in (LauraX,JeanX):
                "She looks annoyed, and kicks you both out of the room."
            else:
                "She looks betrayed, and kicks you both out of the room."
        else:
            if Other in (LauraX,JeanX):
                "She looks annoyed, and storms out of the room."
            else:
                "She looks betrayed, and storms out of the room."
        call change_Girl_stat(Other, "love", 200, -5)
        call change_Girl_stat(Other, "love", 80, -5)
        call change_Girl_stat(Other, "love", 70, -5)
        call change_Girl_stat(Other, "obedience", 90, -5)
        call change_Girl_stat(Other, "lust", 89, 10)
        $ Partner = 0
        $ Other.add_word(1, 0, 0,"saw with " + Girl.tag)
        if Player.location == Other.home:
            $ Other.recent_history.append("angry")
            call are_girls_angry
        call remove_Girl(Other)
    else:

        $ Other.change_face("surprised", 2)
        call change_Girl_stat(Other, "inhibition", 90, 2)
        call change_Girl_stat(Other, "lust", 40, 20)
        if Player.primary_action != "kiss":
            call change_Girl_stat(Other, "love", 90, -10)
            call change_Girl_stat(Other, "obedience", 90, -5)
            call change_Girl_stat(Other, "lust", 80, 10)
        if Player.location == Other.home:
            call change_Girl_stat(Other, "love", 90, -5)
            call change_Girl_stat(Other, "obedience", 90, -5)
            if Other in (LauraX,JeanX):
                "She looks uncomfortable with this, and shoves you both out of the room."
            else:
                "She looks embarrassed, and shoves you both out of the room."
        elif Player.primary_action != "kiss":
            if Other in (LauraX,JeanX):
                "She looks uncomfortable with this, and stalks out of the room."
            else:
                "She looks embarrassed, and bolts from the room."
        else:
            "She looks a bit disgusted and walks away."
        $ Partner = 0
        if Player.location == Other.home:
            $ Other.recent_history.append("angry")
            call are_girls_angry
        call remove_Girl(Other)
    if AloneCheck(Girl) and Girl.taboo == 20:

        $ Girl.taboo = 0
        $ taboo = 0
    if line:

        "[line]."
        $ line = 0
    return

label sex_over(put_clothes_on = True):
    call stop_all_actions

    $ temp_Girls = Present[:]
    $ renpy.random.shuffle(temp_Girls)

    while temp_Girls:
        $ temp_Girls[0].session_orgasms = 0

        call Girl_Cleanup(temp_Girls[0], "after")

        if Player.spunk:
            if temp_Girls[0] == RogueX:
                ch_r "Let me take care of that for you. . ."
            elif temp_Girls[0] == KittyX:
                ch_k "You've got a little something. . ."
                ch_k "just let me get that."
            elif temp_Girls[0] == EmmaX:
                ch_e "[EmmaX.player_petname], let's get you presentable. . ."
            elif temp_Girls[0] == LauraX:
                ch_l "[LauraX.player_petname], you've got a little something. . ."
            elif temp_Girls[0] == JeanX:
                ch_j "[JeanX.player_petname], you might want to clean up. . ."
            elif temp_Girls[0] == StormX:
                ch_s "Allow me to take care of that, [StormX.player_petname]. . ."
            elif temp_Girls[0] == JubesX:
                ch_v "Oh, I can clean that up for you, [JubesX.player_petname]. . ."

            call Girl_Cleanup(temp_Girls[0])

        if "nowhammy" not in JeanX.traits and "saw with Jean" in temp_Girls[0].traits:
            $ temp_Girls[0].traits.remove("saw with Jean")
            $ temp_Girls[0].traits.append("sawJeanW")

        $ temp_Girls.remove(temp_Girls[0])

    $ temp_Girls = Present[:]
    $ renpy.random.shuffle(temp_Girls)

    while temp_Girls:
        call show_full_body(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    if put_clothes_on:
        python:
            line = None

            Girls = 0

            for G in Present:
                if G.change_outfit() == 2:
                    if line:
                        line = line + " and " + G.name
                    else:
                        line = G.name

                    Girls += 1

        if Girls > 1:
            "[line] throw their clothes back on."
        elif Girls:
            "[line] throws her clothes back on."

        call get_dressed

    call checkout
    call reset_player

    return

label Girl_TightsRipped(Girl=0, Count=0):
    if Girl not in all_Girls:
        return

    if Girl.Wardrobe.current_Outfit.Clothes["hose"] == "tights":
        $ Count = 1
        $ Girl.Wardrobe.current_Outfit.Clothes["hose"] = "ripped_tights"
        $ Girl.change_face("angry")
    elif Girl.Wardrobe.current_Outfit.Clothes["hose"] == "pantyhose":
        $ Count = 1
        $ Girl.Wardrobe.current_Outfit.Clothes["hose"] = "ripped_pantyhose"
        $ Girl.change_face("angry")
    else:

        return

    if "ripped_tights" in Girl.inventory or "ripped_pantyhose" in Girl.inventory:

        if Girl == RogueX:
            ch_r "Damnation, that's another pair ruined!"
            ch_r "Tsk, another pair ruined!"
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
            ch_r "Well that's a good pair of tights down the chute."
        elif Girl == KittyX:
            ch_k "Ouch, I guess I missed a dodge. . ."
        elif Girl == EmmaX:
            ch_e "Well that's unfortunate. . ."
        elif Girl == LauraX:
            ch_l "What?"
            ch_l ". . ."
            $ Girl.eyes = "down"
            ch_l "Oh, they got torn."
            $ Girl.eyes = "normal"
        elif Girl == JeanX:
            ch_j "Ugh, new ones will be a pain to find."
        elif Girl == StormX:
            ch_s "It appears these are not fit for combat."

    if Count:

        if not Girl.Wardrobe.current_Outfit.Clothes["bottom"] and Girl.Wardrobe.current_Outfit.Clothes["underwear"] != "shorts":
            if Girl == StormX and StormX in Rules:

                pass
            elif Girl.Wardrobe.current_Outfit.Clothes["underwear"]:
                if Girl.seen_underwear:
                    $ Count = 3 if not approval_check(Girl, 600) else Count
                else:
                    $ Girl.seen_underwear = 1
                    $ Count = 3 if not approval_check(Girl, 900) else Count
                call change_Girl_stat(Girl, "lust", 60, 2)
            else:
                if Girl.seen_pussy:
                    $ Count = 3 if not approval_check(Girl, 900) else Count
                else:
                    call Rogue_First_Bottomless
                    $ Count = 3 if not approval_check(Girl, 1400) else Count

        if Count != 3:
            $ Girl.add_word(1,"ripped", "ripped")

        if Count == 2:

            menu:
                extend ""
                "I think those look really good on you.":
                    $ Girl.change_face("smile", 1)
                    $ Girl.inventory.append(Girl.Wardrobe.current_Outfit.Clothes["hose"])
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

                    $ Girl.change_face("bemused")
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


        elif Count == 3:
            $ Girl.change_face("startled", 2)
            if Girl == RogueX:
                ch_r "I, um, I should get out of here."
            elif Girl == KittyX:
                ch_k "This is. . . a bit breazy for me. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("sexy", 1)
                ch_e "This might cause a bit of a stir, I should probably change. . ."
            elif Girl == LauraX:
                $ Girl.change_face("perplexed", 0)
                ch_l "I guess I should change into something else."
            elif Girl == JeanX:
                ch_j "I'm going to get changed though. . ."
            elif Girl == StormX:
                $ Girl.change_face("bemused", 0)
                ch_s "I really probably should change."
            $ Girl.blushing = "_blush1"
            call remove_Girl(Girl)
            $ Girl.change_outfit()

    return
