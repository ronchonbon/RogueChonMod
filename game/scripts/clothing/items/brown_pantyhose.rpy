init -1 python:

    def brown_pantyhose(Owner):
        name = "brown pantyhose"
        string = "brown_pantyhose"

        clothing_type = "hose"

        dialogue_lines = {
            }

        shame = -2

        hides = []
        covers = ["pussy", "thighs", "feet"]

        number_of_states = 1

        if Owner.tag == "Laura":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "sex"]
        elif Owner.tag == "Mystique":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
