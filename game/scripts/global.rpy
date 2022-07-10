init -1:

    default stack_depth = 0

    default day = 1
    default round = 100
    default time_options = ["morning", "midday", "evening", "night", "night"]
    default time_index = 2
    default current_time = time_options[time_index]
    default week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default weekday = 6
    default day_of_week = week[weekday]

    default Present = []
    default Nearby = []
    default Rules = []
    default active_Girls = []
    default all_Girls = []

    default total_SEXP = 0

    default bedrooms = ["bg_player"]

    default door_locked = False

    default show_feet = False

    define stage_far_far_left = 0.15
    define stage_far_left = 0.25
    define stage_left = 0.35
    define stage_center = 0.5
    define stage_right = 0.65
    define stage_far_right = 0.75
    define stage_far_far_right = 0.85

    define all_Clothing_types = ["face_tattoos", "face_piercings", "makeup", "gag",
        "face_inner_accessory", "hair", "face_outer_accessory",
        "body_tattoos", "body_piercings", "buttplug",
        "nipple_accessories", "underwear", "hose",
        "bodysuit", "rope",
        "socks", "pants", "skirt", "boots",
        "bra", "dress", "top",
        "neck", "gloves", "sleeves", "belt", "suspenders",
        "jacket", "cloak"]

    define intrinsic_Clothing_types = ["face_tattoos", "face_piercings",
        "body_tattoos", "body_piercings"]

    define removable_Clothing_types = ["makeup", "gag",
        "face_inner_accessory", "face_outer_accessory",
        "buttplug",
        "nipple_accessories", "underwear", "hose",
        "bodysuit", "rope",
        "socks", "pants", "skirt", "boots",
        "bra", "dress", "top",
        "neck", "gloves", "sleeves", "belt", "suspenders",
        "jacket", "cloak"]

    define breast_hiding_Clothing_types = ["bodysuit", "bra", "dress", "top", "jacket"]
    define underwear_hiding_Clothing_types = ["bodysuit", "pants", "skirt", "dress", "top", "jacket"]
    define pussy_hiding_Clothing_types = ["underwear", "bodysuit", "pants", "skirt", "dress"]
    define thigh_covering_Clothing_types = ["bodysuit", "hose", "pants", "skirt", "boots", "dress"]
    define feet_covering_Clothing_types = ["hose", "socks", "boots"]

    define Clothing_coverage = {"face_tattoos": [],
        "face_piercings": [],
        "makeup": [],
        "gag": [],
        "face_inner_accessory": [],
        "hair": [],
        "face_outer_accessory": [],
        "body_tattoos": [],
        "body_piercings": [],
        "buttplug": ["underwear"],
        "nipple_accessories": ["bodysuit", "bra", "dress", "top"],
        "underwear": ["hose", "bodysuit", "pants", "suspenders", "boots"],
        "hose": ["bodysuit", "pants", "socks", "boots"],
        "bodysuit": ["bra", "dress", "top", "jacket", "cloak", "socks", "pants", "skirt", "boots"],
        "rope": ["bra", "dress", "top", "jacket", "cloak", "socks", "pants", "skirt", "boots"],
        "socks": ["boots"],
        "pants": ["boots", "suspenders"],
        "skirt": ["boots", "suspenders"],
        "boots": [],
        "bra": ["dress", "top", "suspenders", "jacket", "cloak"],
        "dress": ["top", "belt", "suspenders", "jacket", "cloak"],
        "top": ["belt", "suspenders", "jacket", "cloak"],
        "neck": [],
        "gloves": [],
        "sleeves": ["jacket"],
        "belt": ["suspenders"],
        "suspenders": ["jacket", "cloak"],
        "jacket": ["cloak"],
        "cloak": []}

    define hand_Action_types = ["massage", "fondle_thighs", "fondle_breasts", "fondle_pussy", "finger_pussy", "fondle_ass", "finger_ass"]
    define finger_Action_types = ["finger_pussy", "finger_ass"]
    define mouth_Action_types = ["kiss", "suck_breasts", "eat_pussy", "eat_ass"]
    define cock_Action_types = ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"]
    define dildo_Action_types = ["dildo_pussy", "dildo_ass"]
    define breast_Action_types = ["fondle_breasts", "suck_breasts"]
    define pussy_Action_types = ["fondle_pussy", "finger_pussy", "eat_pussy", "dildo_pussy"]
    define ass_Action_types = ["fondle_ass", "finger_ass", "eat_ass", "dildo_ass"]

    define active_Action_types = ["massage", "kiss", "fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]
    define passive_Action_types = ["striptease", "masturbation", "handjob", "footjob", "titjob", "blowjob"]
    define fondle_Action_types = ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
    define job_Action_types = ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]
    define sex_Action_types = ["sex", "anal", "hotdog"]

    define below_Action_types = ["fondle_thighs", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"]
    define inside_panties_Action_types = ["finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"]
    define insertion_Action_types = ["finger_pussy", "finger_ass", "dildo_pussy", "dildo_ass", "sex", "anal"]
    define pussy_insertion_Action_types = ["finger_pussy", "dildo_pussy", "sex"]
    define anal_insertion_Action_types = ["finger_ass", "dildo_ass", "anal"]
    define contact_Action_types = ["massage", "kiss", "fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_ass", "finger_ass", "eat_ass", "handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"]
    define kinky_Action_types = ["masturbation", "finger_ass", "eat_ass", "titjob", "footjob", "dildo_pussy", "dildo_ass", "anal", "hotdog"]

    define all_Action_types = [
        "massage", "kiss",
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

    define EventScheduler = EventSchedulerClass()
