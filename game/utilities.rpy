init python:

    def CallHolder(Value, Color, XPOS):
        global number_of_holders

        number_of_holders += 1 if number_of_holders < 10 else -9

        renpy.show_screen("StatHolder"+str(number_of_holders), Value, Color, XPOS)

        return

transform StatAnimation(Timer, XPOS):
    alpha 0
    pause Timer
    xpos XPOS ypos 0.15 alpha 1
    parallel:
        linear 1 ypos 0.0
    parallel:
        pause .3
        linear .3 alpha 0

screen StatGraphic(Value, Color, Timer, XPOS):
    showif Value > 0:
        text "+[Value]" size 30 color Color at StatAnimation(Timer, XPOS)
    else:
        text "[Value]" size 30 color Color at StatAnimation(Timer, XPOS)

screen StatHolder1(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.0, XPOS-30)

    timer 0.6 action Hide("StatHolder1")
screen StatHolder2(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.1, XPOS)

    timer 0.7 action Hide("StatHolder2")
screen StatHolder3(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.2, XPOS+30)

    timer 0.8 action Hide("StatHolder3")
screen StatHolder4(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.3, XPOS-30)

    timer 0.9 action Hide("StatHolder4")
screen StatHolder5(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.4, XPOS)

    timer 1.0 action Hide("StatHolder5")
screen StatHolder6(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.5, XPOS+30)

    timer 1.1 action Hide("StatHolder6")
screen StatHolder7(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.6, XPOS-30)

    timer 1.2 action Hide("StatHolder7")
screen StatHolder8(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.7, XPOS)

    timer 1.3 action Hide("StatHolder8")
screen StatHolder9(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.8, XPOS+30)

    timer 1.4 action Hide("StatHolder9")
screen StatHolder10(Value, Color, XPOS):
    use StatGraphic(Value, Color, 0.9, XPOS-30)

    timer 1.5 action Hide("StatHolder10")

label Round10(BO=[], Occupant=0):

    if time_index >= 3:
        call Sleepover
        return



    if bg_current not in PersonalRooms or bg_current == "bg_player":

        call Wait
        return


    $ BO = all_Girls[:]
    while BO:

        if BO[0].home == bg_current:
            $ Occupant = BO[0]
            $ BO = [1]
        $ BO.remove(BO[0])

    if not Occupant:

        call Wait
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

    call Wait

    call Girls_Location

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
        $ bg_current == "bg_campus"
        jump Misplaced
    return




label checkout(Total=0, BO=[]):


    $ BO = all_Girls[:]
    while BO:
        $ BO[0].love = 1000 if BO[0].love > 1000 else BO[0].love
        $ BO[0].obedience = 1000 if BO[0].obedience > 1000 else BO[0].obedience
        $ BO[0].inhibition = 1000 if BO[0].inhibition > 1000 else BO[0].inhibition
        $ BO[0].lust = 99 if BO[0].lust > 99 else BO[0].lust

        $ BO[0].love = 0 if BO[0].love < 0 else BO[0].love
        $ BO[0].obedience = 0 if BO[0].obedience < 0 else BO[0].obedience
        $ BO[0].inhibition = 0 if BO[0].inhibition < 0 else BO[0].inhibition
        $ BO[0].lust = 0 if BO[0].lust < 0 else BO[0].lust

        $ BO[0].remaining_actions = BO[0].max_actions if BO[0].remaining_actions > BO[0].max_actions else BO[0].remaining_actions
        $ BO[0].remaining_actions = 0 if BO[0].remaining_actions < 0 else BO[0].remaining_actions

        $ BO[0].addiction = 100 if BO[0].addiction > 100 else BO[0].addiction
        $ BO[0].addiction = 0 if BO[0].addiction < 0 else BO[0].addiction
        $ BO[0].addiction_rate = 10 if BO[0].addiction_rate > 10 else BO[0].addiction_rate
        $ BO[0].addiction_rate = 0 if BO[0].addiction_rate < 0 else BO[0].addiction_rate
        $ BO[0].Thirst = 100 if BO[0].Thirst > 100 else BO[0].Thirst
        $ BO[0].Thirst = 0 if BO[0].Thirst < 0 else BO[0].Thirst

        if BO[0].Forced and BO[0].event_counter["forced"] < 10:
            $ BO[0].event_counter["forced"] += 1
        if BO[0] == LauraX:
            $ LauraX.ScentTimer = 0

        $ BO.remove(BO[0])


    $ Player.focus = 99 if Player.focus > 99 else Player.focus
    $ Player.focus = 0 if Player.focus < 0 else Player.focus
    $ Player.semen = Player.max_semen if Player.semen > Player.max_semen else Player.semen
    $ Player.semen = 0 if Player.semen < 0 else Player.semen

    if Total:
        $ multi_action = 1
        $ Player.drain_word("cockout")
        $ Player.drain_word("nude")
        $ primary_action = 0
        $ offhand_action = 0
        $ girl_offhand_action = 0
        $ second_girl_primary_action = 0
        $ second_girl_offhand_action = 0
        $ position_timer = 100
        $ Partner = 0
        $ Player.focusing = 0
    return




label Wait(Outfit=1, Lights=1, BO=[]):


    show blackscreen onlayer black

    call checkout (1)
    $ Player.XP = 3330 if Player.XP > 3330 else Player.XP

    if time_index < 3:
        $ time_index += 1
    else:

        $ del Party[:]


        $ time_index = 0
        $ Day += 1
        if Weekday < 6:
            $ Weekday += 1
        else:
            $ Weekday = 0
        $ DayofWeek = Week[Weekday]

        if PunishmentX:

            $ Player.cash += int(Player.income / 2)
            if PunishmentX == 1:
                "Your punishment from Xavier has expired."
            $ PunishmentX -= 1
        else:

            $ Player.cash += Player.income



        $ Player.semen = Player.max_semen
        $ Player.spunk = 0
        $ Player.reputation = 0 if Player.reputation < 0 else Player.reputation
        $ Player.reputation += 10 if Player.reputation < 800 else 0
        $ Player.reputation = 1000 if Player.reputation > 1000 else Player.reputation

        $ TotalSEXP = 0


        if "mandrill" in Player.traits:
            $ Player.traits.remove("mandrill")
        if "purple" in Player.traits:
            $ Player.traits.remove("purple")
        if "corruption" in Player.traits:
            $ Player.traits.remove("corruption")
        call Favorite_Actions



        if "halloween" in Player.daily_history:
            if RogueX.hair == "_cosplay":
                if "_evo" in RogueX.daily_history:
                    $ RogueX.hair = "_evo"
                elif "wet" in RogueX.daily_history:
                    $ RogueX.hair = "wet"
            if JeanX.hair == "pony":
                if "short" in JeanX.daily_history:
                    $ JeanX.hair = "short"
                elif "wet" in JeanX.daily_history:
                    $ JeanX.hair = "wet"
            if EmmaX.hair == "_hat":
                $ EmmaX.hair = "wave"
            elif EmmaX.hair == "hat wet":
                $ EmmaX.hair = "wet"
            if StormX.hair == "short":
                if "long" in StormX.daily_history:
                    $ StormX.hair = "long"
                elif "mohawk" in StormX.daily_history:
                    $ StormX.hair = "mohawk"
                elif "wet" in StormX.daily_history:
                    $ StormX.hair = "wet"
                elif "wethawk" in StormX.daily_history:
                    $ StormX.hair = "wethawk"

        $ BO = all_Girls[:]
        while BO:

            if BO[0] in active_Girls and BO[0].location != bg_current:
                $ BO[0].location = BO[0].home
            if BO[0].Todo:
                call Todo (BO[0])
            $ BO[0].Outfit = "sleep"
            $ BO[0].change_outfit("sleep")


            $ BO[0].addiction += BO[0].addiction_rate
            $ BO[0].addiction -= (3*BO[0].resistance)
            if "nonaddictive" in Player.traits:
                $ BO[0].addiction_rate -= 2
                $ BO[0].addiction -= 5
            if "addictive" not in Player.traits:
                $ BO[0].addiction_rate -= BO[0].resistance
                if BO[0] != RogueX and BO[0].addiction_rate >= 3:

                    $ BO[0].addiction_rate -= BO[0].resistance

            $ BO[0].event_counter["forced"] -= 1 if BO[0].event_counter["forced"] > 0 else 0
            if BO[0].event_counter["forced"] > 0:
                $ BO[0].event_counter["forced"] -= 1 if approval_check(BO[0], 1000, "LO") else 0
            $ BO[0].remaining_actions = BO[0].max_actions

            $ BO[0].reputation = 0 if BO[0].reputation < 0 else BO[0].reputation
            $ BO[0].reputation += 10 if BO[0].reputation < 800 else 0
            $ BO[0].reputation = 1000 if BO[0].reputation > 1000 else BO[0].reputation

            $ BO[0].lust -= 5 if BO[0].lust >= 50 else 0
            $ TotalSEXP += BO[0].SEXP

            if BO[0].SEXP >= 15:

                if BO[0].SEXP >= 50:
                    $ BO[0].Thirst += 8 if BO[0].Thirst <= 70 else 4
                elif BO[0].SEXP >= 25:
                    $ BO[0].Thirst += 5 if BO[0].Thirst <= 60 else 2
                else:
                    $ BO[0].Thirst += 3 if BO[0].Thirst <= 50 else 1

                $ BO[0].Thirst -= 5 if BO[0].Break[0] else 0
                $ BO[0].Thirst += 1 if BO[0].lust >= 50 else 0

            if "gonnafap" in BO[0].daily_history and BO[0].location != bg_current:

                $ BO[0].lust = 25
                $ BO[0].Thirst -= int(BO[0].Thirst/2) if BO[0].Thirst >= 50 else int(BO[0].Thirst/4)
            elif "wannafap" in BO[0].daily_history:

                $ BO[0].Thirst += 10 if BO[0].Thirst <= 50 else 5

            $ BO[0].Break[0] -= 1 if BO[0].Break[0] > 0 else 0

            $ del BO[0].spunk[:]

            if "lover" in BO[0].player_petnames and BO[0].love > 800:
                $ BO[0].love += 10
            if "master" in BO[0].player_petnames and BO[0].obedience > 600:
                $ BO[0].obedience += 10
            if "fuck buddy" in BO[0].player_petnames:
                $ BO[0].inhibition += 10

            $ BO[0].SluttyClothes()

            if BO[0] == JeanX:
                if BO[0].love < 1000 and BO[0].StatStore > 0:

                    if BO[0].obedience >= 900:
                        $ BO[0].love += 10
                        $ BO[0].StatStore -= 10
                    elif BO[0].obedience >= 700:
                        $ BO[0].love += 5
                        $ BO[0].StatStore -= 5
                    elif BO[0].obedience >= 500:
                        $ BO[0].love += 1
                        $ BO[0].StatStore -= 1
                if BO[0].reputation <= 800 and "nowhammy" not in JeanX.traits:

                    $ BO[0].reputation = 800

            if "Jeaned" in BO[0].traits:

                $ BO[0].traits.remove("Jeaned")
                $ BO[0].LikeJean = getattr(JeanX,"LikeS"+BO[0].tag)

            $ BO.remove(BO[0])




    $ Player.semen += 1
    $ multi_action = 1
    $ Player.focus -= 5 if Player.focus >= 10 else 0
    $ action_context = 0
    $ current_time = time_options[(time_index)]
    $ Round = 100

    $ del Player.recent_history[:]
    if time_index == 0:
        $ del Player.daily_history[:]
    call Taboo_Level (0)
    call GirlWaitUp


    if time_index == 3:

        call Study_Time
    $ BO = all_Girls[:]
    while BO:


        $ BO[0].remaining_actions += 1 if time_index != 0 else 0

        $ BO[0].session_orgasms = 0
        if BO[0].lust >= 70 or BO[0].Thirst >= 30 or (renpy.random.randint(1, 40) + BO[0].lust)>= 70:

            if "nofap" in BO[0].traits:
                $ BO[0].add_word(1,0,"wannafap",0,0)
            else:
                $ BO[0].add_word(1,0,"gonnafap",0,0)

        if "les" in BO[0].recent_history:
            $ BO[0].Thirst -= int(BO[0].Thirst/2)
            $ BO[0].lust = 20


        $ BO[0].Chat[5] = 0

        $ BO[0].Event[3] -= 1 if BO[0].Event[3] else 0

        $ BO[0].Forced = 0
        if BO[0].location == "bg_classroom" or BO[0].location == "bg_dangerroom" or BO[0].location == "bg_teacher":
            $ BO[0].XP += 10
        elif (bg_current == "bg_classroom" or bg_current == "bg_dangerroom") and BO[0].location == "nearby":
            $ BO[0].XP += 10
        elif BO[0].location == "bg_showerroom":
            call Remove_Girl (BO[0])

        if BO[0] in active_Girls and "met" not in BO[0].history:
            $ active_Girls.remove(BO[0])


        $ BO[0].blushing = ""
        $ BO[0].Water = 0
        $ BO[0].held_item = 0


        $ BO[0].addiction += BO[0].addiction_rate
        $ BO[0].addiction_rate -= BO[0].resistance if BO[0].addiction_rate > 3 else 0


        if BO[0].Taboo and BO[0].Shame and BO[0] in active_Girls:
            if BO[0].location == "bg_dangerroom":
                $ BO[0].Shame -= 10 if BO[0].Shame >=10 else BO[0].Shame
            $ Count = int((BO[0].Taboo*BO[0].Shame) / 200)
            $ BO[0].change_stat("obedience", 90, Count)
            $ BO[0].change_stat("inhibition", 90, Count)
            $ BO[0].reputation -= Count


        $ BO[0].love -= 5*BO[0].recent_history.count("unsatisfied")


        $ del BO[0].recent_history[:]
        if "_angry" in BO[0].daily_history:
            $ BO[0].recent_history.append("_angry")
        if time_index == 0:
            $ del BO[0].daily_history[:]
        elif time_index == 3 and "yesdate" in BO[0].daily_history and "stoodup" not in BO[0].traits:

            $ Player.drain_word("yesdate",0,1)
            $ BO[0].traits.append("stoodup")

        if BO[0].used_to_anal < 2:
            if (BO[0].action_counter["anal"] + BO[0].action_counter["dildo_ass"] + BO[0].Plug) >= 15:
                $ BO[0].used_to_anal = 2
            elif (BO[0].action_counter["anal"] + BO[0].action_counter["dildo_ass"] + BO[0].Plug) >= 3:
                $ BO[0].used_to_anal = 1

        $ BO[0].XP = 3330 if BO[0].XP > 3330 else BO[0].XP
        if BO[0].XP >= BO[0].XP_goal and BO[0].level < 10:
            $ BO[0].XP_goal = int((1.15*BO[0].XP_goal) + 100)
            $ BO[0].level += 1
            $ BO[0].stat_points += 1
            "[BO[0].name]'s leveled up! I bet she has some new tricks to learn."
            if BO[0].level == 10:
                "[BO[0].name]'s reached max level!"
        if BO[0] == LauraX:
            $ BO[0].addiction_rate -= (2*BO[0].resistance) if BO[0].addiction_rate > 5 else 0
        elif BO[0] == JubesX and "met" in JubesX.history:
            $ BO[0].addiction_rate = 2 if BO[0].addiction_rate < 2 else BO[0].addiction_rate
            if "sunshine" not in JubesX.history:

                $ BO[0].addiction = 40 if BO[0].addiction > 40 else BO[0].addiction

        $ BO[0].DefaultFaces()
        $ BO[0].change_face(5)

        $ BO.remove(BO[0])


    call Girls_Schedule

    if Outfit:
        $ BO = all_Girls[:]
        while BO:

            $ BO[0].change_outfit(BO[0].OutfitDay)
            $ BO.remove(BO[0])


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



    call LesCheck


    call checkout
    if time_index < 3:
        hide NightMask onlayer nightmask
    if Lights:
        hide blackscreen onlayer black
    return






label Girls_Schedule(Girls=[], Clothes=1, Location=1, LocTemp=0):




    if not Girls:

        $ Girls = active_Girls[:]
    elif Girls[0] not in all_Girls:
        return
    while Girls:
        if Girls[0] in Party and Clothes != 2 or not Location:

            pass
        elif Clothes != 2 and "sleepover" in Girls[0].traits and time_index == 0:

            pass
        else:
            if (time_index == 0 and Clothes and Round >= 90) or Clothes == 2:

                $ Girls[0].OutfitDay = 0
                if Girls[0].Break[0]:
                    pass
                elif Girls[0].Clothing[Weekday] == 1:
                    $ Girls[0].OutfitDay = "casual1"
                elif Girls[0].Clothing[Weekday] == 2:
                    $ Girls[0].OutfitDay = "casual2"
                elif Girls[0].Clothing[Weekday] == 3 and Girls[0].Custom1[0]:
                    $ Girls[0].OutfitDay = "custom1"
                elif Girls[0].Clothing[Weekday] == 4:
                    $ Girls[0].OutfitDay = "gym"
                elif Girls[0].Clothing[Weekday] == 5 and Girls[0].Custom2[0]:
                    $ Girls[0].OutfitDay = "custom2"
                elif Girls[0].Clothing[Weekday] == 6 and Girls[0].Custom3[0]:
                    $ Girls[0].OutfitDay = "custom3"
                if not Girls[0].OutfitDay:
                    $ Options = ["casual1", "casual2"]
                    if not Girls[0].Break[0]:
                        $ Options.append("custom1") if Girls[0].Custom1[0] == 2 else Options
                        $ Options.append("custom2") if Girls[0].Custom2[0] == 2 else Options
                        $ Options.append("custom3") if Girls[0].Custom3[0] == 2 else Options
                    $ renpy.random.shuffle(Options)
                    $ Girls[0].OutfitDay = Options[0]
                    $ del Options[:]
                $ Girls[0].Outfit = Girls[0].OutfitDay



            $ LocTemp = Girls[0].location
            if Girls[0] not in active_Girls:
                $ LocTemp = "hold"
                $ Girls[0].location = "hold"
            elif Girls[0] in Party or Girls[0].location == "hold":
                pass
            else:
                $ Girls[0].location = Girls[0].Schedule[Weekday][time_index]
                if Girls[0] == JubesX and JubesX.addiction > 60:

                    $ JubesX.location = JubesX.home

            if Girls[0].location != LocTemp and Girls[0] not in Party:

                if LocTemp == bg_current:
                    if approval_check(Girls[0], 1200) and Girls[0].location not in ("bg_classroom","bg_teacher","bg_dangerroom"):

                        $ Girls[0].location = LocTemp
                    else:

                        $ Girls[0].recent_history.append("leaving")
                elif Girls[0].location == bg_current:

                    $ Girls[0].recent_history.append("arriving")
            if Girls[0] in Nearby:
                $ Nearby.remove(Girls[0])
        if Girls[0].location == "bg_teacher":
            call AltClothes (Girls[0], 8)
            $ Girls[0].change_outfit()

        $ Girls.remove(Girls[0])

    return




label Study_Time(BO=[], Studiers=[]):

    $ BO = all_Girls[:]
    while BO:
        if BO[0].location != bg_current and BO[0].location in PersonalRooms:

            $ Studiers.append(BO[0])
        $ BO.remove(BO[0])
    if len(Studiers) < 2:

        return

    $ renpy.random.shuffle(Studiers)
    $ Studiers[0].GLG(Studiers[1],800,5,1)
    $ Studiers[1].GLG(Studiers[0],800,5,1)

    $ Studiers[0].XP += 5
    $ Studiers[1].XP += 5
    return




label Todo(Chr=0):


    if Chr not in all_Girls:
        return

    if Chr == LauraX:
        if "pubes" in Chr.Todo:
            $ Chr.pubes = "_hairy"
            $ Chr.Todo.remove("pubes")

        if "mission" in Chr.Todo:
            $ Chr.PubeC -= 1
            if Chr.PubeC >= 1:
                $ Chr.location = "hold"
            else:
                $ Chr.history.append("dress0")
                $ Chr.Todo.remove("mission")
        if "cleanhouse" in Chr.Todo:

            if LauraX in Player.Harem or not Player.Harem:

                $ LauraX.Event[5] = 2
                $ Chr.Todo.remove("cleanhouse")
            $ LauraX.Event[5] -= 1 if LauraX.Event[5] > 1 else 0
    else:
        if "pubes" in Chr.Todo:
            $ Chr.PubeC -= 1
            if Chr.PubeC >= 1:
                pass
            else:
                $ Chr.pubes = "_hairy"
                $ Chr.Todo.remove("pubes")

    if "shave" in Chr.Todo:
        $ Chr.pubes = "_bare"
        $ Chr.Todo.remove("shave")

    if "hair" in Chr.Todo:
        if StormX.hair == "long":
            $ StormX.hair = "mohawk"
        elif StormX.hair == "wethawk":
            $ StormX.hair = "wet"
        elif StormX.hair == "wet":
            $ StormX.hair = "wethawk"
        else:
            $ StormX.hair = "long"
        $ Chr.Todo.remove("hair")


    if "_ring" in Chr.Todo:
        $ Chr.piercings = "_ring"
        $ Chr.Todo.remove("_ring")
    if "_barbell" in Chr.Todo:
        $ Chr.piercings = "_barbell"
        $ Chr.Todo.remove("_barbell")
    return





label EventCalls(EGirls=[]):
    call Present_Check
    $ D20 = renpy.random.randint(1, 20)
    call Get_Dressed

    if time_index == 2 and "yesdate" in Player.daily_history:
        if bg_current == "bg_campus":
            call DateNight
            $ Player.drain_word("yesdate",0,1)
            return
        else:
            menu:
                "You have a date to get to, head for the square?"
                "Yes":
                    $ renpy.pop_call()
                    jump Campus_Entry
                "No":
                    "Suit yourself. . ."

    if Day < 3 or Round <= 10:

        return


    if JubesX in active_Girls:

        if time_index < 3 and "sunshine" not in JubesX.history and "traveling" in Player.recent_history and bg_current in ("bg_classroom","bg_dangerroom","bg_campus","bg_pool"):
            jump Jubes_Sunshine
            return
        elif "mall" not in Player.history and "sunshine" in JubesX.history and time_index < 3 and JubesX.addiction < 50:
            call Jubes_Mall
            jump Misplaced
        elif not JubesX.Event[1] and JubesX.addiction < 50:

            $ JubesX.addiction += 5



    if KittyX in active_Girls:
        if "Kate" not in KittyX.names and KittyX.inhibition >= 500 and KittyX.location == bg_current:

            call Kitty_Kate
            return
    else:
        if "traveling" in Player.recent_history and "met" not in KittyX.history and bg_current == "bg_classroom":
            jump KittyMeet
            return


    if LauraX in active_Girls:
        pass
    elif "met" not in LauraX.history and "traveling" in Player.recent_history:
        if bg_current == "bg_dangerroom":
            if Day >= 7 and "dress0" not in LauraX.history and "mission" not in LauraX.Todo:
                call LauraMeet
                return


        if time_index < 3 and "met" in KittyX.history:
            if "dress0" in LauraX.history:
                call Laura_Dressup
                return


    if EmmaX in active_Girls:
        if bg_current == "bg_classroom" and time_index == 2 and Weekday in (0,2,4):

            if "traveling" in Player.recent_history and not Party:

                if "classcaught" not in EmmaX.history:

                    jump Emma_Caught_Classroom
                    return
                elif D20 <= 10 and "gonnafap" in EmmaX.daily_history:

                    jump Emma_Caught_Classroom
                    return

            if "detention" in Player.traits and not Party:
                jump Emma_Detention

            if Round >= 70:

                $ EmmaX.location = "bg_classroom"
    else:

        if Day >= 4 and "met" not in EmmaX.history and "traveling" in Player.recent_history and bg_current == "bg_classroom" and Weekday < 5:
            jump EmmaMeet
            return



    if StormX in active_Girls:
        if bg_current == "bg_classroom" and StormX.location == "bg_teacher" and "Peter" in StormX.history and "traveling" in Player.recent_history:

            call Storm_Peter
            return
        if bg_current == "bg_classroom" and time_index == 2 and Weekday in (1,3):
            if "mohawk" not in StormX.history and "traveling" not in Player.recent_history and approval_check(StormX, 200, "I"):
                jump Storm_Hairtalk
                return
            if Round >= 70:

                $ StormX.location = "bg_classroom"
        if time_index == 3 and bg_current == "bg_pool" and "poolnight" in Player.history:
            if "sex friend" not in StormX.player_petnames or (D20 < 5 and "poolnight" not in Player.recent_history):

                call Storm_Poolnight
                return


    elif "met" not in StormX.history and "met" in JeanX.history:
        if bg_current == "bg_player" and "attic" not in Player.history and "noise" not in Player.history:

            call StormMeetPrelude
            return
        elif bg_current == "bg_classroom" and "noise" in Player.history and "traveling" in Player.recent_history:

            call StormMeetAsk
            return
        elif bg_current == "bg_player" and time_index < 2 and 0 < StormX.Break[0] <= 101 and "traveling" in Player.recent_history:

            call StormMeetWater
            jump Misplaced




    if "goto" in Player.recent_history:
        $ Player.recent_history.remove("goto")
        return


    if "locked" in Player.traits:

        return

    if "micro" not in Player.history and Day > 13:

        call Microtransactions_Intro




    if "fix" not in Player.daily_history:
        call AddictCheck

    if bg_current == "bg_player":

        $ EGirls = active_Girls[:]
        while EGirls and "asked meet" not in EGirls[0].daily_history:

            if "asked meet" in EGirls[0].daily_history:
                $ EGirls = ["x",EGirls[0]]
            $ EGirls.remove(EGirls[0])

    if not EGirls:



        call ShareCheck




        call CheatCheck


        call JumperCheck





        if time_index >= 2 and "fapcall" not in Player.daily_history:

            $ EGirls = active_Girls[:]
            $ renpy.random.shuffle(EGirls)
            while EGirls:
                if "wannafap" in EGirls[0].daily_history:

                    call CalltoFap (EGirls[0])
                    if not EGirls:
                        return
                $ EGirls.remove(EGirls[0])


    $ EGirls = active_Girls[:] if not EGirls else EGirls
    $ renpy.random.shuffle(EGirls)


    while EGirls:
        if "relationship" not in EGirls[0].daily_history:
            if "stoodup" in EGirls[0].traits:
                call Date_Stood_Up (EGirls[0])
                return
            if EGirls[0].Break[0] or "_angry" in EGirls[0].daily_history:

                pass
            elif not EGirls[0].Event[0] and EGirls[0].event_counter["sleepover"] >= 5:
                if EGirls[0].location == bg_current or EGirls[0] in Party:
                    call expression EGirls[0].tag + "_Key"
                    return
            elif EGirls[0] == JubesX:
                pass
            elif EGirls[0] == JeanX:
                if bg_current != "bg_classroom":
                    if JeanX.obedience >= 500 and "sir" not in JeanX.history:
                        call Jean_Sub
                    elif JeanX.obedience >= 800 and "master" not in JeanX.history:
                        call Jean_Master
                    elif JeanX.love >= 500 and "sexfriend" not in JeanX.history:
                        call Jean_Like
                    elif JeanX.love >= 800 and JeanX.obedience >= 600 and not JeanX.Event[5]:
                        call Jean_Love
                    elif "daddy" not in JeanX.player_petnames and approval_check(JeanX, 750, "L"):
                        if (bg_current == EGirls[0].home or bg_current == "bg_player") and EGirls[0].location == bg_current:
                            call Jean_Daddy
                    return
            elif "boyfriend" not in EGirls[0].player_petnames and EGirls[0].love >= 800 and EGirls[0].Event[5] != 20 and EGirls[0].tag + "No" not in Player.traits:


                if EGirls[0] == LauraX and LauraX.Event[5] == 3:

                    call Laura_Cleanhouse
                elif Player.Harem and EGirls[0].tag + "Yes" not in Player.traits:
                    call Poly_Start (EGirls[0])
                elif bg_current == EGirls[0].home or bg_current == "bg_player":
                    call expression EGirls[0].tag + "_BF"
                else:
                    call AskedMeet (EGirls[0], "_bemused")
                return
            elif "lover" not in EGirls[0].player_petnames and EGirls[0].love >= 950 and EGirls[0].Event[6] < 15:

                if bg_current == EGirls[0].home or bg_current == "bg_player":
                    call expression EGirls[0].tag + "_Love"
                else:
                    call AskedMeet (EGirls[0], "_bemused")
                return
            elif "sir" not in EGirls[0].history and "sir" not in EGirls[0].player_petnames and EGirls[0].obedience >= 500:
                if bg_current == EGirls[0].home or bg_current == "bg_player":
                    call expression EGirls[0].tag + "_Sub"
                else:
                    call AskedMeet (EGirls[0], "_bemused")
                return
            elif "master" not in EGirls[0].history and "master" not in EGirls[0].player_petnames and EGirls[0].obedience >= 850 and EGirls[0].Event[8] < 2:

                if bg_current == EGirls[0].home or bg_current == "bg_player":
                    call expression EGirls[0].tag + "_Master"
                else:
                    call AskedMeet (EGirls[0], "_bemused")
                return
            elif "daddy" not in EGirls[0].player_petnames and approval_check(EGirls[0], 750, "L") and approval_check(EGirls[0], 500, "O") and approval_check(EGirls[0], 500, "I"):
                if (bg_current == EGirls[0].home or bg_current == "bg_player") and EGirls[0].location == bg_current:
                    call expression EGirls[0].tag + "_Daddy"
                return
            elif "sex friend" not in EGirls[0].player_petnames and EGirls[0].inhibition >= 500:
                if EGirls[0] == EmmaX:
                    if bg_current == "bg_classroom" and (EmmaX.location == "bg_teacher" or EmmaX.location == "bg_classroom") and time_index == 2:
                        call Emma_Sexfriend
                        return
                elif EGirls[0] == StormX:
                    if StormX.Event[9]:
                        pass
                    elif "traveling" in Player.recent_history and time_index < 2:
                        call Storm_Sexfriend
                        return
                elif bg_current == EGirls[0].home or bg_current == "bg_player":
                    call expression EGirls[0].tag + "_Sexfriend"
                    return
                elif EGirls[0] in Player.Harem and EGirls[0].location == bg_current:
                    call expression EGirls[0].tag + "_Sexfriend"
                    return
                elif EGirls[0] == LauraX:
                    call expression EGirls[0].tag + "_Sexfriend"
                    return



            elif "fuck buddy" not in EGirls[0].player_petnames and EGirls[0].inhibition >= 800:
                if EGirls[0] == RogueX:
                    if bg_current != EGirls[0].location:
                        call expression EGirls[0].tag + "_Fuckbuddy"
                        return
                elif EGirls[0] == LauraX:
                    if bg_current == "bg_player" and EGirls[0].location != bg_current:
                        call expression EGirls[0].tag + "_Fuckbuddy"
                        return
                elif EGirls[0] == StormX:
                    if bg_current == "bg_classroom" and time_index == 2 and Weekday in (1,3):
                        call Storm_Fuckbuddy
                        return
                elif bg_current == EGirls[0].home or bg_current == "bg_player":
                    call expression EGirls[0].tag + "_Fuckbuddy"
                    return
                elif EGirls[0] in Player.Harem and EGirls[0].location == bg_current:
                    call expression EGirls[0].tag + "_Fuckbuddy"
                    return



        $ EGirls.remove(EGirls[0])


    if "fix" in Player.daily_history:
        call AddictCheck


label QuickEvents(EGirls=[]):

    $ Options = []
    call Present_Check

    $ EGirls = all_Girls[:]
    $ renpy.random.shuffle(EGirls)
    while EGirls:
        if EGirls[0].location == bg_current:
            if EGirls[0].lust >= 90:
                $ EGirls[0].blushing = "_blush1"
                $ EGirls[0].grool = 2
            elif EGirls[0].lust >= 60:
                $ EGirls[0].blushing = "_blush1"
                $ EGirls[0].grool = 1
            else:
                $ EGirls[0].grool = 0


            if Taboo and EGirls[0].lust >= 75:
                if EGirls[0].inhibition > 800 or "exhibitionist" in EGirls[0].traits:
                    "[EGirls[0].name] gets a sly smile on her face and squirms a bit."
                elif EGirls[0].inhibition > 500 and EGirls[0].lust < 90:
                    "[EGirls[0].name] looks a bit flushed and uncomfortable."
                elif bg_current != "bg_showerroom":
                    "[EGirls[0].name] gets an embarrassed look on her face and suddenly leaves the room."

                    call Remove_Girl (EGirls[0])
                    call set_the_scene
                    $ EGirls[0].location = EGirls[0].home if bg_current != EGirls[0].home else "bg_campus"
                    if "nofap" in EGirls[0].traits:
                        $ EGirls[0].add_word(1,0,"wannafap",0,0)
                        call CalltoFap (EGirls[0])
                    else:
                        $ EGirls[0].add_word(1,0,"gonnafap",0,0)
        else:

            if EGirls[0].location == "bg_showerroom" and "showered" in EGirls[0].daily_history:

                $ EGirls[0].location = EGirls[0].Schedule[Weekday][time_index]
                if EGirls[0] == JubesX and JubesX.addiction > 60:

                    $ JubesX.location = JubesX.home
                $ EGirls[0].spunk = []
                $ EGirls[0].change_outfit()

        if EGirls:
            $ EGirls.remove(EGirls[0])
    return



label AskedMeet(Girl=0, Emotion="_bemused", Why=0):

    if "asked meet" not in Girl.daily_history and Girl.location != bg_current:
        $ Girl.change_face(Emotion)
        "[Girl.name] asks if you could meet her in your room later."
        $ Girl.add_word(1,"asked meet","asked meet",0,0)
        $ Player.add_word(1,0,"meet girl",0,0)
        if RTR_Toggle:
            call ReturnToRoom
    return



label ReturnToRoom:

    menu:
        "Return to your room and deal with that?"
        "Yes":
            $ renpy.pop_call()
            $ renpy.pop_call()
            jump Player_Room_Entry
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
                    "You can always just \"Wait.\" This causes you to waste time, but who knows, maybe something interesting will happen."
                    "Of course when it's night time, this becomes \"Sleep.\" You can only sleep in your own room at first, but maybe someone else would let you sleep in her room."
                "Shop":
                    "You can also access the school's fabricator store, where you can order various items to be delivered to your room."
                "Class":
                    "You can always attend classes. These are typically not that interesting, but will raise your XP, and various events might occur in class."
                    "Classes are open during weekday morning and midday periods. You might bump into Rogue there."
                    "You can access the classroom by using \"Leave [[Go to Campus Square].\""
                "Danger Room":
                    "You can also attend a Danger Room training session. These also raise your XP."
                    "The Danger Room is open any time except late at night (students need their sleep)."
                    "You can access the Danger Room by using \"Leave [[Go to Campus Square].\""
                "Shower":
                    "You can also take a shower, but don't worry, you'll do that off camera automatically if you don't get around to it."
                    "You can access the showers by using \"Leave [[Go to Campus Square].\""
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
jump Tutorial

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
                        jump Player_Room
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
                        call Halloween_Party_Entry
                    "No":
                        return


            "Do some Microtransactions [[locked] (locked)" if "micro" not in Player.history:
                call Microtransactions
            "Do some Microtransactions" if "micro" in Player.history:
                call Microtransactions
            "Visit McCoy's lab to change things about myself.":
                call Hanks_Lab
            "Reset Custom Outfits":
                call Emergency_Clothing_Reset
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
                    "Yes [[current]" if RTR_Toggle:
                        pass
                    "Yes" if not RTR_Toggle:
                        $ RTR_Toggle = 1
                    "No [[current]" if not RTR_Toggle:
                        pass
                    "No" if RTR_Toggle:
                        $ RTR_Toggle = 0
            "Activate Travel Mode" if not TravelMode:
                "This mode causes you to travel directly to adjacent areas, but not directly to more distant ones."
                "If you would prefer to use the default, more \"world map\" style of travel, you can toggle this back off."
                "You can use \"Leave\" to open the location directory."
                $ TravelMode = 1
            "Deactivate Travel Mode" if TravelMode:
                $ TravelMode = 0

            "Press the red button" if False:
                "Huh, wonder what that was about. . ."
            "Never mind.":

                return
    return



label Hanks_Lab(Line=0):
    "This is Professor McCoy's lab. You can do various self-modifications here."
    "The changes will be so seemless, it's almost like nobody will even notice!"
    while True:
        $ Line = 0
        menu:
            "What would you like to do?"
            "Alter skin color":
                menu:
                    "What skin color would you like?"
                    "Green":
                        $ Player.color = "green"
                    "White":
                        $ Player.color = "pink"
                    "Black":
                        $ Player.color = "brown"
                    "Never mind":
                        $ Line = 1
                if not Line:
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
                    call Lastnamer
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
                $ Line = "This is Halloween." if "halloween" in RogueX.history else "no"
                "Rogue: [Line]"
                $ Line = "This is Halloween." if "halloween" in KittyX.history else "no"
                "Kitty: [Line]"
                $ Line = "This is Halloween." if "halloween" in EmmaX.history else "no"
                "Emma: [Line]"
                $ Line = "This is Halloween." if "halloween" in LauraX.history else "no"
                "Laura: [Line]"
                $ Line = "This is Halloween." if "halloween" in JeanX.history else "no"
                "Jean: [Line]"
                $ Line = "This is Halloween." if "halloween" in StormX.history else "no"
                "Storm: [Line]"
                $ Line = 0
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





label Remove_Girl(Girl=0, HideGirl=1, Hold=0, BO=[]):



    if Girl == "All":
        $ Party = []
        $ Nearby = []
        $ Partner = 0
        $ BO = all_Girls[:]
    else:
        while Girl in Party:
            $ Party.remove(Girl)
        while Girl in Present:
            $ Present.remove(Girl)
        while Girl in Nearby:
            $ Nearby.remove(Girl)
        if Partner == Girl:
            $ Partner = 0
        $ BO = [Girl]

    while BO:
        $ BO[0].drain_word("leaving",1,0,0)
        $ BO[0].drain_word("arriving",1,0,0)

        if BO[0].location == bg_current or (bg_current == "bg_classroom" and BO[0].location == "bg_teacher"):
            if Hold and bg_current in ("bg_campus","bg_classroom","bg_dangerroom","bg_pool"):

                if BO[0] not in Nearby:
                    $ Nearby.append(BO[0])
                $ BO[0].location = "nearby"
            elif bg_current == BO[0].home:

                if BO[0] == JubesX and JubesX.addiction >= 60:
                    $ BO[0].location = "bg_showerroom"
                $ BO[0].location = "bg_campus"
                $ Player.drain_word("locked",0,0,1)
            else:

                $ BO[0].location = BO[0].home
                $ Player.drain_word("locked",0,0,1)


        if HideGirl:
            call expression BO[0].tag + "_Hide" pass (1)
        $ BO.remove(BO[0])
    return




label clear_the_room(Character=0, Passive=0, Silent=0, Girls=[], BO=[]):













    $ BO = all_Girls[:]
    $ BO.remove(Character) if Character in all_Girls else BO
    while BO:
        if BO[0].location == bg_current or BO[0] in Party:

            $ Girls.append(BO[0])
        elif BO[0].location == "bg_teacher" and bg_current == "bg_classroom":

            $ Girls.append(BO[0])

        $ BO.remove(BO[0])

    $ Nearby = []

    if not Silent and not Passive:

        if Character.location != bg_current:
            "[Character.name] enters the room."
            $ Character.location = bg_current
        if not Girls:

            if Character in all_Girls:
                call Display_Girl (Character)
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
        elif not Passive and Character != "All":

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
            if Character != "All":

                $ bg_current = Character.home
                $ Character.location = Character.home
                call set_the_scene
                call clear_the_room (Character)
                call Taboo_Level
                if not Silent:
                    "[Character.name] brings you back to her room. . ."
                jump Misplaced
                return
            else:
                $ Girls[0].location = "bg_campus"
        else:
            $ Girls[0].location = Girls[0].home

        if Girls[0] == RogueX:
            hide Rogue_sprite with easeoutright
        elif Girls[0] == KittyX:
            hide Kitty_sprite with easeoutbottom
        elif Girls[0] == EmmaX:
            hide Emma_Sprite with easeoutright
        elif Girls[0] == LauraX:
            hide Laura_Sprite with easeoutright
        elif Girls[0] == JeanX:
            hide Jean_Sprite with easeoutright
        elif Girls[0] == StormX:
            hide Storm_Sprite with easeoutright
        elif Girls[0] == JubesX:
            hide Jubes_Sprite with easeoutright
        $ Girls.remove(Girls[0])
    if Character in all_Girls:
        call Display_Girl (Character)
    call Taboo_Level
    return





label Girls_Location(GirlsNum=0, Change=0, BOptions=[]):






    $ BOptions = all_Girls[:]
    $ renpy.random.shuffle(BOptions)
    while BOptions:

        if "leaving" in BOptions[0].recent_history:
            if "sleepover" in BOptions[0].traits:
                $ BOptions[0].drain_word("sleepover",0,0,1)
            call expression BOptions[0].tag + "_Leave"
            if BOptions[0].location != bg_current:
                if BOptions[0] in Present:
                    $ Present.remove(BOptions[0])
                $ Change = 1
            $ GirlsNum += 1

        if BOptions[0] in Nearby and BOptions[0].location != "nearby":
            $ Nearby.remove(BOptions[0])
        $ BOptions.remove(BOptions[0])





    if Change:

        call set_the_scene (Dress=0)

    $ BOptions = all_Girls[:]
    while BOptions:
        if "arriving" in BOptions[0].recent_history:
            call Girls_Arrive
            return
        $ BOptions.remove(BOptions[0])
    return





label Girls_Arrive(Primary=0, Secondary=0, GirlsNum=0, BO=[]):





    $ Options = []

    call Present_Check
    $ BO = Present[:]
    while BO:

        if "arriving" in BO[0].recent_history and BO[0] not in Party:
            $ GirlsNum += 1
            $ Options.append(BO[0])
        $ BO[0].drain_word("arriving")
        $ BO.remove(BO[0])

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
            call Locked_Door (KittyX)
            if KittyX.location != bg_current:
                $ Primary = 0
            elif Secondary:

                "You hear a \"thump\" as if someone was trying to follow Kitty."
                call Locked_Door (Secondary)
                if Secondary.location != bg_current:
                    $ Secondary = 0
        elif Primary.home == bg_current:

            "You hear a key jiggling in the lock."
        else:
            call Locked_Door (Primary)
            if Primary.location != bg_current:
                $ Primary = 0


    if not Primary:
        return




    call shift_focus (Primary)
    if bg_current == "bg_dangerroom":


        $ Primary.Outfit = "gym"
        $ Primary.change_outfit()
        if Secondary:
            $ Secondary.Outfit = "gym"
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
                $ Line = "sure"
            "Not right now, maybe later.":
                $ Line = "later"
            "Nope.":
                $ Line = "no"

        if Line == "sure":
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

        if Line == "later":
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
                call Remove_Girl (Secondary)
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
                call Remove_Girl (Primary)

        if Line == "no":
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
                call Remove_Girl (Primary)
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
                call Remove_Girl (Secondary)
                if Primary == JeanX:
                    "[Secondary.name] storms out."
                else:
                    "The girls storm out."
                    if Primary == StormX or Secondary == StormX:
                        "-so to speak."



    elif bg_current in PersonalRooms:

        if Secondary:

            "[Primary.name] and [Secondary.name] just entered the room."
        else:

            "[Primary.name] just entered the room."
        if bg_current == Primary.home:
            if "_angry" in Primary.daily_history:

                $ Primary.change_face("_bemused", 1,Brows="_angry")
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
                $ Line = "stay"
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
                $ Line = "stay"
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
                $ Line = "stay"
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
            if Line != "stay":

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
                                ch_l "[[growls] . . .You probably shouldn't."
                            elif Primary == JeanX:
                                ch_j "Oh, bad call, [Primary.player_petname]"
                            elif Primary == StormX:
                                ch_s "Quite certain."
                            elif Primary == JubesX:
                                ch_v "Oh, let me check. . ."
                                $ Primary.change_face("_angry",Eyes="_side")
                                ch_v ". . ."
                                $ Primary.change_face("_angry",Mouth="open")
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
                            $ Line = "stay"
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
                                $ Line = "stay"
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
                            $ Line = "stay"
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
                        if Line != "stay":
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
                            $ Line = "stay"
                        if Line != "stay":
                            $ Primary.change_stat("love", 60, -5, 1)
                            $ Primary.change_stat("love", 80, -5)
                            $ Primary.change_stat("obedience", 50, 2)
                            $ Primary.change_stat("inhibition", 60, 5)
                            "[Primary.name] kicks you out of the room."

            if Line != "stay":
                $ bg_current = "bg_player"
                jump Misplaced

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

        $ Line = 0
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
                    $ Line = Primary.name + " takes the seat next to you"
                    $ Present.append(Primary)
                else:
                    $ Line = Primary.name + " sits across the room from you"
                    $ Nearby.append(Primary)
            else:
                $ Line = Primary.name + " sits across the room from you"
                $ Nearby.append(Primary)

        if Secondary:
            if approval_check(Secondary, 1000):
                if len(Present) < 2 and D20 >= 10:

                    if Primary in Present:
                        $ Line = Primary.name + " and " + Secondary.name + " sit down next to you"
                    else:
                        $ Line = Line + ", while " + Secondary.name + " takes the seat next to you"
                    $ Present.append(Secondary)
                else:
                    if Primary in Nearby:
                        $ Line = Primary.name + " and " + Secondary.name + " sit across the room from you"
                    else:
                        $ Line = Line + ", while " + Secondary.name + " sits across the room from you"
                    $ Nearby.append(Secondary)
            else:
                if Primary in Nearby:
                    $ Line = Primary.name + " and " + Secondary.name + " sit across the room from you"
                else:
                    $ Line = Line + ", while " + Secondary.name + " sits across the room from you"
                $ Nearby.append(Secondary)
        if Line:
            "[Line]."

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


    $ BO = all_Girls[:]
    while BO:
        if BO[0] in Nearby:
            $ BO[0].location = "nearby"
        elif BO[0].location == bg_current:
            $ Present.append(BO[0])
        $ BO.remove(BO[0])
    if Nearby:
        "There were some others as well, but they kept their distance."
    return






label Gym_Entry(BO=[], GirlsNum=0):
    if Taboo == 0 and bg_current == "bg_dangerroom":
        menu:
            "Is this visit for work or for play?"
            "Work [[get geared up]":
                pass
            "Play [[keep on this outfit]":
                return
    $ BO = all_Girls[:]
    while BO:

        if BO[0].location != "bg_dangerroom" and BO[0].Outfit == "gym":

            $ BO[0].Outfit = BO[0].OutfitDay
        elif BO[0].Outfit == "gym":

            pass
        elif BO[0].location == "bg_dangerroom" and BO[0] not in Party:

            $ BO[0].Outfit = "gym"
        $ BO.remove(BO[0])
    call set_the_scene
    $ BO = Present[:]
    while BO:
        if BO[0].Outfit != "gym":

            if approval_check(BO[0], 1300, "LO") or "passive" in BO[0].traits:
                pass
            elif approval_check(BO[0], 800, "LO") and BO[0].Custom1[0]:
                pass
            elif approval_check(BO[0], 600, "LO") and BO[0].Gym[0] != 1:
                pass
            else:
                $ Line = "no"

            if Line == "no" or "asked gym" in BO[0].daily_history or "no_ask gym" in BO[0].traits:

                show blackscreen onlayer black
                if BO[0] == EmmaX:
                    ch_e "I should change too."
                elif BO[0] == LauraX:
                    ch_l "I'll be right back. . ."
                elif BO[0] == StormX:
                    ch_s "I should change as well. . ."
                else:
                    if GirlsNum:
                        BO[0].voice "I'll be right back too."
                    else:
                        BO[0].voice "I'll be back soon, gotta change."
                $ BO[0].Outfit = "gym"
            else:

                $ BO[0].daily_history.append("asked gym")
                if GirlsNum:

                    if BO[0] == EmmaX:
                        $ Line = "Do you think I should change as well?"
                    elif BO[0] == LauraX:
                        $ Line = "Did you want me to change into my gym clothes?"
                    elif BO[0] == StormX:
                        $ Line = "Do you think I should change as well?"
                    else:
                        $ Line = "Should I change too?"
                else:
                    if BO[0] == EmmaX:
                        $ Line = "Did you want me to change into my gear?"
                    elif BO[0] == LauraX:
                        $ Line = "Did you want me to change into my gym clothes?"
                    elif BO[0] == StormX:
                        $ Line = "Do you think I should change into my gym clothes?"
                    else:
                        $ Line = "Would you like me to change into my gym clothes?"
                BO[0].voice "[Line]"
                menu:
                    extend ""
                    "Yeah, they look great.":
                        $ BO[0].change_face("_smile")
                        $ BO[0].change_stat("love", 80, 2)
                        $ BO[0].change_stat("obedience", 40, 1)
                        $ BO[0].change_stat("inhibition", 30, 1)
                        $ Line = 1
                    "No, stay in that.":
                        $ BO[0].change_face("_confused")
                        $ BO[0].change_stat("obedience", 50, 5)
                        $ Line = 0
                    "Whichever you like.":
                        $ BO[0].change_face("_confused")
                        $ BO[0].change_stat("inhibition", 50, 1)
                        $ Line = renpy.random.randint(0, 3)
                    "I don't care.":
                        $ BO[0].change_face("_angry")
                        $ BO[0].change_stat("love", 50, -3, 1)
                        $ BO[0].change_stat("obedience", 50, 4)
                        $ BO[0].change_stat("inhibition", 50, 2)
                        $ Line = renpy.random.randint(0, 1)
                if Line:

                    if BO[0] == RogueX:
                        ch_r "Ok, be right back."
                    elif BO[0] == KittyX:
                        ch_k "Ok, back in a bit."
                    elif BO[0] == EmmaX:
                        ch_e "Fine, I'll be right back."
                    elif BO[0] == LauraX:
                        ch_l "I'll be right back then."
                    elif BO[0] == StormX:
                        ch_s "Then I will return shortly."
                    elif BO[0] == JubesX:
                        ch_v "K, be right back."
                    $ BO[0].Outfit = "gym"

            if BO[0].Outfit == "gym":
                $ GirlsNum += 1
            $ Line = 0

        $ BO.remove(BO[0])


    $ BO = all_Girls[:]
    while BO:

        $ BO[0].change_outfit()
        $ BO.remove(BO[0])
    hide blackscreen onlayer black
    return




label Gym_Exit(BO=[]):


    if BO and BO[0] in all_Girls:
        pass
    else:
        $ BO = Party[:]
    while BO:
        if BO[0].Outfit == "gym":

            if len(Party) > 1:
                $ Line = "We should change out of these if we're leaving. . ."
            else:
                $ Line = "I should change out of these if we're leaving. . ."
            $ BO[0].Outfit = BO[0].OutfitDay
        $ BO.remove(BO[0])
    if Party:
        Party[0].voice "[Line]"
    if Line:
        show blackscreen onlayer black with dissolve
        $ BO = Party[:]
        while BO:

            $ BO[0].change_outfit()
            $ BO.remove(BO[0])
        $ Line = 0
        hide blackscreen onlayer black
    return





label Gym_Clothes_Off(BO=[]):

    if BO and BO[0] in all_Girls:
        pass
    else:
        $ BO = all_Girls[:]
    while BO:

        if BO[0] not in Party:
            if BO[0].Outfit == "gym" and BO[0].location != "bg_dangerroom":
                $ BO[0].Outfit = BO[0].OutfitDay
            elif BO[0].location == "bg_dangerroom":
                $ BO[0].Outfit = "gym"
        $ BO.remove(BO[0])
    return





label Present_Check(Hold=1, BO=[], TempList=[]):



    while len(Party) > 2:


        $ Party.remove(Party[2])


    $ Present = Party[:] if Party else []





    $ BO = all_Girls[:]
    $ renpy.random.shuffle(BO)
    while BO:

        if BO[0] not in Present and BO[0].location == bg_current:
            $ Present.append(BO[0])
        $ BO.remove(BO[0])

    while len(Present) > 2:



        call Remove_Girl (Present[2], Hold=Hold)

    if Present and focused_Girl not in Present:
        $ renpy.random.shuffle(Present)
        call shift_focus (Present[0])

    $ BO = Present[:]
    while BO:

        if BO[0] in Nearby:
            $ Nearby.remove(BO[0])
        $ BO[0].location = bg_current
        $ BO.remove(BO[0])
    return






label ReturnToSender:


    $ BO = active_Girls[:]
    while BO:



        if BO[0] not in Party and BO[0].Schedule[Weekday][time_index] != bg_current:

            $ BO[0].location = BO[0].Schedule[Weekday][time_index]
            if BO[0] == JubesX and JubesX.addiction > 60:

                $ JubesX.location = JubesX.home
        $ BO.remove(BO[0])
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
                call Remove_Girl (RogueX, 1, 1)
            "[KittyX.name]" if KittyX.location == bg_current:
                "You shift away from [KittyX.name]"
                call Remove_Girl (KittyX, 1, 1)
            "[EmmaX.name]" if EmmaX.location == bg_current:
                "You shift away from [EmmaX.name]"
                call Remove_Girl (EmmaX, 1, 1)
            "[LauraX.name]" if LauraX.location == bg_current:
                "You shift away from [LauraX.name]"
                call Remove_Girl (LauraX, 1, 1)
            "[JeanX.name]" if JeanX.location == bg_current:
                "You shift away from [JeanX.name]"
                call Remove_Girl (JeanX, 1, 1)
            "[StormX.name]" if StormX.location == bg_current:
                "You shift away from [StormX.name]"
                call Remove_Girl (StormX, 1, 1)
            "[JubesX.name]" if JubesX.location == bg_current:
                "You shift away from [JubesX.name]"
                call Remove_Girl (JubesX, 1, 1)
            "No, never mind.":
                return
    "[Girl.name] comes over and joins you."


    $ Nearby.remove(Girl)
    $ Present.append(Girl)
    call shift_focus (Girl)
    $ Girl.location = bg_current
    call set_the_scene (1, 0, 0, 0)
    return




label Dismissed:

    menu:
        "Did you want to ask someone to leave?"
        "[RogueX.name]" if RogueX.location == bg_current or RogueX in Party:
            call Girl_Dismissed (RogueX)
        "[KittyX.name]" if KittyX.location == bg_current or KittyX in Party:
            call Girl_Dismissed (KittyX)
        "[EmmaX.name]" if EmmaX.location == bg_current or EmmaX in Party:
            call Girl_Dismissed (EmmaX)
        "[LauraX.name]" if LauraX.location == bg_current or LauraX in Party:
            call Girl_Dismissed (LauraX)
        "[JeanX.name]" if JeanX.location == bg_current or JeanX in Party:
            call Girl_Dismissed (JeanX)
        "[StormX.name]" if StormX.location == bg_current or StormX in Party:
            call Girl_Dismissed (StormX)
        "[JubesX.name]" if JubesX.location == bg_current or JubesX in Party:
            call Girl_Dismissed (JubesX)
        "Nevermind.":
            pass
    return




label Locked_Door(Girl=0, Entry=0, Current=0):



    if Girl not in all_Girls:
        return
    if Current not in all_Girls:
        $ Current = 0
    $ Player.add_word(1,"interruption")
    if not primary_action:

        call set_the_scene
    if Girl == KittyX:
        if bg_current == "bg_campus" or bg_current == "bg_pool":
            "Suddently, [Girl.name] rounds a corner."
        else:
            "You look to the door just as [KittyX.name] phases into the room."
        $ KittyX.location = bg_current
        call Taboo_Level
        $ KittyX.change_outfit()
        call Display_Girl (KittyX, TrigReset=0)
        ch_k "Hi, [KittyX.player_petname]!"
        return 1
    if "locked" not in Player.traits:
        $ Girl.location = bg_current
        if Entry:
            call Display_Girl (Girl, TrigReset=0)
            if bg_current == "bg_campus" or bg_current == "bg_pool":
                "Suddently, [Girl.name] rounds a corner."
            else:
                "Suddently, [Girl.name] enters the room, apparently without knocking."
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
        return 1
    if Girl.location == Girl.home:
        "You hear a key in the lock, and [Girl.name] enters the room."
    elif Girl == JeanX:
        "You hear a rattle at the door."
        "After a moment, and some clicking in the lock, the door pops open."
        "[JeanX.name] walks into the room."
        $ JeanX.location = bg_current
        call Taboo_Level
        $ JeanX.change_outfit()
        call Display_Girl (JeanX, TrigReset=0)
        ch_j "Hey, [JeanX.player_petname]!"
        return 1
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
            "Open door [[but stop fucking first]" if primary_action:
                ch_p "Hold on, [Girl.name]!"
                call Sex_Over (1, Primary)
                "You unlock the door and let her in."
                $ Girl.location = bg_current
                $ Girl.change_outfit()
                call Display_Girl (Girl, TrigReset=0)
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
                jump Misplaced
            "Send her away":
                ch_p "Er, sorry, could you come back later?"
                $ Girl.change_stat("love", 80, -2)
                if Girl == RogueX:
                    ch_r "C'mon, [Girl.player_petname], don't yank my chain like this!"
                    if Girl.location == bg_current:
                        call Remove_Girl (Girl)
                    return 0
                elif Girl == EmmaX:
                    $ Girl.change_stat("obedience", 80, -2)
                    ch_e "I have to say, [EmmaX.player_petname], I understand the appeal of having someone at your beck and call. . ."
                    ch_e "but I don't appreciate being on the receiving end!"
                    if Girl.location == bg_current:
                        call Remove_Girl (Girl)
                    return 0
                elif Girl in (LauraX,JubesX):
                    "[Girl.name] goes quiet."
                    if approval_check(Girl, 500,"I") and not approval_check(Girl, 500,"O"):
                        $ Girl.location = bg_current
                        $ Girl.change_outfit()
                        if Girl == LauraX:
                            $ LauraX.ArmPose = 2
                            $ LauraX.Claws = 1
                            "snickt"
                            call Display_Girl (Girl, TrigReset=0)
                            "The door swings open."
                            $ LauraX.Claws = 0
                            ch_l "Hey, so I don't like being jerked around, so don't do that, okay?"
                        else:
                            "A thin mist passes under the door, and forms into a human shape."
                            call Display_Girl (Girl, TrigReset=0)
                            ch_v "Well, I wanted to talk."
                        $ Girl.change_stat("obedience", 80, -4)
                    else:
                        $ Girl.change_stat("love", 80, -1)
                        $ Girl.change_stat("obedience", 80, 3)
                        Girl.voice "Ok."
                        "You hear her shuffling off."
                        if Girl.location == bg_current:
                            call Remove_Girl (Girl)
                        return 0
                elif Girl == StormX:
                    if approval_check(Girl, 800,"LI") and not approval_check(Girl, 500,"O"):
                        $ Girl.location = bg_current
                        $ Girl.change_outfit()
                        call Display_Girl (Girl, TrigReset=0)
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
                            call Remove_Girl (Girl)
                        return 0
    if Current:
        if Current == EmmaX and ("three" not in EmmaX.history or "classcaught" not in EmmaX.history):

            $ Girl.add_word(1,0,0,"saw with " + Current.tag)
            if bg_current == EmmaX.home:

                ch_e "I. . . This isn't what it looks like. . ."
                "She shoves the two of you out of her room and slams the door."
                $ Girl.location = "bg_player"
                call Remove_Girl (EmmaX)
            else:
                ch_e "I. . . This isn't what it looks like. . ."
                call Remove_Girl (EmmaX)
                "She seems uncomfortable with the situation and leaves the room."
                "Perhaps you should ask her about it later."
            jump Misplaced

        if "poly " + Current.tag in Girl.traits or (Current in Player.Harem and Girl in Player.Harem):

            pass
        else:

            if approval_check(Current, 1500, TabM=2, Bonus = (Girl.GirlLikeCheck(Current) - 500)):

                $ Current.change_face("_sexy", 1)
                $ Current.change_stat("obedience", 90, 5)
                $ Current.change_stat("inhibition", 90, 5)
                $ Current.change_stat("lust", 90, 3)
            else:

                $ Current.change_face("_angry", 1)
                if Current == RogueX:
                    ch_r "Hey, [Girl.tag], we're a little busy here?"
                elif Current == KittyX:
                    ch_k "Um, [Girl.tag]? Read the room?"
                elif Current == EmmaX:
                    ch_e "[Girl.tag], could you please leave?"
                elif Current == LauraX:
                    ch_l "Scram, [Girl.tag]."
                elif Current == JeanX:
                    ch_j "Leave, [Girl.tag]."
                elif Current == StormX:
                    ch_s "Would you mind give us some space?"
                elif Current == JubesX:
                    ch_v "Yeah, we were. . . busy."
                $ Girl.add_word(1,0,0,"saw with " + Current.tag)
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
                $ Current.change_face("_sexy", 1)
                if Girl.location == bg_current:
                    call Remove_Girl (Girl)
                return 0
        if Current == RogueX:
            ch_r "Oh, [Girl.tag], did you want to join in?"
        elif Current == KittyX:
            ch_k "Um, [Girl.tag]? Did you want something?"
        elif Current == EmmaX:
            ch_e "Oh, [Girl.tag]. . . care to join us?"
        elif Current == LauraX:
            ch_l "Oh, hey, [Girl.tag]."
        elif Current == JeanX:
            ch_j "Hey."
        elif Current == StormX:
            ch_s "Oh, hello [Girl.tag], did you want to join in?"
        elif Current == JubesX:
            ch_v "Hey, [Girl.tag], did you need something?"

    $ Girl.location = bg_current
    call Taboo_Level
    $ Girl.change_outfit(5)
    $ Player.drain_word("locked",0,0,1)
    call set_the_scene (1, 0, 0, 0)

    if Partner == Girl:

        $ Silent = 1
    $ Partner = Girl
    $ Line = 0
    return 1




label Taboo_Level(Taboo_Loc=1, Teach=0, BO=[]):




    if EmmaX.location == "bg_teacher":
        $ EmmaX.location = "bg_classroom"
        $ Teach = 1
    elif StormX.location == "bg_teacher":
        $ StormX.location = "bg_classroom"
        $ Teach = 2

    call CheckTaboo (Player, bg_current)

    $ BO = all_Girls[:]
    if JeanX in BO and "nowhammy" not in JeanX.traits:

        $ JeanX.Taboo = 0
        $ BO.remove(JeanX)
    while BO:


        if BO[0] in Party:
            $ BO[0].location = bg_current
        if BO[0].location == "nearby":
            $ Taboo_Check = bg_current
        else:
            $ Taboo_Check = BO[0].location
        if not Taboo_Loc or Taboo_Check == bg_current:

            call CheckTaboo (BO[0], Taboo_Check)
        $ BO.remove(BO[0])

    if Teach == 2:
        $ StormX.location = "bg_teacher"
    elif Teach:
        $ EmmaX.location = "bg_teacher"
    return


label CheckTaboo(Girl=0, Taboo_Check=0, Girl2=[]):



    if Taboo_Check in PersonalRooms or Taboo_Check == "hold":
        $ Girl.Taboo = 0
    elif "locked" in Player.traits and Taboo_Check == bg_current:
        $ Girl.Taboo = 0
    elif Taboo_Check in ("bg_classroom", "bg_study"):
        if time_index >= 3:
            $ Girl.Taboo = 10
        elif time_index == 2 or Weekday >= 5:
            $ Girl.Taboo = 30
        else:
            $ Girl.Taboo = 40
    elif Taboo_Check == "bg_dangerroom":
        if time_index >= 3:
            $ Girl.Taboo = 20
        else:
            $ Girl.Taboo = 40
    elif Taboo_Check == "bg_campus" or Taboo_Check == "bg_pool":
        if time_index >= 3:
            $ Girl.Taboo = 20
        else:
            $ Girl.Taboo = 40
    elif Taboo_Check == "bg_showerroom":
        $ Girl.Taboo = 20
    else:
        $ Girl.Taboo = 40
    if Girl == Player:

        $ Taboo = Girl.Taboo
        return
    if Girl.Taboo >= 20:

        return

    $ Girl2 = all_Girls[:]
    while Girl2:

        if Girl2[0] != Girl:

            if Girl.location == Girl2[0].location and Girl.GirlLikeCheck(Girl2[0]) <= 700 and not (Girl in Player.Harem and Girl2[0] in Player.Harem):

                $ Girl.Taboo = 20
        $ Girl2.remove(Girl2[0])

    $ Taboo = Girl.Taboo if (Girl.Taboo > Taboo and bg_current == Girl.location) else Taboo

    return






label action_speed_Shift(S=0):


    $ action_speed = S
    show blackscreen onlayer black
    pause 0.01
    hide blackscreen onlayer black
    return




label Shop:
    menu:
        "You are logged into the store. You have [Player.cash] dollars."
        "Buy dildo for $20.":
            if Player.inventory.count("_dildo") >= 10:
                "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
            elif Player.cash >= 20:
                "You purchase one dildo."
                $ Player.inventory.append("_dildo")
                $ Player.cash -= 20
            else:
                "You don't have enough for that."
        "Buy \"Shocker\" vibrator for $25.":
            if Player.inventory.count("_vibrator") >= 10:
                "If you bought one more vibrator, you would risk a geological event."
            elif Player.cash >= 25:
                "You purchase one vibrator."
                $ Player.inventory.append("_vibrator")
                $ Player.cash -= 25
            else:
                "You don't have enough for that."
        "Gifts for [RogueX.name]":
            menu:
                "Buy green lace nighty for $75." if "nighty" not in RogueX.inventory and "Rogue nighty" not in Player.inventory:
                    if Player.cash >= 75:
                        "You purchase the nighty, this will look nice on [RogueX.name]."
                        $ Player.inventory.append("Rogue nighty")
                        $ Player.cash -= 75
                    else:
                        "You don't have enough for that."
                "Buy black lace bra for $90." if "lace_bra" not in RogueX.inventory and "Rogue lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [RogueX.name]."
                        $ Player.inventory.append("Rogue lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "_lace_panties" not in RogueX.inventory and "Rogue lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [RogueX.name]."
                        $ Player.inventory.append("Rogue lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in RogueX.inventory and "_stockings_and_garterbelt" not in Player.inventory and approval_check(RogueX, 1500):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [RogueX.name]."
                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy yellow bikini top for $50." if "_bikini_top" not in RogueX.inventory and "Rogue bikini_top" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini top, this will look nice on [RogueX.name]."
                        $ Player.inventory.append("Rogue bikini_top")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy green bikini bottoms for $50." if "_bikini_bottoms" not in RogueX.inventory and "Rogue bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini bottoms, these will look nice on [RogueX.name]."
                        $ Player.inventory.append("Rogue bikini_bottoms")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [KittyX.name]" if "met" in KittyX.history:
            menu:
                "Buy white lace bra for $90." if "lace_bra" not in KittyX.inventory and "Kitty lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [KittyX.name]."
                        $ Player.inventory.append("Kitty lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "_lace_panties" not in KittyX.inventory and "Kitty lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [KittyX.name]."
                        $ Player.inventory.append("Kitty lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."

                "Buy pantyhose for $50." if "pantyhose" not in KittyX.inventory and "Kitty_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [KittyX.name]."
                        $ Player.inventory.append("Kitty_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in KittyX.inventory and "_stockings_and_garterbelt" not in Player.inventory:
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [KittyX.name]."
                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy knee-stockings for $50." if "knee" not in KittyX.inventory and "knee" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the stockings, these will look nice on [KittyX.name]."
                        $ Player.inventory.append("knee")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."

                "Buy blue cat bikini top for $60." if "_bikini_top" not in KittyX.inventory and "Kitty bikini_top" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini top, this will look nice on [KittyX.name]."
                        $ Player.inventory.append("Kitty bikini_top")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy blue bikini bottoms for $60." if "_bikini_bottoms" not in KittyX.inventory and "Kitty bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini bottoms, these will look nice on [KittyX.name]."
                        $ Player.inventory.append("Kitty bikini_bottoms")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy blue miniskirt for $50." if "_blue_skirt" not in KittyX.inventory and "Kitty blue_skirt" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the blue skirt, this will look nice on [KittyX.name]."
                        $ Player.inventory.append("Kitty blue_skirt")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [EmmaX.name]" if "met" in EmmaX.history:
            menu:
                "Buy white lace bra for $90." if "lace_bra" not in EmmaX.inventory and "Emma lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [EmmaX.name]."
                        $ Player.inventory.append("Emma lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "_lace_panties" not in EmmaX.inventory and "Emma lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [EmmaX.name]."
                        $ Player.inventory.append("Emma lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in EmmaX.inventory and "Emma_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [EmmaX.name]."
                        $ Player.inventory.append("Emma_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in EmmaX.inventory and "_stockings_and_garterbelt" not in Player.inventory and approval_check(EmmaX, 1500):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [EmmaX.name]."
                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy white bikini top for $60." if "_bikini_top" not in EmmaX.inventory and "Emma bikini_top" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini top, this will look nice on [EmmaX.name]."
                        $ Player.inventory.append("Emma bikini_top")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy white bikini bottoms for $60." if "_bikini_bottoms" not in EmmaX.inventory and "Emma bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini bottoms, these will look nice on [EmmaX.name]."
                        $ Player.inventory.append("Emma bikini_bottoms")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [LauraX.name]" if "met" in LauraX.history:
            menu:
                "Buy red corset for $70." if "_corset" not in LauraX.inventory and "Laura corset" not in Player.inventory:
                    if Player.cash >= 70:
                        "You purchase the corset, this will look nice on [LauraX.name]."
                        $ Player.inventory.append("Laura corset")
                        $ Player.cash -= 70
                    else:
                        "You don't have enough for that."
                "Buy red lace corset for $90." if "lace corset" not in LauraX.inventory and "Laura lace corset" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace corset, this will look nice on [LauraX.name]."
                        $ Player.inventory.append("Laura lace corset")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy red lace panties for $110." if "_lace_panties" not in LauraX.inventory and "Laura lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [LauraX.name]."
                        $ Player.inventory.append("Laura lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy black bikini top for $50." if "_bikini_top" not in LauraX.inventory and "Laura bikini_top" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini top, this will look nice on [LauraX.name]."
                        $ Player.inventory.append("Laura bikini_top")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "_bikini_bottoms" not in LauraX.inventory and "Laura bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini bottoms, these will look nice on [LauraX.name]."
                        $ Player.inventory.append("Laura bikini_bottoms")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass

        "Gifts for [JeanX.name]" if "met" in JeanX.history:
            menu:
                "Buy black corset for $70." if "_corset" not in JeanX.inventory and "Jean corset" not in Player.inventory:
                    if Player.cash >= 70:
                        "You purchase the corset, this will look nice on [JeanX.name]."
                        $ Player.inventory.append("Jean corset")
                        $ Player.cash -= 70
                    else:
                        "You don't have enough for that."







                "Buy green lace bra for $90." if "lace_bra" not in JeanX.inventory and "Jean lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [JeanX.name]."
                        $ Player.inventory.append("Jean lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy green lace panties for $110." if "_lace_panties" not in JeanX.inventory and "Jean lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [JeanX.name]."
                        $ Player.inventory.append("Jean lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy \"X\" bikini top for $50." if "_bikini_top" not in JeanX.inventory and "Jean bikini_top" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini top, this will look nice on [JeanX.name]."
                        $ Player.inventory.append("Jean bikini_top")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "_bikini_bottoms" not in JeanX.inventory and "Jean bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the bikini bottoms, these will look nice on [JeanX.name]."
                        $ Player.inventory.append("Jean bikini_bottoms")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in JeanX.inventory and "Jean_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [JeanX.name]."
                        $ Player.inventory.append("Jean_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in JeanX.inventory and "_stockings_and_garterbelt" not in Player.inventory and approval_check(JeanX, 800):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [JeanX.name]."
                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Gifts for [StormX.name]" if "met" in StormX.history:
            menu:
                "Buy black lace bra for $90." if "lace_bra" not in StormX.inventory and "Storm lace_bra" not in Player.inventory:
                    if Player.cash >= 90:
                        "You purchase the lace bra, this will look nice on [StormX.name]."
                        $ Player.inventory.append("Storm lace_bra")
                        $ Player.cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "_lace_panties" not in StormX.inventory and "Storm lace_panties" not in Player.inventory:
                    if Player.cash >= 110:
                        "You purchase the lace panties, these will look nice on [StormX.name]."
                        $ Player.inventory.append("Storm lace_panties")
                        $ Player.cash -= 110
                    else:
                        "You don't have enough for that."
                "Buy pantyhose for $50." if "pantyhose" not in StormX.inventory and "Storm_pantyhose" not in Player.inventory:
                    if Player.cash >= 50:
                        "You purchase the hose, these will look nice on [StormX.name]."
                        $ Player.inventory.append("Storm_pantyhose")
                        $ Player.cash -= 50
                    else:
                        "You don't have enough for that."
                "Buy stockings and garterbelt for $100." if "_stockings_and_garterbelt" not in StormX.inventory and "_stockings_and_garterbelt" not in Player.inventory and approval_check(StormX, 1500):
                    if Player.cash >= 100:
                        "You purchase the stockings, these will look nice on [StormX.name]."
                        $ Player.inventory.append("_stockings_and_garterbelt")
                        $ Player.cash -= 100
                    else:
                        "You don't have enough for that."
                "Buy black bikini top for $60." if "_bikini_top" not in StormX.inventory and "Storm bikini_top" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini top, this will look nice on [StormX.name]."
                        $ Player.inventory.append("Storm bikini_top")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Buy black bikini bottoms for $60." if "_bikini_bottoms" not in StormX.inventory and "Storm bikini_bottoms" not in Player.inventory:
                    if Player.cash >= 60:
                        "You purchase the bikini bottoms, these will look nice on [StormX.name]."
                        $ Player.inventory.append("Storm bikini_bottoms")
                        $ Player.cash -= 60
                    else:
                        "You don't have enough for that."
                "Never mind.":
                    pass
        "Buy books":

            menu Shop_Books:
                "Buy \"Dazzler and Longshot\" for $20.":
                    "A sappy romantic novel about two starcrossed lovers."
                    if "DL" not in Shop_Inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.cash >= 20:
                        "You purchase the book."
                        $ Shop_Inventory.remove("DL")
                        $ Player.inventory.append("Dazzler and Longshot")
                        $ Player.cash -= 20
                    else:
                        "You don't have enough for that."
                "Buy \"256 Shades of Grey\" for $20.":
                    "A gripping sexual thriller about a stern red-headed \"goblin queen\" and her subject."
                    if "G" not in Shop_Inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.cash >= 20:
                        "You purchase the book."
                        $ Shop_Inventory.remove("G")
                        $ Player.inventory.append("256 Shades of Grey")
                        $ Player.cash -= 20
                    else:
                        "You don't have enough for that."
                "Buy \"Avengers Tower Penthouse\" for $20.":
                    "A book filled with nude pictures of various Avengers, sexy."
                    if "A" not in Shop_Inventory:
                        "They seem to be out of stock at the moment."
                    elif Player.cash >= 20:
                        "You purchase the book."
                        $ Shop_Inventory.remove("A")
                        $ Player.inventory.append("Avengers Tower Penthouse")
                        $ Player.cash -= 20
                    else:
                        "You don't have enough for that."
                "Back":
                    jump Shop
            jump Shop_Books
        "Buy Cologne":
            if Day < 50:
                "These are currently out of stock, check back later."
                jump Shop
            menu:
                "Examine the Mandrill Cologne (\"Nothin says lovin like a shiny red butt\").":
                    menu:
                        "This cologne is guaranteed to make women love you more [[+Love]."
                        "Buy Mandrill Cologne for $150":
                            pass
                        "Never mind.":
                            jump Shop
                    if "Mandrill Cologne" in Player.inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.cash >= 150:
                        "You purchase one bottle of Mandrill Cologne."
                        $ Player.inventory.append("Mandrill Cologne")
                        $ Player.inventory.append("Mandrill Cologne")
                        $ Player.inventory.append("Mandrill Cologne")
                        $ Player.inventory.append("Mandrill Cologne")
                        $ Player.inventory.append("Mandrill Cologne")
                        $ Player.cash -= 150
                    else:
                        "You don't have enough for that."
                "Examine the Purple Rain Cologne (\"They can't resist your charms\").":
                    menu:
                        "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]."
                        "Buy Purple Rain Cologne for $200":
                            pass
                        "Never mind.":
                            jump Shop
                    if "Purple Rain Cologne" in Player.inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.cash >= 200:
                        "You purchase one bottle of Purple Rain Cologne."
                        $ Player.inventory.append("Purple Rain Cologne")
                        $ Player.inventory.append("Purple Rain Cologne")
                        $ Player.inventory.append("Purple Rain Cologne")
                        $ Player.inventory.append("Purple Rain Cologne")
                        $ Player.inventory.append("Purple Rain Cologne")
                        $ Player.inventory.append("Purple Rain Cologne")
                        $ Player.cash -= 200
                    else:
                        "You don't have enough for that."
                "Examine the Corruption Cologne (\"Let the wild out\").":
                    menu:
                        "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]."
                        "Buy Corruption Cologne for $250":
                            pass
                        "Never mind.":
                            jump Shop
                    if "Corruption Cologne" in Player.inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif Player.cash >= 250:
                        "You purchase one bottle of Corruption Cologne."
                        $ Player.inventory.append("Corruption Cologne")
                        $ Player.inventory.append("Corruption Cologne")
                        $ Player.inventory.append("Corruption Cologne")
                        $ Player.inventory.append("Corruption Cologne")
                        $ Player.inventory.append("Corruption Cologne")
                        $ Player.cash -= 250
                    else:
                        "You don't have enough for that."
                "Back":
                    pass
        "Exit Store":
            return
    jump Shop
return


























label set_the_scene(Chr=1, Entry=0, Dress=1, TrigReset=1, Quiet=0, BO=[]):






    if not Quiet:
        show blackscreen onlayer black

    if Entry:
        $ Chr = 0
        call AllHide
        $ entering = True
    else:
        $ entering = False

    if time_index >= 3:
        show NightMask onlayer nightmask
    else:
        hide NightMask onlayer nightmask

    if TrigReset:

        $ primary_action = 0
        $ offhand_action = 0 if offhand_action != "jackin" else "jackin"
        $ girl_offhand_action = 0
        $ second_girl_primary_action = 0
        $ second_girl_offhand_action = 0
        $ TrigReset = 0

    if Chr:
        call Present_Check


        $ BO = all_Girls[:]

        while BO:





            if focused_Girl != BO[0]:

                $ BO[0].sprite_location = stage_right
                $ BO[0].sprite_layer = 75
            call Display_Girl (BO[0], Dress, TrigReset)
            $ BO.remove(BO[0])

        if focused_Girl.location == bg_current:
            $ focused_Girl.sprite_location = stage_center
            $ focused_Girl.sprite_layer = 100
            call Display_Girl (focused_Girl, Dress, TrigReset)

        if bg_current == "bg_study" and time_index < 3:
            show Xavier_sprite zorder 25 at sprite_location(stage_left)
        else:
            hide Xavier_sprite
    else:

        call AllHide (1)
    show Chibi_UI
    hide Cellphone

    if bg_current == "bg_classroom":
        if EmmaX.location == "bg_teacher":


            $ EmmaX.change_outfit()
        if StormX.location == "bg_teacher":


            $ StormX.change_outfit()

    if bg_current != "bg_pool":

        hide FullPool
    if TrigReset and Dress:

        call Get_Dressed

    hide DressScreen
    if "Historia" in Player.traits:
        show BlueScreen onlayer black
    else:
        hide BlueScreen onlayer black
    hide blackscreen onlayer black

    return




label shift_focus(Chr=RogueX, Second=0, BO=[], Return=0):

    if Chr not in all_Girls:
        "Tell Oni [Chr]"
        "Then Tell Oni [Chr.tag]"
    if Chr == focused_Girl == Partner:

        $ BO = all_Girls[:]
        if Partner in all_Girls:
            $ BO.remove(Partner)
        else:
            "Tell Oni, in Shift Focus, P:[Partner]"
        while BO:

            if BO[0].location == bg_current:
                $ Partner = BO[0]
            $ BO.remove(BO[0])

    if Chr.location == bg_current:

        $ BO = all_Girls[:]
        if Chr in all_Girls:
            $ BO.remove(Chr)
        else:
            "Tell Oni, in Shift Focus, C:[Chr]"
        while BO:

            if BO[0].location == bg_current:

                $ BO[0].sprite_location = stage_right
                $ BO[0].sprite_layer = 75
                $ BO = [1]
            $ BO.remove(BO[0])

        $ Chr.sprite_location = stage_center
        $ Chr.sprite_layer = 100
    if focused_Girl == Chr:

        pass
    elif Second and Second != Chr:

        $ Partner = Second
    elif Partner == Chr:

        $ Partner = focused_Girl
    $ focused_Girl = Chr
    if Partner == Chr:
        $ Partner = 0

    $ renpy.restart_interaction()



    return



transform sprite_location(Loc=stage_right, LocY=50):

    pos (Loc,LocY)

label Display_Girl(Chr=0, Dress=1, TrigReset=1, DLoc=0, YLoc=50):


    if Chr not in all_Girls:
        "Tell Oni that in Display_Girl, Chr is [Chr]"
        return

    if Chr not in Party and Chr.location != bg_current:













        call expression Chr.tag + "_Hide" pass (1)
        $ Chr.change_outfit(Changed=1)
        return

    if Dress:
        if Chr.Outfit == "swimwear":
            if Chr.location == "bg_pool":
                $ Chr.change_outfit(Changed=1)
            elif Chr.OutfitDay != "swimwear":
                $ Chr.Outfit = Chr.OutfitDay
                $ Chr.change_outfit(Changed=1)
        elif Taboo:
            $ Chr.change_outfit(Changed=1)
        elif Chr.location != "bg_dangerroom" and Chr.OutfitDay != "gym":

            $ Chr.Outfit = Chr.OutfitDay
            $ Chr.change_outfit(Changed=1)

    elif Chr.location != "bg_showerroom" and Chr.location != "bg_pool":
        $ Chr.Water = 0

    if TrigReset:

        $ primary_action = 0
        $ offhand_action = 0 if offhand_action != "jackin" else "jackin"
        $ girl_offhand_action = 0
        $ second_girl_primary_action = 0
        $ second_girl_offhand_action = 0

    if Partner == Chr:
        $ DLoc = stage_right

    if DLoc:
        $ Chr.sprite_location = DLoc
    else:
        $ DLoc = Chr.sprite_location

    call expression Chr.tag + "_Hide"


    $ Chr.location = bg_current

    if Dress:

        call OutfitShame (Chr)

    if bg_current == "bg_movies" or bg_current == "bg_restaurant":

        $ YLoc = 250


    if Chr == RogueX:
        show Rogue_sprite zorder Chr.sprite_layer at sprite_location(DLoc,YLoc):
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)
    elif Chr == KittyX:
        show Kitty_sprite zorder Chr.sprite_layer at sprite_location(DLoc,YLoc):
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)
    elif Chr == EmmaX:
        show Emma_Sprite zorder Chr.sprite_layer at sprite_location(DLoc,YLoc):
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)
    elif Chr == LauraX:
        $ Chr.Claws = 0
        show Laura_Sprite zorder Chr.sprite_layer at sprite_location(DLoc,YLoc):
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)
    elif Chr == JeanX:
        show Jean_Sprite zorder Chr.sprite_layer at sprite_location(DLoc,YLoc):
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)
    elif Chr == StormX:
        show Storm_Sprite zorder Chr.sprite_layer at sprite_location(DLoc,YLoc):
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)
    elif Chr == JubesX:
        show Jubes_Sprite zorder Chr.sprite_layer at sprite_location(DLoc,YLoc):
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)

    return





















label ViewShift(Girl=0, View=0, ShouldHide=1, ViewTrig=primary_action):


    if Girl not in all_Girls:
        return
    if View == "menu":
        if not renpy.showing(Girl.tag+"_Sprite") and not renpy.showing(Girl.tag+"_Doggy_Animation") and not renpy.showing(Girl.tag+"_SexSprite"):

            return
        menu:
            "Full Body":
                call expression Girl.tag + "_Pos_Reset" pass (ViewTrig, 1)
            "Upper half":
                call expression Girl.tag + "_Breasts_Launch" pass (ViewTrig)
            "Middle View":
                call expression Girl.tag + "_Middle_Launch" pass (ViewTrig)
            "Lower half":
                call expression Girl.tag + "_Pussy_Launch" pass (ViewTrig)
            "Rear view" if Girl in (RogueX,KittyX,EmmaX,LauraX,JeanX):
                $ Girl.pose = "doggy"
                call expression Girl.tag + "_Sex_Launch" pass (ViewTrig)
            "On top of you" if Girl in (EmmaX,JeanX,StormX):
                $ Girl.pose = "sex"
                call expression Girl.tag + "_Sex_Launch" pass (ViewTrig)
            "Laying down" if Girl in (RogueX,KittyX,LauraX):
                $ Girl.pose = "sex"
                call expression Girl.tag + "_Sex_Launch" pass (ViewTrig)
            "Never mind":
                pass
    else:
        if ShouldHide:
            call expression Girl.tag + "_Hide"
        if View == "full":
            call expression Girl.tag + "_Pos_Reset" pass (ViewTrig, 1)
        elif View == "breasts":
            call expression Girl.tag + "_Breasts_Launch" pass (ViewTrig)
        elif View == "mid":
            call expression Girl.tag + "_Middle_Launch" pass (ViewTrig)
        elif View == "pussy":
            call expression Girl.tag + "_Pussy_Launch" pass (ViewTrig)
        elif View == "doggy" or View == "sex":
            call expression Girl.tag + "_Sex_Launch" pass (ViewTrig)
        elif View == "kiss":
            call expression Girl.tag + "_Kissing_Launch" pass (ViewTrig)
    return

image Punchout:
    Null(0,0)

label Punch:

    show Punchout with vpunch
    hide Punchout
    return


label AllReset(Chr=0, BO=[]):


    if Chr in all_Girls:
        $ BO = [Chr]
    else:
        $ BO = all_Girls[:]

    while BO:
        call expression BO[0].tag + "_BJ_Reset"
        call expression BO[0].tag + "_TJ_Reset"
        call expression BO[0].tag + "_HJ_Reset"
        call expression BO[0].tag + "_Sex_Reset"
        call expression BO[0].tag + "_Doggy_Reset"
        call expression BO[0].tag + "_Hide"
        if BO[0] == RogueX:
            if RogueX.location == bg_current:
                show Rogue_sprite zorder RogueX.sprite_layer at sprite_location(RogueX.sprite_location,50):
                    ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0)
                show Rogue_sprite:
                    zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.6, 0.0) pos (RogueX.sprite_location,50)
            else:
                hide Rogue_sprite
        elif BO[0] == KittyX:
            if KittyX.location == bg_current:
                show Kitty_sprite zorder KittyX.sprite_layer at sprite_location(KittyX.sprite_location,50):
                    ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                show Kitty_sprite:
                    zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (KittyX.sprite_location,50)
            else:
                hide Kitty_sprite
        elif BO[0] == EmmaX:
            if EmmaX.location == bg_current:
                show Emma_Sprite zorder EmmaX.sprite_layer at sprite_location(EmmaX.sprite_location,50):
                    ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                show Emma_Sprite:
                    zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (EmmaX.sprite_location,50)
            else:
                hide Emma_Sprite
        elif BO[0] == LauraX:
            if LauraX.location == bg_current:
                show Laura_Sprite zorder LauraX.sprite_layer at sprite_location(LauraX.sprite_location,50):
                    ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                show Laura_Sprite:
                    zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (LauraX.sprite_location,50)
            else:
                hide Laura_Sprite
        elif BO[0] == JeanX:
            if JeanX.location == bg_current:
                show Jean_Sprite zorder JeanX.sprite_layer at sprite_location(JeanX.sprite_location,50):
                    ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                show Jean_Sprite:
                    zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (JeanX.sprite_location,50)
            else:
                hide Jean_Sprite
        elif BO[0] == StormX:
            if StormX.location == bg_current:
                show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location,50):
                    ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                show Storm_Sprite:
                    zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (StormX.sprite_location,50)
            else:
                hide Storm_Sprite
        elif BO[0] == JubesX:
            if JubesX.location == bg_current:
                show Jubes_Sprite zorder JubesX.sprite_layer at sprite_location(JubesX.sprite_location,50):
                    ease .5 zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0)
                show Jubes_Sprite:
                    zoom 1 xzoom 1 yzoom 1 offset (0,0) anchor (0.5, 0.0) pos (JubesX.sprite_location,50)
            else:
                hide Jubes_Sprite
        $ BO.remove(BO[0])
    return



label AllHide(Cull=0):
    if Cull or RogueX.location != bg_current:
        hide Rogue_sprite
        call Rogue_Hide
    if Cull or KittyX.location != bg_current:
        hide Kitty_sprite
        call Kitty_Hide
    if Cull or EmmaX.location != bg_current:
        hide Emma_Sprite
        call Emma_Hide
    if Cull or LauraX.location != bg_current:
        hide Laura_Sprite
        call Laura_Hide
    if Cull or JeanX.location != bg_current:
        hide Jean_Sprite
        call Jean_Hide
    if Cull or StormX.location != bg_current:
        hide Storm_Sprite
        call Storm_Hide
    if Cull or JubesX.location != bg_current:
        hide Jubes_Sprite
        call Jubes_Hide
    if Cull or "bg_study" != bg_current:
        hide Xavier_sprite
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
                    call Rogue_SexAct ("switch")
                elif RogueX.location == bg_current:
                    ch_r "I s'pose I could lend a hand . ."
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

                    ch_k "Whoa, drama much? . ."
                    call Kitty_SexAct ("switch")
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
                    call Emma_SexAct ("switch")
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
                    call Laura_SexAct ("switch")
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
                    call Jean_SexAct ("switch")
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
                    call Storm_SexAct ("switch")
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
                    call Jubes_SexAct ("switch")
                elif JubesX.location == bg_current:
                    ch_v "Sure!"
                else:
                    "She seems uncomfortable with this situation and leaves the room."
        "Never mind [[something else]":

            pass
    if AloneCheck(Girl) and Girl.Taboo == 20:
        $ Girl.Taboo = 0
        $ Taboo = 0
    return

label Partner_Like(Girl=0, Value=1, AltValue=1, Measure=800, Partner=Partner):




    if Girl not in all_Girls or Partner not in all_Girls:
        return

    if second_girl_primary_action:

        if second_girl_primary_action == "watch":
            pass
        elif second_girl_primary_action in ("handjob","blowjob"):
            $ Value += 1
        elif second_girl_primary_action in ("eat_pussy","eat_ass"):
            $ Value += 3
        else:
            $ Value += 2


    $ Partner.GLG(Girl,Measure,Value,1)
    $ Girl.GLG(Partner,Measure,Value,1)
    return




label RoomStatboost(Type=0, Check=0, Amount=0, BO=[]):


    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current or BO[0] in Nearby:
            $ BO[0].change_stat(Type, Check, Amount)
        $ BO.remove(BO[0])
    return




label GirlWaitUp(Local=0, Check=70, D20=0, Teach=0, BOA=[], BOB=[]):






    $ D20 = renpy.random.randint(0,1) if not D20 else D20

    if EmmaX.location == "bg_teacher":
        $ EmmaX.location = "bg_classroom"
        $ Teach = 1
    elif StormX.location == "bg_teacher":
        $ StormX.location = "bg_classroom"
        $ Teach = 2
    $ BOA = all_Girls[:]

    while BOA:

        $ BOB = all_Girls[:]
        while BOB:

            if BOA[0] != BOB[0] and BOA[0].location == BOB[0].location:

                if BOA[0].location == "bg_classroom":
                    $ BOA[0].GLG(BOB[0],700,1,1)

                elif BOA[0].location == "bg_dangerroom":
                    $ BOA[0].GLG(BOB[0],700,(1+D20),1)

                elif BOA[0].location == "bg_showerroom":
                    if BOA[0] == EmmaX:

                        $ BOA[0].GLG(BOB[0],900,3,1)

                    elif BOB[0] in (EmmaX,StormX) and BOA[0] != LauraX:

                        $ BOA[0].GLG(BOB[0],900,3,1)
                    else:

                        $ BOA[0].GLG(BOB[0],900,2,1)
                else:

                    $ BOA[0].GLG(BOB[0],Check, D20,1)



                if BOA[0] == EmmaX:


                    $ BOA[0].GLG(BOB[0],1000,(int(BOB[0].Shame/4)),1)
                elif BOB[0] in (EmmaX,StormX) and BOA[0] != LauraX:


                    $ BOA[0].GLG(BOB[0],1000, (int(BOB[0].Shame/4)),1)
                else:

                    $ BOA[0].GLG(BOB[0],1000, (int(BOB[0].Shame/5)),1)

            $ BOB.remove(BOB[0])
        $ BOA.remove(BOA[0])

    if Teach == 2:
        $ StormX.location = "bg_teacher"
    elif Teach:
        $ EmmaX.location = "bg_teacher"
    return




label LesCheck(Girls=[], BO=[]):



    if "three" not in EmmaX.history:

        if EmmaX.Thirst >= 30 and approval_check(EmmaX, 800, "I"):
            $ EmmaX.history.append("three")

    $ BO = active_Girls[:]
    while BO:

        if BO[0] == RogueX and "touch" not in RogueX.traits:

            pass
        elif BO[0] == EmmaX and "three" not in EmmaX.history:

            pass
        elif approval_check(BO[0], 500, "I",Alt=[[EmmaX,JeanX],300]) and BO[0].Thirst >= 30:
            if ("mono" not in BO[0].traits or BO[0].Break[0]) and BO[0] not in Party:
                $ Girls.append(BO[0])
                if BO[0].Thirst >= 60:
                    $ Girls.append(BO[0])
            if BO[0].Thirst >= 90:
                $ Girls.append(BO[0])
        $ BO.remove(BO[0])
    if not Girls:
        return

    if Girls[0] != JeanX:
        $ renpy.random.shuffle(Girls)

    $ Partner = 0
    while len(Girls) >= 2:


        if Partner:

            $ Girls.remove(Girls[1])
        elif Girls[1] == Girls[0] or Girls[1].location == bg_current or Girls[1] in Party:


            $ Girls.remove(Girls[1])
        elif Girls[0] == JeanX and Girls[1].GirlLikeCheck(Girls[0]) >= 500:

            $ Partner = Girls[1]
        elif (Girls[1] in Player.Harem and Girls[0] in Player.Harem) and Girls[0].GirlLikeCheck(Girls[1]) >= 600:
            $ Partner = Girls[1]
        elif Girls[1].GirlLikeCheck(Girls[0]) >= 800 and Girls[0].GirlLikeCheck(Girls[1]) >= 800:
            $ Partner = Girls[1]
        elif Girls[1].Thirst >= 90 and Girls[0].GirlLikeCheck(Girls[1]) >= 600:
            $ Partner = Girls[1]
        else:

            $ Girls.remove(Girls[1])

    if not Partner:

        return

    $ Girls.append(Partner)
    $ Partner = 0


    if bg_current != Girls[0].home:

        $ Girls[0].location = Girls[0].home
        $ Girls[1].location = Girls[0].home
    elif bg_current != Girls[1].home:

        $ Girls[0].location = Girls[1].home
        $ Girls[1].location = Girls[1].home

    $ Girls[0].add_word(1,"les",0,0,0)
    $ Girls[1].add_word(1,"les",0,0,0)

    $ Girls[0].GLG(Girls[1],700,15,1)
    $ Girls[1].GLG(Girls[0],700,15,1)

    $ Girls[0].GLG(Girls[1],900,10,1)
    $ Girls[1].GLG(Girls[0],900,10,1)

    $ Girls[0].GLG(Girls[1],1000,5,1)
    $ Girls[1].GLG(Girls[0],1000,5,1)

    $ Girls[0].drain_word("arriving",1,0)
    $ Girls[1].drain_word("arriving",1,0)

    $ Girls[0].change_stat("lust", 60, 20)
    $ Girls[1].change_stat("lust", 60, 20)

    $ Girls[0].Thirst -= 5
    $ Girls[1].Thirst -= 5
    return




label Haremchange_stat(Girl=0, Check=1000, Value=0, Greater=0, BOA=[], BOB=[]):



    if "Historia" in Player.traits:
        return
    if Girl == "All" or Girl == 0:
        $ BOA = Player.Harem[:]
    elif Girl in all_Girls:
        $ BOA = [Girl]
    else:
        return
    while BOA:

        $ BOB = Player.Harem[:]
        if BOA[0] in BOB:

            $ BOB.remove(BOA[0])
        while BOB:

            $ BOA[0].GLG(BOB[0],Check,Value,1)
            $ BOB.remove(BOB[0])
        $ BOA.remove(BOA[0])
    return








label JumperCheck(Girls=[], BO=[]):

    if "nope" in Player.recent_history or Party:

        return

    $ BO = active_Girls[:]
    while BO:
        if "les" in BO[0].recent_history and "no_les" not in Player.recent_history and approval_check(BO[0], 1600 - BO[0].SEXP, TabM=0):

            call Call_For_Les (BO[0])

        if "locked" in Player.traits and BO[0].location != bg_current:

            pass
        elif BO[0].remaining_actions and BO[0].Thirst >= 30 and approval_check(BO[0], 500, "I") and "refused" not in BO[0].daily_history and "met" in BO[0].history:
            if "chill" not in BO[0].traits and BO[0].tag not in Player.daily_history and "jumped" not in BO[0].daily_history and BO[0].location != "bg_teacher":

                if renpy.random.randint(0,3) > 1:
                    $ Girls.append(BO[0])
                if BO[0].Thirst >= 60:
                    $ Girls.append(BO[0])
            if BO[0].Thirst >= 90:
                $ Girls.append(BO[0])
        $ BO.remove(BO[0])

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
        elif Girls[0].GirlLikeCheck(Girls[1]) >= 800 and Girls[1].GirlLikeCheck(Girls[0]) >= 800:
            $ Partner = Girls[1]

    call Jumped

    if "nope" in Player.recent_history:

        while Girls:
            call Remove_Girl (Girls[0])
            $ Girls.remove(Girls[0])
        jump Misplaced
    elif Girls:

        if Girls[0].location == bg_current:
            call expression Girls[0].tag + "_SexMenu"

    if bg_current == "bg_player":

        jump Player_Room
    return


label Jumped(Act=0):




    if Girls[0] == EmmaX and Partner and "three" not in EmmaX.history:

        $ Girls.remove(Partner)
        $ Partner = 0
    elif EmmaX in Girls and ((Taboo and "taboo" not in EmmaX.history) or "three" not in EmmaX.history):

        $ Girls.remove(EmmaX)
        $ Partner = 0

    if not Girls:
        return

    if Girls[0].location != bg_current and "locked" in Player.traits:

        call Locked_Door (Girls[0])
        if not Girls or Girls[0].location != bg_current:

            $ Player.recent_history.append("nope")
            return


    $ BO = Girls[:]
    while BO:
        $ BO[0].location = bg_current
        $ BO.remove(BO[0])
    $ Girls[0].add_word(1,"jumped","jumped")

    call Taboo_Level

    if Taboo and (not approval_check(Girls[0], 1500, TabM=3) or (Girls[0] == EmmaX and Taboo and "taboo" not in EmmaX.history)):

        $ Act = "leave"

    if bg_current in PersonalRooms:

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

    $ BO = Girls[:]
    while BO:
        $ BO[0].location = bg_current
        $ BO.remove(BO[0])

    call Taboo_Level
    call set_the_scene (Dress=0)

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

    call Favorite_Actions (Girls[0], 1)
    $ Act = _return
    $ action_context = Girls[0]

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


    if Act == "anal":
        call expression Girls[0].tag + "_AnalPrep"
    elif Act == "sex":
        call expression Girls[0].tag + "_SexPrep"
    elif Act ==  "eat_pussy":
        call expression Girls[0].tag + "_LP_Prep"
    elif Act == "fondle_pussy":
        call expression Girls[0].tag + "_FP_Prep"
    elif Act == "blowjob":
        call expression Girls[0].tag + "_BJ_Prep"
    elif Act == "titjob":
        call expression Girls[0].tag + "_TJ_Prep"


    elif Act == "handjob":
        call expression Girls[0].tag + "_HJ_Prep"
    elif Act == "hotdog":
        call expression Girls[0].tag + "_HotdogPrep"
    elif Act == "suck_breasts":
        call expression Girls[0].tag + "_SB_Prep"
    elif Act == "fondle_breasts":
        call expression Girls[0].tag + "_FB_Prep"
    elif Act == "finger_ass" or Act == "eat_ass":
        call expression Girls[0].tag + "_IA_Prep"
    else:
        call KissPrep (Girls[0])
    return






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
            $ Line = 0
            $ Girl.change_stat("love", 80, -2)
            if (2*Girl.obedience) >= (Girl.love + Girl.inhibition + (5*Girl.Thirst)):

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
                        $ Line = "ask"
                    ". . . [[say nothing, still no].":
                        pass
            elif (approval_check(Girl, 600, "I") and Girl.Thirst >= 30) or Girl.Thirst >= 50:

                $ Girl.change_face("_confused",1,Eyes="_surprised")
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
                    ch_j "Seriously? . ."
                elif Girl == StormX:
                    ch_s "Are you quite sure? . ."
                elif Girl == JubesX:
                    ch_v "I can make it worth your while. . ."
                $ Line = "ask"

            if Line == "ask":
                $ Line = 0
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
                            $ Line = "beg"
                        "Beg me again." if counter >= 100:
                            $ Girl.change_stat("obedience", 90, 2)
                            $ Line = "beg"
                        "Only if I get to choose.":

                            $ Girl.change_face("_smile",1,Brows="_confused")
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
                            call expression Girl.tag + "_SexMenu"
                            return
                        "Still no.":

                            $ Girl.change_stat("love", 85, -2)
                            $ Girl.change_stat("obedience", 90, 3)
                            if approval_check(Girl, 1500+(5*counter)-(10*Girl.Thirst), "LI"):

                                $ Line = "beg"
                            elif not counter and Count:

                                $ Girl.top_pulled_up = 1
                                pause 1
                                call expression Girl.tag + "_First_Topless" pass (1)
                                $ Girl.top_pulled_up = 0
                                $ Girl.change_face("_confused",1,Mouth="_smile")
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
                    if Line == "beg":
                        if approval_check(Girl, 600+counter, "O") or approval_check(Girl, 1500+(5*counter)-(10*Girl.Thirst)):

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
                                    ch_j "Ok. . . please? . ."
                                elif Girl == StormX:
                                    ch_s "No? You're that certain?"
                                elif Girl == JubesX:
                                    ch_v "Ya'sure?"
                            else:

                                $ Girl.change_face("_sad",2,Eyes="_surprised")
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

                            $ Girl.change_face("_sad",2,Brows="_confused")
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


            $ Line = 0
            if not Act:

                $ Girl.change_stat("love", 80, -2)
                if Girl == RogueX:
                    ch_r "Ok, your loss, I guess. . ."
                elif Girl == KittyX:
                    ch_k "Too bad . ."
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

    call Favorite_Actions (Girl, 1)
    $ Act = _return

    if Act in ("anal","sex","blowjob","titjob","handjob","hotdog"):

        "[Girl.name] reaches down and unzips your fly. . ."
        if not Player.semen:
            "You wish you weren't already drained. . . you stop her hands."
            ch_p "I could actually use a break right now. . "
            $ Act = "fondle_breasts"
        else:
            call Seen_First_Peen (Girl, Partner, 1)

    $ action_context = Girl


    if Act == "anal":
        call expression Girl.tag + "_AnalPrep"
    elif Act == "sex":
        call expression Girl.tag + "_SexPrep"
    elif Act ==  "eat_pussy":
        call expression Girl.tag + "_LP_Prep"
    elif Act == "fondle_pussy":
        call expression Girl.tag + "_FP_Prep"
    elif Act == "blowjob":
        call expression Girl.tag + "_BJ_Prep"
    elif Act == "titjob":
        call expression Girl.tag + "_TJ_Prep"
    elif Act == "handjob":
        call expression Girl.tag + "_HJ_Prep"
    elif Act == "hotdog":
        call expression Girl.tag + "_HotdogPrep"
    elif Act == "suck_breasts":
        call expression Girl.tag + "_SB_Prep"
    elif Act == "fondle_breasts":
        call expression Girl.tag + "_FB_Prep"
    elif Act == "finger_ass" or Act == "eat_ass":
        call expression Girl.tag + "_IA_Prep"
    else:
        call KissPrep (Girl)
    return






label Escalation(Girl=0):


    if counter < 10 or position_timer <= Round or Girl.Forced:

        return

    $ action_context = Girl

    if primary_action == "fondle_breast" and approval_check(Girl,1050,TabM=4,Alt=[[JeanX],800]) and Girl.lust >= 30 and Girl.action_counter["suck_breasts"]:

        if offhand_action == "suck_breasts":
            $ offhand_action = 0
        $ Girl.change_stat("inhibition", 80, 2)
        call expression Girl.tag + "_SB_Prep"
        if "suck_breasts" in Girl.recent_history:

            $ renpy.pop_call()
    elif primary_action == "fondle_thighs" and approval_check(Girl,1050,TabM=4,Alt=[[JeanX],800]) and Girl.lust >= 30 and Girl.action_counter["fondle_pussy"]:

        if offhand_action == "fondle_thighs":
            $ offhand_action = 0
        $ Girl.change_stat("inhibition", 80, 4)
        call expression Girl.tag + "_FP_Prep"
        if "fondle_pussy" in Girl.recent_history:

            $ renpy.pop_call()
    elif not Player.semen:

        pass
    elif primary_action == "handjob" and approval_check(Girl,1200,TabM=4) and Girl.lust >= 30 and Girl.action_counter["blowjob"]:

        $ Girl.change_stat("inhibition", 80, 3)
        call expression Girl.tag + "_BJ_Prep"
        if "blowjob" in Girl.recent_history:

            $ renpy.pop_call()
    elif primary_action not in ("sex","anal") and approval_check(Girl,1400,TabM=5,Alt=[[JeanX],1200]) and Girl.lust >= 60 and Girl.action_counter["sex"] >= 3:

        $ Girl.change_stat("inhibition", 80, 4)
        call expression Girl.tag + "_SexPrep"
        if "sex" in Girl.recent_history:

            $ renpy.pop_call()
    elif primary_action != "anal" and approval_check(Girl,1400,TabM=5,Alt=[[JeanX],1200]) and Girl.lust >= 70 and Girl.action_counter["anal"] >= 5:

        $ Girl.change_stat("inhibition", 80, 5)
        call expression Girl.tag + "_AnalPrep"
        if "anal" in Girl.recent_history:

            $ renpy.pop_call()


    $ position_timer = 0
    $ action_context = 0
    return







label Sex_Dialog(Primary=focused_Girl, Secondary=0, TempFocus=0, PrimaryLust=0, SecondaryLust=0, Line1=0, Line2=0, Line3=0, Line4=0, D20S=0):






    $ D20S = renpy.random.randint(1, 20) if not D20S else D20S
    $ Line = 0







    call Girls_Taboo (Primary)
    if not primary_action:
        return

    $ Secondary = Partner

    call Primary_SexDialog
    $ Line1 = Line



    if offhand_action and D20S <= 15:

        $ Line = ""
        call Offhand_Dialog
        $ Line1 = Line1 + Line



    if D20S >= 7 and primary_action not in ("masturbation", "lesbian"):

        $ Line = 0
        call Girl_Self_Lines (Primary, "T3", girl_offhand_action, D20X=D20S)
        if Line:
            $ Line3 = Line + "."



    if Secondary and (not second_girl_primary_action or 7 <= D20S <= 17 or second_girl_primary_action == "watch"):

        $ Line = 0
        call SexDialog_Threeway
        if Line:
            $ Line4 = Line + "."



    $ Player.change_stat("focus", 200, TempFocus)


    $ Primary.change_stat("lust", 200, PrimaryLust)
    $ Primary.lust_face()


    if Secondary:
        $ SecondaryLust += (int(PrimaryLust/10)) if Secondary.GirlLikeCheck(Primary) >= 700 else 0
        $ Secondary.change_stat("lust", 200, SecondaryLust)
        $ Secondary.lust_face()


    "[Line1]"
    if Line3:

        call Seen_First_Peen (Primary, Secondary, Passive=3)
        "[Line3]"
    if Line4:


        call Seen_First_Peen (Primary, Secondary, Passive=4)
        "[Line4]"
        if second_girl_primary_action == "suck_breasts" or second_girl_primary_action == "fondle_breasts":

            if approval_check(Primary,500,"I",TabM=2) and Primary.lust >= 50 and (Primary.ChestNum() > 1 or Primary.OverNum() > 1):

                $ Primary.top_pulled_up = 1
                "[Primary.name] seems frustrated and pulls her top open."

    call Activity_Check (Primary, Secondary, 0)
    if not _return:

        if Primary.Forced:


            return
        if Secondary and Secondary.location == bg_current:

            $ primary_action = Secondary
            $ Partner = 0
            $ second_girl_primary_action = 0
            $ second_girl_offhand_action = 0
        else:



            call Trig_Reset
        jump Misplaced

    call Dirty_Talk

    return


label Trig_Reset(Visual=0):

    $ primary_action = 0
    $ offhand_action = 0
    $ girl_offhand_action = 0
    $ second_girl_primary_action = 0
    $ second_girl_offhand_action = 0
    $ action_context = 0
    if Visual:
        call AllReset
    return


label primary_action_Swap(Active=0, primary_actionX1=primary_action, primary_actionX3=girl_offhand_action, Primary=Partner):






    $ offhand_action = 0 if offhand_action != "jackin" else offhand_action
    $ approval_bonus = 0

    if second_girl_primary_action:

        if second_girl_primary_action == "masturbation":
            $ primary_action = "masturbation"
            $ girl_offhand_action = second_girl_offhand_action
            $ second_girl_primary_action = 0


        elif primary_actionX1 == "lesbian":
            $ primary_action = "lesbian"
            $ girl_offhand_action = second_girl_primary_action
            $ second_girl_primary_action = 0
        elif second_girl_primary_action in ("handjob","blowjob","kiss"):
            $ primary_action = second_girl_primary_action
            $ girl_offhand_action = 0
            $ second_girl_primary_action = 0
        else:
            $ primary_action = 0
            $ girl_offhand_action = 0
            $ second_girl_primary_action = 0
    else:



        $ primary_action = 0
        $ girl_offhand_action = 0

    call shift_focus (Primary)
    if not Active:

        $ BO = active_Girls[:]
        $ BO.remove(Primary) if Primary in BO else BO
        while BO:
            if BO[0].location == bg_current:
                $ Partner = BO[0]
                $ BO = [1]
            $ BO.remove(BO[0])
    else:
        $ Partner = Active


    if primary_actionX1 == "masturbation":
        $ second_girl_primary_action = "masturbation"
        $ second_girl_offhand_action = primary_actionX3


    elif primary_actionX1 == "lesbian":
        $ second_girl_primary_action = primary_actionX3
    else:
        if primary_actionX1 in ("handjob","blowjob","kiss"):
            $ second_girl_primary_action = primary_actionX1
            $ second_girl_offhand_action = 0
        else:
            $ second_girl_primary_action = "masturbation"
            if primary_actionX1 in ("fondle_thighs","fondle_ass","finger_ass","eat_ass"):
                $ second_girl_offhand_action = "fondle_ass"
                "You pull back from [Partner.name]."
            elif primary_actionX1 in ("dildo_pussy","dildo_anal"):
                $ second_girl_offhand_action = primary_actionX1
                "You pull back from [Partner.name]."
            elif primary_actionX1 in ("titjob","hotdog","fondle_breasts","suck_breasts"):
                $ second_girl_offhand_action = "fondle_breasts"
                "You pull back from [Partner.name]."
            elif primary_actionX1 in ("fondle_pussy","eat_pussy"):
                $ second_girl_offhand_action = "fondle_pussy"
                "You pull back from [Partner.name]."
            elif primary_actionX1 == "sex":
                $ second_girl_offhand_action = "fondle_pussy"
                "You pull out of [Partner.name] and shift your attention to [Primary.name]."
            elif primary_actionX1 == "anal":
                $ second_girl_offhand_action = "fondle_ass"
                "You pull out of [Partner.name] and shift your attention to [Primary.name]."
            else:
                $ second_girl_offhand_action = 0
    call AllReset (Partner)

    if not primary_action:


        if Primary == RogueX:
            $ renpy.pop_call()
            $ renpy.pop_call()
            jump Rogue_SMenu
        if Primary == KittyX:
            $ renpy.pop_call()
            $ renpy.pop_call()
            jump Kitty_SMenu
        if Primary == EmmaX:
            $ renpy.pop_call()
            $ renpy.pop_call()
            jump Emma_SMenu
        if Primary == LauraX:
            $ renpy.pop_call()
            $ renpy.pop_call()
            jump Laura_SMenu
        if Primary == JeanX:
            $ renpy.pop_call()
            $ renpy.pop_call()
            jump Jean_SMenu
        if Primary == StormX:
            $ renpy.pop_call()
            $ renpy.pop_call()
            jump Storm_SMenu
        if Primary == JubesX:
            $ renpy.pop_call()
            $ renpy.pop_call()
            jump Jubes_SMenu
    else:
        call set_the_scene (Dress=0, TrigReset=0, Quiet=1)
        call expression Primary.tag + "_SexAct" pass ("SkipTo")
    return



label Activity_Check(Girl=0, Girl2=0, Silent=0, Removal=1, ClothesCheck=1, Mod=0, approval=1, Tempshame=0, TabooM=1):






    if Girl == Girl2:
        "Tell oni that the activity check failed after [primary_action]."
        $ Girl.NotAStat = 5


    if "unseen" in Girl.recent_history or "classcaught" in Girl.recent_history:
        return 2

    $ Mod += 200 if Girl.Forced else 0
    $ Mod += (Girl.lust*5) if Girl.lust >= 50 else 0

    if Girl2 and ClothesCheck != 2:

        $ Mod = int(Mod/2) if Mod > 0 else Mod

        $ Mod = (Girl.GirlLikeCheck(Girl2)-600)

        if Girl in Player.Harem and Girl2 in Player.Harem:
            $ Mod += 500

    if ClothesCheck and Girl2:


        call OutfitShame (Girl2, 20)
        $ Tempshame = Girl2.Shame

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

        $ TabooM = 0
    elif approval_check(Girl,50,"X") or approval_check(Girl,800,"I"):
        $ TabooM = .5

    if not approval:

        pass
    elif primary_action == "strip" and offhand_action != "jackin":
        pass
    elif not primary_action:
        pass
    elif primary_action == "eat_ass":
        $ approval = approval_check(Girl,1550,Bonus=Mod, TabM = (TabooM* 3 ))
    elif primary_action == "anal":
        $ approval = approval_check(Girl,1550,Bonus=Mod, TabM = (TabooM* 3 ))
    elif primary_action == "sex":
        $ approval = approval_check(Girl,1400,Bonus=Mod, TabM = (TabooM* 3 ))
    elif primary_action == "eat_pussy":
        $ approval = approval_check(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
    elif offhand_action == "jackin":
        $ approval = approval_check(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
    elif primary_action == "blowjob":
        $ approval = approval_check(Girl,1300,Bonus=Mod, TabM = (TabooM* 2 ))
    elif primary_action == "titjob":
        $ approval = approval_check(Girl,1200,Bonus=Mod, TabM = (TabooM* 3 ))
    elif primary_action == "hotdog":
        $ approval = approval_check(Girl,1000,Bonus=Mod, TabM = (TabooM* 3 ))
    elif primary_action == "handjob" or girl_offhand_action == "handjob":
        $ approval = approval_check(Girl,1100,Bonus=Mod, TabM = (TabooM* 2 ))
    elif primary_action == "footjob":
        $ approval = approval_check(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
    elif primary_action == "dildo_anal":
        $ approval = approval_check(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
    elif primary_action == "dildo_pussy":
        $ approval = approval_check(Girl,1250,Bonus=Mod, TabM = (TabooM* 2 ))
    elif primary_action == "finger_ass":
        $ approval = approval_check(Girl,1300,Bonus=Mod, TabM = (TabooM* 2 ))
    elif primary_action == "fondle_pussy" or primary_action == "finger_pussy":
        $ approval = approval_check(Girl,1050,Bonus=Mod, TabM = (TabooM* 2 ))
    elif primary_action == "suck_breasts":
        $ approval = approval_check(Girl,1050,Bonus=Mod, TabM = (TabooM* 3 ))
    elif primary_action == "fondle_breasts":
        $ approval = approval_check(Girl,950,Bonus=Mod, TabM = (TabooM* 2 ))
    elif primary_action == "fondle_ass":
        $ approval = approval_check(Girl,850,Bonus=Mod, TabM = (TabooM* 1 ))

    elif primary_action == "masturbation":
        $ approval = approval_check(Girl,1200,Bonus=Mod, TabM = (TabooM* 2 ))

    elif primary_action == "kiss":
        $ approval = approval_check(Girl,500,Bonus=Mod, TabM = 0)
    elif primary_action == "fondle_thighs":
        $ approval = approval_check(Girl,750,Bonus=Mod, TabM = 0)

    elif primary_action == "lesbian":
        $ approval = approval_check(Girl,1350,Bonus=Mod, TabM = (TabooM* 2 ))


    if not approval:

        pass
    elif not second_girl_primary_action:
        pass
    elif second_girl_primary_action == "eat_ass":
        $ approval = approval_check(Girl,1750,Bonus=(Mod+200), TabM = (TabooM* 3 ))
    elif second_girl_primary_action == "eat_pussy":
        $ approval = approval_check(Girl,1450,Bonus=(Mod+200), TabM = (TabooM* 2 ))
    elif second_girl_primary_action == "blowjob":
        $ approval = approval_check(Girl,1300,Bonus=(Mod+200), TabM = (TabooM* 2 ))
    elif second_girl_primary_action == "handjob":
        $ approval = approval_check(Girl,1200,Bonus=(Mod+200), TabM = (TabooM* 2 ))
    elif second_girl_primary_action == "finger_ass":
        $ approval = approval_check(Girl,1500,Bonus=(Mod+200), TabM = (TabooM* 2 ))
    elif second_girl_primary_action == "fondle_pussy":
        $ approval = approval_check(Girl,1250,Bonus=(Mod+200), TabM = (TabooM* 2 ))
    elif second_girl_primary_action == "suck_breasts":
        $ approval = approval_check(Girl,1250,Bonus=(Mod+200), TabM = (TabooM* 3 ))
    elif second_girl_primary_action == "fondle_breasts":
        $ approval = approval_check(Girl,1150,Bonus=(Mod+200), TabM = (TabooM* 2 ))
    elif second_girl_primary_action == "kiss girl":
        $ approval = approval_check(Girl,1050,Bonus=(Mod+200), TabM = 0)
    elif second_girl_primary_action == "kiss both":
        $ approval = approval_check(Girl,1050,Bonus=(Mod+200), TabM = 0)
    elif second_girl_primary_action == "fondle_ass":
        $ approval = approval_check(Girl,1050,Bonus=(Mod+200), TabM = (TabooM* 1 ))
    elif second_girl_primary_action == "masturbation":
        $ approval = approval_check(Girl,1400,Bonus=(Mod+200), TabM = (TabooM* 2 ))
    elif second_girl_primary_action == "watch":
        $ approval = approval_check(Girl,1000,Bonus=(Mod+200), TabM = 0)
    elif second_girl_primary_action == "kiss":
        $ approval = approval_check(Girl,600,Bonus=Mod, TabM = 0)

    if not Silent and not approval and not Girl.Forced:
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

    if Removal and not approval and not Girl.Forced:
        call Remove_Girl (Girl, 2)
        "[Girl.name] takes off."

    return approval



label Seen_First_Peen(Primary=0, Secondary=0, Silent=0, Undress=0, Passive=0, GirlsNum=0, React=0, BOptions=[]):






    if not Primary:

        $ BOptions = Present[:]
        $ renpy.random.shuffle(BOptions)
        while BOptions:


            if (focused_Girl == BOptions[0] or D20 >= 10) and "peen" not in BOptions[0].recent_history:


                call Girl_First_Peen (BOptions[0], Silent, Undress)
                $ GirlsNum = _return
            $ BOptions.remove(BOptions[0])

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
    $ Girl.SeenPeen += 1
    $ Girl.change_stat("inhibition", 30, 2)
    $ Girl.change_stat("inhibition", 80, 1)

    if Second:

        if Girl.SeenPeen == 1:
            $ Girl.change_face("_surprised", 2)
            if Girl == RogueX:
                ch_r "Wow, yeah, that's pretty nice. . ."
            elif Girl == KittyX:
                ch_k "Oh, wow, you aren't kidding. . ."
            elif Girl == EmmaX:
                $ Girl.change_face("_smirk", 2, Eyes = "_down")
                ch_e "My, that certainly is an impressive specimen. . ."
            elif Girl == LauraX:
                $ Girl.change_face("_smirk", 2, Eyes = "_down")
                ch_l "Huh, that's a pretty good one you got there. . ."
            elif Girl == JeanX:
                $ Girl.change_face("_smirk", 2, Eyes = "_down")
                ch_j "Yeah, looking good. . ."
            elif Girl == StormX:
                $ Girl.change_face("_smirk", 2, Eyes = "_down")
                ch_s "Yes, that is impressive. . ."
            elif Girl == JubesX:
                $ Girl.change_face("_smirk", 2, Eyes = "_down")
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
                    ch_l "I guess . ."
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
        if not Girl.Forced and not React and Taboo > 20 and (not approval_check(Girl, 1500) or Girl.SEXP < 10) and bg_current != "bg_showerroom" and Girl not in (JeanX,StormX):

            if not approval_check(Girl, 800) and not approval_check(Girl, 500, "I"):

                if Girl == EmmaX and ("detention" in Girl.recent_history or "classcaught" in Girl.recent_history):

                    $ Girl.change_face("_confused", Eyes="_down")
                    ch_e "Mmm?"
                    $ Girl.change_face("_surprised", Eyes="_squint")
                    if Girl.SeenPeen == 1:
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
                    if Girl.SeenPeen == 1:
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
                if Girl.SeenPeen == 1:
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


        elif Girl.SeenPeen > 10:

            return 0
        elif approval_check(Girl, 1200) or approval_check(Girl, 500, "L"):

            $ Girl.change_face("_sly",1)
            if Girl.SeenPeen == 1:
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
                    $ Girl.change_face("_surprised",1, Eyes="_down")
                    ch_e "Well that's certainly an interesting specimen."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("love", 50, 5)
                    $ Girl.change_stat("love", 90, 10)
                elif Girl == LauraX:
                    $ Girl.change_face("_surprised",1, Eyes="_down")
                    ch_l "Huh, that's a pretty good one you got there. . ."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("love", 50, 5)
                    $ Girl.change_stat("love", 90, 10)
                elif Girl == JeanX:
                    $ Girl.change_face("_confused",1, Eyes="_down",Mouth="_smile")
                    ch_j "Well, what do we have here. . ."
                    $ Girl.change_face("_bemused",1)
                    ch_j "Preeety nice there, [Girl.player_petname]."
                    $ Girl.change_stat("love", 50, 5)
                    $ Girl.change_stat("love", 90, 10)
                    $ Girl.change_stat("obedience", 80, 3)
                elif Girl == StormX:
                    $ Girl.change_face("_confused",1, Eyes="_down")
                    ch_s "Hmm. . . that is a lovely one."
                    $ Girl.change_face("_bemused",1)
                    $ Girl.change_stat("love", 50, 5)
                    $ Girl.change_stat("love", 90, 5)
                    $ Girl.change_stat("inhibition", 60, 2)
                elif Girl == JubesX:
                    $ Girl.change_face("_surprised",2, Eyes="_down")
                    ch_v "Oh. . . nice."
                    $ Girl.change_face("_sly",1)
                    $ Girl.change_stat("love", 80, 3)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 4)
            elif Girl.SeenPeen == 2:
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
                    $ Girl.change_face("_sly",1, Eyes="_down")
                    ch_v "Hello again."
                    $ Girl.change_face("_sly",1)
                    $ Girl.change_stat("obedience", 80, 1)
                    $ Girl.change_stat("inhibition", 60, 1)
            elif Girl.SeenPeen == 5:
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
                    $ Girl.change_face("_sly",1, Eyes="_down")
                    ch_v "Hey there. . ."
                    $ Girl.change_face("_sly",1)
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 80, 2)
                    $ Girl.change_stat("inhibition", 60, 2)
            elif Girl.SeenPeen == 10:
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
                    $ Girl.change_face("_confused",1, Eyes="_down")
                    ch_v "Kinda. . . hypnotic. . ."
                    $ Girl.change_face("_sly",1)
                    $ Girl.change_stat("love", 80, 1)
                    $ Girl.change_stat("obedience", 80, 3)
                    $ Girl.change_stat("inhibition", 60, 2)
            $ React = 1
        else:

            $ Girl.change_face("_sad",1)
            if Girl.SeenPeen == 1:
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
            elif Girl.SeenPeen < 5:
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
            elif Girl.SeenPeen == 10:
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
        if Girl.SeenPeen > 10:
            return
        elif approval_check(Girl, 1200) or approval_check(Girl, 500, "L"):
            if Girl.SeenPeen == 1:
                $ Girl.change_stat("love", 90, 5)
            elif Girl.SeenPeen == 2:
                $ Girl.change_stat("obedience", 50, 5)
            elif Girl.SeenPeen == 5:
                $ Girl.change_stat("inhibition", 60, 5)
            elif Girl.SeenPeen == 10:
                $ Girl.change_stat("love", 90, 10)
        else:
            if Girl.SeenPeen == 1:
                $ Girl.change_stat("obedience", 50, 5)
                $ Girl.change_stat("inhibition", 60, 5)
                $ Girl.add_word(1,0,0,0,"seenpeen")
            elif Girl.SeenPeen < 5:
                $ Girl.change_stat("inhibition", 60, 2)
            elif Girl.SeenPeen == 10:
                $ Girl.change_stat("obedience", 50, 5)
                $ Girl.change_stat("inhibition", 60, 5)
        if Girl == JubesX:
            $ Girl.change_stat("obedience", 80, 1)
    if Girl.SeenPeen == 1:
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





label Girls_Taboo(Girl=0, counter=1, Choice=0, D20=0):




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

        if Taboo > 20:
            if (primary_action == "kiss" and not offhand_action and not girl_offhand_action):

                pass
            elif Girl not in Rules:

                $ Girl.change_face("_surprised", 1)
                if primary_action == "blowjob" or primary_action == "handjob" or primary_action == "titjob":
                    "[Girl.name] stops what she's doing with a startled look."
                else:
                    "You feel a slight buzzing in your head and stop what you're doing."
                ch_x "Cease that behavior at once! Come to my office immediately!"
                call AllReset (Girl)
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
                    $ second_girl_offhand_action = Choice[0]
                    $ Choice = [1]
                $ Choice.remove(Choice[0])
            if second_girl_offhand_action:
                call Locked_Door (second_girl_offhand_action, 1, Girl)

            $ Choice = 0
            $ second_girl_offhand_action = 0



        call Girls_Noticed (Girl)

    if Taboo <= 20:

        call Girls_Noticed (Girl)
        return
    elif (primary_action == "kiss" and not offhand_action and not girl_offhand_action):

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
        elif approval_check(Girl, 650, "I", TabM=counter):

            $ Girl.change_face("_sexy", 1, Brows="_sad")
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
        elif approval_check(Girl, 1000, "OI", TabM=counter):

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

                        $ Girl.change_face("_sexy", 1,Brows="_sad")
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
            show blackscreen onlayer black
            call AllReset (Girl)
            call Remove_Girl (Girl)
            $ Girl.change_outfit(Changed=0)
            hide blackscreen onlayer black
            $ bg_current = "bg_player"
            jump Misplaced
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





label Girls_Noticed(Girl=Primary, Other=0, Silent=0, B=0, BO=[]):



    if not Girl or Girl not in all_Girls:
        "Tell Oni that in noticed, no primary is set."
        return
    $ BO = all_Girls[:]
    $ BO.remove(Girl)
    while BO:
        if BO[0].location == bg_current and BO[0] != Girl:


            $ Other = BO[0]
            $ BO = [1]
        $ BO.remove(BO[0])
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
    if Other == EmmaX and ("three" not in EmmaX.history or "classcaught" not in EmmaX.history):

        $ Other.add_word(1,0,0,"saw with " + Girl.tag)
        if bg_current == EmmaX.home:

            ch_e "If the two of you cannot keep your hands off each other, please do so elsewhere. . ."
            "She shoves the two of you out of her room and slams the door."
            $ Girl.location = "bg_player"
            jump Misplaced
        call Remove_Girl (EmmaX)
        if not Silent:
            "She seems uncomfortable with the situation and leaves the room."
            "Perhaps you should ask her about it later."
        return

    if "poly " + Girl.tag in Other.traits or (Girl in Player.Harem and Other in Player.Harem):

        $ B = (1000-(20*Taboo))
    else:

        $ B = (Other.GirlLikeCheck(Girl) - 500)
        if Other in Player.Harem:

            $ B -= 200

    $ Other.sprite_location = stage_far_right
    call Display_Girl (Other, 0, 0)
    if Partner == Other:

        $ Silent = 1
    $ Partner = Other
    $ Line = 0
    if approval_check(Other, 2000, TabM=2, Bonus = B) or approval_check(Other, 950, "L", TabM=2, Bonus = (B/3)):

        $ Other.change_face("_sexy", 1)
        if not Silent:
            "She decides to join you."
        $ Other.change_stat("obedience", 90, 5)
        $ Other.change_stat("inhibition", 90, 5)
        $ Other.change_stat("lust", 90, 3)
        $ Other.add_word(1,0,0,"poly " + Girl.tag)
        call Threeway_Set (Other, Mode="start", GirlB=Girl)
    elif approval_check(Other, 650, "O", TabM=2) and approval_check(Other, 450, "L", TabM=1) or approval_check(Other, 800, "O", TabM=2, Bonus = (B/3)):

        $ Other.change_face("_sexy")
        if not Silent:
            "She sits down patiently off to the side and watches."
        $ Other.change_stat("love", 90, 5)
        $ Other.change_stat("inhibition", 90, 5)
        $ Other.change_stat("lust", 90, 2)
        $ Other.add_word(1,0,0,"poly " + Girl.tag)
        call Threeway_Set (Other, "watch", Mode="start", GirlB=Girl)
    elif approval_check(Other, 650, "I", TabM=2) and approval_check(Other, 450, "L", TabM=1) or approval_check(Other, 800, "I", TabM=2, Bonus = (B/3)):

        $ Other.change_face("_sexy")
        if not Silent:
            "She sits down and watches you with a hungry look."
        $ Other.change_stat("love", 90, 5)
        $ Other.change_stat("obedience", 90, 2)
        $ Other.change_stat("inhibition", 90, 2)
        $ Other.change_stat("lust", 90, 5)
        $ Other.add_word(1,0,0,"poly " + Girl.tag)
        call Threeway_Set (Other, "watch", Mode="start", GirlB=Girl)
    elif approval_check(Other, 1500, TabM=2, Bonus = B):
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
    elif approval_check(Other, 650, "L", TabM=1) or approval_check(Other, 400, "O", TabM=2):

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
            call GirlsAngry
        call Remove_Girl (Other)
    else:

        $ Other.change_face("_surprised", 2)
        $ Other.change_stat("inhibition", 90, 2)
        $ Other.change_stat("lust", 40, 20)
        if primary_action != "kiss":
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
        elif primary_action != "kiss":
            if Other in (LauraX,JeanX):
                "She looks uncomfortable with this, and stalks out of the room."
            else:
                "She looks embarrassed, and bolts from the room."
        else:
            "She looks a bit disgusted and walks away."
        $ Partner = 0
        if bg_current == Other.home:
            $ Other.recent_history.append("_angry")
            call GirlsAngry
        call Remove_Girl (Other)
    if AloneCheck(Girl) and Girl.Taboo == 20:

        $ Girl.Taboo = 0
        $ Taboo = 0
    if Line:

        "[Line]."
        $ Line = 0
    return




label CloseOut(Chr=focused_Girl):

    $ Chr = GirlCheck(Chr)
    if primary_action == "blowjob":
        call expression Chr.tag + "_BJ_After"
    elif primary_action == "handjob":
        call expression Chr.tag + "_HJ_After"
    elif primary_action == "titjob":
        call expression Chr.tag + "_TJ_After"
    elif primary_action == "kiss":
        call Kiss_After
    elif primary_action == "fondle_breasts":
        call expression Chr.tag + "_FB_After"
    elif primary_action == "suck_breasts":
        call expression Chr.tag + "_SB_After"
    elif primary_action == "fondle_thighs":
        call expression Chr.tag + "_FT_After"
    elif primary_action == "fondle_pussy":
        call expression Chr.tag + "_FP_After"
    elif primary_action == "eat_pussy":
        call expression Chr.tag + "_LP_After"
    elif primary_action == "fondle_ass":
        call expression Chr.tag + "_FA_After"
    elif primary_action == "finger_ass":
        call expression Chr.tag + "_IA_After"
    elif primary_action == "eat_ass":
        call expression Chr.tag + "_LA_After"
    elif primary_action == "sex":
        call expression Chr.tag + "_SexAfter"
    elif primary_action == "hotdog":
        call expression Chr.tag + "_HotdogAfter"
    elif primary_action == "anal":
        call expression Chr.tag + "_AnalAfter"
    elif primary_action == "dildo_pussy":
        call expression Chr.tag + "_DP_After"
    elif primary_action == "dildo_anal":
        call expression Chr.tag + "_DA_After"
    elif primary_action == "strip":
        call Group_Strip_End
    elif primary_action == "masturbation":
        $ Chr.remaining_actions -= 1
        $ Chr.action_counter["masturbation"] += 1
    elif primary_action == "lesbian":
        call Les_After
    else:
        "That's odd, tell Oni how you got here, Close [Chr.name] [primary_action]."
    return



label Sex_Over(Clothes=1, Girls=0, BO=[]):



    $ Line = 0
    call Trig_Reset
    if Girls in all_Girls:

        $ BO = [Girls]
    else:
        $ BO = all_Girls[:]
        $ renpy.random.shuffle(BO)
    while BO:
        if BO[0].location == bg_current:

            $ BO[0].session_orgasms = 0
            call Girl_Cleanup (BO[0], "after")
            if Player.spunk:
                if BO[0] == RogueX:
                    ch_r "Let me take care of that for you. . ."
                elif BO[0] == KittyX:
                    ch_k "You've got a little something. . ."
                    ch_k "just let me get that."
                elif BO[0] == EmmaX:
                    ch_e "[EmmaX.player_petname], let's get you presentable. . ."
                elif BO[0] == LauraX:
                    ch_l "[LauraX.player_petname], you've got a little something. . ."
                elif BO[0] == JeanX:
                    ch_j "[JeanX.player_petname], you might want to clean up. . ."
                elif BO[0] == StormX:
                    ch_s "Allow me to take care of that, [StormX.player_petname]. . ."
                elif BO[0] == JubesX:
                    ch_v "Oh, I can clean that up for you, [JubesX.player_petname]. . ."
                call Girl_CleanCock (BO[0])

        if "nowhammy" not in JeanX.traits and "saw with Jean" in BO[0].traits:

            $ BO[0].traits.remove("saw with Jean")
            $ BO[0].traits.append("sawJeanW")
        $ BO.remove(BO[0])

    if Girls == Partner and Girls in all_Girls:

        call shift_focus (Girls)
    $ Girls = 0
    call AllReset ("all")

    if Clothes:

        $ BO = all_Girls[:]
        while BO:
            if BO[0].location == bg_current:
                if BO[0].change_outfit(Changed=1) == 2:
                    if Line:
                        $ Line = Line + " and " + BO[0].name
                    else:
                        $ Line = BO[0].name
                    $ Girls += 1
            $ BO.remove(BO[0])
        if Girls > 1:
            "[Line] throw their clothes back on."
        elif Girls:
            "[Line] throws her clothes back on."
    call Get_Dressed
    call checkout (1)
    return






label SkipTo(Chr=focused_Girl):

    $ Chr = GirlCheck(Chr)
    if primary_action == "blowjob":
        call expression Chr.tag + "_BJ_Cycle"
    elif primary_action == "handjob":
        call expression Chr.tag + "_HJ_Cycle"
    elif primary_action == "titjob":
        call expression Chr.tag + "_TJ_Cycle"
    elif primary_action == "kiss":
        call KissCycle (Chr)
    elif primary_action == "fondle_breasts":
        call expression Chr.tag + "_FB_Cycle"
    elif primary_action == "suck_breasts":
        call expression Chr.tag + "_SB_Cycle"
    elif primary_action == "fondle_thighs":
        call expression Chr.tag + "_FT_Cycle"
    elif primary_action == "fondle_pussy":
        call expression Chr.tag + "_FP_Cycle"
    elif primary_action == "eat_pussy":
        call expression Chr.tag + "_LP_Cycle"
    elif primary_action == "fondle_ass":
        call expression Chr.tag + "_FA_Cycle"
    elif primary_action == "finger_ass":
        call expression Chr.tag + "_IA_Cycle"
    elif primary_action == "eat_ass":
        call expression Chr.tag + "_LA_Cycle"
    elif primary_action == "sex":
        call expression Chr.tag + "_SexCycle"
    elif primary_action == "hotdog":
        call expression Chr.tag + "_HotdogCycle"
    elif primary_action == "anal":
        call expression Chr.tag + "_AnalCycle"
    elif primary_action == "dildo_pussy":
        call expression Chr.tag + "_DP_Cycle"
    elif primary_action == "dildo_anal":
        call expression Chr.tag + "_DA_Cycle"
    elif primary_action == "strip":
        call Group_Strip_End
    elif primary_action == "masturbation":
        $ Chr.remaining_actions -= 1
        $ Chr.action_counter["masturbation"] += 1
    elif primary_action == "lesbian":
        call Les_Cycle (Chr)
    else:
        "That's odd, tell Oni how you got here, Close [Chr.name] [primary_action]."
    return


label Clear_Stack:

    $ StackDepth = renpy.call_stack_depth()
    while StackDepth > 0:
        $ StackDepth -= 1
        $ renpy.pop_call()
    jump Player_Room










label Microtransactions_Intro:
    "You are getting a pulse that feels like Xavier calling."
    ch_x "Could you come to my office please?"
    menu:
        extend ""
        "Ok" if not Party and not Present:
            $ Party = []
            "You head over."
        "I should go for this." if Party or Present:
            $ Party = []
            "You excuse yourself and head out."
        "Nah.":

            ch_x "-Now,- [Player.name]!"
            if Party or Present:
                $ Party = []
                "You excuse yourself and head out."
            else:
                "You head over."
    show blackscreen onlayer black
    pause 0.1
    $ Round -= 5
    $ bg_current = "bg_study"
    call change_Xavier_face ("_happy")
    call set_the_scene
    hide blackscreen onlayer black
    ch_x "[Player.name], I'm glad you came to see me."
    ch_x "I have a problem that I believe you could take off my plate."
    ch_x " I've heard that you have been having. . . financial problems of late."
    ch_x "I may be able to help those problems go away."
    ch_x "I've come up with a fantstic new method of acquiring money."
    ch_x "I call it \"micro transactions!\""
    menu:
        extend ""
        "What, like -I- give -you- cash?":
            call change_Xavier_face ("shocked")
            ch_x "What? How would that make sense? You give me cash so I give you cash?"
        "What a rip-off!":
            call change_Xavier_face ("shocked")
            ch_x "I haven't even explained the system yet!"
        "Shill!":
            call change_Xavier_face ("shocked")
            ch_x "what are you even talking about?"
    ch_x "I don't understand what the problem is, it's just a form of surprise mechanic!"
    call change_Xavier_face ("_happy")
    ch_x "You open a small box and receive an item!"
    ch_x "It really is a remarkable system!"
    ch_x "It involves using a certain invention developed by a friend of mine."
    ch_x "They are called \"Pym particles.\""
    menu:
        extend ""
        "What?!":
            pass
        "Oh. I see where this is going. . .":
            pass
    ch_x "Yes, what it allows me to do is take large. . ."
    ch_x ". . . cumbersome. . . "
    ch_x ". . . objects, and shrink them down to a more manageable size."
    ch_x "Then those items can be conveniently delivered all over town."
    ch_x "All I need from you is to pick up these packages and deliver them to their destinations."
    ch_x "Microtransactions!"
    menu:
        "Yes, I get it.":
            pass
        "Huh?":
            call change_Xavier_face ("shocked")
            ch_x ". . . I don't think I could dumb it down further."
    call change_Xavier_face ("_happy")
    ch_x "Here, a nice starter package, just bring this to Henry in the lab."
    menu:
        extend ""
        "Ok.":
            pass
        "No thank you.":
            ch_x "If this isn't something you want to do, I understand."
            ch_x "But this is actually a rather urgent delivery, so I'm afraid that just this once. . ."
            ch_x "I must insist."
    show blackscreen onlayer black
    scene
    pause 0.1
    scene empty_class onlayer backdrop
    hide blackscreen onlayer black
    $ Round -= 5
    "You take a small metal box from the Professor, and head to Professor McCoy's lab."
    "You drop it off in the corner, and it rapidly expands into a large device labeled \"Pym\""
    ch_b "Oh, my shirnk ray!"
    $ bg_current = "bg_study"
    show blackscreen onlayer black
    pause 0.1
    call set_the_scene
    hide blackscreen onlayer black
    $ Round -= 5
    "You return to Xavier's office."
    $ Player.cash += 5
    ch_x "See? Simple!"
    $ Player.history.append("micro")
    ch_x "If you wish to make further microtransactions, just access it from McCoy's lab."
    ch_x "I'm sure there will be plenty of business."
    "You return to your room."
    $ bg_current = "bg_player"
    show blackscreen onlayer black
    pause 0.1
    call set_the_scene
    hide blackscreen onlayer black
    return

label Microtransactions:



    if Round < 20:
        "You don't have time for that now, maybe later."
        return
    if Player.daily_history.count("micro") >= 3:
        "There are no more Microtransactions for today."
        return
    menu:
        "What do you want to do?"
        "Deliver a nearby MT":
            $ Line = renpy.random.choice(["the danger room",
                        "the classroom",
                        "the pool",
                        "Scott's room",
                        "Kurt's room",
                        "Bobby's room",
                        "Logan's room",
                        "-|A|-'s room",
                        "an unmarked room with a single flickering bulb and odd staining patterns",
                        "the library",
                        "Xavier's study",
                        "the caffeteria"])
            $ Round -= 10
            show blackscreen onlayer black
            pause 0.1
            hide blackscreen onlayer black
            "You grab a package from McCoy and deliver it to [Line]."
            $ Line = renpy.random.choice(["a refridgerator",
                        "a microwave",
                        "a sex doll. That's awkward",
                        "a sex doll. That makes sense",
                        "a car. Maybe you should have opened this outside?",
                        "a desk",
                        "a large bed",
                        "a crate full of wrapped white powder. Flour, probably",
                        "a giant pile of wrapped clothing",
                        "a giant crate of booze"])
            "It quickly grows into [Line]."
            $ Round -= 5
            $ Player.cash += 1
            show blackscreen onlayer black
            pause 0.1
            hide blackscreen onlayer black
            "You head back home."
        "Deliver a distant MT [[locked] (locked)" if Round < 50:
            pass
        "Deliver a distant MT" if Round >= 50:
            $ Line = renpy.random.choice(["the restaurant",
                        "the theater",
                        "a local boutique",
                        "mayor's house",
                        "the mall",
                        "the fire station",
                        "the other restaurant, the one you don't go to",
                        "the dance club",
                        "a broken down shack",
                        "the local highschool"])
            $ Round -= 20
            show blackscreen onlayer black
            pause 0.1
            hide blackscreen onlayer black
            "You grab a package from McCoy and deliver it to [Line]."
            $ Line = renpy.random.choice(["a refridgerator",
                        "a microwave",
                        "a sex doll. That's awkward",
                        "a sex doll. That makes sense",
                        "a car. Maybe you should have opened this outside?",
                        "a sofa",
                        "a large bed",
                        "a crate full of wrapped white powder. Flour, probably",
                        "a giant pile of wrapped clothing",
                        "a giant crate of popcorn"])
            "It quickly grows into [Line]."
            $ Round -= 10
            $ Player.cash += 3
            show blackscreen onlayer black
            pause 0.1
            hide blackscreen onlayer black
            "You head back home."
        "Exit":
            return
    $ Player.daily_history.append("micro")
    return





label Girl_TightsRipped(Girl=0, Count=0):

    if Girl not in all_Girls:
        return
    if Girl.hose == "_tights":
        $ Count = 1
        $ Girl.hose = "ripped_tights"
        $ Girl.change_face("_angry")
    elif Girl.hose == "pantyhose":
        $ Count = 1
        $ Girl.hose = "ripped_pantyhose"
        $ Girl.change_face("_angry")
    else:

        return

    if "ripped_tights" in Girl.inventory or "ripped_pantyhose" in Girl.inventory:

        if Girl == RogueX:
            ch_r "Damnation, that's another pair ruined!"
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

        if not Girl.legs and Girl.underwear != "_shorts":
            if Girl == StormX and StormX in Rules:

                pass
            elif Girl.underwear:
                if Girl.SeenPanties:
                    $ Count = 3 if not approval_check(Girl, 600) else Count
                else:
                    $ Girl.SeenPanties = 1
                    $ Count = 3 if not approval_check(Girl, 900) else Count
                $ Girl.change_stat("lust", 60, 2)
            else:
                if Girl.SeenPussy:
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
                    $ Girl.inventory.append(Girl.hose)
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
            call Remove_Girl (Girl)
            $ Girl.change_outfit()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
