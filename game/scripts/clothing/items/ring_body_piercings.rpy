init -1 python:

    def ring_body_piercings(Owner):
        name = "ring body piercings"
        string = "ring_body_piercings"

        clothing_type = "body_piercings"

        dialogue_lines = {
            }

        shame = 2

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "footjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
