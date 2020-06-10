#!/usr/bin/python3
"""
    Base class for the proyect
"""


import json
import csv


class Base:
    """[summary]

    Returns:
        [type]: [description]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        self.id = None
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """
        if list_dictionaries is not None:
            new_json_array = []
            for dictionary in list_dictionaries:
                new_json_array.append(dictionary)
            else:
                return json.dumps(new_json_array)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        towrite = []
        with open(cls.__name__ + ".json", mode='w+') as file:
            if list_objs is None:
                file.write(cls.to_json_string(None))
            else:
                for obj in list_objs:
                    towrite.append(obj.to_dictionary())
                else:
                    file.write(cls.to_json_string(towrite))

    @staticmethod
    def from_json_string(json_string):
        """[summary]

        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """[summary]

        Returns:
            [type]: [description]
        """
        new_instance = cls(**dictionary)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """[summary]

        Returns:
            [type]: [description]
        """
        instances = []
        try:
            with open(cls.__name__ + ".json", "r") as jsonfile:
                load = cls.from_json_string(jsonfile.read())
                for dictionary in load:
                    instances.append(cls.create(**dictionary))
                else:
                    return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        with open(cls.__name__ + '.csv', 'w') as f:
            if list_objs is None:
                f.write([])
            else:
                for obj in list_objs:
                    x = obj.to_dictionary().keys()
                    w = csv.DictWriter(f, fieldnames=x)
                    w.writeheader()
                    w.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """[summary]
        Returns:
            [type]: [description]
        """
        instances = []
        keys = []
        v1 = []
        c = 0
        try:
            with open(cls.__name__ + '.csv', mode='r') as infile:
                reader = csv.reader(infile)
                for dictionary in reader:
                    if c % 2 == 0:
                        keys.append(dictionary)
                    else:
                        v1.append(dictionary)
                    c += 1
                else:
                    c = 0
                    for k in keys:
                        for v in range(len(v1)):
                            n = {k1: int(val) for k1, val in zip(k, v1[v + c])}
                            instances.append(cls.create(**n))
                            c += 1
                            break
        except FileNotFoundError:
            return []
        return instances
