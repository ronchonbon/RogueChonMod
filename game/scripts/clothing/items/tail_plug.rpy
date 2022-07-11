init -1 python:

    def tail_plug(Owner):
        name = "tail plug"
        string = "tail_plug"

        clothing_type = "buttplug"

        dialogue_lines = {
            }

        shame = 5

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
