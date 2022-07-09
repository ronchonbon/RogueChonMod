init -1 python:

    def black_tights(Owner):
        name = "black tights"
        string = "black_tights"

        clothing_type = "hose"

        dialogue_lines = {
            }

        shame = -2

        hides = ["pussy"]
        covers = ["pussy", "thighs", "feet"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
