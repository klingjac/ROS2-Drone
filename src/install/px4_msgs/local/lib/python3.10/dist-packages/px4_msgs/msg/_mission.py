# generated from rosidl_generator_py/resource/_idl.py.em
# with input from px4_msgs:msg/Mission.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Mission(type):
    """Metaclass of message 'Mission'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('px4_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'px4_msgs.msg.Mission')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mission
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mission
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mission
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mission
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mission

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mission(metaclass=Metaclass_Mission):
    """Message class 'Mission'."""

    __slots__ = [
        '_timestamp',
        '_dataman_id',
        '_count',
        '_current_seq',
        '_mission_update_counter',
        '_geofence_update_counter',
        '_safe_points_update_counter',
    ]

    _fields_and_field_types = {
        'timestamp': 'uint64',
        'dataman_id': 'uint8',
        'count': 'uint16',
        'current_seq': 'int32',
        'mission_update_counter': 'int16',
        'geofence_update_counter': 'int16',
        'safe_points_update_counter': 'int16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.timestamp = kwargs.get('timestamp', int())
        self.dataman_id = kwargs.get('dataman_id', int())
        self.count = kwargs.get('count', int())
        self.current_seq = kwargs.get('current_seq', int())
        self.mission_update_counter = kwargs.get('mission_update_counter', int())
        self.geofence_update_counter = kwargs.get('geofence_update_counter', int())
        self.safe_points_update_counter = kwargs.get('safe_points_update_counter', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.dataman_id != other.dataman_id:
            return False
        if self.count != other.count:
            return False
        if self.current_seq != other.current_seq:
            return False
        if self.mission_update_counter != other.mission_update_counter:
            return False
        if self.geofence_update_counter != other.geofence_update_counter:
            return False
        if self.safe_points_update_counter != other.safe_points_update_counter:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'timestamp' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'timestamp' field must be an unsigned integer in [0, 18446744073709551615]"
        self._timestamp = value

    @builtins.property
    def dataman_id(self):
        """Message field 'dataman_id'."""
        return self._dataman_id

    @dataman_id.setter
    def dataman_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dataman_id' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'dataman_id' field must be an unsigned integer in [0, 255]"
        self._dataman_id = value

    @builtins.property
    def count(self):
        """Message field 'count'."""
        return self._count

    @count.setter
    def count(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'count' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'count' field must be an unsigned integer in [0, 65535]"
        self._count = value

    @builtins.property
    def current_seq(self):
        """Message field 'current_seq'."""
        return self._current_seq

    @current_seq.setter
    def current_seq(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'current_seq' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'current_seq' field must be an integer in [-2147483648, 2147483647]"
        self._current_seq = value

    @builtins.property
    def mission_update_counter(self):
        """Message field 'mission_update_counter'."""
        return self._mission_update_counter

    @mission_update_counter.setter
    def mission_update_counter(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'mission_update_counter' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'mission_update_counter' field must be an integer in [-32768, 32767]"
        self._mission_update_counter = value

    @builtins.property
    def geofence_update_counter(self):
        """Message field 'geofence_update_counter'."""
        return self._geofence_update_counter

    @geofence_update_counter.setter
    def geofence_update_counter(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'geofence_update_counter' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'geofence_update_counter' field must be an integer in [-32768, 32767]"
        self._geofence_update_counter = value

    @builtins.property
    def safe_points_update_counter(self):
        """Message field 'safe_points_update_counter'."""
        return self._safe_points_update_counter

    @safe_points_update_counter.setter
    def safe_points_update_counter(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'safe_points_update_counter' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'safe_points_update_counter' field must be an integer in [-32768, 32767]"
        self._safe_points_update_counter = value
