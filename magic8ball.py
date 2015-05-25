import plugintypes
from random import randint
import sys

class Magic8BallPlugin(plugintypes.TelegramPlugin):
    """
    It's a magic eight ball!
    """

    patterns = ["^!8ball (.*)"]
    usage = ["!8ball <question>"]
    

    def __init__(self):
        super().__init__()

        self.responses = [
                "Maybe", 
                "Probably", 
                "Yes", 
                "No", 
                "In you're dreams", 
                "Not Likely", 
                "That could be the case", 
                "Absolutely", 
                "Most definitely", 
                "No way"
            ]
        
    def run(self, msg, matches):
        try:
            return std_8ball_responses[randint(len(self.responses))]
        except:
            return sys.exc_info()[0]
