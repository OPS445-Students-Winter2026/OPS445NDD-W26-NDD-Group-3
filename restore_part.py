#!/usr/bin/env python3

"""
assignment2.py
OPS445 Assignment 2
Group 3
Branch: Jordan-restore

This part focuses on:
- listing backups
- validating destination
- restoring backups
"""

import os
import sys
import shutil
import argparse
from datetime import datetime

BACKUP_DIR = "backups"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "backup_restore.log")


# =========================
# MEMBER 3 PLACEHOLDER
# =========================
def ensure_directories():
    """Create required directories if they do not already exist."""
    pass


# =========================
# MEMBER 1 PLACEHOLDER
# =========================
def validate_source(path):
    """Return True if source path exists, otherwise False."""
    pass


def create_backup_name(source):
    """Create a timestamped backup name."""
    pass


def backup_file(source, backup_dir=BACKUP_DIR):
    """Back up a file."""
    pass


def backup_directory(source, backup_dir=BACKUP_DIR):
    """Back up a directory."""
    pass


# =========================
# MEMBER 2 FUNCTIONS (JORDAN)
# =========================

def validate_destination(path):
    """Return True if destination path exists, otherwise False."""
    return os.path.exists(path)


def list_backups(backup_dir=BACKUP_DIR):
    """Return a sorted list of available backups."""
    try:
        if not os.path.exists(backup_dir):
            return []

        backups = os.listdir(backup_dir)
        backups.sort()
        return backups

    except Exception as err:
        print(f"Error listing backups: {err}")
        return []


def restore_backup(backup_name, backup_dir, destination):
    """Restore the selected backup into the destination directory."""
    try:
        backup_path = os.path.join(backup_dir, backup_name)

        if not os.path.exists(backup_path):
            raise FileNotFoundError("Backup not found.")

        if not os.path.exists(destination):
            raise FileNotFoundError("Destination path does not exist.")

        target_path = os.path.join(destination, backup_name)

        if os.path.isfile(backup_path):
            shutil.copy2(backup_path, target_path)

        elif os.path.isdir(backup_path):
            shutil.copytree(backup_path, target_path)

        else:
            raise Exception("Backup item is neither file nor directory.")

        return target_path

    except Exception as err:
        print(f"Error restoring backup: {err}")
        return None


# =========================
# MEMBER 3 PLACEHOLDER
# =========================
def write_log(message, logfile=LOG_FILE):
    """Write a timestamped log entry into the log file."""
    pass


def parse_arguments():
    """Create and parse command-line arguments."""
    pass


def main():
    """Main program logic."""
    pass


if __name__ == "__main__":
    main()
