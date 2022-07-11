init -1 python:

    def grey_jacket(Owner):
        name = "grey jacket"
        string = "grey_jacket"

        clothing_type = "jacket"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        if Owner.tag == "Laura":
            number_of_states = 2
        elif Owner.tag == "Mystique":
            number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "sex"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
