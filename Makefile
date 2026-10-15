.PHONY: up run test clean
up:
	docker compose up --build
run:
	python experiments/run_all.py
test:
	pytest -q
clean:
	rm -f results/*.png results/summary.json
