init -1 python:

    def black_lace_bra(Owner):
        name = "black lace bra"
        string = "black_lace_bra"

        clothing_type = "bra"

        dialogue_lines = {
            }

        shame = 1

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        if Owner.tag == "Rogue":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "blowjob",
                "sex"]
        elif Owner.tag == "Storm":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob"]
        elif Owner.tag == "Jubes":
            poses = [
                "arm pose 1",
                "arm pose 2",
                "handjob",
                "titjob",
                "blowjob"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
