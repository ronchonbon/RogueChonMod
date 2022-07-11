init -1 python:

    def skull_belt(Owner):
        name = "skull belt"
        string = "skull_belt"

        clothing_type = "belt"

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
