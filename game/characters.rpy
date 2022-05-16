init python:

    class PlayerClass(object):
        def __init__(self):
            self.name = "Zero"
            self.Semen = 2                  #available semen
            self.Semen_Max = 3              #amount it maxes out at
            self.Focus = 0                  #progress towards orgasm
            self.FocusX = 0                 #is the player trying not to orgasm
            self.XP = 0
            self.SEXP = 0                   #how much sex you've had overall
            self.StatPoints = 0
            self.XPgoal = 100
            self.Lvl = 1
            self.Rep = 600
            self.recent_history = []
            self.daily_history = []
            self.Traits = []
            self.History = []
            self.Harem = []                 #this is a list of all girls the player is currently dating
            self.Male = 1

            self.Income = 12                #how much you make each day
            self.Cash = 20
            self.Inventory = []

            self.Sprite = 0
            self.Color = "green"
            self.Cock = "out"
            self.Spunk = 0
            self.Wet = 0

            self.addictive = False
            self.nonaddictive = False

            self.cologne = None

        def AddWord(self, Only = 0, Recent = 0, Daily = 0, Trait = 0, History = 0):
            if (Recent and not Only) or (Recent and Recent not in self.recent_history):
                self.recent_history.append(Recent)
            if (Daily and not Only) or (Daily and Daily not in self.daily_history):
                self.daily_history.append(Daily)
            if (Trait and not Only) or (Trait and Trait not in self.Traits):
                self.Traits.append(Trait)
            if (History and not Only) or (History and History not in self.History):
                self.History.append(History)
            return

        def DrainWord(self, Word, Recent = 1, Daily = 1, Traits = 0):
            if Recent and Word in self.recent_history:
                while Word in self.recent_history:
                    self.recent_history.remove(Word)
            if Daily and Word in self.daily_history:
                while Word in self.daily_history:
                    self.daily_history.remove(Word)
            if Traits and Word in self.Traits:
                while Word in self.Traits:
                    self.Traits.remove(Word)
            return

        def change_stat(self, flavor, check, value, greater_than = False, x_position = 0.75):
            stat = getattr(self,flavor)

            if greater_than:
                if stat >= check:
                    stat += value
                else:
                    value = 0
            else:
                if stat <= check:
                    stat += value
                else:
                    value = 0

            if value:
                CallHolder(value, "#FFFFFF", x_position)

            stat = 100 if stat > 100 else stat

            setattr(self, flavor, stat)

            return

    class GirlClass(object):
        def __init__(self, Name, love = 0, obedience = 0, inhibition = 0, lust = 0):
            self.name = Name        #changable by player, used in dialog
            self.Tag = Name         #Permanent label, used in code
            self.names = [Name]     #this is a list of primary names you're allowed to use

            self.love = love
            self.obedience = obedience
            self.inhibition = inhibition
            self.lust = lust

            self.Thirst = 0         #how much she wants sex
            self.Addict = 0         #how much she needs a fix, goes 0-100
            self.Addictionrate = 0  #how fast her Addict rises, goes from 0-10
            self.Resistance = 0     #how much her Addiciton drops naturally 0-3
            self.Taboo = 0
            self.XP = 0
            self.StatPoints = 0
            self.XPgoal = 100
            self.Lvl = 1
            self.sprite_location = StageCenter
            self.Layer = 50         #the layer her sprite appears on
            self.Action = 3         #times the girl can do something this turn
            self.MaxAction = 3      #max times the girl can do something per turn
            self.Pose = 0           #The sex pose the girl is in. If "doggy," show doggy style
            self.Rep = 600

            self.recent_history = []
            self.daily_history = []
            self.Traits = []
            self.History = []

            self.Date = 0
            self.Chat = [0,0,0,0,0,0]               #whether certain dialogs occurred
            self.Event = [0,0,0,0,0,0,0,0,0,0,0]    #whether certain relationship milestones happened
            self.Petname = "Zero"
            self.Petnames = ["Zero"]
            self.Pet = "Girl"
            self.Pets = ["Girl"]
            self.Cheated = 0
            self.Break = [0,0]      #minimum time between break-ups/number of total break-ups
            self.Forced = 0         #are they being coerced
            self.ForcedCount = 0    #countdown for how long they stay mad
            self.location = "hold"       #Where she is right now
            self.Home = 0           #where she lives

            self.Outfit = "casual1"         #current outfit
            self.OutfitDay = "casual1"      #outfit she picked for the day
            self.SeenPeen = 0
            self.SeenChest = 0
            self.SeenPussy = 0
            self.SeenPanties = 0
            self.Upskirt = 0
            self.Uptop = 0
            self.PantiesDown = 0
            self.Wet = 0
            self.Water = 0
            self.Spunk = []
            self.Pierce = 0
            self.Pubes = 1
            self.ArmPose = 1
            self.Blush = 0
            self.Eyes = "normal"
            self.Mouth = "normal"
            self.Brows = "normal"
            self.emotion = "normal"
            self.Held = 0                           #object held in hand
            self.Arms = 0
            self.Legs = 0
            self.Over = 0
            self.Neck = 0
            self.Chest = 0
            self.Panties = 0
            self.Acc = 0
            self.Hair = 1
            self.Hose = 0
            self.Shame = 0
            self.Inventory = []

            self.can_flirt = True
            self.wearing_skirt = False

            # toggle(0),arms/gloves(1),pants(2),shirt(3),necklace(4),bra(5),panties(6),accessory(7),hair(8),hose(9)
            self.Casual1 = [0,0,0,0,0,0,0,0,0,0,0]
            self.Casual2 = [0,0,0,0,0,0,0,0,0,0,0]
            self.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
            self.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
            self.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]
            self.TempClothes = [0,0,0,0,0,0,0,0,0,0,0]
            self.Gym = [0,0,0,0,0,0,0,0,0,0,0]
            self.Sleepwear = [0,0,0,0,0,0,0,0,0,0,0]
            self.Swim = [0,0,0,0,0,0,0,0,0,0,0]
            self.Gag = 0
            self.Todo = []                  #todo list, piercing, pubes, etc.
            self.PubeC = 0                  #countdown for when pubes grow back
            self.Schedule = [["MM", "MA", "ME", "MN"],
                            ["TM", "TA", "TE", "TN"],
                            ["WM", "WA", "WE", "WN"],
                            ["ThM", "ThA", "ThE", "ThN"],
                            ["FM", "FA", "FE", "FN"],
                            ["SaM", "SaA", "SaE", "SaN"],
                            ["SuM", "SuA", "SuE", "SuN"],
                            ] #Schedule[0-6][0-4] = Schedule[Day][Time]
            self.Clothing = [0,0,0,0,0,0,0,0,0,0]                      #schedules when she wears what: (0-6) = Mon-Sun, (7) Datewear, (8) Teachingwear, (9) Private

            self.action_counter = {}

            for action in all_actions:
                self.action_counter[action] = 0

            self.event_counter = {"orgasm": 0, "caught": 0, "sleepover": 0, "ass_slapped": 0, "stripped": 0,
                "swallowed": 0, "creampied": 0, "anal_creampied": 0,
                "been_with_girl": 0, "been_watched_with_girl": 0}

            self.OCount = 0
            self.Loose = 0

            self.Vib = 0
            self.Plug = 0

            self.SEXP = 0
            self.MassageChart = [0,0,0,0,0,0,0,0,0,0]
            self.PlayerFav = 0                              #you favorite activity with her
            self.Favorite = 0                               #her favorite activity

            if self.Tag == "Rogue":
                    self.voice = ch_r

                    self.Casual1 = [2,"gloves", "skirt", "mesh top", "spiked collar", "tank", "black panties", 0,0, "tights", 0]
                    self.Casual2 = [2,"gloves", "pants", "pink top", 0, "buttoned tank", "black panties", 0,0,0,0]
                    self.Gym = [0, "gloves", 0, "hoodie", 0, "sports bra", "shorts", 0,0,0,10]
                    self.Sleepwear = [0,0,0,0,0, "tank", "green panties", 0,0,0,20]
                    self.Swim = [0,0,0, "hoodie", 0, "bikini top", "bikini bottoms", 0,0,0,0]
                    self.Costume = [2,"gloves", "skirt", 0,0, "tube top", "black panties", "sweater", "cosplay", 0,0]

                    self.Home = "bg_rogue"
                    self.Hair = "evo"
                    self.LikeKitty = 600
                    self.LikeEmma = 500
                    self.LikeLaura = 500
                    self.Schedule = [["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                    ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                                    ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                    ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                                    ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                    ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"],
                                    ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"]] #Schedule[0-6][0-4] = Schedule[Weekday][time_index]

                    self.SexKitty = 0
                    self.SexEmma = 0
                    self.SexLaura = 0

                    self.History = ["met"]

                    self.MassageChart = ["shoulders", "arms", "arms", "hands", "hands", "back", "hips", "back", "breasts", "breasts"]
            elif self.Tag == "Kitty":
                    self.voice = ch_k

                    self.Casual1 = [2,0, "capris", "pink top", "gold necklace", "cami", "green panties", 0,0,0,0]
                    self.Casual2 = [2,0, "black jeans", "red shirt", "star necklace", "bra", "green panties", 0,0,0,0]
                    self.Gym = [0,0, "shorts", 0,0, "sports bra", "green panties", 0,0,0,10]
                    self.Sleepwear = [0,0, "shorts", 0,0, "cami", "green panties", 0,0,0,20]
                    self.Swim = [0,0, "blue skirt", 0,0, "bikini top", "bikini bottoms", 0,0,0,0]
                    self.Costume = [2,0, "dress", "jacket", "flower necklace", "dress", "lace panties", 0,0,0,0]

                    self.Home = "bg_kitty"
                    self.Hair = "evo"
                    self.LikeRogue = 600
                    self.LikeEmma = 500
                    self.LikeLaura = 500
                    self.like = ", like, "
                    self.Like = "Like, "
                    self.Schedule = [["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                    ["bg_classroom", "bg_pool", "bg_kitty", "bg_kitty"],
                                    ["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                    ["bg_classroom", "bg_pool", "bg_kitty", "bg_kitty"],
                                    ["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                    ["bg_campus", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                    ["bg_campus", "bg_dangerroom", "bg_kitty", "bg_kitty"]] #Schedule[0-6][0-4] = Schedule[Weekday][time_index]

                    self.SexRogue = 0
                    self.SexEmma = 0
                    self.SexLaura = 0

                    self.MassageChart = ["shoulders", "back", "hips", "thighs", "calves", "feet", "feet", "hips", "ass", "pussy"]
            elif self.Tag == "Emma":
                    self.voice = ch_e

                    self.Casual1 = [2,0, "pants", "jacket", "choker", "corset", "white panties", 0,0,0,0]
                    self.Casual2 = [2,"gloves", "pants", 0, "choker", "corset", "white panties", 0,0,0,5]
                    self.Gym = [0,0,0,0,0, "sports bra", "sports panties", 0,0,0,10]
                    self.Sleepwear = [0,0,0,0,0, "corset", "white panties", 0,0,0,25]
                    self.Swim = [0,0,0,0,0, "bikini top", "bikini bottoms", 0,0,0,0]
                    self.Costume =  [2,"gloves", "dress", "dress", "choker", 0, "lace panties", 0, "hat", "stockings and garterbelt", 0]
                    self.Home = "bg_emma"
                    self.Hair = "wavy"
                    self.Pubes = 0
                    self.LikeRogue = 500
                    self.LikeKitty = 500
                    self.LikeLaura = 500
                    self.Schedule = [["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
                                    ["bg_teacher", "bg_teacher", "bg_dangerroom", "bg_emma"],
                                    ["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
                                    ["bg_teacher", "bg_teacher", "bg_dangerroom", "bg_emma"],
                                    ["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
                                    ["bg_pool", "bg_pool", "bg_emma", "bg_emma"],
                                    ["bg_pool", "bg_pool", "bg_emma", "bg_emma"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][time_index]
                    self.SexRogue = 0
                    self.SexKitty = 0
                    self.SexLaura = 0
                    self.Loose = 2
                    self.MassageChart = ["shoulders", "neck", "neck", "back", "hips", "ass", "ass", "back", "breasts", "breasts"]

            elif self.Tag == "Laura":
                    self.voice = ch_l

                    self.Casual1 = [2,"wrists", "leather pants", 0, "leash choker", "leather bra", "black panties", 0,0,0,0]
                    self.Casual2 = [2,0, "skirt", "jacket", "leash choker", "leather bra", "black panties", 0,0,0,0]
                    self.Gym = [2,"wrists", "leather pants", 0,0, "leather bra", "black panties", 0,0,0,0]
                    self.Sleepwear = [0,0,0,0,0, "leather bra", "leather panties", 0,0,0,20]
                    self.Swim = [0,0,0,0,0, "bikini top", "bikini bottoms", 0,0,0,0]
                    self.Costume = [2,"gloves", "other skirt", 0,0, "white tank", "black panties", "suspenders", 0, "black stockings", 0]
                    self.Home = "bg_laura"
                    self.Hair = "long"
                    self.LikeRogue = 500
                    self.LikeKitty = 500
                    self.LikeEmma = 500
                    self.ScentTimer = 0 #this timer gives you X seconds of watching Laura before she notices you there
                    self.Claws = 0
                    self.Schedule = [["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                    ["bg_dangerroom", "bg_classroom", "bg_campus", "bg_laura"],
                                    ["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                    ["bg_dangerroom", "bg_classroom", "bg_campus", "bg_laura"],
                                    ["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                    ["bg_pool", "bg_laura", "bg_dangerroom", "bg_laura"],
                                    ["bg_pool", "bg_laura", "bg_dangerroom", "bg_laura"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][time_index]
                    self.SexRogue = 0
                    self.SexKitty = 0
                    self.SexEmma = 0
                    self.Loose = 2
                    self.MassageChart = ["shoulders", "back", "arms", "hips", "thighs", "calves", "ass", "ass", "pussy", "pussy"]

            elif self.Tag == "Jean":
                    self.voice = ch_j

                    # JeanX = GirlClass("Jean",200,0,1000,10) #inhibition falls to 800
                    self.StatStore = 0      #this stores love stat above 500 and distributes it later.
                    self.IX = 500           #this is an amount subtracted from her inhibition in most checks, and reduces over time

                    self.Casual1 = [2,0, "pants", "pink shirt", 0, "green bra", "green panties", 0,0,0,0]
                    self.Casual2 = [2,0, "skirt", "green shirt", 0, "green bra", "green panties", 0,0,0,0]
                    self.Gym = [0,0, "yoga pants", 0,0, "sports bra", "green panties", 0,0,0,0]
                    self.Sleepwear = [0,0,0, "pink shirt", 0, "green bra", "green panties", 0,0,0,0]
                    self.Swim = [0,0,0,0,0, "bikini top", "bikini bottoms", 0,0,0,0]
                    self.Costume =  [2,0, "shorts", "yellow shirt", 0, "green bra", "green panties", "suspenders", "pony", 0,0]
                    self.Home = "bg_jean"
                    self.Hair = "short"

                    RogueX.LikeJean = 200
                    KittyX.LikeJean = 300
                    EmmaX.LikeJean = 100
                    LauraX.LikeJean = 300

                    RogueX.SexJean = 0
                    KittyX.SexJean = 0
                    EmmaX.SexJean = 0
                    LauraX.SexJean = 0

                    self.LikeRogue = 500
                    self.LikeKitty = 500
                    self.LikeEmma = 300
                    self.LikeLaura = 500
                    self.SexRogue = 0
                    self.SexKitty = 0
                    self.SexEmma = 0
                    self.SexLaura = 0

                    #This stores up their like values for later.
                    self.LikeSRogue = 0
                    self.LikeSKitty = 0
                    self.LikeSEmma = 0
                    self.LikeSLaura = 0

                    self.Schedule = [["bg_classroom", "bg_classroom", "bg_dangerroom", "bg_jean"],
                                    ["bg_jean", "bg_classroom", "bg_jean", "bg_jean"],
                                    ["bg_jean", "bg_classroom", "bg_dangerroom", "bg_jean"],
                                    ["bg_classroom", "bg_classroom", "bg_jean", "bg_jean"],
                                    ["bg_jean", "bg_classroom", "bg_dangerroom", "bg_jean"],
                                    ["bg_dangerroom", "bg_campus", "bg_pool", "bg_jean"],
                                    ["bg_dangerroom", "bg_campus", "bg_pool", "bg_jean"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][time_index]

                    self.MassageChart = ["back", "shoulders", "neck", "neck", "back", "hips", "ass", "ass", "pussy", "pussy"]

            elif self.Tag == "Storm":
                    self.voice = ch_s

                    self.Casual1 = [2,0, "skirt", "white shirt", 0, "black bra", "white panties", 0,0,0,0]
                    self.Casual2 = [2,0, "pants", "jacket", 0, "sports bra", "white panties", 0,0,0,0]
                    self.Gym = [0,0, "yoga pants", 0,0, "sports bra", "white panties", 0,0,0,10]
                    self.Sleepwear = [0,0,0, "white shirt", 0,0, "white panties", 0,0,0,25]
                    self.Swim = [0,0,0,0,0, "bikini top", "bikini bottoms", 0,0,0,0]
                    self.Costume = [2,0,0,0, "ring necklace", "cos bra", "cos panties", "rings", "short", 0,0]
                    self.Home = "bg_storm"
                    self.Hair = "long"

                    self.LikeRogue = 500
                    self.LikeKitty = 600
                    self.LikeLaura = 500
                    self.LikeEmma = 400
                    self.LikeJean = 300
                    self.SexRogue = 0
                    self.SexKitty = 0
                    self.SexLaura = 0
                    self.SexEmma = 0
                    self.SexJean = 0

                    #fills in existing Girls
                    RogueX.LikeStorm = 600
                    KittyX.LikeStorm = 600
                    EmmaX.LikeStorm = 500
                    LauraX.LikeStorm = 500
                    JeanX.LikeStorm = 300

                    RogueX.SexStorm = 0
                    KittyX.SexStorm = 0
                    EmmaX.SexStorm = 0
                    LauraX.SexStorm = 0
                    JeanX.SexStorm = 0

                    self.Schedule = [["bg_storm", "bg_dangerroom", "bg_dangerroom", "bg_storm"],
                                    ["bg_teacher", "bg_teacher", "bg_classroom", "bg_storm"],
                                    ["bg_storm", "bg_dangerroom", "bg_dangerroom", "bg_storm"],
                                    ["bg_teacher", "bg_teacher", "bg_classroom", "bg_storm"],
                                    ["bg_pool", "bg_campus", "bg_classroom", "bg_storm"],
                                    ["bg_storm", "bg_campus", "bg_storm", "bg_pool"],
                                    ["bg_storm", "bg_campus", "bg_storm", "bg_pool"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][time_index]

                    self.MassageChart = ["feet", "calves", "thighs", "hips", "ass", "ass", "pussy", "ass", "pussy", "pussy"]

            elif self.Tag == "Jubes":
                    self.voice = ch_v

                    self.Casual1 = [2,0, "shorts", "red shirt", 0, "sports bra", "blue panties", "jacket", 0,0,0]
                    self.Casual2 = [2,0, "pants", "black shirt", 0, "sports bra", "blue panties", "jacket", 0,0,0]
                    self.Gym = [0,0, "pants", 0,0, "sports bra", "blue panties", 0,0,0,10]
                    self.Sleepwear = [0,0,0,0,0, "sports bra", "blue panties", 0,0,0,25]
                    self.Swim = [0,0,0,0,0, "bikini top", "bikini bottoms", 0,0,0,0]
                    self.Costume = [0,0, "pants", "black shirt", 0, "sports bra", "blue panties", "jacket", 0,0,0]
                    self.Home = "bg_jubes"
                    self.Hair = "shades"

                    self.LikeRogue = 500
                    self.LikeKitty = 600
                    self.LikeLaura = 600
                    self.LikeEmma = 500
                    self.LikeJean = 300
                    self.LikeStorm = 500
                    self.SexRogue = 0
                    self.SexKitty = 0
                    self.SexLaura = 0
                    self.SexEmma = 0
                    self.SexJean = 0
                    self.SexStorm = 0

                    #fills in existing Girls
                    RogueX.LikeJubes = 500
                    KittyX.LikeJubes = 600
                    EmmaX.LikeJubes = 500
                    LauraX.LikeJubes = 600
                    JeanX.LikeJubes = 300
                    StormX.LikeJubes = 500

                    RogueX.SexJubes = 0
                    KittyX.SexJubes = 0
                    EmmaX.SexJubes = 0
                    LauraX.SexJubes = 0
                    JeanX.SexJubes = 0
                    StormX.SexJubes = 0

                    self.Schedule = [["bg_jubes", "bg_dangerroom", "bg_dangerroom", "bg_jubes"],
                                    ["bg_classroom", "bg_classroom", "bg_jubes", "bg_jubes"],
                                    ["bg_jubes", "bg_dangerroom", "bg_dangerroom", "bg_jubes"],
                                    ["bg_dangerroom", "bg_dangerroom", "bg_jubes", "bg_jubes"],
                                    ["bg_pool", "bg_campus", "bg_campus", "bg_jubes"],
                                    ["bg_jubes", "bg_campus", "bg_jubes", "bg_pool"],
                                    ["bg_jubes", "bg_campus", "bg_jubes", "bg_pool"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][time_index]

                    self.MassageChart = ["neck", "shoulders", "calves", "feet", "neck", "shoulders", "calves", "feet", "pussy", "pussy"]

            self.OutfitChange(Changed=1) #assigns their default outfit, hopefully

        def Introduction(self): #rkeljs
                #things to add when girl is introduced
                if self == RogueX: #if self.name == "Rogue":?
                        self.Petname = "Sugar"
                        self.Petnames = ["Sugar",Player.name]
                        self.Pet = "Rogue"
                        self.Pets = ["Rogue"]
                elif self == KittyX:
                        self.Petname = Player.name[:1]
                        self.Petnames = ["sweetie",Player.name[:1],Player.name]
                        self.Pet = "Kitty"
                        self.Pets = ["Kitty"]
                elif self == EmmaX:
                        self.names = ["Ms. Frost"]
                        self.name = "Ms. Frost"
                        self.Petname = "young man"
                        self.Petnames = ["young man",Player.name]
                        self.Pet = EmmaX.name
                        self.Pets = ["Emma", "Ms. Frost"]
                elif self == LauraX:
                        self.Petname = "guy"
                        self.Petnames = ["guy",Player.name]
                        self.Pet = "Laura"
                        self.Pets = ["Laura", "X-23"]
                elif self.Tag == "Jean":
                        self.Petname = "um. . ."
                        self.Petnames = ["um. . ."]
                        self.Pet = JeanX.name
                        self.Pets = ["Jean"]
                elif self.Tag == "Storm":
                        self.Petname = "Player.name"
                        self.Petnames = ["Player.name"]
                        self.Pet = StormX.name
                        self.Pets = ["Storm", "Ororo", "Ms. Munroe"]
                elif self.Tag == "Jubes":
                        self.Petname = "Bro"
                        self.Petnames = ["Bro", "Player.name"]
                        self.Pet = JubesX.name
                        self.Pets = ["Jubes", "Jubilee"]

                self.OutfitChange(6,Changed=1) #assigns their default outfit, hopefully
                global all_Girls
                if self not in all_Girls:
                        all_Girls.append(self)                 #These are the girls you have met at all
                Shop_Inventory.extend(["DL", "G", "A"])     #adds these three items to the store for each girl added
                PersonalRooms.append(self.Home)

        def SluttyClothes(self):
                # called to check if loosened morals will lead to looser default outfits.
                # $ RogueX.SluttyClothes
                if self == RogueX:
                            if "stockings and garterbelt" in self.Inventory:
                                    self.Casual1[9] = "stockings and garterbelt"
                            elif self.inhibition >= 300: #Approvalcheck("Rogue", 300, "I"):
                                    self.Casual1[9] = "stockings"
                            else:
                                    self.Casual1[9] = "tights"

                            if self.Gym[0] == 0 and self.Gym[5] and self.inhibition >= 300:
                                    #removed hoodie if she's no longer shy
                                    self.Gym[3] == 0

                            if self.Swim[0] == 0 and self.Swim[5] and self.inhibition >= 300:
                                    #removed hoodie if she's no longer shy
                                    self.Swim[3] == 0
                elif self == KittyX:
                            if self.Swim[2] == "blue skirt" and self.Swim[6] and self.inhibition > 500:
                                    #removes blue skirt if she gets comfortable with it.
                                    self.Swim[2] = 0
                elif self == LauraX:
                            if self.inhibition >= 400 and self.Casual2[5] == "leather bra" and "corset" in self.Inventory:
                                    self.Casual2[5] = "corset"
                            if self.inhibition >= 600 and "lace panties" in self.Inventory:
                                    self.Casual2[6] = "lace panties"
                            if self.inhibition >= 600 and "stockings and garterbelt" in self.Inventory:
                                    self.Casual2[9] = "stockings and garterbelt"

                elif self == JeanX:
                            if "stockings and garterbelt" in self.Inventory:
                                    self.Casual1[9] = "stockings and garterbelt"
                            elif self.love >= 300: #Approvalcheck("Rogue", 300, "I"):
                                    self.Casual1[9] = "stockings"
                            if self.inhibition >= 600 and "bikini top" in self.Inventory:
                                    self.Gym[5] = "bikini top" if self.Gym[0] == 1 else self.Gym[5]
                            if self.inhibition >= 600 and "lace bra" in self.Inventory:
                                    self.Casual1[5] = "lace bra"
                                    self.Casual2[5] = "lace bra"
                            if self.inhibition >= 600 and "lace panties" in self.Inventory:
                                    self.Casual1[6] = "lace panties"
                                    self.Casual2[6] = "lace panties"
                elif self == StormX:
                            if self.inhibition >= 400 and self.Casual2[5] == "sports bra":
                                    self.Casual2[5] = "tube top"
                            if self.inhibition >= 400 and self.Casual2[5] == "white panties":
                                    self.Casual2[5] = "black panties"
                            if self.inhibition >= 600 and "lace panties" in self.Inventory:
                                    self.Casual2[6] = "lace panties"
                elif self == JubesX:
                            if self.inhibition >= 500 and self.Casual1[3] == "red shirt":
                                    self.Casual1[3] = "tube top"
                                    self.Casual1[5] = 0
                            if self.inhibition >= 600 and "lace panties" in self.Inventory:
                                    self.Casual2[6] = "lace panties"
                            if self.inhibition >= 600 and "stockings and garterbelt" in self.Inventory:
                                    self.Casual2[9] = "stockings and garterbelt"
                return

        def AddWord(self,Only=0,Recent=0,Daily=0,Trait=0,History=0):
                #applies variables to appropriate Girl stats
                # $ RogueX.AddWord(1,"angry", 0,0,0)
                #if Only, then only apply it if it's not already there
                if (Recent and not Only) or (Recent and Recent not in self.recent_history):
                        self.recent_history.append(Recent)
                if (Daily and not Only) or (Daily and Daily not in self.daily_history):
                        self.daily_history.append(Daily)
                if (Trait and not Only) or (Trait and Trait not in self.Traits):
                        self.Traits.append(Trait)
                if (History and not Only) or (History and History not in self.History):
                        self.History.append(History)
                return

        def DrainWord(self, Word = "word", Recent = 1, Daily = 1, Traits=0):
                # to remove words from the daily/recent lists ,
                # $ RogueX.DrainWord("angry", 0,1)
                if Recent and Word in self.recent_history:
                    while Word in self.recent_history:
                            self.recent_history.remove(Word)
                if Daily and Word in self.daily_history:
                    while Word in self.daily_history:
                            self.daily_history.remove(Word)
                if Traits and Word in self.Traits:
                    while Word in self.Traits:
                            self.Traits.remove(Word)
                return

        def change_stat(self, flavor, check, value, greater_than = False, alternates = {}, x_position = 0.75):
            if self.Tag in alternates.keys():
                check = alternates["check"]
                value = alternates["value"]

            if flavor in ["love", "obedience", "inhibition"]:
                check *= 10

            stat = getattr(self, flavor) #sets stat to the value referenced (ie if flavor is "love," stat becomes self.love's value)

            Overflow = self.Chat[4]
            x_position = self.sprite_location

            if self.Tag == "Jean" and flavor == "inhibition" and self.IX > 0:
                stat -= self.IX

            if greater_than:
                if stat >= check:
                    stat += value
                else:
                    value = 0
            else:
                if stat <= check:
                    stat += value
                else:
                    value = 0

            if self.Tag == "Jean" and flavor == "inhibition" and self.IX > 0:
                stat += self.IX

            if value:
                if self.Tag == "Jean" and value > 0:
                    if flavor == "obedience" and self.obedience <= 800 and check < 800:
                        value = int(value/2)
                        stat -= value
                    elif flavor == "inhibition" and self.IX > 0:
                        if self.Taboo >= 40:
                            value += value
                            stat += value
                        if stat > 1000:
                            self.IX -= (stat - 1000)
                            stat = 1000
                            value = 0
                        elif stat > 700:
                            self.IX -= int(value/2)

                        self.IX = 0 if self.IX < 0 else self.IX
                    elif flavor == "love" and stat >= 500 and self.obedience < 700:
                        if self.love < 500: #and stat > 500
                            self.love = 500
                            value = stat - 500

                        self.StatStore += value                                     #stores overflow amount for later

                        if check > self.obedience:
                            flavor = "obedience"                                     #sets the flavor to obed
                            value = int(value/5)                                #sets value change as 1/5th the amount
                            stat = self.obedience + value                            #establishes the new change as obedience+new value, likely 1
                        else:
                            value = 0

                if flavor == "love":
                    Color = "#c11b17"
                elif flavor == "obedience":
                    Color = "#2554c7"
                elif flavor == "inhibition":
                    Color = "#FFF380"
                elif flavor == "lust":
                    Color = "#FAAFBE"

                    CallHolder(value, Color, x_position) #show popup

                    if flavor == "lust" and stat >= 100 and not primary_action:
                        renpy.call("Girl_Cumming",self,1)

                        return

                    stat = 100 if stat > 100 else stat

                    setattr(self, flavor, stat)

                    return

                if stat > 1000:
                    CallHolder((-(stat-1000-value)), Color, x_position)
                    if not self.Chat[4]:
                        value = 0
                    else:
                        value = stat - 1000

                        setattr(self, flavor, 1000)

                        if flavor == "love":
                            if self.Chat[4] == 1:       #[love to obedience]
                                flavor = "obedience"
                            elif self.Chat[4] == 2:     #[love to Inhibition]
                                flavor = "inhibition"
                            else:
                                value = 0
                        elif flavor == "obedience":
                            if self.Chat[4] == 3:       #[obedience to Inhibition]
                                flavor = "inhibition"
                            elif self.Chat[4] == 4:
                                flavor = "love"   #[obedience to love]
                            else:
                                value = 0
                        elif flavor == "inhibition":
                            if self.Chat[4] == 5:       #[Inhibition to obedience]
                                flavor = "obedience"
                            elif self.Chat[4] == 6:
                                flavor = "love"    #[Inhibition to love]
                            else:
                                value = 0

                        stat = getattr(self, flavor)
                        stat += value

                        if flavor == "love":
                            Color = "#c11b17"
                        elif flavor == "obedience":
                            Color = "#2554c7"
                        elif flavor == "inhibition":
                            Color = "#FFF380"
                        else:
                            Color = "#FFFFFF"

                if value:
                    CallHolder(value, Color, x_position)

            stat = 1000 if stat > 1000 else stat

            setattr(self, flavor, stat)

            return

        def change_face(self, emotion = 5, B = 5, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
            emotion = self.emotion if emotion == 5 else emotion
            B = self.Blush if B == 5 else B

            if (self.Forced or "angry" in self.recent_history) and emotion in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                emotion = "angry"
            elif self.ForcedCount > 0 and emotion in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                emotion = "sad"

            if emotion == "normal":
                self.Mouth = "normal"
                self.Brows = "normal"
                self.Eyes = "normal"
            elif emotion == "angry":
                if self == LauraX:
                    self.Mouth = "kiss"
                else:
                    self.Mouth = "sad"
                self.Brows = "angry"
                self.Eyes = "sexy"
            elif emotion == "bemused":
                if self == EmmaX:
                    self.Mouth = "normal"
                else:
                    self.Mouth = "lipbite"
                self.Brows = "sad"
                self.Eyes = "squint"
            elif emotion == "closed":
                if self == RogueX:
                    self.Mouth = "lipbite"
                else:
                    self.Mouth = "normal"
                self.Brows = "sad"
                self.Eyes = "closed"
            elif emotion == "confused":
                self.Mouth = "kiss"
                self.Brows = "confused"
                if self == LauraX or self == EmmaX:
                    self.Eyes = "squint"
                else:
                    self.Eyes = "surprised"
            elif emotion == "kiss":
                self.Mouth = "kiss"
                if self == LauraX or self == EmmaX:
                    self.Brows = "sad"
                else:
                    self.Brows = "normal"
                self.Eyes = "closed"
            elif emotion == "sad":
                self.Mouth = "sad"
                self.Brows = "sad"
                if self == JeanX or self == JubesX:
                    self.Eyes = "normal"
                else:
                    self.Eyes = "sexy"
            elif emotion == "sadside":
                self.Mouth = "sad"
                self.Brows = "sad"
                self.Eyes = "side"
            elif emotion == "sexy":
                self.Mouth = "lipbite"
                if self == EmmaX:
                    self.Brows = "normal"
                    self.Eyes = "squint"
                elif self == LauraX:
                    self.Brows = "sad"
                    self.Eyes = "squint"
                else:
                    self.Brows = "normal"
                    self.Eyes = "sexy"
            elif emotion == "sly":
                self.Brows = "normal"
                self.Eyes = "squint"
                if self == RogueX:
                    self.Mouth = "grimace"
                if self == LauraX:
                    if LauraX.love >= 700:
                        self.Mouth = "smile"
                    else:
                        self.Mouth = "smirk"
                    self.Brows = "confused"
                elif self == KittyX:
                    self.Mouth = "smile"
                else:
                    self.Mouth = "smirk"
            elif emotion == "smile":
                if self == LauraX and LauraX.love < 700:
                    self.Mouth = "smirk"
                else:
                    self.Mouth = "smile"
                self.Brows = "normal"
                self.Eyes = "normal"
            elif emotion == "surprised":
                if self == RogueX or self == KittyX:
                    self.Mouth = "surprised"
                else:
                    self.Mouth = "kiss"
                self.Brows = "surprised"
                self.Eyes = "surprised"
            elif emotion == "oh":
                self.Mouth = "kiss"
                self.Brows = "surprised"
                self.Eyes = "surprised"
            elif emotion == "startled":
                if self == RogueX or self == KittyX:
                    self.Mouth = "grimace"
                else:
                    self.Mouth = "smile"
                self.Brows = "surprised"
                self.Eyes = "surprised"
            elif emotion == "down":
                if self == RogueX or self == KittyX:
                    self.Mouth = "surprised"
                else:
                    self.Mouth = "sad"
                self.Brows = "sad"
                self.Eyes = "down"
            elif emotion == "perplexed":
                if self == RogueX:
                    self.Mouth = "sad"
                    self.Brows = "confused"
                else:
                    self.Mouth = "smile"
                    self.Brows = "sad"
                if self == LauraX:
                    self.Eyes = "surprised"
                else:
                    self.Eyes = "normal"
            elif emotion == "sucking":
                self.Mouth = "sucking"
                if self == EmmaX:
                    self.Brows = "surprised"
                elif self == LauraX:
                    self.Brows = "sad"
                else:
                    self.Brows = "normal"
                self.Eyes = "closed"
            elif emotion == "tongue":
                self.Mouth = "tongue"
                self.Brows = "sad"
                if self == LauraX:
                    self.Eyes = "stunned"
                else:
                    self.Eyes = "sexy"
            elif emotion == "manic":
                if self == RogueX:
                    self.Mouth = "grimace"
                elif self == LauraX:
                    self.Mouth = "lipbite"
                else:
                    self.Mouth = "smile"
                self.Brows = "sad"
                self.Eyes = "manic"
                self.Blush = 1

            if M:
                self.Eyes = "manic"
            if B > 1:
                self.Blush = 2
            elif B:
                self.Blush = 1
            else:
                self.Blush = 0

            if Mouth:
                self.Mouth = Mouth
            if Eyes:
                self.Eyes = Eyes
            if Brows:
                self.Brows = Brows
            return

        def DefaultFaces(self):
                #This sets a default face for the girl
                #was "call Faces"
                # $ RogueX.DefaultFaces()
                if self.lust >= 50 and Approvalcheck(self, 1200):
                        self.emotion = "sexy"
                elif self.Addict > 75:
                        self.emotion = "manic"
                elif self.love >= self.obedience and self.love >= 500:
                        self.emotion = "smile"
                elif self.inhibition >= self.obedience and self.inhibition >= 500:
                        self.emotion = "smile"
                elif self.Addict > 50:
                        self.emotion = "manic"
                elif (self.love + self.obedience) < 300:
                        self.emotion = "angry"
                else:
                        self.emotion = "normal"
                return

        def lustFace(self,Extreme=0,Kissing=0):
                if self.Thirst >= 80:
                        self.lust += 2
                elif self.Thirst >= 50:
                        self.lust += 1

                if self.lust >= 80:
                        self.Blush = 2
                elif self.lust >= 40:
                        self.Blush = 1

                if self.lust >= 80:
                        self.Wet = 2
                elif self.lust >= 50:
                        self.Wet = 1

                if girl_offhand_action == "kiss both" or girl_offhand_action == "kiss girl":
                        #if the girls are kissing or all three are
                        Kissing = 1
                elif second_girl_primary_action == "kiss both" or girl_offhand_action == "kiss girl":
                        #if the girls are kissing or all three are
                        Kissing = 1
                elif Partner != self:
                        #If the called girl is kissing and is primary
                        if primary_action == "kiss" or offhand_action == "kiss":
                            Kissing = 1
                elif second_girl_primary_action == "kiss":
                        #If the called girl is kissing you in a threesome action
                        Kissing = 1

                if Kissing:
                        self.Eyes = "closed"
                        if self.Tag == "Emma":
                            self.Mouth = "kiss"
                        elif self.action_counter["kiss"] >= 10 and self.inhibition >= 300:
                            self.Mouth = "sucking"
                        elif self.action_counter["kiss"] > 1 and self.Addict >= 50:
                            self.Mouth = "sucking"
                        else:
                            self.Mouth = "kiss"
                else:
                        #If called girl is not kissing someone
                        if self.lust >= 90:
                                self.Eyes = "closed"
                                self.Brows = "sad"
                                self.Mouth = "surprised"
                        elif self.lust >= 70 or Extreme:
                                self.Eyes = "sexy"
                                self.Brows = "sad"
                                self.Mouth = "lipbite"
                        elif self.lust >= 50:
                                if self.Tag == "Emma" or self.Tag == "Laura":
                                        self.Eyes = "squint"
                                else:
                                        self.Eyes = "sexy"
                                self.Brows = "sad"
                                self.Mouth = "lipbite"
                        elif self.lust >= 30:
                                self.Eyes = "sexy"
                                self.Brows = "normal"
                                if self.Tag == "Emma" or self.Tag == "Laura":
                                        self.Mouth = "smirk"
                                else:
                                        self.Mouth = "kiss"
                        else:
                                self.Eyes = "sexy"
                                self.Brows = "normal"
                                if self.Tag == "Emma" or self.Tag == "Laura":
                                        self.Mouth = "smirk"
                                else:
                                        self.Mouth = "normal"
                        if self.Tag == "Laura" and self.lust < 50 and not Extreme and not Approvalcheck(self, 1000):
                                self.Eyes = "side"

                if Partner == self and second_girl_primary_action in ("eat_pussy", "eat_ass", "blowjob", "suck_breasts"):
                                self.Mouth = "tongue"
                elif girl_offhand_action in ("eat_pussy", "eat_ass", "suck_breasts"):
                                self.Mouth = "tongue"

                if self.OCount >= 10:
                        #If you've fucked her senseless
                        self.Eyes = "stunned"
                        self.Mouth = "tongue"

                if not self.Loose:
                        #if anal hurts. . .
                        if Partner != self and (primary_action == "anal" or primary_action == "dildo_anal" or girl_offhand_action == "dildo_anal"):
                            self.Eyes = "closed"
                            self.Brows = "angry"

                if "unseen" in self.recent_history:
                        self.Eyes = "closed"
                if Partner and self != Partner:
                        Partner.lustFace()
                return

        def OutfitChange(self, OutfitTemp = 5, Spunk = 0, Undressed = 0, Changed = 1,HolderOutfit=[]):
                # $ RogueX.OutfitChange("casual1")
                # OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed
                #OutfitTemp = self.Outfit if not OutfitTemp else OutfitTemp
                if self not in all_Girls: #should remove "Girl don't exist" errors
                        return

                OutfitTemp = OutfitTemp if OutfitTemp else self.Outfit

                if self.location == bg_current and renpy.showing("NightMask", layer='nightmask') and time_index == 0: #morning time
                        #Skips this check if it's a sleepover
                        return

                if self.location not in ("bg_showerroom", "bg_pool") or (OutfitTemp not in ("nude", "swimwear", "towel")):
                        #Dries her off
                        self.Water = 0
                if self.Spunk:
                        #Removes spunk if told to do so.
                        if "painted" not in self.daily_history or "cleaned" not in self.daily_history:
                            del self.Spunk[:]

                #Resets "half-dressed" states
                if self.Upskirt or self.Uptop or self.PantiesDown:
                        Undressed = 1

                self.Upskirt = 0
                self.Uptop = 0
                self.PantiesDown = 0

                if OutfitTemp == 5:
                        #this sets it to default if using AnyOutfit
                        if "yoinked" in self.recent_history:
                                #if Kitty's yoinked her clothes, don't replace them
                                return
                        OutfitTemp = self.Outfit
                elif OutfitTemp == 6:
                        #this sets it to daily default if using AnyOutfit
                        OutfitTemp = self.OutfitDay
                        self.Outfit = self.OutfitDay
                if OutfitTemp != self.Outfit:
                        #if her new outfit is not what she was wearing before,
                        #don't flag the undressed mechanic
                        Changed = 1
                        self.Outfit = OutfitTemp
                if self in Party and OutfitTemp == self.OutfitDay:
                        #this ignores her daily outfit if she's in a party
                        OutfitTemp = self.Outfit

                if OutfitTemp == "casual1":
                        HolderOutfit = self.Casual1[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "casual2":
                        HolderOutfit = self.Casual2[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "nude":
                        HolderOutfit = [0,0,0,0,0,0,0,0,0,0,50] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "towel":
                        HolderOutfit = [0,0,0, "towel", 0,0,0,0,0,0,35] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "custom1":
                        HolderOutfit = self.Custom1[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "custom2":
                        HolderOutfit = self.Custom2[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "custom3":
                        HolderOutfit = self.Custom3[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "temporary":
                        HolderOutfit = self.TempClothes[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "sleep":
                        HolderOutfit = self.Sleepwear[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "gym":
                        HolderOutfit = self.Gym[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "costume":
                        HolderOutfit = self.Costume[:] #fills Holder with the values of the sent uni. . .
                elif OutfitTemp == "swimwear":
                        if not self.Swim[0]:
                                if "bikini top" not in self.Inventory or "bikini bottoms" not in self.Inventory:
                                        self.Outfit = self.OutfitDay
                                        #if she doesn't own her swimsuit components. . .
                                        if "swim" not in self.daily_history:
                                                if self == RogueX:
                                                    ch_r("I don't really have any swimsuit I could wear. . .", interact=True)
                                                elif self == KittyX:
                                                    ch_k("I wish I had something cute to wear, but I don't. . .", interact=True)
                                                elif self == EmmaX:
                                                    ch_e("I really don't own the proper attire. . .", interact=True)
                                                elif self == LauraX:
                                                    ch_l("Don't have a suit. . .", interact=True)
                                                elif self == JeanX:
                                                    ch_j("I might, if you buy me a suit. . .", interact=True)
                                                elif self == StormX:
                                                    ch_s("I -am- afraid Charles would want me to wear a suit. . .", interact=True)
                                                elif self == JubesX:
                                                    ch_v("I haven't picked out a suit yet. . .", interact=True)
                                        return 0
                                elif self == KittyX and "blue skirt" not in self.Inventory and self.inhibition <= 400:
                                        self.Outfit = self.OutfitDay
                                        if "swim" not in self.daily_history:
                                                    ch_k("I don't know, I do have a suit, but it's a little daring. . .", interact=True)
                                                    ch_k("If only I had a little skirt or something. . .", interact=True)
                                        return 0
                                else:
                                    self.Swim[0] = 1
                        HolderOutfit = self.Swim[:] #fills Holder with the values of the sent uni. . .
                #end Holder setting. . .
                while len(HolderOutfit) < 11:
                    HolderOutfit.append(0)

                if not self.Legs and HolderOutfit[2]:
                    Undressed = 1
                elif not self.Over and HolderOutfit[3]:
                    Undressed = 1
                elif not self.Chest and HolderOutfit[5]:
                    Undressed = 1
                elif not self.Panties and HolderOutfit[6] and "pantyless" not in self.daily_history:
                    Undressed = 1
                elif not self.Hose and HolderOutfit[9]:
                    Undressed = 1

                #renpy.say(None, HolderOutfit[2], interact=True) #fix remove

                if self == EmmaX and (HolderOutfit[8] != "hat" and HolderOutfit[8] != "hat wet"):
                        #returns Emma's hair to default form if she's not deliberately wearing a hat
                        self.Hair = "wet" if HolderOutfit[8] == "hat wet" else "wave"

                self.Arms = HolderOutfit[1]
                self.Legs = HolderOutfit[2]
                self.Over = HolderOutfit[3]
                self.Neck = HolderOutfit[4]
                self.Chest = HolderOutfit[5]
                self.Panties = HolderOutfit[6]
                self.Acc = HolderOutfit[7]
                self.Hair = HolderOutfit[8] if HolderOutfit[8] else self.Hair
                self.Hose = HolderOutfit[9]
                self.Shame = HolderOutfit[10]

                if self.Legs in ["skirt", "dress"]:
                    self.wearing_skirt = True
                elif self == JubesX and self.Acc in ["slut jacket"]:
                    self.wearing_skirt = True
                elif self not in [EmmaX, StormX] and self.Over in ["towel"]:
                    self.wearing_skirt = True
                else:
                    self.wearing_skirt = False

                if "ripped" in self.daily_history and "modesty" not in self.recent_history:
                        #this keeps her in ripped hose all day if they are ripped off her
                        self.Hose = "ripped pantyhose" if self.Hose == "pantyhose" else self.Hose
                        self.Hose = "ripped tights" if self.Hose == "tights" else self.Hose
                if self.Panties and self.Panties != "shorts" and "pantyless" in self.daily_history and "modesty" not in self.daily_history:
                        # This checks the pantyless state from flirting
                        if OutfitTemp != "sleep" and OutfitTemp != "gym":
                                self.Panties = 0

                if not Changed and OutfitTemp == self.Outfit and self.location == bg_current:
                        #If she was partially dressed then it says she gets dressed
                        if Undressed == 2:
                                renpy.say(None,self.name+" throws on a towel.", interact=True)
                        elif Undressed:
                                renpy.say(None,self.name+" throws her clothes back on.", interact=True)
                if Undressed:
                    return 2
                return 1
                #End Outfits

        def Set_Temp_Outfit(self):
                    # This takes whatever the girl is wearing, and sets it as the temporary outfit
                    # $ RogueX.Set_Temp_Outfit()
                    self.TempClothes[1] = self.Arms
                    self.TempClothes[2] = self.Legs
                    self.TempClothes[3] = self.Over
                    self.TempClothes[4] = self.Neck
                    self.TempClothes[5] = self.Chest
                    self.TempClothes[6] = self.Panties
                    self.TempClothes[7] = self.Acc
                    self.TempClothes[8] = self.Hair
                    self.TempClothes[9] = self.Hose
                    self.TempClothes[0] = 1

                    #self.TempClothes = [1,self.Arms,self.Legs,self.Over,self.Neck,self.Chest,self.Panties,self.Acc,self.Hair,self.Hose,0]

                    self.Outfit = "temporary"
                    self.OutfitDay = "temporary"
                    return

        def ChestNum(self,Up=1):
                    #This function determines how much Bra are on, 5 for decent, less for less.
                    if Up and self.Uptop and self.Chest:
                        return 1
                    if self == RogueX:
                            if self.Chest in ("tank", "buttoned tank"):
                                return 5
                    if self == LauraX:
                            if self.Chest in ("leather bra", "white tank"):
                                return 5
                            elif self.Chest == "wolvie top":
                                return 3
                    if self == JeanX:
                            if self.Chest == "sports bra":
                                return 5
                    if self == StormX:
                            if self.Chest == "sports bra":
                                return 5
                    if self.Chest == "tube top":
                        return 5
                    if self.Chest == "lace bra":
                        return 2
                    if self.Chest == "lace corset":
                        return 2
                    if self.Chest == "corset":
                        return 5
                    if self.Chest:
                        return 3
                    if self.Acc == "suspenders" or self.Acc == "suspenders2":
                        return 2
                    #if it falls though. . .
                    return 0

        def OverNum(self,Up=1):
                    #This function determines how much Over are on, 5 for decent, less for less.
                    if Up and self.Uptop and self.Over:
                        return 1
                    if self == RogueX:
                            if self.Over == "mesh top":
                                return 2
                    if self == EmmaX:
                            if self.Over == "towel":
                                return 2
                    if self == StormX:
                            if self.Over == "towel":
                                return 0
                    if self == JubesX:
                            if Up and self.Uptop and self.Acc:
                                return 1
                            if self.Acc == "jacket":
                                return 3
                            if self.Acc == "open jacket":
                                return 1
                            if self.Acc == "shut jacket":
                                return 5
                    if self.Over == "towel":
                        return 3
                    if self.Over == "dress":
                        return 4
                    if self.Over == "jacket":
                        return 4
                    if self.Over == "nighty":
                        return 3
                    if self.Over == "pink top":
                        return 4
                    if self.Over:
                        return 5
                    #if it falls though. . .
                    return 0

        def PantsNum(self,Up=1):
                    #This function determines how much pants are on, 10 for pants, 6 for shorts, 5 for skirt, <5 for non-covering.
                    # Up defaults to 1 and returns 1 if in Upskirt mode, but will skip that check of Up is 0

                    if self == JubesX:
                            if self.Acc == "shut jacket":
                                return 5

                    if Up and self.Upskirt and self.Legs:
                                return 1

                    if self == RogueX and self.Panties == "shorts":
                                return 6
                    if self.Legs == "shorts":
                                return 6

                    if self.Legs == "yoga pants":
                                return 8

                    if self == EmmaX and self.Over == "dress":
                                return 4
                    if self.Legs == "mesh pants":
                                return 2
                    if self.Legs: #pants, mostly
                                return 10

                    #if it falls though. . .
                    return 0

        def PantiesNum(self,Up=1):
                    #This function determines how much panties are on, 5 for decent, less for less.
                    if Up and self.PantiesDown and self.Panties:
                        return 1
                    if self.Panties == "lace panties":
                        return 2
                    if self.Panties == "sports panties" or self.Panties == "shorts":
                        return 8
                    if self.Panties == "bikini bottoms":
                        return 7
                    if self.Panties:
                        return 4
                    return 0

        def HoseNum(self,Up=1):
                    #This function determines how seethrough her hose is, 5 for "visible," 10 for "solid"
                    if Up and self.Hose and (self.PantiesDown or self.Upskirt):
                        return 1
                    if self.Hose == "stockings":
                        return 1
                    if self.Hose == "pantyhose":
                        return 6
                    if self.Hose == "tights":
                        return 10
                    if self.Hose == "stockings and gaterbelt":
                        return 4
                    if self.Hose == "ripped pantyhose":
                        return 4
                    if self.Hose == "ripped tights":
                        return 4
                    #if it falls though. . .
                    return 0

        def Clothingcheck(self,C = 0):
                    C = 0
                    #This function counts how many items of clothing she has on and returns that number.
                    if self.OverNum() >= 5: #if her top is
                        C += 1
                    if self.Chest:
                        C += 1
                    if self.Legs:
                        C += 1
                    if self.HoseNum() >= 5: #double check this one. . .
                        C += 1
                    if self.Panties:
                        C += 1
                    return C

        def Modestycheck(self, check=0,C = 0):
                    C = 0
                    #This function determines whether they are partially nude or not.
                    #if check is 0, check both, if it's 1, check top, if it's 2, check bottom only
                    if check == 2:
                        pass    #skips if only checking bottoms
                    elif self.OverNum() >= 3: #if her top is fine
                        pass
                    elif self.ChestNum() >= 3:
                        pass
                    else:
                        C += 1

                    if check == 1:
                        pass    #skips if only checking tops
                    elif self.PantsNum() >= 5:
                        pass
                    elif self.PantiesNum() >= 4:
                        pass
                    elif self.HoseNum() >= 5:
                        pass
                    else:
                        C += 1
                    return C

        def Seencheck(self, check=0, C = 0):
                    C = 0
                    #This function returns 1-2 if she is partiallly naked and this is the first the player's seen of it.
                    # "check" is 1 if it's intended to see whether she has been seen at all.
                    # "check" is 2 if it's intended to see whether she has been seen topless.
                    # "check" is 3 if it's intended to see whether she has been seen bottomless.
                    if not self.SeenChest:
                        if (not self.Over and not self.Chest) or self.Uptop or check == 1 or check == 2:
                                    C += 1
                    if not self.SeenPussy:
                        if check == 1 or check == 3:
                                    C += 1
                        elif not self.Legs or self.Upskirt:
                            #if no pants or pants down
                            if self.PantiesDown or (self.HoseNum() < 5 and not self.Panties):
                                    # if no panties and loose hose or they're down
                                    C += 1
                    return C

        def GirlLikecheck(self,Girl=0):
                # RogueX.GirlLikecheck(KittyX) will return RogueX.LikeKitty, ie 600
                return getattr(self,"Like"+Girl.Tag)

        def GirlLikeUp(self,Girl=0,value=0,Like=0):
                # RogueX.GirlLikeUp(KittyX,5) will return RogueX.LikeKitty += 5
                if "Jeaned" in self.Traits:
                        #if Jean has messed with their stats, change the stored value instead
                        Like = getattr(JeanX,"LikeS"+self.Tag) #Like = RogueX.LikeKitty
                        if Like + value > 1000:
                                setattr(JeanX,"LikeS"+self.Tag, 1000)
                        elif Like + value < 0:
                                setattr(JeanX,"LikeS"+self.Tag, 0)
                        else:
                                setattr(JeanX,"LikeS"+self.Tag, value + Like) #RogueX.LikeKitty = RogueX.LikeKitty + value
                        return

                Like = getattr(self,"Like"+Girl.Tag) #Like = RogueX.LikeKitty
                if Like + value > 1000:
                        setattr(self,"Like"+Girl.Tag, 1000)
                elif Like + value < 0:
                        setattr(self,"Like"+Girl.Tag, 0)
                else:
                        setattr(self,"Like"+Girl.Tag, value + Like) #RogueX.LikeKitty = RogueX.LikeKitty + value
                return

        def GLG(self, GirlB = 0, check=200, Modifier = 1, Auto = 0, Jealousy = 0, Ok = 0, Likes=0):
                # self is the subject girl, GirlB is the object girl,
                # Modifier is sent as the amount of offense this might cause,
                # Jealousy is the temp value for how mad the girl will get
                # Likes stores the XLikesY stat temporarily
                # Auto quickly raises lust and like by a sent amount
                # returns 2 if very into it, 1 if ok with it, 0 if not cool with it.

                # was call GirlLikesGirl(Party[0],Party[1],700,5,1)
                # now $ RogueX.GLG(Party[1],700,5,1)
                if self not in all_Girls or GirlB not in all_Girls: #should remove "Girl don't exist" errors
                        return
                Jealousy = 0
                Likes = self.GirlLikecheck(GirlB)
                #stores this value temporarily

                if Likes <= check:
                        #if the checked girl likes the second girl less than the checked value. . .
                        if Auto:
                                #if set to auto, just raises the Like stat by the modifier value.
                                setattr(self,"Like"+GirlB.Tag,Likes+Modifier) #updates Like modifier
                                self.change_stat("lust", 200, (int(Modifier/5))) #raises lust by 1/5th modifier
                                return

                        # checks if they have agreed to share or not
                        if self in Player.Harem:
                                #if "dating" in RogueX.Traits or RogueX in Player.Harem:
                                if GirlB not in Player.Harem and "poly " + GirlB.Tag not in self.Traits:
                                        # if KittyX not in Player.Harem and "poly Kitty" not in RogueX.Traits:
                                        Jealousy = 100
                elif Auto: #this is a quick return,
                            self.change_stat("lust", 200, (int(Modifier/5))) #raises lust by 1/5th modifier
                            return

                #Establishes how jealous lead is likely to get
                Jealousy += (self.love - 600) if self.love > 600 else 0
                        #How much her love stat is over 600, +0-400
                Jealousy += self.SEXP if self.inhibition <= 500 else 0
                        #plus her SexP rating if she has low inhibitions, +0-200
                Jealousy -= (self.obedience - 250) if self.obedience > 250 else 0
                        #minus how much her obedience stat is over 250, -0-750
                        # = result of up to 700 if high love, dating, and low obedience

                Jealousy = 0 if Jealousy < 1 else Jealousy
                    #Balances it to no less than zero
                Modifier += 1 if not Jealousy and Likes >= 500 else 0
                    #+ modifier if she doesn't hate Kitty but has no jealousy left


                if Likes >= 900:
                            #If she really likes the girl, then she is turned on, likes both of you more.
                            Likes += Modifier
                            self.change_stat("love", 80, (int(Modifier/2))) #raises love by 1/2 modifier
                            self.change_stat("lust", 200, (int(Modifier/5))) #raises lust by 1/5 modifier
                            Ok = 2
                elif Likes >= 800:
                        #If she mostly likes the girl, and is not super jealous, she likes you both more.
                        if Jealousy <= 300:
                            Likes += Modifier
                            self.change_stat("love", 80, (int(Modifier/2))) #raises love by 1/2 modifier
                            self.change_stat("lust", 200, (int(Modifier/2))) #raises lust by 1/2 modifier
                            Ok = 2
                        else:
                            Likes -= Modifier
                            self.change_stat("lust", 200, (int(Modifier/5))) #raises lust by 1/5 modifier
                            Ok = 1
                elif Likes >= 600:
                        #If she's friends with the girl, only low jealousy is positive
                        if Jealousy <= 100:
                            Likes += Modifier
                            self.change_stat("love", 80, (int(Modifier/4))) #raises love by 1/4 modifier
                            self.change_stat("lust", 200, (int(Modifier/2))) #raises lust by 1/2 modifier
                            Ok = 2
                        elif Jealousy <= 300:
                            Likes -= Modifier
                            self.change_stat("lust", 200, (int(Modifier/2))) #raises lust by 1/5 modifier
                            Ok = 1
                        else:
                            Likes -= (Modifier + (int(Jealousy/50)))
                            self.change_stat("love", 90, (-(int(Modifier)))) #lowers love by 1/2 modifier
                            self.change_stat("lust", 200, (int(Modifier/5))) #raises lust by 1/5 modifier
                            Ok = 2
                elif Likes >= 400:
                        #If she is neutral to the girl, it's all negative
                        if Jealousy <= 100:
                            Likes -= Modifier
                            Ok = 1
                        else:
                            Likes -= (Modifier + (int(Jealousy/100)))
                        self.change_stat("lust", 200, (int(Modifier/10))) #raises lust by 1/10 modifier
                else:
                        #If she hates the girl, it's all very negative
                        Likes -= (Modifier + (int(Jealousy/50)))
                        self.change_stat("lust", 200, (int(Modifier/10))) #raises lust by 1/5 modifier
                self.change_stat("inhibition", 60, (int(Modifier/10))) #raises inhibition by 1/10 modifier

                # restores "likes" to target Girl.

                setattr(self,"Like"+GirlB.Tag,Likes+Modifier) #updates Like modifier

                return Ok
                # returns 2 if very into it, 1 if ok with it, 0 if not cool with it.

        def Namecheck(self, counter = 0): #rkeljs
                #checks how she reacts to you using her petname
                #counter and Ugh are internal count variable
                # $ RogueX.namecheck() #nee
                if self.Pet == self.name:
                        return 0
                if self.Taboo:
                        # +4 if Taboo 40, +2 if Taboo 20
                        counter = int(self.Taboo/10)

                #easy options
                if self.Pet in ("girl", "boo", "bae", "baby", "sweetie"):
                    if Approvalcheck(self, 500, "L", TabM=1,Alt=[[LauraX],600]):
                        self.change_stat("love", 80, 1)
                    else:
                        self.change_stat("love", 50, -1)
                        return 1
                elif self.Pet in ("sexy", "lover", "beloved"):
                    if Approvalcheck(self, 900, TabM=1,Alt=[[LauraX],1100]):
                        self.change_stat("love", 80, 2)
                        self.change_stat("obedience", 80, 1)
                        self.change_stat("inhibition", 70, 1)
                    else:
                        self.change_stat("love", 50, (-1-counter))
                        self.change_stat("obedience", 50, 1)
                        self.change_stat("inhibition", 20, -1)
                        return 1
                #tougher options
                elif self.Pet == "slave":
                        if Approvalcheck(self, 800, "O", TabM=3,Alt=[[EmmaX,StormX],900]):
                            self.change_stat("lust", 90, (3+counter))
                            self.change_stat("obedience", 95, (2+counter))
                            self.change_stat("inhibition", 30, 1)
                            self.change_stat("inhibition", 70, 1)
                        elif Approvalcheck(self, 500, "O", TabM=3,Alt=[[EmmaX,StormX],600]):
                            self.change_stat("lust", 90, 1)
                            self.change_stat("love", 200, -1)
                            self.change_stat("obedience", 80, 2)
                            self.change_stat("inhibition", 70, 1)
                        else:
                            self.change_stat("love", 200, -2)
                            self.change_stat("love", 50, -1, 1)
                            self.change_stat("obedience", 50, 1)
                            self.change_stat("inhibition", 50, -1)
                            return 1
                elif self.Pet == "pet":
                        if Approvalcheck(self, 1500, TabM=2,Alt=[[LauraX],800]):
                            self.change_stat("lust", 90, (3+counter))
                            self.change_stat("obedience", 95, (2+counter))
                            self.change_stat("inhibition", 30, 1)
                            self.change_stat("inhibition", 70, 1)
                        elif Approvalcheck(self, 1200, TabM=2,Alt=[[LauraX],650]):
                            self.change_stat("lust", 60, 1)
                            self.change_stat("obedience", 80, 2)
                            self.change_stat("inhibition", 70, 1)
                        else:
                            self.change_stat("love", 200, -2)
                            self.change_stat("love", 50, -1, 1)
                            self.change_stat("obedience", 50, 1)
                            self.change_stat("inhibition", 50, -1)
                            return 1
                elif self.Pet == "slut":
                        if Approvalcheck(self, 500, "O", TabM=2) or Approvalcheck(self, 500, "I", TabM=2,Alt=[[LauraX],400]):
                            self.change_stat("lust", 90, (4+counter))
                            self.change_stat("obedience", 95, (2+counter))
                            self.change_stat("inhibition", 40, 2)
                            self.change_stat("inhibition", 80, 1)
                        elif Approvalcheck(self, 300, "O", TabM=2) or Approvalcheck(self, 300, "I", TabM=2,Alt=[[LauraX],200]):
                            self.change_stat("lust", 90, 1)
                            self.change_stat("love", 200, (-1-counter))
                            self.change_stat("obedience", 80, (2+counter))
                            self.change_stat("inhibition", 70, 1)
                        else:
                            self.change_stat("love", 200, (-2-counter))
                            self.change_stat("love", 50, (-1-counter), 1)
                            self.change_stat("obedience", 50, 1)
                            self.change_stat("inhibition", 20, -1)
                            return 1
                elif self.Pet == "whore":
                        if Approvalcheck(self, 600, "O", TabM=2,Alt=[[EmmaX],700]) or Approvalcheck(self, 600, "I", TabM=2,Alt=[[LauraX],400]):
                            self.change_stat("lust", 90, 4)
                            self.change_stat("obedience", 95, 2)
                            self.change_stat("inhibition", 50, 2)
                            self.change_stat("inhibition", 80, 1)
                        elif Approvalcheck(self, 400, "O", TabM=2,Alt=[[EmmaX],500]) or Approvalcheck(self, 400, "I", TabM=2):
                            self.change_stat("lust", 90, 1)
                            self.change_stat("love", 200, (-2-counter))
                            self.change_stat("obedience", 80, 2)
                            self.change_stat("inhibition", 70, 1)
                        else:
                            self.change_stat("love", 200, (-3-counter))
                            self.change_stat("love", 50, (-2-counter), 1)
                            self.change_stat("obedience", 50, 1)
                            self.change_stat("inhibition", 21, 1, 1)
                            self.change_stat("inhibition", 20, -1)
                            return 1
                elif self.Pet == "sugartits":
                        if Approvalcheck(self, 1500, TabM=1,Alt=[[EmmaX],1300]):
                            self.change_stat("obedience", 80, 1)
                            self.change_stat("obedience", 50, 2)
                            self.change_stat("inhibition", 70, 1, alternates = {"Emma": {"check": 70, "value": 2}})
                            self.change_stat("inhibition", 30, 2, alternates = {"Storm": {"check": 60, "value": 3}})
                        else:
                            self.change_stat("love", 200, (-2-counter))
                            self.change_stat("love", 50, (-1-counter))
                            self.change_stat("obedience", 50, 1)
                            self.change_stat("inhibition", 20, -1)
                            return 1
                elif self.Pet == "sex friend":
                        if Approvalcheck(self, 750, "O", TabM=1) or Approvalcheck(self, 600, "I", TabM=1):
                            self.change_stat("lust", 90, 3)
                            self.change_stat("obedience", 95, 2)
                            self.change_stat("inhibition", 40, 2)
                            self.change_stat("inhibition", 80, 1)
                        elif Approvalcheck(self, 600, "O", TabM=1) or Approvalcheck(self, 400, "I", TabM=1):
                            self.change_stat("lust", 90, 2)
                            self.change_stat("love", 200, (-1-counter))
                            self.change_stat("obedience", 80, 1)
                            self.change_stat("inhibition", 70, 1)
                            self.Blush = 1
                        else:
                            self.change_stat("love", 200, -counter)
                            self.change_stat("love", 50, (-1-counter), 1)
                            self.change_stat("obedience", 50, 1)
                            self.change_stat("inhibition", 20, -1)
                            return 1
                elif self.Pet == "fuckbuddy":
                        if Approvalcheck(self, 700, "O", TabM=2) or Approvalcheck(self, 700, "I", TabM=1):
                            self.change_stat("lust", 90, 3)
                            self.change_stat("obedience", 95, 2)
                            self.change_stat("inhibition", 40, 2)
                            self.change_stat("inhibition", 85, 1)
                        elif Approvalcheck(self, 600, "O", TabM=2) or Approvalcheck(self, 500, "I", TabM=1):
                            self.change_stat("lust", 90, 2)
                            self.change_stat("love", 200, (-1-counter))
                            self.change_stat("obedience", 80, 1)
                            self.change_stat("inhibition", 70, 1)
                            self.Blush = 1
                        else:
                            self.change_stat("love", 200, -counter)
                            self.change_stat("love", 60, (-2-counter), 1)
                            self.change_stat("obedience", 60, 1)
                            self.change_stat("inhibition", 20, -1)
                            return 1
                elif self.Pet in ("baby girl", "mommy"):
                        if Approvalcheck(self, 1200, TabM=1):
                            self.change_stat("obedience", 80, 1)
                            self.change_stat("obedience", 50, 2)
                            self.change_stat("inhibition", 70, 1)
                            self.change_stat("inhibition", 30, 2)
                        else:
                            self.change_stat("love", 200, (-2-counter))
                            self.change_stat("love", 50, (-1-counter))
                            self.change_stat("obedience", 50, 1)
                            self.change_stat("inhibition", 20, -1)
                            return 1
                #Rogue
                elif self.Pet == "chere":
                        if Approvalcheck(self, 600, "L", TabM=1):
                            self.change_stat("love", 80, 2)
                        else:
                            self.change_stat("love", 50, -1)
                            return 1
                #Kitty
                elif self.Pet == "kitten":
                        if Approvalcheck(self, 600, "L", TabM=1):
                            self.change_stat("love", 80, 2)
                        else:
                            self.change_stat("love", 50, -1)
                            return 1
                #Emma
                elif self.Pet == "darling":
                        if Approvalcheck(self, 600, "L", TabM=1):
                            self.change_stat("love", 80, 2)
                        else:
                            self.change_stat("love", 50, -1)
                            return 1
                #Laura
                elif self.Pet == "Wolvie":
                        if Approvalcheck(self, 500, "I", TabM=1):
                            self.change_stat("love", 80, 1)
                        else:
                            self.change_stat("love", 50, -1)
                            return 1
                elif self.Pet == "X-23":
                        if Approvalcheck(self, 800, "O"):
                            self.change_stat("lust", 90, 3)
                            self.change_stat("love", 90, -1)
                            self.change_stat("obedience", 95, 2)
                        elif Approvalcheck(self, 700, "L") and not Approvalcheck(self, 500, "O"):
                            self.change_stat("love", 200, -2)
                            self.change_stat("love", 50, -1, 1)
                            self.change_stat("obedience", 30, 2)
                            self.change_stat("obedience", 50, 2)
                            self.change_stat("inhibition", 50, -1)
                            return 1
                return 0

label EmotionEditor(Girl=0):
        # call EmotionEditor(RogueX)
        while True:
            menu:
                "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":
                    menu:
                        "Normal":
                            $ Girl.emotion = "normal"
                        "Angry":
                            $ Girl.emotion = "angry"
                        "Smiling":
                            $ Girl.emotion = "smile"
                        "Sexy":
                            $ Girl.emotion = "sexy"
                        "Suprised":
                            $ Girl.emotion = "surprised"
                        "Bemused":
                            $ Girl.emotion = "bemused"
                        "Manic":
                            $ Girl.emotion = "manic"

                "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":
                    menu:
                        "Sad":
                            $ Girl.emotion = "sad"
                        "Sucking":
                            $ Girl.emotion = "sucking"
                        "kiss":
                            $ Girl.emotion = "kiss"
                        "Tongue":
                            $ Girl.emotion = "tongue"
                        "confused":
                            $ Girl.emotion = "confused"
                        "Closed":
                            $ Girl.emotion = "closed"
                        "Down":
                            $ Girl.emotion = "down"

                "Emotions3: Sadside Startled Perplexed Sly":
                    menu:
                        "Sadside":
                            $ Girl.emotion = "sadside"
                        "Startled":
                            $ Girl.emotion = "startled"
                        "Perplexed":
                            $ Girl.emotion = "perplexed"
                        "Sly":
                            $ Girl.emotion = "sly"
                    #$ Girl.change_face
                "Toggle Mouth Spunk":
                    if "mouth" in Girl.Spunk:
                        $ Girl.Spunk.remove("mouth")
                    else:
                        $ Girl.Spunk.append("mouth")
                "Toggle hand Spunk":
                    if "handjob" in Girl.Spunk:
                        $ Girl.Spunk.remove("handjob")
                    else:
                        $ Girl.Spunk.append("handjob")

                "Toggle Facial Spunk":
                    if "facial" in Girl.Spunk and "hair" not in Girl.Spunk:
                        $ Girl.Spunk.append("hair")
                    elif "facial" in Girl.Spunk:
                        $ Girl.Spunk.remove("facial")
                        $ Girl.Spunk.remove("hair")
                    else:
                        $ Girl.Spunk.append("facial")

                "Blush":
                    if Girl.Blush == 2:
                        $ Girl.Blush = 0
                    elif Girl.Blush:
                        $ Girl.Blush = 2
                    else:
                        $ Girl.Blush = 1
                "Exit.":
                    return
            $ Girl.change_face() #applies change
        #end Emotion Editor

label GirlsAngry(Girls = 0,other_Girls=[]): #rkeljsv
        # Causes girls to storm off if you've pissed them off.
        $ temp_modifier = 0
        $ other_Girls = all_Girls[:]
        while other_Girls:
                if other_Girls[0].location == bg_current and "angry" in other_Girls[0].recent_history:
                        if bg_current == other_Girls[0].Home:
                                if other_Girls[0] == RogueX:
                                        ch_r "You should get out, I'm fix'in ta throw down."
                                elif other_Girls[0] == KittyX:
                                        ch_k "You should get out of here, I can't even look at you right now."
                                elif other_Girls[0] == EmmaX:
                                        ch_e "You should leave, or do you want to test me?"
                                elif other_Girls[0] == LauraX:
                                        ch_l "You should leave."
                                elif other_Girls[0] == JeanX:
                                        ch_j "Out, NOW!"
                                elif other_Girls[0] == StormX:
                                        ch_s "Out!"
                                elif other_Girls[0] == JubesX:
                                        ch_v "Get out!"
                                "You head back to your room."
                                $ Party = []
                                $ renpy.pop_call()
                                jump player_room_entry
                        else:
                                $ other_Girls[0].location = other_Girls[0].Home
                        if other_Girls[0] in Party:
                                $ Party.remove(other_Girls[0])
                        if Girls:
                            ". . . and so does [other_Girls[0].name]."
                        else:
                            "[other_Girls[0].name] storms off."
                            if other_Girls[0] == StormX:
                                    ". . . so to speak."
                        $ Girls += 1
                        if other_Girls[0] == RogueX:
                                hide Rogue_Sprite with easeoutleft
                        elif other_Girls[0] == KittyX:
                                hide Kitty_Sprite with easeoutleft
                        elif other_Girls[0] == EmmaX:
                                hide Emma_Sprite with easeoutleft
                        elif other_Girls[0] == LauraX:
                                hide Laura_Sprite with easeoutleft
                        elif other_Girls[0] == JeanX:
                                hide Jean_Sprite with easeoutleft
                        elif other_Girls[0] == StormX:
                                hide Storm_Sprite with easeoutleft
                        elif other_Girls[0] == JubesX:
                                hide Jubes_Sprite with easeoutleft
                $ other_Girls.remove(other_Girls[0])
        return


label LastNamer(Wordcount = 0, Splitname = 0, Lastname = 0):
        # Wordcount = number of words
        $ Wordcount = Player.name.count(" ")

        # Splitname turns the name into a list, ie [Charles, Francis, Xavier]
        $ Splitname = Player.name.split()

        # Lastname picks the last word in that set
        $ Lastname = "Mr. " + Splitname[Wordcount]
        return Lastname

label DrainAll(Word=0,Recent=1,Daily=1,Traits=0):
        # called to remove words from all girls in the game.
        # call DrainAll("arriving")
        $ Girls = all_Girls[:]
        while Girls:
            $ Girls[0].DrainWord(Word,Recent,Daily,Traits)
            $ Girls.remove(Girls[0])
        return
