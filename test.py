#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel

b = BaseModel()
print(b)

print(storage.all())
