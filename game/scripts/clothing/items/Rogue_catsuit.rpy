init -1 python:

    def Rogue_catsuit():
        name = "Rogue's catsuit"
        image_string = "Rogue_catsuit"

        clothing_type = "bodysuit"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            }

        shame = 1

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy", "thighs", "feet"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
