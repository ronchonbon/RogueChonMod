init -1 python:

    def redblue_swimsuit():
        name = "red and blue swimsuit"
        image_string = "redblue_swimsuit"

        clothing_type = "bodysuit"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            }

        shame = 2

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
