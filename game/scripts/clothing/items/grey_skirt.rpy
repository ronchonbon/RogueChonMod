init -1 python:

    def grey_skirt(Owner):
        name = "grey skirt"
        string = "grey_skirt"

        clothing_type = "skirt"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
