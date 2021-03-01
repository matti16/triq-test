import os


def get_resource_path(name: str):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "resources", name)
    return path
