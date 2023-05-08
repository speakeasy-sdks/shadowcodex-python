"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class AdminUsergroupsListChannelsSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class AdminUsergroupsListChannelsRequest:
    
    token: str = dataclasses.field(metadata={'header': { 'field_name': 'token', 'style': 'simple', 'explode': False }})
    r"""Authentication token. Requires scope: `admin.usergroups:read`"""
    usergroup_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'usergroup_id', 'style': 'form', 'explode': True }})
    r"""ID of the IDP group to list default channels for."""
    include_num_members: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include_num_members', 'style': 'form', 'explode': True }})
    r"""Flag to include or exclude the count of members per channel."""
    team_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'team_id', 'style': 'form', 'explode': True }})
    r"""ID of the the workspace."""
    

@dataclasses.dataclass
class AdminUsergroupsListChannelsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    default_error_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response if the token provided is not associated with an Org Admin or Owner"""
    default_success_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    