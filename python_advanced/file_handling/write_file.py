#!/usr/bin/env python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """Write text and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
