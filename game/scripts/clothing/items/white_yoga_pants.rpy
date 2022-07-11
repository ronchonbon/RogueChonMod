init -1 python:

    def white_yoga_pants(Owner):
        name = "white yoga pants"
        string = "white_yoga_pants"

        clothing_type = "pants"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 2

        if Owner.tag == "Emma":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "doggy"]
        elif Owner.tag == "Storm":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
