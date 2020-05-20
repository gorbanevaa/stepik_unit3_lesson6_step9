# Stepik online course homework
**Course name**: Automated testing with python and selenium

**Unit name** stepik_unit3_lesson6_step9

## Task description
https://stepik.org/lesson/237240/step/9

## Preconditions

- Python 3
- chromedriver installed in PATH

## Usage 

git clone https://github.com/ilyasamorodov/stepik-575-u3l6s9.git
cd stepik-575-u3l6s9
python -m venv venv
pip install --upgrade pip
\venv\Scripts\activate
pip install -r ./requirements.txt

pytest --language=es test_items.py
pytest --language=es --browser_name=firefox test_items.py