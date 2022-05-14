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
    ConditionSwitch("Partner == StormX", "images/UI_GirlHandS.png",
            "True", "images/UI_GirlHand.png")

image blackscreen:
    Solid("#000000")
    on show:
        alpha 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

define ch_r = Character('[RogueX.name]', color="#85bb65", image = "arrow", show_two_window = True)
define ch_p = Character('[Player.name]', color="#87CEEB", show_two_window = True)
define ch_x = Character('Professor X', color="#a09400", image = "arrow", show_two_window = True)
define ch_k = Character('[KittyX.name]', color="#F5A9D0", image = "arrow", show_two_window = True)
define ch_e = Character('[EmmaX.name]', color="#98bee7", image = "arrow", show_two_window = True)
define ch_b = Character('Dr. McCoy', color="#1033b2", image = "arrow", show_two_window = True)
define ch_l = Character('[LauraX.name]', color="#d8b600", image = "arrow", show_two_window = True)
define ch_j = Character('[JeanX.name]', color="#b2d950", image = "arrow", show_two_window = True)
define ch_s = Character('[StormX.name]', color="#b2d950", image = "arrow", show_two_window = True)
define ch_v = Character('[JubesX.name]', color="#b2d950", image = "arrow", show_two_window = True) #fix, color change
define ch_u = Character('???', color="#85bb65", image = "arrow", show_two_window = True)
define ch_n = Character('N', image = "arrow", show_two_window = True) #non-Girl, uses focused_Girl #rmoved color, test that. . .
define ch_g = Character('[GwenName]', color="#F08080", image = "arrowG", show_two_window = True,background=Frame("images/WordballoonG.png",50,50))
define ch_usher = Character('Usher', color="#DF0174", show_two_window = True)
define ch_danger = Character('Danger Room:', color="#1033b2",what_color="#1033b2",what_font="dungeon.ttf",show_two_window=False)

label splashscreen:
    if not config.developer:
        scene black onlayer backdrop
        with Pause(1)

        show image "images/Onirating.jpg"
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
    default Round = 100                 #Tracks time within a turn
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
    default TotalSEXP = 0               #tallies the total combined SEXP daily
    default PersonalRooms = ["bg_player"] #,"bg_rogue","bg_kitty","bg_emma","bg_laura"]
    default Taboo = 0
    default Rules = []
    default Digits = []
    default Keys = []
    default action_context = 0               #Whether Auto/Shift
    default multi_action = 1             #0 if the action cannot continue, 1 if it can
    default primary_action = 0                 #Mainhand
    default offhand_action = 0                #Offhand
    default girl_offhand_action = 0                #Girl's offhand
    default second_Girl_primary_action = 0                #this is the 4th sexual act performed by the second girl
    default second_Girl_offhand_action = 0                #this is the 5th sexual act performed by the second girl if masturbating
    default position_change_timer = 100            #This is a timer for changing sexual positions on auto

    default Nearby = []                 #this tracks girls in the same room, but distant from you
    default Present = []                #This list tracks which girls are in this scene
    default Shop_Inventory = []         #These are updated with books available for purchase       ["DL","DL","DL","DL","G","G","G","G","G","A","A","A","A"]
    default inventory_count = 0         #used in screens to keep track of inventory
    default StackDepth = 0

    default Partner = 0                 #this is the second Girl involved in a sex act, make sure to set Partner to 0 after each sex act
    default Events = []
    default PunishmentX = 0             #countdown on your punishment
    default temp_modifier = 0

    default Count = 0                   #For within an event
    default between_event_count = 0                  #For between several events
    default stored_count = 0              #Stores values for after an event ends
    default counter = 0                     #a mini Count variable for discrete operations
    default Stealth = 0                 #How careful you're being
    default action_speed = 0                   #pace of sex acts
    default Achievements = []
    default Options = []
    default Vibration = 0
    default Psychic = 0                 #this is an animation toggle for psychic sex. hand/blow/tit/pussy/ass
    default ShowFeet = 0
    default RTR_Toggle = 1              #sets whether game asks if you want to return to your room when a girl asks you to

    default TravelMode = 0              #used for wandering around, if 0, you use the worldmap
    default StageFarLeft = 150          #these are values for location points on the screen
    default StageLeft = 350
    default StageCenter = 550           #This is the default position for the lead
    default StageRight = 715            #This is the default position for second girl
    default StageFarRight = 900         #these are values for location points on the screen
    default HolderCount = 1             #Used by the popup numbers

    default X_Brows = "happy"
    default X_Mouth = "happy"
    default X_Eyes = "happy"
    default X_Psychic = 0
    default X_emotion = "happy"
    default Xsprite_location = StageCenter
    default GwenName = "????"
    default Load_Options = []

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

    $ RogueX.OutfitChange(6,Changed=1)
    $ KittyX.OutfitChange(6,Changed=1)
    $ EmmaX.OutfitChange(6,Changed=1)
    $ LauraX.OutfitChange(6,Changed=1)
    $ JeanX.OutfitChange(6,Changed=1)
    $ StormX.OutfitChange(6,Changed=1)
    $ JubesX.OutfitChange(6,Changed=1)

    $ focused_Girl = RogueX
    show screen Status_Screen
    show screen Inventorybutton

    jump prologue

label after_load:
    label VersionNumber:
        $ SaveVersion = 0 if "SaveVersion" not in globals().keys() else SaveVersion

        $ Load_Options = all_Girls[:]
        while Load_Options:
                #removes girls with "poly themselves" in traits
                $ Load_Options[0].Pose = "breasts" if Load_Options[0].Pose == "breast" else Load_Options[0].Pose
                $ Load_Options.remove(Load_Options[0])
        if "partysolved" in LauraX.History:
                $ LauraX.History.remove("partysolved")
                $ LauraX.AddWord(1,0,0,0,"partyfoul") #adds "partyfoul" to History
        if "JubesX" not in globals().keys():
                $ JubesX = GirlClass("Jubes",500,50,50,10)
                $ JubesX.Introduction()
        if "bg_teacher" in JubesX.Schedule:
                $ JubesX.Schedule = [["bg_jubes","bg_dangerroom","bg_dangerroom","bg_jubes"],
                                ["bg_classroom","bg_classroom","bg_jubes","bg_jubes"],
                                ["bg_jubes","bg_dangerroom","bg_dangerroom","bg_jubes"],
                                ["bg_dangerroom","bg_dangerroom","bg_jubes","bg_jubes"],
                                ["bg_pool","bg_campus","bg_campus","bg_jubes"],
                                ["bg_jubes","bg_campus","bg_jubes","bg_pool"],
                                ["bg_jubes","bg_campus","bg_jubes","bg_pool"],
                                ] #Schedule[0-6][0-4] = Schedule[Weekday][time_index]
        $ JubesX.Blow = 0
        $ JubesX.Hand = 0

        #this section should return players to their room if it would otherwise fail to load a save properly
        $ StackDepth = renpy.call_stack_depth()
        $ Stack = renpy.get_return_stack()
        #"[Stack]"
        while StackDepth > 0:
            $ StackCheck = Stack[StackDepth-1]
            if not renpy.has_label(StackCheck):
                #"[StackCheck]"
                "This save may have some issues, so you are being returned to the player's room."
                "Progress should be properly saved, although if you were in the middle of a Girl scene, there might be issues continuing forward."
                "Try to load a save in which you were in a neutral situation if you want to keep playing from there."
                "Let Oni know if this happened on a save made in version 0.991 or later."
                "If you would prefer to try your luck, you can see if the save will load, but it will more likely return to the main menu."
                menu:
                    "Return to player's room [[safer]":
                        $ bg_current = "bg_player"
                        jump Misplaced
                    "See if save works [[probably won't]":
                        return
            $ StackDepth -= 1

        return

return
