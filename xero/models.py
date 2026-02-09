import pprint
from functools import singledispatch


class BaseModel:
    openapi_types = {}
    attribute_map = {}

    def to_dict(self):
        return {
            key: serialize_to_dict(getattr(self, key))
            for key in self.openapi_types.keys()
        }

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other


@singledispatch
def serialize_to_dict(value):
    return value


@serialize_to_dict.register(BaseModel)
def serialize_model_to_dict(value):
    return value.to_dict()


@serialize_to_dict.register(list)
def serialize_list_to_dict(value):
    return [serialize_to_dict(item) for item in value]


@serialize_to_dict.register(tuple)
def serialize_tuple_to_dict(value):
    return tuple(serialize_to_dict(item) for item in value)


@serialize_to_dict.register(dict)
def serialize_dict_to_dict(value):
    return {key: serialize_to_dict(val) for key, val in value.items()}
