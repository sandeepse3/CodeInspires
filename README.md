# CodeInspires
Code Inspirations and References

## Ubuntu
sudo apt update
<br> sudo apt install <package name>
<br> sudo apt list | grep <package name>
<br> sudo apt install --only-upgrade <package name>
<br> sudo apt install --only-upgrade <package-name1> <package-name2> <package-name3>

#### Force Delete
sudo rm -rf /path/to/directory

#### Create a Virtual environment
python -m venv .venv
<br> source .venv/bin/activate
<br> source <virtual environment name>/bin/activate
<br> activate
<br> deactivate

#### Install dependencies using pip
pip install -r requirements.txt
<br> pip freeze > requirements.txt (system packages are not included here)
<br> pip --version
<br> pip list
<br> pip list packageName
<br> pip install packageName
<br> pip uninstall packageName
<br> pip install -r requirements.txt
<br> pip freeze (to see all the packages installed)
<br> pip freeze > requirements.txt
<br> pip install --upgrade package-name  (This command tells pip to install the latest version of the package and uninstall the old version.)
<br> pip install --upgrade pip   (to upgrade pip itself)
<br> The -U option in pip install -U langchain stands for --upgrade. It means that pip will upgrade the package langchain-community to the latest version if it’s already installed. If the package is not installed, pip will install the latest version.

## Poetry
poetry init -To initialize pyproject.toml file
<br> poetry -V -Finding poetry version
<br> poetry show -To see all the packages
<br> poetry show <package name> -To see all the dependencies of the package
<br> poetry  shell -Activate the Python environment in the Folder that you are in
<br> poetry add <package name> -Create virtual environment (.venv) and install the package
<br> poetry add <package name>@version -To install exact version
<br> poetry add <package name>^2.12.1 -To install 2.Latest version.Latest version
<br> poetry add <package name>~2.12.1 -To install 2.12.Latest version
<br> poetry remove <package name> -To uninstall / remove the package
<br> poetry config --list -To see all the poetry configuration parameters
<br> poetry config virtualenvs.in-project true -To store the .venv folder in the project directory
<br> poetry config virtualenvs.prompt "{project_name}" -To change the virtual environment name
<br> poetry env info -To see the environment information
<br> poetry version minor -To update poetry to minor version
<br> poetry install -To install the dependencies and packages from the lock file
<br> poetry install --no-root -To install the dependencies and packages from the lock file
<br> poetry publish -To publish the package

## pyenv
pyenv for listing all the subcommands
<br> pyenv version
<br> pyenv versions
<br> pyenv update (to update pyenv)
<br> pyenv install --list
<br> pyenv install 3.11 (installs latest version)

pyenv shell command only activates a particular python version for the shell that you ran that command line. And so when I opened up a new shell or a new terminal session, we can see that the PI shell command was no longer in effect. If we want to change to a version of Python system wide, we can use pyenv global and then a python version.
<br> pyenv global 3.11.9
<br> pyenv uninstall 3.11.7

## Helpful
export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}
<br> sudo apt-get install python3-pip
<br> sudo apt-get update
#### Symbolic Link (symlink) Linux / Mac
ln -s /path/to/original /path/to/symlink
