init -1 python:

    def yellow_bikini_top(Owner):
        name = "yellow bikini top"
        string = "yellow_bikini_top"

        clothing_type = "bra"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        if Owner.tag == "Rogue":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "blowjob",
                "sex",
                "doggy"]
        elif Owner.tag == "Jean":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "titjob",
                "blowjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
