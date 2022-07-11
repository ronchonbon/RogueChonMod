init -1 python:

    def white_stockings_and_garterbelt(Owner):
        name = "white stockings and garterbelt"
        string = "white_stockings_and_garterbelt"

        clothing_type = "hose"

        dialogue_lines = {
            }

        shame = 2

        hides = []
        covers = ["feet"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
