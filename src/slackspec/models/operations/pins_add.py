"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from slackspec import utils
from typing import Any, Optional


@dataclasses.dataclass
class PinsAddSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PinsAddApplicationJSON:
    
    channel: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel') }})
    r"""Channel to pin the item in."""
    timestamp: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'exclude': lambda f: f is None }})
    r"""Timestamp of the message to pin."""
    

@dataclasses.dataclass
class PinsAddRequest:
    
    request_body: PinsAddApplicationJSON = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    token: str = dataclasses.field(metadata={'header': { 'field_name': 'token', 'style': 'simple', 'explode': False }})
    r"""Authentication token. Requires scope: `pins:write`"""
    

@dataclasses.dataclass
class PinsAddResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    pins_add_error_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response"""
    pins_add_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    