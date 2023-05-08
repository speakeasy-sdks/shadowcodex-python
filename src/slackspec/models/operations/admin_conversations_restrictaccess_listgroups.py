"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class AdminConversationsRestrictAccessListGroupsSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class AdminConversationsRestrictAccessListGroupsRequest:
    
    channel_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'channel_id', 'style': 'form', 'explode': True }})
    token: str = dataclasses.field(metadata={'query_param': { 'field_name': 'token', 'style': 'form', 'explode': True }})
    r"""Authentication token. Requires scope: `admin.conversations:read`"""
    team_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'team_id', 'style': 'form', 'explode': True }})
    r"""The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization."""
    

@dataclasses.dataclass
class AdminConversationsRestrictAccessListGroupsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    default_error_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response"""
    default_success_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    