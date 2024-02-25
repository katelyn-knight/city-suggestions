import subprocess


def initialize_test_database():
    """Initialize and populate the test database."""
    subprocess.run(['flask', 'db', 'init', '--database', 'test'])  # Initialize test database
    subprocess.run(['flask', 'db', 'migrate', '-m', 'initialize', '--database', 'test'])  # Migrate test database
    subprocess.run(['flask', 'db', 'upgrade', '--database', 'test'])  # Upgrade test database
    subprocess.run(['python3', 'src/scripts/import_data.py', 'src/scripts/test_data.tsv', '--database', 'test'])  # Import test data

