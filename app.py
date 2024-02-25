import subprocess
from src import config, app


def install_dependencies():
    """Install project dependencies from requirements.txt."""
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    subprocess.run(['pip', 'install'] + requirements)


def initialize_database():
    """Initialize and migrate the database."""
    subprocess.run(['flask', 'db', 'init'])
    subprocess.run(['flask', 'db', 'migrate', '-m', 'initialize'])
    subprocess.run(['flask', 'db', 'upgrade'])


def import_data():
    """Run the import_data.py script."""
    subprocess.run(['python3', 'scripts/import_data.py', 'scripts/cities_canada-usa.tsv'])


if __name__ == '__main__':
    install_dependencies()
    initialize_database()
    import_data()

    app.run(host=config.HOST,
            port=config.PORT,
            debug=config.DEBUG)