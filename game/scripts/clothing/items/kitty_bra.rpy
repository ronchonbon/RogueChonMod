init -1 python:

    def kitty_bra():
        name = "kitty bra"
        image_string = "kitty_bra"

        clothing_type = "bra"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        shame = 1

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)