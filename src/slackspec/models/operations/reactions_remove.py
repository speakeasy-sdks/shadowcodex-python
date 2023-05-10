"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from slackspec import utils
from typing import Any, Optional


@dataclasses.dataclass
class ReactionsRemoveSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReactionsRemoveApplicationJSON:
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Reaction (emoji) name."""
    channel: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel'), 'exclude': lambda f: f is None }})
    r"""Channel where the message to remove reaction from was posted."""
    file: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file'), 'exclude': lambda f: f is None }})
    r"""File to remove reaction from."""
    file_comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_comment'), 'exclude': lambda f: f is None }})
    r"""File comment to remove reaction from."""
    timestamp: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'exclude': lambda f: f is None }})
    r"""Timestamp of the message to remove reaction from."""
    

@dataclasses.dataclass
class ReactionsRemoveRequest:
    
    request_body: ReactionsRemoveApplicationJSON = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    token: str = dataclasses.field(metadata={'header': { 'field_name': 'token', 'style': 'simple', 'explode': False }})
    r"""Authentication token. Requires scope: `reactions:write`"""
    

@dataclasses.dataclass
class ReactionsRemoveResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    reactions_remove_error_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response"""
    reactions_remove_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response"""
    