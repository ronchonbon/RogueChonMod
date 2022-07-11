init -1 python:

    def spiked_collar(Owner):
        name = "spiked collar"
        string = "spiked_collar"

        clothing_type = "neck"

        dialogue_lines = {
            }

        shame = 1

        hides = []
        covers = []

        number_of_states = 1

        if Owner.tag == "Rogue":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "blowjob",
                "sex",
                "doggy"]
        elif Owner.tag == "Emma":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
