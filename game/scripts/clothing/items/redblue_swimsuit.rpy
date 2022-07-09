init -1 python:

    def redblue_swimsuit(Owner):
        name = "red and blue swimsuit"
        string = "redblue_swimsuit"

        clothing_type = "bodysuit"

        dialogue_lines = {
            }

        shame = 2

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
