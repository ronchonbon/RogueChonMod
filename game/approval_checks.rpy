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
