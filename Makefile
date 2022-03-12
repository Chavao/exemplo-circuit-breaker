.PHONY: setup run server1 server2

setup:
	@pip install Flask circuitbreaker requests

run:
	@FLASK_APP=main flask run

server1:
	@cd server1 && ./run
	@cd ..

server2:
	@cd server2 && ./run
	@cd ..
