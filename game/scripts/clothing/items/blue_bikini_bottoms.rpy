init -1 python:

    def blue_bikini_bottoms(Owner):
        name = "blue bikini bottoms"
        string = "blue_bikini_bottoms"

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
            "handjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
