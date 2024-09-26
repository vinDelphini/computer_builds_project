clean: 
	@find . -name "*.pyc" -exec rm -rf {} \; || true
	@find . -name "__pycache__" -delete || true
	@find . -name ".vscode" -type d -exec rm -rf {} \; 2>/dev/null || true
	@find . -name ".idea" -type d -exec rm -rf {} \; 2>/dev/null || true
	@find . -name ".pytest_cache" -type d -exec rm -rf {} \; 2>/dev/null || true

run-tests:
	@echo 'Running tests...'
	pytest -v --color=yes

install_requirements:
	@echo 'Installing Requirements...'
	pip install -r requirements.txt

show-inheritance-tree:
	feh inheritance_tree.png
