init -1 python:

    def bunny_cuffs(Owner):
        name = "bunny cuffs"
        string = "bunny_cuffs"

        clothing_type = "gloves"

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
