init python:

    import copy

    class ClothingClass(object):
        def __init__(self, name, image_string, Clothing_type, Owner_names, dialogue_lines, hides = [], covers = [], number_of_states = 1, menu_image = None, poses = []):
            self.name = name
            self.string = image_string

            self.Owner_names = Owner_names

            self.Clothing_type = Clothing_type

            self.hides = hides
            self.covers = covers

            self.max_undress_state = number_of_states - 1

            self.menu_image = menu_image

            self.poseable = poseable

            self.undress_state = 0

            self.covered_by = [None]

            if self.Clothing_type == "underwear":
                self.covered_by = ["hose"]

            if self.Clothing_type in ["nipple_accessories", "hose"]:
                self.covered_by = ["bodysuit"]

            if self.Clothing_type in ["bodysuit", "rope"]:
                self.covered_by = ["bra", "socks", "pants", "skirt"]

            if self.Clothing_type in ["socks", "pants", "skirt"]:
                self.covered_by = ["boots"]

            if self.Clothing_type == "bra":
                self.covered_by = ["dress"]

            if self.Clothing_type == "dress":
                self.covered_by = ["top"]

            if self.Clothing_type == "top":
                self.covered_by = ["belt", "jacket"]

            if self.Clothing_type in ["sleeves", "belt", "suspenders"]:
                self.covered_by = ["jacket"]

            if self.Clothing_type == "jacket":
                self.covered_by = ["cloak"]

            self.set_Clothing_flags()

        def put_on(self):
            while self.undress_state > 0:
                self.undress_state -= 1

                renpy.pause(0.2)

            self.set_Clothing_flags()

            return

        def take_off(self):
            while self.undress_state < self.max_undress_state:
                self.undress_state += 1

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
                if self.Clothing_type in ["bodysuit", "dress"] and self.undress_state < 2:
                    self.hides_breasts = True
                elif self.Clothing_type in ["top", "jacket"] and not self.undress_state:
                    self.hides_breasts = True
                else:
                    self.hides_breasts = True

            if "breasts" in self.covers:
                if self.Clothing_type in ["bodysuit", "dress"] and self.undress_state < 2:
                    self.covers_breasts = True
                elif self.Clothing_type in ["top", "jacket"] and not self.undress_state:
                    self.covers_breasts = True
                else:
                    self.covers_breasts = True

            if "pussy" in self.hides:
                if not self.undress_state:
                    self.hides_pussy = True

            if "pussy" in self.covers:
                if not self.undress_state:
                    self.covers_pussy = True

            if "thighs" in self.covers:
                if not self.undress_state:
                    self.covers_thighs = True

            if "feet" in self.covers:
                self.covers_feet = True

            return

    class OutfitClass(object):
        def __init__(self, name):
            self.name = name

            self.Clothing_types = ["face_tattoos", "face_piercings", "makeup", "gag",
                "face_inner_accessory", "hair", "face_outer_accessory",
                "body_tattoos", "body_piercings", "buttplug",
                "nipple_accessories", "underwear", "hose",
                "bodysuit", "rope",
                "socks", "pants", "skirt", "boots",
                "bra", "dress", "top",
                "neck", "gloves", "sleeves", "belt", "suspenders",
                "jacket", "cloak"]

            self.intrinsic = ["face_tattoos", "face_piercings",
                "hair",
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
            self.hide_pussy = ["underwear", "bodysuit", "pants", "skirt", "dress"]
            self.cover_thighs = ["bodysuit", "hose", "pants", "skirt", "boots", "dress"]
            self.cover_feet = ["hose", "socks", "boots"]

            self.Clothes = {}

            for Clothing_type in self.Clothing_types:
                self.Clothes[Clothing_type] = None

            self.set_Outfit_flags()

        def add_Clothing(self, Clothing):
            self.Clothes[Clothing.Clothing_type] = Clothing

            return

        def remove_Clothing(self, Clothing_type):
            self.Clothes[Clothing_type] = None

            return

        def change_into(self, Clothing):
            if Clothing == self.Clothes[Clothing.Clothing_type]:
                return

            temp_Clothes = self.Clothes

            covering_Clothes = self.get_covering_Clothes(Clothing)

            for c in reversed(range(len(covering_Clothes))):
                self.Clothes[covering_Clothes[c]].take_off()

                self.remove_Clothing(covering_Clothes[c])

                renpy.pause(0.2)

            Clothing.undress_state = Clothing.max_undress_state
            self.add_Clothing(Clothing)
            self.Clothes[Clothing.Clothing_type].put_on()

            for c in range(len(covering_Clothes)):
                temp_Clothes[covering_Clothes[c]].undress_state = temp_Clothes[covering_Clothes[c]].max_undress_state

                self.Clothes[covering_Clothes[c]] = temp_Clothes[covering_Clothes[c]]
                self.Clothes[covering_Clothes[c]].put_on()

            self.set_Outfit_flags()

            return

        def change_out_of(self, Clothing_type):
            if not self.Clothes[Clothing_type]:
                return

            temp_Clothes = self.Clothes

            covering_Clothes = self.get_covering_Clothes(self.Clothes[Clothing_type])

            for c in reversed(range(len(covering_Clothes))):
                self.Clothes[covering_Clothes[c]].take_off()

            self.Clothes[Clothing_type].take_off()
            self.remove_Clothing(Clothing_type)

            for c in range(len(covering_Clothes)):
                temp_Clothes[covering_Clothes[c]].undress_state = temp_Clothes[covering_Clothes[c]].max_undress_state

                self.Clothes[covering_Clothes[c]] = temp_Clothes[covering_Clothes[c]]
                self.Clothes[covering_Clothes[c]].put_on()

            self.set_Outfit_flags()

            return

        def undress(self, instant = False):
            for Clothing_type in reversed(self.removable):
                if self.Clothes[Clothing_type]:
                    if not instant:
                        self.Clothes[Clothing_type].take_off()

                    self.Clothes[Clothing_type] = None

                    if not instant:
                        renpy.pause(0.2)

            return

        def get_covering_Clothes(self, Clothing):
            covering_Clothes = Clothing.covered_by

            reached = False

            while not reached:
                if covering_Clothes[0] is None:
                    covering_Clothes.remove(None)

                    reached = True
                else:
                    if self.Clothes[covering_Clothes[0]]:
                        for next_Clothing in self.Clothes[covering_Clothes[0]].covered_by:
                            covering_Clothes.append(next_Clothing)

            return covering_Clothes

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
                    elif Clothing.covers_pussy:
                        self.pussy_covered = True

            for Clothing_type in self.cover_thighs:
                Clothing = self.Clothes[Clothing_type]

                if Clothing:
                    if Clothing.covers_thighs:
                        self.thighs_covered = True

            for Clothing_type in self.cover_feet:
                Clothing = self.Clothes[Clothing_type]

                if Clothing:
                    if Clothing.covers_feet:
                        self.feet_covered = True

            for Clothing_type in self.removable:
                Clothing = self.Clothes[Clothing_type]

                if Clothing:
                    self.fully_nude = False

            return

    class WardrobeClass(object):
        def __init__(self):
            self.Clothes = {}

            self.Outfits = {}

            self.current_Outfit = OutfitClass(name = "null")

            self.last_Outfit = OutfitClass(name = "null")

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

            self.current_Outfit.undress(instant = instant)

            for Clothing_type in Outfit.intrinsic:
                if Outfit.Clothes[Clothing_type]:
                    self.current_Outfit.Clothes[Clothing_type] = copy.deepcopy(Outfit.Clothes[Clothing_type])

            for Clothing_type in Outfit.removable:
                if Outfit.Clothes[Clothing_type]:
                    if not instant:
                        Outfit.Clothes[Clothing_type].undress_state = Outfit.Clothes[Clothing_type].max_undress_state
                    else:
                        Outfit.Clothes[Clothing_type].undress_state = 0

                    self.current_Outfit.Clothes[Clothing_type] = copy.deepcopy(Outfit.Clothes[Clothing_type])

                    if not instant:
                        renpy.pause(0.2)

                        self.current_Outfit.Clothes[Clothing_type].put_on()

            return
