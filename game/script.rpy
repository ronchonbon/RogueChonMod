image black_screen:
    Solid("#000000")
    on show:
        alpha 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

define ch_p = Character('[Player.name]', color = "#87CEEB", show_two_window = True)

define ch_r = Character('[RogueX.name]', color = "#85bb65", image = "Rogue_sprite", show_two_window = True)
define ch_k = Character('[KittyX.name]', color = "#F5A9D0", image = "Kitty_sprite", show_two_window = True)
define ch_e = Character('[EmmaX.name]', color = "#98bee7", image = "Emma_sprite", show_two_window = True)
define ch_l = Character('[LauraX.name]', color = "#d8b600", image = "Laura_sprite", show_two_window = True)
define ch_j = Character('[JeanX.name]', color = "#b2d950", image = "Jean_sprite", show_two_window = True)
define ch_s = Character('[StormX.name]', color = "#b2d950", image = "Storm_sprite", show_two_window = True)
define ch_v = Character('[JubesX.name]', color = "#b2d950", image = "Jubes_sprite", show_two_window = True)

define ch_x = Character('Professor X', color = "#a09400", image = "Xavier_sprite", show_two_window = True)
define ch_b = Character('Dr. McCoy', color = "#1033b2", image = "arrow", show_two_window = True)

define ch_u = Character('???', color = "#85bb65", image = "arrow", show_two_window = True)

label splashscreen:
    if not config.developer:
        scene black onlayer backdrop
        with Pause(1)

        show expression "images/Onirating.png"
        show text "This title is for ages 18 and up." with dissolve
        with Pause(2)

        show text "This is a very rough beta version of the game. It has limited function and has not been thoroughly tested. Please report any bugs you find." with dissolve
        with Pause(2)

        hide text with dissolve
        with Pause(1)

    return

init -1:

    default day = 1
    default round = 100
    default time_options = ["morning", "midday", "evening", "night"]
    default time_index = 2
    default current_time = time_options[time_index]
    default week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default weekday = 6
    default day_of_week = week[weekday]

    default bg_current = "bg_study"

    default focused_Girl = None
    default Partner = None
    default Party = []
    default Present = []
    default Nearby = []
    default all_Girls = []
    default active_Girls = []

    default Phonebook = []
    default Keys = []
    default Rules = []

    default total_SEXP = 0

    default personal_rooms = ["bg_player"]

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

    default always_return_to_room = 1

    default stage_far_far_left = 0.1
    default stage_far_left = 0.23
    default stage_left = 0.35
    default stage_center = 0.5
    default stage_right = 0.62
    default stage_far_right = 0.75
    default stage_far_far_right = 0.875

    default number_of_holders = 1

    default Xavier_brows = "_happy"
    default Xavier_eyes = "_happy"
    default Xavier_mouth = "_smile"
    default Xavier_psychic = False
    default Xavier_emotion = "_happy"
    default Xavier_location = stage_center

    default Gwen_name = "????"

    default door_locked = False
    default entering = False

    default simulation = False

    default menu_context = None

    default dresses = ["_chinese_dress", "_red_dress", "_blue_dress"]
    default bodysuits = ["_catsuit", "_raven", "_domme", "_sci_fi", "_onepiece_swimsuit", "_sexy_swimsuit"]
    default pants = ["_pants", "_yoga_pants", "_capris", "_black_jeans", "_leather_pants", "_mesh_pants", "_opaque_fetish", "_sheer_fetish", "_black_and_blue_pants"]
    default skirts = ["_skirt", "_cosplay_skirt", "_blue_skirt", "_cheerleader_skirt"]
    default shorts = ["_shorts", "_cheerleader_skirtshort"]

    default hand_actions = ["massage", "fondle_thighs", "fondle_breasts", "fondle_pussy", "finger_pussy", "fondle_ass", "finger_ass"]
    default finger_actions = ['finger_pussy", "finger_ass"']
    default mouth_actions = ["kiss", "suck_breasts", "eat_pussy", "eat_ass"]
    default cock_actions = ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"]
    default dildo_actions = ["dildo_pussy", "dildo_ass"]
    default breast_actions = ["fondle_breasts", "suck_breasts"]
    default pussy_actions = ["fondle_pussy", "finger_pussy", "eat_pussy", "dildo_pussy"]
    default ass_actions = ["fondle_ass", "finger_ass", "eat_ass", "dildo_ass"]

    default active_actions = ["massage", "kiss", "fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]
    default passive_actions = ["striptease", "masturbation", "handjob", "footjob", "titjob", "blowjob"]
    default fondle_actions = ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
    default job_actions = ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]
    default sex_actions = ["sex", "anal", "hotdog"]

    default below_actions = ["fondle_thighs", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"]
    default inside_panties_actions = ["fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"]
    default insertion_actions = ["finger_pussy", "finger_ass", "dildo_pussy", "dildo_ass"]
    default anal_insertion_actions = ["finger_ass", "dildo_ass", "anal"]
    default contact_actions = ["massage", "kiss", "fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_ass", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"]

    default all_actions = ["massage", "kiss",
        "striptease", "masturbation",
        "fondle_thighs",
        "fondle_breasts", "suck_breasts",
        "fondle_pussy", "finger_pussy", "eat_pussy",
        "fondle_ass", "finger_ass", "eat_ass",
        "handjob", "footjob", "titjob", "blowjob",
        "dildo_pussy", "dildo_ass",
        "sex", "anal", "hotdog"]

label start:
    $ Player = PlayerClass()

    $ RogueX = GirlClass("Rogue", 500, 0, 0, 10)
    $ KittyX = GirlClass("Kitty", 400, 100, 0, 10)
    $ EmmaX = GirlClass("Emma", 300, 0, 200, 15)
    $ LauraX = GirlClass("Laura", 400, 0, 200, 10)
    $ JeanX = GirlClass("Jean", 0, 0, 1000, 10)
    $ StormX = GirlClass("Storm", 500, 0, 100, 10)
    $ JubesX = GirlClass("Jubes", 500, 50, 50, 10)

    $ focused_Girl = RogueX

    show screen status_screen
    show screen inventory_button

    $ bg_current = "bg_emma"
    $ time_index = 2
    $ current_time = "evening"

    scene background onlayer backdrop
    scene

    $ RogueX.change_outfit("nude")

    $ Player.sprite = True
    $ show_feet = False
    $ action_speed = 1
    $ Player.cock_position = "in"
    $ Player.primary_action = "blowjob"
    $ Player.secondary_action = "finger_ass"
    $ RogueX.spunk["anus"] = True
    $ RogueX.spunk["pussy"] = True

    show Rogue_sprite handjob at sprite_location(0.2) as handjob
    show Rogue_sprite titjob at sprite_location(0.4) as titjob
    show Rogue_sprite blowjob at sprite_location(0.5) as blowjob
    show Rogue_sprite sex at sprite_location(0.6) as sex
    show Rogue_sprite doggy at sprite_location(0.8) as anal

    ""

    $ Player.sprite = False
    call stop_all_actions
    $ RogueX.change_outfit("casual1")

    #
    # $ RogueX.sprite_location = stage_far_far_left
    # $ active_Girls.append(RogueX)
    #
    # $ KittyX.sprite_location = stage_far_left
    # $ active_Girls.append(KittyX)
    #
    # $ EmmaX.sprite_location = stage_left
    # $ active_Girls.append(EmmaX)
    #
    # $ LauraX.sprite_location = stage_center
    # $ active_Girls.append(LauraX)
    #
    # $ JeanX.sprite_location = stage_right
    # $ active_Girls.append(JeanX)
    #
    # $ StormX.sprite_location = stage_far_right
    # $ active_Girls.append(StormX)
    #
    # $ JubesX.sprite_location = stage_far_far_right
    # $ active_Girls.append(JubesX)
    #
    # python:
    #     for G in active_Girls:
    #         G.location = bg_current
    #
    # $ RogueX.change_outfit("nude")
    # $ Player.sprite = False
    # $ Player.cock_position = "in"
    # $ Player.primary_action = "suck_breasts"
    # $ Player.secondary_action = "fondle_breasts"

    # show Rogue_sprite sex at sprite_location(stage_center)
    # show Kitty_sprite titjob at sprite_location(stage_center)

    # show Rogue_sprite standing at sprite_location(RogueX.sprite_location)
    # show Kitty_sprite standing at sprite_location(KittyX.sprite_location)
    # show Emma_sprite standing at sprite_location(EmmaX.sprite_location)
    # show Laura_sprite standing at sprite_location(LauraX.sprite_location)
    # show Jean_sprite standing at sprite_location(JeanX.sprite_location)
    # show Storm_sprite standing at sprite_location(StormX.sprite_location)
    # show Jubes_sprite standing at sprite_location(JubesX.sprite_location)

    # ""
    # $ active_Girls = []

    jump prologue

return
