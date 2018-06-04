import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	RESERVATION_SEGMENT_SIZE = 60	# Minimum time of seminar room reservation(min)