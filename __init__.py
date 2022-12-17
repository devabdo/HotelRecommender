from mycroft import MycroftSkill, intent_file_handler


class HotelSearcher(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('searcher.hotel.intent')
    def handle_searcher_hotel(self, message):
        self.speak_dialog('searcher.hotel')


def create_skill():
    return HotelSearcher()

