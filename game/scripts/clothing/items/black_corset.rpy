init -1 python:

    def black_corset(Owner):
        name = "black corset"
        string = "black_corset"

        clothing_type = "bra"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        if Owner == EmmaX:
            number_of_states = 1
        elif Owner == JeanX:
            number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
