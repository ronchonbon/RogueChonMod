init python:

    def get_last_name(character):
        split_name = character.name.split()

        return split_name[character.name.count(" ")]

label wait(outfit = True, lights = True):
    $ stack_depth = renpy.call_stack_depth()

    show black_screen onlayer black

    call checkout(total = True)

    $ Player.XP = 3330 if Player.XP > 3330 else Player.XP

    if time_index < 3:
        $ time_index += 1
    else:
        $ del Party[:]

        $ time_index = 0
        $ day += 1

        if weekday < 6:
            $ weekday += 1
        else:
            $ weekday = 0

        $ day_of_week = week[weekday]

        if being_punished:
            $ Player.cash += int(Player.income / 2)

            if being_punished == 1:
                "Your punishment from Xavier has expired."

            $ being_punished -= 1
        else:
            $ Player.cash += Player.income

        $ Player.semen = Player.max_semen
        $ Player.spunk = 0
        $ Player.reputation = 0 if Player.reputation < 0 else Player.reputation
        $ Player.reputation += 10 if Player.reputation < 800 else 0
        $ Player.reputation = 1000 if Player.reputation > 1000 else Player.reputation

        $ total_SEXP = 0

        if "mandrill" in Player.traits:
            $ Player.traits.remove("mandrill")
        if "purple" in Player.traits:
            $ Player.traits.remove("purple")
        if "corruption" in Player.traits:
            $ Player.traits.remove("corruption")

        call check_favorite_actions

        if "halloween" in Player.daily_history:
            if RogueX.outfit["hair"] == "_cosplay":
                if "_evo" in RogueX.daily_history:
                    $ RogueX.outfit["hair"] = "_evo"
                elif "_wet" in RogueX.daily_history:
                    $ RogueX.outfit["hair"] = "_wet"

            if JeanX.outfit["hair"] == "_pony":
                if "_short" in JeanX.daily_history:
                    $ JeanX.outfit["hair"] = "_short"
                elif "_wet" in JeanX.daily_history:
                    $ JeanX.outfit["hair"] = "_wet"

            if EmmaX.outfit["hair"] == "_hat":
                $ EmmaX.outfit["hair"] = "_wavy"
            elif EmmaX.outfit["hair"] == "_wet_hat":
                $ EmmaX.outfit["hair"] = "_wet"

            if StormX.outfit["hair"] == "_short":
                if "_long" in StormX.daily_history:
                    $ StormX.outfit["hair"] = "_long"
                elif "_mohawk" in StormX.daily_history:
                    $ StormX.outfit["hair"] = "_mohawk"
                elif "_wet" in StormX.daily_history:
                    $ StormX.outfit["hair"] = "_wet"
                elif "_wet_mohawk" in StormX.daily_history:
                    $ StormX.outfit["hair"] = "_wet_mohawk"

        call reset_all_girls_at_end

    $ Player.semen += 1
    $ Player.focus -= 5 if Player.focus >= 10 else 0

    $ multi_action = True

    $ current_time = time_options[(time_index)]

    $ round = 100

    $ del Player.recent_history[:]

    if time_index == 0:
        $ del Player.daily_history[:]

    call taboo_level(taboo_location = False)
    call who_likes_who

    if time_index == 3:
        call offscreen_studying

    call reset_all_girls_at_beginning
    call change_into_scheduled_outfit

    if outfit:
        python:
            for G in all_Girls:
                G.change_outfit(G.today_outfit_name)

    if Player.level < 10 and Player.XP >= Player.XP_goal:
        $ Player.XP_goal = int((1.15*Player.XP_goal) + 100)
        $ Player.level += 1
        $ Player.stat_points += 1

        if Player.level <5:
            $ Count = 1
        elif Player.level <9:
            $ Count = 2
        else:
            $ Count = 3

        $ Player.income += Count

        "You've leveled up!"
        "Xavier has noticed your achievements and raised your stipend by $[Count] per day. It is now $[Player.income]."

        if Player.level == 10:
            "You've reached max level!"

    call lesbian_check
    call checkout

    if time_index < 3:
        hide night_mask onlayer nightmask

    if lights:
        hide black_screen onlayer black

    return

label checkout(total = False):
    python:
        for G in all_Girls:
            G.love = 1000 if G.love > 1000 else G.love
            G.obedience = 1000 if G.obedience > 1000 else G.obedience
            G.inhibition = 1000 if G.inhibition > 1000 else G.inhibition
            G.lust = 99 if G.lust > 99 else G.lust

            G.love = 0 if G.love < 0 else G.love
            G.obedience = 0 if G.obedience < 0 else G.obedience
            G.inhibition = 0 if G.inhibition < 0 else G.inhibition
            G.lust = 0 if G.lust < 0 else G.lust

            G.remaining_actions = G.max_actions if G.remaining_actions > G.max_actions else G.remaining_actions
            G.remaining_actions = 0 if G.remaining_actions < 0 else G.remaining_actions

            G.addiction = 100 if G.addiction > 100 else G.addiction
            G.addiction = 0 if G.addiction < 0 else G.addiction
            G.addiction_rate = 10 if G.addiction_rate > 10 else G.addiction_rate
            G.addiction_rate = 0 if G.addiction_rate < 0 else G.addiction_rate
            G.thirst = 100 if G.thirst > 100 else G.thirst
            G.thirst = 0 if G.thirst < 0 else G.thirst

            if G.forced and G.event_counter["forced"] < 10:
                G.event_counter["forced"] += 1

            if G == LauraX:
                G.scent_timer = 0

    $ Player.focus = 99 if Player.focus > 99 else Player.focus
    $ Player.focus = 0 if Player.focus < 0 else Player.focus
    $ Player.semen = Player.max_semen if Player.semen > Player.max_semen else Player.semen
    $ Player.semen = 0 if Player.semen < 0 else Player.semen

    if total:
        $ Player.drain_word("cockout")
        $ Player.drain_word("nude")

        $ multi_action = True

        call stop_all_actions

        $ position_timer = 100

        $ Partner = None

        $ Player.focusing = False

    return

label reset_all_girls_at_end:
    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        if temp_Girls[0] in active_Girls and temp_Girls[0].location != bg_current:
            $ temp_Girls[0].location = temp_Girls[0].home

        if temp_Girls[0].to_do:
            call to_do(temp_Girls[0])

        $ temp_Girls[0].outfit_name = "sleepwear"
        $ temp_Girls[0].change_outfit("sleepwear")

        $ temp_Girls[0].addiction += temp_Girls[0].addiction_rate
        $ temp_Girls[0].addiction -= (3*temp_Girls[0].resistance)

        if "nonaddictive" in Player.traits:
            $ temp_Girls[0].addiction_rate -= 2
            $ temp_Girls[0].addiction -= 5
        elif "addictive" not in Player.traits:
            $ temp_Girls[0].addiction_rate -= temp_Girls[0].resistance

            if temp_Girls[0] != RogueX and temp_Girls[0].addiction_rate >= 3:
                $ temp_Girls[0].addiction_rate -= temp_Girls[0].resistance

        $ temp_Girls[0].event_counter["forced"] -= 1 if temp_Girls[0].event_counter["forced"] > 0 else 0

        if temp_Girls[0].event_counter["forced"] > 0:
            $ temp_Girls[0].event_counter["forced"] -= 1 if approval_check(temp_Girls[0], 1000, "LO") else 0

        $ temp_Girls[0].remaining_actions = temp_Girls[0].max_actions
        $ temp_Girls[0].reputation = 0 if temp_Girls[0].reputation < 0 else temp_Girls[0].reputation
        $ temp_Girls[0].reputation += 10 if temp_Girls[0].reputation < 800 else 0
        $ temp_Girls[0].reputation = 1000 if temp_Girls[0].reputation > 1000 else temp_Girls[0].reputation
        $ temp_Girls[0].lust -= 5 if temp_Girls[0].lust >= 50 else 0

        $ total_SEXP += temp_Girls[0].SEXP

        if temp_Girls[0].SEXP >= 15:
            if temp_Girls[0].SEXP >= 50:
                $ temp_Girls[0].thirst += 8 if temp_Girls[0].thirst <= 70 else 4
            elif temp_Girls[0].SEXP >= 25:
                $ temp_Girls[0].thirst += 5 if temp_Girls[0].thirst <= 60 else 2
            else:
                $ temp_Girls[0].thirst += 3 if temp_Girls[0].thirst <= 50 else 1

            $ temp_Girls[0].thirst -= 5 if temp_Girls[0].broken_up[0] else 0
            $ temp_Girls[0].thirst += 1 if temp_Girls[0].lust >= 50 else 0

        if "will_masturbate" in temp_Girls[0].daily_history and temp_Girls[0].location != bg_current:
            $ temp_Girls[0].lust = 25
            $ temp_Girls[0].thirst -= int(temp_Girls[0].thirst/2) if temp_Girls[0].thirst >= 50 else int(temp_Girls[0].thirst/4)
        elif "wants_to_masturbate" in temp_Girls[0].daily_history:
            $ temp_Girls[0].thirst += 10 if temp_Girls[0].thirst <= 50 else 5

        $ temp_Girls[0].broken_up[0] -= 1 if temp_Girls[0].broken_up[0] > 0 else 0

        python:
            for key in temp_Girls[0].spunk.keys():
                temp_Girls[0].spunk[key] = False

        if "lover" in temp_Girls[0].player_petnames and temp_Girls[0].love > 800:
            $ temp_Girls[0].love += 10
        if "master" in temp_Girls[0].player_petnames and temp_Girls[0].obedience > 600:
            $ temp_Girls[0].obedience += 10
        if "fuck buddy" in temp_Girls[0].player_petnames:
            $ temp_Girls[0].inhibition += 10

        $ temp_Girls[0].slutty_clothes()

        if temp_Girls[0] == JeanX:
            if temp_Girls[0].love < 1000 and temp_Girls[0].stored_stats > 0:
                if temp_Girls[0].obedience >= 900:
                    $ temp_Girls[0].love += 10
                    $ temp_Girls[0].stored_stats -= 10
                elif temp_Girls[0].obedience >= 700:
                    $ temp_Girls[0].love += 5
                    $ temp_Girls[0].stored_stats -= 5
                elif temp_Girls[0].obedience >= 500:
                    $ temp_Girls[0].love += 1
                    $ temp_Girls[0].stored_stats -= 1
            if temp_Girls[0].reputation <= 800 and "nowhammy" not in JeanX.traits:
                $ temp_Girls[0].reputation = 800

        $ temp_Girls.remove(temp_Girls[0])

    return

label taboo_level(taboo_location = True):
    $ teacher = 0

    if EmmaX.location == "bg_teacher":
        $ EmmaX.location = "bg_classroom"

        $ teacher = 1
    elif StormX.location == "bg_teacher":
        $ StormX.location = "bg_classroom"

        $ teacher = 2

    call taboo_check(Player, location = bg_current)

    $ temp_Girls = all_Girls[:]

    if "nowhammy" not in JeanX.traits:
        $ JeanX.taboo = 0

        $ temp_Girls.remove(JeanX)

    while temp_Girls:
        if temp_Girls[0] in Party:
            $ temp_Girls[0].location = bg_current

        if temp_Girls[0].location == "nearby":
            $ location = bg_current
        else:
            $ location = temp_Girls[0].location

        if not taboo_location or location == bg_current:
            call taboo_check(temp_Girls[0], location)

        $ temp_Girls.remove(temp_Girls[0])

    if teacher == 2:
        $ StormX.location = "bg_teacher"
    elif teacher:
        $ EmmaX.location = "bg_teacher"

    return

label offscreen_studying(Studiers = []):
    python:
        for G in all_Girls:
            if G.location != bg_current and G.location in personal_rooms:
                Studiers.append(G)

    if len(Studiers) < 2:
        return

    $ renpy.random.shuffle(Studiers)

    $ Studiers[0].check_if_likes(Studiers[1],800,5,1)
    $ Studiers[1].check_if_likes(Studiers[0],800,5,1)

    $ Studiers[0].XP += 5
    $ Studiers[1].XP += 5

    return

label reset_all_girls_at_beginning:
    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        $ temp_Girls[0].remaining_actions += 1 if time_index != 0 else 0
        $ temp_Girls[0].session_orgasms = 0

        if temp_Girls[0].lust >= 70 or temp_Girls[0].thirst >= 30 or (renpy.random.randint(1, 40) + temp_Girls[0].lust)>= 70:
            if "no_masturbating" in temp_Girls[0].traits:
                $ temp_Girls[0].add_word(1,0,"wants_to_masturbate",0,0)
            else:
                $ temp_Girls[0].add_word(1,0,"will_masturbate",0,0)

        if "lesbian" in temp_Girls[0].recent_history:
            $ temp_Girls[0].thirst -= int(temp_Girls[0].thirst/2)
            $ temp_Girls[0].lust = 20

        $ temp_Girls[0].had_chat[5] = 0
        $ temp_Girls[0].event_happened[3] -= 1 if temp_Girls[0].event_happened[3] else 0
        $ temp_Girls[0].forced = False

        if temp_Girls[0].location == "bg_classroom" or temp_Girls[0].location == "bg_dangerroom" or temp_Girls[0].location == "bg_teacher":
            $ temp_Girls[0].XP += 10
        elif (bg_current == "bg_classroom" or bg_current == "bg_dangerroom") and temp_Girls[0].location == "nearby":
            $ temp_Girls[0].XP += 10
        elif temp_Girls[0].location == "bg_showerroom":
            call remove_girl(temp_Girls[0])

        $ temp_Girls[0].blushing = ""
        $ temp_Girls[0].wet = False
        $ temp_Girls[0].outfit["held_item"] = None

        $ temp_Girls[0].addiction += temp_Girls[0].addiction_rate
        $ temp_Girls[0].addiction_rate -= temp_Girls[0].resistance if temp_Girls[0].addiction_rate > 3 else 0

        if temp_Girls[0].taboo and temp_Girls[0].outfit["shame"] and temp_Girls[0] in active_Girls:
            if temp_Girls[0].location == "bg_dangerroom":
                $ temp_Girls[0].outfit["shame"] -= 10 if temp_Girls[0].outfit["shame"] >= 10 else temp_Girls[0].outfit["shame"]

            $ Count = int((temp_Girls[0].taboo*temp_Girls[0].outfit["shame"])/200)

            $ temp_Girls[0].change_stat("obedience", 90, Count)
            $ temp_Girls[0].change_stat("inhibition", 90, Count)
            $ temp_Girls[0].reputation -= Count

        $ temp_Girls[0].love -= 5*temp_Girls[0].recent_history.count("unsatisfied")

        $ del temp_Girls[0].recent_history[:]

        if "_angry" in temp_Girls[0].daily_history:
            $ temp_Girls[0].recent_history.append("_angry")

        if time_index == 0:
            $ del temp_Girls[0].daily_history[:]
        elif time_index == 3 and "going_on_date" in temp_Girls[0].daily_history and "stoodup" not in temp_Girls[0].traits:
            $ Player.drain_word("going_on_date",0,1)

            $ temp_Girls[0].traits.append("stoodup")

        if temp_Girls[0].outfit["buttplug"]:
            $ bonus = 1
        else:
            $ bonus = 0

        if temp_Girls[0].used_to_anal < 2:
            if (temp_Girls[0].action_counter["anal"] + temp_Girls[0].action_counter["dildo_ass"] + bonus) >= 15:
                $ temp_Girls[0].used_to_anal = 2
            elif (temp_Girls[0].action_counter["anal"] + temp_Girls[0].action_counter["dildo_ass"] + bonus) >= 3:
                $ temp_Girls[0].used_to_anal = 1

        $ temp_Girls[0].XP = 3330 if temp_Girls[0].XP > 3330 else temp_Girls[0].XP

        if temp_Girls[0].XP >= temp_Girls[0].XP_goal and temp_Girls[0].level < 10:
            $ temp_Girls[0].XP_goal = int((1.15*temp_Girls[0].XP_goal) + 100)
            $ temp_Girls[0].level += 1
            $ temp_Girls[0].stat_points += 1

            "[temp_Girls[0].name]'s leveled up! I bet she has some new tricks to learn."

            if temp_Girls[0].level == 10:
                "[temp_Girls[0].name]'s reached max level!"

        if temp_Girls[0] == LauraX:
            $ temp_Girls[0].addiction_rate -= (2*temp_Girls[0].resistance) if temp_Girls[0].addiction_rate > 5 else 0
        elif temp_Girls[0] == JubesX and "met" in JubesX.history:
            $ temp_Girls[0].addiction_rate = 2 if temp_Girls[0].addiction_rate < 2 else temp_Girls[0].addiction_rate

            if "sunshine" not in JubesX.history:
                $ temp_Girls[0].addiction = 40 if temp_Girls[0].addiction > 40 else temp_Girls[0].addiction

        $ temp_Girls[0].default_faces()
        $ temp_Girls[0].change_face(5)

        $ temp_Girls.remove(temp_Girls[0])

    return

label change_into_scheduled_outfit(Girls = [], clothes = 1, location = 1):
    if not Girls:
        $ Girls = active_Girls[:]

    while Girls:
        if Girls[0] in Party and clothes != 2 or not location:
            pass
        elif clothes != 2 and "sleepover" in Girls[0].traits and time_index == 0:
            pass
        else:
            if (time_index == 0 and clothes and round >= 90) or clothes == 2:
                $ Girls[0].today_outfit_name = 0

                if Girls[0].broken_up[0]:
                    pass
                elif Girls[0].clothing[weekday] == 1:
                    $ Girls[0].today_outfit_name = "casual1"
                elif Girls[0].clothing[weekday] == 2:
                    $ Girls[0].today_outfit_name = "casual2"
                elif Girls[0].clothing[weekday] == 4:
                    $ Girls[0].today_outfit_name = "gym_clothes"
                elif Girls[0].clothing[weekday] == 3 and Girls[0].first_custom_outfit["outfit_active"]:
                    $ Girls[0].today_outfit_name = "custom1"
                elif Girls[0].clothing[weekday] == 5 and Girls[0].second_custom_outfit["outfit_active"]:
                    $ Girls[0].today_outfit_name = "custom2"
                elif Girls[0].clothing[weekday] == 6 and Girls[0].third_custom_outfit["outfit_active"]:
                    $ Girls[0].today_outfit_name = "custom3"

                if not Girls[0].today_outfit_name:
                    $ outfit_options = ["casual1", "casual2"]

                    if not Girls[0].broken_up[0]:
                        $ outfit_options.append("custom1") if Girls[0].first_custom_outfit["outfit_active"] == 2 else outfit_options
                        $ outfit_options.append("custom2") if Girls[0].second_custom_outfit["outfit_active"] == 2 else outfit_options
                        $ outfit_options.append("custom3") if Girls[0].third_custom_outfit["outfit_active"] == 2 else outfit_options

                    $ Girls[0].today_outfit_name = renpy.random.choice(outfit_options)

                $ Girls[0].outfit_name = Girls[0].today_outfit_name

            $ temp_location = Girls[0].location

            if Girls[0] not in active_Girls:
                $ temp_location = "hold"

                $ Girls[0].location = "hold"
            elif Girls[0] in Party or Girls[0].location == "hold":
                pass
            else:
                $ Girls[0].location = Girls[0].weekly_schedule[weekday][time_index]

                if Girls[0] == JubesX and JubesX.addiction > 60:
                    $ JubesX.location = JubesX.home

            if Girls[0].location != temp_location and Girls[0] not in Party:
                if temp_location == bg_current:
                    if approval_check(Girls[0], 1200) and Girls[0].location not in ["bg_classroom","bg_teacher","bg_dangerroom"]:
                        $ Girls[0].location = temp_location
                    else:
                        $ Girls[0].recent_history.append("leaving")
                elif Girls[0].location == bg_current:
                    $ Girls[0].recent_history.append("arriving")

            if Girls[0] in Nearby:
                $ Nearby.remove(Girls[0])

        if Girls[0].location == "bg_teacher":
            call alternate_clothes(Girls[0], 8)

            $ Girls[0].change_outfit()

        $ Girls.remove(Girls[0])

    return

label lesbian_check(Girls = []):
    if "threesome" not in EmmaX.history:
        if EmmaX.thirst >= 30 and approval_check(EmmaX, 800, "I"):
            $ EmmaX.history.append("threesome")

    python:
        for G in active_Girls:
            if G == RogueX and "touch" not in RogueX.traits:
                pass
            elif G == EmmaX and "threesome" not in EmmaX.history:
                pass
            elif approval_check(G, 500, "I", Alt = [[EmmaX, JeanX], 300]) and G.thirst >= 30:
                if ("monogamous" not in G.traits or G.broken_up[0]) and G not in Party:
                    Girls.append(G)

                    if G.thirst >= 60:
                        Girls.append(G)

                if G.thirst >= 90:
                    Girls.append(G)

    if not Girls:
        return

    if Girls[0] != JeanX:
        $ renpy.random.shuffle(Girls)

    $ Partner = None

    while len(Girls) >= 2:
        if Partner:
            $ Girls.remove(Girls[1])
        elif Girls[1] == Girls[0] or Girls[1].location == bg_current or Girls[1] in Party:
            $ Girls.remove(Girls[1])
        elif Girls[0] == JeanX and Girls[1].likes[Girls[0].tag] >= 500:
            $ Partner = Girls[1]
        elif (Girls[1] in Player.Harem and Girls[0] in Player.Harem) and Girls[0].likes[Girls[1].tag] >= 600:
            $ Partner = Girls[1]
        elif Girls[1].likes[Girls[0].tag] >= 800 and Girls[0].likes[Girls[1].tag] >= 800:
            $ Partner = Girls[1]
        elif Girls[1].thirst >= 90 and Girls[0]..likes[Girls[1].tag] >= 600:
            $ Partner = Girls[1]
        else:
            $ Girls.remove(Girls[1])

    if not Partner:
        return

    $ Girls.append(Partner)

    $ Partner = None

    if bg_current != Girls[0].home:
        $ Girls[0].location = Girls[0].home
        $ Girls[1].location = Girls[0].home
    elif bg_current != Girls[1].home:
        $ Girls[0].location = Girls[1].home
        $ Girls[1].location = Girls[1].home

    python:
        for GA in Girls:
            GA.add_word(1, "lesbian", 0, 0, 0)

            for GB in Girls:
                if GA == GB:
                    continue
                else:
                    GA.check_if_likes(GB, 700, 15, 1)
                    GA.check_if_likes(GB, 900, 10, 1)
                    GA.check_if_likes(GB, 1000, 5, 1)

            GA.drain_word("arriving", 1, 0)
            GA.change_stat("lust", 60, 20)
            GA.thirst -= 5

    return

label to_do(Girl):
    if Girl == LauraX:
        if "pubes" in Girl.to_do:
            $ Girl.pubes = "_hairy"
            $ Girl.to_do.remove("pubes")

        if "mission" in Girl.to_do:
            $ Girl.pubes_counter -= 1

            if Girl.pubes_counter >= 1:
                $ Girl.location = "hold"
            else:
                $ Girl.history.append("dress0")
                $ Girl.to_do.remove("mission")

        if "cleanhouse" in Girl.to_do:
            if LauraX in Player.Harem or not Player.Harem:
                $ LauraX.event_happened[5] = 2
                $ Girl.to_do.remove("cleanhouse")

            $ LauraX.event_happened[5] -= 1 if LauraX.event_happened[5] > 1 else 0
    else:
        if "pubes" in Girl.to_do:
            $ Girl.pubes_counter -= 1

            if Girl.pubes_counter >= 1:
                pass
            else:
                $ Girl.pubes = "_hairy"
                $ Girl.to_do.remove("pubes")

    if "shave" in Girl.to_do:
        $ Girl.pubes = "_bare"
        $ Girl.to_do.remove("shave")

    if "hair" in Girl.to_do:
        if StormX.outfit["hair"] == "_long":
            $ StormX.outfit["hair"] = "_mohawk"
        elif StormX.outfit["hair"] == "_wet_mohawk":
            $ StormX.outfit["hair"] = "_wet"
        elif StormX.outfit["hair"] == "_wet":
            $ StormX.outfit["hair"] = "_wet_mohawk"
        else:
            $ StormX.outfit["hair"] = "_long"

        $ Girl.to_do.remove("hair")

    if "_ring" in Girl.to_do:
        $ Girl.outfit["piercings"] = "_ring"
        $ Girl.to_do.remove("_ring")

    if "_barbell" in Girl.to_do:
        $ Girl.outfit["piercings"] = "_barbell"
        $ Girl.to_do.remove("_barbell")

    return

label remove_girl(Girl, also_hide = True, hold = False):
    if Girl == "all":
        $ Party = []
        $ Nearby = []
        $ Partner = None
        $ Girls = all_Girls[:]
    else:
        while Girl in Party:
            $ Party.remove(Girl)
        while Girl in Present:
            $ Present.remove(Girl)
        while Girl in Nearby:
            $ Nearby.remove(Girl)
        if Partner == Girl:
            $ Partner = None

        $ Girls = [Girl]

    while Girls:
        $ Girls[0].drain_word("leaving", 1, 0, 0)
        $ Girls[0].drain_word("arriving", 1, 0, 0)

        if Girls[0].location == bg_current or (bg_current == "bg_classroom" and Girls[0].location == "bg_teacher"):
            if hold and bg_current in ("bg_campus","bg_classroom","bg_dangerroom","bg_pool"):
                if Girls[0] not in Nearby:
                    $ Nearby.append(Girls[0])

                $ Girls[0].location = "nearby"
            elif bg_current == Girls[0].home:
                if Girls[0] == JubesX and JubesX.addiction >= 60:
                    $ Girls[0].location = "bg_showerroom"

                $ Girls[0].location = "bg_campus"

                $ Player.drain_word("locked",0,0,1)
            else:
                $ Girls[0].location = Girls[0].home

                $ Player.drain_word("locked",0,0,1)

        if also_hide:
            call hide_girl(Girls[0])

        $ Girls.remove(Girls[0])

    return

label change_out_of_gym_clothes(Girls = []):
    $ Girls = all_Girls[:] if not Girls else Girls

    python:
        for G in Girls:
            if G not in Party:
                if G.outfit_name == "gym_clothes" and G.location != "bg_dangerroom":
                    G.outfit_name = G.today_outfit_name
                elif G.location == "bg_dangerroom":
                    G.outfit_name = "gym_clothes"

            G.change_outfit()

    return

label hide_girl(Girl):
    if Girl == RogueX:
        hide Rogue_sprite
    elif Girl == KittyX:
        hide Kitty_sprite
    elif Girl == EmmaX:
        hide Emma_sprite
    elif Girl == LauraX:
        hide Laura_sprite
    elif Girl == JeanX:
        hide Jean_sprite
    elif Girl == StormX:
        hide Storm_sprite
    elif Girl == JubesX:
        hide Jubes_sprite

    return

label event_calls(event_Girls=[]):
    call check_who_is_present

    $ D20 = renpy.random.randint(1, 20)
    call Get_Dressed

    if time_index == 2 and "going_on_date" in Player.daily_history:
        if bg_current == "bg_campus":
            call DateNight

            $ Player.drain_word("going_on_date",0,1)

            return
        else:
            menu:
                "You have a date to get to, head for the square?"
                "Yes":
                    jump campus_entry
                "No":
                    "Suit yourself. . ."

    # if day < 3 or round <= 10:
    #     return
    if round <= 10:
        return

    if KittyX in active_Girls:
        if "Kate" not in KittyX.names and KittyX.inhibition >= 500 and KittyX.location == bg_current:
            call Kitty_Kate

            return
    else:
        if "traveling" in Player.recent_history and "met" not in KittyX.history and bg_current == "bg_classroom":
            jump meet_Kitty

            return

    if EmmaX in active_Girls:
        if bg_current == "bg_classroom" and time_index == 2 and weekday in (0,2,4):
            if "traveling" in Player.recent_history and not Party:
                if "classcaught" not in EmmaX.history:
                    jump Emma_Caught_Classroom

                    return
                elif D20 <= 10 and "will_masturbate" in EmmaX.daily_history:
                    jump Emma_Caught_Classroom

                    return

            if "detention" in Player.traits and not Party:
                jump Emma_Detention

            if round >= 70:
                $ EmmaX.location = "bg_classroom"

    if LauraX in active_Girls:
        pass
    elif "met" not in LauraX.history and "traveling" in Player.recent_history:
        if time_index < 3 and "met" in KittyX.history:
            if "dress0" in LauraX.history:
                call Laura_Dressup

                return

    if StormX in active_Girls:
        if bg_current == "bg_classroom" and StormX.location == "bg_teacher" and "Peter" in StormX.history and "traveling" in Player.recent_history:
            call Storm_Peter

            return

        if bg_current == "bg_classroom" and time_index == 2 and weekday in (1,3):
            if "_mohawk" not in StormX.history and "traveling" not in Player.recent_history and approval_check(StormX, 200, "I"):
                jump Storm_Hairtalk

                return
            if round >= 70:
                $ StormX.location = "bg_classroom"

        if time_index == 3 and bg_current == "bg_pool" and "poolnight" in Player.history:
            if "sex friend" not in StormX.player_petnames or (D20 < 5 and "poolnight" not in Player.recent_history):
                call Storm_Poolnight

                return

    if JubesX in active_Girls:
        if time_index < 3 and "sunshine" not in JubesX.history and "traveling" in Player.recent_history and bg_current in ("bg_classroom","bg_dangerroom","bg_campus","bg_pool"):
            jump Jubes_Sunshine

            return
        elif "mall" not in Player.history and "sunshine" in JubesX.history and time_index < 3 and JubesX.addiction < 50:
            call Jubes_Mall
            jump reset_location
        elif not JubesX.event_happened[1] and JubesX.addiction < 50:
            $ JubesX.addiction += 5

    if "goto" in Player.recent_history:
        $ Player.recent_history.remove("goto")

        return

    if "locked" in Player.traits:
        return

    if "micro" not in Player.history and day > 13:
        call Microtransactions_Intro

    if "fix" not in Player.daily_history:
        call check_addiction

    if bg_current == "bg_player":
        $ event_Girls = active_Girls[:]

        while event_Girls and "asked_to_meet" not in event_Girls[0].daily_history:
            if "asked_to_meet" in event_Girls[0].daily_history:
                $ event_Girls = ["x", event_Girls[0]]

            $ event_Girls.remove(event_Girls[0])

    if not event_Girls:
        call ShareCheck
        call CheatCheck
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

            if event_Girls[0].broken_up[0] or "_angry" in event_Girls[0].daily_history:
                pass
            elif not event_Girls[0].event_happened[0] and event_Girls[0].event_counter["sleepover"] >= 5:
                if event_Girls[0].location == bg_current or event_Girls[0] in Party:
                    call expression event_Girls[0].tag + "_Key"

                    return
            elif event_Girls[0] == JubesX:
                pass
            elif event_Girls[0] == JeanX:
                if bg_current != "bg_classroom":
                    if JeanX.obedience >= 500 and "sir" not in JeanX.history:
                        call Jean_Sub
                    elif JeanX.obedience >= 800 and "master" not in JeanX.history:
                        call Jean_Master
                    elif JeanX.love >= 500 and "sexfriend" not in JeanX.history:
                        call Jean_Like
                    elif JeanX.love >= 800 and JeanX.obedience >= 600 and not JeanX.event_happened[5]:
                        call Jean_Love
                    elif "daddy" not in JeanX.player_petnames and approval_check(JeanX, 750, "L"):
                        if (bg_current == event_Girls[0].home or bg_current == "bg_player") and event_Girls[0].location == bg_current:
                            call Jean_Daddy

                    return
            elif "boyfriend" not in event_Girls[0].player_petnames and event_Girls[0].love >= 800 and event_Girls[0].event_happened[5] != 20 and event_Girls[0].tag + "No" not in Player.traits:
                if event_Girls[0] == LauraX and LauraX.event_happened[5] == 3:
                    call Laura_Cleanhouse
                elif Player.Harem and event_Girls[0].tag + "Yes" not in Player.traits:
                    call Poly_Start (event_Girls[0])
                elif bg_current == event_Girls[0].home or bg_current == "bg_player":
                    call expression event_Girls[0].tag + "_BF"
                else:
                    call ask_to_meet (event_Girls[0], "_bemused")

                return
            elif "lover" not in event_Girls[0].player_petnames and event_Girls[0].love >= 950 and event_Girls[0].event_happened[6] < 15:
                if bg_current == event_Girls[0].home or bg_current == "bg_player":
                    call expression event_Girls[0].tag + "_Love"
                else:
                    call ask_to_meet (event_Girls[0], "_bemused")

                return
            elif "sir" not in event_Girls[0].history and "sir" not in event_Girls[0].player_petnames and event_Girls[0].obedience >= 500:
                if bg_current == event_Girls[0].home or bg_current == "bg_player":
                    call expression event_Girls[0].tag + "_Sub"
                else:
                    call ask_to_meet (event_Girls[0], "_bemused")
                return
            elif "master" not in event_Girls[0].history and "master" not in event_Girls[0].player_petnames and event_Girls[0].obedience >= 850 and event_Girls[0].event_happened[8] < 2:
                if bg_current == event_Girls[0].home or bg_current == "bg_player":
                    call expression event_Girls[0].tag + "_Master"
                else:
                    call ask_to_meet (event_Girls[0], "_bemused")

                return
            elif "daddy" not in event_Girls[0].player_petnames and approval_check(event_Girls[0], 750, "L") and approval_check(event_Girls[0], 500, "O") and approval_check(event_Girls[0], 500, "I"):
                if (bg_current == event_Girls[0].home or bg_current == "bg_player") and event_Girls[0].location == bg_current:
                    call expression event_Girls[0].tag + "_Daddy"

                return
            elif "sex friend" not in event_Girls[0].player_petnames and event_Girls[0].inhibition >= 500:
                if event_Girls[0] == EmmaX:
                    if bg_current == "bg_classroom" and (EmmaX.location == "bg_teacher" or EmmaX.location == "bg_classroom") and time_index == 2:
                        call Emma_Sexfriend
                        return
                elif event_Girls[0] == StormX:
                    if StormX.event_happened[9]:
                        pass
                    elif "traveling" in Player.recent_history and time_index < 2:
                        call Storm_Sexfriend

                        return
                elif bg_current == event_Girls[0].home or bg_current == "bg_player":
                    call expression event_Girls[0].tag + "_Sexfriend"

                    return
                elif event_Girls[0] in Player.Harem and event_Girls[0].location == bg_current:
                    call expression event_Girls[0].tag + "_Sexfriend"

                    return
                elif event_Girls[0] == LauraX:
                    call expression event_Girls[0].tag + "_Sexfriend"

                    return
            elif "fuck buddy" not in event_Girls[0].player_petnames and event_Girls[0].inhibition >= 800:
                if event_Girls[0] == RogueX:
                    if bg_current != event_Girls[0].location:
                        call expression event_Girls[0].tag + "_Fuckbuddy"

                        return
                elif event_Girls[0] == LauraX:
                    if bg_current == "bg_player" and event_Girls[0].location != bg_current:
                        call expression event_Girls[0].tag + "_Fuckbuddy"

                        return
                elif event_Girls[0] == StormX:
                    if bg_current == "bg_classroom" and time_index == 2 and weekday in (1,3):
                        call Storm_Fuckbuddy

                        return
                elif bg_current == event_Girls[0].home or bg_current == "bg_player":
                    call expression event_Girls[0].tag + "_Fuckbuddy"

                    return
                elif event_Girls[0] in Player.Harem and event_Girls[0].location == bg_current:
                    call expression event_Girls[0].tag + "_Fuckbuddy"

                    return

        $ event_Girls.remove(event_Girls[0])

    if "fix" in Player.daily_history:
        call check_addiction

    return

label display_girl(Girl, check_if_dressed = True, reset_actions = True, x_position = None, y_position = 0):
    if Girl.location != bg_current:
        call hide_girl(Girl)

        return

    if check_if_dressed:
        if Girl.outfit_name == "swimwear":
            if Girl.location == "bg_pool":
                $ Girl.change_outfit()
            elif Girl.today_outfit_name != "swimwear":
                $ Girl.change_outfit(Girl.today_outfit_name)
        elif taboo:
            $ Girl.change_outfit()
        elif Girl.location != "bg_dangerroom" and Girl.today_outfit_name != "gym_clothes":
            $ Girl.change_outfit(Girl.today_outfit_name)
    elif Girl.location != "bg_showerroom" and Girl.location != "bg_pool":
        $ Girl.wet = False

    if check_if_dressed:
        call outfitShame(Girl)

    if reset_actions:
        call stop_all_actions

    if x_position:
        $ Girl.sprite_location = x_position
    else:
        $ x_position = Girl.sprite_location

    if bg_current == "bg_movies" or bg_current == "bg_restaurant":
        $ y_position = 250

    if Girl == RogueX:
        show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(x_position, y_position):
    elif Girl == KittyX:
        show Kitty_sprite standing zorder Girl.sprite_layer at sprite_location(x_position, y_position):
    elif Girl == EmmaX:
        $ Girl.diamond = False

        show Emma_sprite standing zorder Girl.sprite_layer at sprite_location(x_position, y_position):
    elif Girl == LauraX:
        $ Girl.claws = False

        show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(x_position, y_position):
    elif Girl == JeanX:
        show Jean_sprite standing zorder Girl.sprite_layer at sprite_location(x_position, y_position):
    elif Girl == StormX:
        show Storm_sprite standing zorder Girl.sprite_layer at sprite_location(x_position, y_position):
    elif Girl == JubesX:
        show Jubes_sprite standing zorder Girl.sprite_layer at sprite_location(x_position, y_position):

    return

label set_the_scene(character = True, entering = False, check_if_dressed = True, reset_actions = True, silent = False):
    if not silent:
        show black_screen onlayer black

    if entering:
        $ character = False

        call hide_all

    if time_index >= 3:
        show night_mask onlayer nightmask
    else:
        hide night_mask

    if reset_actions:
        call stop_all_actions

        $ reset_actions = False

    if character:
        call check_who_is_present

        if Present:
            $ temp_Girls = Present[:]

            $ offset = 0.5/(len(Present) + 1)
            $ total_offset = offset

            while temp_Girls:
                if temp_Girls[0] != focused_Girl:
                    $ temp_Girls[0].sprite_location = stage_center + total_offset
                    $ temp_Girls[0].sprite_layer = 75

                    $ total_offset += offset

                    call display_girl(temp_Girls[0], check_if_dressed = check_if_dressed, reset_actions = False)

                $ temp_Girls.remove(temp_Girls[0])

            if focused_Girl.location == bg_current:
                $ focused_Girl.sprite_location = stage_center
                $ focused_Girl.sprite_layer = 100

                call display_girl(focused_Girl, check_if_dressed = check_if_dressed, reset_actions = False)

        if bg_current == "bg_study" and time_index < 3:
            show Xavier_sprite zorder 25 at sprite_location(stage_left)
        else:
            hide Xavier_sprite
    else:
        call hide_all(cull = True)

    show Chibi_UI
    hide cellphone

    if bg_current == "bg_classroom":
        if EmmaX.location == "bg_teacher":
            $ EmmaX.change_outfit()
        if StormX.location == "bg_teacher":
            $ StormX.change_outfit()

    hide dress_screen

    if simulation:
        show blue_screen onlayer black
    else:
        hide blue_screen onlayer black

    call checkout(total = True)

    if not silent:
        hide black_screen onlayer black

    return

label quick_event:
    call check_who_is_present

    $ event_Girls = all_Girls[:]
    $ renpy.random.shuffle(event_Girls)

    while event_Girls:
        if event_Girls[0].location == bg_current:
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
                elif bg_current != "bg_showerroom":
                    "[event_Girls[0].name] gets an embarrassed look on her face and suddenly leaves the room."

                    call remove_girl(event_Girls[0])
                    call set_the_scene

                    $ event_Girls[0].location = event_Girls[0].home if bg_current != event_Girls[0].home else "bg_campus"

                    if "no_masturbating" in event_Girls[0].traits:
                        $ event_Girls[0].add_word(1,0,"wants_to_masturbate",0,0)

                        call CalltoFap(event_Girls[0])
                    else:
                        $ event_Girls[0].add_word(1,0,"will_masturbate",0,0)
        else:
            if event_Girls[0].location == "bg_showerroom" and "showered" in event_Girls[0].daily_history:
                $ event_Girls[0].location = event_Girls[0].weekly_schedule[weekday][time_index]

                if event_Girls[0] == JubesX and JubesX.addiction > 60:
                    $ JubesX.location = JubesX.home

                python:
                    for key in event_Girls[0].spunk.keys():
                        event_Girls[0].spunk[key] = False

                $ event_Girls[0].change_outfit()

        $ event_Girls.remove(event_Girls[0])

    return

label tenth_round:
    if time_index >= 3:
        call sleepover

        return

    if bg_current not in personal_rooms or bg_current == "bg_player":
        call wait

        return

    $ Occupant = None

    python:
        for G in all_Girls:
            if G.home == bg_current:
                Occupant = G

    if not Occupant:
        call wait

        return

    if Occupant.location == bg_current:
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
    call girls_location

    if time_index < 3 or Occupant.location != bg_current:
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

        jump campus

    return

label hide_all(cull = False):
    if cull or RogueX.location != bg_current:
        hide Rogue_sprite

    if cull or KittyX.location != bg_current:
        hide Kitty_sprite

    if cull or EmmaX.location != bg_current:
        hide Emma_sprite

    if cull or LauraX.location != bg_current:
        hide Laura_sprite

    if cull or JeanX.location != bg_current:
        hide Jean_sprite

    if cull or StormX.location != bg_current:
        hide Storm_sprite

    if cull or JubesX.location != bg_current:
        hide Jubes_sprite

    if cull or "bg_study" != bg_current:
        hide Xavier_sprite

    return

label girls_location(change = False):
    $ temp_Girls = all_Girls[:]

    $ renpy.random.shuffle(temp_Girls)

    call change_out_of_gym_clothes(temp_Girls)

    while temp_Girls:
        if "leaving" in temp_Girls[0].recent_history:
            if "sleepover" in temp_Girls[0].traits:
                $ temp_Girls[0].drain_word("sleepover",0,0,1)

            call expression temp_Girls[0].tag + "_Leave"

            if temp_Girls[0].location != bg_current:
                if temp_Girls[0] in Present:
                    $ Present.remove(temp_Girls[0])

                $ change = True

        if temp_Girls[0] in Nearby and temp_Girls[0].location != "nearby":
            $ Nearby.remove(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    if change:
        call set_the_scene(check_if_dressed = False)

    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        if "arriving" in temp_Girls[0].recent_history:
            call Girls_Arrive

            return

        $ temp_Girls.remove(temp_Girls[0])

    return

label stop_all_actions(visual = False):
    $ Player.primary_action = None
    $ Player.secondary_action = None
    $ second_girl_main_action = None
    $ second_girl_secondary_action = None

    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        $ temp_Girls[0].main_action = None
        $ temp_Girls[0].secondary_action = None

        call reset_position(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    return

label reset_outfits:
    "This resets all customized clothing to their defaults."
    menu:
        "Do you want to continue?"
        "Yes":
            python:
                for G in all_Girls:
                    G.set_default_outfits()

            "Done."
            "You will now need to set their custom outfits again."
        "No":
            pass

    return

label drain_all_words(word, recent = True, daily = True, traits = False):
    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        $ temp_Girls[0].drain_word(word, recent, daily, traits)

        $ temp_Girls.remove(temp_Girls[0])

    return

label ask_to_meet(Girl, emotion = "_bemused"):
    if "asked_to_meet" not in Girl.daily_history and Girl.location != bg_current:
        $ Girl.change_face(emotion)

        "[Girl.name] asks if you could meet her in your room later."

        $ Girl.add_word(1, "asked_to_meet","asked_to_meet", 0, 0)

        $ Player.add_word(1, 0, "meet girl", 0, 0)

        if always_return_to_room:
            call return_to_room

    return

label return_to_room:
    menu:
        "Return to your room and deal with that?"
        "Yes":
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
                            $ RogueX.change_stat("love", 200, 1)
                            "You can also lower this number if you do things that make the girl upset, which is represented by a red -X."
                            $ RogueX.change_stat("love", 200, -1)
                        "Obedience Stat":
                            "The blue bar to the right of that is the \"Obedience level.\""
                            "This represents the girl's willingness to do what you want, and raises when you convince her to do something."
                            $ RogueX.change_stat("obedience", 200, 1)
                            "It lowers when you push her too far and she refuses."
                            $ RogueX.change_stat("obedience", 200, -1)
                        "Inhibition Stat":
                            "The yellow bar to the right of that is the \"Inhibition level.\""
                            "This represent's the girl's own sexual interest, and raises when she decides to do something on her own, or something naughty for the first time."
                            $ RogueX.change_stat("inhibition", 200, 1)
                            "It lowers when she becomes overly ashamed, like when caught doing something sexier than she's comfortable with."
                            $ RogueX.change_stat("inhibition", 200, -1)
                            "These are the three core relationship stats, and most activities in the game are gated by how high each is, either alone or in combinations."
                            "If you can reach 1000 in all three stats, she will be up for just about anything, although some activities do require special conditions."
                        "Back":
                            jump Tutorial_Stats
            "Sexual stats":
                "There are several stats which are used in sexual encounters."

                while True:
                    menu:
                        "Which Stat would you like to hear about?"
                        "lust":
                            "The bar underneath \"Love\" represents the girl's \"Lust.\""
                            "This stat raises as she becomes excited, and falls as she gets turned off or after she orgasms (at 100%%)."
                            $ RogueX.change_stat("lust", 200, 1)
                            $ RogueX.lust -= 1
                        "Player Excitement":
                            "The rather \"suggestive\" bar to the right of Inhibitions represents your own excitement."
                            $ Player.change_stat("focus", 200, 1)
                            $ Player.focus -= 1
                            "When it reaches 100%%, you orgasm. If you wish to delay this, you can learn to \"focus\" during sex and slow the progression."
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
                    "You can always just \"Wait\" This causes you to waste time, but who knows, maybe something interesting will happen."
                    "Of course when it's night time, this becomes \"Sleep.\" You can only sleep in your own room at first, but maybe someone else would let you sleep in her room."
                "shop":
                    "You can also access the school's fabricator store, where you can order various items to be delivered to your room."
                "Class":
                    "You can always attend classes. These are typically not that interesting, but will raise your XP, and various events might occur in class."
                    "Classes are open during weekday morning and midday periods. You might bump into Rogue there."
                    "You can access the classroom by using \"Leave [[Go to campus Square].\""
                "Danger Room":
                    "You can also attend a Danger Room training session. These also raise your XP."
                    "The Danger Room is open any time except late at night (students need their sleep)."
                    "You can access the Danger Room by using \"Leave [[Go to campus Square].\""
                "Shower":
                    "You can also take a shower, but don't worry, you'll do that off camera automatically if you don't get around to it."
                    "You can access the showers by using \"Leave [[Go to campus Square].\""
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

label SpecialMenu:
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
            "Halloween Party [[Evening Only] (locked)" if time_index != 2:
                pass
            "Halloween Party" if time_index == 2:
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


            "Do some Microtransactions [[locked] (locked)" if "micro" not in Player.history:
                call Microtransactions
            "Do some Microtransactions" if "micro" in Player.history:
                call Microtransactions
            "Visit McCoy's lab to change things about myself.":
                call Hanks_Lab
            "Reset Custom outfits":
                call reset_outfits
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
                        $ always_return_to_room = 1
                    "No [[current]" if not always_return_to_room:
                        pass
                    "No" if always_return_to_room:
                        $ always_return_to_room = 0
            "Press the red button" if False:
                "Huh, wonder what that was about. . ."
            "Never mind.":

                return
    return

label Hanks_Lab(line=0):
    "This is Professor McCoy's lab. You can do various self-modifications here."
    "The changes will be so seemless, it's almost like nobody will even notice!"
    while True:
        $ line = 0
        menu:
            "What would you like to do?"
            "Alter skin color":
                menu:
                    "What skin color would you like?"
                    "Green":
                        $ Player.color = "Green"
                    "White":
                        $ Player.color = "White"
                    "Black":
                        $ Player.color = "Black"
                    "Never mind":
                        $ line = 1
                if not line:
                    "You fiddle with some of McCoy's machinery and a glowing blue liquid pours into a flask."
                    "You down it in a single gulp, and within minutes your skin tone shifts to be more [Player.color]ish."
            "Change my name.":

                "You log in to McCoy's high end computer, this should allow you to change your name in all offical databases."
                $ Player.name = renpy.input("What name would you like?", default="Zero", length = 10)
                $ Player.name = Player.name.strip()
                if not Player.name:
                    $ Player.name = "Zero"
                if Player.name in ("master", "sir", "lover", "boyfriend", "sex friend", "fuck buddy"):
                    "Nice try, smartass."
                    $ Player.name = "Zero"
                if "met" in KittyX.history:
                    $ KittyX.player_petnames.append(Player.name[:1])
                if "met" in EmmaX.history:
                    call get_last_name
                    $ EmmaX.player_petnames.append(_return)
                "That should do it, your name has been updated and an email has been sent out to everyone on campus about the change."
            "Red Button" if False:
                if not Player.Harem:
                    "No harem"
                elif len(Player.Harem) == 4:
                    "[Player.Harem[0].tag],[Player.Harem[1].tag],[Player.Harem[2].tag],[Player.Harem[3].tag]"
                elif len(Player.Harem) == 3:
                    "[Player.Harem[0].tag],[Player.Harem[1].tag],[Player.Harem[2].tag]"
                elif len(Player.Harem) == 2:
                    "[Player.Harem[0].tag],[Player.Harem[1].tag]"
                else:
                    "[Player.Harem[0].tag]"
            "Blue Button":
                $ Count = len(active_Girls)
                "[Count]"
                if len(active_Girls) == 8:
                    "A-[active_Girls[0].tag],[active_Girls[1].tag],[active_Girls[2].tag],[active_Girls[3].tag]"
                    "B-[active_Girls[4].tag],[active_Girls[5].tag],[active_Girls[6].tag],[active_Girls[7].tag]"
                elif len(active_Girls) == 7:
                    "A-[active_Girls[0].tag],[active_Girls[1].tag],[active_Girls[2].tag],[active_Girls[3].tag]"
                    "B-[active_Girls[4].tag],[active_Girls[5].tag],[active_Girls[6].tag]"
                elif len(active_Girls) == 6:
                    "A-[active_Girls[0].tag],[active_Girls[1].tag],[active_Girls[2].tag],[active_Girls[3].tag]"
                    "B-[active_Girls[4].tag],[active_Girls[5].tag]"
                elif len(active_Girls) == 5:
                    "A-[active_Girls[0].tag],[active_Girls[1].tag],[active_Girls[2].tag],[active_Girls[3].tag]"
                    "B-[active_Girls[4].tag]"
                elif len(active_Girls) == 4:
                    "[active_Girls[0].tag],[active_Girls[1].tag],[active_Girls[2].tag],[active_Girls[3].tag]"
                elif len(active_Girls) == 3:
                    "[active_Girls[0].tag],[active_Girls[1].tag],[active_Girls[2].tag]"
                elif len(active_Girls) == 2:
                    "[active_Girls[0].tag],[active_Girls[1].tag]"
                else:
                    "[active_Girls[0].tag]"
                $ Count = 0
            "Yellow Button":
                $ Count = len(all_Girls)
                "[Count]"
                if len(all_Girls) == 8:
                    "A-[all_Girls[0].tag],[all_Girls[1].tag],[all_Girls[2].tag],[all_Girls[3].tag]"
                    "B-[all_Girls[4].tag],[all_Girls[5].tag],[all_Girls[6].tag],[all_Girls[7].tag]"
                elif len(all_Girls) == 7:
                    "A-[all_Girls[0].tag],[all_Girls[1].tag],[all_Girls[2].tag],[all_Girls[3].tag]"
                    "B-[all_Girls[4].tag],[all_Girls[5].tag],[all_Girls[6].tag]"
                elif len(all_Girls) == 6:
                    "A-[all_Girls[0].tag],[all_Girls[1].tag],[all_Girls[2].tag],[all_Girls[3].tag]"
                    "B-[all_Girls[4].tag],[all_Girls[5].tag]"
                elif len(all_Girls) == 5:
                    "A-[all_Girls[0].tag],[all_Girls[1].tag],[all_Girls[2].tag],[all_Girls[3].tag]"
                    "B-[all_Girls[4].tag]"
                elif len(all_Girls) == 4:
                    "[all_Girls[0].tag],[all_Girls[1].tag],[all_Girls[2].tag],[all_Girls[3].tag]"
                elif len(all_Girls) == 3:
                    "[all_Girls[0].tag],[all_Girls[1].tag],[all_Girls[2].tag]"
                elif len(all_Girls) == 2:
                    "[all_Girls[0].tag],[all_Girls[1].tag]"
                else:
                    "[all_Girls[0].tag]"
                $ Count = 0
            "Orange Button":
                $ line = "This is Halloween." if "halloween" in RogueX.history else "no"
                "Rogue: [line]"
                $ line = "This is Halloween." if "halloween" in KittyX.history else "no"
                "Kitty: [line]"
                $ line = "This is Halloween." if "halloween" in EmmaX.history else "no"
                "Emma: [line]"
                $ line = "This is Halloween." if "halloween" in LauraX.history else "no"
                "Laura: [line]"
                $ line = "This is Halloween." if "halloween" in JeanX.history else "no"
                "Jean: [line]"
                $ line = "This is Halloween." if "halloween" in StormX.history else "no"
                "Storm: [line]"
                $ line = 0
            "Leave.":
                return

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
                "Never Mind, I'll come back later.":

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
                "Never Mind, I'll come back later.":













                    return

    return







label clear_the_room(Character=0, Passive=0, Silent=0, Girls=[]):
    $ temp_Girls = all_Girls[:]
    $ temp_Girls.remove(Character) if Character in all_Girls else temp_Girls
    while temp_Girls:
        if temp_Girls[0].location == bg_current or temp_Girls[0] in Party:

            $ Girls.append(temp_Girls[0])
        elif temp_Girls[0].location == "bg_teacher" and bg_current == "bg_classroom":

            $ Girls.append(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    $ Nearby = []

    if not Silent and not Passive:

        if Character.location != bg_current:
            "[Character.name] enters the room."
            $ Character.location = bg_current
        if not Girls:

            if Character in all_Girls:
                call display_girl (Character)
            return
        if Character == RogueX:

            if len(Girls) > 1:

                ch_r "Ladies, could I talk to [Player.name] alone for a minute?"
            elif Girls:

                ch_r "[Girls[0].name], could I talk to [Player.name] alone for a minute?"
        elif Character == KittyX:
            if len(Girls) > 1:
                ch_k "Girls, could I talk to [Player.name] alone for a sec?"
            elif Girls:
                ch_k "[Girls[0].name], could I talk to [Player.name] alone for a sec?"
        elif Character == EmmaX:
            if len(Girls) > 1:
                ch_e "Girls, would you mind if I had a word alone with [Player.name]?"
            elif Girls:
                ch_e "[Girls[0].name], would you mind if I had a word alone with [Player.name]?"
        elif Character == LauraX:
            if len(Girls) > 1:
                ch_l "Hey, clear out, I need to talk with [Player.name]."
            elif Girls:
                ch_l "[Girls[0].name], clear out, I need to talk with [Player.name]."
        elif Character == JeanX:
            if len(Girls) > 1:
                ch_j "Let me have the room, ladies."
            elif Girls:
                ch_j "You there, clear out."
        elif Character == StormX:
            if len(Girls) > 1:
                ch_s "If I could have the room, ladies?"
            elif Girls:
                ch_s "If you could give me the room, [Girls[0].name], I need to speak with [Player.name]."
        elif Character == JubesX:
            if len(Girls) > 1:
                ch_v "Hey, could you gals check out? I've gotta talk to [Player.name]."
            elif Girls:
                ch_v "Hey, could you check out, [Girls[0].name]? I've gotta talk to [Player.name]."

    $ renpy.random.shuffle(Girls)

    while Girls:
        if Girls[0] in Party:
            $ Party.remove(Girls[0])
        $ Girls[0].drain_word("leaving",1,0,0)
        $ Girls[0].drain_word("arriving",1,0,0)

        if Silent:
            pass
        elif not Passive and Character != "all":

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

        if bg_current == Girls[0].home:
            if Character != "all":

                $ bg_current = Character.home
                $ Character.location = Character.home
                call set_the_scene
                call clear_the_room (Character)
                call taboo_level
                if not Silent:
                    "[Character.name] brings you back to her room. . ."

                $ Girl = Character
                jump girls_room
                return
            else:
                $ Girls[0].location = "bg_campus"
        else:
            $ Girls[0].location = Girls[0].home

        if Girls[0] == RogueX:
            hide Rogue_sprite with easeoutright
        elif Girls[0] == KittyX:
            hide Kitty_sprite with easeoutright
        elif Girls[0] == EmmaX:
            hide Emma_sprite with easeoutright
        elif Girls[0] == LauraX:
            hide Laura_sprite with easeoutright
        elif Girls[0] == JeanX:
            hide Jean_sprite with easeoutright
        elif Girls[0] == StormX:
            hide Storm_sprite with easeoutright
        elif Girls[0] == JubesX:
            hide Jubes_sprite with easeoutright

        $ Girls.remove(Girls[0])

    if Character in all_Girls:
        call display_girl (Character)
    call taboo_level
    return



label Girls_Arrive(Primary=0, Secondary=0, GirlsNum=0):
    $ Options = []

    call check_who_is_present
    $ temp_Girls = Present[:]
    while temp_Girls:

        if "arriving" in temp_Girls[0].recent_history and temp_Girls[0] not in Party:
            $ GirlsNum += 1
            $ Options.append(temp_Girls[0])
        $ temp_Girls[0].drain_word("arriving")
        $ temp_Girls.remove(temp_Girls[0])

    if not Options:

        return

    $ renpy.random.shuffle(Options)
    $ Primary = Options[0]
    if len(Options) >= 2:

        if bg_current == Options[1].home:
            $ Primary = Options[1]
            $ Secondary = Options[0]
        else:
            $ Secondary = Options[1]

    if Secondary not in all_Girls:
        $ Secondary = 0
    $ Options = []

    if "locked" in Player.traits:
        if Primary == KittyX:
            call locked_door (KittyX)
            if KittyX.location != bg_current:
                $ Primary = 0
            elif Secondary:

                "You hear a \"thump\" as if someone was trying to follow Kitty."
                call locked_door (Secondary)
                if Secondary.location != bg_current:
                    $ Secondary = 0
        elif Primary.home == bg_current:

            "You hear a key jiggling in the lock."
        else:
            call locked_door (Primary)
            if Primary.location != bg_current:
                $ Primary = 0


    if not Primary:
        return





    call shift_focus (Primary)
    if bg_current == "bg_dangerroom":


        $ Primary.outfit_name = "gym_clothes"
        $ Primary.change_outfit()
        if Secondary:
            $ Secondary.outfit_name = "gym_clothes"
            $ Secondary.change_outfit()

    call set_the_scene
    if bg_current == "bg_player":
        if Secondary:

            "[Primary.name] and [Secondary.name] just entered your room."
        else:

            "[Primary.name] just entered your room."

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
            "Nope.":
                $ line = "no"

        if line == "sure":
            $ Primary.change_stat("love", 80, 1)
            $ Primary.change_stat("obedience", 50, 2)
            $ Primary.change_stat("inhibition", 50, 2)
            if Primary == RogueX:
                ch_r "Thanks."
            elif Primary == KittyX:
                $ KittyX.change_stat("inhibition", 50, 1)
                ch_k "Cool."
            elif Primary == EmmaX:
                ch_e "Good."
            elif Primary == LauraX:
                $ LauraX.change_stat("love", 50, 1)
                $ LauraX.change_stat("obedience", 60, 1)
                "She doesn't leave."
            elif Primary == JeanX:
                "She doesn't leave."
            elif Primary == StormX:
                ch_s "Good."
            elif Primary == JubesX:
                ch_v "Nice."
            if Secondary:
                $ Secondary.change_stat("love", 80, 1)
                $ Secondary.change_stat("obedience", 50, 2)
                $ Secondary.change_stat("inhibition", 50, 2)

        if line == "later":
            $ Primary.change_stat("love", 60, -1, 1)
            $ Primary.change_stat("obedience", 70, 5)
            $ Primary.change_face("_confused")
            if Secondary and Secondary != JeanX:
                $ Secondary.change_stat("love", 60, -1, 1)
                $ Secondary.change_stat("obedience", 70, 5)
                $ Secondary.change_face("_confused")
                if Primary == RogueX:
                    ch_r "Um, ok, we'll go then."
                elif Primary == KittyX:
                    $ KittyX.change_stat("love", 60, -1, 1)
                    $ KittyX.change_stat("obedience", 70, 2)
                    ch_k "Oh[KittyX.like]we'll get going then."
                elif Primary == EmmaX:
                    $ EmmaX.change_stat("love", 90, -2)
                    $ EmmaX.change_stat("obedience", 30, -7)
                    ch_e "If that's how you wish to play it. . ."
                elif Primary == LauraX:
                    $ LauraX.change_stat("love", 90, -2)
                    $ LauraX.change_stat("obedience", 30, -7)
                    ch_l "Ok, later."
                elif Primary == StormX:
                    ch_s "Ah, then we'll leave you to it."
                elif Primary == JubesX:
                    ch_v "Oh. Ok. . ."
                call remove_girl (Secondary)
            elif Primary == RogueX:
                ch_r "Um, ok."
            elif Primary == KittyX:
                $ KittyX.change_stat("love", 60, -1, 1)
                $ KittyX.change_stat("obedience", 70, 2)
                ch_k "Oh[KittyX.like]I'll get going then."
            elif Primary == EmmaX:
                $ EmmaX.change_stat("love", 90, -2)
                $ EmmaX.change_stat("obedience", 30, -7)
                ch_e "If that's how you wish to play it. . ."
            elif Primary == LauraX:
                $ LauraX.change_stat("love", 90, -2)
                $ LauraX.change_stat("obedience", 30, -7)
                ch_l "Ok, later."
            elif Primary == StormX:
                ch_s "Ah, then I'll leave you to it."
            elif Primary == JubesX:
                ch_v "Oh. Ok. . ."
            if Primary == JeanX or Secondary == JeanX:
                ch_j "Uh-huh."
                "She doesn't leave."
            if Primary != JeanX:
                call remove_girl (Primary)

        if line == "no":
            $ Primary.change_stat("obedience", 50, 5)
            if approval_check(Primary, 1800) or approval_check(Primary, 500, "O"):

                $ Primary.change_stat("obedience", 80, 2)
                if Primary == RogueX:
                    ch_r "I guess that's ok. See you later then."
                elif Primary == KittyX:
                    ch_k "If you want some alone time. . ."
                elif Primary == EmmaX:
                    $ EmmaX.change_stat("obedience", 50, 2)
                    ch_e "I suppose you can have your personal space. . ."
                elif Primary == LauraX:
                    ch_l "Not a problem."
                elif Primary == StormX:
                    ch_s ". . . very well. . ."
                elif Primary == JubesX:
                    ch_v "Oh. Ok. . ."
            else:
                $ Primary.change_face("_angry")
                $ Primary.change_stat("love", 60, -5, 1)
                $ Primary.change_stat("love", 80, -2)
                $ Primary.change_stat("obedience", 80, 3)
                $ Primary.change_stat("inhibition", 50, 1)
                if Primary == RogueX:
                    ch_r "Well fine!"
                elif Primary == KittyX:
                    $ KittyX.change_stat("love", 80, -2)
                    $ KittyX.change_stat("obedience", 80, 2)
                    ch_k "Jerk!"
                elif Primary == EmmaX:
                    $ EmmaX.change_stat("love", 90, -2)
                    $ EmmaX.change_stat("obedience", 80, 3)
                    ch_e "We'll see how long that attitude lasts. . ."
                elif Primary == LauraX:
                    $ LauraX.change_stat("love", 90, -2)
                    "She seems upset."
                elif Primary == StormX:
                    ch_s ". . . I see. . ."
                elif Primary == JubesX:
                    ch_v "Oh, so you're going to be like -that-. . ."
            if Primary == JeanX or Secondary == JeanX:
                ch_j "Uh-huh."
                "She doesn't leave."
            if Primary != JeanX:
                call remove_girl (Primary)
            if Secondary and Secondary != JeanX:
                $ Secondary.change_stat("obedience", 50, 5)
                if approval_check(Secondary, 1800) or approval_check(Secondary, 500, "O"):
                    $ Secondary.change_stat("obedience", 80, 2)
                    if Secondary == RogueX:
                        ch_r "I guess that's ok. See you later then."
                    elif Secondary == KittyX:
                        ch_k "If you want some alone time. . ."
                    elif Secondary == EmmaX:
                        $ EmmaX.change_stat("obedience", 50, 2)
                        ch_e "I suppose you can have your personal space. . ."
                    elif Secondary == LauraX:
                        ch_l "Not a problem."
                    elif Primary == StormX:
                        ch_s ". . . very well. . ."
                    elif Primary == JubesX:
                        ch_v "Oh. Ok. . ."
                else:
                    $ Secondary.change_face("_angry")
                    $ Secondary.change_stat("love", 60, -5, 1)
                    $ Secondary.change_stat("love", 80, -2)
                    $ Secondary.change_stat("obedience", 80, 3)
                    $ Secondary.change_stat("inhibition", 50, 1)
                    if Secondary == RogueX:
                        ch_r "Well fine!"
                    elif Secondary == KittyX:
                        $ KittyX.change_stat("love", 80, -2)
                        $ KittyX.change_stat("obedience", 80, 2)
                        ch_k "Jerk!"
                    elif Secondary == EmmaX:
                        $ EmmaX.change_stat("love", 90, -2)
                        $ EmmaX.change_stat("obedience", 80, 3)
                        ch_e "We'll see how long that attitude lasts. . ."
                    elif Secondary == LauraX:
                        $ LauraX.change_stat("love", 90, -2)
                        "She seems upset."
                    elif Primary == StormX:
                        ch_s ". . . I see. . ."
                    elif Primary == JubesX:
                        ch_v "Oh, so you're going to be like -that-. . ."
                call remove_girl (Secondary)
                if Primary == JeanX:
                    "[Secondary.name] storms out."
                else:
                    "The girls storm out."
                    if Primary == StormX or Secondary == StormX:
                        "-so to speak."



    elif bg_current in personal_rooms:

        if Secondary:

            "[Primary.name] and [Secondary.name] just entered the room."
        else:

            "[Primary.name] just entered the room."
        if bg_current == Primary.home:
            if "_angry" in Primary.daily_history:

                $ Primary.change_face("_bemused", 1,brows="_angry")
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

            elif time_index >= 3 and approval_check(Primary, 1000, "LI") and approval_check(Primary, 600, "OI"):

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
            elif time_index >= 3:

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
                    $ Primary.change_face("_confused")
                    ch_l "Hey, [LauraX.player_petname], why are you here?"
                elif Primary == JeanX:
                    $ Primary.change_face("_confused")
                    ch_j "I didn't invite you here."
                elif Primary == StormX:
                    ch_s "I'm afraid that this is not a good time."
                elif Primary == JubesX:
                    ch_v "Hey, [JubesX.player_petname]? Not a good time."
            if line != "stay":

                menu:
                    extend ""
                    "Sure, ok. [[you go]":
                        $ Primary.change_stat("love", 80, 1)
                        $ Primary.change_stat("obedience", 50, 2)
                        $ Primary.change_stat("inhibition", 50, 2)
                        Primary.voice "Thanks."
                        "You head back to your room."
                    "Sorry, I'll go.":
                        $ Primary.change_stat("love", 90, 2)
                        $ Primary.change_stat("obedience", 50, 3)
                        $ Primary.change_face("_smile")
                        Primary.voice "Thanks."
                        "You head back to your room."
                    "Are you sure I can't stay?":
                        if "_angry" in Primary.daily_history:
                            $ Primary.change_face("_angry")
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
                                $ Primary.change_face("_angry",eyes="_side")
                                ch_v ". . ."
                                $ Primary.change_face("_angry",mouth="open")
                                ch_v "-YES.-"
                                $ Primary.change_face("_angry")
                        elif time_index >= 3 and approval_check(Primary, 800, "LI") and approval_check(Primary, 400, "OI"):
                            $ Primary.change_face("_sadside")
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
                        elif time_index >= 3:
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
                            $ Primary.change_face("_angry")
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
                            $ Primary.change_stat("love", 80, -1)
                            $ Primary.change_stat("inhibition", 50, 3)
                            "[Primary.name] kicks you out of the room."
                    "I'm sticking around, thanks.":

                        if "_angry" in Primary.daily_history or (not approval_check(Primary, 1800) and not approval_check(Primary, 500, "O")):
                            $ Primary.change_face("_angry")
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
                            $ Primary.change_stat("obedience", 80, 5)
                            $ Primary.change_face("_sad")
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
                            $ Primary.change_stat("love", 60, -5, 1)
                            $ Primary.change_stat("love", 80, -5)
                            $ Primary.change_stat("obedience", 50, 2)
                            $ Primary.change_stat("inhibition", 60, 5)
                            "[Primary.name] kicks you out of the room."

            if line != "stay":
                $ bg_current = "bg_player"
                jump player_room

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


    elif bg_current == "bg_classroom":



        if Secondary:

            "[Primary.name] and [Secondary.name] just entered the room."
        else:

            "[Primary.name] just entered the room."

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

        $ line = 0
        $ D20 = renpy.random.randint(1, 20)

        if Primary == EmmaX or Primary == StormX:

            if Secondary:
                $ Primary = Secondary
                $ Secondary = 0
            else:
                $ Primary = 0
        if Primary:

            if approval_check(Primary, 1000):
                if len(Present) < 2 and D20 >= 10:
                    $ line = Primary.name + " takes the seat next to you"

                    $ Present.append(Primary)
                else:
                    $ line = Primary.name + " sits across the room from you"

                    $ Nearby.append(Primary)
            else:
                $ line = Primary.name + " sits across the room from you"

                $ Nearby.append(Primary)

        if Secondary:
            if approval_check(Secondary, 1000):
                if len(Present) < 2 and D20 >= 10:

                    if Primary in Present:
                        $ line = Primary.name + " and " + Secondary.name + " sit down next to you"
                    else:
                        $ line = line + ", while " + Secondary.name + " takes the seat next to you"

                    $ Present.append(Secondary)
                else:
                    if Primary in Nearby:
                        $ line = Primary.name + " and " + Secondary.name + " sit across the room from you"
                    else:
                        $ line = line + ", while " + Secondary.name + " sits across the room from you"

                    $ Nearby.append(Secondary)
            else:
                if Primary in Nearby:
                    $ line = Primary.name + " and " + Secondary.name + " sit across the room from you"
                else:
                    $ line = line + ", while " + Secondary.name + " sits across the room from you"

                $ Nearby.append(Secondary)
        if line:
            "[line]."

        if EmmaX.location == "bg_teacher":
            "[EmmaX.name] takes her position behind the podium."
        elif StormX.location == "bg_teacher":
            "[StormX.name] takes her position behind the podium."

    elif bg_current == "bg_dangerroom":
        if Secondary:

            "[Primary.name] and [Secondary.name] just entered the room."
        else:

            "[Primary.name] just entered the room."

    elif bg_current == "bg_campus":
        if Secondary:

            "[Primary.name] and [Secondary.name] just entered the square."
        else:

            "[Primary.name] just entered the square."

    elif bg_current == "bg_pool":
        if Secondary:

            "[Primary.name] and [Secondary.name] just entered the pool area."
        else:

            "[Primary.name] just entered the pool area."
    else:

        if Secondary:

            "[Primary.name] and [Secondary.name] just entered the room."
        else:

            "[Primary.name] just entered the room."


    if bg_current in ("bg_campus","bg_dangerroom","bg_pool"):
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
            elif G.location == bg_current:
                Present.append(G)

    if Nearby:
        "There were some others as well, but they kept their distance."
    return



label gym_clothes_menu:
    menu:
        extend ""
        "Yeah, they look great.":
            $ G.change_face("_smile")
            $ G.change_stat("love", 80, 2)
            $ G.change_stat("obedience", 40, 1)
            $ G.change_stat("inhibition", 30, 1)

            return 1
        "No, stay in that.":
            $ G.change_face("_confused")
            $ G.change_stat("obedience", 50, 5)

            return 0
        "Whichever you like.":
            $ G.change_face("_confused")
            $ G.change_stat("inhibition", 50, 1)

            return renpy.random.randint(0, 3)
        "I don't care.":
            $ G.change_face("_angry")
            $ G.change_stat("love", 50, -3, 1)
            $ G.change_stat("obedience", 50, 4)
            $ G.change_stat("inhibition", 50, 2)

            return renpy.random.randint(0, 1)

label exit_gym(temp_Girls = []):
    if temp_Girls and temp_Girls[0] in all_Girls:
        pass
    else:
        $ temp_Girls = Party[:]

    $ line = None

    while temp_Girls:
        if temp_Girls[0].outfit_name == "gym_clothes":

            if len(Party) > 1:
                $ line = "We should change out of these if we're leaving. . ."
            else:
                $ line = "I should change out of these if we're leaving. . ."

            $ temp_Girls[0].outfit_name = temp_Girls[0].today_outfit_name

        $ temp_Girls.remove(temp_Girls[0])

    if Party and line:
        Party[0].voice "[line]"

    if line:
        show black_screen onlayer black with dissolve

        $ temp_Girls = Party[:]

        while temp_Girls:
            $ temp_Girls[0].change_outfit()
            $ temp_Girls.remove(temp_Girls[0])

        hide black_screen onlayer black

    return





label ReturnToSender:
    python:
        for G in active_Girls:
            if G not in Party and G.weekly_schedule[weekday][time_index] != bg_current:
                G.location = G.weekly_schedule[weekday][time_index]

                if G == JubesX and JubesX.addiction > 60:
                    JubesX.location = JubesX.home

    return





label Swap_Nearby(Girl=0):


    if Girl not in Nearby:
        return
    if bg_current not in ("bg_campus","bg_classroom","bg_dangerroom"):

        "There's no room for that here."
        return

    if len(Present) >= 2:

        Girl.voice "It's a little crowded over there."
        menu:
            "Move away from an adjacent girl?"
            "[RogueX.name]" if RogueX.location == bg_current:
                "You shift away from [RogueX.name]"
                call remove_girl (RogueX, 1, 1)
            "[KittyX.name]" if KittyX.location == bg_current:
                "You shift away from [KittyX.name]"
                call remove_girl (KittyX, 1, 1)
            "[EmmaX.name]" if EmmaX.location == bg_current:
                "You shift away from [EmmaX.name]"
                call remove_girl (EmmaX, 1, 1)
            "[LauraX.name]" if LauraX.location == bg_current:
                "You shift away from [LauraX.name]"
                call remove_girl (LauraX, 1, 1)
            "[JeanX.name]" if JeanX.location == bg_current:
                "You shift away from [JeanX.name]"
                call remove_girl (JeanX, 1, 1)
            "[StormX.name]" if StormX.location == bg_current:
                "You shift away from [StormX.name]"
                call remove_girl (StormX, 1, 1)
            "[JubesX.name]" if JubesX.location == bg_current:
                "You shift away from [JubesX.name]"
                call remove_girl (JubesX, 1, 1)
            "No, never mind.":
                return
    "[Girl.name] comes over and joins you."


    $ Nearby.remove(Girl)
    $ Present.append(Girl)
    call shift_focus (Girl)
    $ Girl.location = bg_current
    call set_the_scene (1, 0, 0, 0)
    return

label dismiss_menu:
    menu:
        "Did you want to ask someone to leave?"
        "[RogueX.name]" if RogueX.location == bg_current or RogueX in Party:
            call dismiss_girl(RogueX)
        "[KittyX.name]" if KittyX.location == bg_current or KittyX in Party:
            call dismiss_girl(KittyX)
        "[EmmaX.name]" if EmmaX.location == bg_current or EmmaX in Party:
            call dismiss_girl(EmmaX)
        "[LauraX.name]" if LauraX.location == bg_current or LauraX in Party:
            call dismiss_girl(LauraX)
        "[JeanX.name]" if JeanX.location == bg_current or JeanX in Party:
            call dismiss_girl(JeanX)
        "[StormX.name]" if StormX.location == bg_current or StormX in Party:
            call dismiss_girl(StormX)
        "[JubesX.name]" if JubesX.location == bg_current or JubesX in Party:
            call dismiss_girl(JubesX)
        "Nevermind.":
            pass

    return

label locked_door(Girl=0, entering=0, current_Girl=0):
    $ Player.add_word(1,"interruption")

    if not Player.primary_action:
        call set_the_scene

    if Girl == KittyX:
        if bg_current == "bg_campus" or bg_current == "bg_pool":
            "Suddenly, [Girl.name] rounds a corner."
        else:
            "You look to the door just as [KittyX.name] phases into the room."

        $ KittyX.location = bg_current

        call taboo_level

        $ KittyX.change_outfit()

        call display_girl (KittyX, reset_actions=0)

        ch_k "Hi, [KittyX.player_petname]!"

        return True

    if "locked" not in Player.traits:
        $ Girl.location = bg_current

        if entering:
            call display_girl (Girl, reset_actions=0)

            if bg_current == "bg_campus" or bg_current == "bg_pool":
                "Suddenly, [Girl.name] rounds a corner."
            else:
                "Suddenly, [Girl.name] enters the room, apparently without knocking."

            if Girl == RogueX:
                ch_r "Hey, got a minute, [Girl.player_petname]?"
            elif Girl == EmmaX:
                ch_e "[Girl.player_petname], I had something I wanted to discuss. . ."
            elif Girl == LauraX:
                ch_l "Hey, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "Hey, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "May I come in, [Girl.player_petname]?"
            elif Girl == JubesX:
                ch_v "Hey, [Girl.player_petname]."

        return True

    if Girl.location == Girl.home:
        "You hear a key in the lock, and [Girl.name] enters the room."
    elif Girl == JeanX:
        "You hear a rattle at the door."
        "After a moment, and some clicking in the lock, the door pops open."
        "[JeanX.name] walks into the room."

        $ JeanX.location = bg_current

        call taboo_level

        $ JeanX.change_outfit()

        call display_girl (JeanX, reset_actions=0)

        ch_j "Hey, [JeanX.player_petname]!"

        return True
    else:
        "The doorknob jiggles. A moment later, you hear a knock."

        if Girl == RogueX:
            ch_r "Could I come in, [Girl.player_petname]?"
        elif Girl == EmmaX:
            ch_e "[Girl.player_petname], I'm waiting."
        elif Girl == LauraX:
            ch_l "It's me."
        elif Girl == StormX:
            ch_s "[Girl.player_petname], may I come in?"
        elif Girl == JubesX:
            ch_v "Hey, it's [Girl.name]."

        menu:
            extend ""
            "Open door":
                ch_p "Hold on, [Girl.name]!"
                "You unlock the door and let her in."

                $ Girl.location = bg_current
                $ Girl.change_outfit()
            "Open door [[but stop fucking first]" if Player.primary_action:
                ch_p "Hold on, [Girl.name]!"

                call Sex_Over (1, Primary)
                "You unlock the door and let her in."

                $ Girl.location = bg_current
                $ Girl.change_outfit()

                call display_girl (Girl, reset_actions=0)

                if Girl == RogueX:
                    ch_r "Hey, got a minute, [Girl.player_petname]?"
                elif Girl == EmmaX:
                    ch_e "[Girl.player_petname], I had something I wanted to discuss. . ."
                elif Girl == LauraX:
                    ch_l "Hey, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "Hello, I wanted to talk with you. . ."
                elif Girl == JubesX:
                    ch_v "Hey, [Girl.player_petname]."

                jump reset_location
            "Send her away":
                ch_p "Er, sorry, could you come back later?"

                $ Girl.change_stat("love", 80, -2)

                if Girl == RogueX:
                    ch_r "C'mon, [Girl.player_petname], don't yank my chain like this!"

                    if Girl.location == bg_current:
                        call remove_girl (Girl)

                    return False
                elif Girl == EmmaX:
                    $ Girl.change_stat("obedience", 80, -2)

                    ch_e "I have to say, [EmmaX.player_petname], I understand the appeal of having someone at your beck and call. . ."
                    ch_e "but I don't appreciate being on the receiving end!"

                    if Girl.location == bg_current:
                        call remove_girl (Girl)

                    return False
                elif Girl in [LauraX, JubesX]:
                    "[Girl.name] goes quiet."

                    if approval_check(Girl, 500, "I") and not approval_check(Girl, 500, "O"):
                        $ Girl.location = bg_current
                        $ Girl.change_outfit()

                        if Girl == LauraX:
                            $ LauraX.arm_pose = 2
                            $ LauraX.claws = 1

                            "snickt"

                            call display_girl (Girl, reset_actions=0)

                            "The door swings open."

                            $ LauraX.claws = 0

                            ch_l "Hey, so I don't like being jerked around, so don't do that, okay?"
                        else:
                            "A thin mist passes under the door, and forms into a human shape."

                            call display_girl (Girl, reset_actions=0)

                            ch_v "Well, I wanted to talk."

                        $ Girl.change_stat("obedience", 80, -4)
                    else:
                        $ Girl.change_stat("love", 80, -1)
                        $ Girl.change_stat("obedience", 80, 3)

                        Girl.voice "Ok."

                        "You hear her shuffling off."

                        if Girl.location == bg_current:
                            call remove_girl (Girl)

                        return False
                elif Girl == StormX:
                    if approval_check(Girl, 800,"LI") and not approval_check(Girl, 500,"O"):
                        $ Girl.location = bg_current
                        $ Girl.change_outfit()

                        call display_girl (Girl, reset_actions=0)

                        "You hear some clicking from the door."
                        "The door swings open."

                        $ Girl.change_stat("obedience", 80, -4)

                        ch_s "That was not a quality lock."
                    else:
                        $ Girl.change_stat("love", 80, -1)
                        $ Girl.change_stat("obedience", 80, 3)

                        ch_s ". . ."
                        ch_s "Very well, I can respect that."

                        if Girl.location == bg_current:
                            call remove_girl (Girl)

                        return False

    if current_Girl:
        if current_Girl == EmmaX and ("threesome" not in EmmaX.history or "classcaught" not in EmmaX.history):

            $ Girl.add_word(1,0,0,"saw with " + current_Girl.tag)

            if bg_current == EmmaX.home:
                ch_e "I. . . This isn't what it looks like. . ."
                "She shoves the two of you out of her room and slams the door."

                $ Girl.location = "bg_player"

                call remove_girl (EmmaX)
            else:
                ch_e "I. . . This isn't what it looks like. . ."

                call remove_girl (EmmaX)

                "She seems uncomfortable with the situation and leaves the room."
                "Perhaps you should ask her about it later."

            jump reset_location

        if "poly " + current_Girl.tag in Girl.traits or (current_Girl in Player.Harem and Girl in Player.Harem):
            pass
        else:
            if approval_check(current_Girl, 1500, taboo_modifier=2, Bonus = (Girl.likes[current_Girl.tag] - 500)):
                $ current_Girl.change_face("_sexy", 1)
                $ current_Girl.change_stat("obedience", 90, 5)
                $ current_Girl.change_stat("inhibition", 90, 5)
                $ current_Girl.change_stat("lust", 90, 3)
            else:

                $ current_Girl.change_face("_angry", 1)

                if current_Girl == RogueX:
                    ch_r "Hey, [Girl.tag], we're a little busy here?"
                elif current_Girl == KittyX:
                    ch_k "Um, [Girl.tag]? Read the room?"
                elif current_Girl == EmmaX:
                    ch_e "[Girl.tag], could you please leave?"
                elif current_Girl == LauraX:
                    ch_l "Scram, [Girl.tag]."
                elif current_Girl == JeanX:
                    ch_j "Leave, [Girl.tag]."
                elif current_Girl == StormX:
                    ch_s "Would you mind give us some space?"
                elif current_Girl == JubesX:
                    ch_v "Yeah, we were. . . busy."

                $ Girl.add_word(1,0,0,"saw with " + current_Girl.tag)

                if Girl == RogueX:
                    $ Girl.change_face("_perplexed", 2)

                    ch_r "Oh, sorry about that! I'll head out."
                elif Girl == KittyX:
                    $ Girl.change_face("_perplexed", 2)

                    ch_k "Oh! Sorrysorrysorry!"
                elif Girl == EmmaX:
                    $ Girl.change_face("_bemused", 2)

                    ch_e "I wouldn't want to spoil the mood. . ."
                elif Girl == LauraX:
                    ch_l "Oh, sure. Whatever."
                elif Girl == JeanX:
                    $ Girl.change_face("_bemused", 1)

                    ch_j "Fine."
                elif Girl == StormX:
                    $ Girl.change_face("_bemused", 1)

                    ch_s "Yes. . ."
                elif Girl == JubesX:
                    $ Girl.change_face("_perplexed", 2)

                    ch_v "Oh, yes! Sorry!"

                $ Girl.change_face("_sad", 1)
                $ current_Girl.change_face("_sexy", 1)

                if Girl.location == bg_current:
                    call remove_girl (Girl)

                return False

        if current_Girl == RogueX:
            ch_r "Oh, [Girl.tag], did you want to join in?"
        elif current_Girl == KittyX:
            ch_k "Um, [Girl.tag]? Did you want something?"
        elif current_Girl == EmmaX:
            ch_e "Oh, [Girl.tag]. . . care to join us?"
        elif current_Girl == LauraX:
            ch_l "Oh, hey, [Girl.tag]."
        elif current_Girl == JeanX:
            ch_j "Hey."
        elif current_Girl == StormX:
            ch_s "Oh, hello [Girl.tag], did you want to join in?"
        elif current_Girl == JubesX:
            ch_v "Hey, [Girl.tag], did you need something?"

    $ Girl.location = bg_current

    call taboo_level

    $ Girl.change_outfit(check_if_yoinked = True)
    $ Player.drain_word("locked",0,0,1)

    call set_the_scene (1, 0, 0, 0)

    if Partner == Girl:
        $ Silent = 1

    $ Partner = Girl

    return True



label shift_focus(Girl, Second = None):
    if Girl.location == bg_current:
        python:
            for G in active_Girls:
                if G != Girl and G.location == bg_current:
                    G.sprite_location = stage_right
                    G.sprite_layer = 75

        $ Girl.sprite_location = stage_center
        $ Girl.sprite_layer = 100

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

transform sprite_location(x_position = stage_right, y_position = 0):
    pos (x_position, y_position)

image punchout:
    Null(0,0)

label punch:
    show punchout with vpunch
    hide punchout

    return


label Sex_Menu_Threesome(Girl=0):
    if not Girl or Girl not in all_Girls:
        return

    menu:
        "Do you want to join us [RogueX.name]?" if RogueX.location == bg_current and Girl != RogueX:
            if Partner == RogueX:

                ch_r "If I'd been do'in it right you wouldn't hafta ask. . ."
            else:
                if Girl == JeanX:

                    call Girl_Whammy (RogueX)
                call Girls_Noticed (Girl, RogueX, 1)
                if Girl.location != bg_current:

                    ch_r "Oh, well. . . I'm still game. . ."
                    call shift_focus(RogueX)
                    $ renpy.pop_call()
                elif RogueX.location == bg_current:
                    ch_r "I s'pose I could lend a hand 0. ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [KittyX.name]?" if KittyX.location == bg_current and Girl != KittyX:
            if Partner == KittyX:

                ch_k "Lol, what are you even talking about?"
            else:
                if Girl == JeanX:

                    call Girl_Whammy (KittyX)
                call Girls_Noticed (Girl, KittyX, 1)
                if Girl.location != bg_current:

                    ch_k "Whoa, drama much? 0. ."
                    call shift_focus(KittyX)
                    $ renpy.pop_call()
                elif KittyX.location == bg_current:
                    ch_k "I could[KittyX.like]give it a try. . ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [EmmaX.name]?" if EmmaX.location == bg_current and Girl != EmmaX:
            if Partner == EmmaX:

                ch_e "Have I not been keeping up?"
            else:
                if Girl == JeanX:

                    call Girl_Whammy (EmmaX)
                call Girls_Noticed (Girl, EmmaX, 1)
                if Girl.location != bg_current:

                    ch_e "Pity. . ."
                    call shift_focus(EmmaX)
                    $ renpy.pop_call()
                elif EmmaX.location == bg_current:
                    ch_e "So what did you have in mind for us. . ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [LauraX.name]?" if LauraX.location == bg_current and Girl != LauraX:
            if Partner == LauraX:

                ch_l "I already am."
            else:
                if Girl == JeanX:

                    call Girl_Whammy (LauraX)
                call Girls_Noticed (Girl, LauraX, 1)
                if Girl.location != bg_current:

                    ch_l "Her loss. . ."
                    call shift_focus(LauraX)
                    $ renpy.pop_call()
                elif LauraX.location == bg_current:
                    ch_l "Hm, ok. . ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [JeanX.name]?" if JeanX.location == bg_current and Girl != JeanX:
            if Partner == JeanX:

                ch_j "I've been here the entire time. . ."
            else:
                call Girls_Noticed (Girl, JeanX, 1)
                if Girl.location != bg_current:

                    ch_j "Huh. Her loss. . ."
                    call shift_focus(JeanX)
                    $ renpy.pop_call()
                elif JeanX.location == bg_current:
                    ch_j "Sure."
                else:
                    "She seems annoyed with this whole situation and leaves the room."

        "Do you want to join us [StormX.name]?" if StormX.location == bg_current and Girl != StormX:
            if Partner == StormX:

                ch_s "You hadn't noticed?"
            else:
                if Girl == JeanX:

                    call Girl_Whammy (StormX)
                call Girls_Noticed (Girl, StormX, 1)
                if Girl.location != bg_current:

                    ch_s "Oh, that's too bad. . ."
                    call shift_focus(StormX)
                    $ renpy.pop_call()

                elif StormX.location == bg_current:
                    ch_s "Delighted. . ."
                else:
                    "She seems uncomfortable with this situation and leaves the room."

        "Do you want to join us [JubesX.name]?" if JubesX.location == bg_current and Girl != JubesX:
            if Partner == JubesX:

                ch_v "I thought I already was!"
            else:
                if Girl == JeanX:

                    call Girl_Whammy (JubesX)
                call Girls_Noticed (Girl, JubesX, 1)
                if Girl.location != bg_current:

                    ch_v "Oh, well. . ."
                    call shift_focus(JubesX)
                    $ renpy.pop_call()
                elif JubesX.location == bg_current:
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
            elif second_girl_main_action in ("handjob","blowjob"):
                $ value += 1
            elif second_girl_main_action in ("eat_pussy","eat_ass"):
                $ value += 3
            else:
                $ value += 2


        $ Partner.check_if_likes(Girl,Measure,value,1)
        $ Girl.check_if_likes(Partner,Measure,value,1)

    return

label RoomStatboost(Type=0, Check=0, Amount=0):


    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == bg_current or temp_Girls[0] in Nearby:
            $ temp_Girls[0].change_stat(Type, Check, Amount)
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

            $ temp_GirlsA[0].check_if_likes(temp_GirlsB[0],Check,value,1)
            $ temp_GirlsB.remove(temp_GirlsB[0])
        $ temp_GirlsA.remove(temp_GirlsA[0])
    return

label JumperCheck(Girls=[]):

    if "nope" in Player.recent_history or Party:

        return

    $ temp_Girls = active_Girls[:]
    while temp_Girls:
        if "lesbian" in temp_Girls[0].recent_history and "no_les" not in Player.recent_history and approval_check(temp_Girls[0], 1600 - temp_Girls[0].SEXP, taboo_modifier=0):

            call Call_For_Les (temp_Girls[0])

        if "locked" in Player.traits and temp_Girls[0].location != bg_current:

            pass
        elif temp_Girls[0].remaining_actions and temp_Girls[0].thirst >= 30 and approval_check(temp_Girls[0], 500, "I") and "refused" not in temp_Girls[0].daily_history and "met" in temp_Girls[0].history:
            if "chill" not in temp_Girls[0].traits and temp_Girls[0].tag not in Player.daily_history and "jumped" not in temp_Girls[0].daily_history and temp_Girls[0].location != "bg_teacher":

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
            call remove_girl (Girls[0])
            $ Girls.remove(Girls[0])
        jump reset_location
    elif Girls:

        if Girls[0].location == bg_current:
            call enter_main_sex_menu(Girls[0])

    if bg_current == "bg_player":

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

    if Girls[0].location != bg_current and "locked" in Player.traits:

        call locked_door (Girls[0])
        if not Girls or Girls[0].location != bg_current:

            $ Player.recent_history.append("nope")
            return


    $ temp_Girls = Girls[:]
    while temp_Girls:
        $ temp_Girls[0].location = bg_current
        $ temp_Girls.remove(temp_Girls[0])
    $ Girls[0].add_word(1,"jumped","jumped")

    call taboo_level

    if taboo and (not approval_check(Girls[0], 1500, taboo_modifier=3) or (Girls[0] == EmmaX and taboo and "taboo" not in EmmaX.history)):

        $ Act = "leave"

    if bg_current in personal_rooms:

        if bg_current == "bg_player":
            pass
        elif Girls[0].home != bg_current and not (Partner and Partner.home == bg_current):

            $ Act = "leave"

    if Room_Full():
        $ Act = "leave"

    call shift_focus (Girls[0])
    call set_the_scene

    $ Player.recent_history.append("jumped")
    $ Girls[0].change_face("_sly",1)
    if Act == "leave":

        "Suddenly, [Girls[0].name] grabs your arm with a miscevious smile, and starts to lead you back towards your room."
        menu:
            "Go along with it":
                $ Girls[0].change_stat("inhibition", 95, 3)
                "You follow after her."
            "Pull away from her and head back.":
                $ Girls[0].change_stat("love", 90, -10)
                $ Girls[0].change_stat("obedience", 50, 10)
                $ Girls[0].change_stat("obedience", 95, 5)
                $ Girls[0].change_stat("inhibition", 95, -5)
                $ Girls[0].change_face("_sad",1)
                "You tell her to cut it out, and head back to what you were doing."
                $ Player.recent_history.append("nope")
                $ Girls[0].add_word(1,"refused","refused")
                if not approval_check(Girls[0], 500, "O"):
                    $ Girls[0].add_word(1,"_angry","_angry")
                return

        if Partner:
            "[Partner.name] also follows along behind you."

        $ bg_current = "bg_player"
        call clear_the_room (Girls[0], 1, 1)
    else:


        if Partner in all_Girls:
            $ Girls[1].change_face("_sly",1)
            "Suddenly, [Girls[0].name] pulls you aside and [Partner.name] follows along."
        else:
            "Suddenly, [Girls[0].name] pulls you aside."
        menu:
            "See where this is going":
                $ Girls[0].change_stat("inhibition", 95, 2)
            "Not here [[head to your room]":
                $ Girls[0].change_stat("inhibition", 95, 1)
                "You head to your room first."
                $ bg_current = "bg_player"
                call clear_the_room (Girls[0], 1, 1)
            "Pull away from her and head back.":
                $ Girls[0].change_stat("love", 90, -10)
                $ Girls[0].change_stat("obedience", 50, 10)
                $ Girls[0].change_stat("obedience", 95, 5)
                $ Girls[0].change_stat("inhibition", 95, -5)
                $ Girls[0].change_face("_sad",1)
                "You tell her to cut it out, and head back to what you were doing."
                $ Player.recent_history.append("nope")
                $ Girls[0].add_word(1,"refused","refused")
                if not approval_check(Girls[0], 500, "O"):
                    $ Girls[0].add_word(1,"_angry","_angry")
                return

    $ temp_Girls = Girls[:]
    while temp_Girls:
        $ temp_Girls[0].location = bg_current
        $ temp_Girls.remove(temp_Girls[0])

    call taboo_level
    call set_the_scene(check_if_dressed = False)

    $ Girls[0].add_word(1,"jumped","jumped",0,"jumped")

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

    if Act in ("anal","sex","blowjob","titjob","handjob","hotdog"):

        "[Girls[0].name] reaches down and unzips your fly. . ."
        if not Player.semen:
            "You wish you weren't already drained. . . you stop her hands."
            ch_p "I could actually use a break right now. . "
            $ Act = "fondle_breasts"
        else:
            call Seen_First_Peen (Girls[0], Partner, 1)

    if Partner:
        call Girls_Noticed (Girls[0], 1)

    call before_action(Girls[0], Act, Girls[0])

label Quick_Sex(Girl=focused_Girl, Act=0):


    $ Girl.change_face("_sly",1)
    $ Girl.add_word(1,"quicksex","quicksex")
    menu:
        extend ""
        "Sure":
            $ Girl.change_stat("love", 95, 4)
            $ Girl.change_stat("obedience", 50, 1)
            $ Girl.change_stat("inhibition", 70, 2)
            $ Girl.change_stat("inhibition", 90, 3)
        "No thanks":
            $ line = 0
            $ Girl.change_stat("love", 80, -2)
            if (2*Girl.obedience) >= (Girl.love + Girl.inhibition + (5*Girl.thirst)):

                $ Girl.change_face("_sadside",1)
                $ Girl.change_stat("obedience", 90, 7)
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
                        $ Girl.change_stat("love", 80, -2)
                        $ Girl.change_stat("obedience", 80, -8)
                        $ line = "ask"
                    ". . . [[say nothing, still no].":
                        pass
            elif (approval_check(Girl, 600, "I") and Girl.thirst >= 30) or Girl.thirst >= 50:

                $ Girl.change_face("_confused",1,eyes="_surprised")
                $ Girl.change_stat("love", 80, -1)
                $ Girl.change_stat("obedience", 70, 4)
                $ Girl.change_stat("inhibition", 60, 5)
                $ Girl.change_stat("inhibition", 90, 3)
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
                            $ Girl.change_face("_sly",1)
                            $ Girl.change_stat("love", 80, 2)
                            $ Girl.change_stat("love", 95, 3)
                            $ Girl.change_stat("obedience", 70, 2)
                            $ Girl.change_stat("inhibition", 90, 3)

                        "Beg me." if counter < 100:
                            $ Girl.change_stat("obedience", 80, 2)
                            $ line = "beg"
                        "Beg me again." if counter >= 100:
                            $ Girl.change_stat("obedience", 90, 2)
                            $ line = "beg"
                        "Only if I get to choose.":

                            $ Girl.change_face("_smile",1,brows="_confused")
                            $ Girl.change_stat("love", 90, 2)
                            $ Girl.change_stat("obedience", 80, 3)
                            $ Girl.change_stat("obedience", 95, 3)
                            $ Girl.change_stat("inhibition", 85, 2)
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

                            $ Girl.change_stat("love", 85, -2)
                            $ Girl.change_stat("obedience", 90, 3)
                            if approval_check(Girl, 1500+(5*counter)-(10*Girl.thirst), "LI"):

                                $ line = "beg"
                            elif not counter and Count:

                                $ Girl.top_pulled_up = 1
                                pause 1
                                call expression Girl.tag + "_First_Topless" pass (1)
                                $ Girl.top_pulled_up = 0
                                $ Girl.change_face("_confused",1,mouth="_smile")
                                $ Girl.change_stat("inhibition", 70, 3)
                                $ Girl.change_stat("inhibition", 95, 3)
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

                                $ Girl.change_face("_sad",2)
                                $ Girl.change_stat("love", 90, -2)
                                $ Girl.change_stat("obedience", 50, 5)
                                $ Girl.change_stat("obedience", 95, 3)
                                $ Girl.change_stat("inhibition", 90, 3)
                                if Girl == RogueX:
                                    ch_r "Please?"
                                elif Girl == KittyX:
                                    ch_k "Pretty please?"
                                elif Girl == EmmaX:
                                    ch_e ". . ."
                                    $ Girl.change_stat("love", 90, -2)
                                    $ Girl.change_stat("obedience", 200, 3)
                                    ch_e ". . .Please?"
                                elif Girl == LauraX:
                                    ch_l "Um. . . Please?"
                                elif Girl == JeanX:
                                    ch_j "Huh. . ."
                                    $ Girl.change_stat("obedience", 90, 3)
                                    ch_j "Ok. . . please? 0. ."
                                elif Girl == StormX:
                                    ch_s "No? You're that certain?"
                                elif Girl == JubesX:
                                    ch_v "Ya'sure?"
                            else:

                                $ Girl.change_face("_sad",2,eyes="_surprised")
                                $ Girl.change_stat("love", 90, -4)
                                $ Girl.change_stat("obedience", 70, 6)
                                $ Girl.change_stat("obedience", 200, 3)
                                $ Girl.change_stat("inhibition", 90, 5)
                                if Girl == RogueX:
                                    ch_r "Come on, I really need it. . ."
                                elif Girl == KittyX:
                                    ch_k "I need you, [Girl.player_petname]!"
                                elif Girl == EmmaX:
                                    $ Girl.change_stat("love", 90, -2)
                                    $ Girl.change_stat("obedience", 200, 1)
                                    ch_e "I. . . really need you here, [Girl.player_petname]. . ."
                                elif Girl == LauraX:
                                    $ Girl.change_stat("obedience", 80, 1)
                                    ch_l "I've got a fevah, and the only prescription is your dick. . ."
                                elif Girl == JeanX:
                                    ch_j "I. . ."
                                    ch_j "Come on, man. . ."
                                    $ Girl.change_stat("obedience", 90, 5)
                                    ch_j "Please?"
                                elif Girl == StormX:
                                    ch_s ". . ."
                                elif Girl == JubesX:
                                    ch_v "Pretty Please?"
                            $ Count = 1 if Count <= 0 else Count
                            $ counter += 100
                        elif counter > 50:

                            $ Girl.change_face("_angry",1)
                            $ Girl.change_stat("love", 70, -3)
                            $ Girl.change_stat("love", 85, -5)
                            $ Girl.change_stat("obedience", 80, -2)
                            $ Girl.change_stat("inhibition", 90, 4)
                            if Girl == RogueX:
                                ch_r "I'm not going to beg again."
                            elif Girl == KittyX:
                                ch_k "Not even!"
                            elif Girl == EmmaX:
                                $ Girl.change_stat("love", 90, -3)
                                $ Girl.change_stat("obedience", 70, -3)
                                $ Girl.change_stat("obedience", 200, 2)
                                ch_e "I. . . Once was too much!"
                            elif Girl == LauraX:
                                ch_l "Ooooh, you are pushing it, [Player.name]."
                            elif Girl == JeanX:
                                $ Girl.change_stat("obedience", 90, 4)
                                ch_j "Whatever. . ."
                            elif Girl == StormX:
                                ch_s "So be it."
                            elif Girl == JubesX:
                                ch_v "Boooo."
                        else:

                            $ Girl.change_face("_sad",2,brows="_confused")
                            $ Girl.change_stat("love", 95, -2)
                            $ Girl.change_stat("obedience", 50, -2)
                            $ Girl.change_stat("obedience", 90, -2)
                            $ Girl.change_stat("inhibition", 90, 5)
                            if Girl == RogueX:
                                ch_r "I'm not going to beg."
                            elif Girl == KittyX:
                                ch_k "That's. . . rude."
                            elif Girl == EmmaX:
                                $ Girl.change_stat("obedience", 70, -2)
                                ch_e "That is so beneath me."
                            elif Girl == LauraX:
                                ch_l "Not worth it. ."
                            elif Girl == JeanX:
                                $ Girl.change_stat("obedience", 90, 4)
                                ch_j "Yeah, not worth it. . ."
                            elif Girl == StormX:
                                ch_s "So be it."
                            elif Girl == JubesX:
                                ch_v "Booo."


            $ line = 0
            if not Act:

                $ Girl.change_stat("love", 80, -2)
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

    if Act in ("anal","sex","blowjob","titjob","handjob","hotdog"):

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

    if Player.primary_action == "fondle_breast" and approval_check(Girl,1050,taboo_modifier=4,Alt=[[JeanX],800]) and Girl.lust >= 30 and Girl.action_counter["suck_breasts"]:

        if Player.secondary_action == "suck_breasts":
            $ Player.secondary_action = None
        $ Girl.change_stat("inhibition", 80, 2)

        call before_action(Girl, "suck_breasts", Girl)

        if "suck_breasts" in Girl.recent_history:

            $ renpy.pop_call()
    elif Player.primary_action == "fondle_thighs" and approval_check(Girl,1050,taboo_modifier=4,Alt=[[JeanX],800]) and Girl.lust >= 30 and Girl.action_counter["fondle_pussy"]:

        if Player.secondary_action == "fondle_thighs":
            $ Player.secondary_action = None
        $ Girl.change_stat("inhibition", 80, 4)

        call before_action(Girl, "fondle_thighs", Girl)

        if "fondle_pussy" in Girl.recent_history:

            $ renpy.pop_call()
    elif not Player.semen:

        pass
    elif Player.primary_action == "handjob" and approval_check(Girl,1200,taboo_modifier=4) and Girl.lust >= 30 and Girl.action_counter["blowjob"]:

        $ Girl.change_stat("inhibition", 80, 3)

        call before_action(Girl, "blowjob", Girl)
        if "blowjob" in Girl.recent_history:

            $ renpy.pop_call()
    elif Player.primary_action not in ("sex","anal") and approval_check(Girl,1400,taboo_modifier=5,Alt=[[JeanX],1200]) and Girl.lust >= 60 and Girl.action_counter["sex"] >= 3:

        $ Girl.change_stat("inhibition", 80, 4)

        call before_action(Girl, "sex", Girl)
        if "sex" in Girl.recent_history:

            $ renpy.pop_call()
    elif Player.primary_action != "anal" and approval_check(Girl,1400,taboo_modifier=5,Alt=[[JeanX],1200]) and Girl.lust >= 70 and Girl.action_counter["anal"] >= 5:

        $ Girl.change_stat("inhibition", 80, 5)

        call before_action(Girl, "anal", Girl)
        if "anal" in Girl.recent_history:

            $ renpy.pop_call()


    $ position_timer = 0

    return

label Sex_Dialog(Primary=focused_Girl, Secondary=0, TempFocus=0, PrimaryLust=0, SecondaryLust=0, line1=0, line2=0, line3=0, line4=0, D20S=0):






    $ D20S = renpy.random.randint(1, 20) if not D20S else D20S
    $ line = 0







    call Girls_taboo (Primary)
    if not Player.primary_action and not Primary.secondary_action:
        return

    $ Secondary = Partner

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
            $ line3 = line + "."



    if Secondary and (not second_girl_main_action or 7 <= D20S <= 17 or second_girl_main_action == "watch"):

        $ line = 0
        call SexDialog_Threeway
        if line:
            $ line4 = line + "."



    $ Player.change_stat("focus", 200, TempFocus)


    $ Primary.change_stat("lust", 200, PrimaryLust)
    $ Primary.lust_face()


    if Secondary:
        $ SecondaryLust += (int(PrimaryLust/10)) if Secondary.likes[Primary.tag] >= 700 else 0
        $ Secondary.change_stat("lust", 200, SecondaryLust)
        $ Secondary.lust_face()


    "[line1]"
    if line3:

        call Seen_First_Peen (Primary, Secondary, Passive=3)
        "[line3]"
    if line4:


        call Seen_First_Peen (Primary, Secondary, Passive=4)
        "[line4]"
        if second_girl_main_action == "suck_breasts" or second_girl_main_action == "fondle_breasts":

            if approval_check(Primary,500,"I",taboo_modifier=2) and Primary.lust >= 50 and (Primary.outfit["bra"] or Primary.top_number() > 1):

                $ Primary.top_pulled_up = 1
                "[Primary.name] seems frustrated and pulls her top open."

    call Activity_Check (Primary, Secondary, 0)
    if not _return:

        if Primary.forced:


            return
        if Secondary and Secondary.location == bg_current:
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
        $ Tempshame = Girl2.outfit["shame"]

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
        $ approval = approval_check(Girl,1550,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "anal":
        $ approval = approval_check(Girl,1550,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "sex":
        $ approval = approval_check(Girl,1400,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "eat_pussy":
        $ approval = approval_check(Girl,1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.secondary_action == "jerking_off":
        $ approval = approval_check(Girl,1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "blowjob":
        $ approval = approval_check(Girl,1300,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "titjob":
        $ approval = approval_check(Girl,1200,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "hotdog":
        $ approval = approval_check(Girl,1000,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "handjob" or girl_offhand_action == "handjob":
        $ approval = approval_check(Girl,1100,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "footjob":
        $ approval = approval_check(Girl,1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "dildo_ass":
        $ approval = approval_check(Girl,1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "dildo_pussy":
        $ approval = approval_check(Girl,1250,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "finger_ass":
        $ approval = approval_check(Girl,1300,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "fondle_pussy" or Player.primary_action == "finger_pussy":
        $ approval = approval_check(Girl,1050,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "suck_breasts":
        $ approval = approval_check(Girl,1050,Bonus=Mod, taboo_modifier = (tabooM* 3 ))
    elif Player.primary_action == "fondle_breasts":
        $ approval = approval_check(Girl,950,Bonus=Mod, taboo_modifier = (tabooM* 2 ))
    elif Player.primary_action == "fondle_ass":
        $ approval = approval_check(Girl,850,Bonus=Mod, taboo_modifier = (tabooM* 1 ))

    elif Player.primary_action == "masturbation":
        $ approval = approval_check(Girl,1200,Bonus=Mod, taboo_modifier = (tabooM* 2 ))

    elif Player.primary_action == "kiss":
        $ approval = approval_check(Girl,500,Bonus=Mod, taboo_modifier = 0)
    elif Player.primary_action == "fondle_thighs":
        $ approval = approval_check(Girl,750,Bonus=Mod, taboo_modifier = 0)

    elif Player.primary_action == "lesbian":
        $ approval = approval_check(Girl,1350,Bonus=Mod, taboo_modifier = (tabooM* 2 ))


    if not approval:

        pass
    elif not second_girl_main_action:
        pass
    elif second_girl_main_action == "eat_ass":
        $ approval = approval_check(Girl,1750,Bonus=(Mod+200), taboo_modifier = (tabooM* 3 ))
    elif second_girl_main_action == "eat_pussy":
        $ approval = approval_check(Girl,1450,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "blowjob":
        $ approval = approval_check(Girl,1300,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "handjob":
        $ approval = approval_check(Girl,1200,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "finger_ass":
        $ approval = approval_check(Girl,1500,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "fondle_pussy":
        $ approval = approval_check(Girl,1250,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "suck_breasts":
        $ approval = approval_check(Girl,1250,Bonus=(Mod+200), taboo_modifier = (tabooM* 3 ))
    elif second_girl_main_action == "fondle_breasts":
        $ approval = approval_check(Girl,1150,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "kiss girl":
        $ approval = approval_check(Girl,1050,Bonus=(Mod+200), taboo_modifier = 0)
    elif second_girl_main_action == "kiss both":
        $ approval = approval_check(Girl,1050,Bonus=(Mod+200), taboo_modifier = 0)
    elif second_girl_main_action == "fondle_ass":
        $ approval = approval_check(Girl,1050,Bonus=(Mod+200), taboo_modifier = (tabooM* 1 ))
    elif second_girl_main_action == "masturbation":
        $ approval = approval_check(Girl,1400,Bonus=(Mod+200), taboo_modifier = (tabooM* 2 ))
    elif second_girl_main_action == "watch":
        $ approval = approval_check(Girl,1000,Bonus=(Mod+200), taboo_modifier = 0)
    elif second_girl_main_action == "kiss":
        $ approval = approval_check(Girl,600,Bonus=Mod, taboo_modifier = 0)

    if not Silent and not approval and not Girl.forced:
        $ Girl.change_face("_sadside",1)
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
        call remove_girl (Girl, 2)
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
                $ Player.add_word(1,"naked",0,0,0)
            elif "cockout" in Player.recent_history:
                return
            else:
                "You whip your cock out."

            $ Player.add_word(1,"cockout",0,0,0)
    else:


        if Passive:

            if approval == Passive and "cockout" not in Player.recent_history:

                call CockOut
            if "cockout" not in Player.recent_history:
                return


        call Girl_First_Peen (Primary, Silent, Undress, React=React)

        if Secondary:

            call Girl_First_Peen (Secondary, Silent, Undress, Second=_return)
    return

label CockOut:

    if approval == 3:


        call Girl_First_Peen (Primary, React=1)
    elif approval == 4:


        call Girl_First_Peen (Secondary, React=1)
    $ approval = 0
    return

label Get_Dressed:

    if "naked" in Player.recent_history:
        "You get dressed."
        $ Player.drain_word("naked")
        $ Player.drain_word("cockout")
    elif "cockout" in Player.recent_history:
        "You put your cock away."
        $ Player.drain_word("cockout")
    return

label Girl_First_Peen(Girl=0, Silent=0, Undress=0, Second=0, React=0):







    if Girl.location != bg_current:
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
    $ Girl.change_stat("inhibition", 30, 2)
    $ Girl.change_stat("inhibition", 80, 1)

    if Second:

        if Girl.seen_peen == 1:
            $ Girl.change_face("_surprised", 2)
            if Girl == RogueX:
                ch_r "Wow, yeah, that's pretty nice. . ."
            elif Girl == KittyX:
                ch_k "Oh, wow, you aren't kidding. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("_smirk", 2, eyes = "_down")
                ch_e "My, that certainly is an impressive specimen. . ."
            elif Girl == LauraX:
                $ Girl.change_face("_smirk", 2, eyes = "_down")
                ch_l "Huh, that's a pretty good one you got there. . ."
            elif Girl == JeanX:
                $ Girl.change_face("_smirk", 2, eyes = "_down")
                ch_j "Yeah, looking good. . ."
            elif Girl == StormX:
                $ Girl.change_face("_smirk", 2, eyes = "_down")
                ch_s "Yes, that is impressive. . ."
            elif Girl == JubesX:
                $ Girl.change_face("_smirk", 2, eyes = "_down")
                ch_v "Oh, wow, yeah. . ."
            $ Girl.change_face("_bemused", 1)
        elif Second == 1:

            if not approval_check(Girl, 800) and not approval_check(Girl, 500, "I"):
                $ Girl.change_face("_sad", 1)
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
                $ Girl.change_face("_bemused", 1)
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
                $ Girl.change_face("_sad", 1)
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
                $ Girl.change_face("_confused", 1)
                if Girl == RogueX:
                    ch_r "Well I liked it. . ."
                    $ Girl.change_face("_sexy", 1)
                elif Girl == KittyX:
                    ch_k "Come on, it's really cute!"
                    $ Girl.change_face("_smile", 1)
                elif Girl == EmmaX:
                    ch_e "You just don't appreciate the finer things. . ."
                    $ Girl.change_face("_sly",0)
                elif Girl == LauraX:
                    ch_l "Aw, come on, it's not that bad. . ."
                    $ Girl.change_face("_sly",0)
                elif Girl == JeanX:
                    ch_j "I mean, I've seen worse. . ."
                    $ Girl.change_face("_sly",0)
                elif Girl == StormX:
                    ch_s "It's far from the worst I've seen. . ."
                    $ Girl.change_face("_sly",0)
                elif Girl == JubesX:
                    ch_v "More for me, I guess. . ."
                    $ Girl.change_face("_sly",0)
        $ Silent = 1

    if Undress:
        $ Player.add_word(1,"naked")
    if not Silent:
        if "cockout" in Player.recent_history:
            $ Girl.change_face("_down", 2)
            "[Girl.name] glances down at your exposed cock."
        elif React:

            "[Girl.name] reaches for your pants and pulls out your cock."
        elif Undress:
            "You strip nude."
        else:
            "You whip your cock out."
        $ Player.add_word(1,"cockout")
        if not Girl.forced and not React and taboo > 20 and (not approval_check(Girl, 1500) or Girl.SEXP < 10) and bg_current != "bg_showerroom" and Girl not in (JeanX,StormX):

            if not approval_check(Girl, 800) and not approval_check(Girl, 500, "I"):

                if Girl == EmmaX and ("detention" in Girl.recent_history or "classcaught" in Girl.recent_history):

                    $ Girl.change_face("_confused", eyes="_down")
                    ch_e "Mmm?"
                    $ Girl.change_face("_surprised", eyes="_squint")
                    if Girl.seen_peen == 1:
                        $ Girl.change_stat("love", 30, 10)
                        $ Girl.change_stat("love", 90, 5)
                        $ Girl.change_stat("obedience", 50, 20)
                        $ Girl.change_stat("inhibition", 60, 30)
                    else:
                        $ Girl.change_stat("love", 90, 2)
                        $ Girl.change_stat("obedience", 50, 3)
                        $ Girl.change_stat("inhibition", 60, 5)
                    ch_e "Well I suppose I can make an exception in this case."
                    $ React = 1
                else:

                    $ Girl.change_face("_surprised", 2)
                    if Girl == RogueX:
                        ch_r "What the hell?"
                    elif Girl == KittyX:
                        ch_k "Huh?!"
                    elif Girl == EmmaX:
                        $ Girl.eyes = "_down"
                        ch_e "Mmm?"
                    elif Girl == LauraX:
                        $ Girl.eyes = "_down"
                        ch_l "Mmm?"
                    elif Girl == JubesX:
                        $ Girl.eyes = "_down"
                        ch_v "Hey. . ."
                        $ Girl.eyes = "_squint"
                        ch_v "What's that about?"
                    $ Girl.change_face("_angry", 1)
                    $ Girl.recent_history.append("_angry")
                    $ Girl.daily_history.append("_angry")
                    $ React = 2
                    if Girl.seen_peen == 1:
                        $ Girl.change_stat("love", 90, -20)
                        $ Girl.change_stat("obedience", 50, 30)
                        $ Girl.change_stat("inhibition", 60, 20)
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

                            $ Girl.change_stat("love", 90, -1)
                            $ Girl.change_stat("obedience", 50, 1)
                            $ Girl.change_stat("inhibition", 60, 2)
                        else:
                            $ Girl.change_stat("love", 90, -5)
                            $ Girl.change_stat("obedience", 50, 10)
                            $ Girl.change_stat("inhibition", 60, 10)
            else:


                $ Girl.change_face("_surprised", 2)
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
                $ Girl.change_face("_bemused", 1)
                if Girl.seen_peen == 1:
                    if Girl == RogueX:
                        ch_r "I mean. . . no, definitely put that away!"
                    elif Girl == KittyX:
                        ch_k "Or[Girl.like]maybe. . ."
                    elif Girl == EmmaX:
                        $ Girl.eyes = "_down"
                        ch_e ". . . impressive though it may be. . ."
                    elif Girl == LauraX:
                        ch_l ". . . not that I mind, myself. . ."
                    elif Girl == JubesX:
                        ch_v "Or. . . not. . ."
                    $ Girl.change_stat("love", 90, 20)
                    $ Girl.change_stat("obedience", 50, 20)
                    $ Girl.change_stat("inhibition", 60, 30)
                $ React = 2


        elif Girl.seen_peen > 10:

            return False
        elif approval_check(Girl, 1200) or approval_check(Girl, 500, "L"):

            $ Girl.change_face("_sly",1)
            if Girl.seen_peen == 1:
                $ Girl.change_face("_surprised",2)
                if Girl == RogueX:
                    ch_r "Whoa, I didn't know they looked so big up close."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("love", 90, 5)
                elif Girl == KittyX:
                    $ Girl.change_face("_surprised",2)
                    ch_k "That's. . . impressive."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("love", 90, 3)
                elif Girl == EmmaX:
                    $ Girl.change_face("_surprised",1, eyes="_down")
                    ch_e "Well that's certainly an interesting specimen."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("love", 50, 5)
                    $ Girl.change_stat("love", 90, 10)
                elif Girl == LauraX:
                    $ Girl.change_face("_surprised",1, eyes="_down")
                    ch_l "Huh, that's a pretty good one you got there. . ."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("love", 50, 5)
                    $ Girl.change_stat("love", 90, 10)
                elif Girl == JeanX:
                    $ Girl.change_face("_confused",1, eyes="_down",mouth="_smile")
                    ch_j "Well, what do we have here. . ."
                    $ Girl.change_face("_bemused",1)
                    ch_j "Preeety nice there, [Girl.player_petname]."
                    $ Girl.change_stat("love", 50, 5)
                    $ Girl.change_stat("love", 90, 10)
                    $ Girl.change_stat("obedience", 80, 3)
                elif Girl == StormX:
                    $ Girl.change_face("_confused",1, eyes="_down")
                    ch_s "Hmm. . . that is a lovely one."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("love", 50, 5)
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("inhibition", 60, 2)
                elif Girl == JubesX:
                    $ Girl.change_face("_surprised",2, eyes="_down")
                    ch_v "Oh. . . nice."
                    $ Girl.change_face("_sly",1)
                    $ Girl.change_stat("love", 80, 3)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 4)
            elif Girl.seen_peen == 2:
                if Girl == RogueX:
                    ch_r "That thing sure is impressive."
                    $ Girl.change_stat("obedience", 50, 5)
                elif Girl == KittyX:
                    ch_k "I can't get over that."
                    $ Girl.change_stat("obedience", 50, 7)
                elif Girl == EmmaX:
                    $ Girl.eyes = "_down"
                    ch_e "Oh, hello again."
                    $ Girl.change_stat("inhibition", 50, 5)
                elif Girl == LauraX:
                    $ Girl.eyes = "_down"
                    ch_l "Oh, there it is."
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 50, 3)
                elif Girl == JeanX:
                    $ Girl.eyes = "_down"
                    ch_j "Still pretty impressive. . ."
                    $ Girl.change_stat("love", 90, 3)
                    $ Girl.change_stat("obedience", 80, 3)
                elif Girl == StormX:
                    $ Girl.eyes = "_down"
                    ch_s "Hmm. . ."
                    $ Girl.change_stat("inhibition", 50, 2)
                elif Girl == JubesX:
                    $ Girl.change_face("_sly",1, eyes="_down")
                    ch_v "Hello again."
                    $ Girl.change_face("_sly",1)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 1)
            elif Girl.seen_peen == 5:
                if Girl == RogueX:
                    ch_r "I certainly appreciate that guy."
                    $ Girl.change_stat("inhibition", 60, 5)
                elif Girl == KittyX:
                    ch_k "There it is."
                    $ Girl.change_stat("inhibition", 60, 5)
                elif Girl == EmmaX:
                    ch_e "Yes, we've seen that before."
                    $ Girl.change_stat("obedience", 60, 7)
                elif Girl == LauraX:
                    ch_l "Yeah, I've seen that one."
                    $ Girl.change_stat("obedience", 60, 4)
                    $ Girl.change_stat("inhibition", 60, 3)
                elif Girl == JeanX:
                    $ Girl.eyes = "_down"
                    ch_j "Nice. . ."
                    $ Girl.change_stat("love", 90, 3)
                    $ Girl.change_stat("obedience", 80, 2)
                elif Girl == StormX:
                    ch_s ". . ."
                    $ Girl.change_stat("inhibition", 60, 5)
                elif Girl == JubesX:
                    $ Girl.change_face("_sly",1, eyes="_down")
                    ch_v "Hey there. . ."
                    $ Girl.change_face("_sly",1)
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
            elif Girl.seen_peen == 10:
                if Girl == RogueX:
                    ch_r "I never get tired of seeing that."
                    $ Girl.change_stat("love", 90, 10)
                elif Girl == KittyX:
                    ch_k "So beautiful."
                    $ Girl.change_stat("obedience", 80, 10)
                    $ Girl.change_stat("inhibition", 60, 3)
                elif Girl == EmmaX:
                    $ Girl.eyes = "_down"
                    ch_e "I do appreciate some of your features."
                    $ Girl.change_stat("obedience", 80, 5)
                    $ Girl.change_stat("inhibition", 60, 10)
                elif Girl == LauraX:
                    $ Girl.eyes = "_down"
                    ch_l "I don't get tired of that view."
                    $ Girl.change_stat("obedience", 80, 8)
                    $ Girl.change_stat("inhibition", 60, 7)
                elif Girl == JeanX:
                    $ Girl.eyes = "_down"
                    ch_j "Thanks for that. . ."
                    $ Girl.change_stat("love", 90, 10)
                    $ Girl.change_stat("obedience", 80, 8)
                elif Girl == StormX:
                    $ Girl.eyes = "_down"
                    ch_s "Well, I do enjoy that one."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("inhibition", 60, 2)
                elif Girl == JubesX:
                    $ Girl.change_face("_confused",1, eyes="_down")
                    ch_v "Kinda. . . hypnotic. . ."
                    $ Girl.change_face("_sly",1)
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 60, 2)
            $ React = 1
        else:

            $ Girl.change_face("_sad",1)
            if Girl.seen_peen == 1:
                $ Girl.change_face("_perplexed",1 )
                $ Girl.eyes = "_down"
                if Girl == RogueX:
                    ch_r "Well, I guess that's impressive. What do you plan to do with it?"
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("inhibition", 60, 5)
                elif Girl == KittyX:
                    ch_k "Well that happened. . ."
                elif Girl == EmmaX:
                    ch_e "Are you aware that your dick is out?"
                    $ Girl.change_stat("obedience", 50, 2)
                elif Girl == LauraX:
                    ch_l "Your dick is out."
                    $ Girl.change_stat("inhibition", 60, 2)
                elif Girl == JeanX:
                    ch_j "Hey, you're penis is out."
                    $ Girl.change_stat("obedience", 80, 4)
                    $ Girl.change_stat("inhibition", 70, 4)
                elif Girl == StormX:
                    ch_s "Apparently you enjoy a nice breeze as well. . ."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("inhibition", 60, 5)
                elif Girl == JubesX:
                    ch_v "Hmm, ok. . ."
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
                $ Girl.change_stat("obedience", 50, 5)
                $ Girl.change_stat("inhibition", 60, 5)
            elif Girl.seen_peen < 5:
                $ Girl.change_face("_sad",0)
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
                    $ Girl.change_stat("obedience", 80, 2)
                $ Girl.change_stat("inhibition", 60, 2)
            elif Girl.seen_peen == 10:
                if Girl == RogueX:
                    ch_r "I'm getting tired of seeing that."
                    $ Girl.change_stat("obedience", 50, 5)
                    $ Girl.change_stat("inhibition", 60, 5)
                elif Girl == KittyX:
                    ch_k "[Girl.Like]put that away."
                    $ Girl.change_stat("obedience", 50, 7)
                    $ Girl.change_stat("inhibition", 60, 3)
                elif Girl == EmmaX:
                    ch_e "Yes, we've all seen that before."
                    $ Girl.change_stat("obedience", 50, 7)
                    $ Girl.change_stat("inhibition", 60, 5)
                elif Girl == LauraX:
                    ch_l "Yeah, yeah, waving your cock around again."
                    $ Girl.change_stat("obedience", 50, 8)
                    $ Girl.change_stat("inhibition", 60, 4)
                elif Girl == JeanX:
                    ch_j "Oh, Penis. So original."
                    $ Girl.change_stat("obedience", 50, 8)
                    $ Girl.change_stat("inhibition", 60, 4)
                elif Girl == StormX:
                    ch_s ". . ."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("obedience", 50, 2)
                    $ Girl.change_stat("inhibition", 60, 4)
                elif Girl == JubesX:
                    ch_v ". . ."
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
            $ React = 2
    else:

        $ Player.recent_history.append("cockout")
        if Girl.seen_peen > 10:
            return
        elif approval_check(Girl, 1200) or approval_check(Girl, 500, "L"):
            if Girl.seen_peen == 1:
                $ Girl.change_stat("love", 90, 5)
            elif Girl.seen_peen == 2:
                $ Girl.change_stat("obedience", 50, 5)
            elif Girl.seen_peen == 5:
                $ Girl.change_stat("inhibition", 60, 5)
            elif Girl.seen_peen == 10:
                $ Girl.change_stat("love", 90, 10)
        else:
            if Girl.seen_peen == 1:
                $ Girl.change_stat("obedience", 50, 5)
                $ Girl.change_stat("inhibition", 60, 5)
                $ Girl.add_word(1,0,0,0,"seenpeen")
            elif Girl.seen_peen < 5:
                $ Girl.change_stat("inhibition", 60, 2)
            elif Girl.seen_peen == 10:
                $ Girl.change_stat("obedience", 50, 5)
                $ Girl.change_stat("inhibition", 60, 5)
        if Girl == JubesX:
            $ Girl.change_stat("obedience", 80, 1)
    if Girl.seen_peen == 1:
        if Girl == JeanX:
            $ Girl.change_stat("love", 90, 10)
            $ Girl.change_stat("obedience", 30, 20)
            $ Girl.change_stat("obedience", 50, 10)
            $ Girl.change_stat("obedience", 80, 5)
        elif Girl == JubesX:
            $ Girl.change_stat("obedience", 80, 3)
        $ Girl.change_stat("love", 90, 15)
        $ Girl.change_stat("obedience", 90, 20,Alt=[[StormX],900,0])
        $ Girl.change_stat("inhibition", 60, 20)
        $ Girl.change_stat("lust", 200, 5)
    $ Girl.change_face("_sly",1)
    return React

label Girls_taboo(Girl=0, counter=1, Choice=0, D20=0):




    if Girl not in all_Girls:
        $ Girl = focused_Girl
    $ Player.add_word(1,0,Girl.tag)
    $ Player.add_word(1,0,"scent")

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
            if (Player.primary_action == "kiss" and not Player.secondary_action and not girl_offhand_action):

                pass
            elif Girl not in Rules:

                $ Girl.change_face("_surprised", 1)
                if Player.primary_action == "blowjob" or Player.primary_action == "handjob" or Player.primary_action == "titjob":
                    "[Girl.name] stops what she's doing with a startled look."
                else:
                    "You feel a slight buzzing in your head and stop what you're doing."
                ch_x "Cease that behavior at once! Come to my office immediately!"
                call reset_position(Girl)
                call Girls_Caught (Girl)
                return
            else:

                ch_x "Hmmm. . ."
                $ Girl.change_stat("inhibition", 90, 2)
                $ Girl.change_stat("lust", 200, 3)
        if bg_current == "bg_classroom" and EmmaX.location == "bg_teacher" and Girl != EmmaX:

            call Emma_Teacher_Caught (Girl)
        elif bg_current == "bg_classroom" and StormX.location == "bg_teacher" and Girl != StormX:

            call Storm_Teacher_Caught (Girl)
        elif "interruption" in Player.recent_history:

            pass
        elif D20 == 1 and AloneCheck(Girl) and time_index < 3:

            $ Choice = active_Girls[:]
            $ Choice.remove(Girl)
            $ renpy.random.shuffle(Choice)
            while Choice:
                if Choice[0].location != bg_current and "lockedout" not in Girl.traits:
                    $ second_girl_secondary_action = Choice[0]
                    $ Choice = [1]
                $ Choice.remove(Choice[0])
            if second_girl_secondary_action:
                call locked_door (second_girl_secondary_action, 1, Girl)

            $ Choice = 0
            $ second_girl_secondary_action = None



        call Girls_Noticed (Girl)

    if taboo <= 20:

        call Girls_Noticed (Girl)
        return
    elif (Player.primary_action == "kiss" and not Player.secondary_action and not girl_offhand_action):

        pass
    elif counter < 4:


        if Girl in (EmmaX,StormX) and "public" not in Girl.history:
            $ Girl.history.append("public")

        if "spotted" not in Girl.recent_history:
            "Some of the other students notice you and [Girl.name]."
            $ Girl.change_stat("inhibition", 200, 2)
            $ Girl.reputation -= 2
            $ Player.reputation -= 2
        elif counter < 3:
            "A few more students notice you and [Girl.name]."
            $ Girl.change_stat("inhibition", 200, 2)
            $ Girl.reputation -= 1
            $ Player.reputation -= 1
        elif counter == 3:
            "You've got quite an audience."
            $ Girl.change_stat("inhibition", 200, 3)
            $ Girl.reputation -= 1
            $ Player.reputation -= 1
        if Partner:
            $ Partner.reputation -= 1


        if "exhibitionist" in Girl.traits:
            $ Girl.change_face("_sexy", 0)
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
            $ Girl.change_stat("lust", 200, 4)
            $ Choice = "A"
        elif approval_check(Girl, 650, "I", taboo_modifier=counter):

            $ Girl.change_face("_sexy", 1, brows="_sad")
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
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 80, 3)
                    ch_j "Looks like we have an audience. . ."
                elif Girl == StormX:
                    ch_s "We seem to have attracted some attention. . ."
                elif Girl == JubesX:
                    ch_v "Oh, um, they're looking. . ."
            $ Girl.change_stat("lust", 200, 3)
            $ Choice = "B"
        elif approval_check(Girl, 1000, "OI", taboo_modifier=counter):

            $ Girl.change_face("_surprised", 2)
            if Girl in (EmmaX,StormX):
                "[Girl.name] looks a bit concerned."
            elif Girl == LauraX:
                "[Girl.name] looks a bit uncomfortable."
            else:
                "[Girl.name] looks a bit panicked."
            $ Girl.change_stat("lust", 200, 3)
            $ Choice = "C"
        else:

            $ Girl.change_face("_surprised", 2)
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
                    $ Girl.change_stat("love", 90, -15)
                    "With a sudden embarrassed start, [Girl.name] panics. She dives through the nearest wall."
                elif Girl in (EmmaX,StormX):
                    $ Girl.change_stat("love", 90, -15)
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
                        $ Girl.change_face("_sexy", 0)
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

                        $ Girl.change_face("_sexy", 1,brows="_sad")
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
                        $ Girl.change_face("_sexy",2)
                        if Girl.obedience > Girl.inhibition:
                            $ Girl.eyes = "_side"
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
                            $ Girl.mouth = "_smile"
                            $ Girl.brows = "_sad"
                            if Girl == RogueX:
                                ch_r "Uh, I guess. . ."
                            elif Girl == KittyX:
                                ch_k "Yeah[KittyX.like]sure. . ."
                            elif Girl == EmmaX:
                                ch_e "Not that I mind, of course."
                            elif Girl == LauraX:
                                ch_l "Whatever. . ."
                            elif Girl == JeanX:
                                $ Girl.change_stat("obedience", 80, 3)
                                $ Girl.change_stat("inhibition", 80, 3)
                                ch_j "Yeah. . ."
                            elif Girl == StormX:
                                ch_s "Very well. . ."
                            elif Girl == JubesX:
                                ch_v "I guess."
                        $ Girl.change_stat("obedience", 200, 5)
                    "You get back to it."
                    $ Girl.blushing = "_blush1"
                "Continue" if "spotted" in Girl.recent_history:
                    if Choice == "C":
                        $ Girl.change_stat("obedience", 200, 4)
                "Ok, let's stop.":
                    if Choice == "A":
                        $ Girl.change_face("_sad")
                        if Girl == KittyX:
                            ch_k "Booo."
                        elif Girl == LauraX:
                            ch_l "Sissy."
                        elif Girl == StormX:
                            ch_s "Oh, if you insist. . ."
                        else:
                            Girl.voice "Spoilsport."
                    elif Choice == "B":
                        $ Girl.change_face("_sad")
                        if Girl == RogueX:
                            ch_r "Yeah, probably."
                        elif Girl == KittyX:
                            ch_k "Um, yeah."
                        elif Girl == EmmaX:
                            ch_e "I suppose."
                        elif Girl == LauraX:
                            ch_l "Probably a good call."
                        elif Girl == JeanX:
                            $ Girl.change_stat("love", 80, 3)
                            $ Girl.change_stat("obedience", 80, 3)
                            ch_j "Yeah. . . wouldn't want to cause a riot."
                        elif Girl == StormX:
                            ch_s "I suppose it's for the best. . ."
                        elif Girl == JubesX:
                            ch_v "Yeah, I guess so. . ."
                    elif Choice == "C":
                        $ Girl.change_stat("love", 90, 5)
                        $ Girl.change_face("_smile")
                        if Girl == RogueX:
                            ch_r "Heh, thanks [Girl.player_petname]"
                        elif Girl == KittyX:
                            ch_k "Heh, thanks [Girl.player_petname]."
                            $ Girl.change_stat("love", 90, 5)
                        elif Girl == EmmaX:
                            ch_e "That probably would be for the best. . ."
                        elif Girl == LauraX:
                            ch_l "Yeah, thanks."
                            $ Girl.change_stat("love", 90, 5)
                        elif Girl == JeanX:
                            $ Girl.change_stat("love", 80, 3)
                            $ Girl.change_stat("obedience", 80, 3)
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
            call reset_position(Girl)
            call remove_girl (Girl)
            $ Girl.change_outfit()
            hide black_screen onlayer black
            $ bg_current = "bg_player"
            jump player_room
    elif "exhibitionist" not in Girl.traits:
        $ Girl.change_face("_sly")
        if Girl == JeanX and "nowhammy" not in JeanX.traits:

            pass
        else:
            $ Girl.traits.append("exhibitionist")
            "[Girl.name] seems to have become something of an exhibitionist."
    elif D20 > 15:
        $ Girl.change_face("_sexy")
        "The crowd cheers."

    $ Girl.recent_history.append("spotted") if counter < 4 else Girl.recent_history
    $ Girl.daily_history.append("spotted")  if "spotted" not in Girl.daily_history else Girl.daily_history
    return

label Girls_Noticed(Girl=Primary, Other=0, Silent=0, B=0):
    python:
        for temp_Girl in all_Girls:
            if temp_Girl == Girl:
                continue
            elif temp_Girl.location == bg_current:
                Other = temp_Girl

                break

    if Other not in all_Girls or Other == Girl:
        return
    if "threesome" in Other.recent_history:
        return
    if Partner == Other and "noticed " + Girl.tag in Other.recent_history:
        return

    if not Silent:
        if Partner != Other:

            $ Other.change_face("_surprised", 1)
            "[Other.name] noticed what you and [Girl.name] are up to."
        else:

            $ Other.change_face("_sly", 1)
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

        $ Other.add_word(1,0,0,"saw with " + Girl.tag)
        if bg_current == EmmaX.home:

            ch_e "If the two of you cannot keep your hands off each other, please do so elsewhere. . ."
            "She shoves the two of you out of her room and slams the door."
            $ Girl.location = "bg_player"
            jump player_room
        call remove_girl (EmmaX)
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

    $ Other.sprite_location = stage_far_right
    call display_girl (Other, 0, 0)
    if Partner == Other:

        $ Silent = 1
    $ Partner = Other
    $ line = 0
    if approval_check(Other, 2000, taboo_modifier=2, Bonus = B) or approval_check(Other, 950, "L", taboo_modifier=2, Bonus = (B/3)):

        $ Other.change_face("_sexy", 1)
        if not Silent:
            "She decides to join you."
        $ Other.change_stat("obedience", 90, 5)
        $ Other.change_stat("inhibition", 90, 5)
        $ Other.change_stat("lust", 90, 3)
        $ Other.add_word(1,0,0,"poly " + Girl.tag)
        call Threeway_Set (Other, Mode="start", GirlB=Girl)
    elif approval_check(Other, 650, "O", taboo_modifier=2) and approval_check(Other, 450, "L", taboo_modifier=1) or approval_check(Other, 800, "O", taboo_modifier=2, Bonus = (B/3)):

        $ Other.change_face("_sexy")
        if not Silent:
            "She sits down patiently off to the side and watches."
        $ Other.change_stat("love", 90, 5)
        $ Other.change_stat("inhibition", 90, 5)
        $ Other.change_stat("lust", 90, 2)
        $ Other.add_word(1,0,0,"poly " + Girl.tag)
        call Threeway_Set (Other, "watch", Mode="start", GirlB=Girl)
    elif approval_check(Other, 650, "I", taboo_modifier=2) and approval_check(Other, 450, "L", taboo_modifier=1) or approval_check(Other, 800, "I", taboo_modifier=2, Bonus = (B/3)):

        $ Other.change_face("_sexy")
        if not Silent:
            "She sits down and watches you with a hungry look."
        $ Other.change_stat("love", 90, 5)
        $ Other.change_stat("obedience", 90, 2)
        $ Other.change_stat("inhibition", 90, 2)
        $ Other.change_stat("lust", 90, 5)
        $ Other.add_word(1,0,0,"poly " + Girl.tag)
        call Threeway_Set (Other, "watch", Mode="start", GirlB=Girl)
    elif approval_check(Other, 1500, taboo_modifier=2, Bonus = B):
        $ Other.change_face("_perplexed", 1)
        if not Silent:
            "She looks a little confused at what's happening, but she stays put and watches."
        if Other.love >= Other.obedience and Other.love >= Other.inhibition:
            $ Other.change_stat("obedience", 90, 2)
            $ Other.change_stat("inhibition", 90, 2)
        elif Other.obedience >= Other.inhibition:
            $ Other.change_stat("love", 90, 2)
            $ Other.change_stat("inhibition", 90, 2)
        else:
            $ Other.change_stat("love", 90, 2)
            $ Other.change_stat("obedience", 90, 1)
            $ Other.change_stat("inhibition", 90, 1)
        $ Other.change_stat("lust", 90, 5)
        call Threeway_Set (Other, "watch", Mode="start", GirlB=Girl)
    elif approval_check(Other, 650, "L", taboo_modifier=1) or approval_check(Other, 400, "O", taboo_modifier=2):

        $ Other.change_face("_angry", 2)
        if bg_current == Other.home:
            if Other in (LauraX,JeanX):
                "She looks annoyed, and kicks you both out of the room."
            else:
                "She looks betrayed, and kicks you both out of the room."
        else:
            if Other in (LauraX,JeanX):
                "She looks annoyed, and storms out of the room."
            else:
                "She looks betrayed, and storms out of the room."
        $ Other.change_stat("love", 200, -5)
        $ Other.change_stat("love", 80, -5)
        $ Other.change_stat("love", 70, -5)
        $ Other.change_stat("obedience", 90, -5)
        $ Other.change_stat("lust", 89, 10)
        $ Partner = 0
        $ Other.add_word(1,0,0,"saw with " + Girl.tag)
        if bg_current == Other.home:
            $ Other.recent_history.append("_angry")
            call are_girls_angry
        call remove_girl (Other)
    else:

        $ Other.change_face("_surprised", 2)
        $ Other.change_stat("inhibition", 90, 2)
        $ Other.change_stat("lust", 40, 20)
        if Player.primary_action != "kiss":
            $ Other.change_stat("love", 90, -10)
            $ Other.change_stat("obedience", 90, -5)
            $ Other.change_stat("lust", 80, 10)
        if bg_current == Other.home:
            $ Other.change_stat("love", 90, -5)
            $ Other.change_stat("obedience", 90, -5)
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
        if bg_current == Other.home:
            $ Other.recent_history.append("_angry")
            call are_girls_angry
        call remove_girl (Other)
    if AloneCheck(Girl) and Girl.taboo == 20:

        $ Girl.taboo = 0
        $ taboo = 0
    if line:

        "[line]."
        $ line = 0
    return

label Sex_Over(Clothes = True, Girls = None):
    call stop_all_actions

    if Girls in all_Girls:
        $ temp_Girls = [Girls]
    else:
        $ temp_Girls = all_Girls[:]
        $ renpy.random.shuffle(temp_Girls)

    while temp_Girls:
        if temp_Girls[0].location == bg_current:
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

    if Girls == Partner and Girls in all_Girls:
        call shift_focus (Girls)

    $ Girls = 0

    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        call reset_position(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    if Clothes:
        $ line = None

        python:
            for G in all_Girls:
                if G.location == bg_current:
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

    call Get_Dressed
    call checkout(total = True)

    return

label SkipTo(Girl=focused_Girl):

    $ Girl = check_girl(Girl)
    if Player.primary_action == "blowjob":
        call expression Girl.tag + "_BJ_Cycle"
    elif Player.primary_action == "handjob":
        call expression Girl.tag + "_HJ_Cycle"
    elif Player.primary_action == "titjob":
        call expression Girl.tag + "_TJ_Cycle"
    elif Player.primary_action == "kiss":
        call KissCycle (Girl)
    elif Player.primary_action == "fondle_breasts":
        call expression Girl.tag + "_FB_Cycle"
    elif Player.primary_action == "suck_breasts":
        call expression Girl.tag + "_SB_Cycle"
    elif Player.primary_action == "fondle_thighs":
        call expression Girl.tag + "_FT_Cycle"
    elif Player.primary_action == "fondle_pussy":
        call expression Girl.tag + "_FP_Cycle"
    elif Player.primary_action == "eat_pussy":
        call expression Girl.tag + "_LP_Cycle"
    elif Player.primary_action == "fondle_ass":
        call expression Girl.tag + "_FA_Cycle"
    elif Player.primary_action == "finger_ass":
        call expression Girl.tag + "_IA_Cycle"
    elif Player.primary_action == "eat_ass":
        call expression Girl.tag + "_LA_Cycle"
    elif Player.primary_action == "sex":
        call expression Girl.tag + "_SexCycle"
    elif Player.primary_action == "hotdog":
        call expression Girl.tag + "_HotdogCycle"
    elif Player.primary_action == "anal":
        call expression Girl.tag + "_AnalCycle"
    elif Player.primary_action == "dildo_pussy":
        call expression Girl.tag + "_DP_Cycle"
    elif Player.primary_action == "dildo_ass":
        call expression Girl.tag + "_DA_Cycle"
    elif Player.primary_action == "striptease":
        call Group_Strip_End
    elif Player.primary_action == "masturbation":
        $ Girl.remaining_actions -= 1
        $ Girl.action_counter["masturbation"] += 1
    elif Player.primary_action == "lesbian":
        call Les_Cycle (Girl)
    else:
        "That's odd, tell Oni how you got here, Close [Girl.name] [Player.primary_action]."
    return

label clear_stack:
    $ stack_depth = renpy.call_stack_depth()

    while stack_depth > 0:
        $ stack_depth -= 1

        $ renpy.pop_call()

    return

label Girl_TightsRipped(Girl=0, Count=0):
    if Girl not in all_Girls:
        return

    if Girl.outfit["hose"] == "_tights":
        $ Count = 1
        $ Girl.outfit["hose"] = "_ripped_tights"
        $ Girl.change_face("_angry")
    elif Girl.outfit["hose"] == "_pantyhose":
        $ Count = 1
        $ Girl.outfit["hose"] = "_ripped_pantyhose"
        $ Girl.change_face("_angry")
    else:

        return

    if "_ripped_tights" in Girl.inventory or "_ripped_pantyhose" in Girl.inventory:

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
            $ Girl.eyes = "_down"
            ch_l "Oh, they got torn."
            $ Girl.eyes = "_normal"
        elif Girl == JeanX:
            ch_j "Ugh, new ones will be a pain to find."
        elif Girl == StormX:
            ch_s "It appears these are not fit for combat."

    if Count:

        if not Girl.outfit["bottom"] and Girl.outfit["underwear"] != "_shorts":
            if Girl == StormX and StormX in Rules:

                pass
            elif Girl.outfit["underwear"]:
                if Girl.seen_underwear:
                    $ Count = 3 if not approval_check(Girl, 600) else Count
                else:
                    $ Girl.seen_underwear = 1
                    $ Count = 3 if not approval_check(Girl, 900) else Count
                $ Girl.change_stat("lust", 60, 2)
            else:
                if Girl.seen_pussy:
                    $ Count = 3 if not approval_check(Girl, 900) else Count
                else:
                    call Rogue_First_Bottomless
                    $ Count = 3 if not approval_check(Girl, 1400) else Count

        if Count != 3:
            $ Girl.add_word(1,"ripped","ripped")

        if Count == 2:

            menu:
                extend ""
                "I think those look really good on you.":
                    $ Girl.change_face("_smile", 1)
                    $ Girl.inventory.append(Girl.outfit["hose"])
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

                    $ Girl.change_face("_bemused")
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
                $ Girl.change_face("_sexy", 1)
                ch_e "This might cause a bit of a stir, I should probably change. . ."
            elif Girl == LauraX:
                $ Girl.change_face("_perplexed", 0)
                ch_l "I guess I should change into something else."
            elif Girl == JeanX:
                ch_j "I'm going to get changed though. . ."
            elif Girl == StormX:
                $ Girl.change_face("_bemused", 0)
                ch_s "I really probably should change."
            $ Girl.blushing = "_blush1"
            call remove_girl (Girl)
            $ Girl.change_outfit()

    return
