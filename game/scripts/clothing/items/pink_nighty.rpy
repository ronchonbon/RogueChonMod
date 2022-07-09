init -1 python:

    def pink_nighty(Owner):
        name = "pink nighty"
        string = "pink_nighty"

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
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
