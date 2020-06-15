IMAGE=sitoi/scrapyd:latest

.PHONY: build up push

build:
	docker-compose build --no-cache

up: build
	docker-compose up -d

push: build
	docker push $(IMAGE)
