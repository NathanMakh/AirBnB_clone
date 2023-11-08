<<<<<<< HEAD
#!/usr/bin/python3
""" FileStorage instance """


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State

storage = FileStorage()
storage.reload()
=======
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""CNC - dictionary = { Class Name (string) : Class Type }"""

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    from models.engine import db_storage
    CNC = db_storage.DBStorage.CNC
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    CNC = file_storage.FileStorage.CNC
    storage = file_storage.FileStorage()

storage.reload()
>>>>>>> 26ff94de27ea6b5d9f5ee96f010aa565168d547d
