init -1 python:

    def plaid_skirt():
        name = "plaid skirt"
        image_string = "plaid_skirt"

        clothing_type = "skirt"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
