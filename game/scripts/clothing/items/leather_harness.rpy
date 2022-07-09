init -1 python:

    def leather_harness(Owner):
        name = "leather harness"
        image_string = "leather_harness"

        clothing_type = "underwear"

        dialogue_lines = {
            }

        shame = 5

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
