#!/usr/bin/env python3

"""
assignment2.py
OPS445 Assignment 2
Group 3
Branch: bhavya-backup

This part focuses on:
- validating source path
- creating backup names
- backing up files and directories
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
# MEMBER 1 FUNCTIONS (YOU)
# =========================

def validate_source(path):
    """Return True if source path exists, otherwise False."""
    return os.path.exists(path)


def create_backup_name(source):
    """Create a timestamped backup name from the source basename."""
    base_name = os.path.basename(os.path.normpath(source))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}"


def backup_file(source, backup_dir=BACKUP_DIR):
    """Copy a single file into the backup directory."""
    try:
        backup_name = create_backup_name(source)
        destination = os.path.join(backup_dir, backup_name)

        shutil.copy2(source, destination)

        return backup_name

    except Exception as err:
        print(f"Error backing up file: {err}")
        return None


def backup_directory(source, backup_dir=BACKUP_DIR):
    """Copy a directory into the backup directory."""
    try:
        backup_name = create_backup_name(source)
        destination = os.path.join(backup_dir, backup_name)

        shutil.copytree(source, destination)

        return backup_name

    except Exception as err:
        print(f"Error backing up directory: {err}")
        return None


# =========================
# MEMBER 2 PLACEHOLDER
# =========================
def validate_destination(path):
    """Return True if destination path exists, otherwise False."""
    pass


def list_backups(backup_dir=BACKUP_DIR):
    """Return a sorted list of available backups."""
    pass


def restore_backup(backup_name, backup_dir, destination):
    """Restore the selected backup into the destination directory."""
    pass


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
