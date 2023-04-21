import json
import turtle


class Base:
    """
    base model
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new base
        Args:
            id (int): object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: dict):
        """Return json"""
        if list_dictionaries is None or list_directories == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save te json file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """change JSON string representation `json_string` to a list"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a object from dictionary"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        elif cls.__name__ == "Square":
            new = cls(10, 10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """return file"""
        filename = cls.__name__ + ".json"
        object_created = []
        with open(filename, 'r') as f:
            file_string = f.read().replace('\n', '')
            data = cls.from_json_string(file_string)
            for el in data:
                object_created.append(cls.create(**el))

        return object_created

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        filename = cls.__name__ + ".csv"
        itm = ""
        text = []
        if list_objs is not None:
            itm += ','.join(list_objs[0].to_dictionary().keys())
            itm += '\n'
            for lst in list_objs:
                itm += ','.join(
                    map(str, lst.to_dictionary().values())
                )
                itm += '\n'

        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(itm)

    @classmethod
    def load_from_file_csv(cls):
        """Return file from csv"""
        filename = cls.__name__ + ".csv"
        object_created = []

        with open(filename, 'r') as f:
            header = f.readline().replace('\n', '').split(',')
            for el in f.readlines():
                values = map(int, el.replace('\n', '').split(','))
                data = dict(zip(header, values))
                object_created.append(cls.create(**data))

        return object_created

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """draw figure
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
