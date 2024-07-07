# CodeInspires
Code Inspirations and References

## Ubuntu
sudo apt update
sudo apt install <package name>
sudo apt list | grep <package name>
sudo apt install --only-upgrade <package name>
sudo apt install --only-upgrade <package-name1> <package-name2> <package-name3>

#### Force Delete
sudo rm -rf /path/to/directory

#### Create a Virtual environment
python -m venv .venv
source .venv/bin/activate
source <virtual environment name>/bin/activate
activate
deactivate

#### Install dependencies using pip
pip install -r requirements.txt
pip freeze > requirements.txt (system packages are not included here)

pip --version
pip list
pip list packageName
pip install packageName
pip uninstall packageName
pip install -r requirements.txt
pip freeze (to see all the packages installed)
pip freeze > requirements.txt

pip install --upgrade package-name  (This command tells pip to install the latest version of the package and uninstall the old version.)
pip install --upgrade pip   (to upgrade pip itself)

The -U option in pip install -U langchain stands for --upgrade. It means that pip will upgrade the package langchain-community to the latest version if it’s already installed. If the package is not installed, pip will install the latest version.

## Poetry
To initialize pyproject.toml file
poetry init

Finding poetry version
poetry -V

To see all the packages
poetry show
To see all the dependencies of the package
poetry show <package name>

Activate the Python environment in the Folder that you are in
poetry  shell

Create virtual environment (.venv) and install the package
poetry add <package name>

To install exact version
poetry add <package name>@version

To install 2.Latest version.Latest version
poetry add <package name>^2.12.1

To install 2.12.Latest version
poetry add <package name>~2.12.1

To uninstall / remove the package
poetry remove <package name>

To see all the poetry configuration parameters
poetry config --list

To store the .venv folder in the project directory
poetry config virtualenvs.in-project true

To change the virtual environment name
poetry config virtualenvs.prompt "{project_name}"

To see the environment information
poetry env info

To update poetry to minor version
poetry version minor

To install the dependencies and packages from the lock file
poetry install

To install the dependencies and packages from the lock file
poetry install --no-root

To publish the package
poetry publish

## pyenv
pyenv for listing all the subcommands
pyenv version
pyenv versions
pyenv update (to update pyenv)
pyenv install --list
pyenv install 3.11 (installs latest version)

pyenv shell command only activates a particular python version for the shell that you ran that command line. And so when I opened up a new shell or a new terminal session, we can see that the PI shell command was no longer in effect. If we want to change to a version of Python system wide, we can use pyenv global and then a python version.
pyenv global 3.11.9
pyenv uninstall 3.11.7

## Helpful
export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}

sudo apt-get install python3-pip
sudo apt-get update

#### Symbolic Link (symlink) Linux / Mac
ln -s /path/to/original /path/to/symlink
