init python:

    def check_girl(Girl, local = False):
        if Girl in all_Girls and (not local or Player.location == Check.location):
            return Girl
        elif Player.location == Player.focused_Girl.location:
            return Player.focused_Girl
        else:
            for Girl in all_Girls:
                if Player.location == Girl.location:
                    Player.focused_Girl = Girl

                    return Girl

    def approval_check(Girl, T = 1000, flavor = "LOI", spread = 150, temp_modifier = 1, taboo_modifier = 0, cologne = True, Bonus = 0, Loc = 0, Check=0, Alt=[[], 0]):
        while Alt[0]:
            if Girl in Alt[0]:
                T = Alt[1] if Alt[1] else T

            Alt[0].remove(Alt[0][0])

        L = Girl.love
        O = Girl.obedience
        I = Girl.inhibition

        local_taboo = Girl.taboo
        Loc = Girl.location if not Loc else Loc

        if Girl == JeanX and (O <= 800 or JeanX.taboo):

            I = (I - JeanX.IX)

        if Loc == Player.location and cologne:
            if Girl == LauraX:
                if "mandrill" in Player.traits:
                    if L <= 400:
                        L += 600
                    else:
                        L = 1200
                    if "drugged" not in Girl.traits:
                        Girl.traits.append("drugged")
                elif "purple" in Player.traits:
                    if O <= 400:
                        O += 600
                    else:
                        O = 1200
                    if "drugged" not in Girl.traits:
                        Girl.traits.append("drugged")
                elif "corruption" in Player.traits:
                    if I <= 400:
                        I += 600
                    else:
                        I = 1200
                    if "drugged" not in Girl.traits:
                        Girl.traits.append("drugged")
            else:
                if "mandrill" in Player.traits:
                    if L <= 500:
                        L += 500
                    else:
                        L = 1000
                elif "purple" in Player.traits:
                    if O <= 500:
                        O += 500
                    else:
                        O = 1000
                elif "corruption" in Player.traits:
                    if I <= 500:
                        I += 500
                    else:
                        I = 1000

        if flavor == "LOI":
            local_taboo *= 10
            Localapproval_bonus = approval_bonus*10
        elif flavor == "LO":
            I = 0
            local_taboo = local_taboo*6
            Localapproval_bonus = approval_bonus*6
        elif flavor == "OI":
            L = 0
            local_taboo = local_taboo*6
            Localapproval_bonus = approval_bonus*6
        elif flavor == "LI":
            O = 0
            local_taboo = local_taboo*6
            Localapproval_bonus = approval_bonus*6
        elif flavor == "L":
            O = 0
            I = 0
            local_taboo = local_taboo*3
            Localapproval_bonus = approval_bonus*3
        elif flavor == "O":
            L = 0
            I = 0
            local_taboo = local_taboo*3
            Localapproval_bonus = approval_bonus*3
        elif flavor == "I":
            O = 0
            L = 0
            local_taboo = local_taboo*3
            Localapproval_bonus = approval_bonus*3
        else:
            local_taboo = local_taboo*10
            Localapproval_bonus = approval_bonus*10

        taboo_modifier = 0 if taboo_modifier <= 0 else taboo_modifier

        if Check:
            return (L + O + I + Bonus + (temp_modifier*Localapproval_bonus) - (taboo_modifier*local_taboo))

        if (L + O + I + Bonus + (temp_modifier*Localapproval_bonus) - (taboo_modifier*local_taboo)) >= (T + (2*spread)):
            return 3
        elif (L + O + I + Bonus + (temp_modifier*Localapproval_bonus) - (taboo_modifier*local_taboo)) >= (T + spread):
            return 2
        elif (L + O + I + Bonus + (temp_modifier*Localapproval_bonus) - (taboo_modifier*local_taboo)) >= T:
            return True
        else:
            return False

    def AloneCheck(Girl):
        for G in all_Girls:
            if G != Girl and G.location == Player.location:
                return False

        return True

label check_who_is_present(location = Player.location):
    $ Present = Player.Party[:] if Player.Party else []

    python:
        for G in all_Girls:
            if G not in Player.Party:
                if G not in Present and G.location == location:
                    Present.append(G)
                elif G in Present and G.location != location:
                    Present.remove(G)

        for G in Present:
            if G in Nearby:
                Nearby.remove(G)

    if Present and Player.focused_Girl not in Present:
        $ renpy.random.shuffle(Present)

        call shift_focus(Present[0])

    return

label check_taboo(Character):
    if Character.location in bedrooms:
        $ Character.taboo = 0
    elif Character.location in ["bg_classroom", "bg_study"]:
        if time_index > 2:
            $ Character.taboo = 20
        elif time_index == 2 or weekday >= 5:
            $ Character.taboo = 30
        else:
            $ Character.taboo = 40
    elif Character.location == "bg_dangerroom":
        if time_index > 2:
            $ Character.taboo = 20
        else:
            $ Character.taboo = 30
    elif Character.location in ["bg_campus", "bg_pool"]:
        if time_index > 2:
            $ Character.taboo = 20
        else:
            $ Character.taboo = 40
    elif Character.location == "bg_showerroom":
        $ Character.taboo = 20
    else:
        $ Character.taboo = 40

    if door_locked:
        $ Character.taboo -= 10 if Character.taboo >= 10 else 0

    python:
        if Character != Player:
            for G in all_Girls:
                if G != Character and Character.location == G.location and Character.likes[G.tag] <= 700 and not (Character in Player.Harem and G in Player.Harem):
                    Character.taboo = 20 if Character.taboo < 20 else Character.taboo

            if Character.taboo > taboo and Character.location == Player.location:
                taboo = Character.taboo

    return

label are_girls_angry:
    $ multiple = False

    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        if temp_Girls[0].location == Player.location and "angry" in temp_Girls[0].recent_history:
            if Player.location == temp_Girls[0].home:
                if temp_Girls[0] == RogueX:
                    ch_r "You should get out, I'm fix'in ta throw down."
                elif temp_Girls[0] == KittyX:
                    ch_k "You should get out of here, I can't even look at you right now."
                elif temp_Girls[0] == EmmaX:
                     ch_e "You should leave, or do you want to test me?"
                elif temp_Girls[0] == LauraX:
                    ch_l "You should leave."
                elif temp_Girls[0] == JeanX:
                    ch_j "Out, NOW!"
                elif temp_Girls[0] == StormX:
                    ch_s "Out!"
                elif temp_Girls[0] == JubesX:
                    ch_v "Get out!"

                $ Player.location = "bg_campus"

                jump reset_location
            else:
                if multiple:
                    ". . . and so does [temp_Girls[0].name]."
                else:
                    "[temp_Girls[0].name] storms off."

                    if temp_Girls[0] == StormX:
                        ". . . so to speak."

                    call remove_Girl(temp_Girls[0])

                    $ multiple = True

        $ temp_Girls.remove(temp_Girls[0])

    return

label check_favorite_actions(Girl = None):
    if Girl:
        $ temp_Girls = [Girl]
    else:
        $ temp_Girls = active_Girls[:]

    python:
        for G in temp_Girls:
            pussy_count = 0
            ass_count = 0
            fondle_count = 0

            handjob_count = G.action_counter["handjob"]
            footjob_count = G.action_counter["footjob"]
            titjob_count = G.action_counter["titjob"]
            blowjob_count = G.action_counter["blowjob"]

            for action in all_actions:
                if action in pussy_actions:
                    pussy_count += G.action_counter[action]

                if action in ass_actions:
                    ass_count += G.action_counter[action]

                if action in fondle_actions:
                    fondle_count += G.action_counter[action]

            if G.player_favorite_action and approval_check(character, 1500):
                if G.player_favorite_action == "handjob":
                    handjob_count += 20
                elif G.player_favorite_action == "footjob":
                    footjob_count += 20
                elif G.player_favorite_action == "titjob":
                    titjob_count += 20
                elif G.player_favorite_action == "blowjob":
                    blowjob_count += 20
                elif G.player_favorite_action == "sex":
                    pussy_count += 20
                elif G.player_favorite_action == "anal":
                    ass_count += 20
                else:
                    fondle_count += 20
            elif G.player_favorite_action and approval_check(character, 800):
                if G.player_favorite_action == "handjob":
                    handjob_count += 5
                elif G.player_favorite_action == "footjob":
                    footjob_count += 5
                elif G.player_favorite_action == "titjob":
                    titjob_count += 5
                elif G.player_favorite_action == "blowjob":
                    blowjob_count += 5
                elif G.player_favorite_action == "sex":
                    pussy_count += 5
                elif G.player_favorite_action == "anal":
                    ass_count += 5
                else:
                    fondle_count += 5

            total = ass_count + pussy_count + blowjob_count + titjob_count + handjob_count + footjob_count + fondle_count + G.action_counter["kiss"]

            if total <= 0:
                D20F = 999
            else:
                D20F = renpy.random.randint(1, total)

            if D20F <= ass_count:
                if G.action_counter["anal"] >= 5:
                    favorite_action = "anal"
                elif G.action_counter["eat_ass"] >= 5:
                    favorite_action = "eat_ass"
                else:
                    favorite_action = "finger_ass"
            elif D20F <= ass_count + pussy_count:
                if G.action_counter["sex"] >= 5:
                    favorite_action = "sex"
                elif G.action_counter["eat_pussy"] >= 5:
                    favorite_action = "eat_pussy"
                else:
                    favorite_action = "fondle_pussy"
            elif D20F <= ass_count + pussy_count + blowjob_count:
                favorite_action = "blowjob"
            elif D20F <= ass_count + pussy_count + blowjob_count + titjob_count:
                favorite_action = "titjob"
            elif D20F <= ass_count + pussy_count + blowjob_count + titjob_count + footjob_count + handjob_count:
                favorite_action = "footjob"
            elif D20F <= ass_count + pussy_count + blowjob_count + titjob_count + footjob_count + handjob_count:
                favorite_action = "handjob"
            elif D20F <= ass_count + pussy_count + blowjob_count + titjob_count + footjob_count + handjob_count + fondle_count:
                D20F = renpy.random.randint(1, 20)

                if D20F >= 15 and G.action_counter["hotdog"]:
                    favorite_action = "hotdog"
                elif D20F >= 10 and G.action_counter["suck_breasts"]:
                    favorite_action = "suck_breasts"
                elif D20F >= 5 and G.action_counter["fondle_breasts"]:
                    favorite_action = "fondle_breasts"
                else:
                    favorite_action = "fondle_thighs"
            else:
                favorite_action = "kiss"

            G.favorite_action = favorite_action

    return

label who_likes_who(Check = 70, D20 = 0):
    $ D20 = renpy.random.randint(0, 1) if not D20 else D20

    python:
        for GA in all_Girls:
            for GB in all_Girls:
                if GA != GB and GA.location == GB.location:
                    if GA.location == "bg_classroom":
                        GA.check_if_likes(GB, 700, 1, 1)
                    elif GA.location == "bg_dangerroom":
                        GA.check_if_likes(GB, 700, 1 + D20, 1)
                    elif GA.location == "bg_showerroom":
                        if GA == EmmaX:
                            GA.check_if_likes(GB, 900, 3, 1)
                        elif GB in [EmmaX, StormX] and GA != LauraX:
                            GA.check_if_likes(GB, 900, 3, 1)
                        else:
                            GA.check_if_likes(GB, 900, 2, 1)
                    else:
                        GA.check_if_likes(GB, Check, D20, 1)

    return

label check_addiction:
    $ addicted_Girls = active_Girls[:]
    $ renpy.random.shuffle(addicted_Girls)

    if JubesX in addicted_Girls and JubesX.addiction >= 40 and JubesX.resistance:
        $ addicted_Girls.remove(JubesX)

        if "sunshine" not in JubesX.history or "addiction" in JubesX.daily_history:
            pass
        elif Player.location == JubesX.home or Player.location == "bg_player":
            if not JubesX.resistance:
                call addiction_event(JubesX)
            else:
                call addiction_fix(JubesX)
        else:
            if "asked_to_meet" in JubesX.daily_history or JubesX not in Player.Phonebook:
                pass
            elif "asked_to_meet" in JubesX.daily_history and JubesX.addiction >= 60:
                "[JubesX.name] texts you. . ."

                JubesX.voice "I know I asked to meet you in your room earlier, but I really need a fix."

                $ Player.add_word(1,"asked_for_fix", 0, 0, 0)
                $ JubesX.add_word(1,"asked_to_meet", "asked_to_meet", 0, 0)

                call return_to_room

                return
            else:
                "[JubesX.name] texts and asks if you could get her a fix later."

                $ JubesX.add_word(1,"asked_to_meet", "asked_to_meet", 0, 0)

                call return_to_room

                return

    while addicted_Girls:
        if "locked" in Player.traits and addicted_Girls[0].location != Player.location:
            pass
        elif "asked_for_fix" in Player.daily_history and "asked_to_meet" not in addicted_Girls[0].daily_history:
            pass
        elif addicted_Girls[0].event_happened[3]:
            pass
        elif "angry" not in addicted_Girls[0].recent_history and "addiction" not in addicted_Girls[0].daily_history and addicted_Girls[0].remaining_actions >= 1:
            if (addicted_Girls[0].addiction >= 60 or (addicted_Girls[0].addiction >= 40 and addicted_Girls[0] == JubesX)) and addicted_Girls[0].resistance:
                if Player.location == addicted_Girls[0].home or Player.location == "bg_player":
                    call addiction_fix(addicted_Girls[0])
                else:
                    if "asked_to_meet" in addicted_Girls[0].recent_history or addicted_Girls[0] not in Player.Phonebook:
                        pass
                    elif "asked_to_meet" in addicted_Girls[0].daily_history and addicted_Girls[0].addiction >= 80:
                        "[addicted_Girls[0].name] texts you. . ."
                        addicted_Girls[0].voice "I know I asked to meet you in your room earlier, but I'm serious, this is important."

                        $ Player.add_word(1,"asked_for_fix", 0, 0, 0)

                        $ addicted_Girls[0].add_word(1,"asked_to_meet", "asked_to_meet", 0, 0)

                        call return_to_room

                        return
                    else:
                        "[addicted_Girls[0].name] texts and asks if you could meet her in your room later."

                        $ addicted_Girls[0].add_word(1,"asked_to_meet", "asked_to_meet", 0, 0)

                        call return_to_room

                        return
            elif addicted_Girls[0].resistance:
                pass
            elif addicted_Girls[0] == JubesX and addicted_Girls[0].addiction < 50:
                pass
            elif (addicted_Girls[0].addiction >= 35 and not addicted_Girls[0].event_happened[1]) or (addicted_Girls[0].addiction >= 60 and addicted_Girls[0].event_happened[1] <= 2) or addicted_Girls[0].addiction >= 90:
                if Player.location == addicted_Girls[0].home or Player.location == "bg_player":
                    call addiction_event(addicted_Girls[0])
                else:
                    if "asked_to_meet" in addicted_Girls[0].recent_history or addicted_Girls[0] not in Player.Phonebook:
                        pass
                    elif "asked_to_meet" in addicted_Girls[0].daily_history and addicted_Girls[0].addiction >= 80:
                        "[addicted_Girls[0].name] texts you. . ."
                        addicted_Girls[0].voice "I know I asked to meet you in your room earlier, but I'm serious, this is important."

                        $ Player.add_word(1,"asked_for_fix", 0, 0, 0)

                        $ addicted_Girls[0].add_word(1,"asked_to_meet", "asked_to_meet", 0, 0)

                        call return_to_room

                        return
                    else:
                        "[addicted_Girls[0].name] texts and asks if you could meet her in your room later."

                        $ addicted_Girls[0].add_word(1,"asked_to_meet", "asked_to_meet", 0, 0)

                        call return_to_room

                        return

        $ addicted_Girls.remove(addicted_Girls[0])

    return

label dildo_check(Girl):
    if "dildo" in Player.inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in Girl.inventory:
        "You ask [Girl.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."

        return "not_found"

    return "found"

label vibrator_check(Girl):
    if "vibrator" in Player.inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in Girl.inventory:
        "You ask [Girl.name] to get out her vibrator."
    else:
        "You don't have one of those on you."

        return "not_found"

    return "found"

label check_if_cheated:
    $ temp_Girls = all_Girls[:]
    $ renpy.random.shuffle(temp_Girls)

    while temp_Girls:
        if "locked" in Player.traits and temp_Girls[0].location != Player.location:
            pass
        else:
            $ temp_Girls2 = all_Girls[:]

            while temp_Girls2:
                if "meet girl" in Player.daily_history:
                    return
                elif temp_Girls[0] in Player.Harem:
                    if "saw with " + temp_Girls2[0].tag in temp_Girls[0].traits:
                        if temp_Girls[0] in Player.Harem and temp_Girls2[0] in Player.Harem:
                            $ temp_Girls[0].drain_word("saw with "+temp_Girls2[0].tag, 0, 0, 1)
                        elif temp_Girls[0] in Player.Harem and temp_Girls2[0].tag + "_Yes" in Player.traits:
                            $ temp_Girls[0].drain_word("saw with "+temp_Girls2[0].tag, 0, 0, 1)
                        elif Player.location == "bg_player" or Player.location == temp_Girls[0].home:
                            call Cheated (temp_Girls[0], temp_Girls2[0])

                            $ renpy.pop_call()

                            return

                $ temp_Girls2.remove(temp_Girls2[0])

        $ temp_Girls.remove(temp_Girls[0])

    return

label check_if_shared:
    $ temp_Girls = all_Girls[:]
    $ temp_Girls.remove(StormX)

    while temp_Girls:
        if temp_Girls[0] in Player.Harem:
            $ temp_Girls2 = all_Girls[:]
            $ temp_Girls2.remove(StormX)

            while temp_Girls2:
                if "ask " + temp_Girls2[0].tag in temp_Girls[0].traits:
                    if temp_Girls[0] in Player.Harem and temp_Girls2[0] in Player.Harem:
                        $ temp_Girls[0].drain_word("ask "+temp_Girls2[0].tag, 0, 0, 1)
                    else:
                        call Share(temp_Girls[0], temp_Girls2[0])

                        $ renpy.pop_call()

                        return

                $ temp_Girls2.remove(temp_Girls2[0])

        $ temp_Girls.remove(temp_Girls[0])

    return
