init python:

    class PlayerClass(object):
        def __init__(self, name, color):
            self.name = name
            self.color = color

            self.location = "bg_entrance"
            self.traveling = False

            self.sprite = False

            self.naked = False
            self.cock_out = False
            self.cock_wet = False
            self.spunk = False

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

            self.primary_Action = ActionClass(None, Target = None)
            self.secondary_Action = ActionClass(None, Target = None)

            self.semen = 2
            self.max_semen = 3

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
            self.wet = False
            self.spunk = {
                "hair": False, "face": False, "mouth": False, "chin": False,
                "breasts": False, "back": False, "belly": False, "hand": False,
                "pussy": False, "anus": False}

            self.location = "hold"
            self.teaching = False

            self.level = 1
            self.XP = 0
            self.XP_goal = 100
            self.stat_points = 0
            self.SEXP = 0

            self.reputation = 600

            # sprite_layer = [background_characters (eg. teachers), midground (eg. pool mask), midground_characters (eg. students), foreground (eg. desks), foreground_characters (eg. Present), Player.focused_Girl, cover (eg. fog)]
            self.sprite_location = stage_center
            self.sprite_layer = 6

            self.remaining_Actions = 3
            self.max_Actions = 3

            self.seen_peen = False
            self.seen_breasts = False
            self.seen_pussy = False
            self.seen_underwear = False

            self.event_counter = {
                "orgasmed": 0, "caught": 0, "sleepover": 0, "ass_slapped": 0,
                "swallowed": 0, "creampied": 0, "anal_creampied": 0,
                "been_with_girl": 0, "seen_with_girl": 0,
                "forced": 0}

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

            self.primary_Action = ActionClass(None, Target = None)
            self.secondary_Action = ActionClass(None, Target = None)

            self.Action_counter = {}

            for Action_type in all_Action_types:
                self.Action_counter[Action_type] = 0

            self.petname = self.name
            self.petnames = [self.name]

            if self.tag == "Rogue":
                self.voice = ch_r

                self.pubes = "_hairy"

                self.home = "bg_rogue"

                self.weekly_schedule = [
                    ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                    ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                    ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                    ["bg_classroom", "bg_dangerroom", "bg_rogue", "bg_rogue"],
                    ["bg_rogue", "bg_classroom", "bg_dangerroom", "bg_rogue"],
                    ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"],
                    ["bg_dangerroom", "bg_pool", "bg_rogue", "bg_rogue"]]

                self.likes = {"Kitty": 600, "Emma": 500, "Laura": 500, "Jean": 200, "Storm": 600, "Jubes": 500, "Mystique": 0}

                self.used_to_anal = 0

                self.player_petname = "Sugar"
                self.player_petnames = [self.player_petname, Player.name]
            elif self.tag == "Kitty":
                self.voice = ch_k

                self.pubes = "_hairy"

                self.home = "bg_kitty"

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

                self.used_to_anal = 0

                self.player_petname = Player.name[:1]
                self.player_petnames = ["sweetie", self.player_petname, Player.name]
            elif self.tag == "Emma":
                self.voice = ch_e

                self.pubes = ""

                self.home = "bg_emma"

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

                self.used_to_anal = 1

                last_name = get_last_name(Player)

                self.player_petname = "Mr. " + last_name
                self.player_petnames = ["young man", self.player_petname, Player.name]
            elif self.tag == "Laura":
                self.voice = ch_l

                self.pubes = "_hairy"

                self.home = "bg_laura"

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

                self.used_to_anal = 1

                self.player_petname = Player.name
                self.player_petnames = ["guy", self.player_petname]
            elif self.tag == "Jean":
                self.voice = ch_j

                self.pubes = "_hairy"

                self.home = "bg_jean"

                self.weekly_schedule = [
                    ["bg_classroom", "bg_classroom", "bg_dangerroom", "bg_jean"],
                    ["bg_jean", "bg_classroom", "bg_jean", "bg_jean"],
                    ["bg_jean", "bg_classroom", "bg_dangerroom", "bg_jean"],
                    ["bg_classroom", "bg_classroom", "bg_jean", "bg_jean"],
                    ["bg_jean", "bg_classroom", "bg_dangerroom", "bg_jean"],
                    ["bg_dangerroom", "bg_campus", "bg_pool", "bg_jean"],
                    ["bg_dangerroom", "bg_campus", "bg_pool", "bg_jean"]]

                self.likes = {"Rogue": 500, "Kitty": 500, "Emma": 300, "Laura": 500, "Storm": 300, "Jubes": 300, "Mystique": 0}

                self.used_to_anal = 0

                self.player_petname = "um. . ."
                self.player_petnames = [self.player_petname]
            elif self.tag == "Storm":
                self.voice = ch_s

                self.pubes = "_hairy"

                self.home = "bg_storm"

                self.weekly_schedule = [
                    ["bg_storm", "bg_dangerroom", "bg_dangerroom", "bg_storm"],
                    ["bg_teacher", "bg_teacher", "bg_classroom", "bg_storm"],
                    ["bg_storm", "bg_dangerroom", "bg_dangerroom", "bg_storm"],
                    ["bg_teacher", "bg_teacher", "bg_classroom", "bg_storm"],
                    ["bg_pool", "bg_campus", "bg_classroom", "bg_storm"],
                    ["bg_storm", "bg_campus", "bg_storm", "bg_pool"],
                    ["bg_storm", "bg_campus", "bg_storm", "bg_pool"]]

                self.likes = {"Rogue": 500, "Kitty": 600, "Emma": 400, "Laura": 500, "Jean": 300, "Jubes": 500, "Mystique": 0}

                self.used_to_anal = 0

                self.player_petname = Player.name
                self.player_petnames = [self.player_petname]
            elif self.tag == "Jubes":
                self.voice = ch_v

                self.pubes = "_hairy"

                self.home = "bg_jubes"

                self.weekly_schedule = [
                    ["bg_jubes", "bg_dangerroom", "bg_dangerroom", "bg_jubes"],
                    ["bg_classroom", "bg_classroom", "bg_jubes", "bg_jubes"],
                    ["bg_jubes", "bg_dangerroom", "bg_dangerroom", "bg_jubes"],
                    ["bg_dangerroom", "bg_dangerroom", "bg_jubes", "bg_jubes"],
                    ["bg_pool", "bg_campus", "bg_mall", "bg_jubes"],
                    ["bg_jubes", "bg_campus", "bg_mall", "bg_pool"],
                    ["bg_jubes", "bg_campus", "bg_jubes", "bg_pool"]]

                self.likes = {"Rogue": 500, "Kitty": 600, "Emma": 500, "Laura": 600, "Jean": 300, "Storm": 500, "Mystique": 0}

                self.used_to_anal = 0

                self.player_petname = "Bro"
                self.player_petnames = [self.player_petname, Player.name]
            elif self.tag == "Mystique":
                self.voice = ch_m

                self.pubes = ""

                self.home = "bg_mystique"

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

                self.used_to_anal = 1

                last_name = get_last_name(Player)

                self.player_petname = "Mr. " + last_name
                self.player_petnames = [self.player_petname, Player.name]

            bedrooms.append(self.home)

            all_Girls.append(self)

        def change_face(self, emotion = None, blushing = 0, manic = False, mouth = None, eyes = None, brows = None):
            emotion = self.emotion if not emotion else emotion

            if self.mood > 4 and emotion in ["normal", "bemused", "sexy", "sly", "smile", "startled"]:
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

        def undress(self):
            self.Outfit.undress()

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
            for Clothing_type in self.Outfit.removable:
                if self.Wardrobe.temp_Outfit.Clothes[Clothing_type] and not self.Clothes[Clothing_type]:
                    self.Wardrobe.temp_Outfit.Clothes[Clothing_type].state = self.Wardrobe.temp_Outfit.Clothes[Clothing_type].undressed_state

                    self.Outfit.add_Clothing(self.Wardrobe.temp_Outfit.Clothes[Clothing_type])

                    renpy.pause(0.2)

                if self.Clothes[Clothing_type] and self.Clothes[Clothing_type].state > 0:
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
                renpy.say(self.voice, "I don't have an outfit named [Outfit_name].")

                return

            if self.location not in ["bg_shower", "bg_pool"]:
                self.wet = False

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
            sleepwear = OutfitClass(name = "sleepwear")
            shower = OutfitClass(name = "shower")
            nude = OutfitClass(name = "nude")

            if self.tag in ["Emma", "Storm"]:
                teacher = OutfitClass(name = "teacher")

            if self.tag not in ["Jubes", "Mystique"]:
                Halloween_costume = OutfitClass(name = "Halloween_costume")

            if self.tag == "Mystique":
                disguise = OutfitClass(name = "disguise")
                villain = OutfitClass(name = "villain")

            if self.tag == "Rogue":
                first_casual.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": black_panties(self), "hose": black_tights(self),
                    "skirt": black_skirt(self),
                    "bra": black_tanktop(self), "top": green_mesh_top(self),
                    "neck": spiked_collar(self), "gloves": black_gloves(self)})

                second_casual.update_Clothes({
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

                sleepwear.update_Clothes({
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
                first_casual.update_Clothes({
                    "hair": Evolutions_hair(self),
                    "underwear": green_panties(self),
                    "pants": blue_capris(self),
                    "bra": yellow_cami(self), "top": pink_top(self),
                    "neck": gold_necklace(self)})

                second_casual.update_Clothes({
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

                sleepwear.update_Clothes({
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
                first_casual.update_Clothes({
                    "hair": wavy_hair(self),
                    "underwear": white_panties(self),
                    "pants": white_pants(self),
                    "bra": white_corset(self),
                    "neck": white_choker(self),
                    "jacket": white_jacket(self)})

                second_casual.update_Clothes({
                    "hair": wavy_hair(self),
                    "underwear": white_panties(self),
                    "pants": Emma_white_shorts(self), "boots": white_boots(self),
                    "bra": white_corset(self),
                    "neck": white_choker(self),
                    "cloak": Emma_white_cape(self)})

                gym_clothes.update_Clothes({
                    "hair": wavy_hair(self),
                    "underwear": white_sports_panties(self),
                    "bra": white_sports_bra(self),
                    "pants": white_pants(self)})

                sleepwear.update_Clothes({
                    "hair": wavy_hair(self),
                    "underwear": white_panties(self),
                    "bra": white_corset(self)})

                shower.update_Clothes({
                    "hair": wavy_hair(self),
                    "top": white_towel(self)})

                teacher.update_Clothes({
                    "hair": wavy_hair(self),
                    "underwear": white_panties(self),
                    "pants": white_pants(self),
                    "bra": white_corset(self),
                    "neck": white_choker(self),
                    "jacket": white_jacket(self)})

                Halloween_costume.update_Clothes({
                    "hair": wavy_hair(self),
                    "face_outer_accessory": Dimitrescu_hat(self),
                    "underwear": white_panties(self), "hose": white_stockings_and_garterbelt(self),
                    "skirt": Dimitrescu_skirt(self),
                    "top": Dimitrescu_top(self),
                    "neck": white_choker(self)})
            elif self.tag == "Laura":
                first_casual.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": leather_panties(self),
                    "pants": leather_pants(self),
                    "bra": leather_bra(self),
                    "neck": leash_choker(self), "gloves": black_wristbands(self)})

                second_casual.update_Clothes({
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

                sleepwear.update_Clothes({
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
                first_casual.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": green_panties(self),
                    "pants": khaki_pants(self),
                    "bra": green_bra(self), "top": pink_shirt(self)})

                second_casual.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": green_panties(self),
                    "skirt": green_skirt(self),
                    "bra": green_bra(self), "top": green_shirt(self)})

                gym_clothes.update_Clothes({
                    "hair": long_hair(self),
                    "underwear": green_panties(self),
                    "pants": green_yoga_pants(self),
                    "bra": blackyellow_sports_bra(self)})

                sleepwear.update_Clothes({
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
            # elif self.tag == "Storm":
            #     first_casual.update_Clothes({
            #         "hair": long_hair(self),
            #         "underwear": white_panties(self),
            #         "skirt": purple_skirt(self),
            #         "bra": black_bra(self), "top": white_shirt(self)})
            #
            #     second_casual.update_Clothes({
            #         "hair": long_hair(self),
            #         "underwear": white_panties(self),
            #         "pants": black_jeans(self),
            #         "bra": black_sports_bra(self),
            #         "jacket": black_jacket(self)})
            #
            #     gym_clothes.update_Clothes({
            #         "hair": long_hair(self),
            #         "underwear": white_panties(self),
            #         "pants": white_yoga_pants(self),
            #         "bra": black_sports_bra(self)})
            #
            #     sleepwear.update_Clothes({
            #         "hair": long_hair(self),
            #         "underwear": white_panties(self),
            #         "top": white_shirt(self)})
            #
            #     shower.update_Clothes({
            #         "hair": wavy_hair(self), "face_outer_accessory": head_towel(self)})
            #
            #     teacher.update_Clothes({
            #         "hair": long_hair(self),
            #         "underwear": white_panties(self),
            #         "pants": black_jeans(self),
            #         "bra": black_sports_bra(self),
            #         "jacket": black_jacket(self)})
            #
            #     Halloween_costume.update_Clothes({
            #         "hair": short_hair(self),
            #         "underwear": Elena_panties(self),
            #         "boots": ring_anklets(self),
            #         "bra": Elena_bra(self),
            #         "neck": ring_necklace(self), "sleeves": ring_armlets(self)})
            # elif self.tag == "Jubes":
            #     first_casual.update_Clothes({
            #         "hair": short_hair(self), "face_outer_accessory": pink_shades(self),
            #         "underwear": blue_panties(self),
            #         "pants": jean_shorts(self),
            #         "bra": blue_sports_bra(self), "top": red_shirt(self),
            #         "jacket": yellow_jacket(self)})
            #
            #     second_casual.update_Clothes({
            #         "hair": short_hair(self), "face_outer_accessory": pink_shades(self),
            #         "underwear": blue_panties(self),
            #         "pants": leather_pants(self),
            #         "bra": blue_sports_bra(self), "top": black_shirt(self),
            #         "jacket": yellow_jacket(self)})
            #
            #     gym_clothes.update_Clothes({
            #         "hair": short_hair(self),
            #         "underwear": blue_panties(self),
            #         "pants": leather_pants(self),
            #         "bra": blue_sports_bra(self), "top": black_shirt(self)})
            #
            #     sleepwear.update_Clothes({
            #         "hair": short_hair(self),
            #         "underwear": blue_panties(self),
            #         "bra": blue_sports_bra(self)})
            #
            #     shower.update_Clothes({
            #         "hair": short_hair(self),
            #         "top": yellow_towel(self)})
            # elif self.tag == "Mystique":
            #     first_casual.update_Clothes({
            #         "face_inner_accessory": black_glasses(self), "hair": short_hair(self),
            #         "underwear": black_panties(self), "hose": brown_pantyhose(self),
            #         "skirt": grey_skirt(self),
            #         "bra": black_bra(self), "top": purple_shirt(self),
            #         "jacket": grey_jacket(self)})
            #
            #     second_casual.update_Clothes({
            #         "face_inner_accessory": black_glasses(self), "hair": short_hair(self),
            #         "underwear": black_panties(self), "hose": brown_pantyhose(self),
            #         "skirt": grey_skirt(self),
            #         "bra": black_bra(self), "top": purple_shirt(self),
            #         "jacket": grey_jacket(self)})
            #
            #     gym_clothes.update_Clothes({
            #         "hair": short_hair(self),
            #         "underwear": black_panties(self),
            #         "skirt": grey_skirt(self),
            #         "bra": black_bra(self), "top": purple_shirt(self)})
            #
            #     sleepwear.update_Clothes({
            #         "hair": short_hair(self),
            #         "underwear": black_panties(self),
            #         "bra": black_bra(self), "top": purple_shirt(self)})
            #
            #     shower.update_Clothes({
            #         "hair": short_hair(self)})
            #
            #     villain.update_Clothes({
            #         "hair": long_hair(self), "face_outer_accessory": forehead_skull(self),
            #         "boots": white_boots(self),
            #         "dress": white_dress(self),
            #         "gloves": white_gloves(self), "belt": skull_belt(self)})

            self.Wardrobe.Outfits.update({
                "first_casual": first_casual,
                "second_casual": second_casual,
                "gym_clothes": gym_clothes,
                "sleepwear": sleepwear,
                "shower": shower})

            if self.tag in ["Emma", "Storm"]:
                self.Wardrobe.Outfits.update({"teacher": teacher})

            if self.tag not in ["Jubes", "Mystique"]:
                self.Wardrobe.Outfits.update({"Halloween_costume": Halloween_costume})

            for Outfit in self.Wardrobe.Outfits.values():
                for Clothing in Outfit.Clothes.values():
                    if Clothing.name:
                        self.Wardrobe.add_Clothing(Clothing)

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
