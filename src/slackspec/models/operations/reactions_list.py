"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class ReactionsListSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class ReactionsListRequest:
    
    token: str = dataclasses.field(metadata={'query_param': { 'field_name': 'token', 'style': 'form', 'explode': True }})
    r"""Authentication token. Requires scope: `reactions:read`"""
    count: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'count', 'style': 'form', 'explode': True }})
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Parameter for pagination. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \\"page\\" of the collection. See [pagination](/docs/pagination) for more details."""
    full: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'full', 'style': 'form', 'explode': True }})
    r"""If true always return the complete reaction list."""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached."""
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    user: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user', 'style': 'form', 'explode': True }})
    r"""Show reactions made by this user. Defaults to the authed user."""
    

@dataclasses.dataclass
class ReactionsListResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    reactions_list_error_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response"""
    reactions_list_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response"""
    