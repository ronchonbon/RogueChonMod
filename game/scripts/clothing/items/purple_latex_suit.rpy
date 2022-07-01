init -1 python:

    def purple_latex_suit():
        name = "purple latex suit"
        image_string = "purple_latex_suit"

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
