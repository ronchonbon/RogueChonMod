init python:

    class PlayerClass(object):
        def __init__(self):
            self.Name = "Zero"
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
            self.RecentActions = []
            self.DailyActions = []
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

            self.focused_girl = None
            self.primary_action = None
            self.offhand_action = None

        def AddWord(self, Only = 0, Recent = 0, Daily = 0, Trait = 0, History = 0):
            if (Recent and not Only) or (Recent and Recent not in self.RecentActions):
                self.RecentActions.append(Recent)
            if (Daily and not Only) or (Daily and Daily not in self.DailyActions):
                self.DailyActions.append(Daily)
            if (Trait and not Only) or (Trait and Trait not in self.Traits):
                self.Traits.append(Trait)
            if (History and not Only) or (History and History not in self.History):
                self.History.append(History)
            return

        def DrainWord(self, Word, Recent = 1, Daily = 1, Traits = 0):
            if Recent and Word in self.RecentActions:
                while Word in self.RecentActions:
                    self.RecentActions.remove(Word)
            if Daily and Word in self.DailyActions:
                while Word in self.DailyActions:
                    self.DailyActions.remove(Word)
            if Traits and Word in self.Traits:
                while Word in self.Traits:
                    self.Traits.remove(Word)
            return

        def Statup(self, Flavor, Check = 100, Value = 1, Greater = 0, XPOS = 0.75):

            Type = getattr(self,Flavor)

            if Greater:
                if Type >= Check:
                    Type += Value
                else:
                    Value = 0
            else:
                if Type <= Check:
                    Type += Value
                else:
                    Value = 0

            if Value:
                CallHolder(Value, "#FFFFFF", XPOS)

            Type = 100 if Type > 100 else Type

            setattr(self, Flavor, Type)

            return

    class GirlClass(object):
        def __init__(self,Name="no name",Love=0,Obed=0,Inbt=0,Lust=0):
            self.Name = Name        #changable by player, used in dialog
            self.Tag = Name         #Permanent label, used in code
            self.Names = [Name]     #this is a list of primary names you're allowed to use
            self.voice = None
            self.Love = Love
            self.Obed = Obed
            self.Inbt = Inbt
            self.Lust = Lust
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
            self.RecentActions = []
            self.DailyActions = []
            self.Traits = []
            self.History = []
            self.Date = 0                           #how many dates you've been on
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
            self.Loc = "hold"       #Where she is right now
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
            self.Emote = "normal"
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
            self.Schedule = [["MM","MA","ME","MN"],
                            ["TM","TA","TE","TN"],
                            ["WM","WA","WE","WN"],
                            ["ThM","ThA","ThE","ThN"],
                            ["FM","FA","FE","FN"],
                            ["SaM","SaA","SaE","SaN"],
                            ["SuM","SuA","SuE","SuN"],
                            ] #Schedule[0-6][0-4] = Schedule[Day][Time]
            self.Clothing = [0,0,0,0,0,0,0,0,0,0]                      #schedules when she wears what: (0-6) = Mon-Sun, (7) Datewear, (8) Teachingwear, (9) Private

            self.Org = 0                    #lifetime orgasms
            self.OCount = 0                 #orgasms per encounter
            self.Caught = 0
            self.Kissed = 0                 #How many times they've kissed
            self.Sleep = 0                  #How many times they've slept over
            self.Hand = 0
            self.Foot = 0
            self.Slap = 0
            self.Strip = 0
            self.Tit = 0
            self.Sex = 0
            self.Anal = 0
            self.Loose = 0
            self.Hotdog = 0
            self.Mast = 0
            self.Massage = 0
            self.FondleB = 0
            self.FondleT = 0
            self.FondleP = 0
            self.FondleA = 0
            self.DildoP = 0
            self.DildoA = 0
            self.Vib = 0
            self.Plug = 0
            self.SuckB = 0
            self.InsertP = 0
            self.InsertA = 0
            self.LickP = 0
            self.LickA = 0
            self.Blow = 0
            self.Swallow = 0
            self.CreamP = 0
            self.CreamA = 0
            self.Les = 0                                    #how many times she's done les stuff
            self.LesWatch = 0                               #how many times you've watched her lesing
            self.SEXP = 0
            self.MassageChart = [0,0,0,0,0,0,0,0,0,0]
            self.PlayerFav = 0                              #you favorite activity with her
            self.Favorite = 0                               #her favorite activity

            if self.Tag == "Rogue":
                    self.narrator = ch_r

                    self.Casual1 = [2,"gloves","skirt","mesh top","spiked collar","tank","black panties",0,0,"tights",0]
                    self.Casual2 = [2,"gloves","pants","pink top",0,"buttoned tank","black panties",0,0,0,0]
                    self.Gym = [0,"gloves",0,"hoodie",0,"sports bra","shorts",0,0,0,10]
                    self.Sleepwear = [0,0,0,0,0,"tank","green panties",0,0,0,20]
                    self.Swim = [0,0,0,"hoodie",0,"bikini top","bikini bottoms",0,0,0,0]
                    self.Costume = [2,"gloves","skirt",0,0,"tube top","black panties","sweater","cosplay",0,0]

                    self.Home = "bg rogue"
                    self.Hair = "evo"
                    self.LikeKitty = 600
                    self.LikeEmma = 500
                    self.LikeLaura = 500
                    self.Schedule = [["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                    ["bg classroom","bg dangerroom","bg rogue","bg rogue"],
                                    ["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                    ["bg classroom","bg dangerroom","bg rogue","bg rogue"],
                                    ["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                    ["bg dangerroom","bg pool","bg rogue","bg rogue"],
                                    ["bg dangerroom","bg pool","bg rogue","bg rogue"]] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                    self.SexKitty = 0
                    self.SexEmma = 0
                    self.SexLaura = 0

                    self.History = ["met"]

                    self.MassageChart = ["shoulders","arms","arms","hands","hands","back","hips","back","breasts","breasts"]
            elif self.Tag == "Kitty":
                    self.narrator = ch_k

                    self.Casual1 = [2,0,"capris","pink top","gold necklace","cami","green panties",0,0,0,0]
                    self.Casual2 = [2,0,"black jeans","red shirt","star necklace","bra","green panties",0,0,0,0]
                    self.Gym = [0,0,"shorts",0,0,"sports bra","green panties",0,0,0,10]
                    self.Sleepwear = [0,0,"shorts",0,0,"cami","green panties",0,0,0,20]
                    self.Swim = [0,0,"blue skirt",0,0,"bikini top","bikini bottoms",0,0,0,0]
                    self.Costume = [2,0,"dress","jacket","flower necklace","dress","lace panties",0,0,0,0]

                    self.Home = "bg kitty"
                    self.Hair = "evo"
                    self.LikeRogue = 600
                    self.LikeEmma = 500
                    self.LikeLaura = 500
                    self.like = ", like, "
                    self.Like = "Like, "
                    self.Schedule = [["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                    ["bg classroom","bg pool","bg kitty","bg kitty"],
                                    ["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                    ["bg classroom","bg pool","bg kitty","bg kitty"],
                                    ["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                    ["bg campus","bg dangerroom","bg kitty","bg kitty"],
                                    ["bg campus","bg dangerroom","bg kitty","bg kitty"]] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                    self.SexRogue = 0
                    self.SexEmma = 0
                    self.SexLaura = 0

                    self.MassageChart = ["shoulders","back","hips","thighs","calves","feet","feet","hips","ass","pussy"]
            elif self.Tag == "Emma":
                    self.voice = ch_e

                    self.Casual1 = [2,0,"pants","jacket","choker","corset","white panties",0,0,0,0]
                    self.Casual2 = [2,"gloves","pants",0,"choker","corset","white panties",0,0,0,5]
                    self.Gym = [0,0,0,0,0,"sports bra","sports panties",0,0,0,10]
                    self.Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0,25]
                    self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    self.Costume =  [2,"gloves","dress","dress","choker",0,"lace panties",0,"hat","stockings and garterbelt",0]
                    self.Home = "bg emma"
                    self.Hair = "wavy"
                    self.Pubes = 0
                    self.LikeRogue = 500
                    self.LikeKitty = 500
                    self.LikeLaura = 500
                    self.Schedule = [["bg teacher","bg teacher","bg classroom","bg emma"],
                                    ["bg teacher","bg teacher","bg dangerroom","bg emma"],
                                    ["bg teacher","bg teacher","bg classroom","bg emma"],
                                    ["bg teacher","bg teacher","bg dangerroom","bg emma"],
                                    ["bg teacher","bg teacher","bg classroom","bg emma"],
                                    ["bg pool","bg pool","bg emma","bg emma"],
                                    ["bg pool","bg pool","bg emma","bg emma"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]
                    self.SexRogue = 0
                    self.SexKitty = 0
                    self.SexLaura = 0
                    self.Loose = 2
                    self.MassageChart = ["shoulders","neck","neck","back","hips","ass","ass","back","breasts","breasts"]

            elif self.Tag == "Laura":
                    self.voice = ch_l

                    self.Casual1 = [2,"wrists","leather pants",0,"leash choker","leather bra","black panties",0,0,0,0]
                    self.Casual2 = [2,0,"skirt","jacket","leash choker","leather bra","black panties",0,0,0,0]
                    self.Gym = [2,"wrists","leather pants",0,0,"leather bra","black panties",0,0,0,0]
                    self.Sleepwear = [0,0,0,0,0,"leather bra","leather panties",0,0,0,20]
                    self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    self.Costume = [2,"gloves","other skirt",0,0,"white tank","black panties","suspenders",0,"black stockings",0]
                    self.Home = "bg laura"
                    self.Hair = "long"
                    self.LikeRogue = 500
                    self.LikeKitty = 500
                    self.LikeEmma = 500
                    self.ScentTimer = 0 #this timer gives you X seconds of watching Laura before she notices you there
                    self.Claws = 0
                    self.Schedule = [["bg pool","bg classroom","bg dangerroom","bg laura"],
                                    ["bg dangerroom","bg classroom","bg campus","bg laura"],
                                    ["bg pool","bg classroom","bg dangerroom","bg laura"],
                                    ["bg dangerroom","bg classroom","bg campus","bg laura"],
                                    ["bg pool","bg classroom","bg dangerroom","bg laura"],
                                    ["bg pool","bg laura","bg dangerroom","bg laura"],
                                    ["bg pool","bg laura","bg dangerroom","bg laura"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]
                    self.SexRogue = 0
                    self.SexKitty = 0
                    self.SexEmma = 0
                    self.Loose = 2
                    self.MassageChart = ["shoulders","back","arms","hips","thighs","calves","ass","ass","pussy","pussy"]

            elif self.Tag == "Jean":
                    self.voice = ch_j

                    # JeanX = GirlClass("Jean",200,0,1000,10) #Inbt falls to 800
                    self.StatStore = 0      #this stores Love stat above 500 and distributes it later.
                    self.IX = 500           #this is an amount subtracted from her Inbt in most checks, and reduces over time

                    self.Casual1 = [2,0,"pants","pink shirt",0,"green bra","green panties",0,0,0,0]
                    self.Casual2 = [2,0,"skirt","green shirt",0,"green bra","green panties",0,0,0,0]
                    self.Gym = [0,0,"yoga pants",0,0,"sports bra","green panties",0,0,0,0]
                    self.Sleepwear = [0,0,0,"pink shirt",0,"green bra","green panties",0,0,0,0]
                    self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    self.Costume =  [2,0,"shorts","yellow shirt",0,"green bra","green panties","suspenders","pony",0,0]
                    self.Home = "bg jean"
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

                    self.Schedule = [["bg classroom","bg classroom","bg dangerroom","bg jean"],
                                    ["bg jean","bg classroom","bg jean","bg jean"],
                                    ["bg jean","bg classroom","bg dangerroom","bg jean"],
                                    ["bg classroom","bg classroom","bg jean","bg jean"],
                                    ["bg jean","bg classroom","bg dangerroom","bg jean"],
                                    ["bg dangerroom","bg campus","bg pool","bg jean"],
                                    ["bg dangerroom","bg campus","bg pool","bg jean"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                    self.MassageChart = ["back","shoulders","neck","neck","back","hips","ass","ass","pussy","pussy"]

            elif self.Tag == "Storm":
                    self.voice = ch_s

                    self.Casual1 = [2,0,"skirt","white shirt",0,"black bra","white panties",0,0,0,0]
                    self.Casual2 = [2,0,"pants","jacket",0,"sports bra","white panties",0,0,0,0]
                    self.Gym = [0,0,"yoga pants",0,0,"sports bra","white panties",0,0,0,10]
                    self.Sleepwear = [0,0,0,"white shirt",0,0,"white panties",0,0,0,25]
                    self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    self.Costume = [2,0,0,0,"ring necklace","cos bra","cos panties","rings","short",0,0]
                    self.Home = "bg storm"
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

                    #fills in existing characters
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

                    self.Schedule = [["bg storm","bg dangerroom","bg dangerroom","bg storm"],
                                    ["bg teacher","bg teacher","bg classroom","bg storm"],
                                    ["bg storm","bg dangerroom","bg dangerroom","bg storm"],
                                    ["bg teacher","bg teacher","bg classroom","bg storm"],
                                    ["bg pool","bg campus","bg classroom","bg storm"],
                                    ["bg storm","bg campus","bg storm","bg pool"],
                                    ["bg storm","bg campus","bg storm","bg pool"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                    self.MassageChart = ["feet","calves","thighs","hips","ass","ass","pussy","ass","pussy","pussy"]

            elif self.Tag == "Jubes":
                    self.voice = ch_v

                    self.Casual1 = [2,0,"shorts","red shirt",0,"sports bra","blue panties","jacket",0,0,0]
                    self.Casual2 = [2,0,"pants","black shirt",0,"sports bra","blue panties","jacket",0,0,0]
                    self.Gym = [0,0,"pants",0,0,"sports bra","blue panties",0,0,0,10]
                    self.Sleepwear = [0,0,0,0,0,"sports bra","blue panties",0,0,0,25]
                    self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]
                    self.Costume = [0,0,"pants","black shirt",0,"sports bra","blue panties","jacket",0,0,0]
                    self.Home = "bg jubes"
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

                    #fills in existing characters
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

                    self.Schedule = [["bg jubes","bg dangerroom","bg dangerroom","bg jubes"],
                                    ["bg classroom","bg classroom","bg jubes","bg jubes"],
                                    ["bg jubes","bg dangerroom","bg dangerroom","bg jubes"],
                                    ["bg dangerroom","bg dangerroom","bg jubes","bg jubes"],
                                    ["bg pool","bg campus","bg campus","bg jubes"],
                                    ["bg jubes","bg campus","bg jubes","bg pool"],
                                    ["bg jubes","bg campus","bg jubes","bg pool"],
                                    ] #Schedule[0-6][0-4] = Schedule[Weekday][Time_Count]

                    self.MassageChart = ["neck","shoulders","calves","feet","neck","shoulders","calves","feet","pussy","pussy"]

            self.OutfitChange(Changed=1) #assigns their default outfit, hopefully

        def Introduction(self): #rkeljs
                #things to add when girl is introduced
                if self == RogueX: #if self.Name == "Rogue":?
                        self.Petname = "Sugar"
                        self.Petnames = ["Sugar",Player.Name]
                        self.Pet = "Rogue"
                        self.Pets = ["Rogue"]
                elif self == KittyX:
                        self.Petname = Player.Name[:1]
                        self.Petnames = ["sweetie",Player.Name[:1],Player.Name]
                        self.Pet = "Kitty"
                        self.Pets = ["Kitty"]
                elif self == EmmaX:
                        self.Names = ["Ms. Frost"]
                        self.Name = "Ms. Frost"
                        self.Petname = "young man"
                        self.Petnames = ["young man",Player.Name]
                        self.Pet = EmmaX.Name
                        self.Pets = ["Emma","Ms. Frost"]
                elif self == LauraX:
                        self.Petname = "guy"
                        self.Petnames = ["guy",Player.Name]
                        self.Pet = "Laura"
                        self.Pets = ["Laura","X-23"]
                elif self.Tag == "Jean":
                        self.Petname = "um. . ."
                        self.Petnames = ["um. . ."]
                        self.Pet = JeanX.Name
                        self.Pets = ["Jean"]
                elif self.Tag == "Storm":
                        self.Petname = "Player.Name"
                        self.Petnames = ["Player.Name"]
                        self.Pet = StormX.Name
                        self.Pets = ["Storm","Ororo","Ms. Munroe"]
                elif self.Tag == "Jubes":
                        self.Petname = "Bro"
                        self.Petnames = ["Bro","Player.Name"]
                        self.Pet = JubesX.Name
                        self.Pets = ["Jubes","Jubilee"]

                self.OutfitChange(6,Changed=1) #assigns their default outfit, hopefully
                global TotalGirls
                if self not in TotalGirls:
                        TotalGirls.append(self)                 #These are the girls you have met at all
                Shop_Inventory.extend(["DL","G","A"])     #adds these three items to the store for each girl added
                PersonalRooms.append(self.Home)

        def SluttyClothes(self):
                # called to check if loosened morals will lead to looser default outfits.
                # $ RogueX.SluttyClothes
                if self == RogueX:
                            if "stockings and garterbelt" in self.Inventory:
                                    self.Casual1[9] = "stockings and garterbelt"
                            elif self.Inbt >= 300: #ApprovalCheck("Rogue", 300, "I"):
                                    self.Casual1[9] = "stockings"
                            else:
                                    self.Casual1[9] = "tights"

                            if self.Gym[0] == 0 and self.Gym[5] and self.Inbt >= 300:
                                    #removed hoodie if she's no longer shy
                                    self.Gym[3] == 0

                            if self.Swim[0] == 0 and self.Swim[5] and self.Inbt >= 300:
                                    #removed hoodie if she's no longer shy
                                    self.Swim[3] == 0
                elif self == KittyX:
                            if self.Swim[2] == "blue skirt" and self.Swim[6] and self.Inbt > 500:
                                    #removes blue skirt if she gets comfortable with it.
                                    self.Swim[2] = 0
                elif self == LauraX:
                            if self.Inbt >= 400 and self.Casual2[5] == "leather bra" and "corset" in self.Inventory:
                                    self.Casual2[5] = "corset"
                            if self.Inbt >= 600 and "lace panties" in self.Inventory:
                                    self.Casual2[6] = "lace panties"
                            if self.Inbt >= 600 and "stockings and garterbelt" in self.Inventory:
                                    self.Casual2[9] = "stockings and garterbelt"

                elif self == JeanX:
                            if "stockings and garterbelt" in self.Inventory:
                                    self.Casual1[9] = "stockings and garterbelt"
                            elif self.Love >= 300: #ApprovalCheck("Rogue", 300, "I"):
                                    self.Casual1[9] = "stockings"
                            if self.Inbt >= 600 and "bikini top" in self.Inventory:
                                    self.Gym[5] = "bikini top" if self.Gym[0] == 1 else self.Gym[5]
                            if self.Inbt >= 600 and "lace bra" in self.Inventory:
                                    self.Casual1[5] = "lace bra"
                                    self.Casual2[5] = "lace bra"
                            if self.Inbt >= 600 and "lace panties" in self.Inventory:
                                    self.Casual1[6] = "lace panties"
                                    self.Casual2[6] = "lace panties"
                elif self == StormX:
                            if self.Inbt >= 400 and self.Casual2[5] == "sports bra":
                                    self.Casual2[5] = "tube top"
                            if self.Inbt >= 400 and self.Casual2[5] == "white panties":
                                    self.Casual2[5] = "black panties"
                            if self.Inbt >= 600 and "lace panties" in self.Inventory:
                                    self.Casual2[6] = "lace panties"
                elif self == JubesX:
                            if self.Inbt >= 500 and self.Casual1[3] == "red shirt":
                                    self.Casual1[3] = "tube top"
                                    self.Casual1[5] = 0
                            if self.Inbt >= 600 and "lace panties" in self.Inventory:
                                    self.Casual2[6] = "lace panties"
                            if self.Inbt >= 600 and "stockings and garterbelt" in self.Inventory:
                                    self.Casual2[9] = "stockings and garterbelt"
                return

        def AddWord(self,Only=0,Recent=0,Daily=0,Trait=0,History=0):
                #applies variables to appropriate character stats
                # $ RogueX.AddWord(1,"angry",0,0,0)
                #if Only, then only apply it if it's not already there
                if (Recent and not Only) or (Recent and Recent not in self.RecentActions):
                        self.RecentActions.append(Recent)
                if (Daily and not Only) or (Daily and Daily not in self.DailyActions):
                        self.DailyActions.append(Daily)
                if (Trait and not Only) or (Trait and Trait not in self.Traits):
                        self.Traits.append(Trait)
                if (History and not Only) or (History and History not in self.History):
                        self.History.append(History)
                return

        def DrainWord(self, Word = "word", Recent = 1, Daily = 1, Traits=0):
                # to remove words from the daily/recent lists ,
                # $ RogueX.DrainWord("angry",0,1)
                if Recent and Word in self.RecentActions:
                    while Word in self.RecentActions:
                            self.RecentActions.remove(Word)
                if Daily and Word in self.DailyActions:
                    while Word in self.DailyActions:
                            self.DailyActions.remove(Word)
                if Traits and Word in self.Traits:
                    while Word in self.Traits:
                            self.Traits.remove(Word)
                return

        def Statup(self, Flavor=0, Check=100, Value=1, Greater=0, Type=0, Alt=[[],0,0], Overflow=0, BStat=0, XPOS = 0.75):
                # $ RogueX.Statup("Love", 90, 5)
                # $ RogueX.Statup("Love", 90, 5,Alt=[[RogueX,KittyX],500,-10])

                if self not in TotalGirls: #should remove "character don't exist" errors
                        return

                if self in Alt[0]:
                                #if there is an alternate character option. . .
                                Check = Alt[1] if Alt[1] else Check
                                Value = Alt[2] if Alt[2] else Value

                if Flavor == "Love" or Flavor == "Obed" or Flavor == "Inbt":
                        #bumps this stat into the 1000s
                        Check = Check * 10

                Type = getattr(self,Flavor) #sets Type to the value referenced (ie if Flavor is "Love," Type becomes self.Love's value)

                Overflow = self.Chat[4]
                XPOS = self.sprite_location

                if self.Tag == "Jean" and Flavor == "Inbt" and self.IX > 0:
                        #Lowers her Inbt to true levels before check
                        Type -= self.IX

                if Greater:
                        #this checks if it's greater or less than the intended value
                        #if it fails, the value is zeroed out, cancelling the rest
                        if Type >= Check:
                            #If it passes the check, add Value to it
                            Type += Value
                        else:
                            #If not, don't add Value and set Value to 0
                            Value = 0
                else:
                        if Type <= Check:
                            Type += Value
                        else:
                            Value = 0

                if self.Tag == "Jean" and Flavor == "Inbt" and self.IX > 0:
                        #Raises her Inbt back to true levels after check
                        Type += self.IX

                if Value:
                    #If there is any change to the stat
                    #Sets reporting text color based on Flavor
                    if self.Tag == "Jean" and Value > 0:
                            if Flavor == "Obed" and self.Obed <= 800 and Check < 800:
                                    # if her Obedience is under 800 and the check is for less than 800,
                                    # reduces half the gains. This slows low obed farming options
                                    Value = int(Value/2)
                                    Type -= Value
                            elif Flavor == "Inbt" and self.IX > 0:
                                    if self.Taboo >= 40:
                                            # When she can't whammy people, public stuff rewards more
                                            Value += Value
                                            Type += Value
                                    if Type > 1000:
                                            # if her inhibition is maxed, further increases are removed from the IX modifier instead
                                            self.IX -= (Type - 1000)
                                            Type = 1000
                                            Value = 0
                                    elif Type > 700:
                                            # if her inhibition is just high, half the value is applied to her IX
                                            self.IX -= int(Value/2)
                                    self.IX = 0 if self.IX < 0 else self.IX
                            elif Flavor == "Love" and Type >= 500 and self.Obed < 700:
                                    #if the character is Jean, her Love stat will not raise above 500,
                                    #unless her Obedience is over 700. It does get stored up, however,
                                    #and doled out at a later date.
                                    if self.Love < 500: #and Type > 500
                                            # If her Love is just crossing 500, set it to 500 and then make Value the remainder
                                            self.Love = 500
                                            Value = Type - 500
                                    #else:
                                            #Value = (Type - self.Love) if Type > self.Love else 0
                                            ##if the combined value is higher than Love, then Value becomes the remainder

                                    self.StatStore += Value                                     #stores overflow amount for later

                                    if Check > self.Obed:
                                            #if the checked value is higher than her current Obedience
                                            Flavor = "Obed"                                     #sets the flavor to obed
                                            Value = int(Value/5)                                #sets value change as 1/5th the amount
                                            Type = self.Obed + Value                            #establishes the new change as Obed+new value, likely 1
                                    else:
                                            Value = 0
                                    #if her Obedience is over 700, Love checks just pass right through.



                    if Flavor == "Love":
                            Color = "#c11b17"
                    elif Flavor == "Obed":
                            Color = "#2554c7"
                    elif Flavor == "Inbt":
                            Color = "#FFF380"
                    elif Flavor == "Lust":
                            Color = "#FAAFBE"
                            CallHolder(Value, Color, XPOS) #show popup
                            if Flavor == "Lust" and Type >= 100 and not Trigger:
                                        #calls orgasm if Lust goes over 100, breaks routine
                                        renpy.call("Girl_Cumming",self,1)
                                        return
                            Type = 100 if Type > 100 else Type
                            setattr(self,Flavor,Type)
                            return

                    if Type > 1000:
                        CallHolder((-(Type-1000-Value)), Color, XPOS)
                        if not self.Chat[4]:
                            #if no overflow mechanic is prepared. . .
                            Value = 0
                        else:
                            #if the value overflows, play one value meter, then. . .
                            Value = Type - 1000
                            # change the Flavor to the new thing if there is a swap happening
                            setattr(self,Flavor,1000)
                            if Flavor == "Love":
                                    if self.Chat[4] == 1:       #[Love to Obedience]
                                        Flavor = "Obed"
                                    elif self.Chat[4] == 2:     #[Love to Inhibition]
                                        Flavor = "Inbt"
                                    else:
                                        Value = 0
                            elif Flavor == "Obed":
                                    if self.Chat[4] == 3:       #[Obedience to Inhibition]
                                        Flavor = "Inbt"
                                    elif self.Chat[4] == 4:
                                        Flavor = "Love"   #[Obedience to Love]
                                    else:
                                        Value = 0
                            elif Flavor == "Inbt":
                                    if self.Chat[4] == 5:       #[Inhibition to Obedience]
                                        Flavor = "Obed"
                                    elif self.Chat[4] == 6:
                                        Flavor = "Love"    #[Inhibition to Love]
                                    else:
                                        Value = 0

                            Type = getattr(self,Flavor)
                            Type += Value

                            if Flavor == "Love":
                                    #Sets reporting text color based on Flavor
                                    Color = "#c11b17"
                            elif Flavor == "Obed":
                                    Color = "#2554c7"
                            elif Flavor == "Inbt":
                                    Color = "#FFF380"
                            else:
                                    Color = "#FFFFFF"
                    #end Type change element

                    if Value:
                            # show pop-up
                            CallHolder(Value, Color, XPOS)

                #end "if value is positive"

                Type = 1000 if Type > 1000 else Type

                setattr(self,Flavor,Type)
                return

        def FaceChange(self, Emote = 5, B = 5, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
            Emote = self.Emote if Emote == 5 else Emote
            B = self.Blush if B == 5 else B

            if (self.Forced or "angry" in self.RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                Emote = "angry"
            elif self.ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                Emote = "sad"

            if Emote == "normal":
                self.Mouth = "normal"
                self.Brows = "normal"
                self.Eyes = "normal"
            elif Emote == "angry":
                if self == LauraX:
                    self.Mouth = "kiss"
                else:
                    self.Mouth = "sad"
                self.Brows = "angry"
                self.Eyes = "sexy"
            elif Emote == "bemused":
                if self == EmmaX:
                    self.Mouth = "normal"
                else:
                    self.Mouth = "lipbite"
                self.Brows = "sad"
                self.Eyes = "squint"
            elif Emote == "closed":
                if self == RogueX:
                    self.Mouth = "lipbite"
                else:
                    self.Mouth = "normal"
                self.Brows = "sad"
                self.Eyes = "closed"
            elif Emote == "confused":
                self.Mouth = "kiss"
                self.Brows = "confused"
                if self == LauraX or self == EmmaX:
                    self.Eyes = "squint"
                else:
                    self.Eyes = "surprised"
            elif Emote == "kiss":
                self.Mouth = "kiss"
                if self == LauraX or self == EmmaX:
                    self.Brows = "sad"
                else:
                    self.Brows = "normal"
                self.Eyes = "closed"
            elif Emote == "sad":
                self.Mouth = "sad"
                self.Brows = "sad"
                if self == JeanX or self == JubesX:
                    self.Eyes = "normal"
                else:
                    self.Eyes = "sexy"
            elif Emote == "sadside":
                self.Mouth = "sad"
                self.Brows = "sad"
                self.Eyes = "side"
            elif Emote == "sexy":
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
            elif Emote == "sly":
                self.Brows = "normal"
                self.Eyes = "squint"
                if self == RogueX:
                    self.Mouth = "grimace"
                if self == LauraX:
                    if LauraX.Love >= 700:
                        self.Mouth = "smile"
                    else:
                        self.Mouth = "smirk"
                    self.Brows = "confused"
                elif self == KittyX:
                    self.Mouth = "smile"
                else:
                    self.Mouth = "smirk"
            elif Emote == "smile":
                if self == LauraX and LauraX.Love < 700:
                    self.Mouth = "smirk"
                else:
                    self.Mouth = "smile"
                self.Brows = "normal"
                self.Eyes = "normal"
            elif Emote == "surprised":
                if self == RogueX or self == KittyX:
                    self.Mouth = "surprised"
                else:
                    self.Mouth = "kiss"
                self.Brows = "surprised"
                self.Eyes = "surprised"
            elif Emote == "oh":
                self.Mouth = "kiss"
                self.Brows = "surprised"
                self.Eyes = "surprised"
            elif Emote == "startled":
                if self == RogueX or self == KittyX:
                    self.Mouth = "grimace"
                else:
                    self.Mouth = "smile"
                self.Brows = "surprised"
                self.Eyes = "surprised"
            elif Emote == "down":
                if self == RogueX or self == KittyX:
                    self.Mouth = "surprised"
                else:
                    self.Mouth = "sad"
                self.Brows = "sad"
                self.Eyes = "down"
            elif Emote == "perplexed":
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
            elif Emote == "sucking":
                self.Mouth = "sucking"
                if self == EmmaX:
                    self.Brows = "surprised"
                elif self == LauraX:
                    self.Brows = "sad"
                else:
                    self.Brows = "normal"
                self.Eyes = "closed"
            elif Emote == "tongue":
                self.Mouth = "tongue"
                self.Brows = "sad"
                if self == LauraX:
                    self.Eyes = "stunned"
                else:
                    self.Eyes = "sexy"
            elif Emote == "manic":
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
                if self.Lust >= 50 and ApprovalCheck(self, 1200):
                        self.Emote = "sexy"
                elif self.Addict > 75:
                        self.Emote = "manic"
                elif self.Love >= self.Obed and self.Love >= 500:
                        self.Emote = "smile"
                elif self.Inbt >= self.Obed and self.Inbt >= 500:
                        self.Emote = "smile"
                elif self.Addict > 50:
                        self.Emote = "manic"
                elif (self.Love + self.Obed) < 300:
                        self.Emote = "angry"
                else:
                        self.Emote = "normal"
                return

        def LustFace(self,Extreme=0,Kissing=0):
                if self.Thirst >= 80:
                        self.Lust += 2
                elif self.Thirst >= 50:
                        self.Lust += 1

                if self.Lust >= 80:
                        self.Blush = 2
                elif self.Lust >= 40:
                        self.Blush = 1

                if self.Lust >= 80:
                        self.Wet = 2
                elif self.Lust >= 50:
                        self.Wet = 1

                if Trigger3 == "kiss both" or Trigger3 == "kiss girl":
                        #if the girls are kissing or all three are
                        Kissing = 1
                elif Trigger4 == "kiss both" or Trigger3 == "kiss girl":
                        #if the girls are kissing or all three are
                        Kissing = 1
                elif Partner != self:
                        #If the called girl is kissing and is primary
                        if Trigger == "kiss_you" or Trigger2 == "kiss_you":
                            Kissing = 1
                elif Trigger4 == "kiss_you":
                        #If the called girl is kissing you in a threesome action
                        Kissing = 1

                if Kissing:
                        self.Eyes = "closed"
                        if self.Tag == "Emma":
                            self.Mouth = "kiss"
                        elif self.Kissed >= 10 and self.Inbt >= 300:
                            self.Mouth = "sucking"
                        elif self.Kissed > 1 and self.Addict >= 50:
                            self.Mouth = "sucking"
                        else:
                            self.Mouth = "kiss"
                else:
                        #If called girl is not kissing someone
                        if self.Lust >= 90:
                                self.Eyes = "closed"
                                self.Brows = "sad"
                                self.Mouth = "surprised"
                        elif self.Lust >= 70 or Extreme:
                                self.Eyes = "sexy"
                                self.Brows = "sad"
                                self.Mouth = "lipbite"
                        elif self.Lust >= 50:
                                if self.Tag == "Emma" or self.Tag == "Laura":
                                        self.Eyes = "squint"
                                else:
                                        self.Eyes = "sexy"
                                self.Brows = "sad"
                                self.Mouth = "lipbite"
                        elif self.Lust >= 30:
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
                        if self.Tag == "Laura" and self.Lust < 50 and not Extreme and not ApprovalCheck(self, 1000):
                                self.Eyes = "side"

                if Partner == self and Trigger4 in ("lick pussy", "lick ass", "blow", "suck breasts"):
                                self.Mouth = "tongue"
                elif Trigger3 in ("lick pussy", "lick ass", "suck breasts"):
                                self.Mouth = "tongue"

                if self.OCount >= 10:
                        #If you've fucked her senseless
                        self.Eyes = "stunned"
                        self.Mouth = "tongue"

                if not self.Loose:
                        #if anal hurts. . .
                        if Partner != self and (Trigger == "anal" or Trigger == "dildo anal" or Trigger3 == "dildo anal"):
                            self.Eyes = "closed"
                            self.Brows = "angry"

                if "unseen" in self.RecentActions:
                        self.Eyes = "closed"
                if Partner and self != Partner:
                        Partner.LustFace()
                return

        def OutfitChange(self, OutfitTemp = 5, Spunk = 0, Undressed = 0, Changed = 1,HolderOutfit=[]):
                # $ RogueX.OutfitChange("casual1")
                # OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed
                #OutfitTemp = self.Outfit if not OutfitTemp else OutfitTemp
                if self not in TotalGirls: #should remove "character don't exist" errors
                        return

                OutfitTemp = OutfitTemp if OutfitTemp else self.Outfit

                if self.Loc == bg_current and renpy.showing("NightMask", layer='nightmask') and Time_Count == 0: #morning time
                        #Skips this check if it's a sleepover
                        return

                if self.Loc not in ("bg showerroom","bg pool") or (OutfitTemp not in ("nude","swimwear","towel")):
                        #Dries her off
                        self.Water = 0
                if self.Spunk:
                        #Removes spunk if told to do so.
                        if "painted" not in self.DailyActions or "cleaned" not in self.DailyActions:
                            del self.Spunk[:]

                #Resets "half-dressed" states
                if self.Upskirt or self.Uptop or self.PantiesDown:
                        Undressed = 1

                self.Upskirt = 0
                self.Uptop = 0
                self.PantiesDown = 0

                if OutfitTemp == 5:
                        #this sets it to default if using AnyOutfit
                        if "yoinked" in self.RecentActions:
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
                        HolderOutfit = [0,0,0,"towel",0,0,0,0,0,0,35] #fills Holder with the values of the sent uni. . .
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
                                        if "swim" not in self.DailyActions:
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
                                elif self == KittyX and "blue skirt" not in self.Inventory and self.Inbt <= 400:
                                        self.Outfit = self.OutfitDay
                                        if "swim" not in self.DailyActions:
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
                elif not self.Panties and HolderOutfit[6] and "pantyless" not in self.DailyActions:
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

                if "ripped" in self.DailyActions and "modesty" not in self.RecentActions:
                        #this keeps her in ripped hose all day if they are ripped off her
                        self.Hose = "ripped pantyhose" if self.Hose == "pantyhose" else self.Hose
                        self.Hose = "ripped tights" if self.Hose == "tights" else self.Hose
                if self.Panties and self.Panties != "shorts" and "pantyless" in self.DailyActions and "modesty" not in self.DailyActions:
                        # This checks the pantyless state from flirting
                        if OutfitTemp != "sleep" and OutfitTemp != "gym":
                                self.Panties = 0

                if not Changed and OutfitTemp == self.Outfit and self.Loc == bg_current:
                        #If she was partially dressed then it says she gets dressed
                        if Undressed == 2:
                                renpy.say(None,self.Name+" throws on a towel.", interact=True)
                        elif Undressed:
                                renpy.say(None,self.Name+" throws her clothes back on.", interact=True)
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
                            if self.Chest in ("tank","buttoned tank"):
                                return 5
                    if self == LauraX:
                            if self.Chest in ("leather bra","white tank"):
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
                    if self.Legs in ("skirt","blue skirt","other skirt","dress"):
                                return 5
                    if self.Legs == "yoga pants":
                                return 8
                    if self.Over == "towel" and self not in (EmmaX,StormX):
                                return 5
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

        def ClothingCheck(self,C = 0):
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

        def ModestyCheck(self, Check=0,C = 0):
                    C = 0
                    #This function determines whether they are partially nude or not.
                    #if Check is 0, check both, if it's 1, check top, if it's 2, check bottom only
                    if Check == 2:
                        pass    #skips if only checking bottoms
                    elif self.OverNum() >= 3: #if her top is fine
                        pass
                    elif self.ChestNum() >= 3:
                        pass
                    else:
                        C += 1

                    if Check == 1:
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

        def SeenCheck(self, Check=0, C = 0):
                    C = 0
                    #This function returns 1-2 if she is partiallly naked and this is the first the player's seen of it.
                    # "Check" is 1 if it's intended to see whether she has been seen at all.
                    # "Check" is 2 if it's intended to see whether she has been seen topless.
                    # "Check" is 3 if it's intended to see whether she has been seen bottomless.
                    if not self.SeenChest:
                        if (not self.Over and not self.Chest) or self.Uptop or Check == 1 or Check == 2:
                                    C += 1
                    if not self.SeenPussy:
                        if Check == 1 or Check == 3:
                                    C += 1
                        elif not self.Legs or self.Upskirt:
                            #if no pants or pants down
                            if self.PantiesDown or (self.HoseNum() < 5 and not self.Panties):
                                    # if no panties and loose hose or they're down
                                    C += 1
                    return C

        def GirlLikeCheck(self,Chr=0):
                # RogueX.GirlLikeCheck(KittyX) will return RogueX.LikeKitty, ie 600
                return getattr(self,"Like"+Chr.Tag)

        def GirlLikeUp(self,Chr=0,Value=0,Like=0):
                # RogueX.GirlLikeUp(KittyX,5) will return RogueX.LikeKitty += 5
                if "Jeaned" in self.Traits:
                        #if Jean has messed with their stats, change the stored value instead
                        Like = getattr(JeanX,"LikeS"+self.Tag) #Like = RogueX.LikeKitty
                        if Like + Value > 1000:
                                setattr(JeanX,"LikeS"+self.Tag, 1000)
                        elif Like + Value < 0:
                                setattr(JeanX,"LikeS"+self.Tag, 0)
                        else:
                                setattr(JeanX,"LikeS"+self.Tag, Value + Like) #RogueX.LikeKitty = RogueX.LikeKitty + Value
                        return

                Like = getattr(self,"Like"+Chr.Tag) #Like = RogueX.LikeKitty
                if Like + Value > 1000:
                        setattr(self,"Like"+Chr.Tag, 1000)
                elif Like + Value < 0:
                        setattr(self,"Like"+Chr.Tag, 0)
                else:
                        setattr(self,"Like"+Chr.Tag, Value + Like) #RogueX.LikeKitty = RogueX.LikeKitty + Value
                return

        def GLG(self, ChrB = 0, Check=200, Modifier = 1, Auto = 0, Jealousy = 0, Ok = 0, Likes=0):
                # self is the subject girl, ChrB is the object girl,
                # Modifier is sent as the amount of offense this might cause,
                # Jealousy is the temp value for how mad the girl will get
                # Likes stores the XLikesY stat temporarily
                # Auto quickly raises lust and like by a sent amount
                # returns 2 if very into it, 1 if ok with it, 0 if not cool with it.

                # was call GirlLikesGirl(Party[0],Party[1],700,5,1)
                # now $ RogueX.GLG(Party[1],700,5,1)
                if self not in TotalGirls or ChrB not in TotalGirls: #should remove "character don't exist" errors
                        return
                Jealousy = 0
                Likes = self.GirlLikeCheck(ChrB)
                #stores this value temporarily

                if Likes <= Check:
                        #if the checked girl likes the second girl less than the checked value. . .
                        if Auto:
                                #if set to auto, just raises the Like stat by the modifier value.
                                setattr(self,"Like"+ChrB.Tag,Likes+Modifier) #updates Like modifier
                                self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5th modifier
                                return

                        # checks if they have agreed to share or not
                        if self in Player.Harem:
                                #if "dating" in RogueX.Traits or RogueX in Player.Harem:
                                if ChrB not in Player.Harem and "poly " + ChrB.Tag not in self.Traits:
                                        # if KittyX not in Player.Harem and "poly Kitty" not in RogueX.Traits:
                                        Jealousy = 100
                elif Auto: #this is a quick return,
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5th modifier
                            return

                #Establishes how jealous lead is likely to get
                Jealousy += (self.Love - 600) if self.Love > 600 else 0
                        #How much her Love stat is over 600, +0-400
                Jealousy += self.SEXP if self.Inbt <= 500 else 0
                        #plus her SexP rating if she has low inhibitions, +0-200
                Jealousy -= (self.Obed - 250) if self.Obed > 250 else 0
                        #minus how much her Obed stat is over 250, -0-750
                        # = result of up to 700 if high love, dating, and low obedience

                Jealousy = 0 if Jealousy < 1 else Jealousy
                    #Balances it to no less than zero
                Modifier += 1 if not Jealousy and Likes >= 500 else 0
                    #+ modifier if she doesn't hate Kitty but has no jealousy left


                if Likes >= 900:
                            #If she really likes the girl, then she is turned on, likes both of you more.
                            Likes += Modifier
                            self.Statup("Love", 80, (int(Modifier/2))) #raises Love by 1/2 modifier
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5 modifier
                            Ok = 2
                elif Likes >= 800:
                        #If she mostly likes the girl, and is not super jealous, she likes you both more.
                        if Jealousy <= 300:
                            Likes += Modifier
                            self.Statup("Love", 80, (int(Modifier/2))) #raises Love by 1/2 modifier
                            self.Statup("Lust", 200, (int(Modifier/2))) #raises Lust by 1/2 modifier
                            Ok = 2
                        else:
                            Likes -= Modifier
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5 modifier
                            Ok = 1
                elif Likes >= 600:
                        #If she's friends with the girl, only low jealousy is positive
                        if Jealousy <= 100:
                            Likes += Modifier
                            self.Statup("Love", 80, (int(Modifier/4))) #raises Love by 1/4 modifier
                            self.Statup("Lust", 200, (int(Modifier/2))) #raises Lust by 1/2 modifier
                            Ok = 2
                        elif Jealousy <= 300:
                            Likes -= Modifier
                            self.Statup("Lust", 200, (int(Modifier/2))) #raises Lust by 1/5 modifier
                            Ok = 1
                        else:
                            Likes -= (Modifier + (int(Jealousy/50)))
                            self.Statup("Love", 90, (-(int(Modifier)))) #lowers Love by 1/2 modifier
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5 modifier
                            Ok = 2
                elif Likes >= 400:
                        #If she is neutral to the girl, it's all negative
                        if Jealousy <= 100:
                            Likes -= Modifier
                            Ok = 1
                        else:
                            Likes -= (Modifier + (int(Jealousy/100)))
                        self.Statup("Lust", 200, (int(Modifier/10))) #raises Lust by 1/10 modifier
                else:
                        #If she hates the girl, it's all very negative
                        Likes -= (Modifier + (int(Jealousy/50)))
                        self.Statup("Lust", 200, (int(Modifier/10))) #raises Lust by 1/5 modifier
                self.Statup("Inbt", 60, (int(Modifier/10))) #raises Inbt by 1/10 modifier

                # restores "likes" to target character.

                setattr(self,"Like"+ChrB.Tag,Likes+Modifier) #updates Like modifier

                return Ok
                # returns 2 if very into it, 1 if ok with it, 0 if not cool with it.

        def NameCheck(self, Cnt = 0): #rkeljs
                #Checks how she reacts to you using her petname
                #Cnt and Ugh are internal count variable
                # $ RogueX.NameCheck() #nee
                if self.Pet == self.Name:
                        return 0
                if self.Taboo:
                        # +4 if Taboo 40, +2 if Taboo 20
                        Cnt = int(self.Taboo/10)

                #easy options
                if self.Pet in ("girl","boo","bae","baby","sweetie"):
                    if ApprovalCheck(self, 500, "L", TabM=1,Alt=[[LauraX],600]):
                        self.Statup("Love", 80, 1)
                    else:
                        self.Statup("Love", 50, -1)
                        return 1
                elif self.Pet in ("sexy","lover","beloved"):
                    if ApprovalCheck(self, 900, TabM=1,Alt=[[LauraX],1100]):
                        self.Statup("Love", 80, 2)
                        self.Statup("Obed", 80, 1)
                        self.Statup("Inbt", 70, 1)
                    else:
                        self.Statup("Love", 50, (-1-Cnt))
                        self.Statup("Obed", 50, 1)
                        self.Statup("Inbt", 20, -1)
                        return 1
                #tougher options
                elif self.Pet == "slave":
                        if ApprovalCheck(self, 800, "O", TabM=3,Alt=[[EmmaX,StormX],900]):
                            self.Statup("Lust", 90, (3+Cnt))
                            self.Statup("Obed", 95, (2+Cnt))
                            self.Statup("Inbt", 30, 1)
                            self.Statup("Inbt", 70, 1)
                        elif ApprovalCheck(self, 500, "O", TabM=3,Alt=[[EmmaX,StormX],600]):
                            self.Statup("Lust", 90, 1)
                            self.Statup("Love", 200, -1)
                            self.Statup("Obed", 80, 2)
                            self.Statup("Inbt", 70, 1)
                        else:
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 50, -1)
                            return 1
                elif self.Pet == "pet":
                        if ApprovalCheck(self, 1500, TabM=2,Alt=[[LauraX],800]):
                            self.Statup("Lust", 90, (3+Cnt))
                            self.Statup("Obed", 95, (2+Cnt))
                            self.Statup("Inbt", 30, 1)
                            self.Statup("Inbt", 70, 1)
                        elif ApprovalCheck(self, 1200, TabM=2,Alt=[[LauraX],650]):
                            self.Statup("Lust", 60, 1)
                            self.Statup("Obed", 80, 2)
                            self.Statup("Inbt", 70, 1)
                        else:
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 50, -1)
                            return 1
                elif self.Pet == "slut":
                        if ApprovalCheck(self, 500, "O", TabM=2) or ApprovalCheck(self, 500, "I", TabM=2,Alt=[[LauraX],400]):
                            self.Statup("Lust", 90, (4+Cnt))
                            self.Statup("Obed", 95, (2+Cnt))
                            self.Statup("Inbt", 40, 2)
                            self.Statup("Inbt", 80, 1)
                        elif ApprovalCheck(self, 300, "O", TabM=2) or ApprovalCheck(self, 300, "I", TabM=2,Alt=[[LauraX],200]):
                            self.Statup("Lust", 90, 1)
                            self.Statup("Love", 200, (-1-Cnt))
                            self.Statup("Obed", 80, (2+Cnt))
                            self.Statup("Inbt", 70, 1)
                        else:
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Love", 50, (-1-Cnt), 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet == "whore":
                        if ApprovalCheck(self, 600, "O", TabM=2,Alt=[[EmmaX],700]) or ApprovalCheck(self, 600, "I", TabM=2,Alt=[[LauraX],400]):
                            self.Statup("Lust", 90, 4)
                            self.Statup("Obed", 95, 2)
                            self.Statup("Inbt", 50, 2)
                            self.Statup("Inbt", 80, 1)
                        elif ApprovalCheck(self, 400, "O", TabM=2,Alt=[[EmmaX],500]) or ApprovalCheck(self, 400, "I", TabM=2):
                            self.Statup("Lust", 90, 1)
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Obed", 80, 2)
                            self.Statup("Inbt", 70, 1)
                        else:
                            self.Statup("Love", 200, (-3-Cnt))
                            self.Statup("Love", 50, (-2-Cnt), 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 21, 1, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet == "sugartits":
                        if ApprovalCheck(self, 1500, TabM=1,Alt=[[EmmaX],1300]):
                            self.Statup("Obed", 80, 1)
                            self.Statup("Obed", 50, 2)
                            self.Statup("Inbt", 70, 1,Alt=[[EmmaX],70,2])
                            self.Statup("Inbt", 30, 2,Alt=[[KittyX],60,3])
                        else:
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Love", 50, (-1-Cnt))
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet == "sex friend":
                        if ApprovalCheck(self, 750, "O", TabM=1) or ApprovalCheck(self, 600, "I", TabM=1):
                            self.Statup("Lust", 90, 3)
                            self.Statup("Obed", 95, 2)
                            self.Statup("Inbt", 40, 2)
                            self.Statup("Inbt", 80, 1)
                        elif ApprovalCheck(self, 600, "O", TabM=1) or ApprovalCheck(self, 400, "I", TabM=1):
                            self.Statup("Lust", 90, 2)
                            self.Statup("Love", 200, (-1-Cnt))
                            self.Statup("Obed", 80, 1)
                            self.Statup("Inbt", 70, 1)
                            self.Blush = 1
                        else:
                            self.Statup("Love", 200, -Cnt)
                            self.Statup("Love", 50, (-1-Cnt), 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet == "fuckbuddy":
                        if ApprovalCheck(self, 700, "O", TabM=2) or ApprovalCheck(self, 700, "I", TabM=1):
                            self.Statup("Lust", 90, 3)
                            self.Statup("Obed", 95, 2)
                            self.Statup("Inbt", 40, 2)
                            self.Statup("Inbt", 85, 1)
                        elif ApprovalCheck(self, 600, "O", TabM=2) or ApprovalCheck(self, 500, "I", TabM=1):
                            self.Statup("Lust", 90, 2)
                            self.Statup("Love", 200, (-1-Cnt))
                            self.Statup("Obed", 80, 1)
                            self.Statup("Inbt", 70, 1)
                            self.Blush = 1
                        else:
                            self.Statup("Love", 200, -Cnt)
                            self.Statup("Love", 60, (-2-Cnt), 1)
                            self.Statup("Obed", 60, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                elif self.Pet in ("baby girl","mommy"):
                        if ApprovalCheck(self, 1200, TabM=1):
                            self.Statup("Obed", 80, 1)
                            self.Statup("Obed", 50, 2)
                            self.Statup("Inbt", 70, 1)
                            self.Statup("Inbt", 30, 2)
                        else:
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Love", 50, (-1-Cnt))
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                #Rogue
                elif self.Pet == "chere":
                        if ApprovalCheck(self, 600, "L", TabM=1):
                            self.Statup("Love", 80, 2)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                #Kitty
                elif self.Pet == "kitten":
                        if ApprovalCheck(self, 600, "L", TabM=1):
                            self.Statup("Love", 80, 2)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                #Emma
                elif self.Pet == "darling":
                        if ApprovalCheck(self, 600, "L", TabM=1):
                            self.Statup("Love", 80, 2)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                #Laura
                elif self.Pet == "Wolvie":
                        if ApprovalCheck(self, 500, "I", TabM=1):
                            self.Statup("Love", 80, 1)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                elif self.Pet == "X-23":
                        if ApprovalCheck(self, 800, "O"):
                            self.Statup("Lust", 90, 3)
                            self.Statup("Love", 90, -1)
                            self.Statup("Obed", 95, 2)
                        elif ApprovalCheck(self, 700, "L") and not ApprovalCheck(self, 500, "O"):
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 30, 2)
                            self.Statup("Obed", 50, 2)
                            self.Statup("Inbt", 50, -1)
                            return 1
                return 0

label EmotionEditor(Chr=0):
        # call EmotionEditor(RogueX)
        while True:
            menu:
                "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":
                    menu:
                        "Normal":
                            $ Chr.Emote = "normal"
                        "Angry":
                            $ Chr.Emote = "angry"
                        "Smiling":
                            $ Chr.Emote = "smile"
                        "Sexy":
                            $ Chr.Emote = "sexy"
                        "Suprised":
                            $ Chr.Emote = "surprised"
                        "Bemused":
                            $ Chr.Emote = "bemused"
                        "Manic":
                            $ Chr.Emote = "manic"

                "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":
                    menu:
                        "Sad":
                            $ Chr.Emote = "sad"
                        "Sucking":
                            $ Chr.Emote = "sucking"
                        "kiss":
                            $ Chr.Emote = "kiss"
                        "Tongue":
                            $ Chr.Emote = "tongue"
                        "confused":
                            $ Chr.Emote = "confused"
                        "Closed":
                            $ Chr.Emote = "closed"
                        "Down":
                            $ Chr.Emote = "down"

                "Emotions3: Sadside Startled Perplexed Sly":
                    menu:
                        "Sadside":
                            $ Chr.Emote = "sadside"
                        "Startled":
                            $ Chr.Emote = "startled"
                        "Perplexed":
                            $ Chr.Emote = "perplexed"
                        "Sly":
                            $ Chr.Emote = "sly"
                    #$ Chr.FaceChange
                "Toggle Mouth Spunk":
                    if "mouth" in Chr.Spunk:
                        $ Chr.Spunk.remove("mouth")
                    else:
                        $ Chr.Spunk.append("mouth")
                "Toggle hand Spunk":
                    if "hand" in Chr.Spunk:
                        $ Chr.Spunk.remove("hand")
                    else:
                        $ Chr.Spunk.append("hand")

                "Toggle Facial Spunk":
                    if "facial" in Chr.Spunk and "hair" not in Chr.Spunk:
                        $ Chr.Spunk.append("hair")
                    elif "facial" in Chr.Spunk:
                        $ Chr.Spunk.remove("facial")
                        $ Chr.Spunk.remove("hair")
                    else:
                        $ Chr.Spunk.append("facial")

                "Blush":
                    if Chr.Blush == 2:
                        $ Chr.Blush = 0
                    elif Chr.Blush:
                        $ Chr.Blush = 2
                    else:
                        $ Chr.Blush = 1
                "Exit.":
                    return
            $ Chr.FaceChange() #applies change
        #end Emotion Editor

label GirlsAngry(Girls = 0,BO=[]):
        # Causes girls to storm off if you've pissed them off.
        $ temp_modifier = 0
        $ BO = TotalGirls[:]
        while BO:
                if BO[0].Loc == bg_current and "angry" in BO[0].RecentActions:
                        if bg_current == BO[0].Home:
                                if BO[0] == RogueX:
                                        ch_r "You should get out, I'm fix'in ta throw down."
                                elif BO[0] == KittyX:
                                        ch_k "You should get out of here, I can't even look at you right now."
                                elif BO[0] == EmmaX:
                                        ch_e "You should leave, or do you want to test me?"
                                elif BO[0] == LauraX:
                                        ch_l "You should leave."
                                elif BO[0] == JeanX:
                                        ch_j "Out, NOW!"
                                elif BO[0] == StormX:
                                        ch_s "Out!"
                                elif BO[0] == JubesX:
                                        ch_v "Get out!"
                                "You head back to your room."
                                $ Party = []
                                $ renpy.pop_call()
                                jump player_room_entry
                        else:
                                $ BO[0].Loc = BO[0].Home
                        if BO[0] in Party:
                                $ Party.remove(BO[0])
                        if Girls:
                            ". . . and so does [BO[0].Name]."
                        else:
                            "[BO[0].Name] storms off."
                            if BO[0] == StormX:
                                    ". . . so to speak."
                        $ Girls += 1
                        if BO[0] == RogueX:
                                hide Rogue_Sprite with easeoutleft
                        elif BO[0] == KittyX:
                                hide Kitty_Sprite with easeoutleft
                        elif BO[0] == EmmaX:
                                hide Emma_Sprite with easeoutleft
                        elif BO[0] == LauraX:
                                hide Laura_Sprite with easeoutleft
                        elif BO[0] == JeanX:
                                hide Jean_Sprite with easeoutleft
                        elif BO[0] == StormX:
                                hide Storm_Sprite with easeoutleft
                        elif BO[0] == JubesX:
                                hide Jubes_Sprite with easeoutleft
                $ BO.remove(BO[0])
        return

label LastNamer(Wordcount = 0, Splitname = 0, Lastname = 0):
        # Wordcount = number of words
        $ Wordcount = Player.Name.count(" ")

        # Splitname turns the name into a list, ie [Charles, Francis, Xavier]
        $ Splitname = Player.Name.split()

        # Lastname picks the last word in that set
        $ Lastname = "Mr. " + Splitname[Wordcount]
        return Lastname

label DrainAll(Word=0,Recent=1,Daily=1,Traits=0):
        # called to remove words from all girls in the game.
        # call DrainAll("arriving")
        $ BO = TotalGirls[:]
        while BO:
            $ BO[0].DrainWord(Word,Recent,Daily,Traits)
            $ BO.remove(BO[0])
        return
