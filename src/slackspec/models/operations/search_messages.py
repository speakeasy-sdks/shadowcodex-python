"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class SearchMessagesSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class SearchMessagesRequest:
    
    query: str = dataclasses.field(metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Search query."""
    token: str = dataclasses.field(metadata={'query_param': { 'field_name': 'token', 'style': 'form', 'explode': True }})
    r"""Authentication token. Requires scope: `search:read`"""
    count: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'count', 'style': 'form', 'explode': True }})
    r"""Pass the number of results you want per \\"page\\". Maximum of `100`."""
    highlight: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'highlight', 'style': 'form', 'explode': True }})
    r"""Pass a value of `true` to enable query highlight markers (see below)."""
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    r"""Return matches sorted by either `score` or `timestamp`."""
    sort_dir: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort_dir', 'style': 'form', 'explode': True }})
    r"""Change sort direction to ascending (`asc`) or descending (`desc`)."""
    

@dataclasses.dataclass
class SearchMessagesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    default_error_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response"""
    default_success_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    