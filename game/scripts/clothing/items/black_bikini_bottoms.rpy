init -1 python:

    def black_bikini_bottoms(Owner):
        name = "black bikini bottoms"
        image_string = "black_bikini_bottoms"

        clothing_type = "underwear"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)