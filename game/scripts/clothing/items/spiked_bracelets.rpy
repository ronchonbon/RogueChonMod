init -1 python:

    def spiked_bracelets(Owner):
        name = "spiked bracelets"
        string = "spiked_bracelets"

        clothing_type = "gloves"

        dialogue_lines = {
            }

        shame = 1

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 2"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
