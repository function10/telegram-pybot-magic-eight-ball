import plugintypes

class Magic8BallPlugin(plugintypes.TelegramPlugin):
	"""
	It's a magic eight ball!
	"""

	patterns = ["^!8ball (.*)"]
	usage = ["!8ball <question>"]

	def run(self, msg, matches):
		return "What?...Maybe"
