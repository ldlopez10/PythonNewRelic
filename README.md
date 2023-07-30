# PythonNewRelic

Basic Python serverless function with New Relic Monitoring

## How to Run this function

1. Make sure you have python installed on your machine [Install Python Docs](https://www.python.org/downloads/)
2. Create a virtual environment by running
   - `python -m venv .venv`
3. Activate your virtual environment by running
   - `source .venv/Scripts/activate`
   - If this does not work try: `source .venv/bin/activate`
4. Install requirements.txt
   - `pip install -r requirments.txt`
5. Run the function
   - `func start`

MAKE SURE TO ADD NEW RELIC STEPS TOO

## Getting Started with Azure Function

#### Project Structure

The main project folder (<project_root>) can contain the following files:

- **local.settings.json** - Used to store app settings and connection strings when running locally. This file doesn't get published to Azure. To learn more, see [local.settings.file](https://aka.ms/azure-functions/python/local-settings).
- **requirements.txt** - Contains the list of Python packages the system installs when publishing to Azure.
- **host.json** - Contains global configuration options that affect all functions in a function app. This file does get published to Azure. Not all options are supported when running locally. To learn more, see [host.json](https://aka.ms/azure-functions/python/host.json).
- **.vscode/** - (Optional) Contains store VSCode configuration. To learn more, see [VSCode setting](https://aka.ms/azure-functions/python/vscode-getting-started).
- **.venv/** - (Optional) Contains a Python virtual environment used by local development.
- **Dockerfile** - (Optional) Used when publishing your project in a [custom container](https://aka.ms/azure-functions/python/custom-container).
- **tests/** - (Optional) Contains the test cases of your function app. For more information, see [Unit Testing](https://aka.ms/azure-functions/python/unit-testing).
- **.funcignore** - (Optional) Declares files that shouldn't get published to Azure. Usually, this file contains .vscode/ to ignore your editor setting, .venv/ to ignore local Python virtual environment, tests/ to ignore test cases, and local.settings.json to prevent local app settings being published.

Each function has its own code file and binding configuration file ([**function.json**](https://aka.ms/azure-functions/python/function.json)).

#### Developing your first Python function using VS Code

I created my function app using the **[Azure function Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cstorageexplorer%2Cv2%2Cbash&pivots=programming-language-python)**

**MAC installation:**

1. `brew install azure-functions-core-tools@4`
2. `func new --template "Http Trigger" --name HttpTriggerFunc`

If you have not already, please checkout our [quickstart](https://aka.ms/azure-functions/python/quickstart) to get you started with Azure Functions developments in Python.

#### Publishing your function app to Azure

For more information on deployment options for Azure Functions, please visit this [guide](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python#publish-the-project-to-azure).

#### Next Steps

- To learn more about developing Azure Functions, please visit [Azure Functions Developer Guide](https://aka.ms/azure-functions/python/developer-guide).

- To learn more specific guidance on developing Azure Functions with Python, please visit [Azure Functions Developer Python Guide](https://aka.ms/azure-functions/python/python-developer-guide).
# PythonNewRelic
