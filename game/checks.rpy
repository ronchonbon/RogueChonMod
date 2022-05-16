label dildo_check(Girl):
    if "dildo" in Player.inventory:
        "You pull out a large rubber dildo. Lucky you remembered to keep it handy."
    elif "dildo" in Girl.inventory:
        "You ask [Girl.name] to get out her favorite Dildo."
    else:
        "You don't have one of those on you."

        return False

    return True

label vibrator_check(Girl):
    if "vibrator" in Player.inventory:
        "You pull out the \"shocker\" vibrator, handy."
    elif "vibrator" in Girl.inventory:
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
