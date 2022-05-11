image setting:
    contains:
        ConditionSwitch(
            "Time_Count >= 3", "images/sky_night.jpg",
            "Time_Count == 2", "images/sky_sunset.jpg",
            "True", "images/sky_day.jpg"),

    contains:
        ConditionSwitch(
            "bg_current == 'bg study'", "images/study.jpg",
            "bg_current == 'bg player'", "images/playerroom.png",
            "bg_current == 'bg dangerroom'", "images/dangerroom.jpg",
            "bg_current == 'bg showerroom'", "images/Shower.jpg",
            "bg_current == 'bg rogue'", "images/Rogueroom.png",
            "bg_current == 'bg movies'", "images/Movies.jpg",
            "bg_current == 'bg restaurant'", "images/Restaurant.jpg",
            "bg_current == 'bg kitty'", "images/kittyroom.png",
            "bg_current == 'bg emma'", "images/emmaroom.png",
            "Time_Count >= 3", "images/Crossroads_Night.jpg",
            "Time_Count == 2", "images/Crossroads_Evening.jpg",
            "True", "images/Crossroads_Day.jpg")

image bg_entry = "images/Door.jpg"
image bg_halloween = "images/HalloweenParty.jpg"
image bg_danger = "images/dangerroom.jpg"
image bg_shower = "images/Shower.jpg"
image bg_movies = "images/Movies.jpg"
image bg_rest = "images/Restaurant.jpg"
image bg_shop = "images/Shop.jpg"
image bg_dressing = "images/Dressingroom.jpg"
image bg_playermask = "images/playerroom.png"
image bg_roguemask = "images/Rogueroom.png"
image bg_kittymask = "images/kittyroom.png"
image bg_emmamask = "images/emmaroom.png"
image bg_lauramask = "images/lauraroom.png"
image bg_jeanmask = "images/jeanroom.png"
image bg_stormmask = "images/stormroom_day.png"
image bg_jubesmask = "images/jubesroom.png"
image bg_classmask = "images/Classroom.jpg"

image bg_sky:
    contains:
        ConditionSwitch(
            "Time_Count >= 3", "images/sky_night.jpg",
            "Time_Count == 2", "images/sky_sunset.jpg",
            "True", "images/sky_day.jpg")

image bg_player:
    contains:
        "bg_sky"
    contains:
        "images/playerroom.png"

image bg_rogue:
    contains:
        "bg_sky"
    contains:
        "images/rogueroom.png"

image bg_kitty:
    contains:
        "bg_sky"
    contains:
        "images/kittyroom.png"

image bg_emma:
    contains:
        "bg_sky"
    contains:
        "images/emmaroom.png"

image bg_laura:
    contains:
        "bg_sky"
    contains:
        "images/lauraroom.png"

image bg_jean:
    contains:
        "bg_sky"
    contains:
        "images/jeanroom.png"

image bg_storm:
    contains:
        ConditionSwitch(
            "Time_Count >= 3", "images/stormroom_night.png",
            "Time_Count == 2", "images/stormroom_evening.png",
            "True", "images/stormroom_day.png")

image bg_jubes:
    contains:
         "images/jubesroom.png",

image bg_campus:
    contains:
        ConditionSwitch(
            "Time_Count >= 3", "images/Campus_Night.png",
            "Time_Count == 2", "images/Campus_Evening.png",
            "True", "images/Campus_Day.png")

image bg_pool:
    contains:
        ConditionSwitch(
            "Time_Count >= 3", "images/pool_night.png",
            "Time_Count == 2", "images/pool_evening.png",
            "True", "images/pool_day.png")

image bg_class:
    contains:
        "images/Classroom.jpg"
    contains:
        ConditionSwitch(
            "EmmaX.Loc == 'bg teacher' and 'frisky' in EmmaX.RecentActions", "Emma_Behind_Podium",
            "EmmaX.Loc == 'bg teacher'", "Emma_At_Podium",
            "EmmaX.Loc == 'bg desk'", "Emma_At_Desk",
            "StormX.Loc == 'bg teacher' and 'frisky' in StormX.RecentActions", "Storm_Behind_Podium",
            "StormX.Loc == 'bg teacher'", "Storm_At_Podium",
            "StormX.Loc == 'bg desk'", "Storm_At_Desk",
            "True", Null())
    contains:
        "images/ClassroomFront.png"
    contains:
        ConditionSwitch(
            "bg_current != 'bg classroom' or Time_Count >= 2 or Weekday >= 5", Null(),
            "True", "images/ClassroomPupils.png")

image empty_class:
    contains:
        "images/Classroom.jpg"

image bg_study:
    contains:
        ConditionSwitch(
            "Time_Count > 2", "images/StudyNight.jpg",
            "True", "images/StudyDay.jpg")

image bg_mall:
    contains:
        ConditionSwitch(
            "Time_Count > 1", "images/mall_night.png",
            "True", "images/mall_day.png")

label display_background(entering = False):
    if entering:
        scene bg_entry onlayer backdrop
    elif bg_current == "bg player":
        scene bg_player onlayer backdrop
    elif bg_current == "bg rogue":
        scene bg_rogue onlayer backdrop
    elif bg_current == "bg kitty":
        scene bg_kitty onlayer backdrop
    elif bg_current == "bg emma":
        scene bg_emma onlayer backdrop
    elif bg_current == "bg laura":
        scene bg_laura onlayer backdrop
    elif bg_current == "bg jean":
        scene bg_jean onlayer backdrop
    elif bg_current == "bg storm":
        scene bg_storm onlayer backdrop
    elif bg_current == "bg jubes":
        scene bg_jubes onlayer backdrop
    elif bg_current == "bg classroom":
        scene bg_class onlayer backdrop
    elif bg_current == "bg dangerroom":
        scene bg_danger onlayer backdrop
    elif bg_current == "bg showerroom":
        scene bg_shower onlayer backdrop
    elif bg_current == "bg study":
        scene bg_study onlayer backdrop
    elif bg_current == "bg movies":
        scene bg_movies onlayer backdrop
    elif bg_current == "bg restaurant":
        scene bg_rest onlayer backdrop
    elif bg_current == "bg pool":
        scene bg_pool onlayer backdrop
    elif bg_current == "bg mall":
        scene bg_mall onlayer backdrop
    elif bg_current == "bg shop":
        scene bg_shop onlayer backdrop
    elif bg_current == "bg dressing":
        scene bg_dressing onlayer backdrop
    elif bg_current == "HW Party":
        scene bg_halloween onlayer backdrop
    else:
        scene bg_campus onlayer backdrop

    scene

    return

label RoomMask:
    if bg_current == "bg player":
        show bg_playermask onlayer black:
            alpha 0.2
    elif bg_current == "bg rogue":
        show bg_roguemask onlayer black:
            alpha 0.2
    elif bg_current == "bg kitty":
        show bg_kittymask onlayer black:
            alpha 0.2
    elif bg_current == "bg emma":
        show bg_emmamask onlayer black:
            alpha 0.2
    elif bg_current == "bg laura":
        show bg_lauramask onlayer black:
            alpha 0.2
    elif bg_current == "bg jean":
        show bg_jeanmask onlayer black:
            alpha 0.2
    elif bg_current == "bg storm":
        show bg_stormmask onlayer black:
            alpha 0.2
    elif bg_current == "bg jubes":
        show bg_jubesmask onlayer black:
            alpha 0.2
    return
