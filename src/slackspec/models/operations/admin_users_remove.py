"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from slackspec import utils
from typing import Any, Optional


@dataclasses.dataclass
class AdminUsersRemoveSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AdminUsersRemoveApplicationJSON:
    
    team_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('team_id') }})
    r"""The ID (`T1234`) of the workspace."""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    r"""The ID of the user to remove."""
    

@dataclasses.dataclass
class AdminUsersRemoveRequest:
    
    request_body: AdminUsersRemoveApplicationJSON = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    token: str = dataclasses.field(metadata={'header': { 'field_name': 'token', 'style': 'simple', 'explode': False }})
    r"""Authentication token. Requires scope: `admin.users:write`"""
    

@dataclasses.dataclass
class AdminUsersRemoveResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    default_error_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response"""
    default_success_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    