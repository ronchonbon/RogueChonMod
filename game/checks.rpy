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
            return 0

        while Alt[0]:

            if Chr in Alt[0]:
                T = Alt[1] if Alt[1] else T
            Alt[0].remove(Alt[0][0])

        L = Chr.love
        O = Chr.obedience
        I = Chr.inhibition
        LocalTaboo = Chr.Taboo
        Loc = Chr.location if not Loc else Loc

        if Chr == JeanX and (O <= 800 or JeanX.Taboo):

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
            LocalTaboo = LocalTaboo*10
            Localapproval_bonus = approval_bonus*10

        elif Type == "LO":


            I = 0
            LocalTaboo = LocalTaboo*6
            Localapproval_bonus = approval_bonus*6
        elif Type == "OI":
            L = 0
            LocalTaboo = LocalTaboo*6
            Localapproval_bonus = approval_bonus*6
        elif Type == "LI":
            O = 0
            LocalTaboo = LocalTaboo*6
            Localapproval_bonus = approval_bonus*6

        elif Type == "L":
            O = 0
            I = 0
            LocalTaboo = LocalTaboo*3
            Localapproval_bonus = approval_bonus*3
        elif Type == "O":
            L = 0
            I = 0
            LocalTaboo = LocalTaboo*3
            Localapproval_bonus = approval_bonus*3
        elif Type == "I":
            O = 0
            L = 0
            LocalTaboo = LocalTaboo*3
            Localapproval_bonus = approval_bonus*3

        else:
            LocalTaboo = LocalTaboo*10
            Localapproval_bonus = approval_bonus*10

        TabM = 0 if TabM <= 0 else TabM

        if Check:

            Check = (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*LocalTaboo))
            return Check

        if (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*LocalTaboo)) >= (T + (2*Spread)):

            return 3
        elif (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*LocalTaboo)) >= (T + Spread):

            return 2
        elif (L + O + I + Bonus + (TmpM*Localapproval_bonus) - (TabM*LocalTaboo)) >= T:

            return 1
        else:
            return 0




    def Room_Full(Here = [],BO=[]):


        global Party
        Here = []
        while len(Party) > 2:


            Party.remove(Party[2])




        BO = all_Girls[:]
        while BO:
            if BO[0].location == bg_current and BO[0] not in Party:
                Here.append(BO[0])
            BO.remove(BO[0])
        if len(Party) + len(Here) >= 2:
            return 1
        else:
            return 0



    def AloneCheck(Girl=0,BO=[]):


        BO = all_Girls[:]
        if Girl and Girl in all_Girls:
            BO.remove(Girl)
        while BO:
            if BO[0].location == bg_current:
                return 0
            BO.remove(BO[0])
        return 1



    def GirlCheck(Check=0,Local=0,BO=[]):


        global focused_Girl
        if Check in all_Girls and (not Local or bg_current == Check.location):


            return Check
        elif bg_current == focused_Girl.location:

            return focused_Girl
        else:


            BO = all_Girls[:]
            while BO:
                if bg_current == BO[0].location:


                    focused_Girl = BO[0]
                    return BO[0]
                BO.remove(BO[0])
        ch_u("Tell Oni, no appropriate character was found.", interact=True)
        return focused_Girl


label CheatCheck(BO=[], BO2=[]):







    $ BO = all_Girls[:]
    $ renpy.random.shuffle(BO)
    while BO:
        if "locked" in Player.traits and BO[0].location != bg_current:

            pass
        else:
            $ BO2 = all_Girls[:]
            while BO2:
                if "meet girl" in Player.daily_history:

                    return
                elif BO[0] in Player.Harem:

                    if "saw with " + BO2[0].tag in BO[0].traits:

                        if BO[0] in Player.Harem and BO2[0] in Player.Harem:

                            $ BO[0].drain_word("saw with "+BO2[0].tag,0,0,1)
                        elif BO[0] in Player.Harem and BO2[0].tag + "Yes" in Player.traits:
                            $ BO[0].drain_word("saw with "+BO2[0].tag,0,0,1)
                        elif bg_current == "bg_player" or bg_current == BO[0].home:
                            call Cheated (BO[0], BO2[0])
                            $ renpy.pop_call()
                            return
                $ BO2.remove(BO2[0])
        $ BO.remove(BO[0])
    return

label ShareCheck(BO=[], BO2=[]):





    $ BO = all_Girls[:]
    $ BO.remove(StormX)
    while BO:
        if BO[0] in Player.Harem:

            $ BO2 = all_Girls[:]
            $ BO2.remove(StormX)
            while BO2:
                if "ask " + BO2[0].tag in BO[0].traits:

                    if BO[0] in Player.Harem and BO2[0] in Player.Harem:

                        $ BO[0].drain_word("ask "+BO2[0].tag,0,0,1)
                    else:
                        call Share (BO[0], BO2[0])
                        $ renpy.pop_call()
                        return
                $ BO2.remove(BO2[0])
        $ BO.remove(BO[0])
    return

label AddictCheck(BO=[]):


    $ BO = active_Girls[:]
    $ renpy.random.shuffle(BO)
    if JubesX in BO and JubesX.addiction >= 40 and BO[0].resistance:
        $ BO.remove(JubesX)
        if "sunshine" not in JubesX.history or "addiction" in JubesX.daily_history:
            pass
        elif bg_current == JubesX.home or bg_current == "bg_player":
            if not JubesX.resistance:

                call addiction_event (JubesX)
            else:
                call addiction_fix (JubesX)
        else:
            if "asked meet" in JubesX.daily_history:
                pass
            elif "asked meet" in JubesX.daily_history and JubesX.addiction >= 60:
                "[JubesX.name] texts you. . ."
                JubesX.voice "I know I asked to meet you in your room earlier, but I really need a fix."
                $ Player.add_word(1,"asked fix",0,0,0)
                $ JubesX.add_word(1,"asked meet","asked meet",0,0)
                call ReturnToRoom
                return
            else:
                "[JubesX.name] texts and asks if you could get her a fix later."
                $ JubesX.add_word(1,"asked meet","asked meet",0,0)
                call ReturnToRoom
                return
    while BO:
        if "locked" in Player.traits and BO[0].location != bg_current:

            pass
        elif "asked fix" in Player.daily_history and "asked meet" not in BO[0].daily_history:

            pass
        elif BO[0].Event[3]:

            pass
        elif "_angry" not in BO[0].recent_history and "addiction" not in BO[0].daily_history and BO[0].remaining_actions >= 1:

            if (BO[0].addiction >= 60 or (BO[0].addiction >= 40 and BO[0] == JubesX)) and BO[0].resistance:

                if bg_current == BO[0].home or bg_current == "bg_player":
                    call addiction_fix (BO[0])
                else:
                    if "asked meet" in BO[0].recent_history:
                        pass
                    elif "asked meet" in BO[0].daily_history and BO[0].addiction >= 80:
                        "[BO[0].name] texts you. . ."
                        BO[0].voice "I know I asked to meet you in your room earlier, but I'm serious, this is important."
                        $ Player.add_word(1,"asked fix",0,0,0)
                        $ BO[0].add_word(1,"asked meet","asked meet",0,0)
                        call ReturnToRoom
                        return
                    else:
                        "[BO[0].name] texts and asks if you could meet her in your room later."
                        $ BO[0].add_word(1,"asked meet","asked meet",0,0)
                        call ReturnToRoom
                        return

            elif BO[0].resistance:
                pass

            elif BO[0] == JubesX and BO[0].addiction < 50:
                pass
            elif BO[0].addiction >= 35 and not BO[0].Event[1]:

                call addiction_event (BO[0])
            elif BO[0].addiction >= 60 and BO[0].Event[1] <= 2:

                call addiction_event (BO[0])
            elif BO[0].addiction >= 90:

                call addiction_event (BO[0])
        $ BO.remove(BO[0])
    return
