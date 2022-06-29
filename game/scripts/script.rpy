define ch_p = Character('[Player.name]', color = "#87CEEB", show_two_window = True)

define ch_r = Character('[RogueX.name]', color = "#85bb65", image = "Rogue_sprite", show_two_window = True)
define ch_k = Character('[KittyX.name]', color = "#F5A9D0", image = "Kitty_sprite", show_two_window = True)
define ch_e = Character('[EmmaX.name]', color = "#98bee7", image = "Emma_sprite", show_two_window = True)
define ch_l = Character('[LauraX.name]', color = "#d8b600", image = "Laura_sprite", show_two_window = True)
define ch_j = Character('[JeanX.name]', color = "#b2d950", image = "Jean_sprite", show_two_window = True)
define ch_s = Character('[StormX.name]', color = "#b2d950", image = "Storm_sprite", show_two_window = True)
define ch_v = Character('[JubesX.name]', color = "#b2d950", image = "Jubes_sprite", show_two_window = True)
define ch_m = Character('[MystiqueX.name]', color = "b2d950", image = "Mystique_sprite", show_two_window = True)

define ch_x = Character('Professor X', color = "#a09400", image = "Xavier_sprite", show_two_window = True)
define ch_b = Character('Dr. McCoy', color = "#1033b2", show_two_window = True)

define ch_u = Character('???', color = "#85bb65", show_two_window = True)

label splashscreen:
    return

init -1:

    default day = 1
    default round = 100
    default time_options = ["morning", "midday", "evening", "night", "night"]
    default time_index = 2
    default current_time = time_options[time_index]
    default week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default weekday = 6
    default day_of_week = week[weekday]

    default focused_Girl = None
    default Partner = None
    default Present = []
    default Nearby = []
    default all_Girls = []
    default active_Girls = []

    default Rules = []

    default total_SEXP = 0

    default bedrooms = ["bg_player"]

    default taboo = 0

    default action_context = None
    default multi_action = True
    default action_speed = 0

    default girl_secondary_action = None
    default second_girl_main_action = None
    default second_girl_secondary_action = None

    default position_timer = 100

    default shop_inventory = []
    default inventory_count = 0

    default stack_depth = 0

    default Events = []

    default being_punished = 0

    default approval_bonus = 0
    default approval = 0

    default between_event_count = 0
    default stored_count = 0
    default counter = 0

    default achievements = []

    default show_feet = False

    default always_return_to_room = True

    default stage_far_far_left = 0.15
    default stage_far_left = 0.25
    default stage_left = 0.35
    default stage_center = 0.5
    default stage_right = 0.65
    default stage_far_right = 0.75
    default stage_far_far_right = 0.85

    default number_of_holders = 1

    default Xavier_brows = "happy"
    default Xavier_eyes = "happy"
    default Xavier_mouth = "smile"
    default Xavier_psychic = False
    default Xavier_emotion = "happy"
    default Xavier_location = stage_center

    default Gwen_name = "????"

    default door_locked = False

    default simulation = False

    default menu_context = None

    define hand_actions = ["massage", "fondle_thighs", "fondle_breasts", "fondle_pussy", "finger_pussy", "fondle_ass", "finger_ass"]
    define finger_actions = ["finger_pussy", "finger_ass"]
    define mouth_actions = ["kiss", "suck_breasts", "eat_pussy", "eat_ass"]
    define cock_actions = ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"]
    define dildo_actions = ["dildo_pussy", "dildo_ass"]
    define breast_actions = ["fondle_breasts", "suck_breasts"]
    define pussy_actions = ["fondle_pussy", "finger_pussy", "eat_pussy", "dildo_pussy"]
    define ass_actions = ["fondle_ass", "finger_ass", "eat_ass", "dildo_ass"]

    define active_actions = ["massage", "kiss", "fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]
    define passive_actions = ["striptease", "masturbation", "handjob", "footjob", "titjob", "blowjob"]
    define fondle_actions = ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
    define job_actions = ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]
    define sex_actions = ["sex", "anal", "hotdog"]

    define below_actions = ["fondle_thighs", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"]
    define inside_panties_actions = ["finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"]
    define insertion_actions = ["finger_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]
    define pussy_insertion_actions = ["finger_pussy", "dildo_pussy", "sex"]
    define anal_insertion_actions = ["finger_ass", "dildo_ass", "anal"]
    define contact_actions = ["massage", "kiss", "fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_ass", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"]
    define kinky_actions = ["masturbation", "finger_ass", "eat_ass", "titjob", "footjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]

    define all_actions = ["massage", "kiss",
        "striptease", "masturbation",
        "fondle_thighs",
        "fondle_breasts", "suck_breasts",
        "fondle_pussy", "finger_pussy", "eat_pussy",
        "fondle_ass", "finger_ass", "eat_ass",
        "handjob", "footjob", "titjob", "blowjob",
        "dildo_pussy", "dildo_ass",
        "sex", "anal", "hotdog"]

    define Emma_harden = ImageDissolve("images/wipes/Emma_harden.jpg", 0.5, 8)
    define Mystique_dissolve = ImageDissolve("images/wipes/Mystique_dissolve.jpg", 1.0, 8)

label start:
    python:
        renpy.start_predict("images/backgrounds/*.*")

        for G in all_Girls:
            renpy.start_predict("images/" + G.tag + "_standing/*.*")

    $ Player = PlayerClass()

    python:
        Player.name = renpy.input("What is your name?", default = "Zero", length = 10)
        Player.name = Player.name.strip()

        if not Player.name :
            Player.name  = "Zero"

    menu:
        "What is your skin color?"
        "Green":
            $ Player.color = "green"
        "White":
            $ Player.color = "white"
        "Black":
            $ Player.color = "black"

    $ RogueX = GirlClass("Rogue", 500, 0, 0, 10)
    $ KittyX = GirlClass("Kitty", 400, 100, 0, 10)
    $ EmmaX = GirlClass("Emma", 300, 0, 200, 15)
    $ LauraX = GirlClass("Laura", 400, 0, 200, 10)
    $ JeanX = GirlClass("Jean", 0, 0, 1000, 10)
    $ StormX = GirlClass("Storm", 500, 0, 100, 10)
    $ JubesX = GirlClass("Jubes", 500, 50, 50, 10)
    $ MystiqueX = GirlClass("Mystique", 0, 0, 0, 15)

    $ focused_Girl = RogueX

    show screen status_screen
    show screen inventory_button

    $ Player.cash = 100000

    # show Jubes_sprite titjob at sprite_location(0.5)
    # $ action_speed = 2
    #
    # ""

    # $ time_index = 2
    # $ current_time = time_options[time_index]
    #
    # $ Player.location = "bg_campus"
    #
    # scene background onlayer background
    # scene
    #
    # show midground zorder 2
    # show foreground zorder 4
    # show cover zorder 7
    # show Chibi_cock onlayer screens
    #
    # $ exit = False
    #
    # show Rogue_sprite standing at sprite_location(stage_left)
    # show Kitty_sprite standing at sprite_location(stage_right)
    #
    # while not exit:
    #     menu:
    #         "First casual outfit":
    #             $ new_Outfit_name = "first_casual"
    #         "Second casual outfit":
    #             $ new_Outfit_name = "second_casual"
    #         "Gym clothes":
    #             $ new_Outfit_name = "gym_clothes"
    #         "Swimwear":
    #             $ new_Outfit_name = "swimwear"
    #         "Sleepwear":
    #             $ new_Outfit_name = "sleepwear"
    #         "Shower":
    #             $ new_Outfit_name = "shower"
    #         "Halloween costume":
    #             $ new_Outfit_name = "Halloween_costume"
    #
    #     python:
    #         for G in [RogueX, KittyX]:
    #             G.Wardrobe.change_Outfit(new_Outfit_name)

    # $ MystiqueX.change_outfit("supervillain")
    #
    # python:
    #     for G in all_Girls:
    #         active_Girls.append(G)
    #
    # #         G.change_face("surprised", blushing = 2)
    # #         G.change_outfit("nude")
    # #         G.mouth = "smirk"
    # #         G.grool = 2
    # #         G.spunk["mouth"] = True
    # #         G.spunk["pussy"] = True
    # #         G.spunk["anus"] = True
    # #
    # # $ Player.sprite = True
    # # $ show_feet = False
    # # $ action_speed = 2
    # #
    # # $ Player.cock_position = "anal"
    # # $ Player.primary_action = "fondle_breasts"
    # # $ Player.secondary_action = "fondle_thighs"
    # #
    # # $ girl_secondary_action = "finger_pussy"
    #
    # $ location = "bg_campus"
    # $ time_index = 0
    # $ exit = False
    #
    # while not exit:
    #     call add_Girls([RogueX, LauraX, MystiqueX], static = True)
    #
    #     menu:
    #         "Location":
    #             menu:
    #                 "Player's room":
    #                     $ Player.location = "bg_player"
    #                 "Campus":
    #                     $ Player.location = "bg_campus"
    #                 "Classroom":
    #                     $ Player.location = "bg_classroom"
    #                 "Danger Room":
    #                     $ Player.location = "bg_dangerroom"
    #                 "Showers":
    #                     $ Player.location = "bg_showerroom"
    #                 "Pool":
    #                     $ Player.location = "bg_pool"
    #                 "Restaurant":
    #                     $ Player.location = "bg_restaurant"
    #                 "Movie theater":
    #                     $ Player.location = "bg_movies"
    #                 "Back":
    #                     pass
    #         "Time":
    #             menu:
    #                 "Morning":
    #                     $ time_index = 0
    #                     $ current_time = time_options[time_index]
    #                 "Midday":
    #                     $ time_index = 1
    #                     $ current_time = time_options[time_index]
    #                 "Evening":
    #                     $ time_index = 2
    #                     $ current_time = time_options[time_index]
    #                 "Night":
    #                     $ time_index = 3
    #                     $ current_time = time_options[time_index]
    #                 "Lights off":
    #                     $ time_index = 4
    #                     $ current_time = time_options[time_index]
    #                 "Back":
    #                     pass
    #         "Exit":
    #             $ exit = True
    #
    # call hide_all
    #
    # python:
    #     for G in all_Girls:
    #         G.location = "hold"
    #
    # $ active_Girls = []
    # $ focused_Girl = RogueX

    jump prologue

return
