# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rexample.proto\"*\n\x07Request\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"i\n\x08Response\x12+\n\tresponses\x18\x01 \x03(\x0b\x32\x18.Response.ResponsesEntry\x1a\x30\n\x0eResponsesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1b\n\tAllAgents\x12\x0e\n\x06\x61gents\x18\x01 \x03(\t\"\x8a\x01\n\x0b\x41gentFields\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\t\x12\x13\n\x06sender\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04type\x18\x05 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_senderB\n\n\x08_messageB\x07\n\x05_type\"\x07\n\x05\x45mpty2\x82\x01\n\x05\x41gent\x12&\n\rHandleMessage\x12\x08.Request\x1a\t.Response\"\x00\x12!\n\tGetAgents\x12\x06.Empty\x1a\n.AllAgents\"\x00\x12.\n\x0eSetAgentFields\x12\x0c.AgentFields\x1a\x0c.AgentFields\"\x00\x62\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='Request.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='Request.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=59,
)


_RESPONSE_RESPONSESENTRY = _descriptor.Descriptor(
  name='ResponsesEntry',
  full_name='Response.ResponsesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Response.ResponsesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Response.ResponsesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=166,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='Response.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_RESPONSESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=166,
)


_ALLAGENTS = _descriptor.Descriptor(
  name='AllAgents',
  full_name='AllAgents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='agents', full_name='AllAgents.agents', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=195,
)


_AGENTFIELDS = _descriptor.Descriptor(
  name='AgentFields',
  full_name='AgentFields',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='AgentFields.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='context', full_name='AgentFields.context', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='AgentFields.sender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='AgentFields.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='AgentFields.type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_sender', full_name='AgentFields._sender',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_message', full_name='AgentFields._message',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_type', full_name='AgentFields._type',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=198,
  serialized_end=336,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=345,
)

_RESPONSE_RESPONSESENTRY.containing_type = _RESPONSE
_RESPONSE.fields_by_name['responses'].message_type = _RESPONSE_RESPONSESENTRY
_AGENTFIELDS.oneofs_by_name['_sender'].fields.append(
  _AGENTFIELDS.fields_by_name['sender'])
_AGENTFIELDS.fields_by_name['sender'].containing_oneof = _AGENTFIELDS.oneofs_by_name['_sender']
_AGENTFIELDS.oneofs_by_name['_message'].fields.append(
  _AGENTFIELDS.fields_by_name['message'])
_AGENTFIELDS.fields_by_name['message'].containing_oneof = _AGENTFIELDS.oneofs_by_name['_message']
_AGENTFIELDS.oneofs_by_name['_type'].fields.append(
  _AGENTFIELDS.fields_by_name['type'])
_AGENTFIELDS.fields_by_name['type'].containing_oneof = _AGENTFIELDS.oneofs_by_name['_type']
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['AllAgents'] = _ALLAGENTS
DESCRIPTOR.message_types_by_name['AgentFields'] = _AGENTFIELDS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {

  'ResponsesEntry' : _reflection.GeneratedProtocolMessageType('ResponsesEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_RESPONSESENTRY,
    '__module__' : 'example_pb2'
    # @@protoc_insertion_point(class_scope:Response.ResponsesEntry)
    })
  ,
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.ResponsesEntry)

AllAgents = _reflection.GeneratedProtocolMessageType('AllAgents', (_message.Message,), {
  'DESCRIPTOR' : _ALLAGENTS,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:AllAgents)
  })
_sym_db.RegisterMessage(AllAgents)

AgentFields = _reflection.GeneratedProtocolMessageType('AgentFields', (_message.Message,), {
  'DESCRIPTOR' : _AGENTFIELDS,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:AgentFields)
  })
_sym_db.RegisterMessage(AgentFields)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)


_RESPONSE_RESPONSESENTRY._options = None

_AGENT = _descriptor.ServiceDescriptor(
  name='Agent',
  full_name='Agent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=348,
  serialized_end=478,
  methods=[
  _descriptor.MethodDescriptor(
    name='HandleMessage',
    full_name='Agent.HandleMessage',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAgents',
    full_name='Agent.GetAgents',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_ALLAGENTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetAgentFields',
    full_name='Agent.SetAgentFields',
    index=2,
    containing_service=None,
    input_type=_AGENTFIELDS,
    output_type=_AGENTFIELDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENT)

DESCRIPTOR.services_by_name['Agent'] = _AGENT

# @@protoc_insertion_point(module_scope)
