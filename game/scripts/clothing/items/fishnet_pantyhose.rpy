init -1 python:

    def fishnet_pantyhose(Owner):
        name = "fishnet pantyhose"
        string = "fishnet_pantyhose"

        clothing_type = "hose"

        dialogue_lines = {
            }

        shame = 2

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
