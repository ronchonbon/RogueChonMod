init -2 python:

    import copy

    class ClothingClass(object):
        def __init__(self, Owner, name, string, type, dialogue_lines, **kwargs):
            self.Owner = Owner

            self.name = name
            self.string = string

            self.type = type

            self.dialogue_lines = dialogue_lines

            self.shame = kwargs.get("shame", 0)

            self.hides = kwargs.get("hides", [])
            self.covers = kwargs.get("covers", [])

            self.number_of_states = kwargs.get("number_of_states", 1)

            self.poses = kwargs.get("poses", [])

            self.state = 0

            if self.number_of_states > 1:
                self.undressed_state = 1
            else:
                self.undressed_state = 0

            self.set_Clothing_flags()

        def put_on(self):
            while self.state > 0:
                self.state -= 1

                renpy.pause(0.1)

            self.set_Clothing_flags()

            return

        def take_off(self):
            while self.state < self.undressed_state:
                self.state += 1

                renpy.pause(0.1)

            self.set_Clothing_flags()

            return

        def set_Clothing_flags(self):
            self.hides_breasts = False
            self.covers_breasts = False

            self.hides_pussy = False
            self.covers_pussy = False

            self.covers_thighs = False
            self.covers_feet = False

            if "breasts" in self.hides:
                if self.type in ["bodysuit", "dress"] and self.state < 2:
                    self.hides_breasts = True
                elif self.type in ["top", "jacket"] and self.state < 1:
                    self.hides_breasts = True
                else:
                    self.hides_breasts = True

            if "breasts" in self.covers:
                if self.type in ["bodysuit", "dress"] and self.state < 2:
                    self.covers_breasts = True
                elif self.type in ["top", "jacket"] and self.state < 1:
                    self.covers_breasts = True
                else:
                    self.covers_breasts = True

            if "pussy" in self.hides:
                if self.state != 1:
                    self.hides_pussy = True

            if "pussy" in self.covers:
                if self.state != 1:
                    self.covers_pussy = True

            if "thighs" in self.covers:
                if self.state != 1:
                    self.covers_thighs = True

            if "feet" in self.covers:
                self.covers_feet = True

            return

    class OutfitClass(object):
        def __init__(self, name, **kwargs):
            self.name = name

            self.wear_in_public = kwargs.get("wear_in_public", False)
            self.wear_in_private = kwargs.get("wear_in_private", False)
            self.activewear = kwargs.get("activewear", False)
            self.sleepwear = kwargs.get("sleepwear", False)
            self.swimwear = kwargs.get("swimwear", False)

            self.Clothes = {}

            for type in all_Clothing_types:
                self.Clothes[type] = ClothingClass(Owner = None, name = None, string = None, type = None, dialogue_lines = None)

            self.set_Outfit_flags()

        def add_Clothing(self, Clothing):
            self.Clothes[Clothing.type] = Clothing

            return

        def remove_Clothing(self, types):
            if types in all_Clothing_types:
                types = [types]

            for type in types:
                self.Clothes[type] = ClothingClass(Owner = None, name = None, string = None, type = None, dialogue_lines = None)

            return

        def change_into(self, Clothing):
            if self.Clothes[Clothing.type]:
                if Clothing.name == self.Clothes[Clothing.type].name:
                    return

            temp_Clothes = copy.deepcopy(self.Clothes)

            covering_Clothes = Clothing_coverage[Clothing.type]

            for c in reversed(range(len(covering_Clothes))):
                if self.Clothes[covering_Clothes[c]].name:
                    self.Clothes[covering_Clothes[c]].take_off()

                    self.remove_Clothing(covering_Clothes[c])

                    renpy.pause(0.1)

            if Clothing.type in ["underwear", "hose"]:
                if self.Clothes["skirt"] and "skirt" not in covering_Clothes:
                    self.Clothes["skirt"].take_off()

                if self.Clothes["dress"] and "dress" not in covering_Clothes:
                    self.Clothes["dress"].take_off()

            if self.Clothes[Clothing.type].name and Clothing.type in removable_Clothing_types:
                self.Clothes[Clothing.type].take_off()
                self.remove_Clothing(Clothing.type)

                renpy.pause(0.1)

            if Clothing.type == "pants" and self.Clothes["skirt"]:
                self.Clothes["skirt"].take_off()
                self.remove_Clothing("skirt")

                renpy.pause(0.1)
            elif Clothing.type == "skirt" and self.Clothes["pants"]:
                self.Clothes["pants"].take_off()
                self.remove_Clothing("pants")

                renpy.pause(0.1)

            Clothing.state = Clothing.undressed_state
            self.add_Clothing(Clothing)

            renpy.pause(0.1)

            self.Clothes[Clothing.type].put_on()

            if Clothing.type in ["underwear", "hose"]:
                if self.Clothes["skirt"] and "skirt" not in covering_Clothes:
                    self.Clothes["skirt"].put_on()

                if self.Clothes["dress"] and "dress" not in covering_Clothes:
                    self.Clothes["dress"].put_on()

            for c in range(len(covering_Clothes)):
                if temp_Clothes[covering_Clothes[c]].name:
                    temp_Clothes[covering_Clothes[c]].state = temp_Clothes[covering_Clothes[c]].undressed_state
                    self.add_Clothing(temp_Clothes[covering_Clothes[c]])

                    renpy.pause(0.1)

                    self.Clothes[covering_Clothes[c]].put_on()

            self.set_Outfit_flags()

            return

        def change_out_of(self, type):
            if not self.Clothes[type]:
                return
            elif type == "hair":
                return

            temp_Clothes = copy.deepcopy(self.Clothes)

            covering_Clothes = Clothing_coverage[type]

            for c in reversed(range(len(covering_Clothes))):
                if self.Clothes[covering_Clothes[c]].name:
                    self.Clothes[covering_Clothes[c]].take_off()
                    self.remove_Clothing(covering_Clothes[c])

                    renpy.pause(0.1)

            if type in ["underwear", "hose"]:
                if self.Clothes["skirt"] and "skirt" not in covering_Clothes:
                    self.Clothes["skirt"].take_off()

                if self.Clothes["dress"] and "dress" not in covering_Clothes:
                    self.Clothes["dress"].take_off()

            self.Clothes[type].take_off()
            self.remove_Clothing(type)

            renpy.pause(0.1)

            if type in ["underwear", "hose"]:
                if self.Clothes["skirt"] and "skirt" not in covering_Clothes:
                    self.Clothes["skirt"].put_on()

                if self.Clothes["dress"] and "dress" not in covering_Clothes:
                    self.Clothes["dress"].put_on()

            for c in range(len(covering_Clothes)):
                if temp_Clothes[covering_Clothes[c]].name:
                    temp_Clothes[covering_Clothes[c]].state = temp_Clothes[covering_Clothes[c]].undressed_state
                    self.add_Clothing(temp_Clothes[covering_Clothes[c]])

                    renpy.pause(0.1)

                    self.Clothes[covering_Clothes[c]].put_on()

            self.set_Outfit_flags()

            return

        def undress(self, instant = False):
            for type in reversed(removable_Clothing_types):
                if self.Clothes[type].name:
                    if not instant:
                        self.Clothes[type].take_off()

                    self.remove_Clothing(type)

                    if not instant:
                        renpy.pause(0.1)

            return

        def update_Clothes(self, new_Clothes):
            self.Clothes.update(new_Clothes)

            self.set_Outfit_flags()

            return

        def set_Outfit_flags(self):
            self.breasts_supported = False

            self.breasts_hidden = False
            self.breasts_covered = False

            self.underwear_hidden = False
            self.underwear_covered = False

            self.pussy_hidden = False
            self.pussy_covered = False

            self.thighs_covered = False
            self.feet_covered = False

            self.fully_nude = True

            if self.Clothes["bra"]:
                self.breasts_supported = True

            for type in breast_hiding_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing:
                    if Clothing.hides_breasts:
                        self.breasts_hidden = True
                        self.breasts_covered = True

                        break
                    elif Clothing.covers_breasts:
                        self.breasts_covered = True

            for type in underwear_hiding_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing:
                    if Clothing.hides_pussy:
                        self.underwear_hidden = True
                        self.underwear_covered = True

                        break
                    elif Clothing.covers_pussy:
                        self.underwear_covered = True

            for type in pussy_hiding_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing:
                    if Clothing.hides_pussy:
                        self.pussy_hidden = True
                        self.pussy_covered = True

                        break
                    elif Clothing.covers_pussy:
                        self.pussy_covered = True

            for type in thigh_covering_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing:
                    if Clothing.covers_thighs:
                        self.thighs_covered = True

                        break

            for type in feet_covering_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing:
                    if Clothing.covers_feet:
                        self.feet_covered = True

                        break

            for type in removable_Clothing_types:
                Clothing = self.Clothes[type]

                if Clothing:
                    self.fully_nude = False

                    break

            self.shame = 0

            for type in all_Clothing_types:
                if self.Clothes[type]:
                    self.shame += self.Clothes[type].shame
                elif type == "bra":
                    self.shame += 2
                elif type == "underwear":
                    self.shame += 5

            if not self.breasts_covered:
                self.shame += 10
            elif not self.breasts_hidden:
                self.shame += 5

            if not self.pussy_covered:
                self.shame += 20
            elif not self.pussy_hidden:
                self.shame += 15
            elif not self.underwear_covered:
                self.shame += 5
            elif not self.underwear_hidden:
                self.shame += 2

            if not self.thighs_covered:
                self.shame += 2

            if self.shame < 0:
                self.shame = 0

            return

    class WardrobeClass(object):
        def __init__(self):
            self.Clothes = {}

            self.Outfits = {}

            self.public_Outfit = OutfitClass("null")
            self.private_Outfit = OutfitClass("null")
            self.gym_Outfit = OutfitClass("null")
            self.sleeping_Outfit = OutfitClass("null")
            self.swimming_Outfit = OutfitClass("null")

            self.current_Outfit = self.public_Outfit
            self.last_Outfit = self.public_Outfit
            self.temp_Outfit = self.public_Outfit

        def add_Clothing(self, Clothing):
            if Clothing not in self.Clothes:
                self.Clothes[Clothing.name] = Clothing

            return

        def add_Outfit(self, Outfit):
            if Outfit not in self.Outfits:
                self.Outfits[Outfit.name] = Outfit

            return

        def remove_Outfit(self, name):
            for Outfit in self.Outfits:
                if Outfit.name == name:
                    self.Outfits.remove(Outfit)

                    break

            return

        def change_Outfit(self, Outfit, instant = False):
            if self.current_Outfit.name == Outfit.name:
                return

            self.last_Outfit = copy.deepcopy(self.current_Outfit)

            if not instant:
                self.current_Outfit.undress(instant = instant)

                for type in intrinsic_Clothing_types:
                    if Outfit.Clothes[type]:
                        self.current_Outfit.add_Clothing(Outfit.Clothes[type])

                for type in removable_Clothing_types:
                    if Outfit.Clothes[type].name:
                        Outfit.Clothes[type].state = Outfit.Clothes[type].undressed_state

                        self.current_Outfit.add_Clothing(Outfit.Clothes[type])

                        renpy.pause(0.1)

                        self.current_Outfit.Clothes[type].put_on()

                if Outfit.Clothes["hair"]:
                    self.current_Outfit.add_Clothing(Outfit.Clothes["hair"])

            self.current_Outfit = copy.deepcopy(Outfit)

            self.temp_Outfit = copy.deepcopy(self.current_Outfit)

            return

        def choose_Outfits(self):
            public_Outfits = []
            private_Outfits = []
            gym_Outfits = []
            sleeping_Outfits = []
            swimming_Outfits = []

            for Outfit in self.Outfits.values():
                if Outfit.wear_in_public:
                    public_Outfits.append(Outfit)

                if Outfit.wear_in_private:
                    private_Outfits.append(Outfit)

                if Outfit.activewear:
                    gym_Outfits.append(Outfit)

                if Outfit.sleepwear:
                    sleeping_Outfits.append(Outfit)

                if Outfit.swimwear:
                    swimming_Outfits.append(Outfit)

            renpy.random.shuffle(public_Outfits)
            renpy.random.shuffle(private_Outfits)
            renpy.random.shuffle(gym_Outfits)
            renpy.random.shuffle(sleeping_Outfits)
            renpy.random.shuffle(swimming_Outfits)

            self.public_Outfit = public_Outfits[0] if public_Outfits else OutfitClass("null")
            self.private_Outfit = private_Outfits[0] if private_Outfits else OutfitClass("null")
            self.gym_Outfit = gym_Outfits[0] if gym_Outfits else OutfitClass("null")
            self.sleeping_Outfit = sleeping_Outfits[0] if sleeping_Outfits else OutfitClass("null")
            self.swimming_Outfit = swimming_Outfits[0] if swimming_Outfits else OutfitClass("null")

            return
