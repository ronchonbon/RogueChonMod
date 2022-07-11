init -1 python:

    def leather_pants(Owner):
        name = "leather pants"
        string = "leather_pants"

        clothing_type = "pants"

        dialogue_lines = {
            }

        shame = 0

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        if Owner.tag in ["Emma", "Laura"]:
            number_of_states = 1
        elif Owner.tag == "Jubes":
            number_of_states = 2

        if Owner.tag in ["Emma", "Jubes"]:
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]
        elif Owner.tag == "Laura":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "sex"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
