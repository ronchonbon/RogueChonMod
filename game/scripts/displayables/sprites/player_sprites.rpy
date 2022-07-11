image Zero_hand:
    "images/Player/Zero_hand.png"

    anchor (0.5, 0.5)

image Zero_hand_under:
    "images/Player/Zero_hand_under.png"

    anchor (0.5, 0.5)

image Zero_finger:
    "images/Player/Zero_finger.png"

    anchor (0.5, 0.5)

image Zero_tongue:
    "images/Player/Zero_tongue.png"

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
    "images/Player/Zero_sex_finger.png"

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

layeredimage Chibi_cock:
    if Player.cock_out or Player.naked:
        "images/Player/Chibi_cock_[Player.color].png"

    anchor (0.5, 0.5) offset (-850, -180) zoom 0.5
