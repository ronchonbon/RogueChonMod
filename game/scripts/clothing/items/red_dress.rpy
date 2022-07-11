init -1 python:

    def red_dress(Owner):
        name = "red dress"
        string = "red_dress"

        clothing_type = "dress"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
