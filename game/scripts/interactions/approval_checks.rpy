label forced_approval_checks(Girl, action):
    if action in ["masturbation"]:
        $ approval = approval_check(Girl, 450, "OI", taboo_modifier = 2)
    if action in ["fondle_thighs", "fondle_breasts"]:
        $ approval = approval_check(Girl, 350, "OI", taboo_modifier = 2)
    elif action in ["suck_breasts", "fondle_pussy"]:
        $ approval = approval_check(Girl, 450, "OI", taboo_modifier = 3)
    elif action in ["suck_breasts", "blowjob"]:
        $ approval = approval_check(Girl, 750, "OI", taboo_modifier = 3)
    elif action in ["eat_pussy"]:
        $ approval = approval_check(Girl, 750, "OI", taboo_modifier = 4)
    elif action in ["fondle_ass"]:
        $ approval = approval_check(Girl, 250, "OI", taboo_modifier = 3)
    elif action in ["finger_ass", "dildo_pussy"]:
        $ approval = approval_check(Girl, 950, "OI", taboo_modifier = 3)
    elif action in ["eat_ass"]:
        $ approval = approval_check(Girl, 1100, "OI", taboo_modifier = 4)
    elif action in ["handjob"]:
        $ approval = approval_check(Girl, 350, "OI", taboo_modifier = 3)
    elif action in ["footjob", "hotdog"]:
        $ approval = approval_check(Girl, 400, "OI", taboo_modifier = 3)
    elif action in ["titjob"]:
        $ approval = approval_check(Girl, 700, "OI", taboo_modifier = 4)
    elif action in ["dildo_ass"]:
        $ approval = approval_check(Girl, 1050, "OI", taboo_modifier = 3)
    elif action in ["sex"]:
        $ approval = approval_check(Girl, 1150, "OI", taboo_modifier = 3)
    elif action in ["anal"]:
        $ approval = approval_check(Girl, 1250, "OI", taboo_modifier = 3)

    return approval

label action_approval_checks(Girl, action):
    if action == "kiss":
        $ approval = approval_check(Girl, 700, taboo_modifier=1,Alt=[[RogueX,JeanX],500])
    elif action == "masturbation":
        $ approval = approval_check(Girl, 1200, taboo_modifier = 2)
    elif action == "fondle_thighs":
        $ approval = approval_check(Girl, 750, taboo_modifier=1)
    elif action == "fondle_breasts":
        $ approval = approval_check(Girl, 950, taboo_modifier = 3)
    elif action == "suck_breasts":
        $ approval = approval_check(Girl, 1050, taboo_modifier = 4)
    elif action == "fondle_pussy":
        if Girl in [EmmaX, LauraX, JeanX, StormX, JubesX] and taboo and "public" not in Girl.history:
            $ approval_bonus -= 20

        if "no_fondle_pussy" in Girl.daily_history:
            $ approval_bonus -= 5
            $ approval_bonus -= 10 if "no_fondle_pussy" in Girl.recent_history else 0

        $ approval = approval_check(Girl, 1050, taboo_modifier = 2) # 105, 120, 135, taboo -80(185)
    elif action == "finger_pussy":
        $ approval = approval_check(Girl, 1100, taboo_modifier = 2)
    elif action == "eat_pussy":
        $ approval = approval_check(Girl, 1250, taboo_modifier = 4) # 125, 140, 155, taboo -160(285)
    elif action == "fondle_ass":
        $ approval = approval_check(Girl, 850, taboo_modifier=1, Alt = [[StormX], 750]) # 85, 100, 115, taboo -40(125)
    elif action == "finger_ass":
        $ approval = approval_check(Girl, 1300, taboo_modifier = 3) # 130, 145, 160, taboo -120(250)
    elif action == "eat_ass":
        $ approval = approval_check(Girl, 1550, taboo_modifier = 4) # 155, 170, 185, taboo -160(315)
    elif action == "handjob":
        $ approval = approval_check(Girl, 1100, taboo_modifier = 3) # 110, 125, 140, taboo -120(230)
    elif action == "footjob":
        $ approval = approval_check(Girl, 1250, taboo_modifier = 3) # 110, 125, 140, taboo -120(230)
    elif action == "titjob":
        $ approval = approval_check(Girl, 1200, taboo_modifier = 5) # 120, 135, 150, taboo -200(320)
    elif action == "blowjob":
        $ approval = approval_check(Girl, 1300, taboo_modifier = 4) # 130, 145, 160, taboo -160(290)
    elif action == "dildo_pussy":
        $ approval = approval_check(Girl, 1250, taboo_modifier = 4) # 125, 140, 155, taboo -160(335)
    elif action == "dildo_ass":
        $ approval = approval_check(Girl, 1450, taboo_modifier = 4) # 145, 160, 175, taboo -160(355)
    elif action == "sex":
        $ approval = approval_check(Girl, 1400, taboo_modifier = 5) # 135, 150, 165, taboo -200(335)
    elif action == "anal":
        $ approval = approval_check(Girl, 1550, taboo_modifier = 5) # 155, 170, 185, taboo -200(355)
    elif action == "hotdog":
        $ approval = approval_check(Girl, 1000, taboo_modifier = 3) # 100, 115, 130, taboo -120(220)

    return approval
