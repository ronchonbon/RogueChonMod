layeredimage Zero_handjob_cock:
    always:
        "images/Player/Zero_handjob_cock_[Player.color].png"

    pos (200, 400) anchor (0.5, 1.0)

layeredimage Zero_titjob_cock:
    always:
        "images/Player/Zero_blowjob_cock_[Player.color].png"

    if Player.cock_wet:
        "images/Player/Zero_blowjob_spit_cock.png"

    if Player.spunk:
        "images/Player/Zero_blowjob_spunk_cock.png"

    anchor (0.5, 0.5) offset (5, 0) zoom 1.2

layeredimage Zero_blowjob_cock:
    always:
        "images/Player/Zero_blowjob_cock_[Player.color].png"

    if Player.cock_wet:
        "images/Player/Zero_blowjob_spit_cock.png"

    if Player.spunk:
        "images/Player/Zero_blowjob_spunk_cock.png"

    anchor (0.5, 0.5) offset (26, 350)

layeredimage Zero_doggy_cock_out:
    always:
        "images/Player/Zero_doggy_cock_[Player.color].png"

    if Player.cock_wet:
        "images/Player/Zero_doggy_grool_cock.png"

layeredimage Zero_doggy_cock_in:
    always:
        "images/Player/Zero_doggy_cock_[Player.color]_in.png"

    if Player.cock_wet:
        "images/Player/Zero_doggy_grool_cock_in.png"

    if Player.spunk:
        "images/Player/Zero_doggy_spunk_cock_in.png"
