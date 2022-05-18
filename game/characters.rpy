init python:

    class PlayerClass(object):
        def __init__(self):
            self.name = "Zero"

            self.sprite = None
            self.color = "green"

            self.semen = 2
            self.max_semen = 3

            self.focus = 0
            self.focusing = False

            self.reputation = 600

            self.recent_history = []
            self.daily_history = []
            self.traits = []
            self.history = []

            self.Harem = []

            self.XP = 0
            self.SEXP = 0
            self.level = 1
            self.income = 12
            self.cash = 20
            self.XP_goal = 100

            self.inventory = []

            self.stat_points = 0

            self.cock_position = "out"
            self.spunk = 0
            self.cock_wet = 0

            self.addictive = False
            self.nonaddictive = False

            self.cologne = None

        def add_word(self, only = False, recent = None, daily = None, trait = None, history = None):
            if (recent and not only) or (recent and recent not in self.recent_history):
                self.recent_history.append(recent)
            if (daily and not only) or (daily and daily not in self.daily_history):
                self.daily_history.append(daily)
            if (trait and not only) or (trait and trait not in self.traits):
                self.traits.append(trait)
            if (history and not only) or (history and history not in self.history):
                self.history.append(history)
            return

        def drain_word(self, word, recent = True, daily = True, traits = False):
            if recent:
                while word in self.recent_history:
                    self.recent_history.remove(word)
            if daily:
                while word in self.daily_history:
                    self.daily_history.remove(word)
            if traits:
                while word in self.traits:
                    self.traits.remove(word)
            return

        def change_stat(self, flavor, check, update, greater_than = False, x_position = 0.75):
            stat = getattr(self, flavor)

            if greater_than:
                if stat >= check:
                    stat += update
                else:
                    update = 0
            else:
                if stat <= check:
                    stat += update
                else:
                    update = 0

            if update:
                CallHolder(update, "#FFFFFF", x_position)

            stat = 100 if stat > 100 else stat

            setattr(self, flavor, stat)

            return

    class GirlClass(object):
        def __init__(self, name, love = 0, ovedience = 0, inhibition = 0, lust = 0):
            self.name = name
            self.tag = name
            self.names = [name]

            self.love = love
            self.obedience = ovedience
            self.inhibition = inhibition
            self.lust = lust

            self.Thirst = 0
            self.addiction = 0
            self.addiction_rate = 0
            self.resistance = 0
            self.Taboo = 0
            self.XP = 0
            self.stat_points = 0
            self.XP_goal = 100
            self.level = 1

            self.sprite_location = stage_center
            self.sprite_layer = 50

            self.remaining_actions = 3
            self.max_actions = 3
            self.pose = 0
            self.reputation = 600
            self.recent_history = []
            self.daily_history = []
            self.traits = []
            self.history = []
            self.Date = 0
            self.Chat = [0, 0, 0, 0, 0, 0]
            self.Event = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            self.player_petname = "Zero"
            self.player_petnames = ["Zero"]
            self.petname = "Girl"
            self.petnames = ["Girl"]

            self.Cheated = 0
            self.Break = [0, 0]
            self.Forced = 0
            self.location = "hold"
            self.home = 0

            self.Outfit = "casual1"
            self.OutfitDay = "casual1"
            self.SeenPeen = 0
            self.SeenChest = 0
            self.SeenPussy = 0
            self.SeenPanties = 0

            self.upskirt = 0
            self.top_pulled_up = 0
            self.underwear_pulled_down = 0
            self.grool = 0
            self.Water = 0
            self.spunk = []
            self.piercings = ""
            self.pubes = "_hairy"
            self.ArmPose = 1

            self.blushing = ""
            self.eyes = "_normal"
            self.mouth = "_normal"
            self.brows = "_normal"
            self.emotion = "_normal"

            self.held_item = 0
            self.arms = ""
            self.legs = ""
            self.top = ""
            self.neck = ""
            self.bra = ""
            self.underwear = ""
            self.accessory = ""
            self.hair = 1
            self.hose = ""
            self.Shame = 0
            self.inventory = []


            self.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            self.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            self.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            self.TempClothes = [0, "", "", "", "", "", "", "", "", "", 0]
            self.Gag = 0
            self.Todo = []
            self.PubeC = 0
            self.Schedule = [["MM", "MA", "ME", "MN"],
                                ["TM", "TA", "TE", "TN"],
                                ["WM", "WA", "WE", "WN"],
                                ["ThM", "ThA", "ThE", "ThN"],
                                ["FM", "FA", "FE", "FN"],
                                ["SaM", "SaA", "SaE", "SaN"],
                                ["SuM", "SuA", "SuE", "SuN"],
                                ]
            self.Clothing = [0, "", "", "", "", "", "", "", "", 0]                    #schedules when she wears what: (0-6) = Mon-Sun, (7) Datewear, (8) Teachingwear, (9) Private

            self.action_counter = {}

            for action in all_actions:
                self.action_counter[action] = 0

            self.event_counter = {"orgasmed": 0, "caught": 0, "sleepover": 0, "ass_slapped": 0,
                "swallowed": 0, "creampied": 0, "anal_creampied": 0,
                "been_with_girl": 0, "seen_with_girl": 0,
                "forced": 0}

            self.session_orgasms = 0
            self.Strip = 0
            self.used_to_anal = 0
            self.Vib = 0
            self.Plug = 0
            self.SEXP = 0
            self.massage_chart = [0, "", "", "", "", "", "", "", "", 0]
            self.player_favorite_action = 0
            self.favorite_action = 0


            if self.tag == "Rogue":
                self.voice = ch_r

                self.Casual1 = [2,"_gloves", "_skirt", "_mesh_top", "_spiked_collar", "_tank", "_black_panties", "", "", "_tights", 0]
                self.Casual2 = [2,"_gloves", "_pants", "_pink_top", "", "_buttoned_tank", "_black_panties", "", "", "", 0]
                self.Gym = [0, "_gloves", "", "_hoodie", "", "_sports_bra", "_shorts", "", "", "",10]
                self.sleepwear = [0, "", "", "", "", "_tank", "_green_panties", "", "", "",20]
                self.Swim = [0, "", "", "_hoodie", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume = [2,"_gloves", "_skirt", "", "", "_tube_top", "_black_panties", "_sweater", "_cosplay", "", 0]




                self.home = "bg_rogue"
                self.hair = "_evo"
                self.LikeKitty = 600
                self.LikeEmma = 500
                self.LikeLaura = 500
                self.Schedule = [["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                        ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                                        ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                        ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                                        ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                        ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"],
                                        ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"],
                                        ]
                self.SexKitty = 0
                self.SexEmma = 0
                self.SexLaura = 0
                self.history = ["met"]
                self.massage_chart = ["shoulders", "arms", "arms", "hands", "hands", "back", "hips", "back", "breasts", "breasts"]
            elif self.tag == "Kitty":
                self.voice = ch_k

                self.Casual1 = [2,0, "capris", "_pink_top", "gold_necklace", "cami", "_green_panties", "", "", "", 0]
                self.Casual2 = [2,0, "black jeans", "red_shirt", "star_necklace", "bra", "_green_panties", "", "", "", 0]
                self.Gym = [0, "", "_shorts", "", "", "_sports_bra", "_green_panties", "", "", "",10]
                self.sleepwear = [0, "", "_shorts", "", "", "cami", "_green_panties", "", "", "",20]
                self.Swim = [0, "", "blue_skirt", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume = [2,0, "dress", "jacket", "flower_necklace", "dress", "lace_panties", "", "", "", 0]
                self.home = "bg_kitty"
                self.hair = "_evo"
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
                                        ["bg_campus", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                        ]
                self.SexRogue = 0
                self.SexEmma = 0
                self.SexLaura = 0
                self.massage_chart = ["shoulders", "back", "hips", "thighs", "calves", "feet", "feet", "hips", "ass", "pussy"]
            elif self.tag == "Emma":
                self.voice = ch_e

                self.Casual1 = [2,0, "_pants", "jacket", "choker", "corset", "white_panties", "", "", "", 0]
                self.Casual2 = [2,"_gloves", "_pants", "", "choker", "corset", "white_panties", "", "", "",5]
                self.Gym = [0, "", "", "", "", "_sports_bra", "sports_panties", "", "", "",10]
                self.sleepwear = [0, "", "", "", "", "corset", "white_panties", "", "", "",25]
                self.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume =  [2,"_gloves", "dress", "dress", "choker", "", "lace_panties", "", "hat", "stockings_and_garterbelt", 0]
                self.home = "bg_emma"
                self.hair = "wavy"
                self.pubes = "_bare"
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
                                        ]
                self.SexRogue = 0
                self.SexKitty = 0
                self.SexLaura = 0
                self.used_to_anal = 2
                self.massage_chart = ["shoulders", "neck", "neck", "back", "hips", "ass", "ass", "back", "breasts", "breasts"]

            elif self.tag == "Laura":
                self.voice = ch_l

                self.Casual1 = [2,"wrists", "leather_pants", "", "leash_choker", "leather_bra", "_black_panties", "", "", "", 0]
                self.Casual2 = [2,0, "_skirt", "jacket", "leash_choker", "leather_bra", "_black_panties", "", "", "", 0]
                self.Gym = [2,"wrists", "leather_pants", "", "", "leather_bra", "_black_panties", "", "", "", 0]
                self.sleepwear = [0, "", "", "", "", "leather_bra", "leather_panties", "", "", "",20]
                self.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume = [2,"_gloves", "other_skirt", "", "", "white_tank", "_black_panties", "suspenders", "", "black stockings", 0]
                self.home = "bg_laura"
                self.hair = "long"
                self.LikeRogue = 500
                self.LikeKitty = 500
                self.LikeEmma = 500
                self.ScentTimer = 0
                self.Claws = 0
                self.Schedule = [["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                        ["bg_dangerroom", "bg_classroom", "bg_campus", "bg_laura"],
                                        ["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                        ["bg_dangerroom", "bg_classroom", "bg_campus", "bg_laura"],
                                        ["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                        ["bg_pool", "bg_laura", "bg_dangerroom", "bg_laura"],
                                        ["bg_pool", "bg_laura", "bg_dangerroom", "bg_laura"],
                                        ]
                self.SexRogue = 0
                self.SexKitty = 0
                self.SexEmma = 0
                self.used_to_anal = 2
                self.massage_chart = ["shoulders", "back", "arms", "hips", "thighs", "calves", "ass", "ass", "pussy", "pussy"]

            elif self.tag == "Jean":
                self.voice = ch_j

                self.StatStore = 0
                self.IX = 500

                self.Casual1 = [2,0, "_pants", "pink_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
                self.Casual2 = [2,0, "_skirt", "green_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
                self.Gym = [0, "", "yoga_pants", "", "", "_sports_bra", "_green_panties", "", "", "", 0]
                self.sleepwear = [0, "", "", "pink_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
                self.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume =  [2,0, "_shorts", "yellow_shirt", "", "green_bra", "_green_panties", "suspenders", "pony", "", 0]
                self.home = "bg_jean"
                self.hair = "short"

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
                                        ]

                self.massage_chart = ["back", "shoulders", "neck", "neck", "back", "hips", "ass", "ass", "pussy", "pussy"]

            elif self.tag == "Storm":
                self.voice = ch_s

                self.Casual1 = [2,0, "_skirt", "white_shirt", "", "black_bra", "white_panties", "", "", "", 0]
                self.Casual2 = [2,0, "_pants", "jacket", "", "_sports_bra", "white_panties", "", "", "", 0]
                self.Gym = [0, "", "yoga_pants", "", "", "_sports_bra", "white_panties", "", "", "",10]
                self.sleepwear = [0, "", "", "white_shirt", "", "", "white_panties", "", "", "",25]
                self.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume = [2,0, "", "", "ring_necklace", "cos_bra", "cos_panties", "rings", "short", "", 0]
                self.home = "bg_storm"
                self.hair = "long"

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
                                        ]

                self.massage_chart = ["feet", "calves", "thighs", "hips", "ass", "ass", "pussy", "ass", "pussy", "pussy"]

            elif self.tag == "Jubes":
                self.voice = ch_v

                self.Casual1 = [2,0, "_shorts", "red_shirt", "", "_sports_bra", "blue_panties", "jacket", "", "", 0]
                self.Casual2 = [2,0, "_pants", "black_shirt", "", "_sports_bra", "blue_panties", "jacket", "", "", 0]
                self.Gym = [0, "", "_pants", "", "", "_sports_bra", "blue_panties", "", "", "",10]
                self.sleepwear = [0, "", "", "", "", "_sports_bra", "blue_panties", "", "", "",25]
                self.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume = [0, "", "_pants", "black_shirt", "", "_sports_bra", "blue_panties", "jacket", "", "", 0]
                self.home = "bg_jubes"
                self.hair = "shades"

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
                                        ]

                self.massage_chart = ["neck", "shoulders", "calves", "feet", "neck", "shoulders", "calves", "feet", "pussy", "pussy"]

            self.change_outfit(Changed=1)

        def Introduction(self):

            if self == RogueX:
                self.player_petname = "Sugar"
                self.player_petnames = ["Sugar",Player.name]
                self.petname = "Rogue"
                self.petnames = ["Rogue"]
            elif self == KittyX:
                self.player_petname = Player.name[:1]
                self.player_petnames = ["sweetie",Player.name[:1],Player.name]
                self.petname = "Kitty"
                self.petnames = ["Kitty"]
            elif self == EmmaX:
                self.names = ["Ms. Frost"]
                self.name = "Ms. Frost"
                self.player_petname = "young man"
                self.player_petnames = ["young man",Player.name]
                self.petname = EmmaX.name
                self.petnames = ["Emma", "Ms. Frost"]
            elif self == LauraX:
                self.player_petname = "guy"
                self.player_petnames = ["guy",Player.name]
                self.petname = "Laura"
                self.petnames = ["Laura", "X-23"]
            elif self.tag == "Jean":
                self.player_petname = "um. . ."
                self.player_petnames = ["um. . ."]
                self.petname = JeanX.name
                self.petnames = ["Jean"]
            elif self.tag == "Storm":
                self.player_petname = "Player.name"
                self.player_petnames = ["Player.name"]
                self.petname = StormX.name
                self.petnames = ["Storm", "Ororo", "Ms. Munroe"]
            elif self.tag == "Jubes":
                self.player_petname = "Bro"
                self.player_petnames = ["Bro", "Player.name"]
                self.petname = JubesX.name
                self.petnames = ["Jubes", "Jubilee"]

            self.change_outfit(6,Changed=1)
            global all_Girls
            if self not in all_Girls:
                all_Girls.append(self)
            Shop_Inventory.extend(["DL", "G", "A"])
            PersonalRooms.append(self.home)

        def SluttyClothes(self):


            if self == RogueX:
                if "stockings_and_garterbelt" in self.inventory:
                    self.Casual1[9] = "stockings_and_garterbelt"
                elif self.inhibition >= 300:
                    self.Casual1[9] = "_stockings"
                else:
                    self.Casual1[9] = "_tights"

                if self.Gym[0] == 0 and self.Gym[5] and self.inhibition >= 300:

                    self.Gym[3] == 0

                if self.Swim[0] == 0 and self.Swim[5] and self.inhibition >= 300:

                    self.Swim[3] == 0
            elif self == KittyX:
                if self.Swim[2] == "blue_skirt" and self.Swim[6] and self.inhibition > 500:

                    self.Swim[2] = 0
            elif self == LauraX:
                if self.inhibition >= 400 and self.Casual2[5] == "leather_bra" and "corset" in self.inventory:
                    self.Casual2[5] = "corset"
                if self.inhibition >= 600 and "lace_panties" in self.inventory:
                    self.Casual2[6] = "lace_panties"
                if self.inhibition >= 600 and "stockings_and_garterbelt" in self.inventory:
                    self.Casual2[9] = "stockings_and_garterbelt"

            elif self == JeanX:
                if "stockings_and_garterbelt" in self.inventory:
                    self.Casual1[9] = "stockings_and_garterbelt"
                elif self.love >= 300:
                    self.Casual1[9] = "_stockings"
                if self.inhibition >= 600 and "_bikini_top" in self.inventory:
                    self.Gym[5] = "_bikini_top" if self.Gym[0] == 1 else self.Gym[5]
                if self.inhibition >= 600 and "lace_bra" in self.inventory:
                    self.Casual1[5] = "lace_bra"
                    self.Casual2[5] = "lace_bra"
                if self.inhibition >= 600 and "lace_panties" in self.inventory:
                    self.Casual1[6] = "lace_panties"
                    self.Casual2[6] = "lace_panties"
            elif self == StormX:
                if self.inhibition >= 400 and self.Casual2[5] == "_sports_bra":
                    self.Casual2[5] = "_tube_top"
                if self.inhibition >= 400 and self.Casual2[5] == "white_panties":
                    self.Casual2[5] = "_black_panties"
                if self.inhibition >= 600 and "lace_panties" in self.inventory:
                    self.Casual2[6] = "lace_panties"
            elif self == JubesX:
                if self.inhibition >= 500 and self.Casual1[3] == "red_shirt":
                    self.Casual1[3] = "_tube_top"
                    self.Casual1[5] = 0
                if self.inhibition >= 600 and "lace_panties" in self.inventory:
                    self.Casual2[6] = "lace_panties"
                if self.inhibition >= 600 and "stockings_and_garterbelt" in self.inventory:
                    self.Casual2[9] = "stockings_and_garterbelt"
            return

        def add_word(self,Only=0,Recent=0,Daily=0,Trait=0,History=0):



            if (Recent and not Only) or (Recent and Recent not in self.recent_history):
                self.recent_history.append(Recent)
            if (Daily and not Only) or (Daily and Daily not in self.daily_history):
                self.daily_history.append(Daily)
            if (Trait and not Only) or (Trait and Trait not in self.traits):
                self.traits.append(Trait)
            if (History and not Only) or (History and History not in self.history):
                self.history.append(History)
            return

        def drain_word(self, word, Recent = 1, Daily = 1, Traits=0):


            if Recent and word in self.recent_history:
                while word in self.recent_history:
                    self.recent_history.remove(word)
            if Daily and word in self.daily_history:
                while word in self.daily_history:
                    self.daily_history.remove(word)
            if Traits and word in self.traits:
                while word in self.traits:
                    self.traits.remove(word)
            return

        def change_stat(self, flavor=0, Check=100, Value=1, Greater=0, Type=0, Alt=[[],0, 0], Overflow=0, BStat=0, x_position = 0.75):





            if self not in all_Girls:
                return

            if self in Alt[0]:

                Check = Alt[1] if Alt[1] else Check
                Value = Alt[2] if Alt[2] else Value

            if flavor == "love" or flavor == "obedience" or flavor == "inhibition":

                Check = Check*10

            Type = getattr(self,flavor)

            Overflow = self.Chat[4]
            x_position = self.sprite_location

            if self.tag == "Jean" and flavor == "inhibition" and self.IX > 0:

                Type -= self.IX

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

            if self.tag == "Jean" and flavor == "inhibition" and self.IX > 0:

                Type += self.IX

            if Value:


                if self.tag == "Jean" and Value > 0:
                    if flavor == "obedience" and self.obedience <= 800 and Check < 800:


                        Value = int(Value/2)
                        Type -= Value
                    elif flavor == "inhibition" and self.IX > 0:
                        if self.Taboo >= 40:

                            Value += Value
                            Type += Value
                        if Type > 1000:

                            self.IX -= (Type - 1000)
                            Type = 1000
                            Value = 0
                        elif Type > 700:

                            self.IX -= int(Value/2)
                        self.IX = 0 if self.IX < 0 else self.IX
                    elif flavor == "love" and Type >= 500 and self.obedience < 700:



                        if self.love < 500:

                            self.love = 500
                            Value = Type - 500




                        self.StatStore += Value

                        if Check > self.obedience:

                            flavor = "obedience"
                            Value = int(Value/5)
                            Type = self.obedience + Value
                        else:
                            Value = 0




                if flavor == "love":
                    Color = "#c11b17"
                elif flavor == "obedience":
                    Color = "#2554c7"
                elif flavor == "inhibition":
                    Color = "#FFF380"
                elif flavor == "lust":
                    Color = "#FAAFBE"
                    CallHolder(Value, Color, x_position)
                    if flavor == "lust" and Type >= 100 and not primary_action:

                        renpy.call("Girl_Cumming",self,1)
                        return
                    Type = 100 if Type > 100 else Type
                    setattr(self,flavor,Type)
                    return

                if Type > 1000:
                    CallHolder((-(Type-1000-Value)), Color, x_position)
                    if not self.Chat[4]:

                        Value = 0
                    else:

                        Value = Type - 1000

                        setattr(self,flavor,1000)
                        if flavor == "love":
                            if self.Chat[4] == 1:
                                flavor = "obedience"
                            elif self.Chat[4] == 2:
                                flavor = "inhibition"
                            else:
                                Value = 0
                        elif flavor == "obedience":
                            if self.Chat[4] == 3:
                                flavor = "inhibition"
                            elif self.Chat[4] == 4:
                                flavor = "love"
                            else:
                                Value = 0
                        elif flavor == "inhibition":
                            if self.Chat[4] == 5:
                                flavor = "obedience"
                            elif self.Chat[4] == 6:
                                flavor = "love"
                            else:
                                Value = 0

                        Type = getattr(self,flavor)
                        Type += Value

                        if flavor == "love":

                            Color = "#c11b17"
                        elif flavor == "obedience":
                            Color = "#2554c7"
                        elif flavor == "inhibition":
                            Color = "#FFF380"
                        else:
                            Color = "#FFFFFF"


                if Value:

                    CallHolder(Value, Color, x_position)



            Type = 1000 if Type > 1000 else Type

            setattr(self,flavor,Type)
            return


        def change_face(self, emotion = 5, B = 5, M = 0, Mouth = 0, Eyes = 0, Brows = 0):



            emotion = self.emotion if emotion == 5 else emotion
            B = self.blushing if B == 5 else B

            if (self.Forced or "_angry" in self.recent_history) and emotion in ("_normal", "_bemused", "_sexy", "_sly", "_smile", "startled"):
                emotion = "_angry"
            elif self.event_counter["forced"] > 0 and emotion in ("_normal", "_bemused", "_sexy", "_sly", "_smile", "startled"):
                emotion = "_sad"

            if emotion == "_normal":
                self.mouth = "_normal"
                self.brows = "_normal"
                self.eyes = "_normal"
            elif emotion == "_angry":
                if self == LauraX:
                    self.mouth = "_kiss"
                else:
                    self.mouth = "_sad"
                self.brows = "_angry"
                self.eyes = "_sexy"
            elif emotion == "_bemused":
                if self == EmmaX:
                    self.mouth = "_normal"
                else:
                    self.mouth = "_lipbite"
                self.brows = "_sad"
                self.eyes = "_squint"
            elif emotion == "_closed":
                if self == RogueX:
                    self.mouth = "_lipbite"
                else:
                    self.mouth = "_normal"
                self.brows = "_sad"
                self.eyes = "_closed"
            elif emotion == "_confused":
                self.mouth = "_kiss"
                self.brows = "_confused"
                if self == LauraX or self == EmmaX:
                    self.eyes = "_squint"
                else:
                    self.eyes = "_surprised"
            elif emotion == "_kiss":
                self.mouth = "_kiss"
                if self == LauraX or self == EmmaX:
                    self.brows = "_sad"
                else:
                    self.brows = "_normal"
                self.eyes = "_closed"
            elif emotion == "_sad":
                self.mouth = "_sad"
                self.brows = "_sad"
                if self == JeanX or self == JubesX:
                    self.eyes = "_normal"
                else:
                    self.eyes = "_sexy"
            elif emotion == "_sadside":
                self.mouth = "_sad"
                self.brows = "_sad"
                self.eyes = "_side"
            elif emotion == "_sexy":
                self.mouth = "_lipbite"
                if self == EmmaX:
                    self.brows = "_normal"
                    self.eyes = "_squint"
                elif self == LauraX:
                    self.brows = "_sad"
                    self.eyes = "_squint"
                else:
                    self.brows = "_normal"
                    self.eyes = "_sexy"
            elif emotion == "_sly":
                self.brows = "_normal"
                self.eyes = "_squint"
                if self == RogueX:
                    self.mouth = "_grimace"
                if self == LauraX:
                    if LauraX.love >= 700:
                        self.mouth = "_smile"
                    else:
                        self.mouth = "_smirk"
                    self.brows = "_confused"
                elif self == KittyX:
                    self.mouth = "_smile"
                else:
                    self.mouth = "_smirk"
            elif emotion == "_smile":
                if self == LauraX and LauraX.love < 700:
                    self.mouth = "_smirk"
                else:
                    self.mouth = "_smile"
                self.brows = "_normal"
                self.eyes = "_normal"
            elif emotion == "_surprised":
                if self == RogueX or self == KittyX:
                    self.mouth = "_surprised"
                else:
                    self.mouth = "_kiss"
                self.brows = "_surprised"
                self.eyes = "_surprised"
            elif emotion == "_oh":
                self.mouth = "_kiss"
                self.brows = "_surprised"
                self.eyes = "_surprised"
            elif emotion == "startled":
                if self == RogueX or self == KittyX:
                    self.mouth = "_grimace"
                else:
                    self.mouth = "_smile"
                self.brows = "_surprised"
                self.eyes = "_surprised"
            elif emotion == "_down":
                if self == RogueX or self == KittyX:
                    self.mouth = "_surprised"
                else:
                    self.mouth = "_sad"
                self.brows = "_sad"
                self.eyes = "_down"
            elif emotion == "_perplexed":
                if self == RogueX:
                    self.mouth = "_sad"
                    self.brows = "_confused"
                else:
                    self.mouth = "_smile"
                    self.brows = "_sad"
                if self == LauraX:
                    self.eyes = "_surprised"
                else:
                    self.eyes = "_normal"
            elif emotion == "_sucking":
                self.mouth = "_sucking"
                if self == EmmaX:
                    self.brows = "_surprised"
                elif self == LauraX:
                    self.brows = "_sad"
                else:
                    self.brows = "_normal"
                self.eyes = "_closed"
            elif emotion == "_tongue":
                self.mouth = "_tongue"
                self.brows = "_sad"
                if self == LauraX:
                    self.eyes = "_stunned"
                else:
                    self.eyes = "_sexy"
            elif emotion == "_manic":
                if self == RogueX:
                    self.mouth = "_grimace"
                elif self == LauraX:
                    self.mouth = "_lipbite"
                else:
                    self.mouth = "_smile"
                self.brows = "_sad"
                self.eyes = "_manic"
                self.blushing = "_blush1"

            if M:
                self.eyes = "_manic"
            if B > 1:
                self.blushing = "_blush2"
            elif B:
                self.blushing = "_blush1"
            else:
                self.blushing = ""

            if Mouth:
                self.mouth = Mouth
            if Eyes:
                self.eyes = Eyes
            if Brows:
                self.brows = Brows
            return


        def DefaultFaces(self):



            if self.lust >= 50 and approval_check(self, 1200):
                self.emotion = "_sexy"
            elif self.addiction > 75:
                self.emotion = "_manic"
            elif self.love >= self.obedience and self.love >= 500:
                self.emotion = "_smile"
            elif self.inhibition >= self.obedience and self.inhibition >= 500:
                self.emotion = "_smile"
            elif self.addiction > 50:
                self.emotion = "_manic"
            elif (self.love + self.obedience) < 300:
                self.emotion = "_angry"
            else:
                self.emotion = "_normal"
            return

        def lust_face(self,Extreme=0,Kissing=0):
            if self.Thirst >= 80:
                self.lust += 2
            elif self.Thirst >= 50:
                self.lust += 1

            if self.lust >= 80:
                self.blushing = "_blush2"
            elif self.lust >= 40:
                self.blushing = "_blush1"

            if self.lust >= 80:
                self.grool = 2
            elif self.lust >= 50:
                self.grool = 1

            if girl_offhand_action == "kiss both" or girl_offhand_action == "kiss girl":

                Kissing = 1
            elif second_girl_primary_action == "kiss both" or girl_offhand_action == "kiss girl":

                Kissing = 1
            elif Partner != self:

                if primary_action == "kiss" or offhand_action == "kiss":
                    Kissing = 1
            elif second_girl_primary_action == "kiss":

                Kissing = 1

            if Kissing:
                self.eyes = "_closed"
                if self.tag == "Emma":
                    self.mouth = "_kiss"
                elif self.action_counter["kiss"] >= 10 and self.inhibition >= 300:
                    self.mouth = "_sucking"
                elif self.action_counter["kiss"] > 1 and self.addiction >= 50:
                    self.mouth = "_sucking"
                else:
                    self.mouth = "_kiss"
            else:

                if self.lust >= 90:
                    self.eyes = "_closed"
                    self.brows = "_sad"
                    self.mouth = "_surprised"
                elif self.lust >= 70 or Extreme:
                    self.eyes = "_sexy"
                    self.brows = "_sad"
                    self.mouth = "_lipbite"
                elif self.lust >= 50:
                    if self.tag == "Emma" or self.tag == "Laura":
                        self.eyes = "_squint"
                    else:
                        self.eyes = "_sexy"
                    self.brows = "_sad"
                    self.mouth = "_lipbite"
                elif self.lust >= 30:
                    self.eyes = "_sexy"
                    self.brows = "_normal"
                    if self.tag == "Emma" or self.tag == "Laura":
                        self.mouth = "_smirk"
                    else:
                        self.mouth = "_kiss"
                else:
                    self.eyes = "_sexy"
                    self.brows = "_normal"
                    if self.tag == "Emma" or self.tag == "Laura":
                        self.mouth = "_smirk"
                    else:
                        self.mouth = "_normal"
                if self.tag == "Laura" and self.lust < 50 and not Extreme and not approval_check(self, 1000):
                    self.eyes = "_side"

            if Partner == self and second_girl_primary_action in ("eat_pussy", "eat_ass", "blowjob", "suck_breasts"):
                self.mouth = "_tongue"
            elif girl_offhand_action in ("eat_pussy", "eat_ass", "suck_breasts"):
                self.mouth = "_tongue"

            if self.session_orgasms >= 10:

                self.eyes = "_stunned"
                self.mouth = "_tongue"

            if not self.used_to_anal:

                if Partner != self and (primary_action == "anal" or primary_action == "dildo_anal" or girl_offhand_action == "dildo_anal"):
                    self.eyes = "_closed"
                    self.brows = "_angry"

            if "unseen" in self.recent_history:
                self.eyes = "_closed"
            if Partner and self != Partner:
                Partner.lust_face()
            return



        def change_outfit(self, OutfitTemp = 5, Spunk = 0, Undressed = 0, Changed = 1,HolderOutfit=[]):



            if self not in all_Girls:
                return

            OutfitTemp = OutfitTemp if OutfitTemp else self.Outfit

            if self.location == bg_current and renpy.showing("NightMask", layer='nightmask') and time_index == 0:

                return

            if self.location not in ("bg_showerroom", "bg_pool") or (OutfitTemp not in ("nude", "swimwear", "_towel")):

                self.Water = 0
            if self.spunk:

                if "painted" not in self.daily_history or "cleaned" not in self.daily_history:
                    del self.spunk[:]


            if self.upskirt or self.top_pulled_up or self.underwear_pulled_down:
                Undressed = 1

            self.upskirt = 0
            self.top_pulled_up = 0
            self.underwear_pulled_down = 0

            if OutfitTemp == 5:

                if "yoinked" in self.recent_history:

                    return
                OutfitTemp = self.Outfit
            elif OutfitTemp == 6:

                OutfitTemp = self.OutfitDay
                self.Outfit = self.OutfitDay
            if OutfitTemp != self.Outfit:


                Changed = 1
                self.Outfit = OutfitTemp
            if self in Party and OutfitTemp == self.OutfitDay:

                OutfitTemp = self.Outfit

            if OutfitTemp == "casual1":
                HolderOutfit = self.Casual1[:]
            elif OutfitTemp == "casual2":
                HolderOutfit = self.Casual2[:]
            elif OutfitTemp == "nude":
                HolderOutfit = [0, "", "", "", "", "", "", "", "", "",50]
            elif OutfitTemp == "_towel":
                HolderOutfit = [0, "", "", "_towel", "", "", "", "", "", "",35]
            elif OutfitTemp == "custom1":
                HolderOutfit = self.Custom1[:]
            elif OutfitTemp == "custom2":
                HolderOutfit = self.Custom2[:]
            elif OutfitTemp == "custom3":
                HolderOutfit = self.Custom3[:]
            elif OutfitTemp == "temporary":
                HolderOutfit = self.TempClothes[:]
            elif OutfitTemp == "sleep":
                HolderOutfit = self.sleepwear[:]
            elif OutfitTemp == "gym":
                HolderOutfit = self.Gym[:]
            elif OutfitTemp == "costume":
                HolderOutfit = self.Costume[:]
            elif OutfitTemp == "swimwear":
                if not self.Swim[0]:
                    if "_bikini_top" not in self.inventory or "_bikini_bottoms" not in self.inventory:
                        self.Outfit = self.OutfitDay

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
                    elif self == KittyX and "blue_skirt" not in self.inventory and self.inhibition <= 400:
                        self.Outfit = self.OutfitDay
                        if "swim" not in self.daily_history:
                            ch_k("I don't know, I do have a suit, but it's a little daring. . .", interact=True)
                            ch_k("If only I had a little skirt or something. . .", interact=True)
                        return 0
                    else:
                        self.Swim[0] = 1
                HolderOutfit = self.Swim[:]

            while len(HolderOutfit) < 11:
                HolderOutfit.append(0)

            if not self.legs and HolderOutfit[2]:
                Undressed = 1
            elif not self.top and HolderOutfit[3]:
                Undressed = 1
            elif not self.bra and HolderOutfit[5]:
                Undressed = 1
            elif not self.underwear and HolderOutfit[6] and "pantyless" not in self.daily_history:
                Undressed = 1
            elif not self.hose and HolderOutfit[9]:
                Undressed = 1



            if self == EmmaX and (HolderOutfit[8] != "hat" and HolderOutfit[8] != "hat wet"):

                self.hair = "wet" if HolderOutfit[8] == "hat wet" else "wave"

            self.arms = HolderOutfit[1]
            self.legs = HolderOutfit[2]
            self.top = HolderOutfit[3]
            self.neck = HolderOutfit[4]
            self.bra = HolderOutfit[5]
            self.underwear = HolderOutfit[6]
            self.accessory = HolderOutfit[7]
            self.hair = HolderOutfit[8] if HolderOutfit[8] else self.hair
            self.hose = HolderOutfit[9]
            self.Shame = HolderOutfit[10]

            if "ripped" in self.daily_history and "modesty" not in self.recent_history:

                self.hose = "ripped_pantyhose" if self.hose == "pantyhose" else self.hose
                self.hose = "ripped_tights" if self.hose == "_tights" else self.hose
            if self.underwear and self.underwear != "_shorts" and "pantyless" in self.daily_history and "modesty" not in self.daily_history:

                if OutfitTemp != "sleep" and OutfitTemp != "gym":
                    self.underwear = ""



            if not Changed and OutfitTemp == self.Outfit and self.location == bg_current:

                if Undressed == 2:
                    renpy.say(None,self.name+" throws on a towel.", interact=True)
                elif Undressed:
                    renpy.say(None,self.name+" throws her clothes back on.", interact=True)
            if Undressed:
                return 2
            return 1




        def Set_Temp_Outfit(self):


            self.TempClothes[1] = self.arms
            self.TempClothes[2] = self.legs
            self.TempClothes[3] = self.top
            self.TempClothes[4] = self.neck
            self.TempClothes[5] = self.bra
            self.TempClothes[6] = self.underwear
            self.TempClothes[7] = self.accessory
            self.TempClothes[8] = self.hair
            self.TempClothes[9] = self.hose
            self.TempClothes[0] = 1



            self.Outfit = "temporary"
            self.OutfitDay = "temporary"
            return

        def ChestNum(self,Up=1):

            if Up and self.top_pulled_up and self.bra:
                return 1
            if self == RogueX:
                if self.bra in ("_tank", "_buttoned_tank"):
                    return 5
            if self == LauraX:
                if self.bra in ("leather_bra", "white_tank"):
                    return 5
                elif self.bra == "wolvie_top":
                    return 3
            if self == JeanX:
                if self.bra == "_sports_bra":
                    return 5
            if self == StormX:
                if self.bra == "_sports_bra":
                    return 5
            if self.bra == "_tube_top":
                return 5
            if self.bra == "lace_bra":
                return 2
            if self.bra == "lace corset":
                return 2
            if self.bra == "corset":
                return 5
            if self.bra:
                return 3
            if self.accessory == "suspenders" or self.accessory == "suspenders2":
                return 2

            return 0

        def OverNum(self,Up=1):

            if Up and self.top_pulled_up and self.top:
                return 1
            if self == RogueX:
                if self.top == "_mesh_top":
                    return 2
            if self == EmmaX:
                if self.top == "_towel":
                    return 2
            if self == StormX:
                if self.top == "_towel":
                    return 0
            if self == JubesX:
                if Up and self.top_pulled_up and self.accessory:
                    return 1
                if self.accessory == "jacket":
                    return 3
                if self.accessory == "open_jacket":
                    return 1
                if self.accessory == "shut_jacket":
                    return 5
            if self.top == "_towel":
                return 3
            if self.top == "dress":
                return 4
            if self.top == "jacket":
                return 4
            if self.top == "nighty":
                return 3
            if self.top == "_pink_top":
                return 4
            if self.top:
                return 5

            return 0

        def PantsNum(self,Up=1):



            if self == JubesX:
                if self.accessory == "shut_jacket":
                    return 5

            if Up and self.upskirt and self.legs:
                return 1

            if self == RogueX and self.underwear == "_shorts":
                return 6
            if self.legs == "_shorts":
                return 6
            if self.legs in ("_skirt", "blue_skirt", "other_skirt", "dress"):
                return 5
            if self.legs == "yoga_pants":
                return 8
            if self.top == "_towel" and self not in (EmmaX,StormX):
                return 5
            if self == EmmaX and self.top == "dress":
                return 4
            if self.legs == "mesh_pants":
                return 2
            if self.legs:
                return 10


            return 0

        def PantiesNum(self,Up=1):

            if Up and self.underwear_pulled_down and self.underwear:
                return 1
            if self.underwear == "lace_panties":
                return 2
            if self.underwear == "sports_panties" or self.underwear == "_shorts":
                return 8
            if self.underwear == "_bikini_bottoms":
                return 7
            if self.underwear:
                return 4
            return 0

        def HoseNum(self,Up=1):

            if Up and self.hose and (self.underwear_pulled_down or self.upskirt):
                return 1
            if self.hose == "_stockings":
                return 1
            if self.hose == "pantyhose":
                return 6
            if self.hose == "_tights":
                return 10
            if self.hose == "stockings and gaterbelt":
                return 4
            if self.hose == "ripped_pantyhose":
                return 4
            if self.hose == "ripped_tights":
                return 4

            return 0

        def ClothingCheck(self,C = 0):
            C = 0

            if self.OverNum() >= 5:
                C += 1
            if self.bra:
                C += 1
            if self.legs:
                C += 1
            if self.HoseNum() >= 5:
                C += 1
            if self.underwear:
                C += 1
            return C

        def ModestyCheck(self, Check=0,C = 0):
            C = 0


            if Check == 2:
                pass
            elif self.OverNum() >= 3:
                pass
            elif self.ChestNum() >= 3:
                pass
            else:
                C += 1

            if Check == 1:
                pass
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




            if not self.SeenChest:
                if (not self.top and not self.bra) or self.top_pulled_up or Check == 1 or Check == 2:
                    C += 1
            if not self.SeenPussy:
                if Check == 1 or Check == 3:
                    C += 1
                elif not self.legs or self.upskirt:

                    if self.underwear_pulled_down or (self.HoseNum() < 5 and not self.underwear):

                        C += 1
            return C




        def GirlLikeCheck(self,Chr=0):

            return getattr(self,"Like"+Chr.tag)

        def GirlLikeUp(self,Chr=0,Value=0,Like=0):

            if "Jeaned" in self.traits:

                Like = getattr(JeanX,"LikeS"+self.tag)
                if Like + Value > 1000:
                    setattr(JeanX,"LikeS"+self.tag, 1000)
                elif Like + Value < 0:
                    setattr(JeanX,"LikeS"+self.tag, 0)
                else:
                    setattr(JeanX,"LikeS"+self.tag, Value + Like)
                return

            Like = getattr(self,"Like"+Chr.tag)
            if Like + Value > 1000:
                setattr(self,"Like"+Chr.tag, 1000)
            elif Like + Value < 0:
                setattr(self,"Like"+Chr.tag, 0)
            else:
                setattr(self,"Like"+Chr.tag, Value + Like)
            return

        def GLG(self, ChrB = 0, Check=200, Modifier = 1, Auto = 0, Jealousy = 0, Ok = 0, Likes=0):









            if self not in all_Girls or ChrB not in all_Girls:
                return
            Jealousy = 0
            Likes = self.GirlLikeCheck(ChrB)


            if Likes <= Check:

                if Auto:

                    setattr(self,"Like"+ChrB.tag,Likes+Modifier)
                    self.change_stat("lust", 200, (int(Modifier/5)))
                    return


                if self in Player.Harem:

                    if ChrB not in Player.Harem and "poly " + ChrB.tag not in self.traits:

                        Jealousy = 100
            elif Auto:
                self.change_stat("lust", 200, (int(Modifier/5)))
                return


            Jealousy += (self.love - 600) if self.love > 600 else 0

            Jealousy += self.SEXP if self.inhibition <= 500 else 0

            Jealousy -= (self.obedience - 250) if self.obedience > 250 else 0



            Jealousy = 0 if Jealousy < 1 else Jealousy

            Modifier += 1 if not Jealousy and Likes >= 500 else 0



            if Likes >= 900:

                Likes += Modifier
                self.change_stat("love", 80, (int(Modifier/2)))
                self.change_stat("lust", 200, (int(Modifier/5)))
                Ok = 2
            elif Likes >= 800:

                if Jealousy <= 300:
                    Likes += Modifier
                    self.change_stat("love", 80, (int(Modifier/2)))
                    self.change_stat("lust", 200, (int(Modifier/2)))
                    Ok = 2
                else:
                    Likes -= Modifier
                    self.change_stat("lust", 200, (int(Modifier/5)))
                    Ok = 1
            elif Likes >= 600:

                if Jealousy <= 100:
                    Likes += Modifier
                    self.change_stat("love", 80, (int(Modifier/4)))
                    self.change_stat("lust", 200, (int(Modifier/2)))
                    Ok = 2
                elif Jealousy <= 300:
                    Likes -= Modifier
                    self.change_stat("lust", 200, (int(Modifier/2)))
                    Ok = 1
                else:
                    Likes -= (Modifier + (int(Jealousy/50)))
                    self.change_stat("love", 90, (-(int(Modifier))))
                    self.change_stat("lust", 200, (int(Modifier/5)))
                    Ok = 2
            elif Likes >= 400:

                if Jealousy <= 100:
                    Likes -= Modifier
                    Ok = 1
                else:
                    Likes -= (Modifier + (int(Jealousy/100)))
                self.change_stat("lust", 200, (int(Modifier/10)))
            else:

                Likes -= (Modifier + (int(Jealousy/50)))
                self.change_stat("lust", 200, (int(Modifier/10)))
            self.change_stat("inhibition", 60, (int(Modifier/10)))



            setattr(self,"Like"+ChrB.tag,Likes+Modifier)

            return Ok




        def nameCheck(self, counter = 0):



            if self.petname == self.name:
                return 0
            if self.Taboo:

                counter = int(self.Taboo/10)


            if self.petname in ("girl", "boo", "bae", "baby", "sweetie"):
                if approval_check(self, 500, "L", TabM=1,Alt=[[LauraX],600]):
                    self.change_stat("love", 80, 1)
                else:
                    self.change_stat("love", 50, -1)
                    return 1
            elif self.petname in ("_sexy", "lover", "beloved"):
                if approval_check(self, 900, TabM=1,Alt=[[LauraX],1100]):
                    self.change_stat("love", 80, 2)
                    self.change_stat("obedience", 80, 1)
                    self.change_stat("inhibition", 70, 1)
                else:
                    self.change_stat("love", 50, (-1-counter))
                    self.change_stat("obedience", 50, 1)
                    self.change_stat("inhibition", 20, -1)
                    return 1

            elif self.petname == "slave":
                if approval_check(self, 800, "O", TabM=3,Alt=[[EmmaX,StormX],900]):
                    self.change_stat("lust", 90, (3+counter))
                    self.change_stat("obedience", 95, (2+counter))
                    self.change_stat("inhibition", 30, 1)
                    self.change_stat("inhibition", 70, 1)
                elif approval_check(self, 500, "O", TabM=3,Alt=[[EmmaX,StormX],600]):
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
            elif self.petname == "pet":
                if approval_check(self, 1500, TabM=2,Alt=[[LauraX],800]):
                    self.change_stat("lust", 90, (3+counter))
                    self.change_stat("obedience", 95, (2+counter))
                    self.change_stat("inhibition", 30, 1)
                    self.change_stat("inhibition", 70, 1)
                elif approval_check(self, 1200, TabM=2,Alt=[[LauraX],650]):
                    self.change_stat("lust", 60, 1)
                    self.change_stat("obedience", 80, 2)
                    self.change_stat("inhibition", 70, 1)
                else:
                    self.change_stat("love", 200, -2)
                    self.change_stat("love", 50, -1, 1)
                    self.change_stat("obedience", 50, 1)
                    self.change_stat("inhibition", 50, -1)
                    return 1
            elif self.petname == "slut":
                if approval_check(self, 500, "O", TabM=2) or approval_check(self, 500, "I", TabM=2,Alt=[[LauraX],400]):
                    self.change_stat("lust", 90, (4+counter))
                    self.change_stat("obedience", 95, (2+counter))
                    self.change_stat("inhibition", 40, 2)
                    self.change_stat("inhibition", 80, 1)
                elif approval_check(self, 300, "O", TabM=2) or approval_check(self, 300, "I", TabM=2,Alt=[[LauraX],200]):
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
            elif self.petname == "whore":
                if approval_check(self, 600, "O", TabM=2,Alt=[[EmmaX],700]) or approval_check(self, 600, "I", TabM=2,Alt=[[LauraX],400]):
                    self.change_stat("lust", 90, 4)
                    self.change_stat("obedience", 95, 2)
                    self.change_stat("inhibition", 50, 2)
                    self.change_stat("inhibition", 80, 1)
                elif approval_check(self, 400, "O", TabM=2,Alt=[[EmmaX],500]) or approval_check(self, 400, "I", TabM=2):
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
            elif self.petname == "sugartits":
                if approval_check(self, 1500, TabM=1,Alt=[[EmmaX],1300]):
                    self.change_stat("obedience", 80, 1)
                    self.change_stat("obedience", 50, 2)
                    self.change_stat("inhibition", 70, 1,Alt=[[EmmaX],70,2])
                    self.change_stat("inhibition", 30, 2,Alt=[[KittyX],60,3])
                else:
                    self.change_stat("love", 200, (-2-counter))
                    self.change_stat("love", 50, (-1-counter))
                    self.change_stat("obedience", 50, 1)
                    self.change_stat("inhibition", 20, -1)
                    return 1
            elif self.petname == "sex friend":
                if approval_check(self, 750, "O", TabM=1) or approval_check(self, 600, "I", TabM=1):
                    self.change_stat("lust", 90, 3)
                    self.change_stat("obedience", 95, 2)
                    self.change_stat("inhibition", 40, 2)
                    self.change_stat("inhibition", 80, 1)
                elif approval_check(self, 600, "O", TabM=1) or approval_check(self, 400, "I", TabM=1):
                    self.change_stat("lust", 90, 2)
                    self.change_stat("love", 200, (-1-counter))
                    self.change_stat("obedience", 80, 1)
                    self.change_stat("inhibition", 70, 1)
                    self.blushing = "_blush1"
                else:
                    self.change_stat("love", 200, -counter)
                    self.change_stat("love", 50, (-1-counter), 1)
                    self.change_stat("obedience", 50, 1)
                    self.change_stat("inhibition", 20, -1)
                    return 1
            elif self.petname == "fuckbuddy":
                if approval_check(self, 700, "O", TabM=2) or approval_check(self, 700, "I", TabM=1):
                    self.change_stat("lust", 90, 3)
                    self.change_stat("obedience", 95, 2)
                    self.change_stat("inhibition", 40, 2)
                    self.change_stat("inhibition", 85, 1)
                elif approval_check(self, 600, "O", TabM=2) or approval_check(self, 500, "I", TabM=1):
                    self.change_stat("lust", 90, 2)
                    self.change_stat("love", 200, (-1-counter))
                    self.change_stat("obedience", 80, 1)
                    self.change_stat("inhibition", 70, 1)
                    self.blushing = "_blush1"
                else:
                    self.change_stat("love", 200, -counter)
                    self.change_stat("love", 60, (-2-counter), 1)
                    self.change_stat("obedience", 60, 1)
                    self.change_stat("inhibition", 20, -1)
                    return 1
            elif self.petname in ("baby girl", "mommy"):
                if approval_check(self, 1200, TabM=1):
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

            elif self.petname == "chere":
                if approval_check(self, 600, "L", TabM=1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)
                    return 1

            elif self.petname == "kitten":
                if approval_check(self, 600, "L", TabM=1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)
                    return 1

            elif self.petname == "darling":
                if approval_check(self, 600, "L", TabM=1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)
                    return 1

            elif self.petname == "Wolvie":
                if approval_check(self, 500, "I", TabM=1):
                    self.change_stat("love", 80, 1)
                else:
                    self.change_stat("love", 50, -1)
                    return 1
            elif self.petname == "X-23":
                if approval_check(self, 800, "O"):
                    self.change_stat("lust", 90, 3)
                    self.change_stat("love", 90, -1)
                    self.change_stat("obedience", 95, 2)
                elif approval_check(self, 700, "L") and not approval_check(self, 500, "O"):
                    self.change_stat("love", 200, -2)
                    self.change_stat("love", 50, -1, 1)
                    self.change_stat("obedience", 30, 2)
                    self.change_stat("obedience", 50, 2)
                    self.change_stat("inhibition", 50, -1)
                    return 1
            return 0







label EmotionEditor(Chr=0):

    while True:
        menu:
            "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":
                menu:
                    "Normal":
                        $ Chr.emotion = "_normal"
                    "Angry":
                        $ Chr.emotion = "_angry"
                    "Smiling":
                        $ Chr.emotion = "_smile"
                    "Sexy":
                        $ Chr.emotion = "_sexy"
                    "Suprised":
                        $ Chr.emotion = "_surprised"
                    "Bemused":
                        $ Chr.emotion = "_bemused"
                    "Manic":
                        $ Chr.emotion = "_manic"
            "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":

                menu:
                    "Sad":
                        $ Chr.emotion = "_sad"
                    "Sucking":
                        $ Chr.emotion = "_sucking"
                    "kiss":
                        $ Chr.emotion = "kiss"
                    "Tongue":
                        $ Chr.emotion = "_tongue"
                    "_confused":
                        $ Chr.emotion = "_confused"
                    "Closed":
                        $ Chr.emotion = "_closed"
                    "Down":
                        $ Chr.emotion = "_down"
            "Emotions3: Sadside Startled Perplexed Sly":

                menu:
                    "Sadside":
                        $ Chr.emotion = "_sadside"
                    "Startled":
                        $ Chr.emotion = "startled"
                    "Perplexed":
                        $ Chr.emotion = "_perplexed"
                    "Sly":
                        $ Chr.emotion = "_sly"
            "Toggle Mouth Spunk":

                if "mouth" in Chr.spunk:
                    $ Chr.spunk.remove("mouth")
                else:
                    $ Chr.spunk.append("mouth")
            "Toggle hand Spunk":
                if "handjob" in Chr.spunk:
                    $ Chr.spunk.remove("handjob")
                else:
                    $ Chr.spunk.append("handjob")
            "Toggle Facial Spunk":

                if "facial" in Chr.spunk and "hair" not in Chr.spunk:
                    $ Chr.spunk.append("hair")
                elif "facial" in Chr.spunk:
                    $ Chr.spunk.remove("facial")
                    $ Chr.spunk.remove("hair")
                else:
                    $ Chr.spunk.append("facial")
            "Blush":

                if Chr.blushing == "_blush2":
                    $ Chr.blushing = ""
                elif Chr.blushing:
                    $ Chr.blushing = "_blush2"
                else:
                    $ Chr.blushing = "_blush1"
            "Exit.":
                return
        $ Chr.change_face()


label WardrobeEditor(Chr=0):
    while True:
        menu Wardrobe_Menu:
            "View" if True:
                while True:
                    menu:
                        "Default":
                            call expression Chr.tag + "_Pos_Reset" pass (0)
                        "Face":
                            call expression Chr.tag + "_Kissing_Launch" pass (0)
                        "Body":
                            call expression Chr.tag + "_Pussy_Launch" pass (0)
                        "Face Low":
                            call Storm_Hide
                            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(StormX.sprite_location)
                            show Storm_Sprite zorder StormX.sprite_layer at sprite_location(stage_center):
                                ease 0.5 offset (100,200) zoom 1.5 alpha 1
                        "BJ":

                            if not renpy.showing(Chr.tag+"_BJ_Animation"):
                                call expression Chr.tag + "_BJ_Launch"
                            else:
                                call expression Chr.tag + "_BJ_Reset"
                        "HJ":
                            if not renpy.showing(Chr.tag+"_HJ_Animation"):
                                call expression Chr.tag + "_HJ_Launch"
                            else:
                                call expression Chr.tag + "_HJ_Reset"
                        "TJ":
                            if not renpy.showing(Chr.tag+"_TJ_Animation"):
                                call expression Chr.tag + "_TJ_Launch"
                            else:
                                call expression Chr.tag + "_TJ_Reset"
                        "Doggy" if Chr == RogueX:
                            $ Chr.pose = "doggy"
                            if not renpy.showing(Chr.tag+"_Doggy"):
                                call expression Chr.tag + "_Sex_Launch"
                            else:
                                call expression Chr.tag + "_Sex_Reset"
                        "Sexpose" if Chr != RogueX:
                            if not renpy.showing(Chr.tag+"_SexSprite"):
                                call expression Chr.tag + "_Sex_Launch"
                            else:
                                call expression Chr.tag + "_Sex_Reset"
                        "Back":
                            jump Wardrobe_Menu
            "First casual outfit":


                $ Chr.change_outfit("casual1")
            "Second casual outfit":

                $ Chr.change_outfit("casual2")
            "Nude":

                $ Chr.change_outfit("nude")
            "Shirts":
                while True:
                    menu:

                        "Remove [Chr.top]" if Chr.top:
                            $ Chr.top = ""
                        "Add mesh_top" if Chr == RogueX:
                            $ Chr.top = "_mesh_top"
                            $ Chr.neck = "_spiked_collar"
                            $ Chr.arms = "_gloves"
                            if Chr.bra == "_buttoned_tank":
                                $ Chr.bra = "_tank"
                        "Add pink_top" if Chr == RogueX:
                            $ Chr.top = "_pink_top"
                            $ Chr.arms = "_gloves"
                        "Add pink_top" if Chr == KittyX:
                            $ Chr.top = "_pink_top"
                        "Add red_top" if Chr == KittyX or Chr == JubesX:
                            $ Chr.top = "red_shirt"
                        "Add black_top" if Chr == JubesX:
                            $ Chr.top = "black_shirt"
                        "Add tube_top" if Chr == JubesX:
                            $ Chr.top = "_tube_top"
                        "Add pink_shirt" if Chr == JeanX:
                            $ Chr.top = "pink_shirt"
                        "Add green_shirt" if Chr == JeanX:
                            $ Chr.top = "green_shirt"
                        "Add yellow_shirt" if Chr == JeanX:
                            $ Chr.top = "yellow_shirt"
                        "Add_jacket":
                            if Chr == JubesX:
                                $ Chr.accessory = "jacket"
                            else:
                                $ Chr.accessory = "jacket"
                        "Open/shut_jacket" if Chr == JubesX:
                            if Chr.accessory == "jacket":
                                $ Chr.accessory = "shut_jacket"
                            else:
                                $ Chr.accessory = "jacket"
                        "wide open_jacket" if Chr == JubesX:
                            if Chr.accessory == "jacket":
                                $ Chr.accessory = "open_jacket"
                            else:
                                $ Chr.accessory = "jacket"
                        "Remove_jacket" if Chr.accessory == "jacket":
                            $ Chr.accessory = ""

                        "Add white_shirt" if Chr == StormX:
                            $ Chr.top = "white_shirt"
                        "Dress" if Chr == EmmaX:
                            $ Chr.top = "dress"
                        "Add nighty":
                            $ Chr.top = "nighty"
                            $ Chr.arms = ""
                        "Add towel":
                            $ Chr.top = "_towel"
                            $ Chr.arms = ""
                        "Toggle Pierce":
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
                        "Toggle up-top":
                            if Chr.top_pulled_up:
                                $ Chr.top_pulled_up = 0
                            else:
                                $ Chr.top_pulled_up = 1
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Back":
                            jump Wardrobe_Menu
            "Bra":
                while True:
                    menu:

                        "Remove [Chr.bra]" if Chr.bra:
                            $ Chr.bra = ""
                        "Add tank_top" if Chr == RogueX:
                            $ Chr.bra = "_tank"
                        "Add sports_bra":
                            $ Chr.bra = "_sports_bra"
                        "Add leather_bra" if Chr == LauraX:
                            $ Chr.bra = "leather_bra"
                        "Add white_tank" if Chr == LauraX:
                            $ Chr.bra = "white_tank"
                        "Add buttoned tank_top" if Chr == RogueX:
                            $ Chr.bra = "_buttoned_tank"
                        "Add lace_bra":
                            $ Chr.bra = "lace_bra"
                        "Add cami" if Chr == KittyX:
                            $ Chr.bra = "cami"
                        "Add dress" if Chr == KittyX:
                            $ Chr.bra = "dress"
                        "Add wolvie_top" if Chr == LauraX:
                            $ Chr.bra = "wolvie_top"
                        "Add green_bra" if Chr == JeanX:
                            $ Chr.bra = "green_bra"
                        "Add tube_top" if Chr == StormX or Chr == RogueX:
                            $ Chr.bra = "_tube_top"
                        "Add_bra":
                            if Chr == StormX:
                                $ Chr.bra = "black_bra"
                            else:
                                $ Chr.bra = "bra"
                        "Add cosplay_bra" if Chr == StormX:
                            $ Chr.bra = "cos_bra"
                        "Add bikini":
                            $ Chr.bra = "_bikini_top"
                        "Add corset":
                            $ Chr.bra = "corset"
                        "Add lace corset":
                            $ Chr.bra = "lace corset"
                        "Toggle up-top":
                            if Chr.top_pulled_up:
                                $ Chr.top_pulled_up = 0
                            else:
                                $ Chr.top_pulled_up = 1
                        "Toggle Piercings":
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Back":
                            jump Wardrobe_Menu
            "Pants":

                while True:
                    menu:

                        "Remove legs" if Chr.legs:
                            $ Chr.legs = ""
                        "Add Skirt" if Chr != KittyX:
                            $ Chr.legs = "_skirt"
                        "Add cosplay Skirt" if Chr == LauraX:
                            $ Chr.legs = "other_skirt"
                        "Add blue Skirt" if Chr == KittyX:
                            $ Chr.legs = "blue_skirt"
                        "Add_pants" if Chr != KittyX:
                            $ Chr.legs = "_pants"
                        "Add black jeans" if Chr == KittyX:
                            $ Chr.legs = "black jeans"
                        "Add capri_pants" if Chr == KittyX:
                            $ Chr.legs = "capris"
                        "Add_shorts" if Chr == KittyX or Chr == JeanX or Chr == JubesX:
                            $ Chr.legs = "_shorts"
                        "Add leather_pants" if Chr == LauraX:
                            $ Chr.legs = "leather_pants"
                        "Add yoga_pants":
                            $ Chr.legs = "yoga_pants"
                        "Dress" if Chr == EmmaX or Chr == KittyX:
                            $ Chr.legs = "dress"
                        "Boots" if Chr == EmmaX:
                            $ EmmaX.accessory = "thigh boots" if EmmaX.accessory != "thigh boots" else 0
                        "Toggle upskirt":
                            if Chr.upskirt:
                                $ Chr.upskirt = 0
                            else:
                                $ Chr.upskirt = 1
                        "pull down-up_panties":
                            if Chr.underwear_pulled_down:
                                $ Chr.underwear_pulled_down = 0
                            else:
                                $ Chr.underwear_pulled_down = 1
                        "Toggle Pierce":
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
                        "Toggle Wetness":
                            if not Chr.grool:
                                $ Chr.grool = 1
                            elif Chr.grool == 1:
                                $ Chr.grool = 2
                            else:
                                $ Chr.grool  = 0
                        "Back":
                            jump Wardrobe_Menu
            "Panties & Hose":

                while True:
                    menu:
                        "Hose":

                            menu:
                                "Add hose":
                                    $ Chr.hose = "_stockings"
                                "Add garter":
                                    $ Chr.hose = "garterbelt"
                                "Add stockings and garter":
                                    $ Chr.hose = "stockings_and_garterbelt"
                                "Add_pantyhose":
                                    $ Chr.hose = "pantyhose"
                                "Add_tights":
                                    $ Chr.hose = "_tights"
                                "Add ripped hose":
                                    $ Chr.hose = "ripped_pantyhose"
                                "Add ripped_tights":
                                    $ Chr.hose = "ripped_tights"
                                "Add_tights":
                                    $ Chr.hose = "_tights"
                                "Add knee stockings" if Chr == KittyX:
                                    $ Chr.hose = "knee stockings"
                                "Add socks" if Chr == JubesX:
                                    $ Chr.hose = "socks"
                                "Add black stockings" if Chr == LauraX:
                                    $ Chr.hose = "black stockings"
                                "Remove hose" if Chr.hose:
                                    $ Chr.hose = ""
                        "Remove_panties" if Chr.underwear:
                            $ Chr.underwear = ""
                        "Add black_panties":
                            $ Chr.underwear = "_black_panties"
                        "Add white_panties" if Chr == StormX or Chr == EmmaX:
                            $ Chr.underwear = "white_panties"
                        "Add cosplay_panties" if Chr == StormX:
                            $ Chr.underwear = "cos_panties"
                        "Add bikini":
                            $ Chr.underwear = "_bikini_bottoms"
                        "Add_shorts":
                            $ Chr.underwear = "_shorts"
                        "Add green_panties":
                            $ Chr.underwear = "_green_panties"
                        "Add lace_panties":
                            $ Chr.underwear = "lace_panties"
                        "Add wolvie_panties" if Chr == LauraX:
                            $ Chr.underwear = "wolvie_panties"
                        "Add sports_panties" if Chr == EmmaX:
                            $ Chr.underwear = "sports_panties"
                        "Toggle Pierce":
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
                        "pull down-up_panties":
                            if Chr.underwear_pulled_down:
                                $ Chr.underwear_pulled_down = 0
                            else:
                                $ Chr.underwear_pulled_down = 1
                        "Toggle Wetness":
                            if not Chr.grool:
                                $ Chr.grool = 1
                            elif Chr.grool == 1:
                                $ Chr.grool = 2
                            else:
                                $ Chr.grool  = 0
                        "Back":
                            jump Wardrobe_Menu
            "Misc":
                while True:
                    menu:
                        "Emotions":
                            call EmotionEditor (Chr)
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Toggle Wetness":
                            if not Chr.grool:
                                $ Chr.grool = 1
                            elif Chr.grool == 1:
                                $ Chr.grool = 2
                            else:
                                $ Chr.grool  = 0
                        "Toggle wet look":
                            if not Chr.Water:
                                $ Chr.Water = 1
                            elif Chr.Water == 1:
                                $ Chr.Water = 3
                            else:
                                $ Chr.Water  = 0
                        "Toggle pubes":
                            if not Chr.pubes:
                                $ Chr.pubes = "_hairy"
                            else:
                                $ Chr.pubes = "_bare"
                        "Toggle Short Hair" if Chr == KittyX:
                            if Chr.hair == "long":
                                $ Chr.hair = "_evo"
                            else:
                                $ Chr.hair = "long"
                        "Toggle Mohawk" if Chr == StormX:
                            if Chr.hair == "long":
                                $ Chr.hair = "mohawk"
                            else:
                                $ Chr.hair = "long"
                        "Toggle Short Hair" if Chr == StormX:
                            if Chr.hair == "long":
                                $ Chr.hair = "short"
                            else:
                                $ Chr.hair = "long"
                        "Toggle Ponytailr" if Chr == JeanX:
                            if Chr.hair == "pont":
                                $ Chr.hair = "short"
                            else:
                                $ Chr.hair = "pony"
                        "Toggle Hat" if Chr == EmmaX:
                            if Chr.hair == "wavy":
                                $ Chr.hair = "hat"
                            elif Chr.hair == "wet":
                                $ Chr.hair = "hat wet"
                            elif Chr.hair == "hat wet":
                                $ Chr.hair = "wet"
                            else:
                                $ Chr.hair = "wavy"
                        "Cosplay Hair" if Chr == RogueX:
                            if Chr.hair == "_cosplay":
                                $ Chr.hair = "_evo"
                            else:
                                $ Chr.hair = "_cosplay"
                        "Ponytail Hair" if Chr == JeanX:
                            if Chr.hair == "pony":
                                $ Chr.hair = "short"
                            else:
                                $ Chr.hair = "pony"
                        "Toggle held":
                            if not Chr.held_item:
                                $ Chr.held_item  = "_phone"
                            elif Chr.held_item == "_phone":
                                $ Chr.held_item  = "_dildo"
                            elif Chr.held_item == "_dildo":
                                $ Chr.held_item  = "_vibrator"
                            elif Chr.held_item == "_vibrator":
                                $ Chr.held_item  = "_panties"
                            else:
                                $ Chr.held_item  = 0
                        "Toggle gold Necklace" if Chr == StormX:
                            if not Chr.neck:
                                $ Chr.neck = 'gold'
                            else:
                                $ Chr.neck = ""
                        "Toggle flower Necklace":
                            if not Chr.neck:
                                $ Chr.neck = 'flower necklace'
                            else:
                                $ Chr.neck = ""
                        "Toggle ring Necklace" if Chr == StormX:
                            if not Chr.neck:
                                $ Chr.neck = 'rings'
                            else:
                                $ Chr.neck = ""
                        "Toggle Rings" if Chr == StormX:
                            if not Chr.accessory:
                                $ Chr.accessory = 'rings'
                            else:
                                $ Chr.accessory = ""
                        "Toggle_choker" if Chr == EmmaX or Chr == RogueX:
                            if Chr.neck != 'choker':
                                $ Chr.neck ='choker'
                            else:
                                $ Chr.neck = ""
                        "Toggle boots" if Chr == EmmaX:
                            if Chr.accessory != "thigh boots":
                                $ Chr.accessory ='thigh boots'
                            else:
                                $ Chr.accessory = ""
                        "Toggle sweater" if Chr == RogueX:
                            if Chr.accessory != "_sweater":
                                $ Chr.accessory ='sweater'
                            else:
                                $ Chr.accessory = ""
                        "Toggle suspenders" if Chr == LauraX or Chr == JeanX:
                            if Chr.accessory == "suspenders":
                                $ Chr.accessory = "suspenders2"
                            elif Chr.accessory == "suspenders2":
                                $ Chr.accessory = ""
                            else:
                                $ Chr.accessory = "suspenders"
                        "Spunk Level":
                            menu:
                                "Mouth":
                                    if "mouth" in Chr.spunk:
                                        $ Chr.spunk.remove("mouth")
                                    else:
                                        $ Chr.spunk.append("mouth")
                                "Chin":
                                    if "chin" in Chr.spunk:
                                        $ Chr.spunk.remove("chin")
                                    else:
                                        $ Chr.spunk.append("chin")
                                "Facial":
                                    if "facial" in Chr.spunk:
                                        $ Chr.spunk.remove("facial")
                                    else:
                                        $ Chr.spunk.append("facial")
                                "Hair":
                                    if "hair" in Chr.spunk:
                                        $ Chr.spunk.remove("hair")
                                    else:
                                        $ Chr.spunk.append("hair")
                                "Tits":
                                    if "tits" in Chr.spunk:
                                        $ Chr.spunk.remove("tits")
                                    else:
                                        $ Chr.spunk.append("tits")
                                "Belly":
                                    if "belly" in Chr.spunk:
                                        $ Chr.spunk.remove("belly")
                                    else:
                                        $ Chr.spunk.append("belly")
                                "Back":
                                    if "back" in Chr.spunk:
                                        $ Chr.spunk.remove("back")
                                    else:
                                        $ Chr.spunk.append("back")
                                "Pussy":
                                    if "in" in Chr.spunk:
                                        $ Chr.spunk.remove("in")
                                    else:
                                        $ Chr.spunk.append("in")
                                "Ass":
                                    if "anal" in Chr.spunk:
                                        $ Chr.spunk.remove("anal")
                                    else:
                                        $ Chr.spunk.append("anal")
                                "Return":
                                    pass
                        "Toggle Pierce":
                            if Chr.piercings == "_ring":
                                $ Chr.piercings = "_barbell"
                            elif Chr.piercings == "_barbell":
                                $ Chr.piercings = ""
                            else:
                                $ Chr.piercings = "_ring"
                        "Add Gloves" if not Chr.arms:
                            $ Chr.arms = "_gloves"
                        "Remove Gloves" if Chr.arms:
                            $ Chr.arms = ""
                        "Back":
                            jump Wardrobe_Menu
            "Nothing":
                return
return


label StatHacks(Chr=0, counter=0):
    while True:
        menu:
            "[Chr.name]: Love: [Chr.love], Obedience: [Chr.obedience], Inhibition:[Chr.inhibition], Lust: [Chr.lust] Taboo: [Taboo], Location: [Chr.location]"
            "Activities":
                menu:
                    "Recent Actions":
                        "[Chr.recent_history]"
                    "Daily Actions":
                        "[Chr.daily_history]"
                    "Traits":
                        "[Chr.traits]"
                    "History":
                        "[Chr.history]"
            "Gwen's face" if False:
                call Gwen_FaceEditor
            "Raise Love":
                $ Chr.love += 100
            "Lower Love":
                $ Chr.love -= 100
            "Raise Obedience":
                $ Chr.obedience += 100
            "Lower Obedience":
                $ Chr.obedience -= 100
            "Raise Inhibitions":
                $ Chr.inhibition += 100
            "Lower Inhibitions":
                $ Chr.inhibition -= 100
            "Taboo toggle":
                $ Taboo = 40 if Taboo != 40 else 0
                "[Taboo]"
            "Small":
                $ counter = 1
                while counter:
                    menu:
                        "Raise Love":
                            $ Chr.love += 10
                        "Lower Love":
                            $ Chr.love -= 10
                        "Raise Obedience":
                            $ Chr.obedience += 10
                        "Lower Obedience":
                            $ Chr.obedience -= 10
                        "Raise Inhibitions":
                            $ Chr.inhibition += 10
                        "Lower Inhibitions":
                            $ Chr.inhibition -= 10
                        "Back":
                            $ counter = 0
            "Other":
                menu:
                    "Raise Lust":
                        $ Chr.lust += 10
                    "Lower Lust":
                        $ Chr.lust -= 10
                    "Raise Addiction":
                        $ Chr.addiction += 10
                    "Lower Addiction":
                        $ Chr.addiction -= 10
                    "Back":
                        pass
            "Wardrobe":
                call WardrobeEditor (Chr)
            "Return":

                call checkout
                return


label Cheat_Menu(Girl=0):
    if Girl not in all_Girls:
        $ Girl = focused_Girl
    menu:
        "Level-Up":
            $ Girl.action_counter["handjob"] += 5
            $ Girl.action_counter["blowjob"] += 5
            $ Girl.event_counter["swallowed"] += 5
            $ Girl.action_counter["handjob"] += 5
            $ Girl.event_counter["ass_slapped"] += 5
            $ Girl.action_counter["titjob"] += 5
            $ Girl.action_counter["sex"] += 5
            $ Girl.action_counter["anal"] += 5
            $ Girl.action_counter["hotdog"] += 5
            $ Girl.action_counter["masturbation"] += 5
            $ Girl.event_counter["orgasmed"]+= 5
            $ Girl.action_counter["fondle_breasts"]+= 5
            $ Girl.action_counter["fondle_thighs"]+= 5
            $ Girl.action_counter["fondle_pussy"] += 5
            $ Girl.action_counter["fondle_ass"] += 5
            $ Girl.action_counter["dildo_pussy"] += 5
            $ Girl.action_counter["dildo_ass"] += 5
            $ Girl.Plug += 5
            $ Girl.action_counter["suck_breasts"] += 5
            $ Girl.action_counter["finger_pussy"] += 5
            $ Girl.action_counter["finger_ass"] += 5
            $ Girl.action_counter["eat_pussy"] += 5
            $ Girl.action_counter["eat_ass"] += 5
            $ Girl.action_counter["blowjob"] += 5
            $ Girl.event_counter["swallowed"] += 5
            $ Girl.event_counter["creampied"] += 5
            $ Girl.event_counter["anal_creampied"] += 5
            $ Girl.SeenChest = 1
            $ Girl.SeenPanties = 1
            $ Girl.SeenPussy = 1
        "Level Reset":
            $ Girl.action_counter["handjob"] = 0
            $ Girl.action_counter["blowjob"] = 0
            $ Girl.event_counter["swallowed"] = 0
        "Toggle Taboo":
            if not Taboo:
                $ Taboo = 40
            else:
                $ Taboo = 0
        "Maxed":
            $ Girl.love = 1000
            $ Girl.inhibition = 1000
            $ Girl.obedience = 1000
            $ Girl.lust = 50
            $ Girl.addiction = 0
            $ Girl.addiction_rate = 0
            $ Girl.action_counter["kiss"] = 1
            $ Girl.event_counter["swallowed"] = 0
        "50%%":
            $ Girl.love = 500
            $ Girl.inhibition = 500
            $ Girl.obedience = 500
            $ Girl.lust = 65
            $ Girl.addiction = 0
            $ Girl.addiction_rate = 10
            $ Girl.action_counter["kiss"] = 10
            $ Girl.event_counter["swallowed"] = 0
        "25%%":
            $ Girl.love = 250
            $ Girl.inhibition = 250
            $ Girl.obedience = 250
            $ Girl.lust = 85
            $ Girl.addiction = 10
            $ Girl.addiction_rate = 50
            $ Girl.action_counter["kiss"] = 10
            $ Girl.event_counter["swallowed"] = 0
        "Juice up":
            $ Player.semen += 5
            $ Girl.remaining_actions = 10
        "Cold Shower":
            $ Player.focus = 0
        "Exit":
            return
    jump Cheat_Menu



label Clothing_Schedule_Check(Girl=0, Changed=0, Value=0, Count=0):








    while Count < 9:
        if Girl.Clothing[Count] == Changed:
            if Value:

                if Girl.Clothing[Count] == 3 and Girl.Custom1[0] == 2:
                    pass
                elif Girl.Clothing[Count] == 5 and Girl.Custom2[0] == 2:
                    pass
                elif Girl.Clothing[Count] == 6 and Girl.Custom3[0] == 2:
                    pass
                elif Girl.Clothing[Count] == 4 and Girl.Gym[0] != 1:
                    pass
                else:
                    $ Girl.Clothing[Count] = 0
            else:
                $ Girl.Clothing[Count] = 0
        $ Count += 1
    return


label Emergency_Clothing_Reset:
    "This resets all customized clothing to their defaults."
    menu:
        "Do you want to continue?"
        "Yes":
            $ RogueX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ RogueX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ RogueX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ RogueX.Casual1 = [2,"_gloves", "_skirt", "_mesh_top", "_spiked_collar", "_tank", "_black_panties", "", "", "_tights", 0]
            $ RogueX.Casual2 = [2,"_gloves", "_pants", "_pink_top", "_spiked_collar", "_buttoned_tank", "_black_panties", "", "", "", 0]
            $ RogueX.Gym = [0, "_gloves", "", "_hoodie", "", "_sports_bra", "_shorts", "", "", "", 0]
            $ RogueX.sleepwear = [0, "", "", "", "", "_tank", "_green_panties", "", "", "", 0]
            $ RogueX.Swim = [0, "", "", "_hoodie", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ RogueX.Costume = [2,"_gloves", "_skirt", "", "", "_tube_top", "_black_panties", "_sweater", "_cosplay", "", 0]
            $ RogueX.Clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ RogueX.Outfit = "casual1"
            $ RogueX.OutfitDay = "casual1"

            $ KittyX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ KittyX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ KittyX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ KittyX.Casual1 = [2,0, "capris", "_pink_top", "gold_necklace", "cami", "_green_panties", "", "", "", 0]
            $ KittyX.Casual2 = [2,0, "black jeans", "red_shirt", "", "bra", "_green_panties", "", "", "", 0]
            $ KittyX.Gym = [0, "", "_shorts", "", "", "_sports_bra", "_green_panties", "", "", "", 0]
            $ KittyX.sleepwear = [0, "", "_shorts", "", "", "cami", "_green_panties", "", "", "", 0]
            $ KittyX.Swim = [0, "", "blue_skirt", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ KittyX.Costume = [2,0, "dress", "jacket", "flower_necklace", "dress", "lace_panties", "", "", "", 0]
            $ KittyX.Clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ KittyX.Outfit = "casual1"
            $ KittyX.OutfitDay = "casual1"

            $ EmmaX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ EmmaX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ EmmaX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ EmmaX.Casual1 = [2,0, "_pants", "jacket", "choker", "corset", "white_panties", "", "", "", 0]
            $ EmmaX.Casual2 = [2,"_gloves", "_pants", "", "choker", "corset", "white_panties", "", "", "", 0]
            $ EmmaX.Gym = [0, "", "", "", "", "_sports_bra", "sports_panties", "", "", "", 0]
            $ EmmaX.sleepwear = [0, "", "", "", "", "corset", "white_panties", "", "", "", 0]
            $ EmmaX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ EmmaX.Costume =  [2,"_gloves", "dress", "dress", "choker", "", "lace_panties", "", "hat", "stockings_and_garterbelt", 0]
            $ EmmaX.Clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ EmmaX.Outfit = "casual1"
            $ EmmaX.OutfitDay = "casual1"

            $ LauraX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ LauraX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ LauraX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ LauraX.Casual1 = [2,"wrists", "leather_pants", "", "leash_choker", "leather_bra", "_black_panties", "", "", "", 0]
            $ LauraX.Casual2 = [2,0, "_skirt", "jacket", "leash_choker", "leather_bra", "_black_panties", "", "", "", 0]
            $ LauraX.Gym = [0, "wrists", "leather_pants", "", "", "leather_bra", "_black_panties", "", "", "", 0]
            $ LauraX.sleepwear = [0, "", "", "", "", "leather_bra", "leather_panties", "", "", "", 0]
            $ LauraX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ LauraX.Costume = [2,"_gloves", "other_skirt", "", "", "white_tank", "_black_panties", "suspenders", "", "black stockings", 0]
            $ LauraX.Clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ LauraX.Outfit = "casual1"
            $ LauraX.OutfitDay = "casual1"

            $ JeanX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JeanX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JeanX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JeanX.Casual1 = [2,0, "_pants", "pink_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
            $ JeanX.Casual2 = [2,0, "_skirt", "green_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
            $ JeanX.Gym = [0, "", "yoga_pants", "", "", "_sports_bra", "_green_panties", "", "", "", 0]
            $ JeanX.sleepwear = [0, "", "", "pink_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
            $ JeanX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ JeanX.Costume =  [2,0, "_shorts", "yellow_shirt", "", "green_bra", "_green_panties", "suspenders", "pony", "", 0]
            $ JeanX.Clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ JeanX.Outfit = "casual1"
            $ JeanX.OutfitDay = "casual1"

            $ StormX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ StormX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ StormX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ StormX.Casual1 = [2,0, "_skirt", "white_shirt", "", "black_bra", "white_panties", "", "", "", 0]
            $ StormX.Casual2 = [2,0, "_pants", "jacket", "", "_tube_top", "white_panties", "", "", "", 0]
            $ StormX.Gym = [0, "", "yoga_pants", "", "", "_sports_bra", "white_panties", "", "", "",10]
            $ StormX.sleepwear = [0, "", "", "white_shirt", "", "", "white_panties", "", "", "",25]
            $ StormX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ StormX.Costume = [2,0, "", "", "ring_necklace", "cos_bra", "cos_panties", "rings", "short", "", 0]
            $ StormX.Clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ StormX.Outfit = "casual1"
            $ StormX.OutfitDay = "casual1"

            $ JubesX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JubesX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JubesX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JubesX.Casual1 = [2,0, "_shorts", "red_shirt", "", "_sports_bra", "blue_panties", "jacket", "", "", 0]
            $ JubesX.Casual2 = [2,0, "_pants", "black_shirt", "", "_sports_bra", "blue_panties", "jacket", "", "", 0]
            $ JubesX.Gym = [0, "", "_pants", "", "", "_sports_bra", "blue_panties", "", "", "",10]
            $ JubesX.sleepwear = [0, "", "", "", "", "_sports_bra", "blue_panties", "", "", "",25]
            $ JubesX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ JubesX.Costume = [0, "", "_pants", "black_shirt", "", "_sports_bra", "blue_panties", "jacket", "", "", 0]
            $ JubesX.Clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ JubesX.Outfit = "casual1"
            $ JubesX.OutfitDay = "casual1"

            "Done."
            "You will now need to set their custom outfits again."
        "No":
            pass
    return




label AnyLine(Girl=0, Templine=". . ."):




    $ global PassLine
    $ PassLine = Templine
    if Girl == RogueX:
        ch_r "[PassLine]"
    elif Girl == KittyX:
        ch_k "[PassLine]"
    elif Girl == EmmaX:
        ch_e "[PassLine]"
    elif Girl == LauraX:
        ch_l "[PassLine]"
    elif Girl == JeanX:
        ch_j "[PassLine]"
    elif Girl == StormX:
        ch_s "[PassLine]"
    elif Girl == JubesX:
        ch_v "[PassLine]"
    else:
        ch_u "[PassLine]"
    return

label GirlsAngry(Girls=0, BO=[]):

    $ approval_bonus = 0
    $ BO = all_Girls[:]
    while BO:
        if BO[0].location == bg_current and "_angry" in BO[0].recent_history:
            if bg_current == BO[0].home:
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
                jump Player_Room_Entry
            else:
                $ BO[0].location = BO[0].home
            if BO[0] in Party:
                $ Party.remove(BO[0])
            if Girls:
                ". . . and so does [BO[0].name]."
            else:
                "[BO[0].name] storms off."
                if BO[0] == StormX:
                    ". . . so to speak."
            $ Girls += 1
            if BO[0] == RogueX:
                hide Rogue_sprite with easeoutleft
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



label Lastnamer(wordcount=0, Splitname=0, Lastname=0):

    $ wordcount = Player.name.count(" ")


    $ Splitname = Player.name.split()


    $ Lastname = "Mr. " + Splitname[wordcount]
    return Lastname




label DrainAll(word=0, Recent=1, Daily=1, Traits=0):


    $ BO = all_Girls[:]
    while BO:
        $ BO[0].drain_word(word,Recent,Daily,Traits)
        $ BO.remove(BO[0])
    return






label Clothes_Schedule(Girl=0, counter=0):


    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    if Girl == RogueX:
        if approval_check(Girl, 1500, "LO"):
            ch_r "So, you'd like to choose what I wear for the week? Ok, shoot."
            $ counter = 3
        elif approval_check(Girl, 1200, "LO"):
            ch_r "I guess I could set aside a few schooldays for you."
            $ counter = 2
        elif approval_check(Girl, 1000, "LO"):
            ch_r "We can talk about what I wear outside of classes."
            $ counter = 1
        else:
            ch_r "You know, I don't really need fashion advice from you."
            return
    elif Girl == KittyX:
        if approval_check(Girl, 1500, "LO"):
            ch_k "Let me know what you like."
            $ counter = 3
        elif approval_check(Girl, 1200, "LO"):
            ch_k "I could let you pick a few days. . ."
            $ counter = 2
        elif approval_check(Girl, 1000, "LO"):
            ch_k "We could talk about weekends, maybe. . ."
            $ counter = 1
        else:
            ch_k "I think I'll[Girl.like]figure out my own outfits."
            return
    elif Girl == EmmaX:
        if approval_check(Girl, 1500, "LO"):
            ch_e "I'm open to suggestions."
            $ counter = 3
        elif approval_check(Girl, 1200, "LO"):
            ch_e "I could let you choose a few days. . ."
            $ counter = 2
        elif approval_check(Girl, 1000, "LO"):
            ch_e "Perhaps when I'm off the clock. . ."
            $ counter = 1
        else:
            ch_e "I'd prefer to handle my own wardrobe."
            return
    elif Girl == LauraX:
        if approval_check(Girl, 1500, "LO"):
            ch_l "Fine, you pick, whatever."
            $ counter = 3
        elif approval_check(Girl, 1200, "LO"):
            ch_l "I don't know, you could pick a few days. . ."
            $ counter = 2
        elif approval_check(Girl, 1000, "LO"):
            ch_l "Maybe on weekends. . ."
            $ counter = 1
        else:
            ch_l "Nah, I got it covered."
            return
    elif Girl == JeanX:
        if approval_check(Girl, 1500, "LO"):
            ch_j "Ok, I'm tired of having to pick outfits. . ."
            $ counter = 3
        elif approval_check(Girl, 1200, "LO"):
            ch_j "I guess you do have some taste. . ."
            $ counter = 2
        elif approval_check(Girl, 1000, "LO"):
            ch_j "I guess my weekends are free. . ."
            $ counter = 1
        else:
            ch_j "Huh? No."
            return
    elif Girl == StormX:
        if approval_check(Girl, 1500, "LO"):
            ch_s "I'm willing to listen."
            $ counter = 3
        elif approval_check(Girl, 1200, "LO"):
            ch_s "I suppose you could choose a few days. . ."
            $ counter = 2
        elif approval_check(Girl, 1000, "LO"):
            ch_s "Perhaps when I'm not working. . ."
            $ counter = 1
        else:
            ch_s "I think I'd rather choose my own clothing."
            return
    elif Girl == JubesX:
        if approval_check(Girl, 1500, "LO"):
            ch_v "What're you thinking?"
            $ counter = 3
        elif approval_check(Girl, 1200, "LO"):
            ch_v "You could help with a few days?"
            $ counter = 2
        elif approval_check(Girl, 1000, "LO"):
            ch_v "I don't know, weekends maybe?"
            $ counter = 1
        else:
            ch_v "Nah, I'll figure it out myself."
            return
    while True:
        menu:
            extend ""
            "Every Day":
                "This sets her outfit for every day of the week in one go."
                "This overwrites the default schedule, and any scheduling you've already made."
                "Any choices you make later will overwrite this choice."
                menu:
                    "Pick an outfit to wear":
                        call Clothes_ScheduleB
                        if counter > 1:
                            $ Girl.Clothing[0] = _return
                            $ Girl.Clothing[2] = _return
                            $ Girl.Clothing[4] = _return
                        if counter > 2:
                            $ Girl.Clothing[1] = _return
                            $ Girl.Clothing[3] = _return
                        $ Girl.Clothing[5] = _return
                        $ Girl.Clothing[6] = _return
                    "Never mind.":
                        pass
            "Weekdays":
                menu:
                    "On Monday you should wear. . ." if counter > 1:
                        call Clothes_ScheduleB
                        $ Girl.Clothing[0] = _return
                    "On Monday you should wear. . . (locked)" if counter <= 1:
                        pass

                    "On Tuesday you should wear. . ." if counter > 2:
                        call Clothes_ScheduleB
                        $ Girl.Clothing[1] = _return
                    "On Tuesday you should wear. . . (locked)" if counter <= 2:
                        pass

                    "On Wednesday you should wear. . ." if counter > 1:
                        call Clothes_ScheduleB
                        $ Girl.Clothing[2] = _return
                    "On Wednesday you should wear. . . (locked)" if counter <= 1:
                        pass

                    "On Thursday you should wear. . ." if counter > 2:
                        call Clothes_ScheduleB
                        $ Girl.Clothing[3] = _return
                    "On Thursday you should wear. . . (locked)" if counter <= 2:
                        pass

                    "On Friday you should wear. . ." if counter > 1:
                        call Clothes_ScheduleB
                        $ Girl.Clothing[4] = _return
                    "On Friday you should wear. . . (locked)" if counter <= 1:
                        pass
                    "Back":
                        pass
            "Other":
                menu:
                    "On Saturday you should wear. . . (locked)" if counter < 1:
                        pass
                    "On Saturday you should wear. . ." if counter >= 1:
                        call Clothes_ScheduleB
                        $ Girl.Clothing[5] = _return

                    "On Sunday you should wear. . . (locked)" if counter < 1:
                        pass
                    "On Sunday you should wear. . ." if counter >= 1:
                        call Clothes_ScheduleB
                        $ Girl.Clothing[6] = _return

                    "In our rooms you should wear. . . (locked)" if counter < 1:
                        pass
                    "In our rooms you should wear. . ." if counter >= 1:
                        call Clothes_ScheduleB (Girl, 99)
                        $ Girl.Clothing[9] = _return

                    "On dates you should wear. . . (locked)" if counter < 1:
                        pass
                    "On dates you should wear. . ." if counter >= 1:
                        call Clothes_ScheduleB
                        $ Girl.Clothing[7] = _return

                    "When teaching you should wear. . . (locked)" if Girl in (EmmaX,StormX) and counter < 3:
                        pass
                    "When teaching you should wear. . ." if Girl in (EmmaX,StormX) and counter >= 3:
                        call Clothes_ScheduleB (Girl, 90)
                        $ Girl.Clothing[8] = _return
                    "Back":

                        pass
            "About Gym clothes":

                menu:
                    ch_p "You asked me before about your gym clothes?"
                    "Don't ask before changing into gym clothes" if "no_ask gym" not in Girl.traits:
                        Girl.voice "Sure."
                        $ Girl.traits.append("no_ask gym")
                    "Ask me before changing into gym clothes" if "no_ask gym" in Girl.traits:
                        Girl.voice "Sure."
                        $ Girl.traits.remove("no_ask gym")
                    "Never Mind":
                        pass

            "Private outfit" if Girl.Clothing[9]:

                ch_p "You know that outfit you wear in private?"
                if Girl in (EmmaX,StormX):
                    Girl.voice "Yes?"
                else:
                    Girl.voice "Yeah?"
                menu:
                    extend ""
                    "Just put them on without asking me about it." if "comfy" not in Girl.traits:
                        Girl.voice "Sure."
                        $ Girl.traits.append("comfy")
                    "Ask before changing into that." if "comfy" in Girl.traits:
                        Girl.voice "Sure."
                        $ Girl.traits.remove("comfy")
                    "Never Mind":
                        pass
            "Never mind [[Done]":

                return
    jump Clothes_Schedule

label Clothes_ScheduleB(Girl=0, Count=0):


    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)
    menu:
        "Your green outfit." if Girl == RogueX:
            $ Count = 1
        "That pink outfit, with the jeans." if Girl == RogueX:
            $ Count = 2

        "That pink outfit, with the jeans." if Girl == KittyX:
            $ Count = 1
        "Your red shirt outfit." if Girl == KittyX:
            $ Count = 2

        "That teacher outfit." if Girl == EmmaX:
            $ Count = 1
        "Your superhero outfit." if Girl == EmmaX:
            $ Count = 2

        "That leather combat look." if Girl == LauraX:
            $ Count = 1
        "Your jacket and skirt." if Girl == LauraX:
            $ Count = 2

        "That pink shirt and khakis look." if Girl == JeanX:
            $ Count = 1
        "Your green shirt and skirt." if Girl == JeanX:
            $ Count = 2

        "That white top and skirt look." if Girl == StormX:
            $ Count = 1
        "Your black jacket and pants look." if Girl == StormX:
            $ Count = 2

        "That red and blue look." if Girl == JubesX:
            $ Count = 1
        "Your black top and pants look." if Girl == JubesX:
            $ Count = 2
        "That outfit we put together [[custom]":

            if Girl == RogueX:
                ch_r "Which one again?"
            elif Girl == KittyX:
                ch_k "[Girl.Like]which?"
            elif Girl == EmmaX:
                ch_e "Which were you thinking?"
            elif Girl == LauraX:
                ch_l "Which one?"
            elif Girl == JeanX:
                ch_j "What outfit?"
            elif Girl == StormX:
                ch_s "Which did you mean?"
            elif Girl == JubesX:
                ch_v "Which one?"
            menu:
                extend ""
                "The first one. (locked)" if not Girl.Custom1[0]:
                    pass
                "The first one." if Girl.Custom1[0]:
                    if Girl.Custom1[0] == 2 or Count == 99:
                        $ Count = 3
                    else:
                        Girl.voice "Well. . ."
                        call QuickOutfitCheck (Girl, 3)
                        if Girl.Custom1[0] == 2:
                            $ Count = 3
                        else:
                            $ Line = "no"
                "The second one. (locked)" if not Girl.Custom2[0]:
                    pass
                "The second one." if Girl.Custom2[0]:
                    if Girl.Custom2[0] == 2 or Count == 99:
                        $ Count = 5
                    else:
                        Girl.voice "Well. . ."
                        call QuickOutfitCheck (Girl, 5)
                        if Girl.Custom2[0] == 2:
                            $ Count = 5
                        else:
                            $ Line = "no"
                "The third one. (locked)" if not Girl.Custom3[0]:
                    pass
                "The third one." if Girl.Custom3[0]:
                    if Girl.Custom3[0] == 2 or Count == 99:
                        $ Count = 6
                    else:
                        Girl.voice "Well. . ."
                        call QuickOutfitCheck (Girl, 6)
                        if Girl.Custom3[0] == 2:
                            $ Count = 6
                        else:
                            $ Line = "no"
                "Never mind":
                    pass
            if Line == "no":
                if Girl == RogueX:
                    ch_r "No, I'm not wearing that outside, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "I'm[Girl.like]definitely not wearing that one out."
                elif Girl == EmmaX:
                    ch_e "I'm certainly not wearing that one in public."
                elif Girl == LauraX:
                    ch_l "I won't wear that out."
                elif Girl == JeanX:
                    ch_j "Yeah, I wouldn't be caught out in that."
                elif Girl == StormX:
                    ch_s "I cannot wear that one in public."
                elif Girl == JubesX:
                    ch_v "That one's private. . ."
                $ Line = 0
            else:
                Girl.voice "Fine. . ."
        "Your gym clothes.":

            if Count == 90:
                Girl.voice "Not in class, [Girl.player_petname]."
                $ Count = 0
            else:
                $ Count = 4
        "Your sleepwear.":
            if Count == 99:
                $ Count = 7
            else:
                Girl.voice "Well. . ."
                call QuickOutfitCheck (Girl, 7)
                if Girl.Custom1[0] == 2:
                    $ Count = 7
                    Girl.voice "Fine. . ."
                else:
                    if Girl == RogueX:
                        ch_r "I don't know about that, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "That's not really appropriate, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "I don't think that would be appropriate, [Girl.player_petname]."
                    elif Girl == LauraX:
                        ch_l "That's kinda skimpy, [Girl.player_petname]."
                    elif Girl == JeanX:
                        ch_j "I -sleep- in that, I don't wear it out."
                    elif Girl == StormX:
                        ch_s "That's more sleepwear than casual wear."
                    elif Girl == JubesX:
                        ch_v "That's for sleeping in, not going out. . ."
                    $ Count = 0
        "Whatever you like.":
            pass

    if Girl == RogueX:
        if Count:
            ch_r "Ok, sure, I'll wear that."
        else:
            ch_r "I'll just wear whatever then."
    elif Girl == KittyX:
        if Count:
            ch_k "Ok, sure, I'll wear that."
        else:
            ch_k "I'll just wear whatever then."
    elif Girl == EmmaX:
        if Count:
            ch_e "Very well."
        else:
            ch_e "I'll wear something else instead."
    elif Girl == LauraX:
        if Count:
            ch_l "Ok, sure."
        else:
            ch_l "I'll figure something else out."
    elif Girl == JeanX:
        if Count:
            ch_j "Ok, fine."
        else:
            ch_j "I've got my own plans."
    elif Girl == StormX:
        if Count:
            ch_s "I will wear it."
        else:
            ch_s "I will choose something else instead. . ."
    elif Girl == JubesX:
        if Count:
            ch_v "I'd wear it."
        else:
            ch_v "I'll pick something else. . ."
    return Count


label AltClothes(Girl=0, Outfit=1):




    $ Girl = GirlCheck(Girl)

    if Girl.Clothing[Outfit] == 1 or not Girl.Clothing[Outfit]:
        $ Girl.Outfit = "casual1"
    elif Girl.Clothing[Outfit] == 2:
        $ Girl.Outfit = "casual2"
    elif Girl.Clothing[Outfit] == 3:
        $ Girl.Outfit = "custom1"
    elif Girl.Clothing[Outfit] == 5:
        $ Girl.Outfit = "custom2"
    elif Girl.Clothing[Outfit] == 6:
        $ Girl.Outfit = "custom3"
    elif Girl.Clothing[Outfit] == 7:
        $ Girl.Outfit = "sleep"
    elif Girl.Clothing[Outfit] == 4:
        $ Girl.Outfit = "gym"
    elif Girl.Clothing[Outfit] == 10:
        $ Girl.Outfit = "swimwear"
    else:
        $ Girl.Outfit = "casual1"
    return

label Private_Outfit(Girl=0):

    $ Girl = GirlCheck(Girl)
    if Girl.Break[0] or "_angry" in Girl.daily_history:
        return
    if Girl.Outfit == "temporary" or not Girl.Clothing[9]:


        return
    if "comfy" in Girl.recent_history or "comfy" in Girl.traits or Girl.Outfit == Girl.Clothing[9]:
        call AltClothes (Girl, 9)
        $ Girl.change_outfit(Changed=1)
    elif "no_comfy" in Girl.recent_history:
        pass
    elif approval_check(Girl, 1200, "LI") and (2*Girl.inhibition) >= (Girl.love + Girl.obedience +100):

        call shift_focus (Girl)
        if Girl == RogueX:
            ch_r "Be right there [Girl.player_petname]. . ."
            ch_r "I'm slippin' inta somethin' more comfortable. . ."
        elif Girl == KittyX:
            ch_k "Gimme a sec. . ."
            ch_k "I'm throwing on something a bit more. . . fun."
        elif Girl == EmmaX:
            ch_e "I'll be just a moment. . ."
            ch_e "I'll just slip into something more comfortable. . ."
        elif Girl == LauraX:
            ch_l "One minute. . ."
            ch_l "I'm getting a bit more comfortable."
        elif Girl == JeanX:
            ch_j "Let me get changed. . ."
        elif Girl == StormX:
            ch_s "Give me one moment. . ."
            ch_s "I need to change into something more comfortable. . ."
        elif Girl == JubesX:
            ch_v "Gimme a minute. . ."
            ch_v "I wanna slip something else on. . ."
        call AltClothes (Girl, 9)
        $ Girl.change_outfit(Changed=1)
        $ Girl.recent_history.append("comfy")
    else:
        call shift_focus (Girl)
        if Girl == RogueX:
            ch_r "Be right there [Girl.player_petname]. . ."
            menu:
                ch_r "Should I throw on somethin' more comfortable?"
                "Sure.":
                    ch_r "Love to. . ."
                    call AltClothes (Girl, 9)
                    $ Girl.change_outfit(Changed=1)
                    $ Girl.recent_history.append("comfy")
                "No thanks.":
                    ch_r "Suit yourself."
                    $ Girl.recent_history.append("no_comfy")
        elif Girl == KittyX:
            ch_k "Gimme a sec. . ."
            menu:
                ch_k "Want me to wear something more fun?"
                "Sure.":
                    ch_k "Hehe. . ."
                    call AltClothes (Girl, 9)
                    $ Girl.change_outfit(Changed=1)
                    $ Girl.recent_history.append("comfy")
                "No thanks.":
                    ch_k "Oh, ok."
                    $ Girl.recent_history.append("no_comfy")
        elif Girl == EmmaX:
            ch_e "I'll be just a moment. . ."
            menu:
                ch_e "Would you like me to change into something more comfortable?"
                "Sure.":
                    ch_e "Lovely. . ."
                    call AltClothes (Girl, 9)
                    $ Girl.change_outfit(Changed=1)
                    $ Girl.recent_history.append("comfy")
                "No thanks.":
                    ch_e "Very well."
                    $ Girl.recent_history.append("no_comfy")
        elif Girl == LauraX:
            ch_l "One minute. . ."
            menu:
                ch_l "I could throw on something a bit more fun. . ."
                "Sure.":
                    ch_l "Cool. . ."
                    call AltClothes (Girl, 9)
                    $ Girl.change_outfit(Changed=1)
                    $ Girl.recent_history.append("comfy")
                "No thanks.":
                    ch_l "Oh, ok."
                    $ Girl.recent_history.append("no_comfy")
        elif Girl == JeanX:
            menu:
                ch_j "I do have a more fun look. . ."
                "Sure.":
                    call AltClothes (Girl, 9)
                    $ Girl.change_outfit(Changed=1)
                    $ Girl.recent_history.append("comfy")
                "No thanks.":
                    ch_j "Huh. Ok. . ."
                    $ Girl.recent_history.append("no_comfy")
        elif Girl == StormX:
            ch_s "I'll be just a moment. . ."
            menu:
                ch_s "Would you like me to change into something more comfortable?"
                "Sure.":
                    ch_s "Excellent. . ."
                    call AltClothes (Girl, 9)
                    $ Girl.change_outfit(Changed=1)
                    $ Girl.recent_history.append("comfy")
                "No thanks.":
                    ch_s "Very well."
                    $ Girl.recent_history.append("no_comfy")
        elif Girl == JubesX:
            ch_v "Gimme a minute. . ."
            menu:
                ch_v "Hey, how'bout I throw something. . . nice on?"
                "Sure.":
                    ch_v "Cool. . ."
                    call AltClothes (Girl, 9)
                    $ Girl.change_outfit(Changed=1)
                    $ Girl.recent_history.append("comfy")
                "No thanks.":
                    ch_v "Ok, fine."
                    $ Girl.recent_history.append("no_comfy")
    return

label Custom_Out(Girl=0, Custom=3, Shame=0, Agree=0):

    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)
    $ Girl.change_face("_sexy", 1)

    if Custom == 3:
        $ Shame = Girl.Custom1[10]
        if Girl.Custom1[0] == 2 or "exhibitionist" in Girl.traits:
            $ Girl.Outfit = "custom1"
            $ Agree = 1
        else:
            call QuickOutfitCheck (Girl, 3)
            if Girl.Custom1[0] == 2:
                $ Girl.Outfit = "custom1"
                $ Agree = 1
    elif Custom == 5:
        $ Shame = Girl.Custom2[10]
        if Girl.Custom2[0] == 2 or "exhibitionist" in Girl.traits:
            $ Girl.Outfit = "custom2"
            $ Agree = 1
        else:
            call QuickOutfitCheck (Girl, 5)
            if Girl.Custom2[0] == 2:
                $ Girl.Outfit = "custom2"
                $ Agree = 1
    else:
        $ Shame = Girl.Custom3[10]
        if Girl.Custom3[0] == 2 or "exhibitionist" in Girl.traits:
            $ Girl.Outfit = "custom3"
            $ Agree = 1
        else:
            call QuickOutfitCheck (Girl, 6)
            if Girl.Custom3[0] == 2:
                $ Girl.Outfit = "custom3"
                $ Agree = 1

    if Girl == RogueX:
        if Agree:

            $ Girl.Shame = Shame
            if "exhibitionist" in Girl.traits:
                ch_r "Ooo, momma likes."
            elif Shame >= 50:
                ch_r "You realize I'm pretty much naked here, right?"
            elif Shame >= 25:
                ch_r "This is pretty shameless. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_r "I don't know, I guess I could try it. . ."
            else:
                ch_r "Sure, [Girl.player_petname], that one's nice."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_r "Come on, I'd be totally nude!"
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_r "You're lucky I show {i}you{/i} this."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_r "It's kind of daring for me, sorry."
    elif Girl == KittyX:
        if Agree:

            $ Girl.Shame = Shame
            if "exhibitionist" in Girl.traits:
                ch_k "Hmm, I'm getting excited. . ."
            elif Shame >= 50:
                ch_k "This is. . . kinda slutty. . . but. . ."
            elif Shame >= 25:
                ch_k "I'm not really comfortable with this one. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_k "I'll give it a shot. . ."
            else:
                ch_k "Yeah, I like that one too."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_k "You have GOT to be kidding me here."
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_k "This is just between us."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_k "I can't wear this out!"
    elif Girl == EmmaX:
        if Agree:

            $ Girl.Shame = Shame
            if "exhibitionist" in Girl.traits:
                ch_e "Hmm, I'm getting excited. . ."
            elif Shame >= 50:
                ch_e "This is rather. . . shameless. . ."
            elif Shame >= 25:
                ch_e "I'm a bit uncomfortable with this one. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_e "I'll try it. . ."
            else:
                ch_e "Yeah, I like that one too."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_e "You have GOT to be kidding me here."
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_e "This is just between us."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_e "I can't wear this out!"
    elif Girl == LauraX:
        if Agree:

            $ Girl.Shame = Shame
            if "exhibitionist" in Girl.traits:
                ch_l "Mmmmmm. . ."
            elif Shame >= 50:
                ch_l "This is. . . really brave. . ."
            elif Shame >= 25:
                ch_l "This one's pretty skimpy. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_l "Yeah, ok. . ."
            else:
                ch_l "Yup."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_l "Perv."
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_l "Yeah, not in public."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_l "Nah."
    elif Girl == JeanX:
        if Agree:

            $ Girl.Shame = Shame
            if "exhibitionist" in Girl.traits:
                ch_j ". . ."
            elif Shame >= 50:
                ch_j "Pretty daring. . ."
            elif Shame >= 25:
                ch_j "Kinda skimpy. . ."
            elif Shame >= 15:
                $ Girl.change_face("_bemused", 1)
                ch_j "Sure, whatever. . ."
            else:
                ch_j "Sure."
        else:

            if Shame >= 50:
                $ Girl.change_face("_angry", 1)
                ch_j "Gross."
            elif Shame >= 25:
                $ Girl.change_face("_angry", 1)
                ch_j "You wish."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_j "No way."
    elif Girl == StormX:
        $ Girl.change_face("_bemused", 1)
        if Agree:

            $ Girl.Shame = Shame
            if "exhibitionist" in Girl.traits:
                ch_s "Oooh. . ."
            elif Shame >= 25:
                ch_s "You are going to get me into trouble. . ."
            else:
                ch_s "Yes, this will do nicely."
        else:

            $ Girl.change_face("_bemused", 1)
            ch_s "I am afraid cannot wear this out."
    elif Girl == JubesX:
        $ Girl.change_face("_bemused", 1)
        if Agree:

            $ Girl.Shame = Shame
            if "exhibitionist" in Girl.traits:
                ch_s "Oooh. . ."
            elif Shame >= 25:
                ch_s "Whew, this is flat out pornographic. . ."
            else:
                ch_s "Oh, yeah, this'll do. . ."
        else:

            $ Girl.change_face("_bemused", 1)
            ch_s "I really can't wear this one out. . ."
    return



label OutfitShame(Girl=0, Custom=3, Check=0, Count=0, Tempshame=50, Agree=1):






    $ Girl = GirlCheck(Girl)

    if not Check and not Taboo and not Girl.Taboo and Custom != 20:

        if Girl.Clothing[9] and bg_current in PersonalRooms:

            if "halloween" not in Player.daily_history:
                call Private_Outfit
        return

    if Girl.ChestNum() >= 5:
        $ Count = 20
    elif Girl.ChestNum() >= 4:
        $ Count = 15
    elif Girl.ChestNum() >= 3:
        $ Count = 10
    elif Girl.ChestNum() >= 2:
        $ Count = 5
    else:
        $ Count = 0



    if Custom == 20 and Girl.top_pulled_up:
        $ Count = 0
    elif Girl.OverNum() >= 5:
        $ Count += 20
    elif Girl.OverNum() >= 4:
        $ Count += 15
    elif Girl.OverNum() >= 3:
        $ Count += 10
    elif Girl.OverNum() >= 2:
        $ Count += 5



    if Girl.piercings and Count <= 10:
        $ Count = -5

    $ Girl.change_face("_sexy", 0)
    if Custom == 9 or Custom == 7:
        pass
    elif Count >= 20:
        $ Count = 20
        if Check:
            if Girl == RogueX:
                ch_r "Oh, I think this top combination works."
            elif Girl == KittyX:
                ch_k "This is[Girl.like]totally a cute top."
            elif Girl == EmmaX:
                ch_e "This is a fashionable top."
            elif Girl == LauraX:
                ch_l "This top works."
            elif Girl == JeanX:
                ch_j "The top is fine."
            elif Girl == StormX:
                ch_s "The top is fine."
            elif Girl == JubesX:
                ch_v "Yeah, the_top'll work. . ."
    elif not Check:
        pass
    elif Girl == RogueX:
        if Count >= 10 and (approval_check(Girl, 1200, TabM=0) or approval_check(Girl, 500, "I", TabM=0)):
            ch_r "This top is pretty sexy. . ."
        elif Count >= 10:
            ch_r "This top might be a bit daring to wear outside."
        elif Count >= 5 and (approval_check(Girl, 2300, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_r "Not leaving much to the imagination. . ."
        elif Count >= 5:
            $ Girl.change_face("startled", 1)
            ch_r "I really think this is a bit scandalous to wear out. . ."
        elif (approval_check(Girl, 2700, TabM=0) or approval_check(Girl, 950, "I", TabM=0)):
            ch_r "Oooh, I'm getting turned on already. . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_r "This is just for in private, right. . ."
    elif Girl == KittyX:
        if Count >= 10 and (approval_check(Girl, 1200, TabM=0) or approval_check(Girl, 500, "I", TabM=0)):
            ch_k "Kinda hot top."
        elif Count >= 10:
            ch_k "I wouldn't[Girl.like]feel comfortable in this top."
        elif Count >= 5 and (approval_check(Girl, 2300, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_k "This top is is[Girl.like]kinda breezy. . ."
        elif Count >= 5:
            $ Girl.change_face("startled", 1)
            ch_k "This top is[Girl.like]way too slutty."
        elif (approval_check(Girl, 2700, TabM=0) or approval_check(Girl, 950, "I", TabM=0)):
            ch_k "Is it hot in here? Whew. . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_k "I wouldn't wear this out, but maybe indoors."
    elif Girl == EmmaX:
        if Count >= 10:
            if approval_check(Girl, 1200, TabM=0) or approval_check(Girl, 500, "I", TabM=0):
                ch_e "A bit daring. . ."
            else:
                ch_e "I'm not sure about this top."
        elif Count >= 5:
            if approval_check(Girl, 2300, TabM=0) or approval_check(Girl, 800, "I", TabM=0):
                ch_e "I typically cover a {i}bit{/i} more than this."
            else:
                $ Girl.change_face("startled", 1)
                ch_e "This is a bit more cleavage than even I'm comforable with."
        elif (approval_check(Girl, 2700, TabM=0) or approval_check(Girl, 950, "I", TabM=0)):
            ch_e "Aren't my assets a bit. . . exposed here?"
        else:
            $ Girl.change_face("_bemused", 1)
            ch_e "This is considerably more cleavage than even I'm comforable with."
    elif Girl == LauraX:
        if Count >= 10 and (approval_check(Girl, 1200, TabM=0) or approval_check(Girl, 500, "I", TabM=0)):
            ch_l "This top works."
        elif Count >= 10:
            ch_l "The_top's not really a good look."
        elif Count >= 5 and (approval_check(Girl, 2300, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_l "I don't know, the_top's a little light."
        elif Count >= 5:
            $ Girl.change_face("startled", 1)
            ch_l "I can't really wear this top out."
        elif (approval_check(Girl, 2700, TabM=0) or approval_check(Girl, 950, "I", TabM=0)):
            ch_l ". . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_l "I wouldn't go out with my tits out."
    elif Girl == JeanX:
        if Count >= 10:
            ch_j "You must really enjoy these tits. . ."


        elif Count >= 5:
            ch_j "I've kinda got my tits out here. . ."



        elif (approval_check(Girl, 2700, TabM=0) or approval_check(Girl, 950, "I", TabM=0)):
            ch_j ". . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_j "You think I'd go out with my tits on display?"
    elif Girl == StormX:
        if Count >= 10:
            ch_s "A lovely choice for the top."
        elif Count >= 5:
            if StormX not in Rules:
                ch_s "I do typically cover more than this around the school."
            else:
                $ Girl.change_face("_bemused", 1)
                ch_s "I'm not sure Charles would approve of this top."
        elif (approval_check(Girl, 2700, TabM=0) or approval_check(Girl, 950, "I", TabM=0)):
            ch_s "Aren't my assets a bit. . . exposed here?"
        else:
            $ Girl.change_face("_bemused", 1)
            ch_s "I'm not sure Charles would approve of this top."
    elif Girl == JubesX:
        if Count >= 10 and (approval_check(Girl, 1200, TabM=0) or approval_check(Girl, 500, "I", TabM=0)):
            ch_v "Yeah, the_top'll work. . ."
        elif Count >= 10:
            ch_v "I don't know about this top. . ."
        elif Count >= 5 and (approval_check(Girl, 2300, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_v "I don't know, the_top's a little skimpy."
        elif Count >= 5:
            $ Girl.change_face("startled", 1)
            ch_v "I can't really wear this top out."
        elif (approval_check(Girl, 2700, TabM=0) or approval_check(Girl, 950, "I", TabM=0)):
            ch_v "I don't know. . ."
        else:
            $ Girl.change_face("_bemused", 1)
            ch_v "Well, I wouldn't go anywhere with my tits out like this. . ."


    $ Tempshame -= Count
    $ Count = 0

    if Girl.legs and Girl.underwear:
        $ Count = 30
    else:
        if Girl.PantsNum() > 5:

            $ Count = 25
        elif Girl.PantsNum() == 5:

            $ Count = 20
        elif Girl.PantiesNum() >= 8:

            $ Count = 25
        elif Girl.PantiesNum() >= 6:

            $ Count = 15
        elif Girl.PantiesNum() >= 4:

            $ Count = 10
        elif Girl.PantiesNum() >= 2:

            $ Count = 5


        if Girl.HoseNum() >= 10:

            $ Count = 25 if Count < 25 else Count

        if Girl.top == "_towel" and Count:

            $ Count = 25
        elif Girl.top == "_towel":

            $ Count = 15
    if not Check:

        pass
    elif Custom == 9 or Custom == 7:
        pass
    elif Girl == RogueX:
        if Count >= 20:
            if Girl.PantsNum() > 6:
                ch_r "Oh, I think these pants will work fine."
            elif Girl.PantsNum() == 5:
                ch_r "Oh, I think this skirt will work fine."
            elif Girl.HoseNum() >= 10:
                ch_r "Oh, these [Girl.hose] will work."
            elif Girl.underwear == "_shorts":
                ch_r "Oh, I think these shorts will work fine."
            elif Girl.top == "_towel":
                ch_r "The towel's an odd choice. . ."
            else:
                ch_r "Kinda breezy across my nethers, [Girl.player_petname]. . ."
            if not Girl.underwear and approval_check(Girl, 500, "I", TabM=0):
                ch_r "I kinda like going commando."
            elif not Girl.underwear:
                ch_r "Don't know about going commando though."
        elif Count >= 10 and (approval_check(Girl, 2000, TabM=0) or approval_check(Girl, 700, "I", TabM=0)):
            ch_r "These don't really leave much to the imagination. . ."
        elif Count >= 10:
            $ Girl.change_face("_angry", 1)
            ch_r "I'm warning you, I'm not running around in my panties. . ."
        elif (approval_check(Girl, 2500, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_r "Hmm, Breezy. . ."
        else:
            ch_r "So long as we stay inside. . ."
    elif Girl == KittyX:
        if Count >= 20:
            if Girl.PantsNum() >= 5:
                ch_k "and these pants look cute on me."
            elif Girl.legs == "_shorts":
                ch_k "and these are cute shorts."
            elif Girl.HoseNum() >= 10:
                ch_k "I guess these [Girl.hose] will work fine."
            elif Girl.top == "_towel":
                ch_k "The towel's an odd choice. . ."
            else:
                ch_k "This is kinda breezy."
            if not Girl.underwear and approval_check(Girl, 500, "I", TabM=0):
                ch_k "I like going without panties."
            elif not Girl.underwear:
                ch_k "It's a little uncomfortable without panties."
        elif Count >= 10 and (approval_check(Girl, 2000, TabM=0) or approval_check(Girl, 700, "I", TabM=0)):
            ch_k "I'm not sure about the coverage down here. . ."
        elif Count >= 10:
            $ Girl.change_face("_angry", 1)
            ch_k "I'm barely covered down here. . ."
        elif (approval_check(Girl, 2500, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_k "kinda chilly. . ."
        else:
            ch_k "if it's just[Girl.like]you and me. . ."
    elif Girl == EmmaX:
        if Count >= 20:
            if Girl.PantsNum() > 5:
                ch_e "and these pants always did suit me."
            elif Girl.PantsNum() >= 5:
                ch_e "and this skirt always did suit me."
            elif Girl.HoseNum() >= 10:
                ch_e "I guess these [Girl.hose] will work fine."
            elif Girl.top == "_towel":
                ch_e "I'm unsure about wearing a towel out, [Girl.player_petname]. . ."
            else:
                ch_e "I probably could wear something more downstairs, [Girl.player_petname]. . ."
            if not Girl.underwear:
                if approval_check(Girl, 500, "I", TabM=0):
                    ch_e "I do enjoy going without panties."
                else:
                    ch_e "I don't know about going without panties in this situation."
        elif Count >= 10:
            if approval_check(Girl, 2000, TabM=0) or approval_check(Girl, 700, "I", TabM=0):
                ch_e "I hope you don't expect me to wear this out. . ."
            else:
                $ Girl.change_face("_angry", 1)
                ch_e "I don't know about wearing this outside. . ."
        elif (approval_check(Girl, 2500, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_e "This really tests my limits."
        else:
            ch_e "I'll need to put something else on to leave the room though."
    elif Girl == LauraX:
        if Count >= 20:
            if Girl.PantsNum() > 5:
                ch_l "and these pants work."
            elif Girl.PantsNum() >= 5:
                ch_l "and this skirt works."
            elif Girl.HoseNum() >= 10:
                ch_l "and these [Girl.hose] will work fine."
            elif Girl.top == "_towel":
                ch_l "The towel's an odd choice. . ."
            else:
                ch_l "but there's a draft."
            if not Girl.underwear and approval_check(Girl, 500, "I", TabM=0):
                ch_l "Commando's cool."
            elif not Girl.underwear:
                ch_l "I might accidentally flash some people like this though."
        elif Count >= 10 and (approval_check(Girl, 2000, TabM=0) or approval_check(Girl, 700, "I", TabM=0)):
            ch_l "I don't think I'm fully covered. . ."
        elif Count >= 10:
            $ Girl.change_face("_angry", 1)
            ch_l "I'm not covered like this. . ."
        elif (approval_check(Girl, 2500, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_l "It's pretty minimal. . ."
        else:
            ch_l "I wouldn't show off my cooch either. . ."
    elif Girl == JeanX:
        if Count >= 20:
            if Girl.PantsNum() > 5:
                ch_j "I do like these pants. . ."
            elif Girl.PantsNum() >= 5:
                ch_j "I do like this skirt. . ."
            elif Girl.HoseNum() >= 10:
                ch_j "these [Girl.hose] will work fine."
            elif Girl.top == "_towel":
                ch_j "A towel though? . ."
            else:
                ch_j "kinda exposed here. . ."
            if not Girl.underwear and approval_check(Girl, 500, "I", TabM=0):
                ch_j "I don't mind doing without the panties. . ."
            elif not Girl.underwear:
                ch_j "I'd kinda need panties with this. . ."


        elif Count >= 10:
            if (approval_check(Girl, 2000, TabM=0) or approval_check(Girl, 700, "I", TabM=0)):
                $ Girl.change_face("_sly", 1)
            else:
                $ Girl.change_face("_angry", 1)
            ch_j "So you want my puss on display? . ."
        elif (approval_check(Girl, 2500, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_j "This is basically \"nothing\". . ."
        else:
            ch_j "I'm not interested in showing off the goods. . ."
    elif Girl == StormX:
        if Girl.PantsNum() > 5:
            ch_s "and these pants always did suit me."
        elif Girl.PantsNum() >= 5:
            ch_s "and this skirt always did suit me."
        elif Girl.HoseNum() >= 10:
            ch_s "I supposed that these [Girl.hose] will work fine."
        elif Girl.top == "_towel":
            ch_s "I'm unsure about wearing a towel out, [Girl.player_petname]. . ."
        else:
            ch_s "A rather breezy ensemble, [Girl.player_petname]. . ."
        if not Girl.underwear:
            if approval_check(Girl, 500, "I", TabM=0):
                ch_s "I do enjoy doing without panties."
            else:
                ch_s "Certainly quite exposed without panties. . ."
        if Count >= 10 and StormX not in Rules:
            $ Girl.change_face("_bemused", 1)
            ch_s "I don't know that Charles would let me roam the halls in such an exposed state."
        elif StormX in Rules and (approval_check(Girl, 1200, TabM=0) or approval_check(Girl, 500, "I", TabM=0)):
            ch_s "This is quite the daring look you've put together."
        else:
            ch_s "I doubt Charles would let me roam the halls in such an exposed state."
    elif Girl == JubesX:
        if Count >= 20:
            if Girl.PantsNum() > 6:
                ch_v "and these pants work."
            elif Girl.PantsNum() >= 6:
                ch_v "and these shorts work."
            elif Girl.PantsNum() >= 5:
                ch_v "and this skirt works."
            elif Girl.HoseNum() >= 10:
                ch_v "and these [Girl.hose] will work fine."
            elif Girl.top == "_towel":
                ch_v "The towel's an odd choice. . ."
            else:
                ch_v "but I don't know about this. . ."
            if not Girl.underwear and approval_check(Girl, 500, "I", TabM=0):
                ch_v "I guess we're not doing panties now?"
            elif not Girl.underwear:
                ch_v "I don't think I'd want to go without panties. . ."
        elif Count >= 10 and (approval_check(Girl, 2000, TabM=0) or approval_check(Girl, 700, "I", TabM=0)):
            ch_v "This is pretty skimpy. . ."
        elif Count >= 10:
            $ Girl.change_face("_angry", 1)
            ch_v "This is pretty skimpy. . ."
        elif (approval_check(Girl, 2500, TabM=0) or approval_check(Girl, 800, "I", TabM=0)):
            ch_v "Wow, this look is. . . a lot. . ."
        else:
            ch_v "I don't really go around showing the goods. . ."


    $ Tempshame -= Count

    if Check:

        if Check == 2:
            ch_p "So can I see it then?"
        elif Custom == 4:
            ch_p "So would you work out in that?"
        elif Custom == 7:
            ch_p "So would you sleep in that?"
        else:
            ch_p "So would you wear that outside?"

        $ Girl.change_face("_sexy", 0)
        if Girl.PantsNum() > 2:
            pass
        elif Girl == StormX and StormX in Rules:
            pass
        elif Girl.PantiesNum() > 2 and (Girl.SeenPanties or approval_check(Girl, 900, TabM=0)):
            pass
        elif Girl.SeenPussy or approval_check(Girl, 1200, TabM=0):
            pass
        else:
            $ Agree = 0

        if not Agree:
            pass
        elif Girl == StormX and StormX in Rules:
            pass
        elif Girl.OverNum() > 2:
            pass
        elif Girl.ChestNum() > 2 and (Girl.SeenChest or approval_check(Girl, 900, TabM=0)):
            pass
        elif Girl.SeenChest or approval_check(Girl, 1200, TabM=0):
            pass
        else:
            $ Agree = 0

        if Check == 2 and Agree:

            $ Girl.Shame = Tempshame
            $ Girl.change_face("_sly")
            if Girl == RogueX:
                ch_r "This ain't a bad look, I guess. . ."
            elif Girl == KittyX:
                ch_k "I suppose you've put together a cute little outfit. . ."
            elif Girl == EmmaX:
                ch_e "I suppose I could pull this off. . ."
            elif Girl == LauraX:
                ch_l "Huh, this'll work. . ."
            elif Girl == JeanX:
                ch_j "It does look good on me. . ."
            elif Girl == StormX:
                ch_s "I don't see why not. . ."
            elif Girl == JubesX:
                ch_v "Sure, take a look. . ."
            hide DressScreen
            return 1
        if not Agree:

            $ Girl.change_face("_bemused", 2,Eyes="_side")
            if Girl == RogueX:
                ch_r "I don't really feel comfortable in this. . ."
            elif Girl == KittyX:
                ch_k "I don't think I'd be comfortable with you seeing me like this. . ."
            elif Girl == EmmaX:
                ch_e "I wouldn't want to blind you. . ."
            elif Girl == LauraX:
                ch_l "You'll have to earn it."
            elif Girl == JeanX:
                ch_j "It's cute, yeah, but I can't go out in it."
            elif Girl == StormX:
                ch_s "I think you're making fun of me. . ."
            elif Girl == JubesX:
                ch_v "I really can't let you see this. . ."
            menu:
                extend ""
                "Ok then, you can put your normal clothes back on.":
                    $ Girl.change_outfit(Changed=1)
                    hide DressScreen
                "Ok, we can keep tweaking it.":
                    pass
            $ Girl.change_face("_smile", 1)
            if Girl == RogueX:
                ch_r "Thanks, [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "Thanks."
            elif Girl == EmmaX:
                ch_e "Appreciated."
            elif Girl == LauraX:
                ch_l "Thanks."
            elif Girl == JeanX:
                ch_j ". . . that's what I said."
            elif Girl == StormX:
                ch_s "Very well. . ."
            elif Girl == JubesX:
                ch_v "Cool, cool. . ."
            return
        if Girl == RogueX:
            if Girl.Taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_r "It's a little late to worry about that, right?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_r "Hmm. . . yeah, I'd love to. . ."
                $ Girl.change_stat("lust", 80, 10)
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_r "A bit scandalous, but yeah."
                elif Tempshame >= 15:
                    ch_r "Yeah, you're worth it."
                else:
                    ch_r "Sure, it's cute."
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_r "Yeah, I think I like this style, I'd wear this."
            elif Tempshame <= 15:
                if approval_check(Girl, 1700, TabM=0, C = 0) or approval_check(Girl, 400, "I", TabM=0, C = 0):
                    ch_r "It's pretty skimpy, but I can make it work."
                else:
                    $ Girl.change_face("_bemused", 1)
                    ch_r "I think this looks is a bit daring to wear."
                    $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_r "Sure, I can swim in this. . ."
            elif Tempshame <= 25:
                if approval_check(Girl, 2300, TabM=0, C = 0) or approval_check(Girl, 700, "I", TabM=0, C = 0):
                    ch_r "Kinky, but I can rock this."
                else:
                    $ Girl.change_face("_angry", 1)
                    ch_r "I'm definitely not going out in this."
                    $ Agree = 0
            elif approval_check(Girl, 2500, TabM=0, C = 0) or approval_check(Girl, 800, "I", TabM=0, C = 0):
                $ Girl.change_face("_bemused", 1)
                ch_r "I can't believe it. . . but yeah."
            else:
                $ Girl.change_face("_angry", 1)
                ch_r "You have got to be kidding."
                $ Agree = 0
        elif Girl == KittyX:
            if Girl.Taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_k "Kinda late to ask, right?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_k "I'm getting wet just thinking about it. . ."
                $ Girl.change_stat("lust", 80, 10)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_k "Sure, it's a cute look!"
            elif Tempshame <= 15 and (approval_check(Girl, 1700, TabM=0, C = 0) or approval_check(Girl, 400, "I", TabM=0, C = 0)):
                ch_k "It's pretty hot, right?"
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_k "This is[Girl.like]pretty exposed, but ok."
                elif Tempshame >= 15:
                    ch_k "It's kinda naughty, I like it."
                else:
                    ch_k "Yeah, these are fine."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_k "It's too slutty to wear out."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_k "This is a cute swimsuit. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, TabM=0, C = 0) or approval_check(Girl, 700, "I", TabM=0, C = 0)):
                ch_k "So sexy, but I can handle it."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_k "{i}Way{/i} too sexy for outside."
                $ Agree = 0
            elif (approval_check(Girl, 2500, TabM=0, C = 0) or approval_check(Girl, 800, "I", TabM=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_k "OMG, I can't believe I'm doing this."
            else:
                $ Girl.change_face("_angry", 1)
                ch_k "I - can't - even."
                $ Agree = 0
        elif Girl == EmmaX:
            if Girl.Taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                "She glances around."
                ch_e "Is that a trick question?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_e "The thought of it gets me moist. . ."
                $ Girl.change_stat("lust", 80, 10)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_e "Yes, it's a fine choice."
            elif Tempshame <= 15 and (approval_check(Girl, 1700, TabM=0, C = 0) or approval_check(Girl, 400, "I", TabM=0, C = 0)):
                ch_e "Rather daring, how could I resist?"
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_e "You understand I only wear this sort of thing in private."
                else:
                    ch_e "It is a comfortable outfit."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_e "Rather too daring, don't you think?"
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_e "Fine, this is decent swimwear. . ."
            elif Tempshame >= 15 and "public" not in Girl.history:
                ch_e "I doubt I could get away with this in public, [Girl.player_petname]."
                $ Agree = 0
            elif Tempshame <= 25 and (approval_check(Girl, 2300, TabM=0, C = 0) or approval_check(Girl, 700, "I", TabM=0, C = 0)):
                ch_e "This is particularly inappropriate. . . in the best ways."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_e "I don't believe even I could pull off this look, [Girl.player_petname]."
                $ Agree = 0
            elif (approval_check(Girl, 2500, TabM=0, C = 0) or approval_check(Girl, 800, "I", TabM=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_e "This look certainly pushes the boundaries."
            else:
                $ Girl.change_face("_angry", 1)
                ch_e "Even I can't pull this off."
                $ Agree = 0
        elif Girl == LauraX:
            if Girl.Taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_l "Well a bit late for that, I guess."
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                $ Girl.change_stat("lust", 80, 10)
                $ Girl.change_face("_sexy", 2)
                ch_l ". . ."
                $ Girl.change_face("_sexy", 1)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_l "I don't see why not."
            elif Tempshame <= 15 and (approval_check(Girl, 1700, TabM=0, C = 0) or approval_check(Girl, 400, "I", TabM=0, C = 0)):
                ch_l "It looks good, right?"
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_l "Sure, perv."
                elif Tempshame >= 15:
                    ch_l "Sure, why not."
                else:
                    ch_l "Yeah, I guess."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_l "I can't move freely in this without showing off the goods."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_l "Yeah, I can swim in this. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, TabM=0, C = 0) or approval_check(Girl, 700, "I", TabM=0, C = 0)):
                ch_l "I can handle this."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_l "Nah, too slutty."
                $ Agree = 0
            elif (approval_check(Girl, 2500, TabM=0, C = 0) or approval_check(Girl, 800, "I", TabM=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_l "Pretty daring, eh?"
            else:
                $ Girl.change_face("_angry", 1)
                ch_l "As if."
                $ Agree = 0
        elif Girl == JeanX:
            if Girl.Taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_j "Well, I guess so, right?"
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                $ Girl.change_stat("lust", 80, 10)
                $ Girl.change_face("_sexy", 2)
                ch_j ". . ."
                $ Girl.change_face("_sexy", 1)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_j "Sure, whatever."
            elif Tempshame <= 15 and (approval_check(Girl, 1700, TabM=0, C = 0) or approval_check(Girl, 400, "I", TabM=0, C = 0)):
                ch_j "I almost have to. . ."
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_j "If it'll keep you hard. . ."
                elif Tempshame >= 15:
                    ch_j "Yeah, sure."
                else:
                    ch_j "Why not."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_j "I can pull this one off. . ."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_j "Yeah, sure."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, TabM=0, C = 0) or approval_check(Girl, 700, "I", TabM=0, C = 0)):
                ch_j "This'll turn some heads. . ."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_j "I wouldn't want to break anyone. . ."
                $ Agree = 0
            elif (approval_check(Girl, 2500, TabM=0, C = 0) or approval_check(Girl, 800, "I", TabM=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_j "Kinky, but sure."
            else:
                $ Girl.change_face("_angry", 1)
                ch_j "You have to be joking."
                $ Agree = 0
        elif Girl == StormX:

            if Girl.Taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                "She glances around."
                ch_s "It seems a bit late for that question. . ."
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                ch_s "I do find the idea. . . exciting. . ."
                $ Girl.change_stat("lust", 80, 10)
            elif Tempshame <= 10:
                $ Girl.change_face("_smile")
                ch_s "Yes, it's a fine choice."
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 20:
                    ch_s "This is a fine outfit."
                else:
                    ch_s "It may be a bit more than I'm used to. . ."
            elif StormX in Rules:
                ch_s "I don't see why not. . ."
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_s "I suppose I could swim well like this. . ."
            elif Tempshame <= 20 and (approval_check(Girl, 1700, TabM=0, C = 0) or approval_check(Girl, 400, "I", TabM=0, C = 0)):
                ch_s "This certainly does push the limits of good taste. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, TabM=0, C = 0) or approval_check(Girl, 700, "I", TabM=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_s "I doubt Charles would approve, but so what?"
            elif Tempshame <= 25:
                $ Girl.change_face("_bemused", 1)
                ch_s "I'm afraid that Charles would never approve."
                $ Agree = 0
            elif (approval_check(Girl, 2500, TabM=0, C = 0) or approval_check(Girl, 800, "I", TabM=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_s "I doubt Charles would approve, but so what?"
            else:
                $ Girl.change_face("_bemused", 1)
                ch_s "I'm afraid that Charles would never approve."
                $ Agree = 0
        elif Girl == JubesX:
            if Girl.Taboo >= 40:
                $ Girl.change_face("_confused",1)
                $ Girl.mouth = "_smile"
                ch_v "I guess that ship has sailed. . ."
            if "exhibitionist" in Girl.traits and Tempshame >= 20:
                $ Girl.change_stat("lust", 80, 10)
                $ Girl.change_face("_sexy", 2)
                ch_v ". . ."
                $ Girl.change_face("_sexy", 1)
            elif Tempshame <= 5:
                $ Girl.change_face("_smile")
                ch_v "I guess?"
            elif Tempshame <= 15 and (approval_check(Girl, 1700, TabM=0, C = 0) or approval_check(Girl, 400, "I", TabM=0, C = 0)):
                ch_v "It looks totally hot, right?"
            elif Custom == 7:

                $ Girl.change_face("_bemused", 1)
                if Tempshame >= 30:
                    ch_v "Whatever, perv."
                elif Tempshame >= 15:
                    ch_v "Sure, why not."
                else:
                    ch_v "Sure, I guess."
            elif Tempshame <= 15:
                $ Girl.change_face("_bemused", 1)
                ch_v "I think this is too breezy."
                $ Agree = 0
            elif Custom == 10 and Tempshame <= 20:

                $ Girl.change_face("_bemused", 1)
                ch_v "I could swim in this. . ."
            elif Tempshame <= 25 and (approval_check(Girl, 2300, TabM=0, C = 0) or approval_check(Girl, 700, "I", TabM=0, C = 0)):
                ch_v "I guess this is fine. . ."
            elif Tempshame <= 25:
                $ Girl.change_face("_angry", 1)
                ch_v "I really couldn't wear this out."
                $ Agree = 0
            elif (approval_check(Girl, 2500, TabM=0, C = 0) or approval_check(Girl, 800, "I", TabM=0, C = 0)):
                $ Girl.change_face("_bemused", 1)
                ch_v "It's pretty hot, right?"
            else:
                $ Girl.change_face("_angry", 1)
                ch_v "As if."
                $ Agree = 0



        if Custom == 5:
            $ Girl.Custom2 = [2,Girl.arms,Girl.legs,Girl.top,Girl.neck,Girl.bra,Girl.underwear,Girl.accessory,Girl.hair,Girl.hose,Tempshame]
            $ Girl.Custom2[0] = 2 if Agree else 1
            call Clothing_Schedule_Check (Girl, 5, 1)
        elif Custom == 6:
            $ Girl.Custom3 = [2,Girl.arms,Girl.legs,Girl.top,Girl.neck,Girl.bra,Girl.underwear,Girl.accessory,Girl.hair,Girl.hose,Tempshame]
            $ Girl.Custom3[0] = 2 if Agree else 1
            call Clothing_Schedule_Check (Girl, 6, 1)
        elif Custom == 4:
            if Agree:
                $ Girl.Gym = [2,Girl.arms,Girl.legs,Girl.top,Girl.neck,Girl.bra,Girl.underwear,Girl.accessory,Girl.hair,Girl.hose,Tempshame]
                call Clothing_Schedule_Check (Girl, 4, 1)
        elif Custom == 7:
            $ Girl.sleepwear = [2,Girl.arms,Girl.legs,Girl.top,Girl.neck,Girl.bra,Girl.underwear,Girl.accessory,Girl.hair,Girl.hose,Tempshame]
            $ Girl.sleepwear[0] = 2 if Agree else 1
        elif Custom == 10:
            if Agree:
                $ Girl.Swim = [2,Girl.arms,Girl.legs,Girl.top,Girl.neck,Girl.bra,Girl.underwear,Girl.accessory,Girl.hair,Girl.hose,Tempshame]
        elif Custom == 3:
            $ Girl.Custom1 = [2,Girl.arms,Girl.legs,Girl.top,Girl.neck,Girl.bra,Girl.underwear,Girl.accessory,Girl.hair,Girl.hose,Tempshame]
            $ Girl.Custom1[0] = 2 if Agree else 1
            call Clothing_Schedule_Check (Girl, 3, 1)
        else:
            "Tell Oni Custom Outfit was [Custom]"
            $ RogueX.gibberish = 5
    elif Girl.Taboo <= 20:

        $ Tempshame /= 2

    $ Girl.Shame = Tempshame

    if Custom == 20:

        return

    if Check:
        pass
    elif bg_current == "HW Party" or (bg_current == "bg_player" and "halloween" in Player.daily_history):

        pass
    elif "exhibitionist" in Girl.traits and Tempshame <= 20:

        pass
    elif Girl == StormX and StormX in Rules:
        pass
    elif Tempshame <= 12:

        pass
    elif Girl.top == "_towel" and Girl.location == "bg_showerroom":

        pass
    elif Tempshame <= 15 and (approval_check(Girl, 1500) or approval_check(Girl, 500, "I")):

        pass
    elif Tempshame <= 20 and (Girl.location == "bg_dangerroom" or Girl.location == "bg_pool"):

        pass
    elif Tempshame <= 20 and (approval_check(Girl, 1800) or approval_check(Girl, 650, "I")):

        pass
    elif Tempshame <= 25 and (approval_check(Girl, 2000) or approval_check(Girl, 700, "I")):

        pass
    elif (approval_check(Girl, 2500) or approval_check(Girl, 800, "I")):

        pass
    elif Girl.location == "bg_dangerroom" and Girl.Outfit == "gym":
        $ Girl.change_outfit("gym",Changed = 1)
    elif not Girl.Taboo:
        pass
    elif Girl.Outfit == "swimwear" and bg_current == "bg_pool":
        pass
    elif bg_current == "bg_pool" and Girl.ChestNum() >= 3 and Girl.PantiesNum() >= 6:
        pass
    elif Girl.Outfit == "gym" and bg_current == "bg_dangerroom":
        pass
    else:

        if Girl.location == bg_current:
            if Girl == RogueX:
                ch_r "I'll be right back, I've got to change out of this."
            elif Girl == KittyX:
                ch_k "One sec, I gotta change real quick."
            elif Girl == EmmaX:
                ch_e "I'm afraid I'll have to change, one moment."
            elif Girl == LauraX:
                ch_l "One sec, I gotta change real quick."
            elif Girl == JeanX:
                ch_j "Wait while I get changed."
            elif Girl == StormX:
                ch_s "I'll need to change into something more substantial."
            elif Girl == JubesX:
                ch_v "I need to throw something on real quick. . ."
        if Girl.location == "bg_dangerroom":
            $ Girl.Outfit =  "gym"
        elif Girl.location == "bg_pool" and Girl.Swim[0]:
            $ Girl.Outfit =  "swimwear"
        else:
            $ Girl.Outfit = renpy.random.choice(["casual1", "casual2"])

        $ Girl.add_word(1,"modesty", "modesty")
        $ Girl.Water = 0
        $ Girl.change_outfit(Changed=1)
        if Girl == RogueX:
            ch_r "That wasn't really \"outdoor ready\"."
        elif Girl == KittyX:
            ch_k "I just needed to throw some more on."
        elif Girl == EmmaX:
            ch_e "I wouldn't want to be \"inappropriate\"."
        elif Girl == LauraX:
            ch_l "That wasn't really \"outdoors\" wear."
        elif Girl == JeanX:
            ch_j "Couldn't really be out in that."
        elif Girl == StormX:
            ch_s "I'm afraid Charles would not approve of that look around students."
        elif Girl == JubesX:
            ch_v "That was kinda. . . private. . ."
    return





label QuickOutfitCheck(Girl=0, Custom=3, Count=0, Tempshame=50, Agree=1, HolderOutfit=[]):





    $ Girl = GirlCheck(Girl)

    if Custom == 3:
        $ HolderOutfit = Girl.Custom1[:]
    elif Custom == 5:
        $ HolderOutfit = Girl.Custom2[:]
    elif Custom == 6:
        $ HolderOutfit = Girl.Custom3[:]


    elif Custom == 7:
        $ HolderOutfit = Girl.sleepwear[:]
    elif Custom == 4:
        $ HolderOutfit = Girl.Gym[:]
    elif Custom == 10:
        $ HolderOutfit = Girl.Swim[:]
    else:
        "Tell Oni, Outfit check, [Custom]."
        return




    while len(HolderOutfit) < 11:
        $ HolderOutfit.append(0)

    if HolderOutfit[5] in ("_tank", "white_tank", "button_tank", "_sports_bra", "_tube_top", "corset"):
        $ Count = 20
    elif HolderOutfit[5] == "wolvie_top":
        $ Count = 10
    elif HolderOutfit[5] in ("lace_bra", "lace corset"):
        $ Count = 5
    elif HolderOutfit[5]:

        $ Count = 10
    elif HolderOutfit[7] == "suspenders" or HolderOutfit[7] == "suspenders2":
        $ Count = 5
    else:
        $ Count = 0


    if HolderOutfit[3] in ("nighty", "_mesh_top"):
        $ Count += 5
    elif HolderOutfit[3] == "_towel":
        if Girl == EmmaX:
            $ Count += 5
        elif Girl == StormX:
            pass
        else:
            $ Count += 10
    elif HolderOutfit[3] in ("jacket", "dress", "_pink_top") or HolderOutfit[7] == "jacket":
        $ Count += 15
    elif HolderOutfit[3] or HolderOutfit[7] == "shut_jacket":
        $ Count += 20

    if Girl.piercings and Count <= 10:
        $ Count = -5

    $ Count = 20 if Count >= 20 else Count

    $ Tempshame -= Count
    $ Count = 0

    if HolderOutfit[2] and HolderOutfit[6]:
        $ Count = 30
    elif HolderOutfit[2] in ("blue_skirt", "_skirt", "other_skirt"):
        $ Count = 20
    elif HolderOutfit[2] or HolderOutfit[7] == "shut_jacket":
        $ Count = 25
    elif HolderOutfit[6] == "_shorts":
        $ Count = 25
    elif HolderOutfit[6] in ("_bikini_bottoms", "sports_panties", "_shorts"):
        $ Count = 15
    elif HolderOutfit[6] == "lace_panties":
        $ Count = 5
    elif HolderOutfit[6]:
        $ Count = 10

    if HolderOutfit[9] == "_tights":

        $ Count = 25 if Count < 25 else Count

    if HolderOutfit[3] == "_towel" and Girl not in (EmmaX,StormX):

        $ Count = 25 if Count else 15

    $ Tempshame -= Count

    if "exhibitionist" in Girl.traits:
        pass
    elif Tempshame <= 5:
        pass
    elif Tempshame <= 15 and (approval_check(Girl, 1700, TabM=0, C = 0) or approval_check(Girl, 400, "I", TabM=0, C = 0)):
        pass
    elif Custom == 10 and Tempshame <= 20:

        pass
    elif Girl == EmmaX and Tempshame >= 15 and "public" not in Girl.history:
        $ Agree = 0
    elif Girl == StormX and StormX in Rules:
        pass
    elif Tempshame <= 25:
        if approval_check(Girl, 2300, TabM=0, C = 0) or approval_check(Girl, 700, "I", TabM=0, C = 0):
            pass
        else:
            $ Agree = 0
    elif (approval_check(Girl, 2500, TabM=0, C = 0) or approval_check(Girl, 800, "I", TabM=0, C = 0)):
        pass
    else:
        $ Agree = 0




    if Custom == 3:

        $ Girl.Custom1[0] = 2 if Agree else 1
        call Clothing_Schedule_Check (Girl, 3, 1)
    elif Custom == 5:

        $ Girl.Custom2[0] = 2 if Agree else 1
        call Clothing_Schedule_Check (Girl, 5, 1)
    elif Custom == 6:

        $ Girl.Custom3[0] = 2 if Agree else 1
        call Clothing_Schedule_Check (Girl, 6, 1)
    elif Custom == 4:


        $ Girl.Gym[0] = 2 if Agree else 1
        call Clothing_Schedule_Check (Girl, 4, 1)
    elif Custom == 7:

        $ Girl.sleepwear[0] = 2 if Agree else 1
    elif Custom == 10:


        $ Girl.Swim[0] = 2 if Agree else 1
    else:
        "Tell Oni Custom Outfit was [Custom]"
        $ RogueX.gibberish = 5
    return




label AutoStrip(Girl=0):

    $ Girl = GirlCheck(Girl)
    if (Girl.underwear and not Girl.underwear_pulled_down) or Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
        if Girl == RogueX:
            ch_r "Well, I guess some things are necessary, [RogueX.player_petname]."
        elif Girl == KittyX:
            ch_k "We can't exactly do much like this, huh."
        elif Girl == EmmaX:
            ch_e "I suppose we can't do much with all this on."
        elif Girl == LauraX:
            ch_l "Huh. . ."
        elif Girl == JeanX:
            ch_j "Huh. . ."
        elif Girl == StormX:
            ch_s "I suppose our options are limited with these on."
        elif Girl == JubesX:
            ch_v "Let's get these out of the way. . ."

        if (Girl.underwear and not Girl.underwear_pulled_down) and (Girl.PantsNum() > 6 and not Girl.upskirt):
            "She quickly drops her pants and her [Girl.underwear]."
        elif (Girl.underwear and not Girl.underwear_pulled_down) and (Girl.PantsNum() == 6 and not Girl.upskirt):
            "She quickly drops her shorts and her [Girl.underwear]."
        elif Girl.PantsNum() > 6 and not Girl.upskirt:
            "She tugs her pants down, exposing her bare pussy."
        elif Girl.PantsNum() == 6 and not Girl.upskirt:
            "She tugs her shorts down, exposing her bare pussy."
        elif Girl.HoseNum() >= 6 and (Girl.underwear and not Girl.underwear_pulled_down):
            "She tugs her [Girl.hose] and [Girl.underwear] off."

        elif Girl.HoseNum() >= 6:
            "She tugs her [Girl.hose] off and drops them to the ground."

        elif (Girl.underwear and not Girl.underwear_pulled_down):
            "She tugs her [Girl.underwear] off and drops them to the ground."

    $ Girl.upskirt = 1 if Girl.legs else 0
    $ Girl.underwear_pulled_down = 1 if Girl.underwear else 0
    $ Girl.hose = "" if Girl.HoseNum() >= 6 else Girl.hose

    $ Girl.SeenPanties = 1
    call expression Girl.tag + "_First_Bottomless"
    return

label Girl_Undress(Girl=0, Region="ask", stored_count=0):

    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    $ stored_count = approval_bonus
    if Partner == Girl:
        $ approval_bonus = 0
    call shift_focus (Girl)

    if Region == "auto":
        if Girl.upskirt and Girl.underwear_pulled_down:
            return
        if Girl.PantsNum() > 5 and approval_bonus < 20:
            $ approval_bonus = 20
        if Girl.lust >= 90:
            $ approval_bonus += 10
        elif Girl.lust >= 80:
            $ approval_bonus += 5
        $ action_context = "auto"
        call Bottoms_Off (Girl, 0)

    if Region == "ask":
        menu:
            "Which parts?"
            "Her top" if Girl.top or Girl.bra or Girl.arms or Girl.accessory:
                $ Region = "top"
            "Her bottoms" if Girl.legs or Girl.underwear or Girl.hose or Girl.accessory:
                $ Region = "bottom"
            "A little of both. . ." if Girl.top or Girl.bra or Girl.legs or Girl.underwear or Girl.hose or Girl.accessory:
                $ Region = "both"
            "Never mind":
                pass

    if Region == "top":
        if Girl.top or Girl.bra:
            call Top_Off (Girl, 0)
    elif Region == "bottom":
        if Girl.legs or Girl.underwear or Girl.hose:
            call Bottoms_Off (Girl, 0)
    elif Region == "both":
        if Girl.top or Girl.bra:
            call Top_Off (Girl, 0)

        if Partner == Girl:
            $ approval_bonus = 0
        else:
            $ approval_bonus = stored_count

        if "_angry" in Girl.recent_history:
            pass
        elif not Girl.legs and not Girl.underwear and not Girl.hose:
            pass
        elif "no_topless" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "You might want to rethink your next question."
            elif Girl == KittyX:
                ch_k "Don't push it. . ."
            elif Girl == EmmaX:
                ch_e "Care to push your luck?"
            elif Girl == LauraX:
                ch_l "Know when to fold'em, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j "Ha! Keep trying, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I do not see this going your way. . ."
            elif Girl == JubesX:
                ch_v "Well now you're pushing it. . ."
            menu:
                extend ""
                "And now the bottoms?":
                    call Bottoms_Off (Girl, 0)
                "You're probably right, sorry.":
                    pass
        else:
            ch_p "And now the bottoms?"
            call Bottoms_Off (Girl, 0)

    $ approval_bonus = stored_count
    return



label Top_Off(Girl=0, Intro=1, Line=0, counter=0):

    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    if not Girl.top and not Girl.bra:

        $ approval_bonus = 0
        return

    if "_angry" in Girl.recent_history:
        if Girl == RogueX:
            ch_r "I'm just too annoyed to deal with this right now."
        elif Girl == KittyX:
            ch_k "No titties for you."
        elif Girl == EmmaX:
            ch_e "I'm in no mood, [Girl.player_petname]."
        elif Girl == LauraX:
            ch_l "Don't push it, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "No way, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "These are not for your enjoyment."
        elif Girl == JubesX:
            ch_v "The top stays on. . ."
        return

    if Girl.SeenChest and approval_check(Girl, 500) and not Taboo:

        $ approval_bonus += 20
    if "exhibitionist" in Girl.traits:
        $ approval_bonus += (4*Taboo)
    if Girl in Player.Harem or "sex friend" in Girl.player_petnames and not Taboo:
        $ approval_bonus += 10
    elif "ex" in Girl.traits:
        $ approval_bonus -= 40
    if "no_topless" in Girl.recent_history:
        $ approval_bonus -= 10
    elif Girl == StormX and (not Taboo or Girl in Rules):

        $ approval_bonus += 20


    if Intro and not Girl.top_pulled_up:
        if Intro == 2:

            if Girl == RogueX:
                ch_r "I don't know, you'd have to touch them. . ."
            elif Girl == KittyX:
                ch_k "So, you'd have to be able to[KittyX.like]touch them, I guess. . ."
            elif Girl == EmmaX:
                ch_e "I would probably need to be bare-chested to get anything out of that. . ."
            elif Girl == LauraX:
                ch_l "I'd need to be topless to get anything from that. . ."
            elif Girl == JeanX:
                ch_j "I guess I'd have to go topless. . ."
            elif Girl == StormX:
                ch_s "If direct contact is necessary. . ."
            elif Girl == JubesX:
                ch_v "Well, I'd need to be topless for that to. . ."
        else:
            if Girl.top:
                ch_p "This might be easier without your [Girl.top] on."
            elif Girl.bra:
                ch_p "This might be easier without your [Girl.bra] on."


    $ approval = approval_check(Girl, 1100, TabM = 4)

    if action_context == "auto" and  (Girl.top or Girl.bra or (Girl == JubesX and Girl.accessory)) and not Girl.top_pulled_up:
        $ Line = 0
        if approval_check(Girl, 1250, TabM = 1) or (Girl.SeenChest and approval_check(Girl, 500) and not Taboo):

            $ Girl.change_stat("inhibition", 70, 1)
            $ Girl.top_pulled_up = 1
            $ Line = Girl.top if Girl.top else Girl.bra
            "[Girl.name] sighs in frustration, and pulls her [Line] up over her breasts."
            if Girl == RogueX:
                ch_r "I just wasn't getting much out of it that way."
            elif Girl == KittyX:
                ch_k "I[Girl.like]wasn't feeling it that way."
            elif Girl == EmmaX:
                ch_e "Sometimes only direct contact will do."
            elif Girl == LauraX:
                ch_l "That wasn't working out."
            elif Girl == JeanX:
                ch_j "Ok, try that now, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "Does that work better?"
            elif Girl == JubesX:
                ch_v "Ok, that's more comfortable. . ."
            if Taboo:
                $ Girl.change_stat("inhibition", 90, (int(Taboo/20)))
            call expression Girl.tag + "_First_Topless" pass (1)
        elif Girl.top and Girl.bra and approval_check(Girl, 800, TabM = 1):

            $ Girl.change_stat("inhibition", 40, 1)
            $ Line = Girl.top
            $ Girl.top = ""
            if Girl == KittyX:
                "[Girl.name] sighs in frustration, and her [Line] drops to the ground."
            elif Girl == JubesX:
                if Girl.accessory:
                    $ Girl.accessory = ""
                    "[Girl.name] sighs in frustration, and shrugs off her Jacket, before pulling her [Line] over her head."
                else:
                    "[Girl.name] sighs in frustration, and pulls her [Line] over her head, throwing it aside."
            else:
                "[Girl.name] sighs in frustration, and pulls her [Line] over her head, throwing it aside."
            if Girl == RogueX:
                ch_r "I just wasn't getting much out of it that way."
            elif Girl == KittyX:
                ch_k "I[Girl.like]wasn't feeling it that way."
            elif Girl == EmmaX:
                ch_e "I just wasn't getting much out of it that way."
            elif Girl == LauraX:
                ch_l "That wasn't working out."
            elif Girl == JeanX:
                ch_j "Ok, try that now, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "Does that work better?"
            elif Girl == JubesX:
                ch_v "Ok, that's a bit better. . ."


        $ Line = 0
        return

    if approval >= 2:

        if "no_topless" in Girl.daily_history:
            if Girl == RogueX:
                ch_r "Ok, fine, top off."
            elif Girl == KittyX:
                ch_k "Okay, okay!"
            elif Girl == EmmaX:
                ch_e "{i}Fine,{/i} if that will shut you up."
            elif Girl == LauraX:
                ch_l "{i}Fine,{/i} but don't think I'm getting soft on you."
            elif Girl == JeanX:
                ch_j "Oh, fine. . ."
            elif Girl == StormX:
                ch_s "Oh, if you insist. . ."
            elif Girl == JubesX:
                ch_v "Well if you insist. . ."
        $ Girl.change_face("_sexy", 1)
        if Girl.Forced:
            $ Girl.change_face("_sad", 1)
            $ Girl.change_stat("love", 20, -2, 1)
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
        $ Girl.change_stat("inhibition", 50, 3)
        $ counter = 1
        while (Girl.bra or Girl.top or (Girl == JubesX and Girl.accessory)) and counter:
            if Girl == RogueX:
                ch_r "So, [Girl.player_petname]. Did you want me to take my top off?"
            elif Girl == KittyX:
                ch_k "So[Girl.like]how much did you want me to take off?"
            elif Girl == EmmaX:
                ch_e "What was it you were interested in, [Girl.player_petname]?"
            elif Girl == LauraX:
                ch_l "What did you want to see, [Girl.player_petname]?"
            elif Girl == JeanX:
                ch_j "Oh, what were you looking to see, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "What should I remove?"
            elif Girl == JubesX:
                ch_v "Ok then, so what did you want off?"
            menu:
                extend ""


                "Why don't you lose the jacket?" if Girl == JubesX and Girl.accessory:
                    $ Girl.accessory = ""
                    "[Girl.name] shrugs her jacket off."

                "Lose the [Girl.top]." if Girl.top:
                    $ Girl.change_face("_bemused", 1)
                    $ Line = Girl.top
                    $ Girl.top = ""
                    if Girl == KittyX:
                        "[Girl.name] shrugs and her [Line] falls through to the ground."
                    else:
                        "[Girl.name] pulls her [Line] off and tosses it aside."

                "Why don't you lose the [Girl.neck]?" if Girl.neck:
                    $ Line = Girl.neck
                    $ Girl.neck = ""
                    "[Girl.name] pulls her [Line] off."

                "Just lose the [Girl.bra]." if Girl.top and Girl.bra:
                    $ Girl.change_face("_bemused", 1)
                    $ Line = Girl.bra
                    $ Girl.bra = ""
                    if Girl == KittyX:
                        "[Girl.name] reaches through her top and pulls her [Line] free, dropping it to the ground."
                    else:
                        "[Girl.name] slowly removes her [Line] from under the [Girl.top]."
                "Lose the [Girl.bra]." if not Girl.top and Girl.bra:
                    $ Girl.change_face("_bemused", 1)
                    $ Line = Girl.bra
                    $ Girl.bra = ""
                    if Girl == KittyX:
                        "[Girl.name] shrugs and her [Line] falls through to the ground."
                    else:
                        "[Girl.name] throws off her [Line]."
                "Just pull it up." if (Girl.top or Girl.bra) and not Girl.top_pulled_up:
                    $ Girl.change_face("_bemused", 1)
                    $ Girl.top_pulled_up = 1
                    if Girl == EmmaX:
                        "[Girl.name] smiles and pulls out her tits. . ."
                    elif Girl.top and Girl.bra:
                        "[Girl.name] smiles and lifts up her tops. . ."
                    else:
                        "[Girl.name] smiles and lifts up her top. . ."
                "Lose both tops." if Girl.top and Girl.bra:
                    $ Girl.change_face("_bemused", 1)
                    if Girl == KittyX:
                        $ Girl.top = ""
                        $ Girl.bra = ""
                        "[Girl.name] shrugs and her tops fall through her body to the ground."
                    else:
                        if Girl == JubesX and Girl.accessory:
                            $ Girl.accessory = ""
                            "[Girl.name] pulls off her jacket. . ."
                        $ Line = Girl.top
                        $ Girl.top = ""
                        "[Girl.name] tosses the [Line] over her head. . ."
                        $ Line = Girl.bra
                        $ Girl.bra = ""
                        ". . .and then the [Line] as well."
                "Lose the [Girl.arms]. . ." if Girl.arms:
                    $ Girl.change_face("_sexy")
                    $ Line = Girl.arms
                    $ Girl.arms = ""
                    "She pulls off her [Line]."

                "Why don't you lose the suspenders?" if Girl.accessory == "suspenders" or Girl.accessory == "suspenders2":
                    $ Girl.accessory = ""
                    "[Girl.name] pulls her suspenders off."

                "Why don't you lose the hoops?" if Girl.accessory == "rings" or Girl.accessory == "rings":
                    $ Girl.accessory = ""
                    "[Girl.name] pulls her hoops off."

                "Why don't you lose the hat?" if Girl.hair == "hat" or Girl.hair == "hat wet":
                    $ Girl.hair == "wet" if Girl.hair == "hat wet" else "wave"
                    "[Girl.name] tosses her hat aside."
                "That's enough. [[exit]":

                    $ Girl.change_face("_bemused", 1)
                    Girl.voice "All right, [Girl.player_petname]."
                    $ counter = 0
        if Girl.ChestNum() < 3 and Girl.OverNum() < 3:

            $ Girl.change_stat("obedience", 50, 1)
            $ Girl.change_stat("obedience", 90, 1)
            call expression Girl.tag + "_First_Topless"
        $ Girl.change_stat("lust", 80, 3)
        $ Girl.recent_history.append("ask topless")
        $ Girl.daily_history.append("ask topless")
        $ approval_bonus = 0
        return



    $ Girl.change_face("_bemused", 1)
    if Girl == RogueX:
        if Intro == "massage" and not approval:
            ch_r "I'm ok with a massage, but my top stays on."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_r "I just told you no, [Girl.player_petname]."
        elif approval and not Girl.SeenChest:
            ch_r "I'd like to leave something to the imagination. . ."
        elif not Girl.SeenChest:
            ch_r "I'm not ready to show you those yet. . ."
        elif "no_topless" in Girl.daily_history:
            ch_r "I wasn't into it earlier, [Girl.player_petname], what's changed?"
        elif "ask topless" in Girl.recent_history:
            ch_r "Changed your mind, [Girl.player_petname]?"
        elif Taboo:
            ch_r "It's a bit exposed here. . ."
        elif approval:
            ch_r "Well, you've seen them before, but. . ."
        else:
            ch_r "Not right now."
    elif Girl == KittyX:
        if Intro == "massage" and not approval:
            ch_k "A massage is fine, but I'm keeping my top on, ok?"
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_k "I[Girl.like]already told you, no way!"
        elif approval and not Girl.SeenChest:
            ch_k "I'm[Girl.like]not really comfortable with that."
        elif not Girl.SeenChest:
            ch_k "I'd[Girl.like]really rather not, ok?"
        elif "no_topless" in Girl.daily_history:
            ch_k "Do you[Girl.like]think something's changed since earlier?"
        elif "ask topless" in Girl.recent_history:
            ch_k "Did you[Girl.like]want something else off?"
        elif Taboo:
            ch_k "I'm[Girl.like]not that comfortable out here. . ."
        elif approval:
            ch_k "Maybe not?"
        else:
            ch_k "Nu-uh."
    elif Girl == EmmaX:
        if Intro == "massage" and not approval:
            ch_e "I welcome a massage, but I'm staying fully dressed."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_e "Learn from previous mistakes, [Girl.player_petname]."
        elif approval and not Girl.SeenChest:
            ch_e "I don't know if that would be appropriate."
        elif not Girl.SeenChest:
            ch_e "I don't think you're ready for that."
        elif "no_topless" in Girl.daily_history:
            ch_e "Are you still that obsessed?"
        elif "ask topless" in Girl.recent_history:
            ch_e "You want more?"
        elif Taboo:
            ch_e "[Girl.player_petname], not around prying eyes."
        elif approval:
            ch_e "Are you sure you're prepared?"
        else:
            ch_e "No."
    elif Girl == LauraX:
        if Intro == "massage" and not approval:
            ch_l "I could use a massage, but I'm keeping my clothes on."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_l "Don't push it, [Girl.player_petname]."
        elif approval and not Girl.SeenChest:
            ch_l "I don't know, man."
        elif not Girl.SeenChest:
            ch_l "I really don't think so."
        elif "no_topless" in Girl.daily_history:
            ch_l "Dude, relax."
        elif "ask topless" in Girl.recent_history:
            ch_l "Again?"
        elif Taboo:
            ch_l "[Girl.player_petname], not around here, alright?"
        elif approval:
            ch_l "Are you sure?"
        else:
            ch_l "No."
    elif Girl == JeanX:
        if Intro == "massage" and not approval:
            ch_j "Massage, yes, but top on."
        elif "no_topless" in Girl.recent_history:
            $ JeanX.change_face("_angry")
            ch_j "Relax, [Girl.player_petname]."




        elif "no_topless" in Girl.daily_history:
            ch_j "Not happening."
        elif "ask topless" in Girl.recent_history:
            ch_j "So soon?"
        elif Taboo:
            ch_j "Hmm. . . not around here"
        elif approval:
            ch_j "Hmm. . ."
        else:
            ch_j "No way."
    elif Girl == StormX:
        if Intro == "massage" and not approval:
            ch_s "I would enjoy a massage, but I'm staying fully clothed."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_s "I am not so pliable as that, [Girl.player_petname]."
        elif approval and not Girl.SeenChest:
            ch_s "I don't know if that would be appropriate."
        elif "no_topless" in Girl.daily_history:
            ch_s "Do not ask again."
        elif "ask topless" in Girl.recent_history:
            ch_s "Oh, you'd like to see them again?"
        elif Taboo and Girl not in Rules:
            ch_s "I'm afraid not in public, [Girl.player_petname]."
        elif approval:
            ch_s "Are you Certain?"
        else:
            ch_s "No."
    elif Girl == JubesX:
        if Intro == "massage" and not approval:
            ch_v "I could use a massage, but I'm keeping my clothes on."
        elif "no_topless" in Girl.recent_history:
            $ Girl.change_face("_angry")
            ch_v "Don't push it, [Girl.player_petname]."
        elif approval and not Girl.SeenChest:
            ch_v "I don't know, man."
        elif not Girl.SeenChest:
            ch_v "I'm not cool with that."
        elif "no_topless" in Girl.daily_history:
            ch_v "Dude, relax."
        elif "ask topless" in Girl.recent_history:
            ch_v "Again?"
        elif Taboo:
            ch_v "[Girl.player_petname], it's just public here?"
        elif approval:
            ch_v "I dunno, really?"
        else:
            ch_v "Nah."
    menu:
        extend ""
        "Sorry, sorry." if "no_topless" in Girl.recent_history:
            $ Girl.change_face("_bemused", 1)
            if Girl == RogueX:
                ch_r "Ok, just. . . give it a rest, huh?"
            elif Girl == KittyX:
                ch_k "It's cool, I get it, but[Girl.like]chill out, huh?"
            elif Girl == EmmaX:
                ch_e "I can't blame you for your persistance, but learn from your errors."
            elif Girl == LauraX:
                ch_l "Right, I get it, stay thirsty."
            elif Girl == JeanX:
                ch_j "It's not like I can blame you, [Girl.player_petname]."
            elif Girl == StormX:
                ch_s "I cannot blame you."
            elif Girl == JubesX:
                ch_v "Well, you can't win if the don't play, right?"

        "Ok, that's fine." if "no_topless" not in Girl.recent_history:
            if "ask topless" not in Girl.daily_history:
                $ Girl.change_stat("lust", 80, 3)
                $ Girl.change_stat("love", 70, 1)
                $ Girl.change_stat("love", 90, 1)
                $ Girl.change_stat("inhibition", 50, 3)
            if Girl.Forced:
                $ Girl.mouth = "_grimace"
                if Girl == RogueX:
                    ch_r "I really appreciate that."
                elif Girl == KittyX:
                    ch_k "That's[Girl.like]really cool of you."
                elif Girl == EmmaX:
                    ch_e "How. . . generous of you."
                elif Girl == LauraX:
                    ch_l "Ok."
                elif Girl == JeanX:
                    ch_j ". . ."
                elif Girl == StormX:
                    ch_s "Good."
                elif Girl == JubesX:
                    ch_v "Yeah, thanks. . ."
                if "ask topless" not in Girl.daily_history:
                    $ Girl.change_stat("love", 20, 2)
                    $ Girl.change_stat("love", 70, 2)
                    $ Girl.change_stat("inhibition", 60, 1)

        "How about just the jacket?" if Girl == JubesX and Girl.accessory:

            if Girl.top or Girl.accessory == "open_jacket":

                ch_v "Sure, I guess. . ."
                $ Girl.accessory = ""
                "[Girl.name] shrugs off her Jacket."
            elif approval_check(Girl, 800, TabM = 2) and Girl.bra:
                $ Girl.change_face("_sexy")
                ch_v "Well, I guess. . ."
                $ Girl.change_face("_bemused", 1)
                $ Girl.accessory = ""
                "[Girl.name] shrugs off her Jacket."
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 30, 2)
            elif not Girl.bra:
                $ Girl.eyes = "_surprised"
                $ Girl.blushing = "_blush2"
                ch_v "I kinda don't have anything under this. . ."
                $ Girl.change_stat("inhibition", 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ Girl.mouth = "_smile"
                        $ Girl.change_stat("love", 70, 2)
                        ch_v "Whew, thanks. . ."
                    "That doesn't bother me any.":

                        if approval_check(Girl, 500, "I", TabM=3) or approval_check(Girl, 1000, "LI", TabM=3):
                            $ Girl.change_face("_bemused", 1)
                            ch_v "Whoa, spicy. . ."
                            $ Girl.change_stat("obedience", 20, 2)
                            $ Girl.change_stat("obedience", 60, 1)
                            $ Girl.change_face("_sexy")
                            $ Girl.accessory = ""
                            "[Girl.name] shrugs off her Jacket."
                            $ Girl.top = ""
                            $ Girl.change_stat("inhibition", 30, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            call expression Girl.tag + "_First_Topless"
                        else:
                            $ Girl.change_face("_bemused")
                            call Top_Off_Refused (Girl)
                    "I know, take it off.":

                        call ToplessorNothing (Girl)
                $ Girl.blushing = "_blush1"
            else:
                $ Girl.change_face("_sexy")
                call Top_Off_Refused (Girl)

        "How about just the [Girl.top]?" if Girl.top:

            if approval_check(Girl, 800, TabM = 2) and Girl.bra:
                $ Girl.change_face("_sexy")
                if Girl == RogueX:
                    ch_r "Well, that's no big deal I guess. . ."
                elif Girl == KittyX:
                    ch_k "Um, I guess I could. . ."
                elif Girl == EmmaX:
                    ch_e "Well, I suppose that would be fine. . ."
                elif Girl == LauraX:
                    ch_l "I mean. . . I guess. . ."
                elif Girl == JeanX:
                    ch_j "Sure, whatever."
                elif Girl == StormX:
                    ch_s "I suppose so."
                elif Girl == JubesX:
                    ch_v "Well, I guess. . ."
                $ Girl.change_face("_bemused", 1)
                $ Line = Girl.top
                $ Girl.top = ""
                if Girl == KittyX:
                    "[Girl.name] shrugs and her [Line] falls through to the ground."
                elif Girl == JubesX:
                    if Girl.accessory:
                        $ Girl.accessory = ""
                        "[Girl.name] shrugs off her Jacket, before pulling her [Line] over her head."
                    else:
                        "[Girl.name] pulls her [Line] over her head, throwing it aside."
                else:
                    "[Girl.name] tosses the [Line] over her head."
                $ Girl.change_stat("obedience", 50, 1)
                $ Girl.change_stat("inhibition", 30, 2)
            elif not Girl.bra:
                $ Girl.eyes = "_surprised"
                $ Girl.blushing = "_blush2"
                if Girl == RogueX:
                    ch_r "I'm not exactly decent under this, you know."
                elif Girl == KittyX:
                    ch_k "I'd[Girl.like]be {i}totally{/i} exposed here."
                elif Girl == EmmaX:
                    ch_e "I don't think you're prepared for what's under there."
                elif Girl == LauraX:
                    ch_l "I don't really have anything on under here."
                elif Girl == JeanX:
                    ch_j "I'm not wearing a bra at the moment."
                elif Girl == StormX:
                    ch_s "I am naked under this, you know. . ."
                elif Girl == JubesX:
                    ch_v "I kinda don't have anything under this. . ."
                $ Girl.change_stat("inhibition", 30, 1)
                menu:
                    extend ""
                    "Ok, you can leave it on.":
                        $ Girl.mouth = "_smile"
                        $ Girl.change_stat("love", 70, 2)
                        if Girl == RogueX:
                            ch_r "Great!"
                        elif Girl == KittyX:
                            ch_k "Thanks!"
                        elif Girl == EmmaX:
                            ch_e "Good."
                        elif Girl == LauraX:
                            ch_l "Right."
                        elif Girl == JeanX:
                            ch_j "That's what I said."
                        elif Girl == StormX:
                            ch_s "Very well then."
                        elif Girl == JubesX:
                            ch_v "Whew, thanks. . ."
                    "That doesn't bother me any.":

                        if approval_check(Girl, 500, "I", TabM=3) or approval_check(Girl, 1000, "LI", TabM=3):
                            $ Girl.change_face("_bemused", 1)
                            if Girl == RogueX:
                                ch_r "Ooh, at least you know what you like"
                            elif Girl == KittyX:
                                ch_k "Why am I not surprised?"
                            elif Girl == EmmaX:
                                ch_e "Well, I suppose it couldn't hurt to try."
                            elif Girl == LauraX:
                                ch_l "Maybe it should. . ."
                            elif Girl == JeanX:
                                ch_j ". . ."
                            elif Girl == StormX:
                                ch_s "It doesn't bother me much either."
                            elif Girl == JubesX:
                                ch_v "Whoa, spicy. . ."
                            $ Girl.change_stat("obedience", 20, 2)
                            $ Girl.change_stat("obedience", 60, 1)
                            $ Girl.change_face("_sexy")
                            $ Line = Girl.top
                            $ Girl.top = ""
                            if Girl == KittyX:
                                "[Girl.name] shrugs and her [Line] falls through to the ground."
                            elif Girl == JubesX:
                                if Girl.accessory:
                                    $ Girl.accessory = ""
                                    "[Girl.name] shrugs off her Jacket, before pulling her [Line] over her head."
                                else:
                                    "[Girl.name] and pulls her [Line] over her head, throwing it aside."
                            else:
                                "[Girl.name] tosses the [Line] over her head."
                            $ Girl.top = ""
                            $ Girl.change_stat("inhibition", 30, 2)
                            $ Girl.change_stat("inhibition", 60, 1)
                            call expression Girl.tag + "_First_Topless"
                        else:
                            $ Girl.change_face("_bemused")
                            call Top_Off_Refused (Girl)
                    "I know, take it off.":

                        call ToplessorNothing (Girl)
                $ Girl.blushing = "_blush1"
            else:
                $ Girl.change_face("_sexy")
                call Top_Off_Refused (Girl)
        "Come on, Please? [[take it all off]":



            if approval and approval_check(Girl, 600, "L", TabM=1):
                $ Girl.change_stat("obedience", 40, 2)
                $ Girl.change_face("_sexy")
                if Girl == RogueX:
                    if "no_topless" in Girl.recent_history:
                        ch_r "You're pretty persistent, [Girl.player_petname]. I guess this time it'll be rewarded. . ."
                    else:
                        ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ."
                elif Girl == KittyX:
                    if "no_topless" in Girl.recent_history:
                        ch_k "You just don't know when to quit. . . but you got lucky this time. . ."
                    else:
                        ch_k "You[Girl.like]know how to ask nicely . . ."
                elif Girl == EmmaX:
                    if "no_topless" in Girl.recent_history:
                        ch_e "Fine, I can't take your constant begging."
                    else:
                        ch_e "Well, I suppose if you ask nicely . . ."
                elif Girl == LauraX:
                    ch_l "Fine, you thirsty weirdo."
                elif Girl == JeanX:
                    if "no_topless" in Girl.recent_history:
                        ch_j "Oh, whatever."
                    else:
                        ch_j "I guess. . ."
                elif Girl == StormX:
                    ch_s "Oh, very well."
                elif Girl == JubesX:
                    ch_v "Ok, fine, geeze."
                $ Girl.top_pulled_up = 1
                "[Girl.name] just pulls her top up over her tits."
                $ Girl.arms = ""
                $ Girl.change_stat("inhibition", 30, 2)
                $ Girl.change_stat("inhibition", 60, 1)
                call expression Girl.tag + "_First_Topless"
            elif "no_topless" in Girl.recent_history:
                $ Girl.change_face("_angry")
                if Girl == RogueX:
                    ch_r "Nuh uh, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Noooope!"
                elif Girl == EmmaX:
                    ch_e "Again, no."
                elif Girl == LauraX:
                    ch_l "Still no."
                elif Girl == JeanX:
                    ch_j "Still a \"no\" on that, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "Not today, no."
                elif Girl == JubesX:
                    ch_v "Nah. . ."
                $ Girl.change_stat("love", 80, -5)
                $ Girl.recent_history.append("_angry")
                $ Girl.daily_history.append("_angry")
            else:
                $ Girl.change_face("_sexy")
                call Top_Off_Refused (Girl)


        "Lose the [Girl.arms], at least. . ." if Girl.arms:
            $ Girl.change_face("_sexy")
            Girl.voice "Oh, all right."
            $ Line = Girl.arms
            $ Girl.arms = ""
            "She pulls off her [Line]."
        "No, topless or nothing.":

            call ToplessorNothing (Girl)
        "Never mind.":

            pass

    $ Girl.recent_history.append("ask topless")
    $ Girl.daily_history.append("ask topless")
    $ approval_bonus = 0
    return


label Top_Off_Refused(Girl=0):

    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    $ Girl.change_face("_angry")
    if Girl == RogueX:
        if "no_topless" in Girl.recent_history:
            ch_r "Get a clue, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_r "Give it a rest, [Girl.player_petname]."
        else:
            $ Girl.change_face("_sad")
            ch_r "I'm afraid not this time, [Girl.player_petname]. Sure we can't have some fun anyway?"
    elif Girl == KittyX:
        if "no_topless" in Girl.recent_history:
            ch_k "[Girl.Like]back off."
        elif "no_topless" in Girl.daily_history:
            ch_k "Not today, maybe not ever, [Girl.player_petname]."
        else:
            $ KittyX.change_face("_sad")
            ch_k "[Girl.Like], no way, but I don't want to go. . ."
    elif Girl == EmmaX:
        if "no_topless" in Girl.recent_history:
            ch_e "You should probably back off now."
        elif "no_topless" in Girl.daily_history:
            ch_e "I'm tired of this, [Girl.player_petname]."
        else:
            ch_e "Is this a dealbreaker for you?"
    elif Girl == LauraX:
        if "no_topless" in Girl.recent_history:
            ch_l "You're getting real close to the line, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_l "You keep coming back with this, [Girl.player_petname]."
        else:
            ch_l "Let it go?"
    elif Girl == JeanX:
        if "no_topless" in Girl.recent_history:
            ch_j "Step carefully, [Girl.player_petname]."
        elif "no_topless" in Girl.daily_history:
            ch_j "Still on about that?"
        else:
            ch_j "Careful. . ."
    elif Girl == StormX:
        if "no_topless" in Girl.recent_history:
            ch_s "I will not move on this."
        elif "no_topless" in Girl.daily_history:
            ch_s "Find your joy elsewhere, [Girl.player_petname]."
        else:
            ch_s "Do you insist on this path?"
    elif Girl == JubesX:
        if "no_topless" in Girl.recent_history:
            ch_v "I thought I was clear. . ."
        elif "no_topless" in Girl.daily_history:
            ch_v "Look, cut it out, [Girl.player_petname]."
        else:
            ch_v "Whoa, slow your roll there. . ."
    menu:
        extend ""
        "Sure, never mind." if "no_topless" not in Girl.recent_history:
            $ Girl.change_face("_sexy")
            $ Girl.change_stat("love", 70, 2)
            if Girl == RogueX or Girl == KittyX:
                Girl.voice "Great!"
            else:
                Girl.voice "Good."
        "Sorry, I'll drop it." if "no_topless" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Fine. . ."
            elif Girl == KittyX:
                ch_k "Good!"
            else:
                Girl.voice "Good."
        "No, I insist. . .":
            $ Girl.brows = "_angry"
            if Girl == RogueX:
                $ Girl.brows = "_confused"
                ch_r "Ok [Girl.player_petname], your loss."
            elif Girl == KittyX:
                ch_k "Fine then!"
            elif Girl == EmmaX:
                ch_e "Very well."
            elif Girl == LauraX:
                ch_l "Your funeral."
            elif Girl == JeanX:
                $ Girl.change_face("_smile")
                ch_j "Well that was at least good for a laugh."
            elif Girl == StormX:
                ch_s "So be it."
            elif Girl == JubesX:
                ch_v "Too bad then. . ."
            $ Girl.change_stat("lust", 50, 5)
            $ Girl.change_stat("love", 70, -2, 1)
            if "no_topless" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 60, 4)
            $ Girl.recent_history.append("_angry")
            $ Girl.daily_history.append("_angry")
    $ Girl.recent_history.append("no_topless")
    $ Girl.daily_history.append("no_topless")
    return


label ToplessorNothing(Girl=0):

    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    $ Girl.change_face("_angry")
    if approval_check(Girl, 800, "OI", TabM = 4) and approval_check(Girl, 400, "O", TabM = 3):
        $ Girl.change_stat("love", 20, -2, 1)
        $ Girl.change_stat("love", 70, -5, 1)
        $ Girl.change_stat("inhibition", 60, 3)
        $ Girl.change_face("_sad")
        if Girl == RogueX:
            if "no_topless" in Girl.recent_history:
                ch_r "Ok, ok, whatever."
            else:
                ch_r "Fine, if that's what you want."
        elif Girl == KittyX:
            if "no_topless" in Girl.recent_history:
                ch_k "Ok, fine. This time."
            else:
                $ Girl.change_face("_sad")
                ch_k "Whatever."
        elif Girl == EmmaX:
            if "no_topless" in Girl.recent_history:
                ch_e "Oh, very well. . ."
            else:
                $ Girl.change_face("_sad")
                ch_e "Fine."
        elif Girl == LauraX:
            if "no_topless" in Girl.recent_history:
                ch_l "Hrmph, whatever. . ."
            else:
                $ Girl.change_face("_sad")
                ch_l "Ugh, whatever."
        elif Girl == JeanX:
            if "no_topless" in Girl.recent_history:
                ch_j "Ok, fine. . ."
            else:
                $ Girl.change_face("_sad")
                ch_j "Fine! . . whatever."
        elif Girl == StormX:
            $ Girl.change_face("_sad")
            if "no_topless" in Girl.recent_history:
                ch_s "I suppose sometimes I must. . ."
            else:
                ch_s "Fine."
        elif Girl == JubesX:
            if "no_topless" in Girl.recent_history:
                ch_v "Ok, fine, just quit asking."
            else:
                ch_v "Ok, fine, whatever."
        $ Girl.change_stat("obedience", 60, 4)
        $ Girl.change_stat("obedience", 90, 2)
        $ Girl.top_pulled_up = 1
        "[Girl.name] slowly pulls her top up over her tits."
        call expression Girl.tag + "_First_Topless"
    else:
        $ Girl.change_stat("love", 200, -10)
        $ Girl.change_stat("obedience", 40, -1, 1)
        if Girl == RogueX:
            if "no_topless" in Girl.recent_history:
                ch_r "Seriously, cut this shit out."
            else:
                $ Girl.brows = "_confused"
                ch_r "\"Nothing\" it is then."
        elif Girl == KittyX:
            if "no_topless" in Girl.recent_history:
                ch_k "It[Girl.like]wasn't cute the first time."
            else:
                $ Girl.brows = "_angry"
                ch_k "[Girl.Like]no way!"
        elif Girl == EmmaX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_e "Learn to take \"no\" for an answer."
            else:
                ch_e "I'm afraid not."
        elif Girl == LauraX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_l "You have got to chill."
            else:
                ch_l "Nope."
        elif Girl == JeanX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_j "Keep it under control."
            else:
                ch_j "Oh, no."
        elif Girl == StormX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_s "I say again, \"no.\"."
            else:
                ch_s "Then that would be a \"no.\"."
        elif Girl == JubesX:
            if "no_topless" in Girl.recent_history:
                $ Girl.brows = "_angry"
                ch_v "Look, I told you, \"no.\"."
            else:
                ch_v "Sorry, no go."
        $ Girl.recent_history.append("no_topless")
        $ Girl.daily_history.append("no_topless")
        $ Girl.recent_history.append("_angry")
        $ Girl.daily_history.append("_angry")
    return


label Bottoms_Off(Girl=0, Intro=1, Line=0, counter=0):
    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    if not Girl.legs and not Girl.underwear and not Girl.hose:

        $ approval_bonus = 0
        return

    if "_angry" in Girl.recent_history:
        if Girl == RogueX:
            ch_r "I'm just too annoyed to deal with this right now."
        elif Girl == KittyX:
            ch_k "The only \"kitty\" you're getting is up here."
        elif Girl == EmmaX:
            ch_e "I would give up on that."
        elif Girl == LauraX:
            ch_l "You're barking up the wrong tree."
        elif Girl == JeanX:
            ch_j "Definitely not, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "That is certainly optimistic."
            ch_s "No."
        elif Girl == JubesX:
            ch_v "Definitely not."
        return


    if Girl.SeenPussy and approval_check(Girl, 700):
        $ approval_bonus += 20
    elif not Girl.underwear:
        $ approval_bonus -= 20
    elif Girl.SeenPanties and approval_check(Girl, 500):
        $ approval_bonus += 5
    if Intro == "_dildo":
        $ approval_bonus += 20
    if "exhibitionist" in Girl.traits:
        $ approval_bonus += (Taboo*5)
    if (Girl in Player.Harem or "sex friend" in Girl.player_petnames) and not Taboo:
        $ approval_bonus += 10
    elif "ex" in Girl.traits:
        $ approval_bonus -= 40
    if "no_bottomless" in Girl.recent_history:
        $ approval_bonus -= 20
    elif Girl == StormX and (not Taboo or Girl in Rules):

        $ approval_bonus += 20

    if Intro:
        if Intro == 2 and Girl.PantsNum() > 5:

            if Girl == RogueX:
                ch_r "I don't know, I might need my knickers off for that. . ."
            elif Girl == KittyX:
                ch_k "So, you'd have to be able to[KittyX.like]touch down there, I guess. . ."
            elif Girl == EmmaX:
                ch_e "I would probably need to lose these to get anything out of that. . ."
            elif Girl == LauraX:
                ch_l "I'd need to be pantsless to get anything from that. . ."
            elif Girl == JeanX:
                ch_j "I guess I'd have to go bottomless. . ."
            elif Girl == StormX:
                ch_s "I will remove these then. . ."
            elif Girl == JubesX:
                ch_v "I guess these would get in the way. . ."
        else:
            if Girl.legs and not Girl.upskirt:
                ch_p "This might be easier without your [Girl.legs] on."
            elif Girl.underwear and not Girl.underwear_pulled_down:
                ch_p "This might be easier without your [Girl.underwear] on."

    $ approval = approval_check(Girl, 1200, TabM = 5)

    if action_context == "auto":
        $ counter = 0

        if not Girl.upskirt and not Girl.underwear_pulled_down:
            if Girl.PantsNum() == 5:

                if approval >= 2 or (Girl.SeenPussy and not Taboo):
                    $ Girl.change_stat("inhibition", 60, 1)
                    if Taboo:
                        $ Girl.change_stat("inhibition", 90, (int(Taboo/20)))
                    $ Girl.upskirt = 1
                    "She slides her skirt up."
                    $ counter = 1

            if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                if Girl.underwear:

                    if not approval or (not Girl.SeenPanties and Taboo):
                        return
                elif approval < 2 or (not Girl.SeenPussy and Taboo):
                    return
                elif Girl.upskirt:
                    return
                $ Girl.change_stat("inhibition", 60, 1)
                if Girl.HoseNum() >= 6:
                    $ Line = Girl.hose
                    $ Girl.hose = ""
                $ Girl.upskirt = 1

                if Girl == KittyX:
                    if Girl.PantsNum(0) >= 6:
                        "[Girl.name] grumbles to herself, and then allows her [Girl.legs] to drop down her legs."
                    else:
                        "[Girl.name] grumbles to herself, and then allows her [Line] to drop down her legs."
                    if Girl.underwear:
                        $ Girl.SeenPanties = 1
                elif Girl.underwear:
                    if Girl.PantsNum(0) >= 6:
                        "[Girl.name] grumbles to herself, and then unzips her [Girl.legs], sliding them down her legs."
                    else:
                        "[Girl.name] grumbles to herself, and then pulls her [Line] down her legs."
                    $ Girl.SeenPanties = 1
                else:
                    if Girl.PantsNum(0) >= 6:
                        "[Girl.name] grumbles to herself, and then unzips her [Girl.legs], sliding them off her bare ass."
                    else:
                        "[Girl.name] grumbles to herself, and then pulls her [Line] down her bare ass."
                call expression Girl.tag + "_First_Bottomless" pass (1)
                if Taboo:
                    $ Girl.change_stat("inhibition", 90, (int(Taboo/10)))
                $ counter = 1

        if Girl.underwear and not Girl.underwear_pulled_down:

            if approval >= 2 or (Girl.SeenPussy and not Taboo):
                $ Girl.change_stat("inhibition", 70, 2)
                if Taboo:
                    $ Girl.change_stat("inhibition", 90, (int(Taboo/10)))
                $ Girl.underwear_pulled_down = 1
                if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                    $ Girl.upskirt = 1
                if Girl == KittyX:
                    if counter:
                        "With a second thought, [Girl.name] lets her [Girl.underwear] drop too."
                    else:
                        "[Girl.name] tsks in irritation, and her [Girl.underwear] slide off to the ground."
                else:
                    if counter:
                        "[Girl.name] tsks in irritation, and pulls down her [Girl.underwear] too."
                    else:
                        "[Girl.name] tsks in irritation, and pulls down her [Girl.underwear]."
                call expression Girl.tag + "_First_Bottomless" pass (1)
                if Girl == RogueX:
                    ch_r "I wasn't getting anything out of it with those on. Give it another go."
                elif Girl == KittyX:
                    ch_k "It's super annoying not being able to phase you through these."
                elif Girl == EmmaX:
                    ch_e "That was just in the way."
                elif Girl == LauraX:
                    ch_l "I guess all that was in the way."
                elif Girl == JeanX:
                    ch_j "Ok, see if you can make that work, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "That should simplify things. . ."
                elif Girl == JubesX:
                    ch_v "Ok, that's a bit more comfortable. . ."
        return


    if approval >= 2:

        $ Girl.change_face("_sexy", 1)
        if Girl.Forced:
            $ Girl.change_face("_sad", 1)
            $ Girl.change_stat("love", 20, -2, 1)
            $ Girl.change_stat("love", 70, -3, 1)
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 60, 1)
        if Girl == RogueX:
            if approval >= 3:
                $ Line = "Hmmm, what do you want to see? . ."
            else:
                $ Line = "Well, ok. I'd kinda like to keep {i}some{/i} modesty though. . ."
        elif Girl == KittyX:
            if approval >= 3:
                $ Line = "Heh, what would you like to see? . ."
            else:
                $ Line = "Ok, maybe, but don't push it. . ."
        elif Girl == EmmaX:
            if approval >= 3:
                $ Line = "Mmmm, what would you like?"
            else:
                $ Line = "What would you have me take off?"
        elif Girl == LauraX:
            if approval >= 3:
                $ Line = "What did you want off?"
            else:
                $ Line = "Hm, what did you want me to lose?"
        elif Girl == JeanX:
            if approval >= 3:
                $ Line = "What did you want off?"
            else:
                $ Line = "Like. . . what? . ."
        elif Girl == StormX:
            $ Line = "What would you have me remove?"
        elif Girl == JubesX:
            $ Line =  "Well like what did you have in mind here?"
        call Bottoms_Off_Legs (Girl)

        if not Girl.underwear and Girl.recent_history.count("bottomless") < 2:
            $ Girl.change_stat("obedience", 50, 1)
            $ Girl.change_stat("obedience", 90, 1)
            $ Girl.change_stat("inhibition", 50, 3)
            $ Girl.change_stat("lust", 80, 3)

    elif Girl.legs or Girl.underwear or Girl.hose:

        $ Girl.change_face("_bemused", 1)
        if Girl == RogueX:
            if "no_bottomless" in Girl.recent_history:
                $ Girl.change_face("_angry")
                ch_r "What did I just tell you, [Girl.player_petname]?"
            elif "no_topless" in Girl.recent_history:
                $ Girl.change_face("_angry")
                ch_r "I doubt your odds will be better here, [Girl.player_petname]. . ."
            elif approval and not Girl.SeenPussy:
                ch_r "Not everything, right?"
            elif not Girl.SeenPussy and "ask topless" in Girl.recent_history:
                ch_r "I'm not ready to show you that either."
            elif "no_bottomless" in Girl.daily_history:
                ch_r "Have you forgot what I said earlier, [Girl.player_petname]?"
            elif Taboo:
                ch_r "I don't know about doing it here. . ."
            elif approval:
                ch_r "I don't know if I want to take my bottoms off. . ."
            elif Girl.SeenPussy:
                ch_r "Well, you've seen it before, but. . ."
            else:
                ch_r "I'm not taking my bottoms off."
        elif Girl == KittyX:
            if "no_bottomless" in Girl.recent_history:
                $ KittyX.change_face("_angry")
                ch_k "Last warning, [Girl.player_petname]. No."
            elif "no_topless" in Girl.recent_history:
                $ KittyX.change_face("_angry")
                ch_k "Not learning from your mistakes here, [Girl.player_petname]. . ."
            elif approval and not Girl.SeenPussy:
                ch_k "I'm not sure about that. . ."
            elif not Girl.SeenPussy and "ask topless" in Girl.recent_history:
                ch_k "That's a bit too far."
            elif "no_bottomless" in Girl.daily_history:
                ch_k "Short memory, [Girl.player_petname]?"
            elif Taboo:
                ch_k "This is[Girl.like]kinda public. . ."
            elif approval:
                ch_k "I'm[Girl.like]not sure about this. . ."
            elif Girl.SeenPussy:
                ch_k "Well, you've seen[Girl.like]it before . . ."
            elif Girl.PantsNum(0) > 6:
                ch_k "I'm keeping my pants on."
            elif Girl.PantsNum(0) > 5:
                ch_k "I'm keeping my shorts on."
            else:
                ch_k "I'm keeping my panties on."
        elif Girl == EmmaX:
            if "no_bottomless" in Girl.recent_history:
                $ EmmaX.change_face("_angry")
                ch_e "Stop asking, you're embarrassing yourself."
            elif "no_topless" in Girl.recent_history:
                $ EmmaX.change_face("_angry")
                ch_e "Do you really think that's likely?"
            elif approval and not Girl.SeenPussy:
                ch_e "I don't know if you're ready for that."
            elif not Girl.SeenPussy and "ask topless" in Girl.recent_history:
                ch_e "Be careful how far you push it. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_e "Don't you learn anything, [Girl.player_petname]?"
            elif Taboo:
                ch_e "Not with so many eyes around, [Girl.player_petname]. . ."
            elif approval:
                ch_e "Probably not. . ."
            elif Girl.SeenPussy:
                ch_e "I think you've seen enough . . ."
            elif Girl.PantsNum(0) > 6:
                ch_e "I'm keeping my pants on."
            elif Girl.PantsNum(0) == 5:
                ch_e "I'm keeping my skirt on."
            elif Girl.PantsNum(0) == 6:
                ch_e "I'm keeping my shorts on."
            else:
                ch_e "I'm keeping my panties on."
        elif Girl == LauraX:
            if "no_bottomless" in Girl.recent_history:
                $ LauraX.change_face("_angry")
                ch_l "Now you're just embarrassing yourself."
            elif "no_topless" in Girl.recent_history:
                $ LauraX.change_face("_angry")
                ch_l "This is really pushing it."
            elif approval and not Girl.SeenPussy:
                ch_l "I don't know if you're earned that yet."
            elif not Girl.SeenPussy and "ask topless" in Girl.recent_history:
                ch_l "Kinda pushing it, [Girl.player_petname]. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_l "So thirsty. . ."
            elif Taboo:
                ch_l "This is pretty exposed, [Girl.player_petname]. . ."
            elif approval:
                ch_l "Probably not. . ."
            elif Girl.SeenPussy:
                ch_l "You've probably seen enough . . ."
            elif Girl.PantsNum(0) > 6:
                ch_l "Well, I'm keeping my pants on."
            elif Girl.PantsNum(0) == 5:
                ch_l "Well, I'm keeping my skirt on."
            elif Girl.PantsNum(0) == 6:
                ch_l "Well, I'm keeping my shorts on."
            else:
                ch_l "Well, I'm keeping my panties on."
        elif Girl == JeanX:
            if "no_bottomless" in Girl.recent_history:
                $ JeanX.change_face("_angry")
                ch_j "Look, it's just not happening."
            elif "no_topless" in Girl.recent_history:
                $ JeanX.change_face("_angry")
                ch_j "Why did you think that would be different?"
            elif approval and not Girl.SeenPussy:
                ch_j "Hmm. . . have your earned that. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_j "Again with this?"
            elif Taboo:
                ch_j "Not here, [Girl.player_petname]. . ."
            elif approval:
                ch_j "Hmm. . ."
            elif Girl.SeenPussy:
                ch_j "Hmm. . ."
            elif Girl.PantsNum(0) > 6:
                ch_j "I'm keeping my pants on though."
            elif Girl.PantsNum(0) == 5:
                ch_j "I'm keeping my skirt on though."
            elif Girl.PantsNum(0) == 6:
                ch_j "I'm keeping my shorts on though."
            else:
                ch_j "I'm keeping my panties on though."
        elif Girl == StormX:
            if "no_bottomless" in Girl.recent_history:
                $ StormX.change_face("_angry")
                ch_s "You need to stop asking about that."
            elif Taboo and Girl not in Rules:
                ch_s "I cannot in public, [Girl.player_petname]. . ."
            elif approval:
                ch_s "I am unsure. . ."
            elif Girl.PantsNum(0) > 6:
                ch_s "I will be keeping my pants on."
            elif Girl.PantsNum(0) == 5:
                ch_s "I will be keeping my skirt on."
            elif Girl.PantsNum(0) == 6:
                ch_s "I will be keeping my shorts on."
            else:
                ch_s "I will be keeping my panties on."
        elif Girl == JubesX:
            if "no_bottomless" in Girl.recent_history:
                $ JubesX.change_face("_angry")
                ch_v "Don't have a cow, dude."
            elif "no_topless" in Girl.recent_history:
                $ JubesX.change_face("_angry")
                ch_v "Don't push it, [Girl.player_petname]."
            elif approval and not Girl.SeenPussy:
                ch_v "I don't know, man."
            elif not Girl.SeenPussy and "ask topless" in Girl.recent_history:
                ch_v "Kinda pushing it, [Girl.player_petname]. . ."
            elif "no_bottomless" in Girl.daily_history:
                ch_v "So thirsty. . ."
            elif Taboo:
                ch_v "[Girl.player_petname], it's just public here?"
            elif approval:
                ch_v "Doubtful. . ."
            elif Girl.SeenPussy:
                ch_v "Need another look?"
            elif Girl.PantsNum(0) > 6:
                ch_v "Well, I'm keeping my pants on."


            elif Girl.PantsNum(0) == 6:
                ch_v "Well, I'm keeping my shorts on."
            else:
                ch_v "Well, I'm keeping my panties on."
        menu:
            extend ""
            "Ok, never mind." if "no_bottomless" not in Girl.recent_history:
                if "ask bottomless" not in Girl.daily_history:
                    $ Girl.change_stat("lust", 80, 2)
                    $ Girl.change_stat("love", 70, 1)
                    $ Girl.change_stat("love", 90, 1)
                    $ Girl.change_stat("inhibition", 50, 3)
                if Girl.Forced:
                    $ Girl.mouth = "_smile"
                    if Girl == RogueX:
                        ch_r "I really appreciate that."
                    elif Girl == KittyX:
                        ch_k ". . . thank you."
                    elif Girl == EmmaX:
                        ch_e "Very. . . generous."
                    elif Girl == LauraX:
                        ch_l "Right."
                    elif Girl == JeanX:
                        ch_j ". . ."
                    elif Girl == StormX:
                        ch_s "Thank you. . ."
                    elif Girl == JubesX:
                        ch_v "Thanks. . ."
                    if "ask bottomless" not in Girl.daily_history:
                        $ Girl.change_stat("love", 20, 3)
                        $ Girl.change_stat("love", 70, 4)
                        $ Girl.change_stat("inhibition", 60, 2)

            "Sorry, sorry." if "no_bottomless" in Girl.recent_history:
                if Girl == RogueX:
                    ch_r "Ok, fine, just chill out about it."
                elif Girl == KittyX:
                    ch_k "[Girl.Like], fine, whatever."
                else:
                    Girl.voice "Good."
            "Come on, Please?":

                if "no_bottomless" in Girl.daily_history:
                    $ Girl.change_face("_angry", 1)
                    if Girl == RogueX:
                        ch_r "Listen up when I tell you \"no.\""
                    elif Girl == KittyX:
                        ch_k "I already told you \"no.\""
                    elif Girl == EmmaX:
                        ch_e "I believe you've heard my answer on that."
                    elif Girl == LauraX:
                        ch_l "You heard me."
                    elif Girl == JeanX:
                        ch_j "Are you deaf, or stupid?"
                    elif Girl == StormX:
                        ch_s "I have spoken on the matter."
                    elif Girl == JubesX:
                        ch_v "No."
                else:
                    if approval and approval_check(Girl, 600, "L", TabM=1):
                        $ Girl.change_face("_sexy", 1)
                        $ D20 = renpy.random.randint(1, 3)
                        $ approval += 1 if D20 == 3 else 0
                        if Girl == RogueX:
                            $ Line = "Well, what were you thinking then. . ."
                        elif Girl == KittyX:
                            $ Line = "I guess. . ."
                        elif Girl == EmmaX:
                            $ Line = "Perhaps. . ."
                        elif Girl == LauraX:
                            $ Line = "Maybe. . ."
                        elif Girl == JeanX:
                            $ Line = "-sigh-. . . like what?"
                        elif Girl == StormX:
                            ch_s ". . ."
                            $ Line = "What did you want? . ."
                        elif Girl == JubesX:
                            $ Line =  "I mean, maaaybe. . ."
                        call Bottoms_Off_Legs (Girl)
                    else:
                        $ Girl.change_face("_sexy")
                        call Bottoms_Off_Refused (Girl)

            "It doesn't have to be everything. . ." if Girl.legs or Girl.HoseNum() >= 10 or Girl.underwear == "_shorts":
                if approval and "no_bottomless" not in Girl.daily_history:
                    $ Girl.change_face("_bemused", 1)
                    $ Line = "Well what did you have in mind then?"
                    call Bottoms_Off_Legs (Girl)
                else:

                    $ Girl.change_face("_sexy")
                    call Bottoms_Off_Refused (Girl)
            "It doesn't have to be everything. . . (locked)" if not Girl.legs and Girl.HoseNum() < 10 and Girl.underwear != "_shorts":
                pass
            "No, lose 'em.":

                if (approval and Girl.obedience >= 250) or (approval_check(Girl, 850, "OI", TabM = 5) and approval_check(Girl, 400, "O")):
                    $ Girl.change_stat("love", 20, -1, 1)
                    $ Girl.change_stat("love", 70, -5, 1)
                    $ Girl.change_stat("obedience", 50, 4)
                    $ Girl.change_stat("inhibition", 60, 3)
                    if Girl == RogueX:
                        $ Line =  "Fine, if that's what you want. What do you want to see?"
                    elif Girl == KittyX:
                        $ Line =  "Like geez, you're serious. . ."
                    elif Girl == EmmaX:
                        $ Line =  "Don't test me. . ."
                    elif Girl == LauraX:
                        $ Line =  "Don't push me. . ."
                    elif Girl == JeanX:
                        $ Line = "Think very carefully. . ."
                    elif Girl == StormX:
                        ch_s ". . ."
                        $ Line = "What did you want? . ."
                    elif Girl == JubesX:
                        $ Line =  "Tone. . ."
                    $ approval = 1 if approval < 1 else approval
                    $ Girl.Forced = 1
                    call Bottoms_Off_Legs (Girl)
                else:
                    $ Girl.change_stat("love", 200, -10)
                    if approval_check(Girl, 400, "O"):
                        if Girl == RogueX:
                            ch_r "I. . . I really can't."
                        elif Girl == KittyX:
                            ch_k "Sorry[Girl.like]no way."
                        elif Girl == EmmaX:
                            ch_e "Definitely not."
                        elif Girl == LauraX:
                            ch_l "No way."
                        elif Girl == JeanX:
                            ch_j "Ha! No."
                        elif Girl == StormX:
                            ch_s "I am sorry, no."
                        elif Girl == JubesX:
                            ch_v "Definitely not."
                    else:
                        $ Girl.change_face("_angry")
                        if Girl == RogueX:
                            ch_r "Well fuck off then!"
                        elif Girl == KittyX:
                            ch_k "GTFO."
                        elif Girl == EmmaX:
                            ch_e "Out of my sight, [Girl.player_petname]."
                        elif Girl == LauraX:
                            ch_l "Fuck off."
                        elif Girl == JeanX:
                            ch_j "Not even."
                        elif Girl == StormX:
                            ch_s "No."
                        elif Girl == JubesX:
                            ch_v "Nah. . ."
                        $ Girl.recent_history.append("_angry")
                        $ Girl.daily_history.append("_angry")
                    $ Girl.recent_history.append("no_bottomless")
                    $ Girl.daily_history.append("no_bottomless")

    $ approval_bonus = 0
    $ Girl.recent_history.append("ask bottomless")
    $ Girl.daily_history.append("ask bottomless")
    return

label Bottoms_Off_Legs(Girl=0):
    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    if Girl.Forced:
        $ Girl.change_face("_sad", 1)
    elif approval_check(Girl, 1100, "OI", TabM = 3):
        $ Girl.change_face("_sly")
    elif approval_check(Girl, 1400, TabM = 3):
        $ Girl.change_face("_sexy", 1)
    else:
        $ Girl.change_face("_bemused", 1)

    $ Line = "Well what did you want off?" if not Line else Line
    $ counter = 1
    while counter and (Girl.legs or Girl.underwear or Girl.hose):
        Girl.voice "[Line]"
        menu:
            extend ""

            "Take it all off" if Line != "Well what did you have in mind then?":

                if not Girl.underwear and Girl.HoseNum() < 10:
                    call NoPantiesOn (Girl)

                if Girl.legs:
                    $ Line = Girl.legs
                    $ Girl.legs = ""
                    if not Girl.SeenPanties:
                        if Girl == RogueX:
                            "[Girl.name] shyly removes her [Line]."
                        elif Girl == KittyX:
                            "[Girl.name] shyly tugs her [Line] off of her legs."
                        else:
                            "[Girl.name] pulls off her [Line]."
                        $ Girl.SeenPanties = 1
                    else:
                        "[Girl.name] pulls her [Line] off."

                if approval < 2 and not Girl.underwear and Girl.HoseNum() >= 10:
                    call NoPantiesOn (Girl)

                if Girl == JubesX and JubesX.accessory != "shut_jacket":

                    pass
                elif Girl == JubesX and JubesX.accessory == "shut_jacket":
                    $ Girl.accessory = ""
                    "She pulls her [Girl.accessory] off."
                    call expression Girl.tag + "_First_Bottomless"
                elif Girl.accessory:
                    $ Girl.accessory = ""
                    "She pulls her [Girl.accessory] off."

                if Girl.hose:
                    $ Line = Girl.hose
                    $ Girl.hose = ""
                    if Girl == KittyX:
                        "Her [Line] drop to the ground in a heap."
                    else:
                        "She pulls her [Line] down."

                if approval < 2:
                    call NoPantiesOn (Girl)

                if Girl.underwear:
                    $ Line = Girl.underwear
                    $ Girl.underwear = ""
                    if Girl == KittyX:
                        "She glances up at you as her [Line] fall clear of her."
                    else:
                        "She glances up at you as she removes her [Line]."
                call expression Girl.tag + "_First_Bottomless"


            "Lose the [Girl.legs]." if Girl.legs:
                if Girl.underwear and approval >= 2:
                    $ Girl.change_face("_sexy")
                    if Girl == RogueX:
                        ch_r "I guess I could do that. . ."
                    elif Girl == KittyX:
                        ch_k "That's. . . doable. . ."
                    elif Girl == EmmaX:
                        ch_e "I can manage that. . ."
                    elif Girl == LauraX:
                        ch_l "I guess I could. . ."
                    elif Girl == JeanX:
                        ch_j ". . .I guess. . ."
                    elif Girl == StormX:
                        ch_s "I could do that. . ."
                    elif Girl == JubesX:
                        ch_v "Well, I could do that. . ."
                elif approval:
                    $ Girl.change_face("_sexy", 1)
                    if approval < 2 and not Girl.underwear and Girl.HoseNum() < 10:
                        call NoPantiesOn (Girl)
                else:
                    $ Girl.change_face("_sexy")
                    call Bottoms_Off_Refused (Girl)
                    return

                $ Line = Girl.legs
                $ Girl.legs = ""
                if not Girl.underwear and Girl.HoseNum() < 10:
                    $ Girl.change_face("_sly", 2)
                    if Girl == KittyX:
                        "She blushes and looks at you as her [Line] drops at her feet."
                    elif Girl == RogueX:
                        "She blushes and looks at you slyly before removing her [Line]."
                    else:
                        "She glaces at you slyly before removing her [Line]."
                    call expression Girl.tag + "_First_Bottomless"
                elif not Girl.SeenPanties:
                    if Girl == KittyX:
                        "She blushes and looks at you as her [Line] drops at her feet."
                    elif Girl == RogueX:
                        "She blushes and looks at you slyly before removing her [Line]."
                    else:
                        "She glaces at you slyly before removing her [Line]."
                    $ Girl.SeenPanties = 1
                else:
                    "[Girl.name] pulls her [Line] off."
                $ Girl.change_face("_bemused", 1)

            "Lose the [Girl.underwear]." if Girl.underwear:
                if approval < 2:
                    if Girl == RogueX:
                        ch_r "No thanks, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "Sorry, no."
                    elif Girl == EmmaX:
                        ch_e "I'm afraid not."
                    elif Girl == LauraX:
                        ch_l "No way."
                    elif Girl == JeanX:
                        ch_j "Ha! No way."
                    elif Girl == StormX:
                        ch_s "I would rather not."
                    elif Girl == JubesX:
                        ch_v "Um, no thanks. . ."
                    $ Girl.recent_history.append("no_bottomless")
                    $ Girl.daily_history.append("no_bottomless")
                    return
                elif Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                    if Girl == RogueX:
                        ch_r "A little backwards, but sure. . ."
                    elif Girl == KittyX:
                        ch_k "[Girl.Like]I guess. . ."
                    elif Girl == EmmaX:
                        ch_e "I suppose that I could. . ."
                    elif Girl == LauraX:
                        ch_l "Huh, ok. . ."
                    elif Girl == JeanX:
                        ch_j "Hmm. . . I guess. . ."
                    elif Girl == StormX:
                        ch_s "I could do that. . ."
                    elif Girl == JubesX:
                        ch_v "Well, I could do that. . ."
                else:
                    if Girl == EmmaX:
                        ch_e "Of course."
                    elif Girl == LauraX:
                        ch_l "Huh, ok. . ."
                    elif Girl == StormX:
                        ch_s "Fine."
                    else:
                        Girl.voice "Ok, sure, [Girl.player_petname]."
                $ Line = Girl.underwear
                $ Girl.underwear = ""
                if Girl == KittyX:
                    if Girl.PantsNum() >= 5:
                        "She reaches a hand into her [Girl.legs] and pulls her [Line] out through the pocket."
                        "She gives a little wink as she drops them to the ground."
                    elif Girl.HoseNum() >= 5:
                        "She reaches a hand into her [Girl.hose] and pulls her [Line] out through the pocket."
                        "She gives a little wink as she drops them to the ground."
                    else:
                        "With a little shimmy, her [Line] drop to the ground."
                elif Girl.PantsNum() >= 6:
                    "She pulls her [Girl.legs] off, then removes her [Line], before putting them back on."
                elif Girl.HoseNum() >= 6:
                    "She pulls her [Girl.hose] off, then removes her [Line], before putting them back on."
                elif Girl == JubesX and JubesX.accessory == "shut_jacket":
                    "She reaches under her jacket and pulls her [Line] down."
                elif Girl.legs:
                    "She reaches under her [Girl.legs] and pulls her [Line] down."
                else:
                    "She glances up at you as she removes her [Line]."
                call expression Girl.tag + "_First_Bottomless"

            "Just give me a clear view. . ." if (Girl.underwear and not Girl.underwear_pulled_down) or (Girl.legs and not Girl.upskirt):
                if approval >= 2:
                    if Girl == LauraX:
                        ch_l "Whatever."
                    else:
                        Girl.voice "Fine."
                    $ Girl.underwear_pulled_down = 1 if Girl.underwear else 0
                    $ Girl.upskirt = 1 if Girl.legs else 0
                    if Girl.legs:
                        "She shifts her [Girl.legs] out of the way."
                    else:
                        "She shifts her [Girl.underwear] out of the way."
                elif approval >= 1 and Girl.legs and Girl.underwear and not Girl.underwear_pulled_down:
                    if Girl == RogueX:
                        ch_r "I'll show you a little bit. . ."
                    elif Girl == KittyX:
                        ch_k "I guess I could show you something. . ."
                    elif Girl == EmmaX:
                        ch_e "I'll give at least give a little view. . ."
                    elif Girl == LauraX:
                        ch_l "Make do with this. . ."
                    elif Girl == JeanX:
                        ch_j "This should be plenty, [Girl.player_petname]."
                    elif Girl == StormX:
                        ch_s "I have taken off enough. . ."
                    elif Girl == JubesX:
                        ch_v "I guess. . . how 'bout this. . ."
                    $ Girl.upskirt = 1
                else:
                    Girl.voice "No."
                    $ Girl.recent_history.append("no_bottomless")
                    $ Girl.daily_history.append("no_bottomless")
                    return
                call expression Girl.tag + "_First_Bottomless"

            "Lose the [Girl.hose]." if Girl.hose:
                $ Girl.change_face("_bemused", 1)
                if Girl.legs:
                    Girl.voice "All right, fine."
                elif approval < 2 and not Girl.underwear and Girl.HoseNum() >= 10:
                    call NoPantiesOn (Girl)
                elif not approval and Girl.HoseNum() >= 6:
                    if Girl == RogueX:
                        ch_r "No thanks, [Girl.player_petname]."
                    else:
                        Girl.voice "Sorry, no, [Girl.player_petname]."
                    return
                else:
                    if Girl == RogueX:
                        ch_r "Ok, sure, [Girl.player_petname]."
                    else:
                        Girl.voice "Fine, [Girl.player_petname]."
                $ Line = Girl.hose
                $ Girl.hose = ""
                if Girl == KittyX:
                    if Girl.PantsNum() >= 5:
                        "She reaches a hand into her [Girl.legs] and pulls her [Line] right through her legs."
                        "She makes a little flourish and drops them to the ground."
                    else:
                        "She gives a little shake and her [Line] drop to the ground."
                elif Girl.PantsNum() >= 6:
                    "She pulls off her [Girl.legs] and pulls her [Line] off, then puts them back on."
                elif Girl.legs:
                    "She reaches under her [Girl.legs] and pulls her [Line] down."
                elif Girl.HoseNum() < 10:
                    "[Girl.name] pulls her [Line] off."
                elif not Girl.underwear:
                    $ Girl.change_face("_sly", 2)
                    "She blushes and looks at you slyly before removing her [Line]."
                    $ Girl.blushing = "_blush1"
                    call expression Girl.tag + "_First_Bottomless"
                elif not Girl.SeenPanties:
                    "[Girl.name] shyly removes her [Line]."
                    $ Girl.SeenPanties = 1
                else:
                    "[Girl.name] pulls her [Line] off."

            "Rip the [Girl.hose]." if Girl.hose == "pantyhose" or Girl.hose == "_tights":
                $ Girl.change_face("_bemused", 1)
                if Girl.legs:
                    Girl.voice "All right, fine."
                elif approval < 2 and not Girl.underwear and Girl.HoseNum() >= 10:
                    call NoPantiesOn (Girl)
                elif not approval and Girl.HoseNum() >= 6:
                    if Girl == RogueX:
                        ch_r "I'd rather you didn't, [Girl.player_petname]."
                    else:
                        Girl.voice "Sorry, no, [Girl.player_petname]."
                    return

                $ Line = Girl.hose
                if Girl.hose == "_tights":
                    $ Girl.hose = "ripped_tights"
                elif Girl.hose == "pantyhose":
                    $ Girl.hose = "ripped_pantyhose"
                if Girl.hose not in Girl.inventory:
                    $ Girl.inventory.append(Girl.hose)
                $ Girl.add_word(1,"ripped", "ripped")
                "You tear holes in her [Line]."
                if not approval_check(Girl, 1200, TabM=0):
                    $ Girl.change_face("_angry", 1,Eyes="_down")
                    if Girl == RogueX:
                        ch_r "Dammit, [Girl.player_petname], those are gettin expensive!"
                    elif Girl == KittyX:
                        ch_k "Hey, I was using those!"
                    elif Girl == EmmaX:
                        ch_e "I hope you're paying for those."
                    elif Girl == LauraX:
                        ch_l "Hey. Not cool."
                    elif Girl == JeanX:
                        ch_j "Oh, whatever."
                    elif Girl == StormX:
                        ch_s "Those do not grow on trees. . ."
                    elif Girl == JubesX:
                        ch_v "Hey! You'd better replace those. . ."
                    $ Girl.change_face("_bemused", 1)

            "Why don't you lose the sweater?" if Girl.accessory == "_sweater":
                $ Girl.accessory = ""
                "[Girl.name] tosses her sweater off."

            "Keep it all on for now." if counter == 1:
                $ counter = 0

            "Ok, that's enough for now." if counter == 2:
                $ counter = 0

        $ counter = 2 if counter else counter
        $ Line = "Anything else?"
    return


label NoPantiesOn(Girl=0):

    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    if not Girl.underwear:
        return

    if Girl == RogueX:
        if Girl.legs or Girl.HoseNum() >= 10:
            ch_r "Well, I'm not exactly decent under here, you know. . ."
        else:
            ch_r "This is the last bit. . ."
    elif Girl == KittyX:
        if Girl.legs or Girl.HoseNum() >= 10:
            ch_k "[Girl.Like]I'm not wearing any panties. . ."
        else:
            ch_k "Not much else on. . ."
    elif Girl == EmmaX:
        if Girl.legs or Girl.HoseNum() >= 10:
            ch_e "I don't have anything on under this. . ."
        else:
            ch_e "This is all I have on. . ."
    elif Girl == LauraX:
        if Girl.legs or Girl.HoseNum() >= 10:
            ch_l "I don't have anything on under this. . ."
        else:
            ch_l "These are all I have on. . ."
    elif Girl == JeanX:
        if Girl.legs or Girl.HoseNum() >= 10:
            ch_j "I don't have panties on right now. . ."
        else:
            ch_j ". . ."
    elif Girl == StormX:
        if Girl.legs or Girl.HoseNum() >= 10:
            ch_s "I am naked under this. . ."
        else:
            ch_s "This is all I have on. . ."
    elif Girl == JubesX:
        if Girl.PantsNum() >= 5 or Girl.HoseNum() >= 10:
            ch_v "I don't have anything on under this. . ."
        else:
            ch_v "This is all I've got on. . ."
    menu:
        extend ""
        "Could you do it anyway?":
            if approval_check(Girl, 1000, "LI", TabM=1):
                if Girl == RogueX:
                    ch_r "Well, if you're gonna ask so nicely. . . "
                elif Girl == KittyX:
                    ch_k "I[Girl.like]guess so. . . "
                elif Girl == EmmaX:
                    ch_e "I suppose. . . "
                elif Girl == LauraX:
                    ch_l "I guess. . . "
                elif Girl == JeanX:
                    ch_j "Oh, why not. . ."
                elif Girl == StormX:
                    ch_s "I suppose I could. . ."
                elif Girl == JubesX:
                    ch_v "Well, guess. . ."
            else:
                if Girl == RogueX:
                    ch_r "Sorry, I don't think so."
                elif Girl == KittyX:
                    ch_k "No thanks."
                elif Girl == EmmaX:
                    ch_e "I'm afraid not."
                elif Girl == LauraX:
                    ch_l "Nah, not right now."
                elif Girl == JeanX:
                    ch_j "Ha! Keep trying, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s "I do not think so, right now."
                elif Girl == JubesX:
                    ch_v "Nah. . ."
                call Bottoms_Off_Refused (Girl)
                $ renpy.pop_call()
        "Don't care, lose'em.":
            if approval_check(Girl, 800, "OI", TabM=1):
                if Girl == RogueX:
                    ch_r "Fine, whatever."
                elif Girl == KittyX:
                    ch_k "Whatev."
                elif Girl == EmmaX:
                    ch_e "If you insist."
                elif Girl == LauraX:
                    ch_l "Fine."
                elif Girl == JeanX:
                    ch_j ". . ."
                elif Girl == StormX:
                    ch_s ". . ."
                elif Girl == JubesX:
                    ch_v "Fine. . ."
            else:
                call Bottoms_Off_Refused (Girl)
                $ renpy.pop_call()
        "Ok, you can leave it on.":

            $ renpy.pop_call()
    return

label Bottoms_Off_Refused(Girl=0):
    $ Girl = GirlCheck(Girl)
    call shift_focus (Girl)

    if Girl == RogueX:
        if "no_bottomless" in Girl.recent_history:
            ch_r "What part of \"no\" escapes you, [Girl.player_petname]?"
        elif "no_bottomless" in Girl.daily_history:
            ch_r "If you keep this up, not ever, [Girl.player_petname]."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_r "That's enough, [Girl.player_petname]. Sure we can't have some fun anyway?"
            else:
                ch_r "I'm afraid not this time, [Girl.player_petname]. Sure we can't have some fun anyway?"
    elif Girl == KittyX:
        if "no_bottomless" in Girl.recent_history:
            ch_k "You're[Girl.like]on my last nerve here."
        elif "no_bottomless" in Girl.daily_history:
            ch_k "Give it a rest."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_k "What you see is what you get, but[Girl.like]can't we still have some fun?"
            else:
                ch_k "The answer's \"no,\" but[Girl.like]can't we still have some fun?"
    elif Girl == EmmaX:
        if "no_bottomless" in Girl.recent_history:
            ch_e "Try to control your impulses."
        elif "no_bottomless" in Girl.daily_history:
            ch_e "Not today."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_e "That's all I'm willing to do, is that a deal-breaker?"
            else:
                ch_e "I'm afraid not, is that a deal-breaker?"
    elif Girl == LauraX:
        if "no_bottomless" in Girl.recent_history:
            ch_l "Reign it in."
        elif "no_bottomless" in Girl.daily_history:
            ch_l "No, not today."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_l "No more, is that going to be a problem?"
            else:
                ch_l "Nope, is that going to be a problem?"
    elif Girl == JeanX:
        if "no_bottomless" in Girl.recent_history:
            ch_j "Take a breath, [Girl.player_petname]."
        elif "no_bottomless" in Girl.daily_history:
            ch_j "I made myself clear."
        else:
            $ Girl.change_face("_sad")



            ch_j "Do we have a problem?"
    elif Girl == StormX:
        if "no_bottomless" in Girl.recent_history:
            ch_s "Show some restraint."
        else:
            $ Girl.change_face("_sad")
            if counter == 2:
                ch_s "This is all, can we continue without it?"
            else:
                ch_s "I would rather not, can we continue without it?"
    elif Girl == JubesX:
        if "no_bottomless" in Girl.daily_history:
            ch_v "Like I said, nope."
        else:
            $ Girl.change_face("_sad")
            ch_v "This is it, ok?"
    menu:
        extend ""
        "Sure, never mind." if "no_bottomless" not in Girl.recent_history:
            $ Girl.mouth = "_smile"
            $ Girl.change_stat("love", 70, 2)
            $ Girl.change_stat("obedience", 60, 2)
            if Girl == RogueX:
                ch_r "Great."
            elif Girl == KittyX:
                ch_k "Great!"
            elif Girl == EmmaX:
                ch_e "Excellent."
            elif Girl == LauraX:
                ch_l "Right."
            elif Girl == JeanX:
                ch_j "Good. . ."
            elif Girl == StormX:
                ch_s "Good. . ."
            elif Girl == JubesX:
                ch_v "Cool."

        "Sorry, I'll drop it." if "no_bottomless" in Girl.recent_history:
            if Girl == EmmaX:
                ch_e "Good."
            elif Girl == LauraX:
                ch_l "Cool."
            else:
                Girl.voice "Fine. . ."
        "No, let's do something else.":

            $ Girl.brows = "_confused"
            if Girl == RogueX:
                ch_r "Ok [Girl.player_petname], your loss."
            elif Girl == KittyX:
                ch_k "Ok[Girl.like]whatever."
            elif Girl == StormX:
                ch_s "So be it. . ."
            elif Girl == JubesX:
                ch_v "Whatever. . ."
            else:
                Girl.voice "Your loss."
            $ Girl.change_stat("lust", 50, 5)
            $ Girl.change_stat("love", 70, -2, 1)
            if "no_bottomless" not in Girl.recent_history:
                $ Girl.change_stat("obedience", 60, 4)
            $ Girl.recent_history.append("_angry")
            $ Girl.daily_history.append("_angry")

    $ Girl.recent_history.append("no_bottomless")
    $ Girl.daily_history.append("no_bottomless")
    $ approval_bonus = 0
    return








label Rogue_First_Topless(Silent=0, TempLine=0):
    if RogueX.ChestNum() > 1 or RogueX.OverNum() > 2:

        return
    if RogueX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ RogueX.recent_history.append("topless")
    $ RogueX.daily_history.append("topless")
    $ RogueX.drain_word("no_topless")
    $ RogueX.SeenChest += 1
    if RogueX.SeenChest > 1:
        return

    $ RogueX.change_stat("inhibition", 70, 20)
    if not Silent:
        $ RogueX.change_face("_bemused", 1)
        "[RogueX.name] looks a bit shy, and slowly lowers her hands from her chest."
        ch_r "Well, [RogueX.player_petname]? Like what you see?"
        menu Rogue_First_TMenu:
            extend ""
            "Nod":
                $ RogueX.change_stat("love", 90, 20)
                $ RogueX.change_stat("inhibition", 70, 20)
                $ RogueX.change_face("_smile")
                ch_r ". . ."
                $ RogueX.change_stat("love", 40, 20)
            "Whatever.":
                $ RogueX.change_stat("love", 90, -30)
                $ RogueX.change_stat("obedience", 50, 20)
                $ RogueX.change_stat("inhibition", 70, -10)
                $ RogueX.change_face("_angry")
                ch_r "Hmph!"
                $ RogueX.change_stat("obedience", 70, 20)
            "Well, they aren't that bad. . .":
                $ RogueX.change_stat("love", 90, -30)
                $ RogueX.change_stat("obedience", 60, 25)
                $ RogueX.change_stat("inhibition", 70, -15)
                $ RogueX.change_face("_confused",2)
                ch_r "Say what now?"
                menu:
                    "I, um, no, they're great!":
                        $ RogueX.change_face("_angry",2, Mouth="_smile")
                        $ RogueX.change_stat("inhibition", 70, 10)
                        ch_r "Of couse they are!"
                    "[EmmaX.name]'s were bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[StormX.name]'s were bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX

                if TempLine:
                    $ RogueX.change_face("_angry")
                    $ RogueX.mouth = "_surprised"
                    $ RogueX.change_stat("love", 90, -10)
                    $ RogueX.change_stat("obedience", 80, 30)
                    $ RogueX.change_stat("inhibition", 70, -25)
                    ch_r ". . ."
                    $ RogueX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if RogueX.GirlLikeCheck(TempLine) >= 800:
                            $ RogueX.change_face("_sly",2,Eyes="_side")
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "Well, I mean they would be quite the handful. . ."
                            $ RogueX.GirlLikeUp(TempLine,20)
                        elif RogueX.GirlLikeCheck(TempLine) >= 700:
                            $ RogueX.eyes = "_side"
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "I mean, I guess, if you like that kind of thing. . ."
                        else:
                            $ RogueX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"
                    elif TempLine == KittyX:
                        if RogueX.LikeKitty >= 800:
                            $ RogueX.change_face("_sly",2,Eyes="_side")
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "They are kind of adorable. . ."
                            $ RogueX.LikeKitty += 20
                        elif RogueX.LikeKitty >= 700:
                            $ RogueX.eyes = "_side"
                            $ RogueX.change_stat("obedience", 80, 5)
                            ch_r "I mean, yeah, I guess. . ."
                        else:
                            $ RogueX.LikeKitty -= 50
                            $ TempLine = "bad"

                    if TempLine == "bad":
                        $ RogueX.change_stat("love", 90, -20)
                        ch_r "Yeah, that's enough outta you, [RogueX.player_petname]."
                        $ RogueX.change_outfit()
                        $ RogueX.recent_history.append("no_topless")
                        $ RogueX.daily_history.append("no_topless")
                        $ RogueX.recent_history.append("_angry")
                        $ RogueX.daily_history.append("_angry")
    else:
        $ RogueX.add_word(1,0, "", "", "topless")
        if approval_check(RogueX, 800) and not RogueX.Forced:
            $ RogueX.change_stat("inhibition", 70, 5)
            $ RogueX.change_stat("obedience", 70, 5)
        else:
            $ RogueX.change_stat("love", 90, -5)
            $ RogueX.change_stat("inhibition", 70, -5)
            $ RogueX.change_face("_angry")
            $ RogueX.change_stat("obedience", 70, 15)
    return


label Rogue_First_Bottomless(Silent=0):
    if RogueX.PantiesNum() > 1 or RogueX.PantsNum() > 2 or RogueX.HoseNum() > 9:

        return
    if RogueX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ RogueX.recent_history.append("bottomless")
    $ RogueX.daily_history.append("bottomless")
    $ RogueX.drain_word("no_bottomless")
    $ RogueX.SeenPussy += 1
    if RogueX.SeenPussy > 1:

        return

    $ RogueX.change_stat("inhibition", 80, 40)
    if not Silent:
        $ RogueX.change_face("_bemused", 1)
        "[RogueX.name] shyly moves her hands aside, revealing her pussy."
        menu Rogue_First_BMenu:
            ch_r "Well, [RogueX.player_petname]? Was it worth the wait?"
            "Lovely. . .":
                $ RogueX.change_stat("love", 90, 20)
                $ RogueX.change_stat("inhibition", 60, 30)
                $ RogueX.change_face("_smile")
                ch_r ". . ."
                $ RogueX.change_stat("love", 40, 20)
            "I suppose.":
                $ RogueX.change_stat("love", 90, -30)
                $ RogueX.change_stat("obedience", 50, 20)
                $ RogueX.change_stat("inhibition", 70, -20)
                $ RogueX.change_face("_angry")
                ch_r ". . ."
                $ RogueX.change_stat("obedience", 70, 30)
    else:
        $ RogueX.add_word(1,0, "", "", "bottomless")
        if approval_check(RogueX, 500):
            $ RogueX.change_stat("inhibition", 60, 30)
        else:
            $ RogueX.change_stat("love", 90, -5)
            $ RogueX.change_stat("inhibition", 70, -5)
            $ RogueX.change_face("_angry")
            $ RogueX.change_stat("obedience", 70, 15)
    return


label Kitty_First_Topless(Silent=0, TempLine=0):
    if KittyX.ChestNum() > 1 or KittyX.OverNum() > 2:

        return
    if KittyX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ KittyX.recent_history.append("topless")
    $ KittyX.daily_history.append("topless")
    $ KittyX.drain_word("no_topless")
    $ KittyX.SeenChest += 1
    if KittyX.SeenChest > 1:
        return


    $ KittyX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ KittyX.change_face("_bemused", 2)
        "Kitty looks a bit shy, and slowly lowers her hands from her chest."
        ch_k "[KittyX.Like]what do you think?"
        $ KittyX.blushing = "_blush1"
        menu Kitty_First_TMenu:
            extend ""
            "Lovely.":
                $ KittyX.change_stat("love", 90, 20)
                $ KittyX.change_stat("inhibition", 70, 20)
                $ KittyX.change_face("_smile",2)
                ch_k ". . ."
                $ KittyX.change_stat("love", 40, 20)
                $ KittyX.blushing = "_blush1"
            "That's it?":

                $ KittyX.change_stat("love", 90, -30)
                $ KittyX.change_stat("obedience", 60, 25)
                $ KittyX.change_stat("inhibition", 70, -15)
                $ KittyX.change_face("_confused",2)
                ch_k "What?"
                menu:
                    "I, um, no, they're great!":
                        $ KittyX.change_face("_angry",2, Mouth="_smile")
                        $ KittyX.change_stat("inhibition", 70, 10)
                        ch_k "Obviously!"
                    "[EmmaX.name]'s were bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[RogueX.name]'s were bigger, that's all." if RogueX.SeenChest:
                        $ TempLine = RogueX
                    "[LauraX.name]'s were bigger, that's all." if LauraX.SeenChest:
                        $ TempLine = LauraX
                    "[JeanX.name]'s were bigger, that's all." if JeanX.SeenChest:
                        $ TempLine = JeanX
                    "[StormX.name]'s were bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ KittyX.change_face("_angry")
                    $ KittyX.mouth = "_surprised"
                    $ KittyX.change_stat("love", 90, -10)
                    $ KittyX.change_stat("obedience", 80, 30)
                    $ KittyX.change_stat("inhibition", 70, -25)
                    ch_k ". . ."
                    $ KittyX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if KittyX.GirlLikeCheck(TempLine) >= 800:
                            $ KittyX.change_face("_sly",2,Eyes="_side")
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "Yeah, like you just wanna shove your head into there. . ."
                            $ KittyX.GirlLikeUp(TempLine,20)
                        elif KittyX.GirlLikeCheck(TempLine) >= 700:
                            $ KittyX.eyes = "_side"
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "I mean, I guess, if you like that kind of thing. . ."
                        else:
                            $ KittyX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"
                    elif TempLine:
                        if KittyX.GirlLikeCheck(TempLine) >= 800:
                            $ KittyX.change_face("_sly",2,Eyes="_side")
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "Yeah, like two ripe apples. . . I mean-"
                            $ KittyX.GirlLikeUp(TempLine,20)
                        elif KittyX.GirlLikeCheck(TempLine) >= 700:
                            $ KittyX.eyes = "_side"
                            $ KittyX.change_stat("obedience", 80, 5)
                            ch_k "[KittyX.Like]I guess. . ."
                        else:
                            $ KittyX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"

                    if TempLine == "bad":
                        $ KittyX.change_stat("love", 90, -20)
                        ch_k "Well you sure know how to ruin a mood."
                        $ KittyX.change_outfit()
                        $ KittyX.recent_history.append("no_topless")
                        $ KittyX.daily_history.append("no_topless")
                        $ KittyX.recent_history.append("_angry")
                        $ KittyX.daily_history.append("_angry")
    else:


        $ KittyX.add_word(1,0, "", "", "topless")
        if approval_check(KittyX, 800) and not KittyX.Forced:
            $ KittyX.change_stat("inhibition", 70, 5)
            $ KittyX.change_stat("obedience", 70, 10)
        else:
            $ KittyX.change_stat("love", 90, -5)
            $ KittyX.change_stat("inhibition", 70, -5)
            $ KittyX.change_face("_angry")
            $ KittyX.change_stat("obedience", 70, 20)
    return

label Kitty_First_Bottomless(Silent=0):
    if KittyX.PantiesNum() > 1 or KittyX.PantsNum() > 2 or KittyX.HoseNum() > 9:

        return
    if KittyX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ KittyX.recent_history.append("bottomless")
    $ KittyX.daily_history.append("bottomless")
    $ KittyX.drain_word("no_bottomless")
    $ KittyX.SeenPussy += 1
    if KittyX.SeenPussy > 1:
        return

    $ KittyX.change_stat("inhibition", 80, 30)
    $ KittyX.change_stat("obedience", 70, 10)
    if not Silent:
        $ KittyX.change_face("_bemused", 1)
        "[KittyX.name] shyly moves her hands aside, revealing her pussy."
        menu Kitty_First_BMenu:
            extend ""
            "Lovely. . .":
                $ KittyX.change_stat("love", 90, 20)
                $ KittyX.change_stat("inhibition", 60, 25)
                $ KittyX.change_face("_smile")
                ch_k ". . ."
                $ KittyX.change_stat("love", 40, 20)
            "Now {i}that's{/i} the \"Kitty\" I wanted to see.":
                $ KittyX.change_stat("love", 40, 25)
                $ KittyX.change_stat("inhibition", 60, 30)
                $ KittyX.change_face("_perplexed", 2)
                ch_k "[[snort]"
                $ KittyX.change_stat("love", 90, 25)
                $ KittyX.blushing = "_blush1"
            "Pretty messy down there." if KittyX.pubes:
                $ KittyX.change_face("_surprised",2)
                ch_k "!"
                if approval_check(KittyX, 800, "LO"):
                    $ KittyX.change_face("_bemused",1)
                    $ KittyX.change_stat("obedience", 50, 30)
                    $ KittyX.change_stat("inhibition", 60, 25)
                    ch_k "I guess I could trim it up a bit. . ."
                    $ KittyX.Todo.append("shave")
                else:
                    $ KittyX.change_face("_angry",1)
                    $ KittyX.change_stat("love", 40, -20)
                    $ KittyX.change_stat("obedience", 50, 25)
                    $ KittyX.change_stat("inhibition", 60, -5)
                    ch_k "Well[KittyX.like]sorry I don't keep it baby soft!"
            "I've seen better.":
                $ KittyX.change_stat("love", 90, -30)
                $ KittyX.change_stat("obedience", 50, 25)
                $ KittyX.change_stat("inhibition", 70, -30)
                $ KittyX.change_face("_angry")
                ch_k ". . ."
                $ KittyX.change_stat("obedience", 70, 35)
    else:
        $ KittyX.add_word(1,0, "", "", "bottomless")
        if approval_check(KittyX, 800) and not KittyX.Forced:
            $ KittyX.change_stat("inhibition", 60, 15)
            $ KittyX.change_stat("obedience", 70, 10)
        else:
            $ KittyX.change_stat("love", 90, -10)
            $ KittyX.change_stat("inhibition", 70, -5)
            $ KittyX.change_face("_angry")
            $ KittyX.change_stat("obedience", 70, 20)
    return



label Emma_First_Topless(Silent=0, TempLine=0):
    if EmmaX.ChestNum() > 1 or EmmaX.OverNum() > 2:

        return
    if EmmaX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ EmmaX.recent_history.append("topless")
    $ EmmaX.daily_history.append("topless")
    $ EmmaX.drain_word("no_topless")
    $ EmmaX.SeenChest += 1
    if EmmaX.SeenChest > 1:
        return


    $ EmmaX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ EmmaX.change_face("_sly")
        "You get your first look at [EmmaX.name]'s bare chest."
        ch_e "Well, [EmmaX.player_petname]? Is it everything you dreamed?"
        $ EmmaX.blushing = "_blush1"
        menu Emma_First_TMenu:
            extend ""
            "Definitely, and more.":
                $ EmmaX.change_stat("love", 90, 20)
                $ EmmaX.change_stat("inhibition", 70, 20)
                $ EmmaX.change_face("_smile",1)
                ch_e "I do aim to impress."
                $ EmmaX.change_stat("love", 40, 20)
                $ EmmaX.blushing = ""
            ". . . [[stunned]":
                $ EmmaX.change_stat("love", 90, 20)
                $ EmmaX.change_stat("inhibition", 70, 30)
                ch_e "Yes, that would be the usual reaction."
                $ EmmaX.change_stat("love", 40, 10)
            "Huh, not what I was expecting. . .":
                $ EmmaX.change_stat("love", 90, -30)
                $ EmmaX.change_stat("obedience", 60, 25)
                $ EmmaX.change_stat("inhibition", 70, -15)
                $ EmmaX.change_face("_confused",2)
                ch_e "What?"
                menu:
                    "They're even better than I imagined!":
                        $ EmmaX.change_stat("love", 90, 20)
                        $ EmmaX.change_stat("obedience", 60, -20)
                        $ EmmaX.change_stat("inhibition", 70, 20)
                        $ EmmaX.change_face("_perplexed",1)
                        ch_e "Well, I suppose you managed to salvage that one. . ."
                    "I, um, no, they're great!":
                        $ EmmaX.change_face("_angry",2, Mouth="_smile")
                        $ EmmaX.change_stat("inhibition", 70, 10)
                        ch_e "Of couse they are!"
                    "[RogueX.name]'s were tighter, that's all." if RogueX.SeenChest:
                        $ TempLine = RogueX
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX
                    "[LauraX.name]'s were tighter, that's all." if LauraX.SeenChest:
                        $ TempLine = LauraX
                    "[JeanX.name]'s were tighter, that's all." if JeanX.SeenChest:
                        $ TempLine = JeanX
                    "[StormX.name]'s were larger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ EmmaX.change_face("_angry")
                    $ EmmaX.mouth = "_surprised"
                    $ EmmaX.change_stat("love", 90, -10)
                    $ EmmaX.change_stat("obedience", 80, 30)
                    $ EmmaX.change_stat("inhibition", 70, -25)
                    ch_e ". . ."
                    $ EmmaX.mouth = "_sad"
                    if TempLine == KittyX:
                        if EmmaX.LikeKitty >= 800:
                            $ EmmaX.change_face("_sly",2,Eyes="_side")
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "They are rather . . . pert. . ."
                            $ EmmaX.LikeKitty += 20
                        elif EmmaX.LikeKitty >= 700:
                            $ EmmaX.eyes = "_side"
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "Well, for a child. . ."
                        else:
                            $ EmmaX.LikeKitty -= 50
                            $ TempLine = "bad"

                    elif TempLine == StormX:
                        if EmmaX.GirlLikeCheck(TempLine) >= 800:
                            $ EmmaX.change_face("_sly",2,Eyes="_side")
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "They are lovely, but. . ."
                            $ EmmaX.GirlLikeUp(TempLine,20)
                        elif EmmaX.GirlLikeCheck(TempLine) >= 700:
                            $ EmmaX.eyes = "_side"
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "I don't know about that. . ."
                        else:
                            $ EmmaX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"
                    elif TempLine:
                        if EmmaX.GirlLikeCheck(TempLine) >= 800:
                            $ EmmaX.change_face("_sly",2,Eyes="_side")
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "They are rather . . . ripe. . ."
                            $ EmmaX.GirlLikeUp(TempLine,20)
                        elif EmmaX.GirlLikeCheck(TempLine) >= 700:
                            $ EmmaX.eyes = "_side"
                            $ EmmaX.change_stat("obedience", 80, 5)
                            ch_e "I suppose if you prefer that. . ."
                        else:
                            $ EmmaX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"


                    if TempLine == "bad":
                        $ EmmaX.change_stat("love", 90, -20)
                        ch_e "I think you've seen enough for now, [EmmaX.player_petname]."
                        $ EmmaX.change_outfit()
                        $ EmmaX.recent_history.append("no_topless")
                        $ EmmaX.daily_history.append("no_topless")
                        $ EmmaX.recent_history.append("_angry")
                        $ EmmaX.daily_history.append("_angry")
    else:


        $ EmmaX.add_word(1,0, "", "", "topless")
        if approval_check(EmmaX, 800) and not EmmaX.Forced:
            $ EmmaX.change_stat("inhibition", 70, 5)
            $ EmmaX.change_stat("obedience", 70, 5)
        else:
            $ EmmaX.change_stat("love", 90, -10)
            $ EmmaX.change_stat("inhibition", 70, -5)
            $ EmmaX.change_face("_angry")
            $ EmmaX.change_stat("obedience", 70, 15)
    return


label Emma_First_Bottomless(Silent=0):
    if EmmaX.PantiesNum() > 1 or EmmaX.PantsNum() > 2 or EmmaX.HoseNum() > 9:

        return
    if EmmaX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ EmmaX.recent_history.append("bottomless")
    $ EmmaX.daily_history.append("bottomless")
    $ EmmaX.drain_word("no_bottomless")
    $ EmmaX.SeenPussy += 1
    if EmmaX.SeenPussy > 1:
        return


    $ EmmaX.change_stat("inhibition", 80, 30)
    $ EmmaX.change_stat("obedience", 70, 10)
    if not Silent:
        $ EmmaX.change_face("_sly")
        "You find yourself staring at [EmmaX.name]'s bare pussy."
        menu Emma_First_BMenu:
            extend ""
            "Niiice. . .":
                $ EmmaX.change_stat("love", 90, 20)
                $ EmmaX.change_stat("inhibition", 60, 25)
                $ EmmaX.change_face("_smile")
                ch_e "I'm aware. . . "
                $ EmmaX.change_stat("love", 40, 20)
            "I see you keep it smooth down there." if not EmmaX.pubes:
                $ EmmaX.change_face("_confused",1)
                ch_e "Yes?"
                if approval_check(EmmaX, 700, "LO"):
                    $ EmmaX.change_face("_bemused")
                    menu:
                        ch_e "Do you prefer more fuzz?"
                        "Yes":
                            if approval_check(EmmaX, 900, "LO"):
                                $ EmmaX.change_stat("obedience", 50, 30)
                                $ EmmaX.change_stat("inhibition", 60, 25)
                                ch_e "I suppose I could let it go. . ."
                                $ EmmaX.Todo.append("pubes")
                            else:
                                $ EmmaX.change_face("_normal")
                                ch_e "Well that's a pity."
                        "Up to you, I guess.":
                            $ EmmaX.change_stat("love", 80, 10)
                            ch_e "I'm glad you agree."
                        "No, leave it that way.":
                            if approval_check(EmmaX, 900, "LO"):
                                $ EmmaX.change_face("_sly")
                                $ EmmaX.change_stat("love", 80, 10)
                            else:
                                $ EmmaX.change_face("_angry",Mouth="_normal")
                            $ EmmaX.change_stat("inhibition", 60, 25)
                            ch_e "I'm glad I have your. . . permission."
                            $ EmmaX.brows = "_normal"
                else:
                    $ EmmaX.change_face("_angry",1)
                    $ EmmaX.change_stat("love", 40, -20)
                    $ EmmaX.change_stat("obedience", 50, 25)
                    $ EmmaX.change_stat("inhibition", 60, -5)
                    ch_e "Yes, I'm afraid I don't like an unkept garden."
            "Not bad for someone your age.":
                $ EmmaX.change_stat("love", 90, -30)
                $ EmmaX.change_stat("obedience", 50, 25)
                $ EmmaX.change_stat("inhibition", 70, -30)
                $ EmmaX.change_face("_angry",2)
                if not EmmaX.Forced and not approval_check(EmmaX, 900, "LO"):
                    $ EmmaX.recent_history.append("_angry")
                    $ EmmaX.daily_history.append("_angry")
                    $ EmmaX.change_stat("obedience", 70, 25)
                ch_e "You will regret that remark. . ."
    else:

        $ EmmaX.add_word(1,0, "", "", "bottomless")
        if approval_check(EmmaX, 800) and not EmmaX.Forced:
            $ EmmaX.change_stat("inhibition", 60, 5)
            $ EmmaX.change_stat("obedience", 70, 10)
        else:
            $ EmmaX.change_stat("love", 90, -10)
            $ EmmaX.change_stat("inhibition", 70, -5)
            $ EmmaX.change_face("_angry")
            $ EmmaX.change_stat("obedience", 70, 15)
    return


label Laura_First_Topless(Silent=0, TempLine=0):
    if LauraX.ChestNum() > 1 or LauraX.OverNum() > 2:

        return
    if LauraX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ LauraX.recent_history.append("topless")
    $ LauraX.daily_history.append("topless")
    $ LauraX.drain_word("no_topless")
    $ LauraX.SeenChest += 1
    if LauraX.SeenChest > 1:
        return

    $ LauraX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ LauraX.change_face("_sly")
        "You get your first look at Laura's bare chest."
        ch_l "So? What are you looking at?"
        $ LauraX.blushing = "_blush1"
        menu Laura_First_TMenu:
            extend ""
            "Your tits? They look great.":
                $ LauraX.change_stat("love", 90, 20)
                $ LauraX.change_stat("inhibition", 70, 20)
                $ LauraX.change_face("_sexy",1,Eyes="_down")
                ch_l "Huh. I mean I guess so. . ."
                $ LauraX.change_face("_smile", 0)
                $ LauraX.change_stat("love", 40, 20)
            ". . . [[stunned]":
                $ LauraX.change_stat("love", 90, 10)
                $ LauraX.change_stat("inhibition", 70, 10)
                ch_l "Cat got your tongue?"
                $ LauraX.change_stat("love", 40, 10)
            "Huh, not what I was expecting. . .":
                $ LauraX.change_stat("love", 90, -30)
                $ LauraX.change_stat("obedience", 60, 25)
                $ LauraX.change_stat("inhibition", 70, -15)
                $ LauraX.change_face("_confused",2)
                ch_l "Huh?"
                menu:
                    "They're really perky!":
                        $ LauraX.change_stat("love", 90, 20)
                        $ LauraX.change_stat("obedience", 60, -20)
                        $ LauraX.change_stat("inhibition", 70, 20)
                        $ LauraX.change_face("_perplexed",1)
                        ch_l "Oh. Right. . ."
                    "I, um, no, they're great!":
                        $ LauraX.change_face("_angry",2, Mouth="_smile")
                        $ LauraX.change_stat("inhibition", 70, 10)
                        ch_l "Why wouldn't they be?"
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX
                    "[EmmaX.name]'s were a lot bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[StormX.name]'s were a lot bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ LauraX.change_face("_angry")
                    $ LauraX.mouth = "_surprised"
                    $ LauraX.change_stat("love", 90, -10)
                    $ LauraX.change_stat("obedience", 80, 30)
                    $ LauraX.change_stat("inhibition", 70, -25)
                    ch_l ". . ."
                    $ LauraX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if LauraX.GirlLikeCheck(TempLine) >= 800:
                            $ LauraX.change_face("_sly",2,Eyes="_side")
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "They are kinda huge. . ."
                            $ LauraX.GirlLikeUp(TempLine,20)
                        elif LauraX.GirlLikeCheck(TempLine) >= 700:
                            $ LauraX.eyes = "_side"
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "I guess that's true. . ."
                        else:
                            $ LauraX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"

                    elif TempLine == KittyX:
                        if LauraX.LikeKitty >= 800:
                            $ LauraX.change_face("_sly",2,Eyes="_side")
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "She is very. . . streamlined. . ."
                            $ LauraX.LikeKitty += 20
                        elif LauraX.LikeKitty >= 700:
                            $ LauraX.eyes = "_side"
                            $ LauraX.change_stat("obedience", 80, 5)
                            ch_l "they are kinda. . . pointy. . ."
                        else:
                            $ LauraX.LikeKitty -= 50
                            $ TempLine = "bad"


                    if TempLine == "bad":
                        $ LauraX.change_stat("love", 90, -20)
                        ch_l "Still kinda rude though."
                        $ LauraX.change_outfit()
                        $ LauraX.recent_history.append("no_topless")
                        $ LauraX.daily_history.append("no_topless")
                        $ LauraX.recent_history.append("_angry")
                        $ LauraX.daily_history.append("_angry")
    else:


        $ LauraX.add_word(1,0, "", "", "topless")
        if approval_check(LauraX, 800) and not LauraX.Forced:
            $ LauraX.change_stat("inhibition", 70, 5)
            $ LauraX.change_stat("obedience", 70, 10)
        else:
            $ LauraX.change_stat("love", 90, -5)
            $ LauraX.change_stat("inhibition", 70, -5)
            $ LauraX.change_face("_angry")
            $ LauraX.change_stat("obedience", 70, 10)
    return


label Laura_First_Bottomless(Silent=0):
    if LauraX.PantiesNum() > 1 or LauraX.PantsNum() > 2 or LauraX.HoseNum() > 9:

        return
    if LauraX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ LauraX.recent_history.append("bottomless")
    $ LauraX.daily_history.append("bottomless")
    $ LauraX.drain_word("no_bottomless")
    $ LauraX.SeenPussy += 1
    if LauraX.SeenPussy > 1:
        return


    $ LauraX.change_stat("inhibition", 80, 30)
    $ LauraX.change_stat("obedience", 70, 10)
    if not Silent:
        $ LauraX.change_face("_sly")
        if LauraX.pubes:
            "You find yourself staring at [LauraX.name]'s furry pussy."
        else:
            "You find yourself staring at [LauraX.name]'s bare pussy."
        menu Laura_First_BMenu:
            extend ""
            "Niiice. . .":
                $ LauraX.change_stat("love", 90, 20)
                $ LauraX.change_stat("inhibition", 60, 25)
                $ LauraX.change_face("_smile")
                ch_l "You think?"
                ch_l "Yeah, I like it too. . . "
                $ LauraX.change_stat("love", 40, 20)
            "I see you keep it natural down there." if LauraX.pubes:
                $ LauraX.change_face("_confused",1)
                ch_l "Well. . . yeah."
                if approval_check(LauraX, 700, "LO"):
                    $ LauraX.change_face("_bemused")
                    menu:
                        ch_l "What, am I supposed to shave it?"
                        "Yes":
                            if approval_check(LauraX, 900, "LO"):
                                $ LauraX.change_stat("obedience", 50, 30)
                                $ LauraX.change_stat("inhibition", 60, 25)
                                ch_l "I guess I could. . ."
                                $ LauraX.Todo.append("pubes")
                            else:
                                $ LauraX.change_face("_normal")
                                ch_l "Seems like a waste of time."
                                ch_l "Do you know how fast my hair grows?"
                        "Up to you, I guess.":
                            $ LauraX.change_stat("love", 80, 10)
                            ch_l "Yeah, I mean, shaving would be a lot of work."
                        "No, leave it that way.":
                            if approval_check(LauraX, 900, "LO"):
                                $ LauraX.change_face("_sly")
                                $ LauraX.change_stat("love", 80, 10)
                            else:
                                $ LauraX.change_face("_angry",Mouth="_normal")
                            $ LauraX.change_stat("inhibition", 60, 25)
                            ch_l "Right."
                            $ LauraX.brows = "_normal"
                else:
                    $ LauraX.change_face("_angry",1)
                    $ LauraX.change_stat("love", 40, -20)
                    $ LauraX.change_stat("obedience", 50, 25)
                    $ LauraX.change_stat("inhibition", 60, -5)
                    ch_l "I mean, what else would I do?"
            "What a mess.":
                $ LauraX.change_stat("love", 90, -30)
                $ LauraX.change_stat("obedience", 50, 25)
                $ LauraX.change_stat("inhibition", 70, -30)
                $ LauraX.change_face("_angry",2)
                if not LauraX.Forced and not approval_check(LauraX, 900, "LO"):
                    $ LauraX.recent_history.append("_angry")
                    $ LauraX.daily_history.append("_angry")
                    $ LauraX.change_stat("obedience", 70, 25)
                ch_l "I'll make you a mess. . ."
    else:
        $ LauraX.add_word(1,0, "", "", "bottomless")
        if approval_check(LauraX, 800) and not LauraX.Forced:
            $ LauraX.change_stat("inhibition", 60, 5)
            $ LauraX.change_stat("obedience", 70, 10)
        else:
            $ LauraX.change_stat("love", 90, -5)
            $ LauraX.change_stat("inhibition", 70, -5)
            $ LauraX.change_face("_angry")
            $ LauraX.change_stat("obedience", 70, 15)
    return



label Jean_First_Topless(Silent=0, TempLine=0):
    if (JeanX.ChestNum() > 1 or JeanX.OverNum() > 2) and not TempLine:


        return
    if JeanX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JeanX.recent_history.append("topless")
    $ JeanX.daily_history.append("topless")
    $ JeanX.drain_word("no_topless")
    $ JeanX.SeenChest += 1
    if JeanX.SeenChest > 1:
        return

    $ JeanX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ JeanX.change_face("_sly")
        "You get your first look at Jean's bare chest."
        ch_j "So, pretty spectacular, right?"
        $ JeanX.blushing = "_blush1"
        menu Jean_First_TMenu:
            extend ""
            "Yeah, they look amazing.":
                $ JeanX.change_stat("love", 90, 10)
                $ JeanX.change_stat("inhibition", 200, 20)
                $ JeanX.change_face("_sexy",1,Eyes="_down")
                ch_j "Yeah, they are pretty tight. . ."
                $ JeanX.change_face("_smile", 0)
                $ JeanX.change_stat("obedience", 40, 20)
            ". . . [[stunned]":
                $ JeanX.change_stat("love", 90, 20)
                $ JeanX.change_stat("inhibition", 200, 10)
                ch_j "Stunning, I know."
                $ JeanX.change_stat("obedience", 40, 10)
            "Huh, not what I was expecting. . .":
                $ JeanX.change_stat("love", 90, 10)
                $ JeanX.change_stat("obedience", 40, 20)
                $ JeanX.change_stat("inhibition", 200, 20)
                $ JeanX.change_face("_smile", 0)
                ch_j "Exactl-{w=0.3}{nw}"
                $ JeanX.change_stat("love", 90, -40)
                $ JeanX.change_stat("obedience", 60, 10)
                $ JeanX.change_stat("inhibition", 200, -15)
                $ JeanX.change_face("_confused",2)
                ch_j "Exactl- wait, what?"
                $ TempLine = 0
                menu:
                    "They're really perky!":
                        $ JeanX.change_stat("love", 90, 10)
                        $ JeanX.change_stat("obedience", 60, 10)
                        $ JeanX.change_stat("inhibition", 200, 20)
                        $ JeanX.change_face("_perplexed",1)
                        ch_j "Oh. Of course. . ."
                    "I, um, no, they're great!":
                        $ JeanX.change_face("_angry",2, Mouth="_smile")
                        $ JeanX.change_stat("obedience", 80, 20)
                        ch_j "Of course they are!"
                    "[RogueX.name]'s were nicer, that's all." if RogueX.SeenChest:
                        $ TempLine = RogueX
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX
                    "[EmmaX.name]'s were a lot bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[LauraX.name]'s were nicer, that's all." if LauraX.SeenChest:
                        $ TempLine = LauraX
                    "[StormX.name]'s were a lot bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ JeanX.change_face("_angry")
                    $ JeanX.mouth = "_surprised"
                    $ JeanX.change_stat("love", 50, -10)
                    $ JeanX.change_stat("love", 90, -10)
                    $ JeanX.change_stat("obedience", 50, 10)
                    $ JeanX.change_stat("obedience", 80, 30)
                    $ JeanX.change_stat("inhibition", 200, -15)
                    ch_j ". . ."
                    $ JeanX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if JeanX.GirlLikeCheck(TempLine) >= 700:
                            $ JeanX.change_face("_sly",2,Eyes="_side")
                            ch_j "Well, they are. . . heavy. . ."
                            $ JeanX.GirlLikeUp(TempLine,20)
                        else:
                            $ JeanX.eyes = "_side"
                            ch_j "If you have a thing for udders. . ."
                            $ JeanX.LikeEmma -= 50
                            $ JeanX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"

                    elif TempLine == KittyX:
                        if JeanX.LikeKitty >= 700:
                            $ JeanX.change_face("_sly",2,Eyes="_side")
                            ch_j "She is very. . . cute. . ."
                            $ JeanX.LikeKitty += 20
                        else:
                            $ JeanX.eyes = "_side"
                            ch_j "If you have a thing for surf boards. . ."
                            $ JeanX.LikeKitty -= 50
                            $ TempLine = "bad"
                    else:
                        if JeanX.GirlLikeCheck(TempLine) >= 700:
                            $ JeanX.change_face("_sly",2,Eyes="_side")
                            ch_j "She is very. . . petite. . ."
                            $ JeanX.GirlLikeUp(TempLine,20)
                        else:
                            $ JeanX.eyes = "_side"
                            ch_j "they are kinda. . . pointy. . ."
                            $ JeanX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"


                    if TempLine == "bad":
                        $ JeanX.change_stat("love", 90, -20)
                        ch_j "Still, inappropriate on your part!"
                        $ JeanX.change_outfit()
                        $ JeanX.recent_history.append("no_topless")
                        $ JeanX.daily_history.append("no_topless")
                        $ JeanX.recent_history.append("_angry")
                        $ JeanX.daily_history.append("_angry")
    else:


        if approval_check(JeanX, 800) and not JeanX.Forced:
            $ JeanX.change_stat("love", 70, 10)
            $ JeanX.change_stat("obedience", 70, 25)
            $ JeanX.change_stat("inhibition", 70, 15)
        else:
            $ JeanX.change_stat("love", 90, -40)
            $ JeanX.change_stat("inhibition", 200, -20)
            $ JeanX.change_face("_angry")
            $ JeanX.change_stat("obedience", 70, 40)
    return


label Jean_First_Bottomless(Silent=0):
    if JeanX.PantiesNum() > 1 or JeanX.PantsNum() > 2 or JeanX.HoseNum() > 9:

        return
    if JeanX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JeanX.recent_history.append("bottomless")
    $ JeanX.daily_history.append("bottomless")
    $ JeanX.drain_word("no_bottomless")
    $ JeanX.SeenPussy += 1
    if JeanX.SeenPussy > 1:
        return

    $ JeanX.change_stat("inhibition", 200, 30)
    $ JeanX.change_stat("obedience", 90, 10)
    if not Silent:
        $ JeanX.change_face("_sly")
        if JeanX.pubes:
            "You find yourself staring at [JeanX.name]'s fuzzy pussy."
        else:
            "You find yourself staring at [JeanX.name]'s bare pussy."
        menu Jean_First_BMenu:
            extend ""
            "Niiice. . .":
                $ JeanX.change_stat("love", 90, 20)
                $ JeanX.change_stat("inhibition", 200, 25)
                $ JeanX.change_face("_smile")
                ch_j "Right?"
                $ JeanX.change_stat("love", 40, 20)
            "I see you got a fire crotch down there." if JeanX.pubes:
                $ JeanX.change_face("_confused",1)
                ch_j "Well. . . yeah."
                if approval_check(JeanX, 700, "LO"):
                    $ JeanX.change_face("_bemused")
                    menu:
                        ch_j "Do you prefer it smooth?"
                        "Yes":
                            if approval_check(JeanX, 900, "LO"):
                                $ JeanX.change_stat("obedience", 90, 30)
                                $ JeanX.change_stat("inhibition", 200, 25)
                                ch_j "Hmm, I guess. . ."
                                $ JeanX.Todo.append("pubes")
                            else:
                                $ JeanX.change_face("_normal")
                                ch_j "Not worth the hassle."
                        "Up to you, I guess.":
                            $ JeanX.change_stat("love", 80, 10)
                            ch_j "Of course it is."
                        "No, leave it that way.":
                            if approval_check(JeanX, 900, "LO"):
                                $ JeanX.change_face("_sly")
                                $ JeanX.change_stat("love", 80, 10)
                            else:
                                $ JeanX.change_face("_angry",Mouth="_normal")
                            $ JeanX.change_stat("inhibition", 200, 25)
                            ch_j "Of course."
                            $ JeanX.brows = "_normal"
                else:
                    $ JeanX.change_face("_angry",1)
                    $ JeanX.change_stat("love", 40, -20)
                    $ JeanX.change_stat("obedience", 90, 25)
                    $ JeanX.change_stat("inhibition", 200, -5)
                    ch_j "I didn't really feel like waxing it."
            "What a mess." if JeanX.pubes:
                $ JeanX.change_stat("love", 90, -30)
                $ JeanX.change_stat("obedience", 90, 25)
                $ JeanX.change_stat("inhibition", 200, -30)
                $ JeanX.change_face("_angry",2)
                if not JeanX.Forced and not approval_check(JeanX, 900, "LO"):
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")
                    $ JeanX.change_stat("obedience", 90, 25)
                ch_j "Oh, so it's not baby-smooth like [EmmaX.name]'s?"
            "Eh, I've seen better" if not JeanX.pubes:
                $ JeanX.change_stat("love", 90, -30)
                $ JeanX.change_stat("obedience", 90, 25)
                $ JeanX.change_stat("inhibition", 200, -30)
                $ JeanX.change_face("_angry",2)
                if not JeanX.Forced and not approval_check(JeanX, 900, "LO"):
                    $ JeanX.recent_history.append("_angry")
                    $ JeanX.daily_history.append("_angry")
                    $ JeanX.change_stat("obedience", 90, 25)
                ch_j "Oh, so it's not saggy like [EmmaX.name]'s?"
    else:
        $ JeanX.add_word(1,0, "", "", "bottomless")
        if approval_check(JeanX, 800) and not JeanX.Forced:
            $ JeanX.change_stat("inhibition", 60, 5)
            $ JeanX.change_stat("obedience", 90, 10)
        else:
            $ JeanX.change_stat("love", 90, -5)
            $ JeanX.change_stat("inhibition", 200, -5)
            $ JeanX.change_face("_angry")
            $ JeanX.change_stat("obedience", 90, 15)
    return



label Storm_First_Topless(Silent=0, TempLine=0):

    if StormX.ChestNum() > 1 or StormX.OverNum() > 2:

        return
    if StormX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ StormX.recent_history.append("topless")
    $ StormX.daily_history.append("topless")
    $ StormX.drain_word("no_topless")
    $ StormX.SeenChest += 1
    return


label Storm_First_Bottomless(Silent=0):
    if StormX.PantiesNum() > 1 or StormX.PantsNum() > 2 or StormX.HoseNum() > 9:

        return
    if StormX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ StormX.recent_history.append("bottomless")
    $ StormX.daily_history.append("bottomless")
    $ StormX.drain_word("no_bottomless")
    $ StormX.SeenPussy += 1
    return



label Jubes_First_Topless(Silent=0, TempLine=0):
    if JubesX.ChestNum() > 1 or JubesX.OverNum() > 2:

        return
    if JubesX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JubesX.recent_history.append("topless")
    $ JubesX.daily_history.append("topless")
    $ JubesX.drain_word("no_topless")
    $ JubesX.SeenChest += 1
    if JubesX.SeenChest > 1:
        return

    $ JubesX.change_stat("inhibition", 70, 15)
    if not Silent:
        $ JubesX.change_face("_sly")
        "You get your first look at Jubes's bare chest."
        ch_v "So. . . um. . . like what you see?"
        $ JubesX.blushing = "_blush1"
        menu Jubes_First_TMenu:
            extend ""
            "Your tits? They look great.":
                $ JubesX.change_stat("love", 90, 20)
                $ JubesX.change_stat("inhibition", 70, 20)
                $ JubesX.change_face("_smile",2)
                pause 0.5
                $ JubesX.change_face("_sexy",1,Eyes="_down")
                ch_v "Ah! Um. . . yeah, I guess. . ."
                $ JubesX.change_face("_smile")
                $ JubesX.change_stat("love", 40, 20)
            ". . . [[stunned]":
                $ JubesX.change_stat("love", 90, 10)
                $ JubesX.change_stat("inhibition", 70, 10)
                ch_v "Oh, that's a \"hit.\""
                $ JubesX.change_stat("love", 40, 10)
            "Huh, not what I was expecting. . .":
                $ JubesX.change_stat("love", 90, -30)
                $ JubesX.change_stat("obedience", 60, 25)
                $ JubesX.change_stat("inhibition", 70, -15)
                $ JubesX.change_face("_confused",2)
                ch_v "Wha?"
                menu:
                    "They're really perky!":
                        $ JubesX.change_stat("love", 90, 20)
                        $ JubesX.change_stat("obedience", 60, -20)
                        $ JubesX.change_stat("inhibition", 70, 20)
                        $ JubesX.change_face("_perplexed",1)
                        ch_v "Oh. Right. . ."
                    "I, um, no, they're great!":
                        $ JubesX.change_face("_angry",2, Mouth="_smile")
                        $ JubesX.change_stat("inhibition", 70, 10)
                        ch_v ". . ."
                        ch_v "I -know- that, that's why I was confused?"
                    "[KittyX.name]'s were tighter, that's all." if KittyX.SeenChest:
                        $ TempLine = KittyX
                    "[EmmaX.name]'s were a lot bigger, that's all." if EmmaX.SeenChest:
                        $ TempLine = EmmaX
                    "[StormX.name]'s were a lot bigger, that's all." if StormX.SeenChest:
                        $ TempLine = StormX

                if TempLine:
                    $ JubesX.change_face("_angry")
                    $ JubesX.mouth = "_surprised"
                    $ JubesX.change_stat("love", 90, -10)
                    $ JubesX.change_stat("obedience", 80, 30)
                    $ JubesX.change_stat("inhibition", 70, -25)
                    ch_v ". . ."
                    $ JubesX.mouth = "_sad"
                    if TempLine in (EmmaX,StormX):
                        if JubesX.GirlLikeCheck(TempLine) >= 800:
                            $ JubesX.change_face("_sly",2,Eyes="_side")
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v "Well they are really ginormous. . ."
                            $ JubesX.GirlLikeUp(TempLine,20)
                        elif JubesX.GirlLikeCheck(TempLine) >= 700:
                            $ JubesX.eyes = "_side"
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v "Oh. Well I can't compete there. . ."
                        else:
                            $ JubesX.GirlLikeUp(TempLine,-50)
                            $ TempLine = "bad"

                    elif TempLine == KittyX:
                        if JubesX.LikeKitty >= 800:
                            $ JubesX.change_face("_sly",2,Eyes="_side")
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v ". . . I guess they are really cute. . ."
                            $ JubesX.LikeKitty += 20
                        elif JubesX.LikeKitty >= 700:
                            $ JubesX.eyes = "_side"
                            $ JubesX.change_stat("obedience", 80, 5)
                            ch_v "Ok, into that, uh? . ."
                        else:
                            $ JubesX.LikeKitty -= 50
                            $ TempLine = "bad"


                    if TempLine == "bad":
                        $ JubesX.change_stat("love", 90, -20)
                        ch_v "Still, you don't just -say- something like that!"
                        $ JubesX.change_outfit()
                        $ JubesX.recent_history.append("no_topless")
                        $ JubesX.daily_history.append("no_topless")
                        $ JubesX.recent_history.append("_angry")
                        $ JubesX.daily_history.append("_angry")
    else:


        $ JubesX.add_word(1,0, "", "", "topless")
        if approval_check(JubesX, 800) and not JubesX.Forced:
            $ JubesX.change_stat("inhibition", 70, 5)
            $ JubesX.change_stat("obedience", 70, 10)
        else:
            $ JubesX.change_stat("love", 90, -5)
            $ JubesX.change_stat("inhibition", 70, -5)
            $ JubesX.change_face("_angry")
            $ JubesX.change_stat("obedience", 70, 10)
    return


label Jubes_First_Bottomless(Silent=0):
    if JubesX.PantiesNum() > 1 or JubesX.PantsNum() > 2 or JubesX.HoseNum() > 9:

        return
    if JubesX.location != bg_current and "phonesex" not in Player.recent_history:
        return
    $ JubesX.recent_history.append("bottomless")
    $ JubesX.daily_history.append("bottomless")
    $ JubesX.drain_word("no_bottomless")
    $ JubesX.SeenPussy += 1
    if JubesX.SeenPussy > 1:
        return


    $ JubesX.change_stat("inhibition", 80, 30)
    $ JubesX.change_stat("obedience", 70, 10)
    if not Silent:
        $ JubesX.change_face("_sly")
        if JubesX.pubes:
            "You find yourself staring at [JubesX.name]'s furry pussy."
        else:
            "You find yourself staring at [JubesX.name]'s bare pussy."
        menu Jubes_First_BMenu:
            extend ""
            "Niiice. . .":
                $ JubesX.change_stat("love", 90, 20)
                $ JubesX.change_stat("inhibition", 60, 25)
                $ JubesX.change_face("_surprised",2)
                ch_v "!!"
                $ JubesX.change_face("_smile",1)
                ch_v "Oh, um, yeah, I. . . also. . . "
                $ JubesX.change_stat("love", 40, 20)
            "I see you keep it natural down there." if JubesX.pubes:
                $ JubesX.change_face("_confused",2)
                ch_v "Well. . . yeah."
                if approval_check(JubesX, 700, "LO"):
                    $ JubesX.change_face("_bemused",1)
                    menu:
                        ch_v "Did you. . . prefer it shaved?"
                        "Yes":
                            if approval_check(JubesX, 900, "LO"):
                                $ JubesX.change_stat("obedience", 50, 30)
                                $ JubesX.change_stat("inhibition", 60, 25)
                                ch_v "I guess I could. . ."
                                $ JubesX.Todo.append("pubes")
                            else:
                                $ JubesX.change_face("_normal")
                                ch_v "I dunno, seems like a lot of hassle."
                        "Up to you, I guess.":
                            $ JubesX.change_stat("love", 80, 10)
                            ch_v "Well, yeah, right? Of course."
                            if approval_check(JubesX, 900, "LO"):
                                $ JubesX.change_stat("inhibition", 60, 10)
                                $ JubesX.Todo.append("pubes")
                        "No, leave it that way.":
                            if approval_check(JubesX, 900, "LO"):
                                $ JubesX.change_face("_sly")
                                $ JubesX.change_stat("love", 80, 10)
                            else:
                                $ JubesX.change_face("_angry",Mouth="_normal")
                            $ JubesX.change_stat("inhibition", 60, 25)
                            ch_v "Oh, I guess that's your call?"
                            $ JubesX.brows = "_normal"
                else:
                    $ JubesX.change_face("_angry",1)
                    $ JubesX.change_stat("love", 40, -20)
                    $ JubesX.change_stat("obedience", 50, 25)
                    $ JubesX.change_stat("inhibition", 60, -5)
                    ch_v "Well, of course!"
            "What a mess.":
                $ JubesX.change_stat("love", 90, -30)
                $ JubesX.change_stat("obedience", 50, 25)
                $ JubesX.change_stat("inhibition", 70, -30)
                $ JubesX.change_face("_angry",2)
                if not JubesX.Forced and not approval_check(JubesX, 900, "LO"):
                    $ JubesX.recent_history.append("_angry")
                    $ JubesX.daily_history.append("_angry")
                    $ JubesX.change_stat("obedience", 70, 25)
                ch_v "Oh, them's fighting words. . ."
    else:
        $ JubesX.add_word(1,0, "", "", "bottomless")
        if approval_check(JubesX, 800) and not JubesX.Forced:
            $ JubesX.change_stat("inhibition", 60, 5)
            $ JubesX.change_stat("obedience", 70, 10)
        else:
            $ JubesX.change_stat("love", 90, -5)
            $ JubesX.change_stat("inhibition", 70, -5)
            $ JubesX.change_face("_angry")
            $ JubesX.change_stat("obedience", 70, 15)
    return





label Display_DressScreen(Girl=focused_Girl):


    if renpy.showing('DressScreen'):
        return 1

    if Girl == StormX:
        if not Girl.Taboo or StormX in Rules:
            return 1
        else:
            ch_s "I'm afraid rules are rules."

    if Girl.Taboo:
        return 0

    $ Girl.change_face("_bemused",1,Eyes="_side")
    if "screen" in Girl.daily_history:
        pass
    elif Girl == RogueX:
        ch_r "I'm not really comfortable like this."
    elif Girl == KittyX:
        ch_k "I'm getting kinda exposed here."
    elif Girl == EmmaX:
        ch_e "I'm feeling a bit exposed here. . ."
    elif Girl == LauraX:
        ch_l "I don't know about showing this much skin."
    elif Girl == JeanX:
        ch_j "I don't think you're ready for this. . ."
    elif Girl == JeanX:
        ch_j "I don't think you're ready for this. . ."
    elif Girl == JubesX:
        ch_v "I don't know, this is moving a little fast. . ."
    $ Girl.add_word(1,0, "screen")
    $ Girl.change_face("_bemused",1)
    Girl.voice "Mind if I get behind a dressing screen?"
    menu:
        extend ""
        "Go ahead":
            show DressScreen zorder 150
            if Girl == RogueX:
                ch_r "Thanks."
            elif Girl == KittyX:
                ch_k "Great."
            elif Girl == EmmaX:
                ch_e "Thank you."
            elif Girl == LauraX:
                ch_l "K."
            elif Girl == JeanX:
                ch_j "Good."
            elif Girl == JubesX:
                ch_v "Oh, thanks. . ."
            return 1
        "No, don't":
            if Girl == RogueX:
                ch_r "Fine then. . ."
            elif Girl == KittyX:
                ch_k "Ok then. . ."
            elif Girl == EmmaX:
                ch_e "Fair enough. . ."
            elif Girl == LauraX:
                ch_l "Ok. . ."
            elif Girl == JeanX:
                ch_j "Ok then."
            elif Girl == JubesX:
                ch_v "Well, fine. . ."

    return 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
