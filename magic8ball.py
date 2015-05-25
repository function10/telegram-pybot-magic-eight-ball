import plugintypes
import random

class Magic8BallPlugin(plugintypes.TelegramPlugin):
	"""
	It's a magic eight ball!
	"""

	patterns = ["^!8ball (.*)"]
	usage = ["!8ball <question>"]
	
	std_8ball_responses = ["Maybe","Probably","Yes", "No","In you're dreams", "Not Likely", "That could be the case", "Absolutely", "Most definitely", "No way"]
	rand_number = random.randint(0, len(std_8ball_responses))

	def run(self, msg, matches):
		return std_8ball_responses[rand_number]
