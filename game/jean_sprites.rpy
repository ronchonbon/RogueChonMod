layeredimage Jean_kneeling:
    always:
        "images/Jean_kneeling/Jean_kneeling_back_hair[JeanX.outfit[back_hair]].png"

    if JeanX.bound:
        "images/Jean_kneeling/Jean_kneeling_right_arm_bound.png"
    else:
        "images/Jean_kneeling/Jean_kneeling_right_arm.png"

    if JeanX.bound and JeanX.whipped:
        "images/Jean_kneeling/Jean_kneeling_body_harness_whipped.png"
    elif JeanX.whipped:
        "images/Jean_kneeling/Jean_kneeling_body_whipped.png"
    elif JeanX.bound:
        "images/Jean_kneeling/Jean_kneeling_body_harness.png"
    else:
        "images/Jean_kneeling/Jean_kneeling_body.png"

    if JeanX.bound and JeanX.whipped:
        "images/Jean_kneeling/Jean_kneeling_legs_harness_whipped.png"
    elif JeanX.whipped:
        "images/Jean_kneeling/Jean_kneeling_legs_whipped.png"
    elif JeanX.bound:
        "images/Jean_kneeling/Jean_kneeling_legs_harness.png"
    else:
        "images/Jean_kneeling/Jean_kneeling_legs.png"

    if JeanX.bound:
        "images/Jean_kneeling/Jean_kneeling_left_arm_bound.png"
    else:
        "images/Jean_kneeling/Jean_kneeling_left_arm.png"

    # always:
    #     "images/Jean_kneeling/Jean_kneeling_head_reference.png"

    always:
        "Jean_Sprite_Head" pos (0.3526, 0.036) rotate -9.0 zoom 1.97

    if JeanX.outfit["makeup"]:
        "images/Jean_kneeling/Jean_kneeling_makeup[JeanX.outfit[makeup]].png"

    if JeanX.outfit["gag"]:
        "images/Jean_kneeling/Jean_kneeling_gag[JeanX.outfit[gag]].png"

    if JeanX.outfit["front_inner_accessory"]:
        "images/Jean_kneeling/Jean_kneeling_front_inner_accessory[JeanX.outfit[front_inner_accessory]].png"

    if JeanX.outfit["held_item"]:
        "images/Jean_kneeling/Jean_kneeling_held_item[JeanX.outfit[held_item]].png"

    anchor (0.5, -0.35) zoom 0.45
