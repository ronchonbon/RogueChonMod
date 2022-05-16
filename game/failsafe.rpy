label Failsafe(Counter=0, BO=[]):
    if "Player" not in globals().keys():

        $ Player = PlayerClass()
    $ Player.name =     Playername if "Playername" in globals().keys() else 2
    $ Player.semen =    P_Semen if "P_Semen" in globals().keys() else 2
    $ Player.max_semen = P_Semen_Max if "P_Semen_Max" in globals().keys() else 3
    $ Player.focus =    P_Focus if "P_Focus" in globals().keys() else 0
    $ Player.focusing =   P_FocusX if "P_FocusX" in globals().keys() else 0
    $ Player.XP =       P_XP if "P_XP" in globals().keys() else 0
    $ Player.StatPoints =       P_Statpoints if "P_Statpoints" in globals().keys() else 0
    $ Player.XPgoal =    P_XPgoal if "P_XPgoal" in globals().keys() else 100
    $ Player.Lvl =      P_Lvl if "P_Lvl" in globals().keys() else 1
    $ Player.Rep =      P_Rep if "P_Rep" in globals().keys() else 600
    $ Player.recent_history =    P_recent_history[:] if "P_recent_history" in globals().keys() else []
    $ Player.daily_history =     P_daily_history[:] if "P_daily_history" in globals().keys() else []
    $ Player.Traits =   P_Traits[:] if "P_Traits" in globals().keys() else []
    $ Player.history =  P_History[:] if "P_History" in globals().keys() else []
    $ Player.Harem =    P_Harem[:] if "P_Harem" in globals().keys() else []
    $ Player.Male =      P_Male if "P_Male" in globals().keys() else 1

    $ Player.Income =   P_Income if "P_Income" in globals().keys() else 12
    $ Player.Cash =     P_Cash if "P_Cash" in globals().keys() else 20
    $ Player.Inventory =        P_Inventory[:] if "P_Inventory" in globals().keys() else []

    $ Player.Sprite =   P_Sprite if "P_Sprite" in globals().keys() else 0
    $ Player.Color =    P_Color if "P_Color" in globals().keys() else "green"
    $ Player.Cock =     P_Cock if "P_Cock" in globals().keys() else "out"
    $ Player.Spunk =    P_Spunk if "P_Spunk" in globals().keys() else 0
    $ Player.Wet =      P_Wet if "P_Wet" in globals().keys() else 0


    if "RogueX" not in globals().keys():
        $ RogueX = GirlClass("Rogue",500,0,0,10)
    $ RogueX.name = Roguename if "Roguename" in globals().keys() else "Rogue"
    $ RogueX.Tag = "Rogue"
    $ RogueX.names = ["Rogue"]
    $ RogueX.love = R_Love if "R_Love" in globals().keys() else RogueX.love
    $ RogueX.obedience = R_Obed if "R_Obed" in globals().keys() else RogueX.obedience
    $ RogueX.inhibition = R_Inbt if "R_Inbt" in globals().keys() else RogueX.inhibition
    $ RogueX.lust = R_Lust if "R_Lust" in globals().keys() else RogueX.lust
    $ RogueX.Thirst = R_Thirst if "R_Thirst" in globals().keys() else 0
    $ RogueX.addiction = R_Addict if "R_Addict" in globals().keys() else 0
    $ RogueX.addiction_rate = R_Addictionrate if "R_Addictionrate" in globals().keys() else 0
    $ RogueX.resistance = R_Resistance if "R_Resistance" in globals().keys() else 0
    $ RogueX.Taboo = R_Taboo if "R_Taboo" in globals().keys() else 0
    $ RogueX.XP = R_XP if "R_XP" in globals().keys() else 0
    $ RogueX.StatPoints = R_StatPoints if "R_StatPoints" in globals().keys() else 0
    $ RogueX.XPgoal = R_XPgoal if "R_XPgoal" in globals().keys() else 100
    $ RogueX.Lvl = R_Lvl if "R_Lvl" in globals().keys() else 1
    $ RogueX.sprite_location = R_sprite_location if "R_sprite_location" in globals().keys() else stage_center
    $ RogueX.sprite_layer = R_Layer if "R_Layer" in globals().keys() else 50
    $ RogueX.remaining_actions = R_Action if "R_Action" in globals().keys() else 3
    $ RogueX.max_actions = R_MaxAction if "R_MaxAction" in globals().keys() else 3
    $ RogueX.Rep = R_Rep if "R_Rep" in globals().keys() else 600
    $ RogueX.recent_history = R_recent_history[:] if "R_recent_history" in globals().keys() else []
    $ RogueX.daily_history = R_daily_history[:] if "R_daily_history" in globals().keys() else []
    $ RogueX.Traits = R_Traits[:] if "R_Traits" in globals().keys() else []
    $ RogueX.history = R_History[:] if "R_History" in globals().keys() else []
    $ RogueX.Date = R_Date if "R_Date" in globals().keys() else 0
    $ RogueX.Chat = R_Chat[:] if "R_Chat" in globals().keys() else [0,0,0,0,0,0]
    $ RogueX.Event = R_Event[:] if "R_Event" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]


    $ RogueX.petname = R_Pet if "R_Pet" in globals().keys() else "Girl"
    $ RogueX.petnames = R_Pets[:] if "R_Pets" in globals().keys() else ["Girl"]
    $ RogueX.Cheated = R_Cheated if "R_Cheated" in globals().keys() else 0
    $ RogueX.Break = R_Break[:] if "R_Break" in globals().keys() else [0,0]
    $ RogueX.Forced = R_Forced if "R_Forced" in globals().keys() else 0
    $ RogueX.event_counter["forced"] = R_ForcedCount if "R_ForcedCount" in globals().keys() else 0
    $ RogueX.location = R_Loc if "R_Loc" in globals().keys() else "hold"

    $ RogueX.Outfit = R_Outfit if "R_Outfit" in globals().keys() else "casual1"
    $ RogueX.OutfitDay = R_OutfitDay if "R_OutfitDay" in globals().keys() else "casual1"
    $ RogueX.SeenPeen = R_SeenPeen if "R_SeenPeen" in globals().keys() else 0
    $ RogueX.SeenChest = R_SeenChest if "R_SeenChest" in globals().keys() else 0
    $ RogueX.SeenPussy = R_SeenPussy if "R_SeenPussy" in globals().keys() else 0
    $ RogueX.SeenPanties = R_SeenPanties if "R_SeenPanties" in globals().keys() else 0
    $ RogueX.Upskirt = R_Upskirt if "R_Upskirt" in globals().keys() else 0
    $ RogueX.Uptop = R_Uptop if "R_Uptop" in globals().keys() else 0
    $ RogueX.underwearDown = R_PantiesDown if "R_PantiesDown" in globals().keys() else 0
    $ RogueX.Wet = R_Wet if "R_Wet" in globals().keys() else 0
    $ RogueX.Water = R_Water if "R_Water" in globals().keys() else 0
    $ RogueX.Spunk = R_Spunk if "R_Spunk" in globals().keys() else []
    $ RogueX.piercings = R_Pierce if "R_Pierce" in globals().keys() else 0
    $ RogueX.pubes = R_Pubes if "R_Pubes" in globals().keys() else 1
    $ RogueX.ArmPose = R_ArmPose if "R_ArmPose" in globals().keys() else 1
    $ RogueX.blushing = R_Blush if "R_Blush" in globals().keys() else 0
    $ RogueX.eyes = R_Eyes if "R_Eyes" in globals().keys() else "normal"
    $ RogueX.mouth = R_Mouth if "R_Mouth" in globals().keys() else "normal"
    $ RogueX.brows = R_Brows if "R_Brows" in globals().keys() else "normal"
    $ RogueX.emotion = R_emotion if "R_emotion" in globals().keys() else "normal"
    $ RogueX.held_item = R_Held if "R_Held" in globals().keys() else 0
    $ RogueX.arms = R_Arms if "R_Arms" in globals().keys() else 0
    $ RogueX.legs = R_Legs if "R_Legs" in globals().keys() else 0
    $ RogueX.top = R_Over if "R_Over" in globals().keys() else 0
    $ RogueX.neck = R_Neck if "R_Neck" in globals().keys() else 0
    $ RogueX.bra = R_Chest if "R_Chest" in globals().keys() else 0
    $ RogueX.underwear = R_Panties if "R_Panties" in globals().keys() else 0
    $ RogueX.accessory = R_Acc if "R_Acc" in globals().keys() else 0
    $ RogueX.hair = R_Hair if "R_Hair" in globals().keys() else 1
    $ RogueX.hose = R_Hose if "R_Hose" in globals().keys() else 0
    $ RogueX.Shame = R_Shame if "R_Shame" in globals().keys() else 0
    $ RogueX.Inventory = R_Inventory[:] if "R_Inventory" in globals().keys() else []



    $ RogueX.Custom1 = R_Custom[:] if "R_Custom" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ RogueX.Custom2 = R_Custom2[:] if "R_Custom2" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ RogueX.Custom3 = R_Custom3[:] if "R_Custom3" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ RogueX.TempClothes = R_TempClothes[:] if "R_TempClothes" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ RogueX.Gym = R_Gym[:] if "R_Gym" in globals().keys() else [0,"gloves",0,"hoodie",0,"sports_bra","shorts",0,0,0,10]
    $ RogueX.sleepwear = R_Sleepwear[:] if "R_Sleepwear" in globals().keys() else [0,0,0,0,0,"tank","green_panties",0,0,0,20]
    $ RogueX.Swim = R_Swim[:] if "R_Swim" in globals().keys() else [0,0,0,"hoodie",0,"bikini_top","bikini_bottoms",0,0,0,0]

    $ RogueX.Gag = R_Gag if "R_Gag" in globals().keys() else 0
    $ RogueX.Todo = R_Todo[:] if "R_Todo" in globals().keys() else []
    $ RogueX.PubeC = R_PubeC if "R_PubeC" in globals().keys() else 0
    $ RogueX.Clothing = R_Schedule if "R_Schedule" in globals().keys() else [0,0,0,0,0,0,0,0,0,0]

    $ RogueX.event_counter["orgasmed"]= R_Org if "R_Org" in globals().keys() else 0
    $ RogueX.session_orgasms = R_OCount if "R_OCount" in globals().keys() else 0
    $ RogueX.event_counter["caught"] = R_Caught if "R_Caught" in globals().keys() else 0
    $ RogueX.action_counter["kiss"] = R_Kissed if "R_Kissed" in globals().keys() else 0
    $ RogueX.event_counter["sleepover"] = R_Sleep if "R_Sleep" in globals().keys() else 0
    $ RogueX.action_counter["handjob"] = R_Hand if "R_Hand" in globals().keys() else 0
    $ RogueX.action_counter["footjob"] = R_Foot if "R_Foot" in globals().keys() else 0
    $ RogueX.event_counter["ass_slapped"] = R_Slap if "R_Slap" in globals().keys() else 0
    $ RogueX.Strip = R_Strip if "R_Strip" in globals().keys() else 0
    $ RogueX.action_counter["titjob"] = R_Tit if "R_Tit" in globals().keys() else 0
    $ RogueX.action_counter["sex"] = R_Sex if "R_Sex" in globals().keys() else 0
    $ RogueX.action_counter["anal"] = R_Anal if "R_Anal" in globals().keys() else 0
    $ RogueX.used_to_anal = R_Loose if "R_Loose" in globals().keys() else 0
    $ RogueX.action_counter["hotdog"] = R_Hotdog if "R_Hotdog" in globals().keys() else 0
    $ RogueX.action_counter["masturbation"] = R_Mast if "R_Mast" in globals().keys() else 0
    $ RogueX.action_counter["fondle_breasts"]= R_FondleB if "R_FondleB" in globals().keys() else 0
    $ RogueX.action_counter["fondle_thighs"]= R_FondleT if "R_FondleT" in globals().keys() else 0
    $ RogueX.action_counter["fondle_pussy"] = R_FondleP if "R_FondleP" in globals().keys() else 0
    $ RogueX.action_counter["fondle_ass"] = R_FondleA if "R_FondleA" in globals().keys() else 0
    $ RogueX.action_counter["dildo_pussy"] = R_DildoP if "R_DildoP" in globals().keys() else 0
    $ RogueX.action_counter["dildo_ass"] = R_DildoA if "R_DildoA" in globals().keys() else 0
    $ RogueX.Vib = R_Vib if "R_Vib" in globals().keys() else 0
    $ RogueX.Plug = R_Plug if "R_Plug" in globals().keys() else 0
    $ RogueX.action_counter["suck_breasts"] = R_SuckB if "R_SuckB" in globals().keys() else 0
    $ RogueX.action_counter["finger_pussy"] = R_InsertP if "R_InsertP" in globals().keys() else 0
    $ RogueX.action_counter["finger_ass"] = R_InsertA if "R_InsertA" in globals().keys() else 0
    $ RogueX.action_counter["eat_pussy"] = R_LickP if "R_LickP" in globals().keys() else 0
    $ RogueX.action_counter["eat_ass"] = R_LickA if "R_LickA" in globals().keys() else 0
    $ RogueX.action_counter["blowjob"] = R_Blow if "R_Blow" in globals().keys() else 0
    $ RogueX.event_counter["swallowed"] = R_Swallow if "R_Swallow" in globals().keys() else 0
    $ RogueX.event_counter["creampied"] = R_CreamP if "R_CreamP" in globals().keys() else 0
    $ RogueX.event_counter["anal_creampied"] = R_CreamA if "R_CreamA" in globals().keys() else 0
    $ RogueX.event_counter["been_with_girl"] = R_Les if "R_Les" in globals().keys() else 0
    $ RogueX.event_counter["seen_with_girl"] = R_LesWatch if "R_LesWatch" in globals().keys() else 0
    $ RogueX.SEXP = R_SEXP if "R_SEXP" in globals().keys() else 0
    $ RogueX.player_favorite_action = R_PlayerFav if "R_PlayerFav" in globals().keys() else 0
    $ RogueX.favorite_action = R_Favorite if "R_Favorite" in globals().keys() else 0


    $ RogueX.accessory = R_Boots if "R_Boots" in globals().keys() else 0
    $ RogueX.home = "bg_rogue"

    $ RogueX.Outfit = "casual1" if RogueX.Outfit == "evo_green" else RogueX.Outfit
    $ RogueX.OutfitDay = "casual1" if RogueX.OutfitDay == "evo_green" else RogueX.OutfitDay
    $ RogueX.Outfit = "casual2" if RogueX.Outfit == "evo_pink" else RogueX.Outfit
    $ RogueX.OutfitDay = "casual2" if RogueX.OutfitDay == "evo_pink" else RogueX.OutfitDay

    $ RogueX.Casual1 = [2,"gloves","skirt","mesh_top","spiked_collar","tank","black_panties",0,0,"tights",0]
    $ RogueX.Casual2 = [2,"gloves","pants","pink_top",0,"buttoned_tank","black_panties",0,0,0,0]

    $ RogueX.Schedule = [["bg_rogue","bg_classroom","bg_dangerroom","bg_rogue"],
                                        ["bg_classroom","bg_dangerroom","bg_rogue","bg_rogue"],
                                        ["bg_rogue","bg_classroom","bg_dangerroom","bg_rogue"],
                                        ["bg_classroom","bg_dangerroom","bg_rogue","bg_rogue"],
                                        ["bg_rogue","bg_classroom","bg_dangerroom","bg_rogue"],
                                        ["bg_dangerroom","bg_pool","bg_rogue","bg_rogue"],
                                        ["bg_dangerroom","bg_pool","bg_rogue","bg_rogue"],
                                        ]
    $ RogueX.hair = "evo"
    $ RogueX.LikeKitty = R_LikeKitty if "R_LikeKitty" in globals().keys() else 600
    $ RogueX.LikeEmma = R_LikeEmma if "R_LikeEmma" in globals().keys() else 500
    $ RogueX.LikeLaura = R_LikeLaura if "R_LikeLaura" in globals().keys() else 500
    $ RogueX.SexKitty = R_SexKitty if "R_SexKitty" in globals().keys() else 0
    $ RogueX.SexEmma = R_SexEmma if "R_SexEmma" in globals().keys() else 0
    $ RogueX.SexLaura = R_SexLaura if "R_SexLaura" in globals().keys() else 0

    $ RogueX.massage_chart = ["shoulders","arms","arms","hands","hands","back","hips","back","breasts","breasts"]
    $ RogueX.history.append("met") if "met" not in RogueX.history else RogueX.history



    if "KittyX" not in globals().keys():
        $ KittyX = GirlClass("Kitty",500,0,0,10)
    $ KittyX.name = Kittyname if "Kittyname" in globals().keys() else "Kitty"
    $ KittyX.Tag = "Kitty"
    $ KittyX.names = ["Kitty"]
    $ KittyX.love = K_Love if "K_Love" in globals().keys() else KittyX.love
    $ KittyX.obedience = K_Obed if "K_Obed" in globals().keys() else KittyX.obedience
    $ KittyX.inhibition = K_Inbt if "K_Inbt" in globals().keys() else KittyX.inhibition
    $ KittyX.lust = K_Lust if "K_Lust" in globals().keys() else KittyX.lust
    $ KittyX.Thirst = K_Thirst if "K_Thirst" in globals().keys() else 0
    $ KittyX.addiction = K_Addict if "K_Addict" in globals().keys() else 0
    $ KittyX.addiction_rate = K_Addictionrate if "K_Addictionrate" in globals().keys() else 0
    $ KittyX.resistance = K_Resistance if "K_Resistance" in globals().keys() else 0
    $ KittyX.Taboo = K_Taboo if "K_Taboo" in globals().keys() else 0
    $ KittyX.XP = K_XP if "K_XP" in globals().keys() else 0
    $ KittyX.StatPoints = K_StatPoints if "K_StatPoints" in globals().keys() else 0
    $ KittyX.XPgoal = K_XPgoal if "K_XPgoal" in globals().keys() else 100
    $ KittyX.Lvl = K_Lvl if "K_Lvl" in globals().keys() else 1
    $ KittyX.sprite_location = K_sprite_location if "K_sprite_location" in globals().keys() else stage_center
    $ KittyX.sprite_layer = K_Layer if "K_Layer" in globals().keys() else 50
    $ KittyX.remaining_actions = K_Action if "K_Action" in globals().keys() else 3
    $ KittyX.max_actions = K_MaxAction if "K_MaxAction" in globals().keys() else 3
    $ KittyX.Rep = K_Rep if "K_Rep" in globals().keys() else 600
    $ KittyX.recent_history = K_recent_history[:] if "K_recent_history" in globals().keys() else []
    $ KittyX.daily_history = K_daily_history[:] if "K_daily_history" in globals().keys() else []
    $ KittyX.Traits = K_Traits[:] if "K_Traits" in globals().keys() else []
    $ KittyX.history = K_History[:] if "K_History" in globals().keys() else []
    $ KittyX.Date = K_Date if "K_Date" in globals().keys() else 0
    $ KittyX.Chat = K_Chat[:] if "K_Chat" in globals().keys() else [0,0,0,0,0,0]
    $ KittyX.Event = K_Event[:] if "K_Event" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]


    $ KittyX.petname = K_Pet if "K_Pet" in globals().keys() else "Girl"
    $ KittyX.petnames = K_Pets[:] if "K_Pets" in globals().keys() else ["Girl"]
    $ KittyX.Cheated = K_Cheated if "K_Cheated" in globals().keys() else 0
    $ KittyX.Break = K_Break[:] if "K_Break" in globals().keys() else [0,0]
    $ KittyX.Forced = K_Forced if "K_Forced" in globals().keys() else 0
    $ KittyX.event_counter["forced"] = K_ForcedCount if "K_ForcedCount" in globals().keys() else 0
    $ KittyX.location = K_Loc if "K_Loc" in globals().keys() else "hold"

    $ KittyX.Outfit = K_Outfit if "K_Outfit" in globals().keys() else "casual1"
    $ KittyX.OutfitDay = K_OutfitDay if "K_OutfitDay" in globals().keys() else "casual1"
    $ KittyX.SeenPeen = K_SeenPeen if "K_SeenPeen" in globals().keys() else 0
    $ KittyX.SeenChest = K_SeenChest if "K_SeenChest" in globals().keys() else 0
    $ KittyX.SeenPussy = K_SeenPussy if "K_SeenPussy" in globals().keys() else 0
    $ KittyX.SeenPanties = K_SeenPanties if "K_SeenPanties" in globals().keys() else 0
    $ KittyX.Upskirt = K_Upskirt if "K_Upskirt" in globals().keys() else 0
    $ KittyX.Uptop = K_Uptop if "K_Uptop" in globals().keys() else 0
    $ KittyX.underwearDown = K_PantiesDown if "K_PantiesDown" in globals().keys() else 0
    $ KittyX.Wet = K_Wet if "K_Wet" in globals().keys() else 0
    $ KittyX.Water = K_Water if "K_Water" in globals().keys() else 0
    $ KittyX.Spunk = K_Spunk if "K_Spunk" in globals().keys() else []
    $ KittyX.piercings = K_Pierce if "K_Pierce" in globals().keys() else 0
    $ KittyX.pubes = K_Pubes if "K_Pubes" in globals().keys() else 1
    $ KittyX.ArmPose = K_ArmPose if "K_ArmPose" in globals().keys() else 1
    $ KittyX.blushing = K_Blush if "K_Blush" in globals().keys() else 0
    $ KittyX.eyes = K_Eyes if "K_Eyes" in globals().keys() else "normal"
    $ KittyX.mouth = K_Mouth if "K_Mouth" in globals().keys() else "normal"
    $ KittyX.brows = K_Brows if "K_Brows" in globals().keys() else "normal"
    $ KittyX.emotion = K_emotion if "K_emotion" in globals().keys() else "normal"
    $ KittyX.held_item = K_Held if "K_Held" in globals().keys() else 0
    $ KittyX.arms = K_Arms if "K_Arms" in globals().keys() else 0
    $ KittyX.legs = K_Legs if "K_Legs" in globals().keys() else 0
    $ KittyX.top = K_Over if "K_Over" in globals().keys() else 0
    $ KittyX.neck = K_Neck if "K_Neck" in globals().keys() else 0
    $ KittyX.bra = K_Chest if "K_Chest" in globals().keys() else 0
    $ KittyX.underwear = K_Panties if "K_Panties" in globals().keys() else 0
    $ KittyX.accessory = K_Acc if "K_Acc" in globals().keys() else 0
    $ KittyX.hair = K_Hair if "K_Hair" in globals().keys() else 1
    $ KittyX.hose = K_Hose if "K_Hose" in globals().keys() else 0
    $ KittyX.Shame = K_Shame if "K_Shame" in globals().keys() else 0
    $ KittyX.Inventory = K_Inventory[:] if "K_Inventory" in globals().keys() else []



    $ KittyX.Custom1 = K_Custom[:] if "K_Custom" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ KittyX.Custom2 = K_Custom2[:] if "K_Custom2" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ KittyX.Custom3 = K_Custom3[:] if "K_Custom3" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ KittyX.TempClothes = K_TempClothes[:] if "K_TempClothes" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ KittyX.Gym = K_Gym[:] if "K_Gym" in globals().keys() else [0,0,"shorts",0,0,"sports_bra","green_panties",0,0,0,10]
    $ KittyX.sleepwear = K_Sleepwear[:] if "K_Sleepwear" in globals().keys() else [0,0,"shorts",0,0,"cami","green_panties",0,0,0,20]
    $ KittyX.Swim = K_Swim[:] if "K_Swim" in globals().keys() else [0,0,"blue_skirt",0,0,"bikini_top","bikini_bottoms",0,0,0,0]

    $ KittyX.Gag = K_Gag if "K_Gag" in globals().keys() else 0
    $ KittyX.Todo = K_Todo[:] if "K_Todo" in globals().keys() else []
    $ KittyX.PubeC = K_PubeC if "K_PubeC" in globals().keys() else 0
    $ KittyX.Clothing = K_Schedule if "K_Schedule" in globals().keys() else [0,0,0,0,0,0,0,0,0,0]

    $ KittyX.event_counter["orgasmed"]= K_Org if "K_Org" in globals().keys() else 0
    $ KittyX.session_orgasms = K_OCount if "K_OCount" in globals().keys() else 0
    $ KittyX.event_counter["caught"] = K_Caught if "K_Caught" in globals().keys() else 0
    $ KittyX.action_counter["kiss"] = K_Kissed if "K_Kissed" in globals().keys() else 0
    $ KittyX.event_counter["sleepover"] = K_Sleep if "K_Sleep" in globals().keys() else 0
    $ KittyX.action_counter["handjob"] = K_Hand if "K_Hand" in globals().keys() else 0
    $ KittyX.action_counter["footjob"] = K_Foot if "K_Foot" in globals().keys() else 0
    $ KittyX.event_counter["ass_slapped"] = K_Slap if "K_Slap" in globals().keys() else 0
    $ KittyX.Strip = K_Strip if "K_Strip" in globals().keys() else 0
    $ KittyX.action_counter["titjob"] = K_Tit if "K_Tit" in globals().keys() else 0
    $ KittyX.action_counter["sex"] = K_Sex if "K_Sex" in globals().keys() else 0
    $ KittyX.action_counter["anal"] = K_Anal if "K_Anal" in globals().keys() else 0
    $ KittyX.used_to_anal = K_Loose if "K_Loose" in globals().keys() else 0
    $ KittyX.action_counter["hotdog"] = K_Hotdog if "K_Hotdog" in globals().keys() else 0
    $ KittyX.action_counter["masturbation"] = K_Mast if "K_Mast" in globals().keys() else 0
    $ KittyX.action_counter["fondle_breasts"]= K_FondleB if "K_FondleB" in globals().keys() else 0
    $ KittyX.action_counter["fondle_thighs"]= K_FondleT if "K_FondleT" in globals().keys() else 0
    $ KittyX.action_counter["fondle_pussy"] = K_FondleP if "K_FondleP" in globals().keys() else 0
    $ KittyX.action_counter["fondle_ass"] = K_FondleA if "K_FondleA" in globals().keys() else 0
    $ KittyX.action_counter["dildo_pussy"] = K_DildoP if "K_DildoP" in globals().keys() else 0
    $ KittyX.action_counter["dildo_ass"] = K_DildoA if "K_DildoA" in globals().keys() else 0
    $ KittyX.Vib = K_Vib if "K_Vib" in globals().keys() else 0
    $ KittyX.Plug = K_Plug if "K_Plug" in globals().keys() else 0
    $ KittyX.action_counter["suck_breasts"] = K_SuckB if "K_SuckB" in globals().keys() else 0
    $ KittyX.action_counter["finger_pussy"] = K_InsertP if "K_InsertP" in globals().keys() else 0
    $ KittyX.action_counter["finger_ass"] = K_InsertA if "K_InsertA" in globals().keys() else 0
    $ KittyX.action_counter["eat_pussy"] = K_LickP if "K_LickP" in globals().keys() else 0
    $ KittyX.action_counter["eat_ass"] = K_LickA if "K_LickA" in globals().keys() else 0
    $ KittyX.action_counter["blowjob"] = K_Blow if "K_Blow" in globals().keys() else 0
    $ KittyX.event_counter["swallowed"] = K_Swallow if "K_Swallow" in globals().keys() else 0
    $ KittyX.event_counter["creampied"] = K_CreamP if "K_CreamP" in globals().keys() else 0
    $ KittyX.event_counter["anal_creampied"] = K_CreamA if "K_CreamA" in globals().keys() else 0
    $ KittyX.event_counter["been_with_girl"] = K_Les if "K_Les" in globals().keys() else 0
    $ KittyX.event_counter["seen_with_girl"] = K_LesWatch if "K_LesWatch" in globals().keys() else 0
    $ KittyX.SEXP = K_SEXP if "K_SEXP" in globals().keys() else 0
    $ KittyX.player_favorite_action = K_PlayerFav if "K_PlayerFav" in globals().keys() else 0
    $ KittyX.favorite_action = K_Favorite if "K_Favorite" in globals().keys() else 0


    $ KittyX.accessory = K_Boots if "K_Boots" in globals().keys() else 0
    $ KittyX.home = "bg_kitty"

    $ KittyX.Outfit = "casual1" if KittyX.Outfit == "pink outfit" else KittyX.Outfit
    $ KittyX.OutfitDay = "casual1" if KittyX.OutfitDay == "pink outfit" else KittyX.OutfitDay
    $ KittyX.Outfit = "casual2" if KittyX.Outfit == "red outfit" else KittyX.Outfit
    $ KittyX.OutfitDay = "casual2" if KittyX.OutfitDay == "red outfit" else KittyX.OutfitDay

    $ KittyX.Casual1 = [2,0,"capris","pink_top","gold_necklace","cami","green_panties",0,0,0,0]
    $ KittyX.Casual2 = [2,0,"black jeans","red_shirt",0,"bra","green_panties",0,0,0,0]

    $ KittyX.Schedule = [["bg_classroom","bg_dangerroom","bg_kitty","bg_kitty"],
                                        ["bg_classroom","bg_pool","bg_kitty","bg_kitty"],
                                        ["bg_classroom","bg_dangerroom","bg_kitty","bg_kitty"],
                                        ["bg_classroom","bg_pool","bg_kitty","bg_kitty"],
                                        ["bg_classroom","bg_dangerroom","bg_kitty","bg_kitty"],
                                        ["bg_campus","bg_dangerroom","bg_kitty","bg_kitty"],
                                        ["bg_campus","bg_dangerroom","bg_kitty","bg_kitty"],
                                        ]
    $ KittyX.hair = "evo"
    $ KittyX.LikeRogue = K_LikeRogue if "K_LikeRogue" in globals().keys() else 600
    $ KittyX.LikeEmma = K_LikeEmma if "K_LikeEmma" in globals().keys() else 500
    $ KittyX.LikeLaura = K_LikeLaura if "K_LikeLaura" in globals().keys() else 500
    $ KittyX.SexRogue = K_SexRogue if "K_SexRogue" in globals().keys() else 0
    $ KittyX.SexEmma = K_SexEmma if "K_SexEmma" in globals().keys() else 0
    $ KittyX.SexLaura = K_SexLaura if "K_SexLaura" in globals().keys() else 0

    $ KittyX.like = K_like if "K_like" in globals().keys() else ", like, "
    $ KittyX.Like = K_Like if "K_Like" in globals().keys() else "Like, "

    $ KittyX.massage_chart = ["shoulders","back","hips","thighs","calves","feet","feet","hips","ass","pussy"]
    $ KittyX.history.append("met") if "met" not in KittyX.history else KittyX.history




    if "EmmaX" not in globals().keys():
        $ EmmaX = GirlClass("Emma",500,0,0,10)
    $ EmmaX.name = Emmaname if "Emmaname" in globals().keys() else "Emma"
    $ EmmaX.Tag = "Emma"
    $ EmmaX.names = ["Emma"]
    $ EmmaX.love = E_Love if "E_Love" in globals().keys() else EmmaX.love
    $ EmmaX.obedience = E_Obed if "E_Obed" in globals().keys() else EmmaX.obedience
    $ EmmaX.inhibition = E_Inbt if "E_Inbt" in globals().keys() else EmmaX.inhibition
    $ EmmaX.lust = E_Lust if "E_Lust" in globals().keys() else EmmaX.lust
    $ EmmaX.Thirst = E_Thirst if "E_Thirst" in globals().keys() else 0
    $ EmmaX.addiction = E_Addict if "E_Addict" in globals().keys() else 0
    $ EmmaX.addiction_rate = E_Addictionrate if "E_Addictionrate" in globals().keys() else 0
    $ EmmaX.resistance = E_Resistance if "E_Resistance" in globals().keys() else 0
    $ EmmaX.Taboo = E_Taboo if "E_Taboo" in globals().keys() else 0
    $ EmmaX.XP = E_XP if "E_XP" in globals().keys() else 0
    $ EmmaX.StatPoints = E_StatPoints if "E_StatPoints" in globals().keys() else 0
    $ EmmaX.XPgoal = E_XPgoal if "E_XPgoal" in globals().keys() else 100
    $ EmmaX.Lvl = E_Lvl if "E_Lvl" in globals().keys() else 1
    $ EmmaX.sprite_location = E_sprite_location if "E_sprite_location" in globals().keys() else stage_center
    $ EmmaX.sprite_layer = E_Layer if "E_Layer" in globals().keys() else 50
    $ EmmaX.remaining_actions = E_Action if "E_Action" in globals().keys() else 3
    $ EmmaX.max_actions = E_MaxAction if "E_MaxAction" in globals().keys() else 3
    $ EmmaX.Rep = E_Rep if "E_Rep" in globals().keys() else 600
    $ EmmaX.recent_history = E_recent_history[:] if "E_recent_history" in globals().keys() else []
    $ EmmaX.daily_history = E_daily_history[:] if "E_daily_history" in globals().keys() else []
    $ EmmaX.Traits = E_Traits[:] if "E_Traits" in globals().keys() else []
    $ EmmaX.history = E_History[:] if "E_History" in globals().keys() else []
    $ EmmaX.Date = E_Date if "E_Date" in globals().keys() else 0
    $ EmmaX.Chat = E_Chat[:] if "E_Chat" in globals().keys() else [0,0,0,0,0,0]
    $ EmmaX.Event = E_Event[:] if "E_Event" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]


    $ EmmaX.petname = E_Pet if "E_Pet" in globals().keys() else "Girl"
    $ EmmaX.petnames = E_Pets[:] if "E_Pets" in globals().keys() else ["Girl"]
    $ EmmaX.Cheated = E_Cheated if "E_Cheated" in globals().keys() else 0
    $ EmmaX.Break = E_Break[:] if "E_Break" in globals().keys() else [0,0]
    $ EmmaX.Forced = E_Forced if "E_Forced" in globals().keys() else 0
    $ EmmaX.event_counter["forced"] = E_ForcedCount if "E_ForcedCount" in globals().keys() else 0
    $ EmmaX.location = E_Loc if "E_Loc" in globals().keys() else "hold"

    $ EmmaX.Outfit = E_Outfit if "E_Outfit" in globals().keys() else "casual1"
    $ EmmaX.OutfitDay = E_OutfitDay if "E_OutfitDay" in globals().keys() else "casual1"
    $ EmmaX.SeenPeen = E_SeenPeen if "E_SeenPeen" in globals().keys() else 0
    $ EmmaX.SeenChest = E_SeenChest if "E_SeenChest" in globals().keys() else 0
    $ EmmaX.SeenPussy = E_SeenPussy if "E_SeenPussy" in globals().keys() else 0
    $ EmmaX.SeenPanties = E_SeenPanties if "E_SeenPanties" in globals().keys() else 0
    $ EmmaX.Upskirt = E_Upskirt if "E_Upskirt" in globals().keys() else 0
    $ EmmaX.Uptop = E_Uptop if "E_Uptop" in globals().keys() else 0
    $ EmmaX.underwearDown = E_PantiesDown if "E_PantiesDown" in globals().keys() else 0
    $ EmmaX.Wet = E_Wet if "E_Wet" in globals().keys() else 0
    $ EmmaX.Water = E_Water if "E_Water" in globals().keys() else 0
    $ EmmaX.Spunk = E_Spunk if "E_Spunk" in globals().keys() else []
    $ EmmaX.piercings = E_Pierce if "E_Pierce" in globals().keys() else 0
    $ EmmaX.pubes = E_Pubes if "E_Pubes" in globals().keys() else 0
    $ EmmaX.ArmPose = E_ArmPose if "E_ArmPose" in globals().keys() else 1
    $ EmmaX.blushing = E_Blush if "E_Blush" in globals().keys() else 0
    $ EmmaX.eyes = E_Eyes if "E_Eyes" in globals().keys() else "normal"
    $ EmmaX.mouth = E_Mouth if "E_Mouth" in globals().keys() else "normal"
    $ EmmaX.brows = E_Brows if "E_Brows" in globals().keys() else "normal"
    $ EmmaX.emotion = E_emotion if "E_emotion" in globals().keys() else "normal"
    $ EmmaX.held_item = E_Held if "E_Held" in globals().keys() else 0
    $ EmmaX.arms = E_Arms if "E_Arms" in globals().keys() else 0
    $ EmmaX.legs = E_Legs if "E_Legs" in globals().keys() else 0
    $ EmmaX.top = E_Over if "E_Over" in globals().keys() else 0
    $ EmmaX.neck = E_Neck if "E_Neck" in globals().keys() else 0
    $ EmmaX.bra = E_Chest if "E_Chest" in globals().keys() else 0
    $ EmmaX.underwear = E_Panties if "E_Panties" in globals().keys() else 0
    $ EmmaX.accessory = E_Acc if "E_Acc" in globals().keys() else 0
    $ EmmaX.hair = E_Hair if "E_Hair" in globals().keys() else 1
    $ EmmaX.hose = E_Hose if "E_Hose" in globals().keys() else 0
    $ EmmaX.Shame = E_Shame if "E_Shame" in globals().keys() else 0
    $ EmmaX.Inventory = E_Inventory[:] if "E_Inventory" in globals().keys() else []



    $ EmmaX.Custom1 = E_Custom[:] if "E_Custom" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ EmmaX.Custom2 = E_Custom2[:] if "E_Custom2" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ EmmaX.Custom3 = E_Custom3[:] if "E_Custom3" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ EmmaX.TempClothes = E_TempClothes[:] if "E_TempClothes" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ EmmaX.Gym = E_Gym[:] if "E_Gym" in globals().keys() else [0,0,0,0,0,"sports_bra","sports_panties",0,0,0,10]
    $ EmmaX.sleepwear = E_Sleepwear[:] if "E_Sleepwear" in globals().keys() else [0,0,0,0,0,"corset","white_panties",0,0,0,25]
    $ EmmaX.Swim = E_Swim[:] if "E_Swim" in globals().keys() else [0,0,0,0,0,"bikini_top","bikini_bottoms",0,0,0,0]

    $ EmmaX.Gag = E_Gag if "E_Gag" in globals().keys() else 0
    $ EmmaX.Todo = E_Todo[:] if "E_Todo" in globals().keys() else []
    $ EmmaX.PubeC = E_PubeC if "E_PubeC" in globals().keys() else 0
    $ EmmaX.Clothing = E_Schedule if "E_Schedule" in globals().keys() else [0,0,0,0,0,0,0,0,0,0]

    $ EmmaX.event_counter["orgasmed"]= E_Org if "E_Org" in globals().keys() else 0
    $ EmmaX.session_orgasms = E_OCount if "E_OCount" in globals().keys() else 0
    $ EmmaX.event_counter["caught"] = E_Caught if "E_Caught" in globals().keys() else 0
    $ EmmaX.action_counter["kiss"] = E_Kissed if "E_Kissed" in globals().keys() else 0
    $ EmmaX.event_counter["sleepover"] = E_Sleep if "E_Sleep" in globals().keys() else 0
    $ EmmaX.action_counter["handjob"] = E_Hand if "E_Hand" in globals().keys() else 0
    $ EmmaX.action_counter["footjob"] = E_Foot if "E_Foot" in globals().keys() else 0
    $ EmmaX.event_counter["ass_slapped"] = E_Slap if "E_Slap" in globals().keys() else 0
    $ EmmaX.Strip = E_Strip if "E_Strip" in globals().keys() else 0
    $ EmmaX.action_counter["titjob"] = E_Tit if "E_Tit" in globals().keys() else 0
    $ EmmaX.action_counter["sex"] = E_Sex if "E_Sex" in globals().keys() else 0
    $ EmmaX.action_counter["anal"] = E_Anal if "E_Anal" in globals().keys() else 0
    $ EmmaX.used_to_anal = E_Loose if "E_Loose" in globals().keys() else 2
    $ EmmaX.action_counter["hotdog"] = E_Hotdog if "E_Hotdog" in globals().keys() else 0
    $ EmmaX.action_counter["masturbation"] = E_Mast if "E_Mast" in globals().keys() else 0
    $ EmmaX.action_counter["fondle_breasts"]= E_FondleB if "E_FondleB" in globals().keys() else 0
    $ EmmaX.action_counter["fondle_thighs"]= E_FondleT if "E_FondleT" in globals().keys() else 0
    $ EmmaX.action_counter["fondle_pussy"] = E_FondleP if "E_FondleP" in globals().keys() else 0
    $ EmmaX.action_counter["fondle_ass"] = E_FondleA if "E_FondleA" in globals().keys() else 0
    $ EmmaX.action_counter["dildo_pussy"] = E_DildoP if "E_DildoP" in globals().keys() else 0
    $ EmmaX.action_counter["dildo_ass"] = E_DildoA if "E_DildoA" in globals().keys() else 0
    $ EmmaX.Vib = E_Vib if "E_Vib" in globals().keys() else 0
    $ EmmaX.Plug = E_Plug if "E_Plug" in globals().keys() else 0
    $ EmmaX.action_counter["suck_breasts"] = E_SuckB if "E_SuckB" in globals().keys() else 0
    $ EmmaX.action_counter["finger_pussy"] = E_InsertP if "E_InsertP" in globals().keys() else 0
    $ EmmaX.action_counter["finger_ass"] = E_InsertA if "E_InsertA" in globals().keys() else 0
    $ EmmaX.action_counter["eat_pussy"] = E_LickP if "E_LickP" in globals().keys() else 0
    $ EmmaX.action_counter["eat_ass"] = E_LickA if "E_LickA" in globals().keys() else 0
    $ EmmaX.action_counter["blowjob"] = E_Blow if "E_Blow" in globals().keys() else 0
    $ EmmaX.event_counter["swallowed"] = E_Swallow if "E_Swallow" in globals().keys() else 0
    $ EmmaX.event_counter["creampied"] = E_CreamP if "E_CreamP" in globals().keys() else 0
    $ EmmaX.event_counter["anal_creampied"] = E_CreamA if "E_CreamA" in globals().keys() else 0
    $ EmmaX.event_counter["been_with_girl"] = E_Les if "E_Les" in globals().keys() else 0
    $ EmmaX.event_counter["seen_with_girl"] = E_LesWatch if "E_LesWatch" in globals().keys() else 0
    $ EmmaX.SEXP = E_SEXP if "E_SEXP" in globals().keys() else 0
    $ EmmaX.player_favorite_action = E_PlayerFav if "E_PlayerFav" in globals().keys() else 0
    $ EmmaX.favorite_action = E_Favorite if "E_Favorite" in globals().keys() else 0


    $ EmmaX.accessory = E_Boots if "E_Boots" in globals().keys() else 0
    $ EmmaX.home = "bg_emma"

    $ EmmaX.Outfit = "casual1" if EmmaX.Outfit == "teacher" else EmmaX.Outfit
    $ EmmaX.OutfitDay = "casual1" if EmmaX.OutfitDay == "teacher" else EmmaX.OutfitDay
    $ EmmaX.Outfit = "casual2" if EmmaX.Outfit == "costume" else EmmaX.Outfit
    $ EmmaX.OutfitDay = "casual2" if EmmaX.OutfitDay == "costume" else EmmaX.OutfitDay

    $ EmmaX.Casual1 = [2,0,"pants","jacket","choker","corset","white_panties",0,0,0,0]
    $ EmmaX.Casual2 = [2,"gloves","pants",0,"choker","corset","white_panties",0,0,0,5]

    $ EmmaX.Schedule = [["bg_teacher","bg_teacher","bg_classroom","bg_emma"],
                                        ["bg_teacher","bg_teacher","bg_dangerroom","bg_emma"],
                                        ["bg_teacher","bg_teacher","bg_classroom","bg_emma"],
                                        ["bg_teacher","bg_teacher","bg_dangerroom","bg_emma"],
                                        ["bg_teacher","bg_teacher","bg_classroom","bg_emma"],
                                        ["bg_pool","bg_pool","bg_emma","bg_emma"],
                                        ["bg_pool","bg_pool","bg_emma","bg_emma"],
                                        ]
    $ EmmaX.hair = "wavy"
    $ EmmaX.LikeRogue = E_LikeRogue if "E_LikeRogue" in globals().keys() else 500
    $ EmmaX.LikeKitty = E_LikeKitty if "E_LikeKitty" in globals().keys() else 500
    $ EmmaX.LikeLaura = E_LikeLaura if "E_LikeLaura" in globals().keys() else 500
    $ EmmaX.SexRogue = E_SexRogue if "E_SexRogue" in globals().keys() else 0
    $ EmmaX.SexKitty = E_SexKitty if "E_SexKitty" in globals().keys() else 0
    $ EmmaX.SexLaura = E_SexLaura if "E_SexLaura" in globals().keys() else 0
    $ EmmaX.massage_chart = ["shoulders","neck","neck","back","hips","ass","ass","back","breasts","breasts"]
    $ EmmaX.history.append("met") if "met" not in EmmaX.history else EmmaX.history




    if "LauraX" not in globals().keys():
        $ LauraX = GirlClass("Laura",500,0,0,10)
    $ LauraX.name = Lauraname if "Lauraname" in globals().keys() else "Laura"
    $ LauraX.Tag = "Laura"
    $ LauraX.names = ["Laura"]
    $ LauraX.love = L_Love if "L_Love" in globals().keys() else LauraX.love
    $ LauraX.obedience = L_Obed if "L_Obed" in globals().keys() else LauraX.obedience
    $ LauraX.inhibition = L_Inbt if "L_Inbt" in globals().keys() else LauraX.inhibition
    $ LauraX.lust = L_Lust if "L_Lust" in globals().keys() else LauraX.lust
    $ LauraX.Thirst = L_Thirst if "L_Thirst" in globals().keys() else 0
    $ LauraX.addiction = L_Addict if "L_Addict" in globals().keys() else 0
    $ LauraX.addiction_rate = L_Addictionrate if "L_Addictionrate" in globals().keys() else 0
    $ LauraX.resistance = L_Resistance if "L_Resistance" in globals().keys() else 0
    $ LauraX.Taboo = L_Taboo if "L_Taboo" in globals().keys() else 0
    $ LauraX.XP = L_XP if "L_XP" in globals().keys() else 0
    $ LauraX.StatPoints = L_StatPoints if "L_StatPoints" in globals().keys() else 0
    $ LauraX.XPgoal = L_XPgoal if "L_XPgoal" in globals().keys() else 100
    $ LauraX.Lvl = L_Lvl if "L_Lvl" in globals().keys() else 1
    $ LauraX.sprite_location = L_sprite_location if "L_sprite_location" in globals().keys() else stage_center
    $ LauraX.sprite_layer = L_Layer if "L_Layer" in globals().keys() else 50
    $ LauraX.remaining_actions = L_Action if "L_Action" in globals().keys() else 3
    $ LauraX.max_actions = L_MaxAction if "L_MaxAction" in globals().keys() else 3
    $ LauraX.Rep = L_Rep if "L_Rep" in globals().keys() else 600
    $ LauraX.recent_history = L_recent_history[:] if "L_recent_history" in globals().keys() else []
    $ LauraX.daily_history = L_daily_history[:] if "L_daily_history" in globals().keys() else []
    $ LauraX.Traits = L_Traits[:] if "L_Traits" in globals().keys() else []
    $ LauraX.history = L_History[:] if "L_History" in globals().keys() else []
    $ LauraX.Date = L_Date if "L_Date" in globals().keys() else 0
    $ LauraX.Chat = L_Chat[:] if "L_Chat" in globals().keys() else [0,0,0,0,0,0]
    $ LauraX.Event = L_Event[:] if "L_Event" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]


    $ LauraX.petname = L_Pet if "L_Pet" in globals().keys() else "Girl"
    $ LauraX.petnames = L_Pets[:] if "L_Pets" in globals().keys() else ["Girl"]
    $ LauraX.Cheated = L_Cheated if "L_Cheated" in globals().keys() else 0
    $ LauraX.Break = L_Break[:] if "L_Break" in globals().keys() else [0,0]
    $ LauraX.Forced = L_Forced if "L_Forced" in globals().keys() else 0
    $ LauraX.event_counter["forced"] = L_ForcedCount if "L_ForcedCount" in globals().keys() else 0
    $ LauraX.location = L_Loc if "L_Loc" in globals().keys() else "hold"

    $ LauraX.Outfit = L_Outfit if "L_Outfit" in globals().keys() else "casual1"
    $ LauraX.OutfitDay = L_OutfitDay if "L_OutfitDay" in globals().keys() else "casual1"
    $ LauraX.SeenPeen = L_SeenPeen if "L_SeenPeen" in globals().keys() else 0
    $ LauraX.SeenChest = L_SeenChest if "L_SeenChest" in globals().keys() else 0
    $ LauraX.SeenPussy = L_SeenPussy if "L_SeenPussy" in globals().keys() else 0
    $ LauraX.SeenPanties = L_SeenPanties if "L_SeenPanties" in globals().keys() else 0
    $ LauraX.Upskirt = L_Upskirt if "L_Upskirt" in globals().keys() else 0
    $ LauraX.Uptop = L_Uptop if "L_Uptop" in globals().keys() else 0
    $ LauraX.underwearDown = L_PantiesDown if "L_PantiesDown" in globals().keys() else 0
    $ LauraX.Wet = L_Wet if "L_Wet" in globals().keys() else 0
    $ LauraX.Water = L_Water if "L_Water" in globals().keys() else 0
    $ LauraX.Spunk = L_Spunk if "L_Spunk" in globals().keys() else []
    $ LauraX.piercings = L_Pierce if "L_Pierce" in globals().keys() else 0
    $ LauraX.pubes = L_Pubes if "L_Pubes" in globals().keys() else 1
    $ LauraX.ArmPose = L_ArmPose if "L_ArmPose" in globals().keys() else 1
    $ LauraX.blushing = L_Blush if "L_Blush" in globals().keys() else 0
    $ LauraX.eyes = L_Eyes if "L_Eyes" in globals().keys() else "normal"
    $ LauraX.mouth = L_Mouth if "L_Mouth" in globals().keys() else "normal"
    $ LauraX.brows = L_Brows if "L_Brows" in globals().keys() else "normal"
    $ LauraX.emotion = L_emotion if "L_emotion" in globals().keys() else "normal"
    $ LauraX.held_item = L_Held if "L_Held" in globals().keys() else 0
    $ LauraX.arms = L_Arms if "L_Arms" in globals().keys() else 0
    $ LauraX.legs = L_Legs if "L_Legs" in globals().keys() else 0
    $ LauraX.top = L_Over if "L_Over" in globals().keys() else 0
    $ LauraX.neck = L_Neck if "L_Neck" in globals().keys() else 0
    $ LauraX.bra = L_Chest if "L_Chest" in globals().keys() else 0
    $ LauraX.underwear = L_Panties if "L_Panties" in globals().keys() else 0
    $ LauraX.accessory = L_Acc if "L_Acc" in globals().keys() else 0
    $ LauraX.hair = L_Hair if "L_Hair" in globals().keys() else 1
    $ LauraX.hose = L_Hose if "L_Hose" in globals().keys() else 0
    $ LauraX.Shame = L_Shame if "L_Shame" in globals().keys() else 0
    $ LauraX.Inventory = L_Inventory[:] if "L_Inventory" in globals().keys() else []



    $ LauraX.Custom1 = L_Custom[:] if "L_Custom" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ LauraX.Custom2 = L_Custom2[:] if "L_Custom2" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ LauraX.Custom3 = L_Custom3[:] if "L_Custom3" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ LauraX.TempClothes = L_TempClothes[:] if "L_TempClothes" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ LauraX.Gym = L_Gym[:] if "L_Gym" in globals().keys() else [2,"wrists","leather_pants",0,0,"leather_bra","leather_panties",0,0,0,0]
    $ LauraX.sleepwear = L_Sleepwear[:] if "L_Sleepwear" in globals().keys() else [0,0,0,0,0,"leather_bra","leather_panties",0,0,0,20]
    $ LauraX.Swim = L_Swim[:] if "L_Swim" in globals().keys() else [0,0,0,0,0,"bikini_top","bikini_bottoms",0,0,0,0]

    $ LauraX.Gag = L_Gag if "L_Gag" in globals().keys() else 0
    $ LauraX.Todo = L_Todo[:] if "L_Todo" in globals().keys() else []
    $ LauraX.PubeC = L_PubeC if "L_PubeC" in globals().keys() else 0
    $ LauraX.Clothing = L_Schedule if "L_Schedule" in globals().keys() else [0,0,0,0,0,0,0,0,0,0]

    $ LauraX.event_counter["orgasmed"]= L_Org if "L_Org" in globals().keys() else 0
    $ LauraX.session_orgasms = L_OCount if "L_OCount" in globals().keys() else 0
    $ LauraX.event_counter["caught"] = L_Caught if "L_Caught" in globals().keys() else 0
    $ LauraX.action_counter["kiss"] = L_Kissed if "L_Kissed" in globals().keys() else 0
    $ LauraX.event_counter["sleepover"] = L_Sleep if "L_Sleep" in globals().keys() else 0
    $ LauraX.action_counter["handjob"] = L_Hand if "L_Hand" in globals().keys() else 0
    $ LauraX.action_counter["footjob"] = L_Foot if "L_Foot" in globals().keys() else 0
    $ LauraX.event_counter["ass_slapped"] = L_Slap if "L_Slap" in globals().keys() else 0
    $ LauraX.Strip = L_Strip if "L_Strip" in globals().keys() else 0
    $ LauraX.action_counter["titjob"] = L_Tit if "L_Tit" in globals().keys() else 0
    $ LauraX.action_counter["sex"] = L_Sex if "L_Sex" in globals().keys() else 0
    $ LauraX.action_counter["anal"] = L_Anal if "L_Anal" in globals().keys() else 0
    $ LauraX.used_to_anal = L_Loose if "L_Loose" in globals().keys() else 2
    $ LauraX.action_counter["hotdog"] = L_Hotdog if "L_Hotdog" in globals().keys() else 0
    $ LauraX.action_counter["masturbation"] = L_Mast if "L_Mast" in globals().keys() else 0
    $ LauraX.action_counter["fondle_breasts"]= L_FondleB if "L_FondleB" in globals().keys() else 0
    $ LauraX.action_counter["fondle_thighs"]= L_FondleT if "L_FondleT" in globals().keys() else 0
    $ LauraX.action_counter["fondle_pussy"] = L_FondleP if "L_FondleP" in globals().keys() else 0
    $ LauraX.action_counter["fondle_ass"] = L_FondleA if "L_FondleA" in globals().keys() else 0
    $ LauraX.action_counter["dildo_pussy"] = L_DildoP if "L_DildoP" in globals().keys() else 0
    $ LauraX.action_counter["dildo_ass"] = L_DildoA if "L_DildoA" in globals().keys() else 0
    $ LauraX.Vib = L_Vib if "L_Vib" in globals().keys() else 0
    $ LauraX.Plug = L_Plug if "L_Plug" in globals().keys() else 0
    $ LauraX.action_counter["suck_breasts"] = L_SuckB if "L_SuckB" in globals().keys() else 0
    $ LauraX.action_counter["finger_pussy"] = L_InsertP if "L_InsertP" in globals().keys() else 0
    $ LauraX.action_counter["finger_ass"] = L_InsertA if "L_InsertA" in globals().keys() else 0
    $ LauraX.action_counter["eat_pussy"] = L_LickP if "L_LickP" in globals().keys() else 0
    $ LauraX.action_counter["eat_ass"] = L_LickA if "L_LickA" in globals().keys() else 0
    $ LauraX.action_counter["blowjob"] = L_Blow if "L_Blow" in globals().keys() else 0
    $ LauraX.event_counter["swallowed"] = L_Swallow if "L_Swallow" in globals().keys() else 0
    $ LauraX.event_counter["creampied"] = L_CreamP if "L_CreamP" in globals().keys() else 0
    $ LauraX.event_counter["anal_creampied"] = L_CreamA if "L_CreamA" in globals().keys() else 0
    $ LauraX.event_counter["been_with_girl"] = L_Les if "L_Les" in globals().keys() else 0
    $ LauraX.event_counter["seen_with_girl"] = L_LesWatch if "L_LesWatch" in globals().keys() else 0
    $ LauraX.SEXP = L_SEXP if "L_SEXP" in globals().keys() else 0
    $ LauraX.player_favorite_action = L_PlayerFav if "L_PlayerFav" in globals().keys() else 0
    $ LauraX.favorite_action = L_Favorite if "L_Favorite" in globals().keys() else 0


    $ LauraX.accessory = L_Boots if "L_Boots" in globals().keys() else 0
    $ LauraX.home = "bg_laura"

    $ LauraX.Outfit = "casual1" if LauraX.Outfit == "mission" else LauraX.Outfit
    $ LauraX.OutfitDay = "casual1" if LauraX.OutfitDay == "mission" else LauraX.OutfitDay
    $ LauraX.Outfit = "casual2" if LauraX.Outfit == "street" else LauraX.Outfit
    $ LauraX.OutfitDay = "casual2" if LauraX.OutfitDay == "street" else LauraX.OutfitDay

    $ LauraX.Casual1 = [2,"wrists","leather_pants",0,0,"leather_bra","leather_panties",0,0,0,0]
    $ LauraX.Casual2 = [2,0,"skirt",0,"jacket","leather_bra","leather_panties",0,0,0,0]

    $ LauraX.Schedule = [["bg_pool","bg_classroom","bg_dangerroom","bg_laura"],
                                        ["bg_dangerroom","bg_classroom","bg_campus","bg_laura"],
                                        ["bg_pool","bg_classroom","bg_dangerroom","bg_laura"],
                                        ["bg_dangerroom","bg_classroom","bg_campus","bg_laura"],
                                        ["bg_pool","bg_classroom","bg_dangerroom","bg_laura"],
                                        ["bg_pool","bg_laura","bg_dangerroom","bg_laura"],
                                        ["bg_pool","bg_laura","bg_dangerroom","bg_laura"],
                                        ]
    $ LauraX.hair = "long"
    $ LauraX.LikeRogue = L_LikeRogue if "L_LikeRogue" in globals().keys() else 500
    $ LauraX.LikeKitty = L_LikeKitty if "L_LikeKitty" in globals().keys() else 500
    $ LauraX.LikeEmma = L_LikeEmma if "L_LikeEmma" in globals().keys() else 500
    $ LauraX.SexRogue = L_SexRogue if "L_SexRogue" in globals().keys() else 0
    $ LauraX.SexKitty = L_SexKitty if "L_SexKitty" in globals().keys() else 0
    $ LauraX.SexEmma = L_SexEmma if "L_SexEmma" in globals().keys() else 0
    $ LauraX.massage_chart = ["shoulders","back","arms","hips","thighs","calves","ass","ass","pussy","pussy"]
    $ LauraX.history.append("met") if "met" not in LauraX.history else LauraX.history

    $ LauraX.ScentTimer = 0
    $ LauraX.Claws = 0



    $ RogueX.names = ["Rogue"]
    $ RogueX.player_petname = R_Petname if "R_Petname" in globals().keys() else "Sugar"
    $ RogueX.player_petnames = R_Petnames[:] if "R_Petnames" in globals().keys() else ["Sugar",Player.name]
    $ RogueX.petname = R_Pet if "R_Pet" in globals().keys() else "Rogue"
    $ RogueX.petnames = R_Pets[:] if "R_Pets" in globals().keys() else ["Rogue"]
    $ RogueX.history.append("met")

    $ KittyX.names = ["Kitty"]
    $ KittyX.player_petname = K_Petname if "K_Petname" in globals().keys() else Player.name[:1]
    $ KittyX.player_petnames = K_Petnames[:] if "K_Petnames" in globals().keys() else ["sweetie",Player.name[:1],Player.name]
    $ KittyX.petname = K_Pet if "K_Pet" in globals().keys() else "Kitty"
    $ KittyX.petnames = K_Pets[:] if "K_Pets" in globals().keys() else ["Kitty"]

    $ EmmaX.names = ["Ms. Frost","Emma"]
    $ EmmaX.player_petname = E_Petname if "E_Petname" in globals().keys() else "young man"
    $ EmmaX.player_petnames = E_Petnames[:] if "E_Petnames" in globals().keys() else ["young man",Player.name]
    $ EmmaX.petname = E_Pet if "E_Pet" in globals().keys() else EmmaX.name
    $ EmmaX.petnames = E_Pets[:] if "E_Pets" in globals().keys() else ["Emma","Ms. Frost"]

    $ LauraX.names = ["X-23","Laura"]
    $ LauraX.player_petname = L_Petname if "L_Petname" in globals().keys() else "guy"
    $ LauraX.player_petnames = L_Petnames[:] if "L_Petnames" in globals().keys() else ["guy",Player.name]
    $ LauraX.petname = L_Pet if "L_Pet" in globals().keys() else LauraX.name
    $ LauraX.petnames = L_Pets[:] if "L_Pets" in globals().keys() else ["Laura","X-23"]

    if focused_Girl == "Rogue":
        $ focused_Girl = RogueX
    elif focused_Girl == "Kitty":
        $ focused_Girl = KittyX
    elif focused_Girl == "Emma":
        $ focused_Girl = EmmaX
    elif focused_Girl == "Laura":
        $ focused_Girl = LauraX
    else:
        $ focused_Girl = RogueX

    $ PersonalRooms.append("bg_rogue") if "bg_rogue" not in PersonalRooms else PersonalRooms
    $ PersonalRooms.append("bg_kitty") if "met" in KittyX.history and "bg_kitty" not in PersonalRooms else PersonalRooms
    $ PersonalRooms.append("bg_emma") if "met" in EmmaX.history and "bg_emma" not in PersonalRooms else PersonalRooms
    $ PersonalRooms.append("bg_laura") if "met" in LauraX.history and "bg_laura" not in PersonalRooms else PersonalRooms

    $ active_Girls.append(RogueX) if RogueX not in active_Girls else active_Girls
    $ active_Girls.append(KittyX) if "met" in KittyX.history and KittyX not in active_Girls else active_Girls
    $ active_Girls.append(EmmaX) if "met" in EmmaX.history and EmmaX not in active_Girls else active_Girls
    $ active_Girls.append(LauraX) if "met" in LauraX.history and LauraX not in active_Girls else active_Girls

    $ all_Girls.append(RogueX) if RogueX not in all_Girls else all_Girls
    $ all_Girls.append(KittyX) if KittyX not in all_Girls else all_Girls
    $ all_Girls.append(EmmaX) if EmmaX not in all_Girls else all_Girls
    $ all_Girls.append(LauraX) if LauraX not in all_Girls else all_Girls


    $ BO = all_Girls[:]
    while BO:
        if BO[0].Tag in Player.Harem:
            $ Player.Harem.remove(BO[0].Tag)
            $ Player.Harem.append(BO[0])
        if BO[0].Tag in Digits:
            $ Digits.remove(BO[0].Tag)
            $ Digits.append(BO[0])
        if BO[0].Tag in Keys:
            $ Keys.remove(BO[0].Tag)
            $ Keys.append(BO[0])
        if BO[0].Tag in Rules:
            $ Rules.remove(BO[0].Tag)
            $ Rules.append(BO[0])
        $ Counter = 10
        while Counter > 0:
            $ Counter -= 1
            if BO[0].Clothing[Counter] == "custom":
                $ BO[0].Clothing[Counter] = "custom1"

        while len(BO[0].Custom1) < 11:
            $ BO[0].Custom1.append(0)
        while len(BO[0].Custom2) < 11:
            $ BO[0].Custom2.append(0)
        while len(BO[0].Custom3) < 11:
            $ BO[0].Custom3.append(0)
        while len(BO[0].TempClothes) < 11:
            $ BO[0].TempClothes.append(0)
        while len(BO[0].Gym) < 11:
            $ BO[0].Gym.append(0)
        while len(BO[0].sleepwear) < 11:
            $ BO[0].sleepwear.append(0)
        while len(BO[0].Swim) < 11:
            $ BO[0].Swim.append(0)

        $ BO[0].change_outfit(Changed=1)
        $ BO.remove(BO[0])


    $ Party = []
    if "Adjacent" in globals().keys():
        $ del Adjacent
    $ Present = []
    $ Partner = 0

    $ SaveVersion = 990

    call VersionNumber
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
