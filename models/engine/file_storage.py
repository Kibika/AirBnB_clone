#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
	returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """ file storage
        """
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            json.dump(dict_to_json, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except:
            pass
