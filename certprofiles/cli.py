"""Inspect certificate profile bundles."""
import argparse

from .checker import check_profiles

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    for issue in check_profiles(args.path):
        print(issue)

if __name__ == "__main__":
    main()
