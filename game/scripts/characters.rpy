init python:

    class PlayerClass(object):
        def __init__(self):
            self.name = "Zero"

            self.sprite = None
            self.color = "Green"

            self.location = "bg_study"
            self.traveling = False

            self.semen = 2
            self.max_semen = 3

            self.focus = 0
            self.focusing = False

            self.reputation = 600

            self.recent_history = []
            self.daily_history = []
            self.traits = []
            self.history = []

            self.Phonebook = []
            self.Party = []
            self.Keys = []
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
            self.spunk = False
            self.cock_wet = False

            self.addictive = False
            self.nonaddictive = False

            self.cologne = None

            self.primary_action = None
            self.secondary_action = None

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

            stat = 100 if stat > 100 else stat

            setattr(self, flavor, stat)

            return

    class GirlClass(object):
        def __init__(self, name, love = 0, obedience = 0, inhibition = 0, lust = 0):
            self.name = name
            self.tag = name
            self.names = [name]

            self.love = love
            self.obedience = obedience
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

            # sprite_layer = [background_characters (eg. teachers), midground (eg. pool mask), midground_characters (eg. students), foreground (eg. desks), foreground_characters (eg. Present), focused_Girl, cover (eg. fog)]
            self.sprite_location = stage_center
            self.sprite_layer = 6

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
            self.teaching = False

            self.seen_peen = False
            self.seen_breasts = False
            self.seen_pussy = False
            self.seen_underwear = False

            self.blushing = ""
            self.eyes = "_normal"
            self.mouth = "_normal"
            self.brows = "_normal"
            self.emotion = "_normal"

            self.arm_pose = 1

            self.grool = 0
            self.wet = False
            self.spunk = {"hair": False, "face": False, "mouth": False, "chin": False,
                "breasts": False, "back": False, "belly": False, "hand": False,
                "pussy": False, "anus": False}

            self.wearing_pants = False
            self.wearing_skirt = False
            self.wearing_shorts = False

            self.jacket_closed = False
            self.jacket_opened = False
            self.top_pulled_up = False
            self.dress_top_pulled_down = False
            self.bodysuit_top_pulled_aside = False
            self.bra_pulled_up = False

            self.dress_upskirt = False
            self.upskirt = False
            self.suspenders_aside = False
            self.bottom_pulled_down = False
            self.bodysuit_bottom_pulled_aside = False
            self.hose_pulled_down = False
            self.underwear_pulled_down = False

            self.breasts_supported = False
            self.breasts_covered = False
            self.legs_covered = False
            self.pussy_covered = False
            self.fully_nude = False

            self.bound = False
            self.whipped = False

            self.inventory = []

            self.to_do = []
            self.pubes_counter = 0

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

            self.primary_action = None
            self.secondary_action = None

            if self.tag == "Rogue":
                self.voice = ch_r

                self.home = "bg_rogue"
                self.pubes = "_hairy"

                self.weekly_schedule = [["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                 ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                                 ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                 ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                                 ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                                 ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"],
                                 ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"]]

                self.likes = {"Kitty": 600, "Emma": 500, "Laura": 500, "Jean": 200, "Storm": 600, "Jubes": 500, "Mystique": 0}

                self.history = ["met"]

                self.used_to_anal = False

                self.massage_chart = ["shoulders", "arms", "arms", "hands", "hands", "back", "hips", "back", "breasts", "breasts"]

                self.player_petname = "Sugar"
                self.player_petnames = ["Sugar", Player.name]
                self.petname = "Rogue"
                self.petnames = ["Rogue"]
            elif self.tag == "Kitty":
                self.voice = ch_k

                self.home = "bg_kitty"
                self.pubes = "_hairy"

                self.like = ", like, "
                self.Like = "Like, "

                self.weekly_schedule = [["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                 ["bg_classroom", "bg_pool", "bg_kitty", "bg_kitty"],
                                 ["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                 ["bg_classroom", "bg_pool", "bg_kitty", "bg_kitty"],
                                 ["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
                                 ["bg_campus", "bg_dangerroom", "bg_mall", "bg_kitty"],
                                 ["bg_campus", "bg_dangerroom", "bg_kitty", "bg_kitty"]]

                self.likes = {"Rogue": 600, "Emma": 500, "Laura": 500, "Jean": 300, "Storm": 600, "Jubes": 600, "Mystique": 0}

                self.used_to_anal = False

                self.massage_chart = ["shoulders", "back", "hips", "thighs", "calves", "feet", "feet", "hips", "ass", "pussy"]

                self.player_petname = Player.name[:1]
                self.player_petnames = ["sweetie", Player.name[:1], Player.name]
                self.petname = "Kitty"
                self.petnames = ["Kitty"]
            elif self.tag == "Emma":
                self.voice = ch_e

                self.home = "bg_emma"
                self.pubes = ""

                self.diamond = False

                self.weekly_schedule = [["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
                                 ["bg_teacher", "bg_teacher", "bg_dangerroom", "bg_emma"],
                                 ["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
                                 ["bg_teacher", "bg_teacher", "bg_dangerroom", "bg_emma"],
                                 ["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
                                 ["bg_pool", "bg_pool", "bg_emma", "bg_emma"],
                                 ["bg_pool", "bg_pool", "bg_emma", "bg_emma"]]

                self.likes = {"Rogue": 500, "Kitty": 500, "Laura": 500, "Jean": 100, "Storm": 500, "Jubes": 500, "Mystique": 0}

                self.used_to_anal = True

                self.massage_chart = ["shoulders", "neck", "neck", "back", "hips", "ass", "ass", "back", "breasts", "breasts"]

                self.names = ["Ms. Frost"]
                self.name = "Ms. Frost"

                last_name = get_last_name(Player)

                self.player_petname = "Mr. " + last_name
                self.player_petnames = ["young man", Player.name, "Mr. " + last_name]
                self.petname = self.name
                self.petnames = ["Emma", "Ms. Frost"]
            elif self.tag == "Laura":
                self.voice = ch_l

                self.home = "bg_laura"
                self.pubes = "_hairy"

                self.scent_timer = False
                self.claws = False

                self.weekly_schedule = [["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                        ["bg_dangerroom", "bg_classroom", "bg_campus", "bg_laura"],
                                        ["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                        ["bg_dangerroom", "bg_classroom", "bg_campus", "bg_laura"],
                                        ["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
                                        ["bg_pool", "bg_laura", "bg_dangerroom", "bg_laura"],
                                        ["bg_pool", "bg_laura", "bg_dangerroom", "bg_laura"]]

                self.likes = {"Rogue": 500, "Kitty": 500, "Emma": 500, "Jean": 300, "Storm": 500, "Jubes": 600, "Mystique": 0}

                self.used_to_anal = 2

                self.massage_chart = ["shoulders", "back", "arms", "hips", "thighs", "calves", "ass", "ass", "pussy", "pussy"]

                self.player_petname = Player.name
                self.player_petnames = ["guy", Player.name]
                self.petname = "Laura"
                self.petnames = ["Laura", "X-23"]
            elif self.tag == "Jean":
                self.voice = ch_j

                self.IX = 500

                self.home = "bg_jean"
                self.pubes = "_hairy"

                self.weekly_schedule = [["bg_classroom", "bg_classroom", "bg_dangerroom", "bg_jean"],
                                        ["bg_jean", "bg_classroom", "bg_jean", "bg_jean"],
                                        ["bg_jean", "bg_classroom", "bg_dangerroom", "bg_jean"],
                                        ["bg_classroom", "bg_classroom", "bg_jean", "bg_jean"],
                                        ["bg_jean", "bg_classroom", "bg_dangerroom", "bg_jean"],
                                        ["bg_dangerroom", "bg_campus", "bg_pool", "bg_jean"],
                                        ["bg_dangerroom", "bg_campus", "bg_pool", "bg_jean"]]

                self.likes = {"Rogue": 500, "Kitty": 500, "Emma": 300, "Laura": 500, "Storm": 300, "Jubes": 300, "Mystique": 0}

                self.used_to_anal = False

                self.massage_chart = ["back", "shoulders", "neck", "neck", "back", "hips", "ass", "ass", "pussy", "pussy"]

                self.player_petname = "um. . ."
                self.player_petnames = ["um. . ."]
                self.petname = self.name
                self.petnames = ["Jean"]
            elif self.tag == "Storm":
                self.voice = ch_s

                self.home = "bg_storm"
                self.pubes = "_hairy"

                self.weekly_schedule = [["bg_storm", "bg_dangerroom", "bg_dangerroom", "bg_storm"],
                                        ["bg_teacher", "bg_teacher", "bg_classroom", "bg_storm"],
                                        ["bg_storm", "bg_dangerroom", "bg_dangerroom", "bg_storm"],
                                        ["bg_teacher", "bg_teacher", "bg_classroom", "bg_storm"],
                                        ["bg_pool", "bg_campus", "bg_classroom", "bg_storm"],
                                        ["bg_storm", "bg_campus", "bg_storm", "bg_pool"],
                                        ["bg_storm", "bg_campus", "bg_storm", "bg_pool"]]

                self.likes = {"Rogue": 500, "Kitty": 600, "Emma": 400, "Laura": 500, "Jean": 300, "Jubes": 500, "Mystique": 0}

                self.used_to_anal = False

                self.massage_chart = ["feet", "calves", "thighs", "hips", "ass", "ass", "pussy", "ass", "pussy", "pussy"]

                self.player_petname = Player.name
                self.player_petnames = [Player.name]
                self.petname = self.name
                self.petnames = ["Storm", "Ororo", "Ms. Munroe"]
            elif self.tag == "Jubes":
                self.voice = ch_v

                self.home = "bg_jubes"
                self.pubes = "_hairy"

                self.weekly_schedule = [["bg_jubes", "bg_dangerroom", "bg_dangerroom", "bg_jubes"],
                                        ["bg_classroom", "bg_classroom", "bg_jubes", "bg_jubes"],
                                        ["bg_jubes", "bg_dangerroom", "bg_dangerroom", "bg_jubes"],
                                        ["bg_dangerroom", "bg_dangerroom", "bg_jubes", "bg_jubes"],
                                        ["bg_pool", "bg_campus", "bg_mall", "bg_jubes"],
                                        ["bg_jubes", "bg_campus", "bg_mall", "bg_pool"],
                                        ["bg_jubes", "bg_campus", "bg_jubes", "bg_pool"]]

                self.likes = {"Rogue": 500, "Kitty": 600, "Emma": 500, "Laura": 600, "Jean": 300, "Storm": 500, "Mystique": 0}

                self.used_to_anal = False

                self.massage_chart = ["neck", "shoulders", "calves", "feet", "neck", "shoulders", "calves", "feet", "pussy", "pussy"]

                self.player_petname = "Bro"
                self.player_petnames = ["Bro", Player.name]
                self.petname = self.name
                self.petnames = ["Jubes", "Jubilee"]
            elif self.tag == "Mystique":
                self.voice = ch_m

                self.home = "bg_mystique"
                self.pubes = ""

                self.disguise = None

                self.weekly_schedule = [["bg_office", "bg_office", "bg_office", "bg_mystique"],
                                 ["bg_office", "bg_office", "bg_office", "bg_mystique"],
                                 ["bg_office", "bg_office", "bg_office", "bg_mystique"],
                                 ["bg_office", "bg_office", "bg_office", "bg_mystique"],
                                 ["bg_office", "bg_office", "bg_dangerroom", "bg_mystique"],
                                 ["bg_mystique", "bg_office", "bg_dangerroom", "bg_mystique"],
                                 ["bg_mystique", "bg_pool", "bg_mall", "bg_mystique"]]

                self.likes = {"Rogue": 0, "Kitty": 0, "Emma": 0, "Laura": 0, "Jean": 0, "Storm": 0, "Jubes": 0}

                self.used_to_anal = True

                self.massage_chart = ["shoulders", "neck", "neck", "back", "hips", "ass", "ass", "back", "breasts", "breasts"]

                self.names = ["Dr. Darkholme"]
                self.name = "Dr. Darkholme"

                self.player_petname = Player.name
                self.player_petnames = [Player.name]
                self.petname = self.name
                self.petnames = ["Raven", "Ms. Darkholme"]

            self.set_default_outfits()
            self.change_outfit("today")

            shop_inventory.extend(["DL", "G", "A"])
            bedrooms.append(self.home)

            global all_Girls

            all_Girls.append(self)

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

        def change_stat(self, flavor, check, update, greater_than = False, Alt = [[], 0, 0]):
            if self in Alt[0]:
                check = Alt[1] if Alt[1] else check
                update = Alt[2] if Alt[2] else update

            if flavor in ["love", "obedience", "inhibition"]:
                check *= 10

            stat = getattr(self, flavor)

            Overflow = self.had_chat[4]

            if self.tag == "Jean" and flavor == "inhibition" and self.IX > 0:
                stat -= self.IX

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

            if self.tag == "Jean" and flavor == "inhibition" and self.IX > 0:
                stat += self.IX

            if update:
                if self.tag == "Jean" and update > 0:
                    if flavor == "obedience" and self.obedience <= 800 and check < 800:
                        update = int(update/2)
                        stat -= update
                    elif flavor == "inhibition" and self.IX > 0:
                        if self.taboo >= 40:
                            update += update
                            stat += update
                        if stat > 1000:
                            self.IX -= (stat - 1000)

                            stat = 1000
                            update = 0
                        elif stat > 700:
                            self.IX -= int(update/2)

                        self.IX = 0 if self.IX < 0 else self.IX
                    elif flavor == "love" and stat >= 500 and self.obedience < 700:
                        if self.love < 500:
                            self.love = 500

                            update = stat - 500

                        self.stored_stats += update

                        if check > self.obedience:
                            flavor = "obedience"
                            update = int(update/5)
                            stat = self.obedience + update
                        else:
                            update = 0

                if flavor == "love":
                    shade = "#c11b17"
                elif flavor == "obedience":
                    shade = "#2554c7"
                elif flavor == "inhibition":
                    shade = "#FFF380"
                elif flavor == "lust":
                    shade = "#FAAFBE"

                    stat = 100 if stat > 100 else stat

                    setattr(self, flavor, stat)

                    return

                if stat > 1000:
                    renpy.show("stat_increase", what = stat_decrease(stat - 1000 - update, shade))

                    if not self.had_chat[4]:
                        update = 0
                    else:
                        update = stat - 1000

                        setattr(self, flavor, 1000)

                        if flavor == "love":
                            if self.had_chat[4] == 1:
                                flavor = "obedience"
                            elif self.had_chat[4] == 2:
                                flavor = "inhibition"
                            else:
                                update = 0
                        elif flavor == "obedience":
                            if self.had_chat[4] == 3:
                                flavor = "inhibition"
                            elif self.had_chat[4] == 4:
                                flavor = "love"
                            else:
                                update = 0
                        elif flavor == "inhibition":
                            if self.had_chat[4] == 5:
                                flavor = "obedience"
                            elif self.had_chat[4] == 6:
                                flavor = "love"
                            else:
                                update = 0

                        stat = getattr(self, flavor)
                        stat += update

                        if flavor == "love":
                            shade = "#c11b17"
                        elif flavor == "obedience":
                            shade = "#2554c7"
                        elif flavor == "inhibition":
                            shade = "#FFF380"
                        else:
                            shade = "#FFFFFF"

            stat = 1000 if stat > 1000 else stat

            setattr(self, flavor, stat)

            return

        def change_face(self, emotion = None, blushing = 0, manic = False, mouth = None, eyes = None, brows = None):
            emotion = self.emotion if not emotion else emotion

            if (self.forced or "_angry" in self.recent_history) and emotion in ["_normal", "_bemused", "_sexy", "_sly", "_smile", "startled"]:
                emotion = "_angry"
            elif self.event_counter["forced"] > 0 and emotion in ["_normal", "_bemused", "_sexy", "_sly", "_smile", "startled"]:
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
                if self.tag == "Jean":
                    self.mouth = "_smirk"
                else:
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
                    self.mouth = "_smile"
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
                    self.mouth = "_smile"
                elif self.tag == "Laura":
                    self.mouth = "_lipbite"
                else:
                    self.mouth = "_smile"
                self.brows = "_sad"
                self.eyes = "_manic"
                self.blushing = "_blush1"

            if blushing > 1:
                self.blushing = "_blush2"
            elif blushing:
                self.blushing = "_blush1"
            else:
                self.blushing = ""

            if manic:
                self.eyes = "_manic"

            if mouth:
                self.mouth = mouth

            if eyes:
                self.eyes = eyes

            if brows:
                self.brows = brows

            return

        def set_default_faces(self):
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

        def lust_face(self, extreme = False, kissing = False):
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

            if self.secondary_action == "kiss both" or self.secondary_action == "kiss girl":
                kissing = True
            elif second_girl_main_action == "kiss both" or self.secondary_action == "kiss girl":
                kissing = True
            elif Partner != self:
                if Player.primary_action == "kiss" or Player.secondary_action == "kiss":
                    kissing = True
            elif second_girl_main_action == "kiss":
                kissing = True

            if kissing:
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
                elif self.lust >= 70 or extreme:
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
                if self.tag == "Laura" and self.lust < 50 and not extreme and not approval_check(self, 1000):
                    self.eyes = "_side"

            if Partner == self and second_girl_main_action in ["suck_breasts", "eat_pussy", "eat_ass", "blowjob"]:
                self.mouth = "_tongue"
            elif self.secondary_action in ["suck_breasts", "eat_pussy", "eat_ass"]:
                self.mouth = "_tongue"

            if self.session_orgasms >= 10:
                self.eyes = "_stunned"
                self.mouth = "_tongue"

            if not self.used_to_anal:
                if Partner != self and (Player.primary_action == "anal" or Player.primary_action == "dildo_ass" or self.secondary_action == "dildo_ass"):
                    self.eyes = "_closed"
                    self.brows = "_angry"

            if "unseen" in self.recent_history:
                self.eyes = "_closed"

            if Partner and self != Partner:
                Partner.lust_face()

            return

        def change_outfit(self, outfit_name = None, got_dressed = 0, check_if_yoinked = False):
            outfit_name = outfit_name if outfit_name else self.outfit_name

            if self.location not in ["bg_showerroom", "bg_pool"]:
                self.wet = False

            if any(self.spunk) and ("painted" not in self.daily_history or "cleaned" not in self.daily_history):
                for key in self.spunk.keys():
                    self.spunk[key] = False

            self.fix_clothing()

            if check_if_yoinked:
                if "yoinked" in self.recent_history:
                    return

                outfit_name = self.outfit_name
            elif outfit_name == "today":
                outfit_name = self.today_outfit_name

            if outfit_name != self.outfit_name:
                outfit_changed = True

                self.outfit_name = outfit_name
            else:
                outfit_changed = False

            if outfit_name == "casual1":
                outfit_holder = self.first_casual_outfit.copy()
            elif outfit_name == "casual2":
                outfit_holder = self.second_casual_outfit.copy()
            elif outfit_name == "nude":
                outfit_holder = self.nude.copy()
            elif outfit_name == "shower":
                outfit_holder = self.shower.copy()
            elif outfit_name == "custom1":
                outfit_holder = self.first_custom_outfit.copy()
            elif outfit_name == "custom2":
                outfit_holder = self.second_custom_outfit.copy()
            elif outfit_name == "custom3":
                outfit_holder = self.third_custom_outfit.copy()
            elif outfit_name == "temporary":
                outfit_holder = self.temp_outfit.copy()
            elif outfit_name == "sleepwear":
                outfit_holder = self.sleepwear.copy()
            elif outfit_name == "gym_clothes":
                outfit_holder = self.gym_clothes.copy()
            elif outfit_name == "costume":
                outfit_holder = self.halloween_costume.copy()
            elif outfit_name == "swimwear":
                if "swim" not in self.daily_history:
                    if "_bikini_top" not in self.inventory or "_bikini_bottoms" not in self.inventory:
                        if self.tag == "Rogue":
                            ch_r("I don't really have any swimsuit I could wear. . .")
                        elif self.tag == "Kitty":
                            ch_k("I wish I had something cute to wear, but I don't. . .")
                        elif self.tag == "Emma":
                            ch_e("I really don't own the proper attire. . .")
                        elif self.tag == "Laura":
                            ch_l("Don't have a suit. . .")
                        elif self.tag == "Jean":
                            ch_j("I might, if you buy me a suit. . .")
                        elif self.tag == "Storm":
                            ch_s("I -am- afraid Charles would want me to wear a suit. . .")
                        elif self.tag == "Jubes":
                            ch_v("I haven't picked out a suit yet. . .")

                        self.outfit_name = self.today_outfit_name

                        return False
                    elif self.tag == "Kitty" and "_blue_skirt" not in self.inventory and self.inhibition <= 400:

                        ch_k("I don't know, I do have a suit, but it's a little daring. . .")
                        ch_k("If only I had a little skirt or something. . .")

                        self.outfit_name = self.today_outfit_name

                        return False

                outfit_holder = self.swimwear.copy()
            elif outfit_name == "domme_outfit" and self.tag == "Emma":
                outfit_holder = self.domme_outfit.copy()
            elif outfit_name == "bondage_outfit" and self.tag == "Jean":
                outfit_holder = self.bondage_outfit.copy()
            elif outfit_name == "supervillain" and self.tag == "Mystique":
                outfit_holder = self.supervillain.copy()

            if not self.outfit["bottom"] and outfit_holder["bottom"]:
                got_dressed = 1
            elif not self.outfit["top"] and outfit_holder["top"]:
                got_dressed = 1
            elif not self.outfit["bra"] and outfit_holder["bra"]:
                got_dressed = 1
            elif not self.outfit["underwear"] and outfit_holder["underwear"] and "commando" not in self.daily_history:
                got_dressed = 1
            elif not self.outfit["hose"] and outfit_holder["hose"]:
                got_dressed = 1

            self.outfit = outfit_holder.copy()
            self.disguise_outfit = self.outfit.copy()

            if "ripped" in self.daily_history and "modesty" not in self.recent_history:
                self.outfit["hose"] = "_ripped_pantyhose" if self.outfit["hose"] == "_pantyhose" else self.outfit["hose"]
                self.outfit["hose"] = "_ripped_tights" if self.outfit["hose"] == "_tights" else self.outfit["hose"]

            if self.outfit["underwear"] and self.outfit["underwear"] != "_shorts" and "commando" in self.daily_history and "modesty" not in self.daily_history:
                if outfit_holder != "sleepwear" and outfit_holder != "gym_clothes":
                    self.outfit["underwear"] = ""

            if self.location == Player.location and not outfit_changed:
                if got_dressed == 2:
                    renpy.say(None, self.name + " throws on a towel.")
                elif got_dressed:
                    renpy.say(None, self.name + " throws her clothes back on.")

            self.set_outfit_flags()

            return True

        def set_default_outfits(self):
            self.outfit_name = "casual1"
            self.today_outfit_name = "casual1"

            self.clothing = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            self.outfit = get_base_outfit()

            self.nude = get_base_outfit({"shame": 50})

            if self.tag == "Storm":
                self.shower = get_base_outfit(
                    {"hair": "_wet_long",
                    "face_outer_accessory": "_towel", "shame": 0})
            else:
                self.shower = get_base_outfit(
                    {"hair": "_wet",
                    "top": "_towel", "shame": 35})

            self.first_custom_outfit = get_base_outfit()
            self.second_custom_outfit = get_base_outfit()
            self.third_custom_outfit = get_base_outfit()

            if self.tag == "Rogue":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_tank", "underwear": "_black_panties",
                    "hose": "_tights", "bottom": "_skirt",
                    "top": "_mesh_top",
                    "neck": "_spiked_collar", "gloves": "_gloves",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_buttoned_tank", "underwear": "_black_panties",
                    "bottom": "_jeans",
                    "top": "_pink_top",
                    "neck": "_spiked_collar", "gloves": "_gloves",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_sports_bra", "underwear": "_shorts",
                    "jacket": "_hoodie",
                    "gloves": "_gloves",
                    "shame": 10})

                self.sleepwear = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_tank", "underwear": "_green_panties",
                    "gloves": "_gloves",
                    "shame": 20})

                self.swimwear = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_bikini_top", "underwear": "_bikini_bottoms",
                    "jacket": "_hoodie"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "_cosplay",
                    "bra": "_tube_top", "underwear": "_black_panties",
                    "bottom": "_skirt",
                    "gloves": "_gloves",
                    "belt": "_sweater",
                    "outfit_active": 2})

                self.nude["hair"] = "_evo"
            elif self.tag == "Kitty":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_cami", "underwear": "_green_panties",
                    "bottom": "_capris",
                    "top": "_pink_top",
                    "neck": "_gold_necklace",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_strapless_bra", "underwear": "_green_panties",
                    "bottom": "_black_jeans",
                    "top": "_red_shirt",
                    "neck": "_star_necklace",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_sports_bra", "underwear": "_green_panties",
                    "bottom": "_shorts",
                    "shame": 10})

                self.sleepwear = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_cami", "underwear": "_green_panties",
                    "shame": 20})

                self.swimwear = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_bikini_top", "underwear": "_bikini_bottoms",
                    "bottom": "_blue_skirt"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "_evo",
                    "bra": "_dress_corset", "underwear": "_lace_panties",
                    "bottom": "_dress_skirt",
                    "neck": "_flower_necklace",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.nude["hair"] = "_evo"
            elif self.tag == "Emma":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "_wavy",
                    "bra": "_corset", "underwear": "_white_panties",
                    "bottom": "_white_pants",
                    "neck": "_choker",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "_wavy",
                    "bra": "_corset", "underwear": "_white_panties",
                    "bottom": "_skirt",
                    "boots": "_thigh_boots",
                    "neck": "_choker",
                    "shame": 5, "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "_wavy",
                    "bra": "_sports_bra", "underwear": "_sports_panties",
                    "bottom": "_white_pants",
                    "shame": 10})

                self.sleepwear = get_base_outfit(
                    {"hair": "_wavy",
                    "bra": "_corset", "underwear": "_white_panties",
                    "shame": 25})

                self.swimwear = get_base_outfit(
                    {"hair": "_wavy",
                    "bra": "_bikini_top", "underwear": "_bikini_bottoms",
                    "shame": 25})

                self.halloween_costume = get_base_outfit(
                    {"hair": "_wavy",
                    "face_outer_accessory": "_hat",
                    "underwear": "_lace_panties",
                    "hose": "_stockings_and_garterbelt", "bottom": "_dress_skirt",
                    "top": "_dress_top",
                    "neck": "_choker",
                    "outfit_active": 2})

                self.domme_outfit = get_base_outfit(
                    {"hair": "_wavy",
                    "bodysuit": "_domme_suit",
                    "boots": "_domme_suit",
                    "neck": "_spiked_collar", "gloves": "_spiked_bracelets",
                    "held_item": "_whip",
                    "outfit_active": 2})

                self.nude["hair"] = "_wavy"
            elif self.tag == "Laura":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_leather_bra", "underwear": "_leather_panties",
                    "bottom": "_leather_pants",
                    "neck": "_leash_choker",
                    "gloves": "_wrists",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_leather_bra", "underwear": "_leather_panties",
                    "bottom": "_skirt",
                    "neck": "_leash_choker",
                    "gloves": "_wrists",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_leather_bra", "underwear": "_leather_panties",
                    "bottom": "_leather_pants",
                    "gloves": "_wrists"})

                self.sleepwear = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_leather_bra", "underwear": "_leather_panties",
                    "shame": 20})

                self.swimwear = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_bikini_top", "underwear": "_bikini_bottoms"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_white_tank", "underwear": "_leather_panties",
                    "hose": "_black_stockings", "bottom": "_cosplay_skirt",
                    "neck": "_leash_choker",
                    "gloves": "_gloves",
                    "suspenders": "_suspenders",
                    "outfit_active": 2})

                self.nude["hair"] = "_long"
            elif self.tag == "Jean":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_green_bra", "underwear": "_green_panties",
                    "bottom": "_khaki_pants",
                    "top": "_pink_shirt",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_green_bra", "underwear": "_green_panties",
                    "bottom": "_skirt",
                    "top": "_green_shirt",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_sports_bra", "underwear": "_green_panties",
                    "bottom": "_yoga_pants"})

                self.sleepwear = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_green_bra", "underwear": "_green_panties",
                    "top": "_pink_shirt"})

                self.swimwear = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_bikini_top", "underwear": "_bikini_bottoms"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "_pony",
                    "bra": "_green_bra", "underwear": "_green_panties",
                    "bottom": "_shorts",
                    "top": "_yellow_shirt",
                    "suspenders": "_suspenders",
                    "outfit_active": 2})

                self.bondage_outfit = get_base_outfit(
                    {"hair": "_short",
                    "nipple_accessories": "_nipple_pegs", "rope": "_harness",
                    "held_item": "_hitachi",
                    "shame": 100, "outfit_active": 2})

                self.nude["hair"] = "_short"
            elif self.tag == "Storm":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_black_bra", "underwear": "_white_panties",
                    "bottom": "_skirt",
                    "top": "_white_shirt",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_sports_bra", "underwear": "_white_panties",
                    "bottom": "_black_jeans",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_sports_bra", "underwear": "_white_panties",
                    "bottom": "_yoga_pants",
                    "shame": 10})

                self.sleepwear = get_base_outfit(
                    {"hair": "_long",
                    "underwear": "_white_panties",
                    "top": "_white_shirt",
                    "shame": 25})

                self.swimwear = get_base_outfit(
                    {"hair": "_long",
                    "bra": "_bikini_top", "underwear": "_bikini_bottoms",
                    "top": "_white_shirt"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_cosplay_bra", "underwear": "_cosplay_panties",
                    "neck": "_ring_necklace",
                    "boots": "_ring_anklets",
                    "sleeves": "_ring_armlets",
                    "outfit_active": 2})

                self.nude["hair"] = "_long"
            elif self.tag == "Jubes":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "_short", "face_outer_accessory": "_shades",
                    "bra": "_sports_bra", "underwear": "_blue_panties",
                    "bottom": "_shorts",
                    "top": "_red_shirt",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "_short", "face_outer_accessory": "_shades",
                    "bra": "_sports_bra", "underwear": "_blue_panties",
                    "bottom": "_leather_pants",
                    "top": "_black_shirt",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_sports_bra", "underwear": "_blue_panties",
                    "bottom": "_leather_pants",
                    "top": "_black_shirt",
                    "shame": 10})

                self.sleepwear = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_sports_bra", "underwear": "_blue_panties",
                    "shame": 25})

                self.swimwear = get_base_outfit(
                    {"hair": "_short", "face_outer_accessory": "_shades",
                    "bra": "_bikini_top", "underwear": "_bikini_bottoms"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "_short", "face_outer_accessory": "_shades",
                    "bra": "_sports_bra", "underwear": "_blue_panties",
                    "bottom": "_leather_pants",
                    "top": "_black_shirt",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.nude["hair"] = "_short"
            elif self.tag == "Mystique":
                self.first_casual_outfit = get_base_outfit(
                    {"face_inner_accessory": "_glasses", "hair": "_short",
                    "bra": "_black_bra", "underwear": "_black_panties",
                    "bottom": "_skirt",
                    "top": "_purple_shirt",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"face_inner_accessory": "_glasses", "hair": "_short",
                    "bra": "_black_bra", "underwear": "_black_panties",
                    "bottom": "_skirt",
                    "top": "_purple_shirt",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"face_inner_accessory": "", "hair": "_short",
                    "bra": "_black_bra", "underwear": "_black_panties",
                    "bottom": "_skirt",
                    "top": "_purple_shirt",
                    "jacket": "",
                    "outfit_active": 2})

                self.sleepwear = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_black_bra", "underwear": "_black_panties",
                    "shame": 25})

                self.swimwear = get_base_outfit(
                    {"hair": "_short",
                    "bra": "_black_bra", "underwear": "_black_panties"})

                self.halloween_costume = get_base_outfit(
                    {"face_inner_accessory": "_glasses", "hair": "_short",
                    "bra": "_black_bra", "underwear": "_black_panties",
                    "bottom": "_skirt",
                    "top": "_purple_shirt",
                    "jacket": "_jacket",
                    "outfit_active": 2})

                self.supervillain = get_base_outfit(
                    {"hair": "_long", "face_outer_accessory": "_skull",
                    "dress": "_white_dress", "boots": "_thigh_boots",
                    "belt": "_skull_belt", "gloves": "_gloves"})

                self.nude["hair"] = "_short"

            return

        def set_temp_outfit(self):
            self.temp_outfit = self.outfit.copy()

            self.outfit_name = "temporary"
            self.today_outfit_name = "temporary"

            return

        def slutty_clothes(self):
            if self.tag == "Rogue":
                if "_stockings_and_garterbelt" in self.inventory:
                    self.first_casual_outfit["hose"] = "_stockings_and_garterbelt"
                elif self.inhibition >= 300:
                    self.first_casual_outfit["hose"] = "_stockings"
                else:
                    self.first_casual_outfit["hose"] = "_tights"

                if self.gym_clothes["bra"] and self.inhibition >= 300:
                    self.gym_clothes["top"] == ""

                if self.swimwear["bra"] and self.inhibition >= 300:
                    self.swimwear["top"] == ""
            elif self.tag == "Kitty":
                if self.swimwear["bottom"] == "_blue_skirt" and self.swimwear["underwear"] and self.inhibition > 500:
                    self.swimwear["bottom"] = ""
            elif self.tag == "Laura":
                if self.inhibition >= 400 and self.second_casual_outfit["bra"] == "_leather_bra" and "_corset" in self.inventory:
                    self.second_casual_outfit["bra"] = "_corset"

                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.second_casual_outfit["underwear"] = "_lace_panties"

                if self.inhibition >= 600 and "_stockings_and_garterbelt" in self.inventory:
                    self.second_casual_outfit["hose"] = "_stockings_and_garterbelt"
            elif self.tag == "Jean":
                if "_stockings_and_garterbelt" in self.inventory:
                    self.first_casual_outfit["hose"] = "_stockings_and_garterbelt"
                elif self.love >= 300:
                    self.first_casual_outfit["hose"] = "_stockings"

                if self.inhibition >= 600 and "_bikini_top" in self.inventory:
                    self.gym_clothes["bra"] = "_bikini_top" if self.gym_clothes["outfit_active"] == 1 else self.gym_clothes["bra"]

                if self.inhibition >= 600 and "_lace_bra" in self.inventory:
                    self.first_casual_outfit["bra"] = "_lace_bra"
                    self.second_casual_outfit["bra"] = "_lace_bra"

                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.first_casual_outfit["underwear"] = "_lace_panties"
                    self.second_casual_outfit["underwear"] = "_lace_panties"
            elif self.tag == "Storm":
                if self.inhibition >= 400 and self.second_casual_outfit["bra"] == "_sports_bra":
                    self.second_casual_outfit["bra"] = "_tube_top"

                if self.inhibition >= 400 and self.second_casual_outfit["bra"] == "_white_panties":
                    self.second_casual_outfit["bra"] = "_black_panties"

                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.second_casual_outfit["underwear"] = "_lace_panties"
            elif self.tag == "Jubes":
                if self.inhibition >= 500 and self.first_casual_outfit["top"] == "_red_shirt":
                    self.first_casual_outfit["bra"] = "_tube_top"
                    self.first_casual_outfit["bra"] = ""

                if self.inhibition >= 600 and "_lace_panties" in self.inventory:
                    self.second_casual_outfit["underwear"] = "_lace_panties"

                if self.inhibition >= 600 and "_stockings_and_garterbelt" in self.inventory:
                    self.second_casual_outfit["hose"] = "_stockings_and_garterbelt"

            return

        def set_outfit_flags(self):
            if self.outfit["bottom"] in pants or self.outfit["bodysuit"] in ["_catsuit", "_sci_fi"]:
                self.wearing_pants = True
            else:
                self.wearing_pants = False

            if self.outfit["bottom"] in skirts or self.outfit["jacket"] == "_closed_jacket" or self.outfit["top"] == "_towel":
                self.wearing_skirt = True
            else:
                self.wearing_skirt = False

            if self.outfit["bottom"] in shorts or self.outfit["underwear"] in shorts:
                self.wearing_shorts = True
            else:
                self.wearing_shorts = False

            if (self.outfit["bra"] and not self.bra_pulled_up) or (self.tag == "Emma" and self.arm_pose == 1):
                self.breasts_supported = True
            else:
                self.breasts_supported = False

            if self.outfit["jacket"] and not self.jacket_opened:
                self.breasts_covered = True
            elif self.outfit["top"] and not self.top_pulled_up:
                self.breasts_covered = True
            elif self.outfit["dress"] and not self.dress_top_pulled_down:
                self.breasts_covered = True
            elif self.outfit["bodysuit"] and not self.bodysuit_top_pulled_aside:
                self.breasts_covered = True
            elif self.outfit["bra"] and not self.bra_pulled_up:
                self.breasts_covered = True
            elif self.outfit["suspenders"] and not self.suspenders_aside:
                self.breasts_covered = True
            else:
                self.breasts_covered = False

            if self.wearing_pants and not self.bottom_pulled_down or self.outfit["hose"] in ["_tights", "_pantyhose"]:
                self.legs_covered = True
            else:
                self.legs_covered = False

            if self.tag == "Jubes" and self.outfit["jacket"] and self.jacket_closed:
                self.pussy_covered = True
            elif self.outfit["dress"] and not self.dress_upskirt:
                self.pussy_covered = True
            elif self.outfit["top"] == "_towel":
                self.pussy_covered = True
            elif self.outfit["bottom"] and not (self.upskirt or self.bottom_pulled_down):
                self.pussy_covered = True
            elif self.outfit["bodysuit"] and not self.bodysuit_bottom_pulled_aside:
                self.pussy_covered = True
            elif self.outfit["underwear"] and not self.underwear_pulled_down:
                self.pussy_covered = True
            else:
                self.pussy_covered = False

            if self.outfit["jacket"] or self.outfit["top"] or self.outfit["dress"] or self.outfit["bodysuit"] or self.outfit["bra"] or self.outfit["bottom"] or self.outfit["underwear"]:
                self.fully_nude = False
            else:
                self.fully_nude = True

            return

        def fix_clothing(self):
            self.jacket_opened = False
            self.top_pulled_up = False
            self.dress_top_pulled_down = False
            self.bodysuit_top_pulled_aside = False
            self.bra_pulled_up = False

            self.dress_upskirt = False
            self.upskirt = False
            self.suspenders_aside = False
            self.bottom_pulled_down = False
            self.bodysuit_bottom_pulled_aside = False
            self.hose_pulled_down = False
            self.underwear_pulled_down = False

            self.set_outfit_flags()

            return

        def bra_number(self, Up=1):
            if Up and self.top_pulled_up and self.outfit["bra"]:
                return True

            if self.tag == "Rogue":
                if self.outfit["bra"] in ["_tank", "_buttoned_tank"]:
                    return 5

            if self.tag == "Laura":
                if self.outfit["bra"] in ["_leather_bra", "_white_tank"]:
                    return 5
                elif self.outfit["bra"] == "_wolvie_top":
                    return 3

            if self.tag == "Jean":
                if self.outfit["bra"] == "_sports_bra":
                    return 5

            if self.tag == "Storm":
                if self.outfit["bra"] == "_sports_bra":
                    return 5

            if self.outfit["bra"] == "_tube_top":
                return 5

            if self.outfit["bra"] == "_lace_bra":
                return 2

            if self.outfit["bra"] == "_lace_corset":
                return 2

            if self.outfit["bra"] == "_corset":
                return 5

            if self.outfit["bra"]:
                return 3

            if self.outfit["suspenders"] in ["_suspenders", "_suspenders2"]:
                return 2

            return False

        def top_number(self,Up=1):
            if Up and self.top_pulled_up and self.outfit["top"]:
                return True

            if self.tag == "Rogue":
                if self.outfit["top"] == "_mesh_top":
                    return 2

            if self.tag == "Emma":
                if self.outfit["top"] == "_towel":
                    return 2

            if self.tag == "Jubes":
                if Up and self.top_pulled_up and self.outfit["jacket"]:
                    return True

                if self.outfit["jacket"] == "_jacket":
                    return 3

                if self.outfit["jacket"] == "_open_jacket":
                    return True

                if self.outfit["jacket"] == "_closed_jacket":
                    return 5

            if self.outfit["top"] == "_towel":
                return 3

            if self.outfit["top"] == "_dress_top":
                return 4

            if self.outfit["top"] == "_jacket":
                return 4

            if self.outfit["top"] == "_nighty":
                return 3

            if self.outfit["top"] == "_pink_top":
                return 4

            if self.outfit["top"]:
                return 5

            return False

        def bottom_number(self, Up=1):
            if Up and self.upskirt and self.outfit["bottom"]:
                return True

            if self.tag == "Rogue" and self.outfit["underwear"] == "_shorts":
                return 6

            if self.outfit["bottom"] == "_shorts":
                return 6

            if self.outfit["bottom"] == "_yoga_pants":
                return 8

            if self.tag == "Emma" and self.outfit["top"] == "_dress_top":
                return 4

            if self.outfit["bottom"] == "_mesh_pants":
                return 2

            if self.outfit["bottom"]:
                return 10

            return False

        def underwear_number(self,Up=1):
            if Up and self.underwear_pulled_down and self.outfit["underwear"]:
                return True

            if self.outfit["underwear"] == "_lace_panties":
                return 2

            if self.outfit["underwear"] == "_sports_panties" or self.outfit["underwear"] == "_shorts":
                return 8

            if self.outfit["underwear"] == "_bikini_bottoms":
                return 7

            if self.outfit["underwear"]:
                return 4

            return False

        def hose_number(self,Up=1):
            if Up and self.outfit["hose"] and (self.hose_pulled_down or self.upskirt):
                return True

            if self.outfit["hose"] == "_stockings":
                return True

            if self.outfit["hose"] == "_pantyhose":
                return 6

            if self.outfit["hose"] == "_tights":
                return 10

            if self.outfit["hose"] == "stockings and gaterbelt":
                return 4

            if self.outfit["hose"] == "_ripped_pantyhose":
                return 4

            if self.outfit["hose"] == "_ripped_tights":
                return 4

            return False

        def check_clothing(self):
            count = 0

            if self.top_number() >= 5:
                count += 1

            if self.outfit["bra"]:
                count += 1

            if self.outfit["bottom"]:
                count += 1

            if self.outfit["hose"] in ["_tights", "_pantyhose"]:
                count += 1

            if self.outfit["underwear"]:
                count += 1

            return count

        def check_modesty(self, check = 0):
            count = 0

            if check == 2:
                pass
            elif self.top_number() >= 3:
                pass
            elif self.bra_number() >= 3:
                pass
            else:
                count += 1

            if check == 1:
                pass
            elif self.bottom_number() >= 5:
                pass
            elif self.underwear_number() >= 4:
                pass
            elif self.outfit["hose"] in ["_tights", "_pantyhose"]:
                pass
            else:
                count += 1

            return count

        def check_seen(self, check = 0):
            count = 0

            if not self.seen_breasts:
                if (not self.outfit["top"] or self.top_pulled_up) and (not self.outfit["bra"] or self.bra_pulled_up) or check in [1, 2]:
                    count += 1

            if not self.seen_pussy:
                if check in [1, 3]:
                    count += 1
                elif not self.outfit["bottom"] or self.upskirt:
                    if self.underwear_pulled_down or (self.hose_number() < 5 and not self.outfit["underwear"]):
                        count += 1

            return count

        def change_likes(self, GirlB, value):
            if self.likes[GirlB.tag] + value > 1000:
                self.likes[GirlB.tag] = 1000
            elif self.likes[GirlB.tag] + value < 0:
                self.likes[GirlB.tag] = 0
            else:
                self.likes[GirlB.tag] += value

            return

        def check_if_likes(self, GirlB, check = 200, modifier = 1, auto = False):
            jealousy = 0

            likes = self.likes[GirlB.tag]

            if likes <= check:
                if auto:
                    self.likes[GirlB.tag] += modifier

                    self.change_stat("lust", 200, (int(modifier/5)))

                    return

                if self in Player.Harem:
                    if GirlB not in Player.Harem and "poly " + GirlB.tag not in self.traits:
                        jealousy = 100
            elif auto:
                self.change_stat("lust", 200, (int(modifier/5)))

                return

            jealousy += (self.love - 600) if self.love > 600 else 0
            jealousy += self.SEXP if self.inhibition <= 500 else 0
            jealousy -= (self.obedience - 250) if self.obedience > 250 else 0
            jealousy = 0 if jealousy < 1 else jealousy

            modifier += 1 if not jealousy and likes >= 500 else 0

            if likes >= 900:
                likes += modifier

                self.change_stat("love", 80, (int(modifier/2)))
                self.change_stat("lust", 200, (int(modifier/5)))

                return_value = 2
            elif likes >= 800:
                if jealousy <= 300:
                    likes += modifier

                    self.change_stat("love", 80, (int(modifier/2)))
                    self.change_stat("lust", 200, (int(modifier/2)))

                    return_value = 2
                else:
                    likes -= modifier

                    self.change_stat("lust", 200, (int(modifier/5)))

                    return_value = 1
            elif likes >= 600:
                if jealousy <= 100:
                    likes += modifier

                    self.change_stat("love", 80, (int(modifier/4)))
                    self.change_stat("lust", 200, (int(modifier/2)))

                    return_value = 2
                elif jealousy <= 300:
                    likes -= modifier

                    self.change_stat("lust", 200, (int(modifier/2)))

                    return_value = 1
                else:
                    likes -= (modifier + (int(jealousy/50)))

                    self.change_stat("love", 90, (-(int(modifier))))
                    self.change_stat("lust", 200, (int(modifier/5)))

                    return_value = 2
            elif likes >= 400:
                if jealousy <= 100:
                    likes -= modifier

                    return_value = 1
                else:
                    likes -= (modifier + (int(jealousy/100)))

                self.change_stat("lust", 200, (int(modifier/10)))
            else:
                likes -= (modifier + (int(jealousy/50)))

                self.change_stat("lust", 200, (int(modifier/10)))

            self.change_stat("inhibition", 60, (int(modifier/10)))
            self.likes[GirlB.tag] = likes + modifier

            return return_value

        def name_check(self, counter = 0):
            if self.petname == self.name:
                return False

            if self.taboo:
                counter = int(self.taboo/10)

            if self.petname in ("girl", "boo", "bae", "baby", "sweetie"):
                if approval_check(self, 500, "L", taboo_modifier=1,Alt=[[LauraX],600]):
                    self.change_stat("love", 80, 1)
                else:
                    self.change_stat("love", 50, -1)

                    return True
            elif self.petname in ("_sexy", "lover", "beloved"):
                if approval_check(self, 900, taboo_modifier=1,Alt=[[LauraX], 1100]):
                    self.change_stat("love", 80, 2)
                    self.change_stat("obedience", 80, 1)
                    self.change_stat("inhibition", 70, 1)
                else:
                    self.change_stat("love", 50, (-1-counter))
                    self.change_stat("obedience", 50, 1)
                    self.change_stat("inhibition", 20, -1)
                    return True
            elif self.petname == "slave":
                if approval_check(self, 800, "O", taboo_modifier=3,Alt=[[EmmaX,StormX],900]):
                    self.change_stat("lust", 90, (3+counter))
                    self.change_stat("obedience", 95, (2+counter))
                    self.change_stat("inhibition", 30, 1)
                    self.change_stat("inhibition", 70, 1)
                elif approval_check(self, 500, "O", taboo_modifier=3,Alt=[[EmmaX,StormX],600]):
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
                if approval_check(self, 1500, taboo_modifier=2,Alt=[[LauraX],800]):
                    self.change_stat("lust", 90, (3+counter))
                    self.change_stat("obedience", 95, (2+counter))
                    self.change_stat("inhibition", 30, 1)
                    self.change_stat("inhibition", 70, 1)
                elif approval_check(self, 1200, taboo_modifier=2,Alt=[[LauraX],650]):
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
                if approval_check(self, 500, "O", taboo_modifier=2) or approval_check(self, 500, "I", taboo_modifier=2,Alt=[[LauraX],400]):
                    self.change_stat("lust", 90, (4+counter))
                    self.change_stat("obedience", 95, (2+counter))
                    self.change_stat("inhibition", 40, 2)
                    self.change_stat("inhibition", 80, 1)
                elif approval_check(self, 300, "O", taboo_modifier=2) or approval_check(self, 300, "I", taboo_modifier=2,Alt=[[LauraX],200]):
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
                if approval_check(self, 600, "O", taboo_modifier=2,Alt=[[EmmaX],700]) or approval_check(self, 600, "I", taboo_modifier=2,Alt=[[LauraX],400]):
                    self.change_stat("lust", 90, 4)
                    self.change_stat("obedience", 95, 2)
                    self.change_stat("inhibition", 50, 2)
                    self.change_stat("inhibition", 80, 1)
                elif approval_check(self, 400, "O", taboo_modifier=2,Alt=[[EmmaX],500]) or approval_check(self, 400, "I", taboo_modifier=2):
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
                if approval_check(self, 1500, taboo_modifier=1,Alt=[[EmmaX], 1300]):
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
                if approval_check(self, 750, "O", taboo_modifier=1) or approval_check(self, 600, "I", taboo_modifier=1):
                    self.change_stat("lust", 90, 3)
                    self.change_stat("obedience", 95, 2)
                    self.change_stat("inhibition", 40, 2)
                    self.change_stat("inhibition", 80, 1)
                elif approval_check(self, 600, "O", taboo_modifier=1) or approval_check(self, 400, "I", taboo_modifier=1):
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
                if approval_check(self, 700, "O", taboo_modifier=2) or approval_check(self, 700, "I", taboo_modifier=1):
                    self.change_stat("lust", 90, 3)
                    self.change_stat("obedience", 95, 2)
                    self.change_stat("inhibition", 40, 2)
                    self.change_stat("inhibition", 85, 1)
                elif approval_check(self, 600, "O", taboo_modifier=2) or approval_check(self, 500, "I", taboo_modifier=1):
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
            elif self.petname in ["baby girl", "mommy"]:
                if approval_check(self, 1200, taboo_modifier=1):
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
                if approval_check(self, 600, "L", taboo_modifier=1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)

                    return True
            elif self.petname == "kitten":
                if approval_check(self, 600, "L", taboo_modifier=1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)

                    return True
            elif self.petname == "darling":
                if approval_check(self, 600, "L", taboo_modifier=1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)

                    return True
            elif self.petname == "Wolvie":
                if approval_check(self, 500, "I", taboo_modifier=1):
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

    def get_base_outfit(*items):
        outfit = {"buttplug": "",
            "face_tattoos": "", "face_piercings": "", "makeup": "", "gag": "",
            "face_inner_accessory": "", "hair": "", "face_outer_accessory": "",
            "tattoos": "", "piercings": "", "nipple_accessories": "", "rope": "",
            "bodysuit": "", "bra": "", "underwear": "",
            "hose": "", "bottom": "",
            "dress": "", "boots": "", "top": "",
            "neck": "", "gloves": "", "sleeves": "",
            "suspenders": "", "belt": "", "jacket": "", "cloak": "",
            "held_item": "",
            "shame": 0, "outfit_active": False}

        for item in items:
            outfit.update(item)

        return outfit
