install:
	pip install -r requirements.txt

requirements:
	pip freeze > requirements.txt

run:
	python main.py

build:
	pyinstaller --onefile main.py

clean:
	rm -rf build dist *.spec