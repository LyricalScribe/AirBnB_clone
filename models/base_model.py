import uuid
from datetime import datetime
from models import storage
"""The Base model which will be inherited across all class
"""


class BaseModel:
    """The class module doc"""

    def __init__(self, *args, **kwargs):
        """
        The initialisation method that invokes on each call of the Basemodel
        """
        if kwargs:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(kwargs[key], f)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Prints string format for our model"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates with new time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary for our Class"""
        my_dict = {}

        my_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                my_dict[k] = v.isoformat()
            else:
                my_dict[k] = v
        return my_dict
