init -1 python:

    def black_stockings(Owner):
        name = "black stockings"
        string = "black_stockings"

        clothing_type = "socks"

        dialogue_lines = {
            }

        shame = 1

        hides = []
        covers = ["feet"]

        number_of_states = 1

        if Owner.tag == "Rogue":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "blowjob",
                "sex",
                "doggy"]
        elif Owner.tag == "Laura":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "sex"]
        elif Owner.tag in ["Jean", "Storm", "Jubes"]:
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
