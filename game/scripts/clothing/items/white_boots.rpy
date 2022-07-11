init -1 python:

    def white_boots(Owner):
        name = "white boots"
        string = "white_boots"

        clothing_type = "boots"

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        if Owner.tag == "Emma":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "footjob",
                "doggy"]
        elif Owner.tag == "Mystique":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
