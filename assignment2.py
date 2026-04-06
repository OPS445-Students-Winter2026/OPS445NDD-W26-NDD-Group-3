#!/usr/bin/env python3

import os
import sys
import shutil
import argparse
from datetime import datetime

BACKUP_DIR = "backups"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "backup_restore.log")


# =========================
# BACKUP FUNCTIONS (Bhavya)
# =========================
def validate_source(path):
    return os.path.exists(path)


def create_backup_name(source):
    base = os.path.basename(source)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base}_{timestamp}"


def backup_file(source, backup_dir=BACKUP_DIR):
    name = create_backup_name(source)
    dest = os.path.join(backup_dir, name)
    shutil.copy2(source, dest)
    return name


def backup_directory(source, backup_dir=BACKUP_DIR):
    name = create_backup_name(source)
    dest = os.path.join(backup_dir, name)
    shutil.copytree(source, dest)
    return name


# =========================
# RESTORE FUNCTIONS (Jordan)
# =========================
def validate_destination(path):
    return os.path.exists(path)


def list_backups(backup_dir=BACKUP_DIR):
    if not os.path.exists(backup_dir):
        return []
    return sorted(os.listdir(backup_dir))


def restore_backup(name, backup_dir, destination):
    src = os.path.join(backup_dir, name)
    dest = os.path.join(destination, name)

    if os.path.isfile(src):
        shutil.copy2(src, dest)
    else:
        shutil.copytree(src, dest)

    return dest


# =========================
# MAIN + LOG (Allen)
# =========================
def ensure_directories():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)


def write_log(msg):
    with open(LOG_FILE, "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] {msg}\n")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Backup Tool")
    sub = parser.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("backup")
    b.add_argument("-s", "--source", required=True)

    sub.add_parser("list")

    r = sub.add_parser("restore")
    r.add_argument("-n", "--name", required=True)
    r.add_argument("-d", "--destination", required=True)

    return parser.parse_args()


def main():
    ensure_directories()
    args = parse_arguments()

    if args.cmd == "backup":
        if not validate_source(args.source):
            print("Invalid source")
            return

        if os.path.isfile(args.source):
            name = backup_file(args.source)
        else:
            name = backup_directory(args.source)

        print("Backup done:", name)
        write_log(f"BACKUP {args.source} -> {name}")

    elif args.cmd == "list":
        backups = list_backups()
        for i, b in enumerate(backups, 1):
            print(f"{i}. {b}")

    elif args.cmd == "restore":
        if not validate_destination(args.destination):
            print("Invalid destination")
            return

        path = restore_backup(args.name, BACKUP_DIR, args.destination)
        print("Restored to:", path)
        write_log(f"RESTORE {args.name} -> {path}")


if __name__ == "__main__":
    main()
