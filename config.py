import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	RESERVATION_SEGMENT_SIZE = 60	# 세미나실을 예약할 수 있는 최소 시간 단위 (분)