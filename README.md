# PythonNewRelic

Basic Python serverless function with New Relic Monitoring

## MAC Development Environment Set Up

1. Install [Homebrew](https://brew.sh/), if it's not already installed.
   - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

2. Install Python on your machine [Install Python Docs](https://www.python.org/downloads/)

   - verify install
   - `python3 --version` or `python --version`

3. Install **[Azure function Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cstorageexplorer%2Cv2%2Cbash&pivots=programming-language-python#install-the-azure-functions-core-tools)**

   - Install Azure function Core tools using Brew
      ```
      brew tap azure/functions
      brew install azure-functions-core-tools@4
      # if upgrading on a machine that has 2.x or 3.x installed:
      brew link --overwrite azure-functions-core-tools@4
      ```

   -  verify install
   - `func --version`

4. [Create New Relic account](https://newrelic.com/signup)
   - Free account per single email

## Windows Development Environment Set Up

1. Install Python on your machine [Install Python Docs](https://www.python.org/downloads/)
   - verify install
   - `python3 --version` or `python --version`

2. Install **[Azure function Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cstorageexplorer%2Cv2%2Cbash&pivots=programming-language-python#install-the-azure-functions-core-tools)**
    
    Download and run the Core Tools installer, based on your version of Windows:
   - [v4.x - Windows 64-bit](https://go.microsoft.com/fwlink/?linkid=2174087) (Recommended. [Visual Studio Code debugging](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code#debugging-functions-locally) requires 64-bit.)
   - [v4.x - Windows 32-bit](https://go.microsoft.com/fwlink/?linkid=2174159)


   -  verify install
   - `func --version`

3. [Create New Relic account](https://newrelic.com/signup)
- Free account per single email

## How to Run this function

1. Create a virtual environment by running
   - `python -m venv .venv`
2. Activate your virtual environment by running
   - `source .venv/Scripts/activate`
   - If this does not work try: `source .venv/bin/activate`
3. Install requirements.txt
   - `pip install -r requirements.txt`
4. Run the function
   - `func start`

5. (optional) add NewRelic License Key to `local.setting.json` and run the function `func start`
   - `NEW_RELIC_LICENSE_KEY": "123456789NRAL`

## Endpoints

http://localhost:7071/api/HttpTriggerFunc

http://localhost:7071/api/HttpTriggerFunc?name=johndoe

## New Relic Docs

Navigate to https://one.newrelic.com/ then click APM & Services tab to see your data

- [NewRelic University](https://learn.newrelic.com/page/courses) (New Relic training courses)

- **[Python NewRelic Agent Docs](https://docs.newrelic.com/docs/apm/agents/python-agent/python-agent-api/guide-using-python-agent-api/)**
  - see new relic python agent methods that you can use to track your data
-

## External API Cat-Facts Docs

https://alexwohlbruck.github.io/cat-facts/docs/
