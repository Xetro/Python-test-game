import time


class Score:


	
	def __init__(self):
		self.score = 0


	def get_score(self, c_time):
	
		time_passed = (time.time() - c_time) * 10
					
		self.score = int(time_passed) * 10
	
		return self.score	

