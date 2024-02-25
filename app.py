import subprocess
from src import config, app


def install_dependencies():
    # Read requirements.txt file
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    # Install dependencies
    subprocess.run(['pip', 'install'] + requirements)


if __name__ == '__main__':
    # Install dependencies
    install_dependencies()

    # Initialize the database
    subprocess.run(['flask', 'db', 'init'])

    # Create the migration script
    subprocess.run(['flask', 'db', 'migrate', '-m', 'initialize'])

    # Apply the migration
    subprocess.run(['flask', 'db', 'upgrade'])

    # Run the import_data.py script
    subprocess.run(['python3', 'scripts/import_data.py', 'cities_canada-usa.tsv'])

    app.run(host= config.HOST,
            port= config.PORT,
            debug= config.DEBUG)