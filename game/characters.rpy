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

            self.thirst = 0
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
            self.broken_up = [0, 0]
            self.forced = 0
            self.location = "hold"
            self.home = 0

            self.outfit = "casual1"
            self.today_outfit = "casual1"
            self.SeenPeen = 0
            self.SeenChest = 0
            self.SeenPussy = 0
            self.SeenPanties = 0

            self.wearing_skirt = False
            self.upskirt = 0
            self.top_pulled_up = 0
            self.underwear_pulled_down = 0
            self.grool = 0
            self.wet = False
            self.spunk = []
            self.piercings = ""
            self.pubes = "_hairy"
            self.ArmPose = 1

            self.blushing = ""
            self.eyes = "_normal"
            self.mouth = "_normal"
            self.brows = "_normal"
            self.emotion = "_normal"

            self.held_item = None
            self.arms = ""
            self.legs = ""
            self.top = ""
            self.neck = ""
            self.bra = ""
            self.underwear = ""
            self.accessory = ""
            self.hair = 1
            self.hose = ""
            self.shame = 0
            self.inventory = []


            self.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            self.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            self.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            self.TempClothes = [0, "", "", "", "", "", "", "", "", "", 0]
            self.Gag = 0
            self.to_do = []
            self.pubes_counter = 0
            self.Schedule = [["MM", "MA", "ME", "MN"],
                                ["TM", "TA", "TE", "TN"],
                                ["WM", "WA", "WE", "WN"],
                                ["ThM", "ThA", "ThE", "ThN"],
                                ["FM", "FA", "FE", "FN"],
                                ["SaM", "SaA", "SaE", "SaN"],
                                ["SuM", "SuA", "SuE", "SuN"],
                                ]
            self.clothing = [0, "", "", "", "", "", "", "", "", 0]                    #schedules when she wears what: (0-6) = Mon-Sun, (7) Datewear, (8) Teachingwear, (9) Private

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

                self.Casual1 = [2,0, "_capris", "_pink_top", "_gold_necklace", "_cami", "_green_panties", "", "", "", 0]
                self.Casual2 = [2,0, "_black_jeans", "_red_shirt", "star_necklace", "_bra", "_green_panties", "", "", "", 0]
                self.Gym = [0, "", "_shorts", "", "", "_sports_bra", "_green_panties", "", "", "",10]
                self.sleepwear = [0, "", "_shorts", "", "", "_cami", "_green_panties", "", "", "",20]
                self.Swim = [0, "", "_blue_skirt", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume = [2,0, "_dress", "_jacket", "_flower_necklace", "_dress", "_lace_panties", "", "", "", 0]
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

                self.Casual1 = [2,0, "_pants", "_jacket", "_choker", "_corset", "_white_panties", "", "", "", 0]
                self.Casual2 = [2,"_gloves", "_pants", "", "_choker", "_corset", "_white_panties", "", "", "",5]
                self.Gym = [0, "", "", "", "", "_sports_bra", "sports_panties", "", "", "",10]
                self.sleepwear = [0, "", "", "", "", "_corset", "_white_panties", "", "", "",25]
                self.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume =  [2,"_gloves", "_dress", "_dress", "_choker", "", "_lace_panties", "", "_hat", "_stockings_and_garterbelt", 0]
                self.home = "bg_emma"
                self.hair = "_wavy"
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
                self.Casual2 = [2,0, "_skirt", "_jacket", "leash_choker", "leather_bra", "_black_panties", "", "", "", 0]
                self.Gym = [2,"wrists", "leather_pants", "", "", "leather_bra", "_black_panties", "", "", "", 0]
                self.sleepwear = [0, "", "", "", "", "leather_bra", "leather_panties", "", "", "",20]
                self.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume = [2,"_gloves", "other_skirt", "", "", "white_tank", "_black_panties", "suspenders", "", "black stockings", 0]
                self.home = "bg_laura"
                self.hair = "_long"
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
                self.hair = "_short"

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

                self.Casual1 = [2,0, "_skirt", "white_shirt", "", "black_bra", "_white_panties", "", "", "", 0]
                self.Casual2 = [2,0, "_pants", "_jacket", "", "_sports_bra", "_white_panties", "", "", "", 0]
                self.Gym = [0, "", "yoga_pants", "", "", "_sports_bra", "_white_panties", "", "", "",10]
                self.sleepwear = [0, "", "", "white_shirt", "", "", "_white_panties", "", "", "",25]
                self.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume = [2,0, "", "", "ring_necklace", "cos_bra", "cos_panties", "rings", "_short", "", 0]
                self.home = "bg_storm"
                self.hair = "_long"

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

                self.Casual1 = [2,0, "_shorts", "_red_shirt", "", "_sports_bra", "blue_panties", "_jacket", "", "", 0]
                self.Casual2 = [2,0, "_pants", "black_shirt", "", "_sports_bra", "blue_panties", "_jacket", "", "", 0]
                self.Gym = [0, "", "_pants", "", "", "_sports_bra", "blue_panties", "", "", "",10]
                self.sleepwear = [0, "", "", "", "", "_sports_bra", "blue_panties", "", "", "",25]
                self.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.Costume = [0, "", "_pants", "black_shirt", "", "_sports_bra", "blue_panties", "_jacket", "", "", 0]
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
            personal_rooms.append(self.home)

        def SluttyClothes(self):


            if self == RogueX:
                if "_stockings_and_garterbelt" in self.inventory:
                    self.Casual1[9] = "_stockings_and_garterbelt"
                elif self.inhibition >= 300:
                    self.Casual1[9] = "_stockings"
                else:
                    self.Casual1[9] = "_tights"

                if self.Gym[0] == 0 and self.Gym[5] and self.inhibition >= 300:

                    self.Gym[3] == 0

                if self.Swim[0] == 0 and self.Swim[5] and self.inhibition >= 300:

                    self.Swim[3] == 0
            elif self == KittyX:
                if self.Swim[2] == "_blue_skirt" and self.Swim[6] and self.inhibition > 500:

                    self.Swim[2] = 0
            elif self == LauraX:
                if self.inhibition >= 400 and self.Casual2[5] == "leather_bra" and "_corset" in self.inventory:
                    self.Casual2[5] = "_corset"
                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.Casual2[6] = "_lace_panties"
                if self.inhibition >= 600 and "_stockings_and_garterbelt" in self.inventory:
                    self.Casual2[9] = "_stockings_and_garterbelt"

            elif self == JeanX:
                if "_stockings_and_garterbelt" in self.inventory:
                    self.Casual1[9] = "_stockings_and_garterbelt"
                elif self.love >= 300:
                    self.Casual1[9] = "_stockings"
                if self.inhibition >= 600 and "_bikini_top" in self.inventory:
                    self.Gym[5] = "_bikini_top" if self.Gym[0] == 1 else self.Gym[5]
                if self.inhibition >= 600 and "lace_bra" in self.inventory:
                    self.Casual1[5] = "lace_bra"
                    self.Casual2[5] = "lace_bra"
                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.Casual1[6] = "_lace_panties"
                    self.Casual2[6] = "_lace_panties"
            elif self == StormX:
                if self.inhibition >= 400 and self.Casual2[5] == "_sports_bra":
                    self.Casual2[5] = "_tube_top"
                if self.inhibition >= 400 and self.Casual2[5] == "_white_panties":
                    self.Casual2[5] = "_black_panties"
                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.Casual2[6] = "_lace_panties"
            elif self == JubesX:
                if self.inhibition >= 500 and self.Casual1[3] == "_red_shirt":
                    self.Casual1[3] = "_tube_top"
                    self.Casual1[5] = 0
                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.Casual2[6] = "_lace_panties"
                if self.inhibition >= 600 and "_stockings_and_garterbelt" in self.inventory:
                    self.Casual2[9] = "_stockings_and_garterbelt"
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

            if (self.forced or "_angry" in self.recent_history) and emotion in ("_normal", "_bemused", "_sexy", "_sly", "_smile", "startled"):
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


        def default_faces(self):



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
            if self.thirst >= 80:
                self.lust += 2
            elif self.thirst >= 50:
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



        def change_outfit(self, outfitTemp = 5, Spunk = 0, Undressed = 0, Changed = 1,Holderoutfit=[]):



            if self not in all_Girls:
                return

            outfitTemp = outfitTemp if outfitTemp else self.outfit

            if self.location == bg_current and renpy.showing("NightMask", layer='nightmask') and time_index == 0:

                return

            if self.location not in ("bg_showerroom", "bg_pool") or (outfitTemp not in ("nude", "swimwear", "_towel")):

                self.wet = False
            if self.spunk:

                if "painted" not in self.daily_history or "cleaned" not in self.daily_history:
                    del self.spunk[:]


            if self.upskirt or self.top_pulled_up or self.underwear_pulled_down:
                Undressed = 1

            self.upskirt = 0
            self.top_pulled_up = 0
            self.underwear_pulled_down = 0

            if outfitTemp == 5:

                if "yoinked" in self.recent_history:

                    return
                outfitTemp = self.outfit
            elif outfitTemp == 6:

                outfitTemp = self.today_outfit
                self.outfit = self.today_outfit
            if outfitTemp != self.outfit:


                Changed = 1
                self.outfit = outfitTemp
            if self in Party and outfitTemp == self.today_outfit:

                outfitTemp = self.outfit

            if outfitTemp == "casual1":
                Holderoutfit = self.Casual1[:]
            elif outfitTemp == "casual2":
                Holderoutfit = self.Casual2[:]
            elif outfitTemp == "nude":
                Holderoutfit = [0, "", "", "", "", "", "", "", "", "",50]
            elif outfitTemp == "_towel":
                Holderoutfit = [0, "", "", "_towel", "", "", "", "", "", "",35]
            elif outfitTemp == "custom1":
                Holderoutfit = self.Custom1[:]
            elif outfitTemp == "custom2":
                Holderoutfit = self.Custom2[:]
            elif outfitTemp == "custom3":
                Holderoutfit = self.Custom3[:]
            elif outfitTemp == "temporary":
                Holderoutfit = self.TempClothes[:]
            elif outfitTemp == "sleep":
                Holderoutfit = self.sleepwear[:]
            elif outfitTemp == "gym":
                Holderoutfit = self.Gym[:]
            elif outfitTemp == "costume":
                Holderoutfit = self.Costume[:]
            elif outfitTemp == "swimwear":
                if not self.Swim[0]:
                    if "_bikini_top" not in self.inventory or "_bikini_bottoms" not in self.inventory:
                        self.outfit = self.today_outfit

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
                    elif self == KittyX and "_blue_skirt" not in self.inventory and self.inhibition <= 400:
                        self.outfit = self.today_outfit
                        if "swim" not in self.daily_history:
                            ch_k("I don't know, I do have a suit, but it's a little daring. . .", interact=True)
                            ch_k("If only I had a little skirt or something. . .", interact=True)
                        return 0
                    else:
                        self.Swim[0] = 1
                Holderoutfit = self.Swim[:]

            while len(Holderoutfit) < 11:
                Holderoutfit.append(0)

            if not self.legs and Holderoutfit[2]:
                Undressed = 1
            elif not self.top and Holderoutfit[3]:
                Undressed = 1
            elif not self.bra and Holderoutfit[5]:
                Undressed = 1
            elif not self.underwear and Holderoutfit[6] and "pantyless" not in self.daily_history:
                Undressed = 1
            elif not self.hose and Holderoutfit[9]:
                Undressed = 1



            if self == EmmaX and (Holderoutfit[8] != "_hat" and Holderoutfit[8] != "_wet_hat"):

                self.hair = "_wet" if Holderoutfit[8] == "_wet_hat" else "_wave"

            self.arms = Holderoutfit[1]
            self.legs = Holderoutfit[2]
            self.top = Holderoutfit[3]
            self.neck = Holderoutfit[4]
            self.bra = Holderoutfit[5]
            self.underwear = Holderoutfit[6]
            self.accessory = Holderoutfit[7]
            self.hair = Holderoutfit[8] if Holderoutfit[8] else self.hair
            self.hose = Holderoutfit[9]
            self.shame = Holderoutfit[10]

            if "ripped" in self.daily_history and "modesty" not in self.recent_history:

                self.hose = "ripped_pantyhose" if self.hose == "pantyhose" else self.hose
                self.hose = "ripped_tights" if self.hose == "_tights" else self.hose
            if self.underwear and self.underwear != "_shorts" and "pantyless" in self.daily_history and "modesty" not in self.daily_history:

                if outfitTemp != "sleep" and outfitTemp != "gym":
                    self.underwear = ""



            if not Changed and outfitTemp == self.outfit and self.location == bg_current:

                if Undressed == 2:
                    renpy.say(None,self.name+" throws on a towel.", interact=True)
                elif Undressed:
                    renpy.say(None,self.name+" throws her clothes back on.", interact=True)
            if Undressed:
                return 2
            return 1




        def Set_Temp_outfit(self):


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



            self.outfit = "temporary"
            self.today_outfit = "temporary"
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
            if self.bra == "_corset":
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
                if self.accessory == "_jacket":
                    return 3
                if self.accessory == "open_jacket":
                    return 1
                if self.accessory == "shut_jacket":
                    return 5
            if self.top == "_towel":
                return 3
            if self.top == "_dress":
                return 4
            if self.top == "_jacket":
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
            if self.legs in ("_skirt", "_blue_skirt", "other_skirt", "_dress"):
                return 5
            if self.legs == "yoga_pants":
                return 8
            if self.top == "_towel" and self not in (EmmaX,StormX):
                return 5
            if self == EmmaX and self.top == "_dress":
                return 4
            if self.legs == "mesh_pants":
                return 2
            if self.legs:
                return 10


            return 0

        def PantiesNum(self,Up=1):

            if Up and self.underwear_pulled_down and self.underwear:
                return 1
            if self.underwear == "_lace_panties":
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









label Clothing_Schedule_Check(Girl=0, Changed=0, Value=0, Count=0):








    while Count < 9:
        if Girl.clothing[Count] == Changed:
            if Value:

                if Girl.clothing[Count] == 3 and Girl.Custom1[0] == 2:
                    pass
                elif Girl.clothing[Count] == 5 and Girl.Custom2[0] == 2:
                    pass
                elif Girl.clothing[Count] == 6 and Girl.Custom3[0] == 2:
                    pass
                elif Girl.clothing[Count] == 4 and Girl.Gym[0] != 1:
                    pass
                else:
                    $ Girl.clothing[Count] = 0
            else:
                $ Girl.clothing[Count] = 0
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
            $ RogueX.clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ RogueX.outfit = "casual1"
            $ RogueX.today_outfit = "casual1"

            $ KittyX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ KittyX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ KittyX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ KittyX.Casual1 = [2,0, "_capris", "_pink_top", "_gold_necklace", "_cami", "_green_panties", "", "", "", 0]
            $ KittyX.Casual2 = [2,0, "_black_jeans", "_red_shirt", "", "_bra", "_green_panties", "", "", "", 0]
            $ KittyX.Gym = [0, "", "_shorts", "", "", "_sports_bra", "_green_panties", "", "", "", 0]
            $ KittyX.sleepwear = [0, "", "_shorts", "", "", "_cami", "_green_panties", "", "", "", 0]
            $ KittyX.Swim = [0, "", "_blue_skirt", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ KittyX.Costume = [2,0, "_dress", "_jacket", "_flower_necklace", "_dress", "_lace_panties", "", "", "", 0]
            $ KittyX.clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ KittyX.outfit = "casual1"
            $ KittyX.today_outfit = "casual1"

            $ EmmaX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ EmmaX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ EmmaX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ EmmaX.Casual1 = [2,0, "_pants", "_jacket", "_choker", "_corset", "_white_panties", "", "", "", 0]
            $ EmmaX.Casual2 = [2,"_gloves", "_pants", "", "_choker", "_corset", "_white_panties", "", "", "", 0]
            $ EmmaX.Gym = [0, "", "", "", "", "_sports_bra", "sports_panties", "", "", "", 0]
            $ EmmaX.sleepwear = [0, "", "", "", "", "_corset", "_white_panties", "", "", "", 0]
            $ EmmaX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ EmmaX.Costume =  [2,"_gloves", "_dress", "_dress", "_choker", "", "_lace_panties", "", "_hat", "_stockings_and_garterbelt", 0]
            $ EmmaX.clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ EmmaX.outfit = "casual1"
            $ EmmaX.today_outfit = "casual1"

            $ LauraX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ LauraX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ LauraX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ LauraX.Casual1 = [2,"wrists", "leather_pants", "", "leash_choker", "leather_bra", "_black_panties", "", "", "", 0]
            $ LauraX.Casual2 = [2,0, "_skirt", "_jacket", "leash_choker", "leather_bra", "_black_panties", "", "", "", 0]
            $ LauraX.Gym = [0, "wrists", "leather_pants", "", "", "leather_bra", "_black_panties", "", "", "", 0]
            $ LauraX.sleepwear = [0, "", "", "", "", "leather_bra", "leather_panties", "", "", "", 0]
            $ LauraX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ LauraX.Costume = [2,"_gloves", "other_skirt", "", "", "white_tank", "_black_panties", "suspenders", "", "black stockings", 0]
            $ LauraX.clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ LauraX.outfit = "casual1"
            $ LauraX.today_outfit = "casual1"

            $ JeanX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JeanX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JeanX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JeanX.Casual1 = [2,0, "_pants", "pink_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
            $ JeanX.Casual2 = [2,0, "_skirt", "green_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
            $ JeanX.Gym = [0, "", "yoga_pants", "", "", "_sports_bra", "_green_panties", "", "", "", 0]
            $ JeanX.sleepwear = [0, "", "", "pink_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
            $ JeanX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ JeanX.Costume =  [2,0, "_shorts", "yellow_shirt", "", "green_bra", "_green_panties", "suspenders", "pony", "", 0]
            $ JeanX.clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ JeanX.outfit = "casual1"
            $ JeanX.today_outfit = "casual1"

            $ StormX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ StormX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ StormX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ StormX.Casual1 = [2,0, "_skirt", "white_shirt", "", "black_bra", "_white_panties", "", "", "", 0]
            $ StormX.Casual2 = [2,0, "_pants", "_jacket", "", "_tube_top", "_white_panties", "", "", "", 0]
            $ StormX.Gym = [0, "", "yoga_pants", "", "", "_sports_bra", "_white_panties", "", "", "",10]
            $ StormX.sleepwear = [0, "", "", "white_shirt", "", "", "_white_panties", "", "", "",25]
            $ StormX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ StormX.Costume = [2,0, "", "", "ring_necklace", "cos_bra", "cos_panties", "rings", "_short", "", 0]
            $ StormX.clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ StormX.outfit = "casual1"
            $ StormX.today_outfit = "casual1"

            $ JubesX.Custom1 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JubesX.Custom2 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JubesX.Custom3 = [0, "", "", "", "", "", "", "", "", "", 0]
            $ JubesX.Casual1 = [2,0, "_shorts", "_red_shirt", "", "_sports_bra", "blue_panties", "_jacket", "", "", 0]
            $ JubesX.Casual2 = [2,0, "_pants", "black_shirt", "", "_sports_bra", "blue_panties", "_jacket", "", "", 0]
            $ JubesX.Gym = [0, "", "_pants", "", "", "_sports_bra", "blue_panties", "", "", "",10]
            $ JubesX.sleepwear = [0, "", "", "", "", "_sports_bra", "blue_panties", "", "", "",25]
            $ JubesX.Swim = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
            $ JubesX.Costume = [0, "", "_pants", "black_shirt", "", "_sports_bra", "blue_panties", "_jacket", "", "", 0]
            $ JubesX.clothing = [0, "", "", "", "", "", "", "", "", 0]
            $ JubesX.outfit = "casual1"
            $ JubesX.today_outfit = "casual1"

            "Done."
            "You will now need to set their custom outfits again."
        "No":
            pass
    return




label GirlsAngry(Girls=0, temp_Girls=[]):

    $ approval_bonus = 0
    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        if temp_Girls[0].location == bg_current and "_angry" in temp_Girls[0].recent_history:
            if bg_current == temp_Girls[0].home:
                if temp_Girls[0] == RogueX:
                    ch_r "You should get out, I'm fix'in ta throw down."
                elif temp_Girls[0] == KittyX:
                    ch_k "You should get out of here, I can't even look at you right now."
                elif temp_Girls[0] == EmmaX:
                    ch_e "You should leave, or do you want to test me?"
                elif temp_Girls[0] == LauraX:
                    ch_l "You should leave."
                elif temp_Girls[0] == JeanX:
                    ch_j "Out, NOW!"
                elif temp_Girls[0] == StormX:
                    ch_s "Out!"
                elif temp_Girls[0] == JubesX:
                    ch_v "Get out!"
                "You head back to your room."
                $ Party = []
                $ renpy.pop_call()
                jump player_room_entry
            else:
                $ temp_Girls[0].location = temp_Girls[0].home
            if temp_Girls[0] in Party:
                $ Party.remove(temp_Girls[0])
            if Girls:
                ". . . and so does [temp_Girls[0].name]."
            else:
                "[temp_Girls[0].name] storms off."
                if temp_Girls[0] == StormX:
                    ". . . so to speak."
            $ Girls += 1
            if temp_Girls[0] == RogueX:
                hide Rogue_sprite with easeoutleft
            elif temp_Girls[0] == KittyX:
                hide Kitty_sprite with easeoutleft
            elif temp_Girls[0] == EmmaX:
                hide Emma_Sprite with easeoutleft
            elif temp_Girls[0] == LauraX:
                hide Laura_Sprite with easeoutleft
            elif temp_Girls[0] == JeanX:
                hide Jean_Sprite with easeoutleft
            elif temp_Girls[0] == StormX:
                hide Storm_Sprite with easeoutleft
            elif temp_Girls[0] == JubesX:
                hide Jubes_Sprite with easeoutleft
        $ temp_Girls.remove(temp_Girls[0])
    return



label Lastnamer(wordcount=0, Splitname=0, Lastname=0):

    $ wordcount = Player.name.count(" ")


    $ Splitname = Player.name.split()


    $ Lastname = "Mr. " + Splitname[wordcount]
    return Lastname




label DrainAll(word=0, Recent=1, Daily=1, Traits=0):


    $ temp_Girls = all_Girls[:]
    while temp_Girls:
        $ temp_Girls[0].drain_word(word,Recent,Daily,Traits)
        $ temp_Girls.remove(temp_Girls[0])
    return
