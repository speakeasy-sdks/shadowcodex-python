"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DialogOpenSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class DialogOpenRequest:
    
    dialog: str = dataclasses.field(metadata={'query_param': { 'field_name': 'dialog', 'style': 'form', 'explode': True }})
    r"""The dialog definition. This must be a JSON-encoded string."""
    token: str = dataclasses.field(metadata={'header': { 'field_name': 'token', 'style': 'simple', 'explode': False }})
    r"""Authentication token. Requires scope: `none`"""
    trigger_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'trigger_id', 'style': 'form', 'explode': True }})
    r"""Exchange a trigger to post to the user."""
    

@dataclasses.dataclass
class DialogOpenResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dialog_open_error_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response, before getting to any possible validation errors."""
    dialog_open_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response is quite minimal."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    