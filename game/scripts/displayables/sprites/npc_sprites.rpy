layeredimage Xavier_sprite:
    always:
        "images/NPC/Xavier_body.png"

    always:
        "images/NPC/Xavier_brows_[Xavier.brows].png"

    always:
        "images/NPC/Xavier_mouth_[Xavier.mouth].png"

    if Xavier.eyes == "closed":
        "images/NPC/Xavier_eyes_[Xavier.eyes].png"
    else:
        "Xavier_blinking"

    if Xavier.psychic:
        "images/NPC/Xavier_psychic.png"

    anchor (0.5, 0.0) offset (60, 355) zoom 0.7

image Xavier_blinking:
    "images/NPC/Xavier_eyes_[Xavier.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/NPC/Xavier_eyes_half.png"
    0.05
    "images/NPC/Xavier_eyes_closed.png"
    0.15
    "images/NPC/Xavier_eyes_half.png"
    0.05
    repeat
