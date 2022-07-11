init -1 python:

    def white_bikini_bottoms(Owner):
        name = "white bikini bottoms"
        string = "white_bikini_bottoms"

        clothing_type = "underwear"

        dialogue_lines = {
            }

        shame = 2

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
