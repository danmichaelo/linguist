# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protocol-buffer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protocol-buffer.proto',
  package='persons',
  serialized_pb='\n\x15protocol-buffer.proto\x12\x07persons\"\x16\n\x06Person\x12\x0c\n\x04name\x18\x01 \x02(\t')




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='persons.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='persons.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=34,
  serialized_end=56,
)

DESCRIPTOR.message_types_by_name['Person'] = _PERSON

class Person(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PERSON

  # @@protoc_insertion_point(class_scope:persons.Person)


# @@protoc_insertion_point(module_scope)
