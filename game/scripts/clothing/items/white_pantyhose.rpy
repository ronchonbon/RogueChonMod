init -1 python:

    def white_pantyhose(Owner):
        name = "white pantyhose"
        string = "white_pantyhose"

        clothing_type = "hose"

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = ["pussy", "thighs", "feet"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "footjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
