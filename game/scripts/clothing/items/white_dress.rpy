init -1 python:

    def white_dress(Owner):
        name = "white dress"
        string = "white_dress"

        clothing_type = "dress"

        dialogue_lines = {
            }

        shame = 1

        hides = ["pussy", "breasts"]
        covers = ["pussy", "breasts"]

        number_of_states = 3

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
