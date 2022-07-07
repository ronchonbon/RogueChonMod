init -1 python:

    def gold_necklace(Owner):
        name = "gold necklace"
        image_string = "gold_necklace"

        clothing_type = "neck"

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "sex"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
