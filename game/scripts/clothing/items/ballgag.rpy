init -1 python:

    def ballgag():
        name = "ballgag"
        image_string = "ballgag"

        clothing_type = "gag"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        shame = 5

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
