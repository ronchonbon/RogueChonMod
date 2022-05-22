label forced_approval_checks(Girl, action):
    if action in ["masturbation"]:
        $ approval = approval_check(Girl, 450, "OI", TabM = 2)
    if action in ["fondle_thighs", "fondle_breasts"]:
        $ approval = approval_check(Girl, 350, "OI", TabM = 2)
    elif action in ["suck_breasts", "fondle_pussy"]:
        $ approval = approval_check(Girl, 450, "OI", TabM = 3)
    elif action in ["suck_breasts", "blowjob"]:
        $ approval = approval_check(Girl, 750, "OI", TabM = 3)
    elif action in ["eat_pussy"]:
        $ approval = approval_check(Girl, 750, "OI", TabM = 4)
    elif action in ["fondle_ass"]:
        $ approval = approval_check(Girl, 250, "OI", TabM = 3)
    elif action in ["finger_ass", "dildo_pussy"]:
        $ approval = approval_check(Girl, 950, "OI", TabM = 3)
    elif action in ["eat_ass"]:
        $ approval = approval_check(Girl, 1100, "OI", TabM = 4)
    elif action in ["handjob"]:
        $ approval = approval_check(Girl, 350, "OI", TabM = 3)
    elif action in ["footjob", "hotdog"]:
        $ approval = approval_check(Girl, 400, "OI", TabM = 3)
    elif action in ["titjob"]:
        $ approval = approval_check(Girl, 700, "OI", TabM = 4)
    elif action in ["dildo_ass"]:
        $ approval = approval_check(Girl, 1050, "OI", TabM = 3)
    elif action in ["sex"]:
        $ approval = approval_check(Girl, 1150, "OI", TabM = 3)
    elif action in ["anal"]:
        $ approval = approval_check(Girl, 1250, "OI", TabM = 3)

    return

label action_approval_checks(Girl, action):
    if action == "kiss":
        $ approval = approval_check(Girl, 700, TabM=1,Alt=[[RogueX,JeanX],500])
    elif action == "masturbation":
        $ approval = approval_check(Girl, 1200, TabM = 2)
    elif action == "fondle_thighs":
        $ approval = approval_check(Girl, 750, TabM=1)
    elif action == "fondle_breasts":
        $ approval = approval_check(Girl, 950, TabM = 3)
    elif action == "suck_breasts":
        $ approval = approval_check(Girl, 1050, TabM = 4)
    elif action == "fondle_pussy":
        if Girl in [EmmaX, LauraX, JeanX, StormX, JubesX] and Taboo and "public" not in Girl.history:
            $ approval_bonus -= 20

        if "no_fondle_pussy" in Girl.daily_history:
            $ approval_bonus -= 5
            $ approval_bonus -= 10 if "no_fondle_pussy" in Girl.recent_history else 0

        $ approval = approval_check(Girl, 1050, TabM = 2) # 105, 120, 135, Taboo -80(185)
    elif action == "finger_pussy":
        $ approval = approval_check(Girl, 1100, TabM = 2)
    elif action == "eat_pussy":
        $ approval = approval_check(Girl, 1250, TabM = 4) # 125, 140, 155, Taboo -160(285)
    elif action == "fondle_ass":
        $ approval = approval_check(Girl, 850, TabM=1, Alt = [[StormX], 750]) # 85, 100, 115, Taboo -40(125)
    elif action == "finger_ass":
        $ approval = approval_check(Girl, 1300, TabM = 3) # 130, 145, 160, Taboo -120(250)
    elif action == "eat_ass":
        $ approval = approval_check(Girl, 1550, TabM = 4) # 155, 170, 185, Taboo -160(315)
    elif action == "handjob":
        $ approval = approval_check(Girl, 1100, TabM = 3) # 110, 125, 140, Taboo -120(230)
    elif action == "footjob":
        $ approval = approval_check(Girl, 1250, TabM = 3) # 110, 125, 140, Taboo -120(230)
    elif action == "titjob":
        $ approval = approval_check(Girl, 1200, TabM = 5) # 120, 135, 150, Taboo -200(320)
    elif action == "blowjob":
        $ approval = approval_check(Girl, 1300, TabM = 4) # 130, 145, 160, Taboo -160(290)
    elif action == "dildo_pussy":
        $ approval = approval_check(Girl, 1250, TabM = 4) # 125, 140, 155, Taboo -160(335)
    elif action == "dildo_ass":
        $ approval = approval_check(Girl, 1450, TabM = 4) # 145, 160, 175, Taboo -160(355)
    elif action == "sex":
        $ approval = approval_check(Girl, 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)
    elif action == "anal":
        $ approval = approval_check(Girl, 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)
    elif action == "hotdog":
        $ approval = approval_check(Girl, 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    return
