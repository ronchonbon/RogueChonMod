init -1 python:

    def Rogue_catsuit(Owner):
        name = "Rogue's catsuit"
        string = "Rogue_catsuit"

        clothing_type = "bodysuit"

        dialogue_lines = {
            }

        shame = 1

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy", "thighs", "feet"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
