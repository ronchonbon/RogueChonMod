label forced_Action_approval_checks(Girl, Action_type):
    if Action_type in ["masturbation"]:
        $ approval = approval_check(Girl, 450, "OI", taboo_modifier = 2)
    if Action_type in ["fondle_thighs", "fondle_breasts"]:
        $ approval = approval_check(Girl, 350, "OI", taboo_modifier = 2)
    elif Action_type in ["suck_breasts", "fondle_pussy"]:
        $ approval = approval_check(Girl, 450, "OI", taboo_modifier = 3)
    elif Action_type in ["suck_breasts", "blowjob"]:
        $ approval = approval_check(Girl, 750, "OI", taboo_modifier = 3)
    elif Action_type in ["eat_pussy"]:
        $ approval = approval_check(Girl, 750, "OI", taboo_modifier = 4)
    elif Action_type in ["fondle_ass"]:
        $ approval = approval_check(Girl, 250, "OI", taboo_modifier = 3)
    elif Action_type in ["finger_ass", "dildo_pussy"]:
        $ approval = approval_check(Girl, 950, "OI", taboo_modifier = 3)
    elif Action_type in ["eat_ass"]:
        $ approval = approval_check(Girl, 1100, "OI", taboo_modifier = 4)
    elif Action_type in ["handjob"]:
        $ approval = approval_check(Girl, 350, "OI", taboo_modifier = 3)
    elif Action_type in ["footjob", "hotdog"]:
        $ approval = approval_check(Girl, 400, "OI", taboo_modifier = 3)
    elif Action_type in ["titjob"]:
        $ approval = approval_check(Girl, 700, "OI", taboo_modifier = 4)
    elif Action_type in ["dildo_ass"]:
        $ approval = approval_check(Girl, 1050, "OI", taboo_modifier = 3)
    elif Action_type in ["sex"]:
        $ approval = approval_check(Girl, 1150, "OI", taboo_modifier = 3)
    elif Action_type in ["anal"]:
        $ approval = approval_check(Girl, 1250, "OI", taboo_modifier = 3)

    return approval

label Action_approval_checks(Girl, Action_type):
    if Action_type == "kiss":
        $ approval = approval_check(Girl, 700, taboo_modifier = 1, alternate_threshold = {RogueX: 500, JeanX: 500})
    elif Action_type == "masturbation":
        $ approval = approval_check(Girl, 1200, taboo_modifier = 2)
    elif Action_type == "fondle_thighs":
        $ approval = approval_check(Girl, 750, taboo_modifier = 1)
    elif Action_type == "fondle_breasts":
        $ approval = approval_check(Girl, 950, taboo_modifier = 3)
    elif Action_type == "suck_breasts":
        $ approval = approval_check(Girl, 1050, taboo_modifier = 4)
    elif Action_type == "fondle_pussy":
        $ approval = approval_check(Girl, 1050, taboo_modifier = 2)
    elif Action_type == "finger_pussy":
        $ approval = approval_check(Girl, 1100, taboo_modifier = 2)
    elif Action_type == "eat_pussy":
        $ approval = approval_check(Girl, 1250, taboo_modifier = 4)
    elif Action_type == "fondle_ass":
        $ approval = approval_check(Girl, 850, taboo_modifier = 1, alternate_threshold = {StormX: 750})
    elif Action_type == "finger_ass":
        $ approval = approval_check(Girl, 1300, taboo_modifier = 3)
    elif Action_type == "eat_ass":
        $ approval = approval_check(Girl, 1550, taboo_modifier = 4)
    elif Action_type == "handjob":
        $ approval = approval_check(Girl, 1100, taboo_modifier = 3)
    elif Action_type == "footjob":
        $ approval = approval_check(Girl, 1250, taboo_modifier = 3)
    elif Action_type == "titjob":
        $ approval = approval_check(Girl, 1200, taboo_modifier = 5)
    elif Action_type == "blowjob":
        $ approval = approval_check(Girl, 1300, taboo_modifier = 4)
    elif Action_type == "dildo_pussy":
        $ approval = approval_check(Girl, 1250, taboo_modifier = 4)
    elif Action_type == "dildo_ass":
        $ approval = approval_check(Girl, 1450, taboo_modifier = 4)
    elif Action_type == "sex":
        $ approval = approval_check(Girl, 1400, taboo_modifier = 5)
    elif Action_type == "anal":
        $ approval = approval_check(Girl, 1550, taboo_modifier = 5)
    elif Action_type == "hotdog":
        $ approval = approval_check(Girl, 1000, taboo_modifier = 3)

    return approval
