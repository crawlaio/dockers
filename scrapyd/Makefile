IMAGE=sitoi/scrapyd:on-build

.PHONY: build up push

build:
	docker-compose build --no-cache

up: build
	docker-compose up -d

push: build
	docker push $(IMAGE)
