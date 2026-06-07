.PHONY: setup run test clean

setup:
	cd "Final Code and Data" && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

run:
	@echo "Open notebooks in Final Code and Data/ after make setup"

test:
	@python3 -c "import os; assert os.path.isdir('Final Code and Data'); print('structure ok')"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
