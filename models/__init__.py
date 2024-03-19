#!/usr/bin/python3
"""
This module is the __init__ module of
the models package.
It initializes this package.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
