init -1:

    default day = 1
    default round = 100
    default time_options = ["morning", "midday", "evening", "night", "night"]
    default time_index = 2
    default current_time = time_options[time_index]
    default week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default weekday = 6
    default day_of_week = week[weekday]

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

    default being_punished = 0

    default approval_bonus = 0
    default approval = 0

    default between_event_count = 0
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
