init python:

    def check_girl(Girl, local = False):
        global focused_Girl

        if Girl in all_Girls and (not local or bg_current == Check.location):
            return Girl
        elif bg_current == focused_Girl.location:
            return focused_Girl
        else:
            for Girl in all_Girls:
                if bg_current == Girl.location:
                    focused_Girl = Girl

                    return Girl





                    

label dildo_check(Girl):
    if "_dildo" in Player.inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "_dildo" in Girl.inventory:
        "You ask [Girl.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."

        return False

    return True

label vibrator_check(Girl):
    if "_vibrator" in Player.inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "_vibrator" in Girl.inventory:
        "You ask [Girl.name] to get out her vibrator."
    else:
        "You don't have one of those on you."

        return False

    return True












init python:

    def approval_check(Chr = 0, T = 1000, Type = "LOI", Spread = 150, TmpM = 1, TabM = 0, C = 1, Bonus = 0, Loc = 0, Check=0, Alt=[[],0]):
        if Chr not in all_Girls:
            return False

        while Alt[0]:

            if Chr in Alt[0]:
                T = Alt[1] if Alt[1] else T
            Alt[0].remove(Alt[0][0])

        L = Chr.love
        O = Chr.obedience
        I = Chr.inhibition
        Localtaboo = Chr.taboo
        Loc = Chr.location if not Loc else Loc

        if Chr == JeanX and (O <= 800 or JeanX.taboo):

            I = (I - JeanX.IX)

        if Loc == bg_current and C:

            if Chr == LauraX:
                if "mandrill" in Player.traits:
                    if L <= 400:
                        L += 600
                    else:
                        L = 1200
                    if "drugged" not in Chr.traits:
                        Chr.traits.append("drugged")
                elif "purple" in Player.traits:
                    if O <= 400:
                        O += 600
                    else:
                        O = 1200
                    if "drugged" not in Chr.traits:
                        Chr.traits.append("drugged")
                elif "corruption" in Player.traits:
                    if I <= 400:
                        I += 600
                    else:
                        I = 1200
                    if "drugged" not in Chr.traits:
                        Chr.traits.append("drugged")
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

        if Type == "LOI":
            Localtaboo = Localtaboo*10
            Localapproval_bonus = approval_bonus*10

        elif Type == "LO":


            I = 0
            Localtaboo = Localtaboo*6
            Localapproval_bonus = approval_bonus*6
        elif Type == "OI":
            L = 0
            Localtaboo = Localtaboo*6
            Localapproval_bonus = approval_bonus*6
        elif Type == "LI":
            O = 0
            Localtaboo = Localtaboo*6
            Localapproval_bonus = approval_bonus*6

        elif Type == "L":
            O = 0
            I = 0
            Localtaboo = Localtaboo*3
            Localapproval_bonus = approval_bonus*3
        elif Type == "O":
            L = 0
            I = 0
            Localtaboo = Localtaboo*3
            Localapproval_bonus = approval_bonus*3
        elif Type == "I":
            O = 0
            L = 0
            Localtaboo = Localtaboo*3
            Localapproval_bonus = approval_bonus*3

        else:
            Localtaboo = Localtaboo*10
            Localapproval_bonus = approval_bonus*10

        TabM = 0 if TabM <= 0 else TabM

        if Check:

            Check = (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*Localtaboo))
            return Check

        if (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*Localtaboo)) >= (T + (2*Spread)):

            return 3
        elif (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*Localtaboo)) >= (T + Spread):

            return 2
        elif (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*Localtaboo)) >= T:

            return True
        else:
            return False




    def Room_Full(Here = [],temp_Girls=[]):


        global Party
        Here = []
        while len(Party) > 2:


            Party.remove(Party[2])




        temp_Girls = all_Girls[:]
        while temp_Girls:
            if temp_Girls[0].location == bg_current and temp_Girls[0] not in Party:
                Here.append(temp_Girls[0])
            temp_Girls.remove(temp_Girls[0])
        if len(Party) + len(Here) >= 2:
            return True
        else:
            return False



    def AloneCheck(Girl=0,temp_Girls=[]):


        temp_Girls = all_Girls[:]
        if Girl and Girl in all_Girls:
            temp_Girls.remove(Girl)
        while temp_Girls:
            if temp_Girls[0].location == bg_current:
                return False
            temp_Girls.remove(temp_Girls[0])
        return True





label CheatCheck(temp_Girls=[], temp_Girls2=[]):







    $ temp_Girls = all_Girls[:]
    $ renpy.random.shuffle(temp_Girls)
    while temp_Girls:
        if "locked" in Player.traits and temp_Girls[0].location != bg_current:

            pass
        else:
            $ temp_Girls2 = all_Girls[:]
            while temp_Girls2:
                if "meet girl" in Player.daily_history:

                    return
                elif temp_Girls[0] in Player.Harem:

                    if "saw with " + temp_Girls2[0].tag in temp_Girls[0].traits:

                        if temp_Girls[0] in Player.Harem and temp_Girls2[0] in Player.Harem:

                            $ temp_Girls[0].drain_word("saw with "+temp_Girls2[0].tag,0,0,1)
                        elif temp_Girls[0] in Player.Harem and temp_Girls2[0].tag + "Yes" in Player.traits:
                            $ temp_Girls[0].drain_word("saw with "+temp_Girls2[0].tag,0,0,1)
                        elif bg_current == "bg_player" or bg_current == temp_Girls[0].home:
                            call Cheated (temp_Girls[0], temp_Girls2[0])
                            $ renpy.pop_call()
                            return
                $ temp_Girls2.remove(temp_Girls2[0])
        $ temp_Girls.remove(temp_Girls[0])
    return

label ShareCheck(temp_Girls=[], temp_Girls2=[]):





    $ temp_Girls = all_Girls[:]
    $ temp_Girls.remove(StormX)
    while temp_Girls:
        if temp_Girls[0] in Player.Harem:

            $ temp_Girls2 = all_Girls[:]
            $ temp_Girls2.remove(StormX)
            while temp_Girls2:
                if "ask " + temp_Girls2[0].tag in temp_Girls[0].traits:

                    if temp_Girls[0] in Player.Harem and temp_Girls2[0] in Player.Harem:

                        $ temp_Girls[0].drain_word("ask "+temp_Girls2[0].tag,0,0,1)
                    else:
                        call Share (temp_Girls[0], temp_Girls2[0])
                        $ renpy.pop_call()
                        return
                $ temp_Girls2.remove(temp_Girls2[0])
        $ temp_Girls.remove(temp_Girls[0])
    return

label check_addiction:
    $ temp_Girls = active_Girls[:]

    $ renpy.random.shuffle(temp_Girls)

    if JubesX in temp_Girls and JubesX.addiction >= 40 and temp_Girls[0].resistance:
        $ temp_Girls.remove(JubesX)

        if "sunshine" not in JubesX.history or "addiction" in JubesX.daily_history:
            pass
        elif bg_current == JubesX.home or bg_current == "bg_player":
            if not JubesX.resistance:
                call addiction_event(JubesX)
            else:
                call addiction_fix(JubesX)
        else:
            if "asked_to_meet" in JubesX.daily_history:
                pass
            elif "asked_to_meet" in JubesX.daily_history and JubesX.addiction >= 60:
                "[JubesX.name] texts you. . ."

                JubesX.voice "I know I asked to meet you in your room earlier, but I really need a fix."

                $ Player.add_word(1,"asked_for_fix",0,0,0)
                $ JubesX.add_word(1,"asked_to_meet","asked_to_meet",0,0)

                call return_to_room

                return
            else:
                "[JubesX.name] texts and asks if you could get her a fix later."

                $ JubesX.add_word(1,"asked_to_meet","asked_to_meet",0,0)

                call return_to_room

                return
    while temp_Girls:
        if "locked" in Player.traits and temp_Girls[0].location != bg_current:
            pass
        elif "asked_for_fix" in Player.daily_history and "asked_to_meet" not in temp_Girls[0].daily_history:
            pass
        elif temp_Girls[0].event_happened[3]:
            pass
        elif "_angry" not in temp_Girls[0].recent_history and "addiction" not in temp_Girls[0].daily_history and temp_Girls[0].remaining_actions >= 1:
            if (temp_Girls[0].addiction >= 60 or (temp_Girls[0].addiction >= 40 and temp_Girls[0] == JubesX)) and temp_Girls[0].resistance:
                if bg_current == temp_Girls[0].home or bg_current == "bg_player":
                    call addiction_fix(temp_Girls[0])
                else:
                    if "asked_to_meet" in temp_Girls[0].recent_history:
                        pass
                    elif "asked_to_meet" in temp_Girls[0].daily_history and temp_Girls[0].addiction >= 80:
                        "[temp_Girls[0].name] texts you. . ."

                        temp_Girls[0].voice "I know I asked to meet you in your room earlier, but I'm serious, this is important."

                        $ Player.add_word(1,"asked_for_fix",0,0,0)

                        $ temp_Girls[0].add_word(1,"asked_to_meet","asked_to_meet",0,0)

                        call return_to_room

                        return
                    else:
                        "[temp_Girls[0].name] texts and asks if you could meet her in your room later."

                        $ temp_Girls[0].add_word(1,"asked_to_meet","asked_to_meet",0,0)

                        call return_to_room

                        return
            elif temp_Girls[0].resistance:
                pass
            elif temp_Girls[0] == JubesX and temp_Girls[0].addiction < 50:
                pass
            elif temp_Girls[0].addiction >= 35 and not temp_Girls[0].event_happened[1]:
                call addiction_event(temp_Girls[0])
            elif temp_Girls[0].addiction >= 60 and temp_Girls[0].event_happened[1] <= 2:
                call addiction_event(temp_Girls[0])
            elif temp_Girls[0].addiction >= 90:
                call addiction_event(temp_Girls[0])

        if len(temp_Girls) > 0:
            $ temp_Girls.remove(temp_Girls[0])

    return
