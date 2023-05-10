"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class AdminEmojiAddAliasSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class AdminEmojiAddAliasRequestBody:
    
    alias_for: str = dataclasses.field(metadata={'form': { 'field_name': 'alias_for' }})
    r"""The alias of the emoji."""
    name: str = dataclasses.field(metadata={'form': { 'field_name': 'name' }})
    r"""The name of the emoji to be aliased. Colons (`:myemoji:`) around the value are not required, although they may be included."""
    token: str = dataclasses.field(metadata={'form': { 'field_name': 'token' }})
    r"""Authentication token. Requires scope: `admin.teams:write`"""
    

@dataclasses.dataclass
class AdminEmojiAddAliasResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    default_error_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response"""
    default_success_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    