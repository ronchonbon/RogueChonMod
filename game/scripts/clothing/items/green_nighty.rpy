init -1 python:

    def green_nighty(Owner):
        name = "green nighty"
        string = "green_nighty"

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
