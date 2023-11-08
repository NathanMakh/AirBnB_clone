#!/usr/bin/python3
<<<<<<< HEAD
""" FileStorage instance """

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
=======
""" init models """

from models.engine.file_storage import FileStorage
>>>>>>> 3f9ac9f0df72516a04cb800e47fc59f817f986f5

storage = FileStorage()
storage.reload()
