init python:

    import copy

    class PlayerClass(object):
        def __init__(self, name, color):
            self.name = name
            self.color = color

            self.sprite = False

            self.naked = False
            self.cock_out = False
            self.cock_wet = False
            self.spunk = False

            self.destination = "bg_entrance"
            self.location = "bg_entrance"
            self.traveling = False

            self.climax = 0

            self.semen = 3
            self.max_semen = 3

            self.focused_Girl = None
            self.Phonebook = []
            self.Party = []
            self.Keys = []
            self.Harem = []

            self.level = 1
            self.XP = 0
            self.XP_goal = 100
            self.stat_points = 0

            self.SEXP = 0

            self.reputation = 600

            self.income = 12
            self.cash = 20

            self.inventory = []

            self.primary_Action = ActionClass(None, None)
            self.secondary_Action = ActionClass(None, None)

            self.History = HistoryClass(default = False)
            self.recent_History = self.History.recent
            self.daily_History = self.History.daily
            self.permanent_History = self.History.permanent

            self.voice = ch_p
            self.text = ch_p_nvl

    class GirlClass(object):
        def __init__(self, name, love, obedience, inhibition, lust):
            self.name = name
            self.tag = name
            self.names = [name]

            self.love = love
            self.obedience = obedience
            self.inhibition = inhibition

            self.lust = lust

            self.addiction = 0
            self.addiction_rate = 0

            # 0 = happy, 9 = furious
            self.mood = 0

            self.blushing = ""
            self.eyes = "normal"
            self.mouth = "normal"
            self.brows = "normal"
            self.emotion = "normal"

            self.arm_pose = 1

            self.grool = 0
            self.spunk = {
                "hair": False, "face": False, "mouth": False, "chin": False,
                "breasts": False, "back": False, "belly": False, "hand": False,
                "pussy": False, "anus": False}
            self.wet = False

            self.held_item = None

            # sprite_layer = [background_characters (eg. teachers), midground (eg. pool mask), midground_characters (eg. students), foreground (eg. desks), foreground_characters (eg. Present), Player.focused_Girl, cover (eg. fog)]
            self.sprite_location = stage_center
            self.sprite_layer = 6

            self.destination = "hold"
            self.location = "hold"
            self.teaching = False

            self.remaining_Actions = 3
            self.max_Actions = 3

            self.level = 1
            self.XP = 0
            self.XP_goal = 100
            self.stat_points = 0
            self.SEXP = 0

            self.reputation = 600

            self.History = HistoryClass()
            self.recent_History = self.History.recent
            self.daily_History = self.History.daily
            self.permanent_History = self.History.permanent

            self.Wardrobe = WardrobeClass()
            self.Outfit = self.Wardrobe.current_Outfit
            self.Clothes = self.Outfit.Clothes

            self.primary_Action = ActionClass(None, None)
            self.secondary_Action = ActionClass(None, None)

            self.petname = self.name
            self.petnames = [self.name]

            if self.tag == "Rogue":
                self.voice = ch_r
                self.text = ch_r_nvl

                self.pubes = "_hairy"

                self.home = "bg_rogue"

                self.likes = {"Kitty": 600, "Emma": 500, "Laura": 500, "Jean": 200, "Storm": 600, "Jubes": 500, "Mystique": 0}

                self.used_to_anal = 0

                self.player_petname = "Sugar"
                self.player_petnames = [self.player_petname, Player.name]
            elif self.tag == "Kitty":
                self.voice = ch_k
                self.text = ch_k_nvl

                self.pubes = "_hairy"

                self.home = "bg_kitty"

                self.like = ", like, "
                self.Like = "Like, "

                self.likes = {"Rogue": 600, "Emma": 500, "Laura": 500, "Jean": 300, "Storm": 600, "Jubes": 600, "Mystique": 0}

                self.used_to_anal = 0

                self.player_petname = Player.name[:1]
                self.player_petnames = ["sweetie", self.player_petname, Player.name]
            elif self.tag == "Emma":
                self.voice = ch_e
                self.text = ch_e_nvl

                self.pubes = ""

                self.home = "bg_emma"

                self.diamond = False

                self.likes = {"Rogue": 500, "Kitty": 500, "Laura": 500, "Jean": 100, "Storm": 500, "Jubes": 500, "Mystique": 0}

                self.used_to_anal = 1

                last_name = get_last_name(Player)

                self.player_petname = "Mr. " + last_name
                self.player_petnames = ["young man", self.player_petname, Player.name]
            elif self.tag == "Laura":
                self.voice = ch_l
                self.text = ch_l_nvl

                self.pubes = "_hairy"

                self.home = "bg_laura"

                self.claws = False

                self.likes = {"Rogue": 500, "Kitty": 500, "Emma": 500, "Jean": 300, "Storm": 500, "Jubes": 600, "Mystique": 0}

                self.used_to_anal = 1

                self.player_petname = Player.name
                self.player_petnames = ["guy", self.player_petname]
            elif self.tag == "Jean":
                self.voice = ch_j
                self.text = ch_j_nvl

                self.pubes = "_hairy"

                self.home = "bg_jean"

                self.likes = {"Rogue": 500, "Kitty": 500, "Emma": 300, "Laura": 500, "Storm": 300, "Jubes": 300, "Mystique": 0}

                self.used_to_anal = 0

                self.player_petname = "um. . ."
                self.player_petnames = [self.player_petname, Player.name]
            elif self.tag == "Storm":
                self.voice = ch_s
                self.text = ch_s_nvl

                self.pubes = "_hairy"

                self.home = "bg_storm"

                self.likes = {"Rogue": 500, "Kitty": 600, "Emma": 400, "Laura": 500, "Jean": 300, "Jubes": 500, "Mystique": 0}

                self.used_to_anal = 0

                self.player_petname = Player.name
                self.player_petnames = [self.player_petname]
            elif self.tag == "Jubes":
                self.voice = ch_v
                self.text = ch_v_nvl

                self.pubes = "_hairy"

                self.home = "bg_jubes"

                self.likes = {"Rogue": 500, "Kitty": 600, "Emma": 500, "Laura": 600, "Jean": 300, "Storm": 500, "Mystique": 0}

                self.used_to_anal = 0

                self.player_petname = "Bro"
                self.player_petnames = [self.player_petname, Player.name]
            elif self.tag == "Mystique":
                self.voice = ch_m
                self.text = ch_m_nvl

                self.pubes = ""

                self.home = "bg_mystique"

                self.disguise = "Raven"
                self.disguise_Outfit = copy.deepcopy(self.Outfit)
                self.disguise_Clothes = self.disguise_Outfit.Clothes

                self.likes = {"Rogue": 0, "Kitty": 0, "Emma": 0, "Laura": 0, "Jean": 0, "Storm": 0, "Jubes": 0}

                self.used_to_anal = 1

                last_name = get_last_name(Player)

                self.player_petname = "Mr. " + last_name
                self.player_petnames = [self.player_petname, Player.name]

            bedrooms.append(self.home)

            all_Girls.append(self)

            self.default_Outfits()

        def change_face(self, emotion = None, blushing = 0, manic = False, mouth = None, eyes = None, brows = None):
            emotion = self.default_emotion() if not emotion else emotion

            if self.mood > 4 and emotion in ["normal", "bemused", "sexy", "sly", "smile", "startled"]:
                emotion = "angry"
            elif self.daily_History["forced"] > 0 and emotion in ["normal", "bemused", "sexy", "sly", "smile", "startled"]:
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

        def default_emotion(self):
            if self.lust >= 50 and approval_check(self, 1200):
                emotion = "sexy"
            elif self.addiction > 75:
                emotion = "manic"
            elif self.love >= self.obedience and self.love >= 500:
                emotion = "smile"
            elif self.inhibition >= self.obedience and self.inhibition >= 500:
                emotion = "smile"
            elif self.addiction > 50:
                emotion = "manic"
            elif self.love + self.obedience < 300:
                emotion = "angry"
            else:
                emotion = "normal"

            return emotion

        def set_location(self):
            self.location = None

            if time_index < 3 and weekday < 5:
                if self.tag == "Emma":
                    if time_index == 0 and weekday in [1, 3]:
                        self.location = "bg_teacher"
                    elif time_index == 1 and weekday in [0, 2, 4]:
                        self.location = "bg_teacher"
                    elif time_index == 2 and weekday in [0, 2, 4]:
                        self.location = "bg_classroom"
                elif self.tag == "Storm":
                    if time_index == 0 and weekday in [0, 2, 4]:
                        self.location = "bg_teacher"
                    elif time_index == 1 and weekday in [1, 3]:
                        self.location = "bg_teacher"
                    elif time_index == 2 and weekday in [1, 3]:
                        self.location = "bg_classroom"
                elif self.tag == "Mystique":
                    if time_index < 2:
                        self.location = "bg_office"

            if self.location:
                return

            possible_locations = []

            possible_locations.append(self.home)

            if time_index < 2 and weekday < 5:
                possible_locations.append("bg_classroom")

            if time_index < 3:
                possible_locations.append("bg_campus")
                possible_locations.append("bg_dangerroom")
                possible_locations.append("bg_mall")

            if time_index < 3 and weekday > 4:
                possible_locations.append("bg_pool")
            elif time_index in [1, 2]:
                possible_locations.append("bg_pool")

            renpy.random.shuffle(possible_locations)

            self.location = possible_locations[0]

            return

        def try_on(self, Clothing):
            self.Outfit.change_into(Clothing)

            return

        def take_off(self, type):
            self.Outfit.change_out_of(type)

            return

        def give(self, Clothing):
            self.Wardrobe.add_Clothing(Clothing)

            return

        def change_into(self, Clothing_name):
            if Clothing_name not in self.Wardrobe.Clothes.keys():
                self.voice("I don't have a piece of clothing named [Clothing_name].")

                return

            self.Outfit.change_into(self.Wardrobe.Clothes[Clothing_name])

            self.Wardrobe.temp_Outfit = copy.deepcopy(self.Outfit)

            return

        def change_out_of(self, type):
            self.Outfit.change_out_of(type)

            self.Wardrobe.temp_Outfit = copy.deepcopy(self.Outfit)

            return

        def undress(self, instant = False):
            self.Outfit.undress(instant = instant)

            return

        def expose_breasts(self):
            for type in reversed(self.Outfit.hide_breasts):
                if self.Clothes[type].number_of_states > 2:
                    self.Clothes[type].state += 2

                    renpy.pause(0.1)
                elif self.Clothes[type].number_of_states == 1:
                    self.Clothes[type].take_off()
                else:
                    self.Outfit.remove_Clothing(type)

                    renpy.pause(0.1)

            return

        def expose_underwear(self):
            for type in reversed(self.Outfit.hide_underwear):
                self.Clothes[type].take_off()

                if self.Clothes[type].state < 1:
                    self.Outfit.remove_Clothing(type)

            return

        def expose_pussy(self):
            for type in reversed(self.Outfit.hide_pussy):
                self.Clothes[type].take_off()

                if self.Clothes[type].state < 1:
                    self.Outfit.remove_Clothing(type)

            return

        def fix_clothing(self):
            for type in removable_Clothing_types:
                if self.Wardrobe.temp_Outfit.Clothes[type] and not self.Clothes[type]:
                    self.Wardrobe.temp_Outfit.Clothes[type].state = self.Wardrobe.temp_Outfit.Clothes[type].undressed_state

                    self.Outfit.add_Clothing(self.Wardrobe.temp_Outfit.Clothes[type])

                    renpy.pause(0.2)

                if self.Clothes[type] and self.Clothes[type].state > 0:
                    self.Clothes[type].put_on()

            return

        def add_Outfit(self, Outfit):
            self.Wardrobe.add_Outfit(Outfit)

            return

        def remove_Outfit(self, name):
            self.Wardrobe.remove_Outfit(name)

            return

        def change_Outfit(self, name = None, instant = False):
            if not name:
                name = self.Wardrobe.public_Outfit.name

            if name not in self.Wardrobe.Outfits.keys():
                self.voice("I don't have an outfit named [name].")

                return

            if self.location not in ["bg_shower", "bg_pool"]:
                self.wet = False

            for key in self.spunk.keys():
                self.spunk[key] = False

            self.Wardrobe.change_Outfit(self.Wardrobe.Outfits[name], instant = instant)
            self.Outfit = self.Wardrobe.current_Outfit
            self.Clothes = self.Outfit.Clothes

            if self.tag == "Mystique":
                self.disguise_Outfit = copy.deepcopy(self.Outfit)
                self.disguise_Clothes = self.disguise_Outfit.Clothes

            return

        def choose_Outfits(self):
            self.Wardrobe.choose_Outfits()

            return

        def default_Outfits(self):
            default = OutfitClass("default", wear_in_public = True, wear_in_private = True)
            casual = OutfitClass("casual", wear_in_public = True, wear_in_private = True)
            gym_clothes = OutfitClass("gym_clothes", activewear = True)
            pajamas = OutfitClass("pajamas", sleepwear = True)
            shower = OutfitClass("shower")

            if self.tag not in ["Jubes", "Mystique"]:
                Halloween_costume = OutfitClass("Halloween_costume")

            if self.tag == "Mystique":
                villain = OutfitClass("villain")
            # else:
            #     hero = OutfitClass("hero", wear_in_public = True, wear_in_private = True, activewear = True)

            if self.tag == "Rogue":
                default.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": black_panties(self), "hose": black_tights(self),
                    "skirt": black_skirt(self),
                    "bra": black_tanktop(self), "top": green_mesh_top(self),
                    "neck": spiked_collar(self), "gloves": black_gloves(self)})

                casual.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": black_panties(self),
                    "pants": jeans(self),
                    "bra": black_buttoned_tanktop(self), "top": pink_top(self),
                    "neck": spiked_collar(self), "gloves": black_gloves(self)})

                gym_clothes.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": yellowgreen_shorts(self),
                    "bra": yellowgreen_sports_bra(self),
                    "gloves": black_gloves(self),
                    "jacket": green_hoodie(self)})

                pajamas.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": green_panties(self),
                    "bra": black_tanktop(self)})

                shower.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "top": green_towel(self)})

                Halloween_costume.update_Clothes({
                    "hair": Jill_hair(self),
                    "underwear": black_panties(self),
                    "skirt": black_skirt(self),
                    "bra": blue_tubetop(self),
                    "gloves": black_gloves(self), "belt": white_sweater(self)})
            elif self.tag == "Kitty":
                default.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": green_panties(self),
                    "pants": blue_capris(self),
                    "bra": yellow_cami(self), "top": pink_top(self),
                    "neck": gold_necklace(self)})

                casual.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": green_panties(self),
                    "pants": black_jeans(self),
                    "bra": pink_strapless_bra(self), "top": red_shirt(self),
                    "neck": star_necklace(self)})

                gym_clothes.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": green_panties(self),
                    "bra": purple_sports_bra(self),
                    "pants": yellow_shorts(self)})

                pajamas.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": green_panties(self),
                    "bra": yellow_cami(self)})

                shower.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "top": pink_towel(self)})

                Halloween_costume.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": pink_lace_panties(self),
                    "skirt": Aerith_skirt(self),
                    "bra": Aerith_corset(self),
                    "neck": flower_necklace(self),
                    "jacket": Aerith_jacket(self)})
            elif self.tag == "Emma":
                default.update_Clothes({
                    "hair": wavy_hair(self),
                    "underwear": white_panties(self),
                    "pants": white_pants(self),
                    "bra": white_corset(self),
                    "neck": white_choker(self),
                    "jacket": white_jacket(self)})

                casual.update_Clothes({
                    "hair": wavy_hair(self),
                    "underwear": white_panties(self),
                    "pants": white_shorts(self), "boots": white_boots(self),
                    "bra": white_corset(self),
                    "neck": white_choker(self),
                    "cloak": white_cape(self)})

                gym_clothes.update_Clothes({
                    "hair": wavy_hair(self),
                    "underwear": white_sports_panties(self),
                    "bra": white_sports_bra(self),
                    "pants": white_pants(self)})

                pajamas.update_Clothes({
                    "hair": wavy_hair(self),
                    "underwear": white_panties(self),
                    "bra": white_corset(self)})

                shower.update_Clothes({
                    "hair": wavy_hair(self),
                    "top": white_towel(self)})

                Halloween_costume.update_Clothes({
                    "hair": wavy_hair(self),
                    "face_outer_accessory": Dimitrescu_hat(self),
                    "underwear": white_panties(self), "hose": white_stockings_and_garterbelt(self),
                    "skirt": Dimitrescu_skirt(self),
                    "top": Dimitrescu_top(self),
                    "neck": white_choker(self)})
            elif self.tag == "Laura":
                default.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": leather_panties(self),
                    "pants": leather_pants(self),
                    "bra": leather_bra(self),
                    "neck": leash_choker(self), "gloves": black_wristbands(self)})

                casual.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": leather_panties(self),
                    "skirt": black_belty_skirt(self),
                    "bra": leather_bra(self),
                    "neck": leash_choker(self), "gloves": black_wristbands(self),
                    "jacket": grey_jacket(self)})

                gym_clothes.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": leather_panties(self),
                    "bra": leather_bra(self),
                    "gloves": black_wristbands(self)})

                pajamas.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": leather_panties(self),
                    "bra": leather_bra(self)})

                shower.update_Clothes({
                    "hair": long_hair(self),
                    "top": yellow_towel(self)})

                Halloween_costume.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": leather_panties(self), "hose": black_stockings(self),
                    "skirt": black_skirt(self),
                    "bra": white_tanktop(self),
                    "neck": leash_choker(self), "gloves": Tifa_gloves(self), "suspenders": Tifa_suspenders(self)})
            elif self.tag == "Jean":
                default.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": green_panties(self),
                    "pants": khaki_pants(self),
                    "bra": green_bra(self), "top": pink_shirt(self)})

                casual.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": green_panties(self),
                    "skirt": green_skirt(self),
                    "bra": green_bra(self), "top": green_shirt(self)})

                gym_clothes.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": green_panties(self),
                    "pants": green_yoga_pants(self),
                    "bra": blackyellow_sports_bra(self)})

                pajamas.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": green_panties(self),
                    "bra": green_bra(self), "top": pink_shirt(self)})

                shower.update_Clothes({
                    "hair": long_hair(self),
                    "top": red_towel(self)})

                Halloween_costume.update_Clothes({
                    "hair": ponytail(self),
                    "underwear": green_bra(self),
                    "pants": blue_shorts(self),
                    "bra": green_bra(self), "top": yellow_shirt(self),
                    "suspenders": Misty_suspenders(self)})
            elif self.tag == "Storm":
                default.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": white_panties(self),
                    "skirt": purple_skirt(self),
                    "bra": black_bra(self), "top": white_shirt(self)})

                casual.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": white_panties(self),
                    "pants": black_jeans(self),
                    "bra": black_sports_bra(self),
                    "jacket": black_jacket(self)})

                gym_clothes.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": white_panties(self),
                    "pants": white_yoga_pants(self),
                    "bra": black_sports_bra(self)})

                pajamas.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": white_panties(self),
                    "top": white_shirt(self)})

                shower.update_Clothes({
                    "hair": wavy_hair(self), "face_outer_accessory": head_towel(self)})

                Halloween_costume.update_Clothes({
                    "hair": short_hair(self),
                    "underwear": Elena_panties(self),
                    "boots": ring_anklets(self),
                    "bra": Elena_bra(self),
                    "neck": ring_necklace(self), "sleeves": ring_armlets(self)})
            elif self.tag == "Jubes":
                default.update_Clothes({
                    "hair": short_hair(self), "face_outer_accessory": pink_shades(self),
                    "underwear": blue_panties(self),
                    "pants": jean_shorts(self),
                    "bra": blue_sports_bra(self), "top": red_shirt(self),
                    "jacket": yellow_jacket(self)})

                casual.update_Clothes({
                    "hair": short_hair(self), "face_outer_accessory": pink_shades(self),
                    "underwear": blue_panties(self),
                    "pants": leather_pants(self),
                    "bra": blue_sports_bra(self), "top": black_shirt(self),
                    "jacket": yellow_jacket(self)})

                gym_clothes.update_Clothes({
                    "hair": short_hair(self),
                    "underwear": blue_panties(self),
                    "pants": leather_pants(self),
                    "bra": blue_sports_bra(self), "top": black_shirt(self)})

                pajamas.update_Clothes({
                    "hair": short_hair(self),
                    "underwear": blue_panties(self),
                    "bra": blue_sports_bra(self)})

                shower.update_Clothes({
                    "hair": short_hair(self),
                    "top": yellow_towel(self)})
            elif self.tag == "Mystique":
                default.update_Clothes({
                    "face_inner_accessory": black_glasses(self), "hair": short_hair(self),
                    "underwear": black_panties(self), "hose": brown_pantyhose(self),
                    "skirt": grey_skirt(self),
                    "bra": black_bra(self), "top": purple_shirt(self),
                    "jacket": grey_jacket(self)})

                casual.update_Clothes({
                    "face_inner_accessory": black_glasses(self), "hair": short_hair(self),
                    "underwear": black_panties(self), "hose": brown_pantyhose(self),
                    "skirt": grey_skirt(self),
                    "bra": black_bra(self), "top": purple_shirt(self),
                    "jacket": grey_jacket(self)})

                gym_clothes.update_Clothes({
                    "hair": short_hair(self),
                    "underwear": black_panties(self),
                    "skirt": grey_skirt(self),
                    "bra": black_bra(self), "top": purple_shirt(self)})

                pajamas.update_Clothes({
                    "hair": short_hair(self),
                    "underwear": black_panties(self),
                    "bra": black_bra(self), "top": purple_shirt(self)})

                shower.update_Clothes({
                    "hair": short_hair(self)})

                villain.update_Clothes({
                    "hair": long_hair(self), "face_outer_accessory": forehead_skull(self),
                    "boots": white_boots(self),
                    "dress": white_dress(self),
                    "gloves": white_gloves(self), "belt": skull_belt(self)})

            for Outfit in [default, casual, gym_clothes, pajamas, shower]:
                self.Wardrobe.Outfits.update({Outfit.name: Outfit})

            if self.tag not in ["Jubes", "Mystique"]:
                self.Wardrobe.Outfits.update({"Halloween_costume": Halloween_costume})

            if self.tag == "Mystique":
                self.Wardrobe.Outfits.update({"villain": villain})
            # else:
            #     self.Wardrobe.Outfits.update({"hero": hero})

            for Outfit in self.Wardrobe.Outfits.values():
                for Clothing in Outfit.Clothes.values():
                    if Clothing.name:
                        self.Wardrobe.add_Clothing(Clothing)

            self.Wardrobe.choose_Outfits()
            self.change_Outfit(self.Wardrobe.public_Outfit.name, instant = True)

            return

    class NPCClass(object):
        def __init__(self, name):
            self.name = name

            self.brows = "happy"
            self.eyes = "happy"
            self.mouth = "smile"

            self.psychic = False

            self.sprite_location = stage_center

        def change_face(self, emotion):
            if emotion == "psychic":
                self.brows = "concentrate"
                self.eyes = "concentrate"
                self.mouth = "stern"
                self.psychic = True
            elif emotion == "hypno":
                self.brows = "neutral"
                self.eyes = "hypno"
                self.mouth = "neutral"
                self.psychic = False
            elif emotion == "shocked":
                self.brows = "shocked"
                self.eyes = "shocked"
                self.mouth = "neutral"
                self.psychic = False
            elif emotion == "happy":
                self.brows = "happy"
                self.eyes = "happy"
                self.mouth = "smile"
                self.psychic = False
            elif emotion == "angry":
                self.brows = "concentrate"
                self.eyes = "happy"
                self.mouth = "stern"
                self.psychic = False

            return
