init -1 python:

    def black_stockings_and_garterbelt(Owner):
        name = "black stockings and garterbelt"
        string = "black_stockings_and_garterbelt"

        clothing_type = "hose"

        dialogue_lines = {
            }

        shame = 2

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
        elif Owner.tag in ["Jean", "Storm", "Jubes"]:
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
