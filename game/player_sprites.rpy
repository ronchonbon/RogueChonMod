image Zero_hand:
    "images/UI_Hand.png"

    anchor (0.5, 0.5)

image Zero_hand_under:
    "images/UI_HandUnder.png"

    anchor (0.5, 0.5)

image Zero_finger:
    "images/UI_Finger.png"

    anchor (0.5, 0.5)

image Zero_tongue:
    "images/UI_Tongue.png"

    anchor (0.5, 0.5)

image Zero_handjob_cock:
    "images/Player/Zero_handjob_cock_[Player.color].png"

    anchor (0.5, 0.5)

layeredimage Zero_blowjob_cock:
    always:
        "images/Player/Zero_blowjob_cock_[Player.color].png"

    if Player.cock_wet:
        "images/Player/Zero_blowjob_wet_cock.png"

    if Player.spunk:
        "images/Player/Zero_blowjob_spunk_cock.png"

    anchor (0.5, 0.5)

image Zero_sex_finger:
    "images/UI_Fingering.png"

    anchor (0.5, 0.5)

layeredimage Zero_doggy_cock_out:
    always:
        "images/Player/Zero_doggy_cock_[Player.color].png"

    if Player.cock_wet:
        "images/Player/Zero_doggy_wet_cock.png"

    anchor (0.5, 0.5)

layeredimage Zero_doggy_cock_in:
    always:
        "images/Player/Zero_doggy_cock_[Player.color]_in.png"

    if Player.cock_wet:
        "images/Player/Zero_doggy_wet_cock_in.png"

    if Player.spunk:
        "images/Player/Zero_doggy_spunk_cock_in.png"

    anchor (0.5, 0.5)
