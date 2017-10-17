.PHONY: help clean build dev tests lint

help:
	@echo "Available commands:"
	@echo "\tclean - Stop any running containers"
	@echo "\tbuild - Build the docker image"
	@echo "\tdev - Open a development terminal"
	@echo "\ttests - Run all BDD tests"
	@echo "\tlint - Run PEP8 linter"

clean:
	docker-compose down

build: clean
	docker-compose build

dev: build
	docker-compose run ahl-example bash

tests: build
	docker-compose run ahl-example bash -c "py.test -s /ahl-example/tests/"

lint: build
	docker-compose run ahl-example bash -c "flake8 /ahl-example/"
