image black_screen:
    Solid("#000000")

    on show:
        alpha 0.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

image rolling_steam_midground:
    "images/backgrounds/steam2.png"

    subpixel True
    xpos -1920
    block:
        linear 45.0 xpos 1920
        xpos -1920
        repeat

image rolling_steam_cover:
    "images/backgrounds/steam1.png"

    subpixel True
    xpos 1920
    block:
        linear 30.0 xpos -1920
        xpos 1920
        repeat

layeredimage background:
    always:
        "images/backgrounds/sky_[current_time].png"

    if (Player.location in bedrooms or Player.location in ["bg_classroom", "bg_dangerroom"]) and time_index == 4:
        At("images/backgrounds/[Player.location].png", lights_off)
    elif Player.location in ["bg_storm", "bg_campus", "bg_pool", "bg_study", "bg_mall"]:
        "images/backgrounds/[Player.location]_[current_time].png"
    else:
        "images/backgrounds/[Player.location].png"

layeredimage midground:
    if Player.location == "bg_shower":
        "rolling_steam_midground"

    if Player.location == "bg_pool":
        AlphaMask("images/backgrounds/[Player.location]_[current_time].png", "images/backgrounds/bg_pool_mask.png")

layeredimage foreground:
    if Player.location == "bg_classroom":
        "images/backgrounds/bg_classroom_front.png"

    if Player.location == "bg_classroom" and time_index < 2 and weekday < 5 and round > 15:
        "images/backgrounds/bg_classroom_pupils.png"

layeredimage cover:
    if Player.location == "bg_restaurant":
        "images/backgrounds/bg_restaurant_table.png"

    if Player.location == "bg_shower":
        "rolling_steam_cover" alpha 0.8
