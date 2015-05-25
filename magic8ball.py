import plugintypes
from random import randrange
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
            if "will" in matches.group(1).lower():
                return self.responses[randrange(len(self.responses))]
            elif "what" or "where" or "when" or "why" or "how" in matches.group(1).lower():
                return "Those are questions I'm not sure how to answer. Perhaps you can ask Google."
            else:
                return "I'm not even sure that was a question!"
        except:
            return sys.exc_info()[0]
