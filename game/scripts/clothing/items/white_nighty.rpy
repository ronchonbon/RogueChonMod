init -1 python:

    def white_nighty(Owner):
        name = "white nighty"
        string = "white_nighty"

        clothing_type = "top"

        dialogue_lines = {
            }

        shame = 5

        hides = []
        covers = ["breasts", "pussy"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
