init -1 python:

    def bitch_tattoos(Owner):
        name = "bitch tattoos"
        string = "bitch_tattoos"

        clothing_type = "body_tattoos"

        dialogue_lines = {
            }

        shame = 5

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
