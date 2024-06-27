At first you do need to install all the dependencies from requirements.txt

To do that first create a virtual environment:
    python<specific version of python> -m venv <name of your virtual environment>
    eg: python3.11 -m venv env
    
Next activate this virtual environment:
    for Windows users:
      <name of your virtual environment>\Scripts\activate
      eg: env\Scripts\activate
    for macOS / Linux:
      source <name of your virtual environment>/bin/activate

When the environment is ready then you can install all the dependenies using this command
    pip install -r requirements.txt

To Deactivate the Virtual Environment:
    deactivate
