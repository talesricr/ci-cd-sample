### The Project:
This repo contains a simple Phonebook Management class ``phonebook.py`` with it respective unit case test file. The goal is to run the tests everytime a push is made into the project.
#
### How it works:
Checkout the <a href="https://github.com/talesricr/ci-cd-sample/blob/main/.github/workflows/blank.yml">``.github/workflows/blank.yml``</a> file.

This workflow is triggered on two events: a push or a pull request targeting the "main" branch.
```code
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```
#
Than the job is defined by steps:

```code
    steps:
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt  # If have one
```
#
After install python and it respective dependencies ``teste_phonebook.py`` is executed.

```code
    - name: Run tests
      run: python test_phonebook.py
```
