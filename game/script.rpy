


image title card = "images/titleimage.jpg"
image NightMask = "images/nightmask.png"

image Crossroads_E = "images/Crossroads_Evening.jpg"
image Crossroads_N = "images/Crossroads_Night.jpg"
image Crossroads_D = "images/Crossroads_Day.jpg"

image UI_Backpack = "images/UI_Backpack_idle.png"
image UI_Dildo = "images/UI_Dildo.png"
image UI_VibA = "images/UI_VibA.png"
image UI_VibB = "images/UI_VibB.png"
image UI_Tongue = "images/UI_Tongue.png"
image UI_Finger = "images/UI_Finger.png"
image UI_Hand = "images/UI_Hand.png"
image UI_GirlFinger = "images/UI_GirlFinger.png"
image UI_GirlHand = "images/UI_GirlHand.png"






image UI_PartnerHand:
    ConditionSwitch(

            "Partner == StormX", "images/UI_GirlHandS.png",
            "True", "images/UI_GirlHand.png"
            )



image blackscreen:
    Solid("#000000")
    on show:
        alpha 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

define ch_r = Character('[RogueX.name]', color="#85bb65", image = "arrow", show_two_window=True)
define ch_p = Character('[Player.name]', color="#87CEEB", show_two_window=True)
define ch_x = Character('Professor X', color="#a09400", image = "arrow", show_two_window=True)
define ch_k = Character('[KittyX.name]', color="#F5A9D0", image = "arrow", show_two_window=True)
define ch_e = Character('[EmmaX.name]', color="#98bee7", image = "arrow", show_two_window=True)
define ch_b = Character('Dr. McCoy', color="#1033b2", image = "arrow", show_two_window=True)
define ch_l = Character('[LauraX.name]', color="#d8b600", image = "arrow", show_two_window=True)
define ch_j = Character('[JeanX.name]', color="#b2d950", image = "arrow", show_two_window=True)
define ch_s = Character('[StormX.name]', color="#b2d950", image = "arrow", show_two_window=True)
define ch_v = Character('[JubesX.name]', color="#b2d950", image = "arrow", show_two_window=True)
define ch_u = Character('???', color="#85bb65", image = "arrow", show_two_window=True)
define ch_n = Character('N', image = "arrow", show_two_window=True)
define ch_g = Character('[Gwenname]', color="#F08080", image = "arrowG", show_two_window=True,background=Frame("images/WordballoonG.png",50,50))
define ch_usher = Character('Usher', color="#DF0174", show_two_window=True)
define ch_danger = Character('Danger Room:', color="#1033b2",what_color="#1033b2",what_font="dungeon.ttf",show_two_window=False)



label splashscreen:
    if not config.developer:
        scene black onlayer backdrop
        with Pause(1)

        show expression "images/Onirating.jpg"
        show text "This title is for ages 18 and up." with dissolve
        with Pause(2)

        show text "This is a very rough beta version of the game. It has limited function and has not been thoroughly tested. Please report any bugs you find." with dissolve
        with Pause(2)

        hide text with dissolve
        with Pause(1)

    return


init -1:

    default SaveVersion = 997
    default Day = 1
    default Cheat = 0
    default Round = 100
    default Time_Options = ["Morning", "Midday", "Evening", "Night"]
    default time_index = 2
    default Current_Time = Time_Options[(time_index)]
    default Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default Weekday = 6
    default DayofWeek = Week[Weekday]
    default bg_current = "bg_study"
    default focused_Girl = 0
    default Party = []
    default all_Girls = []
    default active_Girls = []
    default TotalSEXP = 0
    default PersonalRooms = ["bg_player"]
    default Taboo = 0
    default Rules = []
    default Digits = []
    default Keys = []
    default Line = 0
    default TempLine = 0
    default PassLine = 0
    default action_context = 0
    default multi_action = 1
    default primary_action = 0
    default offhand_action = 0
    default girl_offhand_action = 0
    default second_girl_primary_action = 0
    default second_girl_offhand_action = 0
    default position_timer = 100

    default Nearby = []
    default Present = []
    default Shop_Inventory = []
    default Inventory_Count = 0
    default StackDepth = 0

    default Partner = 0
    default Events = []
    default PunishmentX = 0
    default approval_bonus = 0
    default approval = 0
    default Count = 0
    default between_event_count = 0
    default stored_count = 0
    default counter = 0
    default Stealth = 0
    default action_speed = 0
    default Achievements = []
    default Options = []
    default Vibration = 0
    default Psychic = 0
    default ShowFeet = 0
    default RTR_Toggle = 1

    default TravelMode = 0
    default stage_far_left = 150
    default stage_left = 350
    default stage_center = 550
    default stage_right = 715
    default stage_far_right = 900
    default number_of_holders = 1

    default X_Brows = "happy"
    default X_Mouth = "happy"
    default X_Eyes = "happy"
    default X_Psychic = 0
    default X_emotion = "happy"
    default Xsprite_location = stage_center
    default Gwenname = "????"
    default Load_Options = []

    default door_locked = False

    default simulation = False

    default hand_actions = ["massage", "fondle_thighs", "fondle_breasts", "fondle_pussy", "finger_pussy", "fondle_ass", "finger_ass"]
    default mouth_actions = ["kiss", "suck_breasts", "eat_pussy", "eat_ass"]
    default cock_actions = ["handjob", "footjob", "titjob", "blowjob", "sex", "anal", "hotdog"]
    default dildo_actions = ["dildo_pussy", "dildo_ass"]
    default breast_actions = ["fondle_breasts", "suck_breasts"]
    default pussy_actions = ["fondle_pussy", "finger_pussy", "eat_pussy", "dildo_pussy"]
    default ass_actions = ["fondle_ass", "finger_ass", "eat_ass", "dildo_ass"]

    default all_actions = ["massage", "kiss", "fondle_thighs",
        "masturbation",
        "fondle_breasts", "suck_breasts",
        "fondle_pussy", "finger_pussy", "eat_pussy",
        "fondle_ass", "finger_ass", "eat_ass",
        "handjob", "footjob", "titjob", "blowjob",
        "dildo_pussy", "dildo_ass",
        "sex", "anal", "hotdog"]

    default active_actions = ["kiss", "massage", "fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]
    default passive_actions = ["strip", "masturbation", "handjob", "footjob", "titjob", "blowjob"]
    default fondle_actions = ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass"]
    default job_actions = ["handjob", "footjob", "titjob", "blowjob", "dildo_pussy", "dildo_ass"]
    default sex_actions = ["sex", "anal", "hotdog"]
    default inside_panties_actions = ["fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"]
    default anal_insertion_actions = ["finger_ass", "dildo_ass", "anal"]

label start:


    $ Player = PlayerClass()
    $ RogueX = GirlClass("Rogue",500,0,0,10)
    $ KittyX = GirlClass("Kitty",400,100,0,10)
    $ EmmaX = GirlClass("Emma",300,0,200,15)
    $ LauraX = GirlClass("Laura",400,0,200,10)
    $ JeanX = GirlClass("Jean",0,0,1000,10)
    $ StormX = GirlClass("Storm",500,0,100,10)
    $ JubesX = GirlClass("Jubes",500,50,50,10)

    $ RogueX.Introduction()
    $ KittyX.Introduction()
    $ EmmaX.Introduction()
    $ LauraX.Introduction()
    $ JeanX.Introduction()
    $ StormX.Introduction()
    $ JubesX.Introduction()



    $ RogueX.change_outfit(6,Changed=1)
    $ KittyX.change_outfit(6,Changed=1)
    $ EmmaX.change_outfit(6,Changed=1)
    $ LauraX.change_outfit(6,Changed=1)
    $ JeanX.change_outfit(6,Changed=1)
    $ StormX.change_outfit(6,Changed=1)
    $ JubesX.change_outfit(6,Changed=1)


    $ focused_Girl = RogueX
    show screen Status_Screen
    show screen Inventorybutton

    jump Prologue



label after_load:
    label VersionNumber:
        return

return
