init -1 python:

    def grey_knee_stockings(Owner):
        name = "grey knee stockings"
        string = "grey_knee_stockings"

        clothing_type = "socks"

        dialogue_lines = {
            }

        shame = 1

        hides = []
        covers = ["feet"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
