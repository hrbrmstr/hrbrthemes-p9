install:
  python3 -m pip install --upgrade .

pre-build:
  python3 -m pip install --upgrade build
  python3 -m build

test-ul:
  python3 -m pip install --upgrade twine
  python3 -m twine upload --repository testpypi dist/*

pypi-ul:
  python3 -m pip install --upgrade twine
  python3 -m twine upload --repository pypi dist/*
