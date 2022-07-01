init -2 python:

    import copy

    class ClothingClass(object):
        def __init__(self, name, image_string, Clothing_type, Owner_names, dialogue_lines, shame = 0, hides = [], covers = [], number_of_states = 1, poses = []):
            self.name = name
            self.string = image_string

            self.type = Clothing_type

            self.Owner_names = Owner_names

            self.dialogue_lines = dialogue_lines

            self.shame = shame

            self.hides = hides
            self.covers = covers

            self.number_of_states = number_of_states

            self.poses = poses

            self.state = 0

            if number_of_states > 1:
                self.undressed_state = 1
            else:
                self.undressed_state = 0

            self.set_Clothing_flags()

        def put_on(self):
            while self.state > 0:
                self.state -= 1

                renpy.pause(0.2)

            self.set_Clothing_flags()

            return

        def take_off(self):
            while self.state < self.undressed_state:
                self.state += 1

                renpy.pause(0.2)

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
        def __init__(self, name):
            self.name = name

            self.types = ["face_tattoos", "face_piercings", "makeup", "gag",
                "face_inner_accessory", "hair", "face_outer_accessory",
                "body_tattoos", "body_piercings", "buttplug",
                "nipple_accessories", "underwear", "hose",
                "bodysuit", "rope",
                "socks", "pants", "skirt", "boots",
                "bra", "dress", "top",
                "neck", "gloves", "sleeves", "belt", "suspenders",
                "jacket", "cloak"]

            self.intrinsic = ["face_tattoos", "face_piercings",
                "body_tattoos", "body_piercings"]

            self.removable = ["makeup", "gag",
                "face_inner_accessory", "face_outer_accessory",
                "buttplug",
                "nipple_accessories", "underwear", "hose",
                "bodysuit", "rope",
                "socks", "pants", "skirt", "boots",
                "bra", "dress", "top",
                "neck", "gloves", "sleeves", "belt", "suspenders",
                "jacket", "cloak"]

            self.hide_breasts = ["bodysuit", "bra", "dress", "top", "jacket"]
            self.hide_underwear = ["bodysuit", "pants", "skirt", "dress"]
            self.hide_pussy = ["underwear", "bodysuit", "pants", "skirt", "dress"]
            self.cover_thighs = ["bodysuit", "hose", "pants", "skirt", "boots", "dress"]
            self.cover_feet = ["hose", "socks", "boots"]

            self.coverage = {"face_tattoos": [],
                "face_piercings": [],
                "makeup": [],
                "gag": [],
                "face_inner_accessory": [],
                "hair": [],
                "face_outer_accessory": [],
                "body_tattoos": [],
                "body_piercings": [],
                "buttplug": [],
                "nipple_accessories": ["bodysuit", "bra", "dress", "top"],
                "underwear": ["hose", "bodysuit", "pants", "boots"],
                "hose": ["bodysuit", "pants", "socks", "boots"],
                "bodysuit": ["bra", "dress", "top", "jacket", "cloak", "socks", "pants", "skirt", "boots"],
                "rope": ["bra", "dress", "top", "jacket", "cloak", "socks", "pants", "skirt", "boots"],
                "socks": ["boots"],
                "pants": ["boots"],
                "skirt": ["boots"],
                "boots": [],
                "bra": ["dress", "top", "jacket", "cloak"],
                "dress": ["top", "belt", "jacket", "cloak"],
                "top": ["belt", "jacket", "cloak"],
                "neck": [],
                "gloves": [],
                "sleeves": ["jacket"],
                "belt": [],
                "suspenders": [],
                "jacket": ["cloak"],
                "cloak": []}

            self.Clothes = {}

            for Clothing_type in self.types:
                self.Clothes[Clothing_type] = None

            self.set_Outfit_flags()

        def add_Clothing(self, Clothing):
            self.Clothes[Clothing.type] = Clothing

            return

        def remove_Clothing(self, Clothing_types):
            if Clothing_types in self.types:
                Clothing_types = [Clothing_types]

            for Clothing_type in Clothing_types:
                self.Clothes[Clothing_type] = None

            return

        def change_into(self, Clothing):
            if self.Clothes[Clothing.type]:
                if Clothing.name == self.Clothes[Clothing.type].name:
                    return

            temp_Clothes = copy.deepcopy(self.Clothes)

            covering_Clothes = self.coverage[Clothing.type]

            for c in reversed(range(len(covering_Clothes))):
                if self.Clothes[covering_Clothes[c]]:
                    self.Clothes[covering_Clothes[c]].take_off()

                    self.remove_Clothing(covering_Clothes[c])

                    renpy.pause(0.2)

            if Clothing.type in ["underwear", "hose"]:
                if self.Clothes["skirt"] and "skirt" not in covering_Clothes:
                    self.Clothes["skirt"].take_off()

                if self.Clothes["dress"] and "dress" not in covering_Clothes:
                    self.Clothes["dress"].take_off()

            if self.Clothes[Clothing.type] and Clothing.type in self.removable:
                self.Clothes[Clothing.type].take_off()
                self.remove_Clothing(Clothing.type)

                renpy.pause(0.2)

            if Clothing.type == "pants" and self.Clothes["skirt"]:
                self.Clothes["skirt"].take_off()
                self.remove_Clothing("skirt")

                renpy.pause(0.2)
            elif Clothing.type == "skirt" and self.Clothes["pants"]:
                self.Clothes["pants"].take_off()
                self.remove_Clothing("pants")

                renpy.pause(0.2)

            Clothing.state = Clothing.undressed_state
            self.add_Clothing(Clothing)

            renpy.pause(0.2)

            self.Clothes[Clothing.type].put_on()

            if Clothing.type in ["underwear", "hose"]:
                if self.Clothes["skirt"] and "skirt" not in covering_Clothes:
                    self.Clothes["skirt"].put_on()

                if self.Clothes["dress"] and "dress" not in covering_Clothes:
                    self.Clothes["dress"].put_on()

            for c in range(len(covering_Clothes)):
                if temp_Clothes[covering_Clothes[c]]:
                    temp_Clothes[covering_Clothes[c]].state = temp_Clothes[covering_Clothes[c]].undressed_state
                    self.add_Clothing(temp_Clothes[covering_Clothes[c]])

                    renpy.pause(0.2)

                    self.Clothes[covering_Clothes[c]].put_on()

            self.set_Outfit_flags()

            return

        def change_out_of(self, Clothing_type):
            if not self.Clothes[Clothing_type]:
                return
            elif Clothing_type == "hair":
                return

            temp_Clothes = copy.deepcopy(self.Clothes)

            covering_Clothes = self.coverage[Clothing_type]

            for c in reversed(range(len(covering_Clothes))):
                if self.Clothes[covering_Clothes[c]]:
                    self.Clothes[covering_Clothes[c]].take_off()
                    self.remove_Clothing(covering_Clothes[c])

                    renpy.pause(0.2)

            if Clothing_type in ["underwear", "hose"]:
                if self.Clothes["skirt"] and "skirt" not in covering_Clothes:
                    self.Clothes["skirt"].take_off()

                if self.Clothes["dress"] and "dress" not in covering_Clothes:
                    self.Clothes["dress"].take_off()

            self.Clothes[Clothing_type].take_off()
            self.remove_Clothing(Clothing_type)

            renpy.pause(0.2)

            if Clothing_type in ["underwear", "hose"]:
                if self.Clothes["skirt"] and "skirt" not in covering_Clothes:
                    self.Clothes["skirt"].put_on()

                if self.Clothes["dress"] and "dress" not in covering_Clothes:
                    self.Clothes["dress"].put_on()

            for c in range(len(covering_Clothes)):
                if temp_Clothes[covering_Clothes[c]]:
                    temp_Clothes[covering_Clothes[c]].state = temp_Clothes[covering_Clothes[c]].undressed_state
                    self.add_Clothing(temp_Clothes[covering_Clothes[c]])

                    renpy.pause(0.2)

                    self.Clothes[covering_Clothes[c]].put_on()

            self.set_Outfit_flags()

            return

        def undress(self):
            for Clothing_type in reversed(self.removable):
                if self.Clothes[Clothing_type]:
                    self.Clothes[Clothing_type].take_off()

                    self.remove_Clothing(Clothing_type)

                    renpy.pause(0.2)

            return

        def update_Clothes(self, new_Clothes):
            self.Clothes.update(new_Clothes)

            self.set_Outfit_flags()

            return

        def set_Outfit_flags(self):
            self.breasts_supported = False

            self.breasts_hidden = False
            self.breasts_covered = False

            self.pussy_hidden = False
            self.pussy_covered = False

            self.thighs_covered = False
            self.feet_covered = False

            self.fully_nude = True

            if self.Clothes["bra"]:
                self.breasts_supported = True

            for Clothing_type in self.hide_breasts:
                Clothing = self.Clothes[Clothing_type]

                if Clothing:
                    if Clothing.hides_breasts:
                        self.breasts_hidden = True
                        self.breasts_covered = True

                        break
                    elif Clothing.covers_breasts:
                        self.breasts_covered = True

            for Clothing_type in self.hide_pussy:
                Clothing = self.Clothes[Clothing_type]

                if Clothing:
                    if Clothing.hides_pussy:
                        self.pussy_hidden = True
                        self.pussy_covered = True

                        break
                    elif Clothing.covers_pussy:
                        self.pussy_covered = True

            for Clothing_type in self.cover_thighs:
                Clothing = self.Clothes[Clothing_type]

                if Clothing:
                    if Clothing.covers_thighs:
                        self.thighs_covered = True

                        break

            for Clothing_type in self.cover_feet:
                Clothing = self.Clothes[Clothing_type]

                if Clothing:
                    if Clothing.covers_feet:
                        self.feet_covered = True

                        break

            for Clothing_type in self.removable:
                Clothing = self.Clothes[Clothing_type]

                if Clothing:
                    self.fully_nude = False

                    break

            self.shame = 0

            for Clothing_type in self.types:
                if self.Clothes[Clothing_type]:
                    self.shame += self.Clothes[Clothing_type].shame

            if not self.breasts_hidden:
                self.shame += 5

            if not self.breasts_covered:
                self.shame += 5

            if not self.pussy_hidden:
                self.shame += 10

            if not self.pussy_covered:
                self.shame += 10

            if not self.thighs_covered:
                self.shame += 2

            if not self.Clothes["underwear"]:
                self.shame += 5

            if self.shame < 0:
                self.shame = 0

            return

    class WardrobeClass(object):
        def __init__(self):
            self.Clothes = {}

            self.Outfits = {}

            self.current_Outfit = OutfitClass(name = "null")

            self.last_Outfit = OutfitClass(name = "null")

            self.temp_Outfit = OutfitClass(name = "null")

        def add_Clothing(self, Clothing):
            if Clothing not in self.Clothes:
                self.Clothes[Clothing.name] = Clothing

            return

        def add_Outfit(self, Outfit):
            if Outfit not in self.Outfits:
                self.Outfits[Outfit.name] = Outfit

            return

        def remove_Outfit(self, Outfit_name):
            for Outfit in self.Outfits:
                if Outfit.name == Outfit_name:
                    self.Outfits.remove(Outfit)

                    break

            return

        def change_Outfit(self, Outfit, instant = False):
            self.last_Outfit = copy.deepcopy(self.current_Outfit)

            if not instant:
                self.current_Outfit.undress()

                for Clothing_type in Outfit.intrinsic:
                    if Outfit.Clothes[Clothing_type]:
                        self.current_Outfit.add_Clothing(Outfit.Clothes[Clothing_type])

                for Clothing_type in Outfit.removable:
                    if Outfit.Clothes[Clothing_type]:
                        Outfit.Clothes[Clothing_type].state = Outfit.Clothes[Clothing_type].undressed_state

                        self.current_Outfit.add_Clothing(Outfit.Clothes[Clothing_type])

                        renpy.pause(0.2)

                        self.current_Outfit.Clothes[Clothing_type].put_on()

                if Outfit.Clothes["hair"]:
                    self.current_Outfit.add_Clothing(Outfit.Clothes["hair"])

            self.current_Outfit = Outfit

            self.temp_Outfit = copy.deepcopy(self.current_Outfit)

            return
