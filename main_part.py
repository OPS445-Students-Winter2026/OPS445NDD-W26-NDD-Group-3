#!/usr/bin/env python3

"""
assignment2.py
OPS445 Assignment 2
Group 3
Branch: Allen-main

This part focuses on:
- creating required directories
- writing logs
- parsing command-line arguments
- main program flow
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
# MEMBER 3 FUNCTIONS (ALLEN)
# =========================
def ensure_directories():
    """Create required directories if they do not already exist."""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)


def write_log(message, logfile=LOG_FILE):
    """Write a timestamped log entry into the log file."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(logfile, "a") as log:
            log.write(f"[{timestamp}] {message}\n")
    except Exception as err:
        print(f"Error writing log: {err}")


def parse_arguments():
    """Create and parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Data Backup and Restore Tool"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    backup_parser = subparsers.add_parser(
        "backup",
        help="Back up a file or directory"
    )
    backup_parser.add_argument(
        "-s", "--source",
        required=True,
        help="Source path"
    )

    subparsers.add_parser(
        "list",
        help="List all backups"
    )

    restore_parser = subparsers.add_parser(
        "restore",
        help="Restore a backup"
    )
    restore_parser.add_argument(
        "-n", "--name",
        required=True,
        help="Backup name"
    )
    restore_parser.add_argument(
        "-d", "--destination",
        required=True,
        help="Restore destination"
    )

    return parser.parse_args()


def main():
    """Main program logic."""
    ensure_directories()
    args = parse_arguments()

    try:
        if args.command == "backup":
            source = args.source

            if not validate_source(source):
                print("Error: source path does not exist.")
                write_log(f"FAILED BACKUP: source does not exist: {source}")
                sys.exit(1)

            if os.path.isfile(source):
                backup_name = backup_file(source)
            elif os.path.isdir(source):
                backup_name = backup_directory(source)
            else:
                print("Error: source must be a file or directory.")
                write_log(f"FAILED BACKUP: invalid source type: {source}")
                sys.exit(1)

            if backup_name is None:
                print("Backup failed.")
                write_log(f"FAILED BACKUP: could not back up {source}")
                sys.exit(1)

            print("Backup completed successfully.")
            print(f"Source: {source}")
            print(f"Backup Name: {backup_name}")
            print(f"Saved In: {BACKUP_DIR}")
            write_log(f"SUCCESS BACKUP: {source} -> {backup_name}")

        elif args.command == "list":
            backups = list_backups()

            if not backups:
                print("No backups found.")
            else:
                print("Available backups:")
                counter = 1
                for item in backups:
                    print(f"{counter}. {item}")
                    counter += 1

        elif args.command == "restore":
            backup_name = args.name
            destination = args.destination

            if not validate_destination(destination):
                print("Error: destination path does not exist.")
                write_log(f"FAILED RESTORE: destination does not exist: {destination}")
                sys.exit(1)

            restored_path = restore_backup(backup_name, BACKUP_DIR, destination)

            if restored_path is None:
                print("Restore failed.")
                write_log(f"FAILED RESTORE: could not restore {backup_name}")
                sys.exit(1)

            print("Restore completed successfully.")
            print(f"Backup Name: {backup_name}")
            print(f"Restored To: {restored_path}")
            write_log(f"SUCCESS RESTORE: {backup_name} -> {restored_path}")

    except FileExistsError:
        print("Error: target already exists.")
        write_log("FAILED: target already exists")
        sys.exit(1)

    except PermissionError:
        print("Error: permission denied.")
        write_log("FAILED: permission denied")
        sys.exit(1)

    except FileNotFoundError as err:
        print(f"Error: {err}")
        write_log(f"FAILED: {err}")
        sys.exit(1)

    except Exception as err:
        print(f"Unexpected error: {err}")
        write_log(f"FAILED: unexpected error: {err}")
        sys.exit(1)


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


if __name__ == "__main__":
    main()
