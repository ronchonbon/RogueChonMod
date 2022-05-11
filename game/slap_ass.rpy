label Slap_Ass(girl = 0):  #rkeljsv
        if girl not in TotalGirls:
                return
        call Shift_Focus(girl)
        # fix add sound here?
        call Punch

        $ girl.Slap += 1 #add in slap-base obedience

        $ girl.Blush = 2 if Taboo else 1
        if ApprovalCheck(girl, 200, "O", TabM=1):
                $ girl.FaceChange("sexy", 1)
                $ girl.Mouth = "surprised"
                $ girl.Statup("Lust", 51, 3, 1)
                $ girl.Statup("Lust", 80, 1)
                if girl.RecentActions.count("slap") < 4:
                        $ girl.Statup("Lust", 200, 1)
                        if girl.Slap <= 5:
                                $ girl.Statup("Obed", 50, 2)
                        if girl.Slap <= 10:
                                $ girl.Statup("Obed", 80, 1)
                "You slap her ass and she jumps with pleasure."
        else:
                $ girl.FaceChange("surprised", 1)
                if girl.RecentActions.count("slap") < 4:
                        $ girl.Statup("Obed", 70, 2)
                        $ girl.Statup("Love", 50, -1)
                "You slap her ass and she looks back at you a bit startled."

        if Trigger and girl.Lust >= 100:
                #If you're still going at it and Rogue can cum
                call girl_Cumming(girl)

        if Taboo:
                if not ApprovalCheck(girl, 800, TabM=2):
                        if girl.Slap <= 5:
                                $ girl.Statup("Obed", 80, 2)
                                $ girl.Statup("Obed", 50, 2)
                        $ girl.Statup("Love", 70, -2)
                        $ girl.Statup("Love", 50, -1)
                        "She looks pretty mad though."
                elif not ApprovalCheck(girl, 1500, TabM=2):
                        if girl.Slap <= 5:
                                $ girl.Statup("Obed", 80, 2)
                        $ girl.Statup("Love", 70, -1)
                        "She looks a bit embarrassed."
                else:                         #Over 1500
                        $ girl.FaceChange("sexy")
                        $ girl.Mouth = "smile"
                        if girl.Slap <= 5:
                                $ girl.Statup("Obed", 80, 1)
                        "She gives you a naughty grin."
                $ girl.Blush = 1
        if girl.PantsNum() < 5 and girl.PantiesNum() < 5:
                if ApprovalCheck(girl, 500, "O") and girl.RecentActions.count("slap") < 4:
                        $ girl.Statup("Obed", 90, 1)
                        $ girl.Statup("Lust", 200, 3)
                else:
                        $ girl.Statup("Lust", 80, 1)
                $ girl.Addict -= 1
        $ girl.RecentActions.append("slap") if girl.RecentActions.count("slap") < 4 else girl.RecentActions
        $ girl.DailyActions.append("slap") if girl.DailyActions.count("slap") < 10 else girl.DailyActions
        return
