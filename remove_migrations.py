# remove_migrations.py

from unipath import Path

this_file = Path(__file__).absolute()
current_dir = this_file.parent
dir_list = current_dir.listdir()

for paths in dir_list:
    migration_folder = paths.child('migrations')
    if migration_folder.exists():
        list_files = migration_folder.listdir()
        for files in list_files:
            if not ('__pycache__') in files:
                split = files.components()
                if split[-1] != Path('__init__.py'):
                    files.remove()
