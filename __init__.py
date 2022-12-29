from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import match_one
from mycroft.audio import wait_while_speaking
from mycroft.util.log import LOG
from hotels import search

class HotelSearcher(MycroftSkill):
    def __init__(self):
        
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist. """
        
        super().__init__()
        self.learning = True
        self.is_reading = False
        self.register_entity_file('city.entity')

    @intent_handler('searcher.hotel.intent')
     def handle_searcher_hotel(self, message):
        if message.data.get('city') is None:
            response = self.get_response('searcher.hotel')
            if response is None:
                return
        else:
            response = message.data.get('city')
            self.speak_dialog('let_me_think', data={'city': response})
            hotels_result = hotels.search(response)
            self.log.info('Hotels result: {str(hotels_result)}')
            for hotel in hotels_result:
                self.speak(hotel, wait=True)

def create_skill():
    return HotelSearcher()
