# flake8: NOQA
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: optuna/protobuf/session.proto

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import reflection as _reflection
from google.protobuf import message as _message
from google.protobuf import descriptor as _descriptor
import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='optuna/protobuf/session.proto',
    package='optuna.protobuf',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\x1doptuna/protobuf/session.proto\x12\x0foptuna.protobuf\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\"N\n\x16SessionAllocateRequest\x12\x34\n\x11keepalive_timeout\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\" \n\nSessionRef\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x32\xfb\x01\n\x07Session\x12Z\n\x10\x61llocate_session\x12\'.optuna.protobuf.SessionAllocateRequest\x1a\x1b.optuna.protobuf.SessionRef\"\x00\x12H\n\x0frelease_session\x12\x1b.optuna.protobuf.SessionRef\x1a\x16.google.protobuf.Empty\"\x00\x12J\n\x11heartbeat_session\x12\x1b.optuna.protobuf.SessionRef\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'),
    dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR, google_dot_protobuf_dot_empty__pb2.DESCRIPTOR, ])


_SESSIONALLOCATEREQUEST = _descriptor.Descriptor(
    name='SessionAllocateRequest',
    full_name='optuna.protobuf.SessionAllocateRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='keepalive_timeout', full_name='optuna.protobuf.SessionAllocateRequest.keepalive_timeout', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=111,
    serialized_end=189,
)


_SESSIONREF = _descriptor.Descriptor(
    name='SessionRef',
    full_name='optuna.protobuf.SessionRef',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='session_id', full_name='optuna.protobuf.SessionRef.session_id', index=0,
            number=1, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=191,
    serialized_end=223,
)

_SESSIONALLOCATEREQUEST.fields_by_name['keepalive_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['SessionAllocateRequest'] = _SESSIONALLOCATEREQUEST
DESCRIPTOR.message_types_by_name['SessionRef'] = _SESSIONREF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionAllocateRequest = _reflection.GeneratedProtocolMessageType('SessionAllocateRequest', (_message.Message,), dict(
    DESCRIPTOR=_SESSIONALLOCATEREQUEST,
    __module__='optuna.protobuf.session_pb2'
    # @@protoc_insertion_point(class_scope:optuna.protobuf.SessionAllocateRequest)
))
_sym_db.RegisterMessage(SessionAllocateRequest)

SessionRef = _reflection.GeneratedProtocolMessageType('SessionRef', (_message.Message,), dict(
    DESCRIPTOR=_SESSIONREF,
    __module__='optuna.protobuf.session_pb2'
    # @@protoc_insertion_point(class_scope:optuna.protobuf.SessionRef)
))
_sym_db.RegisterMessage(SessionRef)


_SESSION = _descriptor.ServiceDescriptor(
    name='Session',
    full_name='optuna.protobuf.Session',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=226,
    serialized_end=477,
    methods=[
        _descriptor.MethodDescriptor(
            name='allocate_session',
            full_name='optuna.protobuf.Session.allocate_session',
            index=0,
            containing_service=None,
            input_type=_SESSIONALLOCATEREQUEST,
            output_type=_SESSIONREF,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='release_session',
            full_name='optuna.protobuf.Session.release_session',
            index=1,
            containing_service=None,
            input_type=_SESSIONREF,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='heartbeat_session',
            full_name='optuna.protobuf.Session.heartbeat_session',
            index=2,
            containing_service=None,
            input_type=_SESSIONREF,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_SESSION)

DESCRIPTOR.services_by_name['Session'] = _SESSION

# @@protoc_insertion_point(module_scope)