# pre_install.py

import subprocess
import sys
import platform


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        result.check_returncode()
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(e.stderr.strip())


def install_package(command, package_name):
    try:
        output = run_command(command)
        print(output)
        return output
    except RuntimeError as e:
        raise RuntimeError(f"Failed to install {package_name}: {e}")


def check_and_install():
    pass


if __name__ == "__main__":
    check_and_install()
