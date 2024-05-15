@echo off

rem Create virtual environment
python -m venv env

rem Activate virtual environment
call env\Scripts\activate.bat

rem Install dependencies
pip install selenium
pip install behave
pip install allure-behave

rem Run Behave tests
behave -f allure_behave.formatter:AllureFormatter -o Reports\feature

rem Deactivate virtual environment
deactivate
