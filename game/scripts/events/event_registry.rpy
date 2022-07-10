init python:

    def Event_registry():
        Events = [
            meet_Kitty()]

        for Event in Events:
            EventScheduler.add_Event(Event)

        return
