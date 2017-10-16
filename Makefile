.PHONY: help clean build start dev open_terminal tests run_tests lint run_lint

help:
	@echo "Available commands:"
	@echo "\tclean - Stop any running containers"
	@echo "\tbuild - Build the docker image"
	@echo "\tstart - Run the application in the background"
	@echo "\tdev - Run application and open a dev terminal"
	@echo "\topen_terminal - Enter into a dev terminal of running application"
	@echo "\ttests - Run all BDD tests"
	@echo "\tlint - Run PEP8 linter"

clean:
	docker-compose down

build: clean
	docker-compose build

start: build
	docker-compose up -d ahl-example

dev: build
	docker-compose run ahl-example bash

open_terminal:
	docker-compose exec ahl-example bash

tests: build
	docker-compose run ahl-example bash -c "py.test /ahl-example/tests/"

run_tests:
	docker-compose run ahl-example bash -c "py.test /ahl-example/tests/"

lint: build
	docker-compose run ahl-example bash -c "flake8 /ahl-example/"

run_lint:
	docker-compose run ahl-example bash -c "flake8 /ahl-example/"
