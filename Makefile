clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

run-tests:
	@echo 'Running tests...'
	pytest

install_requirements:
	@echo 'Installing Requirements...'
	pip install -r requirements.txt
