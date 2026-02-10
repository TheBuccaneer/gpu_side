
.PHONY: run clean

run:
	. .venv/bin/activate && python3 src/run.py --config configs/default.yaml

clean:
	rm -rf out/* data/processed/*
