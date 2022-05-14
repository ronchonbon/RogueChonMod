label Slap_Ass(Girl = 0):  #rkeljsv
        if Girl not in all_Girls:
                return
        call Shift_Focus(Girl)
        # fix add sound here?
        call Punch

        $ Girl.Slap += 1 #add in slap-base obedience

        $ Girl.Blush = 2 if Taboo else 1
        if ApprovalCheck(Girl, 200, "O", TabM=1):
                $ Girl.change_face("sexy", 1)
                $ Girl.Mouth = "surprised"
                $ Girl.change_stat("lust", 51, 3, 1)
                $ Girl.change_stat("lust", 80, 1)
                if Girl.recent_history.count("slap") < 4:
                        $ Girl.change_stat("lust", 200, 1)
                        if Girl.Slap <= 5:
                                $ Girl.change_stat("obedience", 50, 2)
                        if Girl.Slap <= 10:
                                $ Girl.change_stat("obedience", 80, 1)
                "You slap her ass and she jumps with pleasure."
        else:
                $ Girl.change_face("surprised", 1)
                if Girl.recent_history.count("slap") < 4:
                        $ Girl.change_stat("obedience", 70, 2)
                        $ Girl.change_stat("love", 50, -1)
                "You slap her ass and she looks back at you a bit startled."

        if primary_action and Girl.lust >= 100:
                #If you're still going at it and Rogue can cum
                call Girl_Cumming(Girl)

        if Taboo:
                if not ApprovalCheck(Girl, 800, TabM=2):
                        if Girl.Slap <= 5:
                                $ Girl.change_stat("obedience", 80, 2)
                                $ Girl.change_stat("obedience", 50, 2)
                        $ Girl.change_stat("love", 70, -2)
                        $ Girl.change_stat("love", 50, -1)
                        "She looks pretty mad though."
                elif not ApprovalCheck(Girl, 1500, TabM=2):
                        if Girl.Slap <= 5:
                                $ Girl.change_stat("obedience", 80, 2)
                        $ Girl.change_stat("love", 70, -1)
                        "She looks a bit embarrassed."
                else:                         #Over 1500
                        $ Girl.change_face("sexy")
                        $ Girl.Mouth = "smile"
                        if Girl.Slap <= 5:
                                $ Girl.change_stat("obedience", 80, 1)
                        "She gives you a naughty grin."
                $ Girl.Blush = 1
        if Girl.PantsNum() < 5 and Girl.PantiesNum() < 5:
                if ApprovalCheck(Girl, 500, "O") and Girl.recent_history.count("slap") < 4:
                        $ Girl.change_stat("obedience", 90, 1)
                        $ Girl.change_stat("lust", 200, 3)
                else:
                        $ Girl.change_stat("lust", 80, 1)
                $ Girl.Addict -= 1
        $ Girl.recent_history.append("slap") if Girl.recent_history.count("slap") < 4 else Girl.recent_history
        $ Girl.daily_history.append("slap") if Girl.daily_history.count("slap") < 10 else Girl.daily_history
        return
