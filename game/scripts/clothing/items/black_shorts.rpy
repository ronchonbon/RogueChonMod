init -1 python:

    def black_shorts(Owner):
        name = "black shorts"
        string = "black_shorts"

        clothing_type = "pants"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy"]

        if Owner.tag in ["Kitty", "Storm"]:
            number_of_states = 1
        elif Owner.tag == "Emma":
            number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
