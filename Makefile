BASE_DIR := src
ENV_PATH := $(shell poetry env info --path)
ACTIVATE_PATH := /bin/activate
WIN_ACTIVATE_PATH := \Scripts\activate.bat

run:
	python $(BASE_DIR)/manage.py runserver

migrations:
	python $(BASE_DIR)/manage.py makemigrations

migrate:
	python $(BASE_DIR)/manage.py migrate

lint:
	black $(BASE_DIR)
	pylint $(BASE_DIR)
	pycodestyle --exclude=migrations --max-line-length=88 $(BASE_DIR)

superuser:
	python $(BASE_DIR)/manage.py shell -c "import createsuperuser"

build:
	docker-compose up --build

setup: config.yml
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
	export PATH="$HOME/.poetry/bin:$PATH"

	echo "Create shell..."
	poetry env use 3.9
	poetry env info --path

	echo "Activating virtual environment..."
	$(shell source $(ENV_PATH)$(ACTIVATE_PATH))

	echo "Installing requirements..."
	poetry install

	echo "Checking config.yml exists and has basic setup..."
	python $(BASE_DIR)/manage.py shell -c "import check_config_vars"

	echo "Setting up database..."
	make migrate

	echo "Ensuring admin user..."
	make superuser

	echo "Launching server..."
	make run

setup-win: config.yml
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
	call set PATH=%PATH%;%USERPROFILE%\.poetry\bin;
	call set PATH=%USERPROFILE%\AppData\Local\Programs\Python\Python39;%PATH%;
	call set PATH=%USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts;%PATH%;

	pip install pyyaml
	python $(BASE_DIR)/check_config_vars.py

	echo "Activating venv..."
	call poetry shell
	call $(call  poetry env info --path)$(WIN_ACTIVATE_PATH)

	echo "Installing requirements..."
	call poetry install

	echo "Setting up database..."
	make migrate

	echo "Ensuring admin user..."
	make superuser

	echo "Launching server..."
	make run