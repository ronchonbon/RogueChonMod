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
                call_holder(update, "#FFFFFF", x_position)

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
            self.taboo = 0
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

            self.went_on_date = 0
            self.had_chat = [0, 0, 0, 0, 0, 0]
            self.event_happened = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            self.cheated_on = 0
            self.broken_up = [0, 0]
            self.forced = 0

            self.location = "hold"

            self.outfit = "casual1"
            self.today_outfit = "casual1"

            self.seen_peen = False
            self.seen_breasts = False
            self.seen_pussy = False
            self.seen_underwear = False

            self.wearing_skirt = False
            self.upskirt = False
            self.top_pulled_up = False
            self.underwear_pulled_down = False
            self.grool = 0
            self.wet = False
            self.spunk = []
            self.piercings = ""
            self.arm_pose = 1

            self.blushing = ""
            self.eyes = "_normal"
            self.mouth = "_normal"
            self.brows = "_normal"
            self.emotion = "_normal"
            self.arms = ""

            self.legs = ""
            self.top = ""
            self.neck = ""
            self.bra = ""
            self.underwear = ""
            self.accessory = ""
            self.hose = ""

            self.shame = 0

            self.held_item = None
            self.inventory = []

            self.first_custom_outfit = [0, "", "", "", "", "", "", "", "", "", 0]
            self.second_custom_outfit = [0, "", "", "", "", "", "", "", "", "", 0]
            self.third_custom_outfit = [0, "", "", "", "", "", "", "", "", "", 0]
            self.temp_outfit = [0, "", "", "", "", "", "", "", "", "", 0]

            self.gag = False
            self.buttplug = False

            self.to_do = []
            self.pubes_counter = 0

            self.clothing = [0, "", "", "", "", "", "", "", "", 0]

            self.action_counter = {}

            for action in all_actions:
                self.action_counter[action] = 0

            self.event_counter = {"orgasmed": 0, "caught": 0, "sleepover": 0, "ass_slapped": 0,
                "swallowed": 0, "creampied": 0, "anal_creampied": 0,
                "been_with_girl": 0, "seen_with_girl": 0,
                "forced": 0}

            self.session_orgasms = 0
            self.SEXP = 0

            self.player_favorite_action = 0
            self.favorite_action = 0

            self.stored_stats = 0

            if self.tag == "Rogue":
                self.voice = ch_r

                self.first_casual_outfit = [2,"_gloves", "_skirt", "_mesh_top", "_spiked_collar", "_tank", "_black_panties", "", "", "_tights", 0]
                self.second_casual_outfit = [2,"_gloves", "_pants", "_pink_top", "", "_buttoned_tank", "_black_panties", "", "", "", 0]
                self.gym_clothes = [0, "_gloves", "", "_hoodie", "", "_sports_bra", "_shorts", "", "", "",10]
                self.sleepwear = [0, "", "", "", "", "_tank", "_green_panties", "", "", "",20]
                self.swimwear = [0, "", "", "_hoodie", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.halloween_costume = [2,"_gloves", "_skirt", "", "", "_tube_top", "_black_panties", "_sweater", "_cosplay", "", 0]

                self.home = "bg_rogue"
                self.hair = "_evo"
                self.pubes = "_hairy"

                self.weekly_schedule = [["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                 ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                                 ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                 ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                                 ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                 ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"],
                                 ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"]]

                self.likes = {"Rogue": None, "Kitty": 600, "Emma": 500, "Laura": 500, "Jean": 200, "Storm": 600, "Jubes": 500}

                self.history = ["met"]

                self.used_to_anal = 0

                self.massage_chart = ["shoulders", "arms", "arms", "hands", "hands", "back", "hips", "back", "breasts", "breasts"]

                self.player_petname = "Sugar"
                self.player_petnames = ["Sugar", Player.name]
                self.petname = "Rogue"
                self.petnames = ["Rogue"]
            elif self.tag == "Kitty":
                self.voice = ch_k

                self.first_casual_outfit = [2,0, "_capris", "_pink_top", "_gold_necklace", "_cami", "_green_panties", "", "", "", 0]
                self.second_casual_outfit = [2,0, "_black_jeans", "_red_shirt", "_star_necklace", "_bra", "_green_panties", "", "", "", 0]
                self.gym_clothes = [0, "", "_shorts", "", "", "_sports_bra", "_green_panties", "", "", "",10]
                self.sleepwear = [0, "", "_shorts", "", "", "_cami", "_green_panties", "", "", "",20]
                self.swimwear = [0, "", "_blue_skirt", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.halloween_costume = [2,0, "_dress", "_jacket", "_flower_necklace", "_dress", "_lace_panties", "", "", "", 0]

                self.home = "bg_kitty"
                self.hair = "_evo"
                self.pubes = "_hairy"

                self.like = ", like, "
                self.Like = "Like, "

                self.weekly_schedule = [["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                 ["bg_classroom", "bg_pool", "bg_kitty", "bg_kitty"],
                                 ["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                 ["bg_classroom", "bg_pool", "bg_kitty", "bg_kitty"],
                                 ["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                 ["bg_campus", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                 ["bg_campus", "bg_dangerroom", "bg_kitty", "bg_kitty"]]

                self.likes = {"Rogue": 600, "Kitty": None, "Emma": 500, "Laura": 500, "Jean": 300, "Storm": 600, "Jubes": 600}

                self.used_to_anal = 0

                self.massage_chart = ["shoulders", "back", "hips", "thighs", "calves", "feet", "feet", "hips", "ass", "pussy"]

                self.player_petname = Player.name[:1]
                self.player_petnames = ["sweetie", Player.name[:1], Player.name]
                self.petname = "Kitty"
                self.petnames = ["Kitty"]
            elif self.tag == "Emma":
                self.voice = ch_e

                self.first_casual_outfit = [2,0, "_pants", "_jacket", "_choker", "_corset", "_white_panties", "", "", "", 0]
                self.second_casual_outfit = [2,"_gloves", "_pants", "", "_choker", "_corset", "_white_panties", "", "", "",5]
                self.gym_clothes = [0, "", "", "", "", "_sports_bra", "sports_panties", "", "", "",10]
                self.sleepwear = [0, "", "", "", "", "_corset", "_white_panties", "", "", "",25]
                self.swimwear = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.halloween_costume =  [2,"_gloves", "_dress", "_dress", "_choker", "", "_lace_panties", "", "_hat", "_stockings_and_garterbelt", 0]

                self.home = "bg_emma"
                self.hair = "_wavy"
                self.pubes = "_bare"

                self.weekly_schedule = [["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
                                 ["bg_teacher", "bg_teacher", "bg_dangerroom", "bg_emma"],
                                 ["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
                                 ["bg_teacher", "bg_teacher", "bg_dangerroom", "bg_emma"],
                                 ["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
                                 ["bg_pool", "bg_pool", "bg_emma", "bg_emma"],
                                 ["bg_pool", "bg_pool", "bg_emma", "bg_emma"]]

                self.likes = {"Rogue": 500, "Kitty": 500, "Emma": None, "Laura": 500, "Jean": 100, "Storm": 500, "Jubes": 500}

                self.used_to_anal = 2

                self.massage_chart = ["shoulders", "neck", "neck", "back", "hips", "ass", "ass", "back", "breasts", "breasts"]

                self.names = ["Ms. Frost"]
                self.name = "Ms. Frost"
                self.player_petname = "young man"
                self.player_petnames = ["young man", Player.name]
                self.petname = self.name
                self.petnames = ["Emma", "Ms. Frost"]
            elif self.tag == "Laura":
                self.voice = ch_l

                self.first_casual_outfit = [2,"wrists", "leather_pants", "", "leash_choker", "leather_bra", "_black_panties", "", "", "", 0]
                self.second_casual_outfit = [2,0, "_skirt", "_jacket", "leash_choker", "leather_bra", "_black_panties", "", "", "", 0]
                self.gym_clothes = [2,"wrists", "leather_pants", "", "", "leather_bra", "_black_panties", "", "", "", 0]
                self.sleepwear = [0, "", "", "", "", "leather_bra", "leather_panties", "", "", "",20]
                self.swimwear = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.halloween_costume = [2,"_gloves", "other_skirt", "", "", "white_tank", "_black_panties", "suspenders", "", "black stockings", 0]

                self.home = "bg_laura"
                self.hair = "_long"
                self.pubes = "_hairy"

                self.scent_timer = 0
                self.claws = 0
                self.weekly_schedule = [["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                        ["bg_dangerroom", "bg_classroom", "bg_campus", "bg_laura"],
                                        ["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                        ["bg_dangerroom", "bg_classroom", "bg_campus", "bg_laura"],
                                        ["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                        ["bg_pool", "bg_laura", "bg_dangerroom", "bg_laura"],
                                        ["bg_pool", "bg_laura", "bg_dangerroom", "bg_laura"]]

                self.likes = {"Rogue": 500, "Kitty": 500, "Emma": 500, "Laura": None, "Jean": 300, "Storm": 500, "Jubes": 600}

                self.used_to_anal = 2

                self.massage_chart = ["shoulders", "back", "arms", "hips", "thighs", "calves", "ass", "ass", "pussy", "pussy"]

                self.player_petname = "guy"
                self.player_petnames = ["guy", Player.name]
                self.petname = "Laura"
                self.petnames = ["Laura", "X-23"]
            elif self.tag == "Jean":
                self.voice = ch_j

                self.IX = 500

                self.first_casual_outfit = [2,0, "_pants", "pink_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
                self.second_casual_outfit = [2,0, "_skirt", "green_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
                self.gym_clothes = [0, "", "yoga_pants", "", "", "_sports_bra", "_green_panties", "", "", "", 0]
                self.sleepwear = [0, "", "", "pink_shirt", "", "green_bra", "_green_panties", "", "", "", 0]
                self.swimwear = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.halloween_costume =  [2,0, "_shorts", "yellow_shirt", "", "green_bra", "_green_panties", "suspenders", "pony", "", 0]

                self.home = "bg_jean"
                self.hair = "_short"
                self.pubes = "_hairy"

                self.weekly_schedule = [["bg_classroom", "bg_classroom", "bg_dangerroom", "bg_jean"],
                                        ["bg_jean", "bg_classroom", "bg_jean", "bg_jean"],
                                        ["bg_jean", "bg_classroom", "bg_dangerroom", "bg_jean"],
                                        ["bg_classroom", "bg_classroom", "bg_jean", "bg_jean"],
                                        ["bg_jean", "bg_classroom", "bg_dangerroom", "bg_jean"],
                                        ["bg_dangerroom", "bg_campus", "bg_pool", "bg_jean"],
                                        ["bg_dangerroom", "bg_campus", "bg_pool", "bg_jean"]]

                self.likes = {"Rogue": 500, "Kitty": 500, "Emma": 300, "Laura": 500, "Jean": None, "Storm": 300, "Jubes": 300}

                self.used_to_anal = 0

                self.massage_chart = ["back", "shoulders", "neck", "neck", "back", "hips", "ass", "ass", "pussy", "pussy"]

                self.player_petname = "um. . ."
                self.player_petnames = ["um. . ."]
                self.petname = self.name
                self.petnames = ["Jean"]
            elif self.tag == "Storm":
                self.voice = ch_s

                self.first_casual_outfit = [2,0, "_skirt", "white_shirt", "", "black_bra", "_white_panties", "", "", "", 0]
                self.second_casual_outfit = [2,0, "_pants", "_jacket", "", "_sports_bra", "_white_panties", "", "", "", 0]
                self.gym_clothes = [0, "", "yoga_pants", "", "", "_sports_bra", "_white_panties", "", "", "",10]
                self.sleepwear = [0, "", "", "white_shirt", "", "", "_white_panties", "", "", "",25]
                self.swimwear = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.halloween_costume = [2,0, "", "", "ring_necklace", "cos_bra", "cos_panties", "rings", "_short", "", 0]

                self.home = "bg_storm"
                self.hair = "_long"
                self.pubes = "_hairy"

                self.weekly_schedule = [["bg_storm", "bg_dangerroom", "bg_dangerroom", "bg_storm"],
                                        ["bg_teacher", "bg_teacher", "bg_classroom", "bg_storm"],
                                        ["bg_storm", "bg_dangerroom", "bg_dangerroom", "bg_storm"],
                                        ["bg_teacher", "bg_teacher", "bg_classroom", "bg_storm"],
                                        ["bg_pool", "bg_campus", "bg_classroom", "bg_storm"],
                                        ["bg_storm", "bg_campus", "bg_storm", "bg_pool"],
                                        ["bg_storm", "bg_campus", "bg_storm", "bg_pool"]]

                self.likes = {"Rogue": 500, "Kitty": 600, "Emma": 400, "Laura": 500, "Jean": 300, "Storm": None, "Jubes": 500}

                self.used_to_anal = 0

                self.massage_chart = ["feet", "calves", "thighs", "hips", "ass", "ass", "pussy", "ass", "pussy", "pussy"]

                self.player_petname = Player.name
                self.player_petnames = [Player.name]
                self.petname = self.name
                self.petnames = ["Storm", "Ororo", "Ms. Munroe"]
            elif self.tag == "Jubes":
                self.voice = ch_v

                self.first_casual_outfit = [2,0, "_shorts", "_red_shirt", "", "_sports_bra", "_blue_panties", "_jacket", "", "", 0]
                self.second_casual_outfit = [2,0, "_pants", "_black_shirt", "", "_sports_bra", "_blue_panties", "_jacket", "", "", 0]
                self.gym_clothes = [0, "", "_pants", "", "", "_sports_bra", "_blue_panties", "", "", "",10]
                self.sleepwear = [0, "", "", "", "", "_sports_bra", "_blue_panties", "", "", "",25]
                self.swimwear = [0, "", "", "", "", "_bikini_top", "_bikini_bottoms", "", "", "", 0]
                self.halloween_costume = [0, "", "_pants", "_black_shirt", "", "_sports_bra", "_blue_panties", "_jacket", "", "", 0]

                self.home = "bg_jubes"
                self.hair = "_shades"
                self.pubes = "_hairy"

                self.weekly_schedule = [["bg_jubes", "bg_dangerroom", "bg_dangerroom", "bg_jubes"],
                                        ["bg_classroom", "bg_classroom", "bg_jubes", "bg_jubes"],
                                        ["bg_jubes", "bg_dangerroom", "bg_dangerroom", "bg_jubes"],
                                        ["bg_dangerroom", "bg_dangerroom", "bg_jubes", "bg_jubes"],
                                        ["bg_pool", "bg_campus", "bg_campus", "bg_jubes"],
                                        ["bg_jubes", "bg_campus", "bg_jubes", "bg_pool"],
                                        ["bg_jubes", "bg_campus", "bg_jubes", "bg_pool"]]

                self.likes = {"Rogue": 500, "Kitty": 600, "Emma": 500, "Laura": 600, "Jean": 300, "Storm": 500, "Jubes": None}

                self.used_to_anal = 0

                self.massage_chart = ["neck", "shoulders", "calves", "feet", "neck", "shoulders", "calves", "feet", "pussy", "pussy"]

                self.player_petname = "Bro"
                self.player_petnames = ["Bro", Player.name]
                self.petname = self.name
                self.petnames = ["Jubes", "Jubilee"]

            self.change_outfit(6)

            shop_inventory.extend(["DL", "G", "A"])
            personal_rooms.append(self.home)

            global all_Girls

            all_Girls.append(self)

        def slutty_clothes(self):
            if self.tag == "Rogue":
                if "_stockings_and_garterbelt" in self.inventory:
                    self.first_casual_outfit[9] = "_stockings_and_garterbelt"
                elif self.inhibition >= 300:
                    self.first_casual_outfit[9] = "_stockings"
                else:
                    self.first_casual_outfit[9] = "_tights"

                if self.gym_clothes[0] == 0 and self.gym_clothes[5] and self.inhibition >= 300:
                    self.gym_clothes[3] == 0

                if self.swimwear[0] == 0 and self.swimwear[5] and self.inhibition >= 300:
                    self.swimwear[3] == 0
            elif self.tag == "Kitty":
                if self.swimwear[2] == "_blue_skirt" and self.swimwear[6] and self.inhibition > 500:
                    self.swimwear[2] = 0
            elif self.tag == "Laura":
                if self.inhibition >= 400 and self.second_casual_outfit[5] == "leather_bra" and "_corset" in self.inventory:
                    self.second_casual_outfit[5] = "_corset"
                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.second_casual_outfit[6] = "_lace_panties"
                if self.inhibition >= 600 and "_stockings_and_garterbelt" in self.inventory:
                    self.second_casual_outfit[9] = "_stockings_and_garterbelt"
            elif self.tag == "Jean":
                if "_stockings_and_garterbelt" in self.inventory:
                    self.first_casual_outfit[9] = "_stockings_and_garterbelt"
                elif self.love >= 300:
                    self.first_casual_outfit[9] = "_stockings"

                if self.inhibition >= 600 and "_bikini_top" in self.inventory:
                    self.gym_clothes[5] = "_bikini_top" if self.gym_clothes[0] == 1 else self.gym_clothes[5]

                if self.inhibition >= 600 and "lace_bra" in self.inventory:
                    self.first_casual_outfit[5] = "lace_bra"
                    self.second_casual_outfit[5] = "lace_bra"

                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.first_casual_outfit[6] = "_lace_panties"
                    self.second_casual_outfit[6] = "_lace_panties"
            elif self.tag == "Storm":
                if self.inhibition >= 400 and self.second_casual_outfit[5] == "_sports_bra":
                    self.second_casual_outfit[5] = "_tube_top"

                if self.inhibition >= 400 and self.second_casual_outfit[5] == "_white_panties":
                    self.second_casual_outfit[5] = "_black_panties"

                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.second_casual_outfit[6] = "_lace_panties"
            elif self.tag == "Jubes":
                if self.inhibition >= 500 and self.first_casual_outfit[3] == "_red_shirt":
                    self.first_casual_outfit[3] = "_tube_top"
                    self.first_casual_outfit[5] = 0

                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.second_casual_outfit[6] = "_lace_panties"

                if self.inhibition >= 600 and "_stockings_and_garterbelt" in self.inventory:
                    self.second_casual_outfit[9] = "_stockings_and_garterbelt"

            return

        def add_word(self, only = False, recent = False, daily = False, trait = False, history = False):
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
            if recent and word in self.recent_history:
                while word in self.recent_history:
                    self.recent_history.remove(word)

            if daily and word in self.daily_history:
                while word in self.daily_history:
                    self.daily_history.remove(word)

            if traits and word in self.traits:
                while word in self.traits:
                    self.traits.remove(word)

            return

        def change_stat(self, flavor, check, value, greater_than = False, Alt = [[], 0, 0], x_position = 0.75):
            if self in Alt[0]:
                check = Alt[1] if Alt[1] else check
                value = Alt[2] if Alt[2] else value

            if flavor == "love" or flavor == "obedience" or flavor == "inhibition":
                check = check*10

            stat = getattr(self,flavor)

            Overflow = self.had_chat[4]
            x_position = self.sprite_location

            if self.tag == "Jean" and flavor == "inhibition" and self.IX > 0:
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

            if self.tag == "Jean" and flavor == "inhibition" and self.IX > 0:
                stat += self.IX

            if value:
                if self.tag == "Jean" and value > 0:
                    if flavor == "obedience" and self.obedience <= 800 and check < 800:
                        value = int(value/2)
                        stat -= value
                    elif flavor == "inhibition" and self.IX > 0:
                        if self.taboo >= 40:
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
                        if self.love < 500:
                            self.love = 500

                            value = stat - 500

                        self.stored_stats += value

                        if check > self.obedience:
                            flavor = "obedience"
                            value = int(value/5)
                            stat = self.obedience + value
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

                    call_holder(value, Color, x_position)

                    if flavor == "lust" and stat >= 100 and not primary_action:
                        renpy.call("Girl_Cumming",self,1)

                        return

                    stat = 100 if stat > 100 else stat

                    setattr(self, flavor, stat)

                    return

                if stat > 1000:
                    call_holder((-(stat-1000-value)), Color, x_position)

                    if not self.had_chat[4]:
                        value = 0
                    else:
                        value = stat - 1000

                        setattr(self, flavor, 1000)

                        if flavor == "love":
                            if self.had_chat[4] == 1:
                                flavor = "obedience"
                            elif self.had_chat[4] == 2:
                                flavor = "inhibition"
                            else:
                                value = 0
                        elif flavor == "obedience":
                            if self.had_chat[4] == 3:
                                flavor = "inhibition"
                            elif self.had_chat[4] == 4:
                                flavor = "love"
                            else:
                                value = 0
                        elif flavor == "inhibition":
                            if self.had_chat[4] == 5:
                                flavor = "obedience"
                            elif self.had_chat[4] == 6:
                                flavor = "love"
                            else:
                                value = 0

                        stat = getattr(self,flavor)
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
                    call_holder(value, Color, x_position)

            stat = 1000 if stat > 1000 else stat

            setattr(self, flavor, stat)

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
                if self.tag == "Laura":
                    self.mouth = "_kiss"
                else:
                    self.mouth = "_sad"
                self.brows = "_angry"
                self.eyes = "_sexy"
            elif emotion == "_bemused":
                if self.tag == "Emma":
                    self.mouth = "_normal"
                else:
                    self.mouth = "_lipbite"
                self.brows = "_sad"
                self.eyes = "_squint"
            elif emotion == "_closed":
                if self.tag == "Rogue":
                    self.mouth = "_lipbite"
                else:
                    self.mouth = "_normal"
                self.brows = "_sad"
                self.eyes = "_closed"
            elif emotion == "_confused":
                self.mouth = "_kiss"
                self.brows = "_confused"
                if self.tag == "Laura" or self.tag == "Emma":
                    self.eyes = "_squint"
                else:
                    self.eyes = "_surprised"
            elif emotion == "_kiss":
                self.mouth = "_kiss"
                if self.tag == "Laura" or self.tag == "Emma":
                    self.brows = "_sad"
                else:
                    self.brows = "_normal"
                self.eyes = "_closed"
            elif emotion == "_sad":
                self.mouth = "_sad"
                self.brows = "_sad"
                if self.tag == "Jean" or self.tag == "Jubes":
                    self.eyes = "_normal"
                else:
                    self.eyes = "_sexy"
            elif emotion == "_sadside":
                self.mouth = "_sad"
                self.brows = "_sad"
                self.eyes = "_side"
            elif emotion == "_sexy":
                self.mouth = "_lipbite"
                if self.tag == "Emma":
                    self.brows = "_normal"
                    self.eyes = "_squint"
                elif self.tag == "Laura":
                    self.brows = "_sad"
                    self.eyes = "_squint"
                else:
                    self.brows = "_normal"
                    self.eyes = "_sexy"
            elif emotion == "_sly":
                self.brows = "_normal"
                self.eyes = "_squint"
                if self.tag == "Rogue":
                    self.mouth = "_grimace"
                if self.tag == "Laura":
                    if self.love >= 700:
                        self.mouth = "_smile"
                    else:
                        self.mouth = "_smirk"
                    self.brows = "_confused"
                elif self.tag == "Kitty":
                    self.mouth = "_smile"
                else:
                    self.mouth = "_smirk"
            elif emotion == "_smile":
                if self.tag == "Laura" and self.love < 700:
                    self.mouth = "_smirk"
                else:
                    self.mouth = "_smile"
                self.brows = "_normal"
                self.eyes = "_normal"
            elif emotion == "_surprised":
                if self.tag == "Rogue" or self.tag == "Kitty":
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
                if self.tag == "Rogue" or self.tag == "Kitty":
                    self.mouth = "_grimace"
                else:
                    self.mouth = "_smile"
                self.brows = "_surprised"
                self.eyes = "_surprised"
            elif emotion == "_down":
                if self.tag == "Rogue" or self.tag == "Kitty":
                    self.mouth = "_surprised"
                else:
                    self.mouth = "_sad"
                self.brows = "_sad"
                self.eyes = "_down"
            elif emotion == "_perplexed":
                if self.tag == "Rogue":
                    self.mouth = "_sad"
                    self.brows = "_confused"
                else:
                    self.mouth = "_smile"
                    self.brows = "_sad"
                if self.tag == "Laura":
                    self.eyes = "_surprised"
                else:
                    self.eyes = "_normal"
            elif emotion == "_sucking":
                self.mouth = "_sucking"
                if self.tag == "Emma":
                    self.brows = "_surprised"
                elif self.tag == "Laura":
                    self.brows = "_sad"
                else:
                    self.brows = "_normal"
                self.eyes = "_closed"
            elif emotion == "_tongue":
                self.mouth = "_tongue"
                self.brows = "_sad"
                if self.tag == "Laura":
                    self.eyes = "_stunned"
                else:
                    self.eyes = "_sexy"
            elif emotion == "_manic":
                if self.tag == "Rogue":
                    self.mouth = "_grimace"
                elif self.tag == "Laura":
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



        def change_outfit(self, temp_outfit = 5, undressed = 0, outfit_changed = 1):
            temp_outfit = temp_outfit if temp_outfit else self.outfit

            if self.location == bg_current and renpy.showing("night_mask", layer = 'nightmask') and time_index == 0:
                return

            if self.location not in ["bg_showerroom", "bg_pool"] or (temp_outfit not in ["nude", "swimwear", "_towel"]):
                self.wet = False

            if self.spunk:
                if "painted" not in self.daily_history or "cleaned" not in self.daily_history:
                    del self.spunk[:]

            if self.upskirt or self.top_pulled_up or self.underwear_pulled_down:
                undressed = 1

            self.upskirt = 0
            self.top_pulled_up = 0
            self.underwear_pulled_down = 0

            if temp_outfit == 5:
                if "yoinked" in self.recent_history:
                    return

                temp_outfit = self.outfit
            elif temp_outfit == 6:
                temp_outfit = self.today_outfit

                self.outfit = self.today_outfit

            if temp_outfit != self.outfit:
                outfit_changed = 1

                self.outfit = temp_outfit
            if self in Party and temp_outfit == self.today_outfit:
                temp_outfit = self.outfit

            if temp_outfit == "casual1":
                outfit_holder = self.first_casual_outfit[:]
            elif temp_outfit == "casual2":
                outfit_holder = self.second_casual_outfit[:]
            elif temp_outfit == "nude":
                outfit_holder = [0, "", "", "", "", "", "", "", "", "", 50]
            elif temp_outfit == "_towel":
                outfit_holder = [0, "", "", "_towel", "", "", "", "", "", "", 35]
            elif temp_outfit == "custom1":
                outfit_holder = self.first_custom_outfit[:]
            elif temp_outfit == "custom2":
                outfit_holder = self.second_custom_outfit[:]
            elif temp_outfit == "custom3":
                outfit_holder = self.third_custom_outfit[:]
            elif temp_outfit == "temporary":
                outfit_holder = self.temp_outfit[:]
            elif temp_outfit == "sleep":
                outfit_holder = self.sleepwear[:]
            elif temp_outfit == "gym":
                outfit_holder = self.gym_clothes[:]
            elif temp_outfit == "costume":
                outfit_holder = self.Costume[:]
            elif temp_outfit == "swimwear":
                if not self.swimwear[0]:
                    if "_bikini_top" not in self.inventory or "_bikini_bottoms" not in self.inventory:
                        self.outfit = self.today_outfit

                        if "swim" not in self.daily_history:
                            if self.tag == "Rogue":
                                ch_r("I don't really have any swimsuit I could wear. . .", interact=True)
                            elif self.tag == "Kitty":
                                ch_k("I wish I had something cute to wear, but I don't. . .", interact=True)
                            elif self.tag == "Emma":
                                ch_e("I really don't own the proper attire. . .", interact=True)
                            elif self.tag == "Laura":
                                ch_l("Don't have a suit. . .", interact=True)
                            elif self.tag == "Jean":
                                ch_j("I might, if you buy me a suit. . .", interact=True)
                            elif self.tag == "Storm":
                                ch_s("I -am- afraid Charles would want me to wear a suit. . .", interact=True)
                            elif self.tag == "Jubes":
                                ch_v("I haven't picked out a suit yet. . .", interact=True)

                        return False
                    elif self.tag == "Kitty" and "_blue_skirt" not in self.inventory and self.inhibition <= 400:
                        self.outfit = self.today_outfit

                        if "swim" not in self.daily_history:
                            ch_k("I don't know, I do have a suit, but it's a little daring. . .", interact=True)
                            ch_k("If only I had a little skirt or something. . .", interact=True)

                        return False
                    else:
                        self.swimwear[0] = 1

                outfit_holder = self.swimwear[:]

            while len(outfit_holder) < 11:
                outfit_holder.append(0)

            if not self.legs and outfit_holder[2]:
                undressed = 1
            elif not self.top and outfit_holder[3]:
                undressed = 1
            elif not self.bra and outfit_holder[5]:
                undressed = 1
            elif not self.underwear and outfit_holder[6] and "commando" not in self.daily_history:
                undressed = 1
            elif not self.hose and outfit_holder[9]:
                undressed = 1

            if self.tag == "Emma" and (outfit_holder[8] != "_hat" and outfit_holder[8] != "_wet_hat"):
                self.hair = "_wet" if outfit_holder[8] == "_wet_hat" else "_wave"

            self.arms = outfit_holder[1]
            self.legs = outfit_holder[2]
            self.top = outfit_holder[3]
            self.neck = outfit_holder[4]
            self.bra = outfit_holder[5]
            self.underwear = outfit_holder[6]
            self.accessory = outfit_holder[7]
            self.hair = outfit_holder[8] if outfit_holder[8] else self.hair
            self.hose = outfit_holder[9]
            self.shame = outfit_holder[10]

            if "ripped" in self.daily_history and "modesty" not in self.recent_history:
                self.hose = "_ripped_pantyhose" if self.hose == "_pantyhose" else self.hose
                self.hose = "_ripped_tights" if self.hose == "_tights" else self.hose

            if self.underwear and self.underwear != "_shorts" and "commando" in self.daily_history and "modesty" not in self.daily_history:
                if temp_outfit != "sleep" and temp_outfit != "gym":
                    self.underwear = ""

            if not outfit_changed and temp_outfit == self.outfit and self.location == bg_current:
                if undressed == 2:
                    renpy.say(None, self.name + " throws on a towel.", interact = True)
                elif undressed:
                    renpy.say(None, self.name + " throws her clothes back on.", interact = True)

            if undressed:
                return 2

            return 1

        def Set_Temp_outfit(self):


            self.temp_outfit[1] = self.arms
            self.temp_outfit[2] = self.legs
            self.temp_outfit[3] = self.top
            self.temp_outfit[4] = self.neck
            self.temp_outfit[5] = self.bra
            self.temp_outfit[6] = self.underwear
            self.temp_outfit[7] = self.accessory
            self.temp_outfit[8] = self.hair
            self.temp_outfit[9] = self.hose
            self.temp_outfit[0] = 1



            self.outfit = "temporary"
            self.today_outfit = "temporary"
            return

        def ChestNum(self,Up=1):

            if Up and self.top_pulled_up and self.bra:
                return True
            if self.tag == "Rogue":
                if self.bra in ("_tank", "_buttoned_tank"):
                    return 5
            if self.tag == "Laura":
                if self.bra in ("leather_bra", "white_tank"):
                    return 5
                elif self.bra == "wolvie_top":
                    return 3
            if self.tag == "Jean":
                if self.bra == "_sports_bra":
                    return 5
            if self.tag == "Storm":
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

            return False

        def OverNum(self,Up=1):

            if Up and self.top_pulled_up and self.top:
                return True
            if self.tag == "Rogue":
                if self.top == "_mesh_top":
                    return 2
            if self.tag == "Emma":
                if self.top == "_towel":
                    return 2
            if self.tag == "Storm":
                if self.top == "_towel":
                    return False
            if self.tag == "Jubes":
                if Up and self.top_pulled_up and self.accessory:
                    return True
                if self.accessory == "_jacket":
                    return 3
                if self.accessory == "open_jacket":
                    return True
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

            return False

        def PantsNum(self,Up=1):



            if self.tag == "Jubes":
                if self.accessory == "shut_jacket":
                    return 5

            if Up and self.upskirt and self.legs:
                return True

            if self.tag == "Rogue" and self.underwear == "_shorts":
                return 6
            if self.legs == "_shorts":
                return 6
            if self.legs in ("_skirt", "_blue_skirt", "other_skirt", "_dress"):
                return 5
            if self.legs == "yoga_pants":
                return 8
            if self.top == "_towel" and self not in (EmmaX,StormX):
                return 5
            if self.tag == "Emma" and self.top == "_dress":
                return 4
            if self.legs == "mesh_pants":
                return 2
            if self.legs:
                return 10


            return False

        def PantiesNum(self,Up=1):

            if Up and self.underwear_pulled_down and self.underwear:
                return True
            if self.underwear == "_lace_panties":
                return 2
            if self.underwear == "sports_panties" or self.underwear == "_shorts":
                return 8
            if self.underwear == "_bikini_bottoms":
                return 7
            if self.underwear:
                return 4
            return False

        def HoseNum(self,Up=1):

            if Up and self.hose and (self.underwear_pulled_down or self.upskirt):
                return True
            if self.hose == "_stockings":
                return True
            if self.hose == "_pantyhose":
                return 6
            if self.hose == "_tights":
                return 10
            if self.hose == "stockings and gaterbelt":
                return 4
            if self.hose == "_ripped_pantyhose":
                return 4
            if self.hose == "_ripped_tights":
                return 4

            return False

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

            if not self.seen_breasts:
                if (not self.top and not self.bra) or self.top_pulled_up or Check == 1 or Check == 2:
                    C += 1
            if not self.seen_pussy:
                if Check == 1 or Check == 3:
                    C += 1
                elif not self.legs or self.upskirt:

                    if self.underwear_pulled_down or (self.HoseNum() < 5 and not self.underwear):

                        C += 1
            return C

        def check_if_likes(self, ChrB = 0, Check=200, Modifier = 1, Auto = 0, Jealousy = 0, Ok = 0, Likes=0):
            Jealousy = 0
            Likes = self.likes[ChrB.tag]

            if Likes <= Check:
                if Auto:
                    self.likes[ChrB.tag] += Modifier

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

                return_value = 2
            elif Likes >= 800:
                if Jealousy <= 300:
                    Likes += Modifier

                    self.change_stat("love", 80, (int(Modifier/2)))
                    self.change_stat("lust", 200, (int(Modifier/2)))

                    return_value = 2
                else:
                    Likes -= Modifier

                    self.change_stat("lust", 200, (int(Modifier/5)))

                    return_value = 1
            elif Likes >= 600:
                if Jealousy <= 100:
                    Likes += Modifier

                    self.change_stat("love", 80, (int(Modifier/4)))
                    self.change_stat("lust", 200, (int(Modifier/2)))

                    return_value = 2
                elif Jealousy <= 300:
                    Likes -= Modifier

                    self.change_stat("lust", 200, (int(Modifier/2)))

                    return_value = 1
                else:
                    Likes -= (Modifier + (int(Jealousy/50)))

                    self.change_stat("love", 90, (-(int(Modifier))))
                    self.change_stat("lust", 200, (int(Modifier/5)))

                    return_value = 2
            elif Likes >= 400:
                if Jealousy <= 100:
                    Likes -= Modifier

                    return_value = 1
                else:
                    Likes -= (Modifier + (int(Jealousy/100)))

                self.change_stat("lust", 200, (int(Modifier/10)))
            else:
                Likes -= (Modifier + (int(Jealousy/50)))

                self.change_stat("lust", 200, (int(Modifier/10)))

            self.change_stat("inhibition", 60, (int(Modifier/10)))

            self.likes[ChrB.tag] = Likes + Modifier

            return return_value

        def name_check(self, counter = 0):



            if self.petname == self.name:
                return False
            if self.taboo:

                counter = int(self.taboo/10)


            if self.petname in ("girl", "boo", "bae", "baby", "sweetie"):
                if approval_check(self, 500, "L", TabM=1,Alt=[[LauraX],600]):
                    self.change_stat("love", 80, 1)
                else:
                    self.change_stat("love", 50, -1)
                    return True
            elif self.petname in ("_sexy", "lover", "beloved"):
                if approval_check(self, 900, TabM=1,Alt=[[LauraX],1100]):
                    self.change_stat("love", 80, 2)
                    self.change_stat("obedience", 80, 1)
                    self.change_stat("inhibition", 70, 1)
                else:
                    self.change_stat("love", 50, (-1-counter))
                    self.change_stat("obedience", 50, 1)
                    self.change_stat("inhibition", 20, -1)
                    return True

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
                    return True
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
                    return True
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
                    return True
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
                    return True
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
                    return True
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
                    return True
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
                    return True
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
                    return True

            elif self.petname == "chere":
                if approval_check(self, 600, "L", TabM=1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)
                    return True

            elif self.petname == "kitten":
                if approval_check(self, 600, "L", TabM=1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)
                    return True

            elif self.petname == "darling":
                if approval_check(self, 600, "L", TabM=1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)
                    return True

            elif self.petname == "Wolvie":
                if approval_check(self, 500, "I", TabM=1):
                    self.change_stat("love", 80, 1)
                else:
                    self.change_stat("love", 50, -1)
                    return True
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
                    return True
            return False
