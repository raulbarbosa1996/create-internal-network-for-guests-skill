from mycroft import MycroftSkill, intent_file_handler


class CreateInternalNetworkForGuests(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('guests.for.network.internal.create.intent')
    def handle_guests_for_network_internal_create(self, message):
        self.speak_dialog('guests.for.network.internal.create')


def create_skill():
    return CreateInternalNetworkForGuests()

