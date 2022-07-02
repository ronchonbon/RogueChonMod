init python:

    class PlayerClass(object):
        def __init__(self):
            self.name = "Zero"

            self.sprite = None
            self.color = "green"

            self.location = "bg_entrance"
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

            self.focused_Girl = None
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

        def change_stat(self, flavor, check, update, greater_than = False):
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

            # sprite_layer = [background_characters (eg. teachers), midground (eg. pool mask), midground_characters (eg. students), foreground (eg. desks), foreground_characters (eg. Present), Player.focused_Girl, cover (eg. fog)]
            self.sprite_location = stage_center
            self.sprite_layer = 6

            self.remaining_actions = 3
            self.max_actions = 3

            self.pose = "full"

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
            self.eyes = "normal"
            self.mouth = "normal"
            self.brows = "normal"
            self.emotion = "normal"

            self.arm_pose = 1

            self.grool = 0
            self.wet = False
            self.spunk = {
                "hair": False, "face": False, "mouth": False, "chin": False,
                "breasts": False, "back": False, "belly": False, "hand": False,
                "pussy": False, "anus": False}

            self.to_do = []
            self.pubes_counter = 0

            self.action_counter = {}

            for action in all_actions:
                self.action_counter[action] = 0

            self.event_counter = {
                "orgasmed": 0, "caught": 0, "sleepover": 0, "ass_slapped": 0,
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

            self.Wardrobe = WardrobeClass()
            self.Outfit = self.Wardrobe.current_Outfit
            self.Clothes = self.Outfit.Clothes

            self.Outfit_schedule = [
                "first_casual",
                "second_casual",
                "first_casual",
                "second_casual",
                "first_casual",
                "second_casual",
                "first_casual"]

            self.todays_Outfit_name = self.Outfit_schedule[weekday]

            self.set_default_Outfits()
            self.change_Outfit("first_casual", instant = True)

            self.held_item = None

            if self.tag == "Rogue":
                self.voice = ch_r

                self.home = "bg_rogue"
                self.pubes = "_hairy"

                self.weekly_schedule = [
                    ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                    ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                    ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                    ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                    ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                    ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"],
                    ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"]]

                self.likes = {"Kitty": 600, "Emma": 500, "Laura": 500, "Jean": 200, "Storm": 600, "Jubes": 500, "Mystique": 0}

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

                self.weekly_schedule = [
                    ["bg_classroom", "bg_dangerroom", "bg_kitty", "bg_kitty"],
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

                self.weekly_schedule = [
                    ["bg_teacher", "bg_teacher", "bg_classroom", "bg_emma"],
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

                self.weekly_schedule = [
                    ["bg_pool", "bg_classroom", "bg_dangerroom", "bg_laura"],
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

                self.weekly_schedule = [
                    ["bg_classroom", "bg_classroom", "bg_dangerroom", "bg_jean"],
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

                self.weekly_schedule = [
                    ["bg_storm", "bg_dangerroom", "bg_dangerroom", "bg_storm"],
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

                self.weekly_schedule = [
                    ["bg_jubes", "bg_dangerroom", "bg_dangerroom", "bg_jubes"],
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

                self.weekly_schedule = [
                    ["bg_office", "bg_office", "bg_office", "bg_mystique"],
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

            shop_inventory.extend(["DL", "G", "A"])
            bedrooms.append(self.home)

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

            if (self.forced or "angry" in self.recent_history) and emotion in ["normal", "bemused", "sexy", "sly", "smile", "startled"]:
                emotion = "angry"
            elif self.event_counter["forced"] > 0 and emotion in ["normal", "bemused", "sexy", "sly", "smile", "startled"]:
                emotion = "sad"

            if emotion == "normal":
                self.mouth = "normal"
                self.brows = "normal"
                self.eyes = "normal"
            elif emotion == "angry":
                if self.tag == "Laura":
                    self.mouth = "kiss"
                else:
                    self.mouth = "sad"
                self.brows = "angry"
                self.eyes = "sexy"
            elif emotion == "bemused":
                if self.tag == "Emma":
                    self.mouth = "normal"
                else:
                    self.mouth = "lipbite"
                self.brows = "sad"
                self.eyes = "squint"
            elif emotion == "closed":
                if self.tag == "Rogue":
                    self.mouth = "lipbite"
                else:
                    self.mouth = "normal"
                self.brows = "sad"
                self.eyes = "closed"
            elif emotion == "confused":
                self.mouth = "kiss"
                self.brows = "confused"
                if self.tag == "Laura" or self.tag == "Emma":
                    self.eyes = "squint"
                else:
                    self.eyes = "surprised"
            elif emotion == "kiss":
                self.mouth = "kiss"
                if self.tag == "Laura" or self.tag == "Emma":
                    self.brows = "sad"
                else:
                    self.brows = "normal"
                self.eyes = "closed"
            elif emotion == "sad":
                self.mouth = "sad"
                self.brows = "sad"
                if self.tag == "Jean" or self.tag == "Jubes":
                    self.eyes = "normal"
                else:
                    self.eyes = "sexy"
            elif emotion == "sadside":
                self.mouth = "sad"
                self.brows = "sad"
                self.eyes = "side"
            elif emotion == "sexy":
                if self.tag == "Jean":
                    self.mouth = "smirk"
                else:
                    self.mouth = "lipbite"
                if self.tag == "Emma":
                    self.brows = "normal"
                    self.eyes = "squint"
                elif self.tag == "Laura":
                    self.brows = "sad"
                    self.eyes = "squint"
                else:
                    self.brows = "normal"
                    self.eyes = "sexy"
            elif emotion == "sly":
                self.brows = "normal"
                self.eyes = "squint"
                if self.tag == "Rogue":
                    self.mouth = "smile"
                if self.tag == "Laura":
                    if self.love >= 700:
                        self.mouth = "smile"
                    else:
                        self.mouth = "smirk"
                    self.brows = "confused"
                elif self.tag == "Kitty":
                    self.mouth = "smile"
                else:
                    self.mouth = "smirk"
            elif emotion == "smile":
                if self.tag == "Laura" and self.love < 700:
                    self.mouth = "smirk"
                else:
                    self.mouth = "smile"
                self.brows = "normal"
                self.eyes = "normal"
            elif emotion == "surprised":
                if self.tag == "Rogue" or self.tag == "Kitty":
                    self.mouth = "surprised"
                else:
                    self.mouth = "kiss"
                self.brows = "surprised"
                self.eyes = "surprised"
            elif emotion == "oh":
                self.mouth = "kiss"
                self.brows = "surprised"
                self.eyes = "surprised"
            elif emotion == "startled":
                self.mouth = "smile"
                self.brows = "surprised"
                self.eyes = "surprised"
            elif emotion == "down":
                if self.tag == "Rogue" or self.tag == "Kitty":
                    self.mouth = "surprised"
                else:
                    self.mouth = "sad"
                self.brows = "sad"
                self.eyes = "down"
            elif emotion == "perplexed":
                if self.tag == "Rogue":
                    self.mouth = "sad"
                    self.brows = "confused"
                else:
                    self.mouth = "smile"
                    self.brows = "sad"
                if self.tag == "Laura":
                    self.eyes = "surprised"
                else:
                    self.eyes = "normal"
            elif emotion == "sucking":
                self.mouth = "sucking"
                if self.tag == "Emma":
                    self.brows = "surprised"
                elif self.tag == "Laura":
                    self.brows = "sad"
                else:
                    self.brows = "normal"
                self.eyes = "closed"
            elif emotion == "tongue":
                self.mouth = "tongue"
                self.brows = "sad"
                if self.tag == "Laura":
                    self.eyes = "stunned"
                else:
                    self.eyes = "sexy"
            elif emotion == "manic":
                if self.tag == "Rogue":
                    self.mouth = "smile"
                elif self.tag == "Laura":
                    self.mouth = "lipbite"
                else:
                    self.mouth = "smile"
                self.brows = "sad"
                self.eyes = "manic"
                self.blushing = "_blush1"

            if blushing > 1:
                self.blushing = "_blush2"
            elif blushing:
                self.blushing = "_blush1"
            else:
                self.blushing = ""

            if manic:
                self.eyes = "manic"

            if mouth:
                self.mouth = mouth

            if eyes:
                self.eyes = eyes

            if brows:
                self.brows = brows

            return

        def set_default_faces(self):
            if self.lust >= 50 and approval_check(self, 1200):
                self.emotion = "sexy"
            elif self.addiction > 75:
                self.emotion = "manic"
            elif self.love >= self.obedience and self.love >= 500:
                self.emotion = "smile"
            elif self.inhibition >= self.obedience and self.inhibition >= 500:
                self.emotion = "smile"
            elif self.addiction > 50:
                self.emotion = "manic"
            elif self.love + self.obedience < 300:
                self.emotion = "angry"
            else:
                self.emotion = "normal"
            return

        def try_on(self, Clothing):
            self.Outfit.change_into(Clothing = Clothing)

            return

        def take_off(self, Clothing_type):
            self.Outfit.change_out_of(Clothing_type)

            return

        def give(self, Clothing):
            self.Wardrobe.add_Clothing(Clothing = Clothing)

            return

        def change_into(self, Clothing_name):
            if Clothing_name not in self.Wardrobe.Clothes.keys():
                renpy.say(self.voice, "I don't have a piece of clothing named [Clothing_name].")

                return

            self.Outfit.change_into(Clothing = self.Wardrobe.Clothes[Clothing_name])

            self.Wardrobe.temp_Outfit = copy.deepcopy(self.Outfit)

            return

        def change_out_of(self, Clothing_type):
            self.Outfit.change_out_of(Clothing_type = Clothing_type)

            self.Wardrobe.temp_Outfit = copy.deepcopy(self.Outfit)

            return

        def undress(self, instant = False):
            self.Outfit.undress(instant = instant)

            return

        def expose_breasts(self):
            for Clothing_type in reversed(self.Outfit.hide_breasts):
                if self.Clothes[Clothing_type].number_of_states > 2:
                    self.Clothes[Clothing_type].state += 2

                    renpy.pause(0.2)
                elif self.Clothes[Clothing_type].number_of_states == 1:
                    self.Clothes[Clothing_type].take_off()
                else:
                    self.Outfit.remove_Clothing(Clothing_type)

                    renpy.pause(0.2)

            return

        def expose_underwear(self):
            for Clothing_type in reversed(self.Outfit.hide_underwear):
                self.Clothes[Clothing_type].take_off()

                if self.Clothes[Clothing_type].state < 1:
                    self.Outfit.remove_Clothing(Clothing_type)

            return

        def expose_pussy(self):
            for Clothing_type in reversed(self.Outfit.hide_pussy):
                self.Clothes[Clothing_type].take_off()

                if self.Clothes[Clothing_type].state < 1:
                    self.Outfit.remove_Clothing(Clothing_type)

            return

        def fix_clothing(self):
            for Clothing_type in self.Outfit.removable():
                if self.Wardrobe.temp_Outfit.Clothes[Clothing_type] and not self.Clothes[Clothing_type]:
                    self.Wardrobe.temp_Outfit.Clothes[Clothing_type].state = self.Wardrobe.temp_Outfit.Clothes[Clothing_type].undressed_state

                    self.Outfit.add_Clothing(self.Wardrobe.temp_Outfit.Clothes[Clothing_type])

                    renpy.pause(0.2)

                if self.Clothes[Clothing_type].state > 0:
                    self.Clothes[Clothing_type].put_on()

            return

        def add_Outfit(self, Outfit):
            self.Wardrobe.add_Outfit(Outfit = Outfit)

            return

        def remove_Outfit(self, Outfit_name):
            self.Wardrobe.remove_Outfit(Outfit_name = Outfit_name)

            return

        def change_Outfit(self, Outfit_name = None, instant = False):
            if not Outfit_name:
                Outfit_name = self.todays_Outfit_name

            if Outfit_name not in self.Wardrobe.Outfits.keys():
                renpy.say(self.voice, "I don't have an outfit named [new_Outfit_name].")

                return

            if self.location not in ["bg_showerroom", "bg_pool"]:
                self.wet = False

            if any(self.spunk) and ("painted" not in self.daily_history or "cleaned" not in self.daily_history):
                for key in self.spunk.keys():
                    self.spunk[key] = False

            self.Wardrobe.change_Outfit(Outfit = self.Wardrobe.Outfits[Outfit_name], instant = instant)

            self.Outfit = self.Wardrobe.current_Outfit

            self.Clothes = self.Outfit.Clothes

            return

        def set_default_Outfits(self):
            first_casual = OutfitClass(name = "first_casual")
            second_casual = OutfitClass(name = "second_casual")
            gym_clothes = OutfitClass(name = "gym_clothes")
            swimwear = OutfitClass(name = "swimwear")
            sleepwear = OutfitClass(name = "sleepwear")
            shower = OutfitClass(name = "shower")
            nude = OutfitClass(name = "nude")

            if self.tag in ["Emma", "Storm"]:
                teacher = OutfitClass(name = "teacher")

            Halloween_costume = OutfitClass(name = "Halloween_costume")

            if self.tag == "Rogue":
                first_casual.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": black_panties(), "hose": black_tights(),
                    "skirt": black_skirt(),
                    "bra": black_tanktop(), "top": green_mesh_top(),
                    "neck": spiked_collar(), "gloves": black_gloves()})

                second_casual.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": black_panties(),
                    "pants": jeans(),
                    "bra": black_buttoned_tanktop(), "top": pink_top(),
                    "neck": spiked_collar(), "gloves": black_gloves()})

                gym_clothes.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": yellowgreen_shorts(),
                    "bra": yellowgreen_sports_bra(),
                    "gloves": black_gloves(),
                    "jacket": green_hoodie()})

                swimwear.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": green_bikini_bottoms(),
                    "bra": yellow_bikini_top()})

                sleepwear.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": green_panties(),
                    "bra": black_tanktop()})

                shower.update_Clothes({
                    "hair": Evolutions_hair(),
                    "top": green_towel()})

                Halloween_costume.update_Clothes({
                    "hair": Jill_hair(),
                    "underwear": black_panties(),
                    "skirt": black_skirt(),
                    "bra": blue_tubetop(),
                    "gloves": black_gloves(), "belt": white_sweater()})
            elif self.tag == "Kitty":
                first_casual.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": green_panties(),
                    "pants": blue_capris(),
                    "bra": yellow_cami(), "top": pink_top(),
                    "neck": gold_necklace()})

                second_casual.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": green_panties(),
                    "pants": black_jeans(),
                    "bra": pink_strapless_bra(), "top": red_shirt(),
                    "neck": star_necklace()})

                gym_clothes.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": green_panties(),
                    "bra": purple_sports_bra(),
                    "pants": yellow_shorts()})

                swimwear.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": blue_bikini_bottoms(),
                    "bra": blue_bikini_top(),
                    "skirt": blue_skirt()})

                sleepwear.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": green_panties(),
                    "bra": yellow_cami()})

                shower.update_Clothes({
                    "hair": Evolutions_hair(),
                    "top": pink_towel()})

                nude.update_Clothes({
                    "hair": Evolutions_hair()})

                Halloween_costume.update_Clothes({
                    "hair": Evolutions_hair(),
                    "underwear": pink_lace_panties(),
                    "skirt": Aerith_skirt(),
                    "bra": Aerith_corset(),
                    "neck": flower_necklace(),
                    "jacket": Aerith_jacket()})

            self.Wardrobe.Outfits.update({
                "first_casual": first_casual,
                "second_casual": second_casual,
                "gym_clothes": gym_clothes,
                "swimwear": swimwear,
                "sleepwear": sleepwear,
                "shower": shower,
                "nude": nude,
                "Halloween_costume": Halloween_costume})

            # if self.tag in ["Emma", "Storm"]:
            #     self.Wardrobe.Outfits.update({"teacher": teacher})

            for Outfit in self.Wardrobe.Outfits.values():
                for Clothing in Outfit.Clothes.values():
                    if Clothing:
                        self.Wardrobe.add_Clothing(Clothing)

            return











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
                if approval_check(self, 500, "L", taboo_modifier = 1,Alt=[[LauraX],600]):
                    self.change_stat("love", 80, 1)
                else:
                    self.change_stat("love", 50, -1)

                    return True
            elif self.petname in ("sexy", "lover", "beloved"):
                if approval_check(self, 900, taboo_modifier = 1,Alt=[[LauraX], 1100]):
                    self.change_stat("love", 80, 2)
                    self.change_stat("obedience", 80, 1)
                    self.change_stat("inhibition", 70, 1)
                else:
                    self.change_stat("love", 50, (-1-counter))
                    self.change_stat("obedience", 50, 1)
                    self.change_stat("inhibition", 20, -1)
                    return True
            elif self.petname == "slave":
                if approval_check(self, 800, "O", taboo_modifier = 3,Alt=[[EmmaX,StormX],900]):
                    self.change_stat("lust", 90, (3+counter))
                    self.change_stat("obedience", 95, (2+counter))
                    self.change_stat("inhibition", 30, 1)
                    self.change_stat("inhibition", 70, 1)
                elif approval_check(self, 500, "O", taboo_modifier = 3,Alt=[[EmmaX,StormX],600]):
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
                elif approval_check(self, 300, "O", taboo_modifier=2) or approval_check(self, 300, "I", taboo_modifier=2,Alt=[[LauraX], 200]):
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
                if approval_check(self, 1500, taboo_modifier = 1,Alt=[[EmmaX], 1300]):
                    self.change_stat("obedience", 80, 1)
                    self.change_stat("obedience", 50, 2)
                    self.change_stat("inhibition", 70, 1,Alt=[[EmmaX],70, 2])
                    self.change_stat("inhibition", 30, 2,Alt=[[KittyX],60,3])
                else:
                    self.change_stat("love", 200, (-2-counter))
                    self.change_stat("love", 50, (-1-counter))
                    self.change_stat("obedience", 50, 1)
                    self.change_stat("inhibition", 20, -1)

                    return True
            elif self.petname == "sex friend":
                if approval_check(self, 750, "O", taboo_modifier = 1) or approval_check(self, 600, "I", taboo_modifier = 1):
                    self.change_stat("lust", 90, 3)
                    self.change_stat("obedience", 95, 2)
                    self.change_stat("inhibition", 40, 2)
                    self.change_stat("inhibition", 80, 1)
                elif approval_check(self, 600, "O", taboo_modifier = 1) or approval_check(self, 400, "I", taboo_modifier = 1):
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
                if approval_check(self, 700, "O", taboo_modifier=2) or approval_check(self, 700, "I", taboo_modifier = 1):
                    self.change_stat("lust", 90, 3)
                    self.change_stat("obedience", 95, 2)
                    self.change_stat("inhibition", 40, 2)
                    self.change_stat("inhibition", 85, 1)
                elif approval_check(self, 600, "O", taboo_modifier=2) or approval_check(self, 500, "I", taboo_modifier = 1):
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
                if approval_check(self, 1200, taboo_modifier = 1):
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
                if approval_check(self, 600, "L", taboo_modifier = 1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)

                    return True
            elif self.petname == "kitten":
                if approval_check(self, 600, "L", taboo_modifier = 1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)

                    return True
            elif self.petname == "darling":
                if approval_check(self, 600, "L", taboo_modifier = 1):
                    self.change_stat("love", 80, 2)
                else:
                    self.change_stat("love", 50, -1)

                    return True
            elif self.petname == "Wolvie":
                if approval_check(self, 500, "I", taboo_modifier = 1):
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
                self.eyes = "closed"
                if self.tag == "Emma":
                    self.mouth = "kiss"
                elif self.action_counter["kiss"] >= 10 and self.inhibition >= 300:
                    self.mouth = "sucking"
                elif self.action_counter["kiss"] > 1 and self.addiction >= 50:
                    self.mouth = "sucking"
                else:
                    self.mouth = "kiss"
            else:
                if self.lust >= 90:
                    self.eyes = "closed"
                    self.brows = "sad"
                    self.mouth = "surprised"
                elif self.lust >= 70 or extreme:
                    self.eyes = "sexy"
                    self.brows = "sad"
                    self.mouth = "lipbite"
                elif self.lust >= 50:
                    if self.tag == "Emma" or self.tag == "Laura":
                        self.eyes = "squint"
                    else:
                        self.eyes = "sexy"
                    self.brows = "sad"
                    self.mouth = "lipbite"
                elif self.lust >= 30:
                    self.eyes = "sexy"
                    self.brows = "normal"
                    if self.tag == "Emma" or self.tag == "Laura":
                        self.mouth = "smirk"
                    else:
                        self.mouth = "kiss"
                else:
                    self.eyes = "sexy"
                    self.brows = "normal"
                    if self.tag == "Emma" or self.tag == "Laura":
                        self.mouth = "smirk"
                    else:
                        self.mouth = "normal"
                if self.tag == "Laura" and self.lust < 50 and not extreme and not approval_check(self, 1000):
                    self.eyes = "side"

            if Partner == self and second_girl_main_action in ["suck_breasts", "eat_pussy", "eat_ass", "blowjob"]:
                self.mouth = "tongue"
            elif self.secondary_action in ["suck_breasts", "eat_pussy", "eat_ass"]:
                self.mouth = "tongue"

            if self.session_orgasms >= 10:
                self.eyes = "stunned"
                self.mouth = "tongue"

            if not self.used_to_anal:
                if Partner != self and (Player.primary_action == "anal" or Player.primary_action == "dildo_ass" or self.secondary_action == "dildo_ass"):
                    self.eyes = "closed"
                    self.brows = "angry"

            if "unseen" in self.recent_history:
                self.eyes = "closed"

            if Partner and self != Partner:
                Partner.lust_face()

            return

        def set_default_outfits(self):
            if self.tag == "Emma":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "wavy",
                    "bra": "corset", "underwear": "white_panties",
                    "bottom": "white_pants",
                    "neck": "choker",
                    "jacket": "jacket",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "wavy",
                    "bra": "corset", "underwear": "white_panties",
                    "bottom": "skirt",
                    "boots": "thigh_boots",
                    "neck": "choker",
                    "shame": 5, "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "wavy",
                    "bra": "sports_bra", "underwear": "sports_panties",
                    "bottom": "white_pants",
                    "shame": 10})

                self.sleepwear = get_base_outfit(
                    {"hair": "wavy",
                    "bra": "corset", "underwear": "white_panties",
                    "shame": 25})

                self.swimwear = get_base_outfit(
                    {"hair": "wavy",
                    "bra": "bikini_top", "underwear": "bikini_bottoms",
                    "shame": 25})

                self.halloween_costume = get_base_outfit(
                    {"hair": "wavy",
                    "face_outer_accessory": "hat",
                    "underwear": "lace_panties",
                    "hose": "stockings_and_garterbelt", "bottom": "dress_skirt",
                    "top": "dress_top",
                    "neck": "choker",
                    "outfit_active": 2})

                self.domme_outfit = get_base_outfit(
                    {"hair": "wavy",
                    "bodysuit": "domme_suit",
                    "boots": "domme_suit",
                    "neck": "spiked_collar", "gloves": "spiked_bracelets",
                    "held_item": "whip",
                    "outfit_active": 2})

                self.nude["hair"] = "wavy"
            elif self.tag == "Laura":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "long",
                    "bra": "leather_bra", "underwear": "leather_panties",
                    "bottom": "leather_pants",
                    "neck": "leash_choker",
                    "gloves": "wrists",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "long",
                    "bra": "leather_bra", "underwear": "leather_panties",
                    "bottom": "skirt",
                    "neck": "leash_choker",
                    "gloves": "wrists",
                    "jacket": "jacket",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "long",
                    "bra": "leather_bra", "underwear": "leather_panties",
                    "bottom": "leather_pants",
                    "gloves": "wrists"})

                self.sleepwear = get_base_outfit(
                    {"hair": "long",
                    "bra": "leather_bra", "underwear": "leather_panties",
                    "shame": 20})

                self.swimwear = get_base_outfit(
                    {"hair": "long",
                    "bra": "bikini_top", "underwear": "bikini_bottoms"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "long",
                    "bra": "white_tank", "underwear": "leather_panties",
                    "hose": "black_stockings", "bottom": "cosplay_skirt",
                    "neck": "leash_choker",
                    "gloves": "gloves",
                    "suspenders": "suspenders",
                    "outfit_active": 2})

                self.nude["hair"] = "long"
            elif self.tag == "Jean":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "short",
                    "bra": "green_bra", "underwear": "green_panties",
                    "bottom": "khaki_pants",
                    "top": "pink_shirt",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "short",
                    "bra": "green_bra", "underwear": "green_panties",
                    "bottom": "skirt",
                    "top": "green_shirt",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "short",
                    "bra": "sports_bra", "underwear": "green_panties",
                    "bottom": "yoga_pants"})

                self.sleepwear = get_base_outfit(
                    {"hair": "short",
                    "bra": "green_bra", "underwear": "green_panties",
                    "top": "pink_shirt"})

                self.swimwear = get_base_outfit(
                    {"hair": "short",
                    "bra": "bikini_top", "underwear": "bikini_bottoms"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "pony",
                    "bra": "green_bra", "underwear": "green_panties",
                    "bottom": "shorts",
                    "top": "yellow_shirt",
                    "suspenders": "suspenders",
                    "outfit_active": 2})

                self.bondage_outfit = get_base_outfit(
                    {"hair": "short",
                    "nipple_accessories": "nipple_pegs", "rope": "harness",
                    "held_item": "hitachi",
                    "shame": 100, "outfit_active": 2})

                self.nude["hair"] = "short"
            elif self.tag == "Storm":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "long",
                    "bra": "black_bra", "underwear": "white_panties",
                    "bottom": "skirt",
                    "top": "white_shirt",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "long",
                    "bra": "sports_bra", "underwear": "white_panties",
                    "bottom": "black_jeans",
                    "jacket": "jacket",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "long",
                    "bra": "sports_bra", "underwear": "white_panties",
                    "bottom": "yoga_pants",
                    "shame": 10})

                self.sleepwear = get_base_outfit(
                    {"hair": "long",
                    "underwear": "white_panties",
                    "top": "white_shirt",
                    "shame": 25})

                self.swimwear = get_base_outfit(
                    {"hair": "long",
                    "bra": "bikini_top", "underwear": "bikini_bottoms",
                    "top": "white_shirt"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "short",
                    "bra": "cosplay_bra", "underwear": "cosplay_panties",
                    "neck": "ring_necklace",
                    "boots": "ring_anklets",
                    "sleeves": "ring_armlets",
                    "outfit_active": 2})

                self.nude["hair"] = "long"
            elif self.tag == "Jubes":
                self.first_casual_outfit = get_base_outfit(
                    {"hair": "short", "face_outer_accessory": "shades",
                    "bra": "sports_bra", "underwear": "blue_panties",
                    "bottom": "shorts",
                    "top": "red_shirt",
                    "jacket": "jacket",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"hair": "short", "face_outer_accessory": "shades",
                    "bra": "sports_bra", "underwear": "blue_panties",
                    "bottom": "leather_pants",
                    "top": "black_shirt",
                    "jacket": "jacket",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"hair": "short",
                    "bra": "sports_bra", "underwear": "blue_panties",
                    "bottom": "leather_pants",
                    "top": "black_shirt",
                    "shame": 10})

                self.sleepwear = get_base_outfit(
                    {"hair": "short",
                    "bra": "sports_bra", "underwear": "blue_panties",
                    "shame": 25})

                self.swimwear = get_base_outfit(
                    {"hair": "short", "face_outer_accessory": "shades",
                    "bra": "bikini_top", "underwear": "bikini_bottoms"})

                self.halloween_costume = get_base_outfit(
                    {"hair": "short", "face_outer_accessory": "shades",
                    "bra": "sports_bra", "underwear": "blue_panties",
                    "bottom": "leather_pants",
                    "top": "black_shirt",
                    "jacket": "jacket",
                    "outfit_active": 2})

                self.nude["hair"] = "short"
            elif self.tag == "Mystique":
                self.first_casual_outfit = get_base_outfit(
                    {"face_inner_accessory": "glasses", "hair": "short",
                    "bra": "black_bra", "underwear": "black_panties",
                    "bottom": "skirt",
                    "top": "purple_shirt",
                    "jacket": "jacket",
                    "outfit_active": 2})

                self.second_casual_outfit = get_base_outfit(
                    {"face_inner_accessory": "glasses", "hair": "short",
                    "bra": "black_bra", "underwear": "black_panties",
                    "bottom": "skirt",
                    "top": "purple_shirt",
                    "jacket": "jacket",
                    "outfit_active": 2})

                self.gym_clothes = get_base_outfit(
                    {"face_inner_accessory": "", "hair": "short",
                    "bra": "black_bra", "underwear": "black_panties",
                    "bottom": "skirt",
                    "top": "purple_shirt",
                    "jacket": "",
                    "outfit_active": 2})

                self.sleepwear = get_base_outfit(
                    {"hair": "short",
                    "bra": "black_bra", "underwear": "black_panties",
                    "shame": 25})

                self.swimwear = get_base_outfit(
                    {"hair": "short",
                    "bra": "black_bra", "underwear": "black_panties"})

                self.halloween_costume = get_base_outfit(
                    {"face_inner_accessory": "glasses", "hair": "short",
                    "bra": "black_bra", "underwear": "black_panties",
                    "bottom": "skirt",
                    "top": "purple_shirt",
                    "jacket": "jacket",
                    "outfit_active": 2})

                self.supervillain = get_base_outfit(
                    {"hair": "long", "face_outer_accessory": "skull",
                    "dress": "white_dress", "boots": "thigh_boots",
                    "belt": "skull_belt", "gloves": "gloves"})

                self.nude["hair"] = "short"

            return
