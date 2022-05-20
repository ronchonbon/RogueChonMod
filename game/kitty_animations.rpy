image Kitty_blinking:
    "Kitty_eyes"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Kitty_sprite/Kitty_standing_eyes_squint.png"
    0.05
    "images/Kitty_sprite/Kitty_standing_eyes_closed.png"
    0.15
    "images/Kitty_sprite/Kitty_standing_eyes_squint.png"
    0.05
    repeat

image Kitty_squinting:
    "images/Kitty_sprite/Kitty_standing_eyes_sexy.png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Kitty_sprite/Kitty_standing_eyes_squint.png"
    0.25
    repeat

image Kitty_sex_animation:
    LiveComposite(
        (1120,840),
        (0, 0), ConditionSwitch(
            "not Player.sprite", "Kitty_sex_body_Anim0",
            "Player.cock_position in ['sex', 'anal']", "Kitty_sex_body_Anim[action_speed]",
            "Player.cock_position == 'footjob'", "Kitty_sex_body_FootAnim[action_speed]",
            "Player.cock_position == 'out' and action_speed >= 2", "Kitty_Hotdog_Body_Anim2",
            "True", "Kitty_sex_body_Anim0"),
        (0, 0), ConditionSwitch(
            "not Player.sprite", "Kitty_sex_legs_Anim0",
            "Player.cock_position in ['sex', 'anal']", "Kitty_sex_legs_Anim[action_speed]",
            "Player.cock_position == 'footjob'", "Kitty_sex_legs_FootAnim[action_speed]",
            "Player.cock_position == 'out' and action_speed >= 2", "Kitty_Hotdog_Legs_Anim2",
            "True", "Kitty_sex_legs_Anim0"))

    align (0.6, 1.3) zoom 0.7
