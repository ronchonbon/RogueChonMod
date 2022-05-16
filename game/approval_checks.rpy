label forced_approval_checks(Girl, action):
    if action in ["fondle_thighs", "fondle_breasts"]:
        $ Approval = Approvalcheck(Girl, 350, "OI", TabM = 2)
    elif action in ["suck_breasts", "fondle_pussy"]:
        $ Approval = Approvalcheck(Girl, 450, "OI", TabM = 3)
    elif action in ["suck_breasts", "blowjob"]:
        $ Approval = Approvalcheck(Girl, 750, "OI", TabM = 3)
    elif action in ["eat_pussy"]:
        $ Approval = Approvalcheck(Girl, 750, "OI", TabM = 4)
    elif action in ["fondle_ass"]:
        $ Approval = Approvalcheck(Girl, 250, "OI", TabM = 3)
    elif action in ["finger_ass", "dildo_pussy"]:
        $ Approval = Approvalcheck(Girl, 950, "OI", TabM = 3)
    elif action in ["eat_ass"]:
        $ Approval = Approvalcheck(Girl, 1100, "OI", TabM = 4)
    elif action in ["handjob"]:
        $ Approval = Approvalcheck(Girl, 350, "OI", TabM = 3)
    elif action in ["footjob", "hotdog"]:
        $ Approval = Approvalcheck(Girl, 400, "OI", TabM = 3)
    elif action in ["titjob"]:
        $ Approval = Approvalcheck(Girl, 700, "OI", TabM = 4)
    elif action in ["dildo_ass"]:
        $ Approval = Approvalcheck(Girl, 1050, "OI", TabM = 3)
    elif action in ["sex"]:
        $ Approval = Approvalcheck(Girl, 1150, "OI", TabM = 3)
    elif action in ["anal"]:
        $ Approval = Approvalcheck(Girl, 1250, "OI", TabM = 3)

    return

label action_approval_checks(Girl, action):
    if action == "fondle_thighs":
        $ Approval = Approvalcheck(Girl, 750, TabM=1)
    elif action == "fondle_breasts":
        $ Approval = Approvalcheck(Girl, 950, TabM = 3)
    elif action == "suck_breasts":
        $ Approval = Approvalcheck(Girl, 1050, TabM = 4)
    elif action == "fondle_pussy":
        if Girl in [EmmaX, LauraX, JeanX, StormX, JubesX] and Taboo and "public" not in Girl.History:
            $ temp_modifier -= 20

        if "no_fondle_pussy" in Girl.daily_history:
            $ temp_modifier -= 5
            $ temp_modifier -= 10 if "no_fondle_pussy" in Girl.recent_history else 0

        $ Approval = Approvalcheck(Girl, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    elif action == "finger_pussy":
        $ Approval = Approvalcheck(Girl, 1100, TabM = 2)
    elif action == "eat_pussy":
        $ Approval = Approvalcheck(Girl, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    elif action == "fondle_ass":
        $ Approval = Approvalcheck(Girl, 850, TabM=1, Alt = [[StormX], 750]) # 85, 100, 115, Taboo -40(125)
    elif action == "finger_ass":
        $ Approval = Approvalcheck(Girl, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    elif action == "eat_ass":
        $ Approval = Approvalcheck(Girl, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    elif action == "handjob":
        $ Approval = Approvalcheck(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
    elif action == "footjob":
        $ Approval = Approvalcheck(Girl, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)
    elif action == "titjob":
        $ Approval = Approvalcheck(Girl, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)
    elif action == "blowjob":
        $ Approval = Approvalcheck(Girl, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)
    elif action == "dildo_pussy":
        $ Approval = Approvalcheck(Girl, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)
    elif action == "dildo_ass":
        $ Approval = Approvalcheck(Girl, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    elif action == "sex":
        $ Approval = Approvalcheck(Girl, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
    elif action == "anal":
        $ Approval = Approvalcheck(Girl, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    elif action == "hotdog":
        $ Approval = Approvalcheck(Girl, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)
