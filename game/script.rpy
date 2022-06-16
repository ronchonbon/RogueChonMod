define ch_p = Character('[Player.name]', color = "#87CEEB", show_two_window = True)

define ch_r = Character('[RogueX.name]', color = "#85bb65", image = "Rogue_sprite", show_two_window = True)
define ch_k = Character('[KittyX.name]', color = "#F5A9D0", image = "Kitty_sprite", show_two_window = True)
define ch_e = Character('[EmmaX.name]', color = "#98bee7", image = "Emma_sprite", show_two_window = True)
define ch_l = Character('[LauraX.name]', color = "#d8b600", image = "Laura_sprite", show_two_window = True)
define ch_j = Character('[JeanX.name]', color = "#b2d950", image = "Jean_sprite", show_two_window = True)
define ch_s = Character('[StormX.name]', color = "#b2d950", image = "Storm_sprite", show_two_window = True)
define ch_v = Character('[JubesX.name]', color = "#b2d950", image = "Jubes_sprite", show_two_window = True)
# define ch_m = Character('[MystiqueX.name]', color = "b2d950", image = "Mystique_sprite", show_two_window = True)

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

    default dresses = ["_chinese", "_red_dress", "_blue_dress", "_white_dress"]
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
    default kinky_actions = ["masturbation", "finger_ass", "eat_ass", "titjob", "footjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]

    default all_actions = ["massage", "kiss",
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
    $ Player = PlayerClass()

    $ RogueX = GirlClass("Rogue", 500, 0, 0, 10)
    $ KittyX = GirlClass("Kitty", 400, 100, 0, 10)
    $ EmmaX = GirlClass("Emma", 300, 0, 200, 15)
    $ LauraX = GirlClass("Laura", 400, 0, 200, 10)
    $ JeanX = GirlClass("Jean", 0, 0, 1000, 10)
    $ StormX = GirlClass("Storm", 500, 0, 100, 10)
    $ JubesX = GirlClass("Jubes", 500, 50, 50, 10)
    # $ MystiqueX = GirlClass("Mystique", 0, 0, 0, 15)

    $ focused_Girl = RogueX

    show screen status_screen
    show screen inventory_button

    $ bg_current = "bg_emma"
    $ time_index = 2
    $ current_time = "evening"

    scene background onlayer backdrop
    scene

    python:
        for G in all_Girls:
            active_Girls.append(G)
            G.recent_history.append("blanket")
    #         # G.change_face("_sexy")
            # G.change_outfit("nude")
    #         # G.grool = 2
    #         # G.spunk["mouth"] = True
    #         # G.spunk["pussy"] = True
    #         # G.spunk["anus"] = True
    #
    $ Player.sprite = True
    $ show_feet = True
    $ action_speed = 4
    $ Player.cock_position = "in"
    $ Player.primary_action = "sex"
    $ Player.secondary_action = "finger_ass"
    # #
    # # $ RogueX.change_outfit("nude")
    # # $ RogueX.outfit["dress"] = "_raven"
    # # $ RogueX.outfit["cloak"] = "_raven_cloak"
    # # $ KittyX.change_outfit("nude")
    # # $ KittyX.outfit["dress"] = "_chinese"
    # # $ EmmaX.change_outfit("domme_outfit")
    # # $ EmmaX.arm_pose = 2
    # # $ LauraX.change_outfit("nude")
    # # $ LauraX.outfit["dress"] = "_bunny_suit"
    # # $ LauraX.outfit["hose"] = "_pantyhose"
    # # $ LauraX.outfit["gloves"] = "_bunny"
    # # $ LauraX.outfit["face_outer_accessory"] = "_bunny_ears"
    # # $ JeanX.change_outfit("nude")
    # # $ JeanX.outfit["dress"] = "_sci_fi"
    # $ MystiqueX.change_outfit("true_self")
    # #
    # show Rogue_sprite titjob at sprite_location(0.5)
    show Kitty_sprite blowjob at sprite_location(0.5)
    # show Emma_sprite titjob at sprite_location(0.5)
    # show Laura_sprite titjob at sprite_location(0.5)
    # show Jean_sprite titjob at sprite_location(0.5)
    # show Storm_sprite titjob at sprite_location(0.5)
    # show Jubes_sprite titjob at sprite_location(0.5)
    #
    # show Rogue_sprite standing at sprite_location(0.15)
    # show Kitty_sprite standing at sprite_location(0.25)
    # show Emma_sprite standing normal at sprite_location(0.35)
    # show Laura_sprite standing at sprite_location(0.45)
    # show Jean_sprite standing at sprite_location(0.55)
    # show Storm_sprite standing at sprite_location(0.65)
    # show Jubes_sprite standing at sprite_location(0.75)
    # show Mystique_sprite standing normal at sprite_location(0.85)
    #
    ""
    #
    # $ active_Girls = []
    # $ focused_Girl = RogueX

    jump prologue

return
