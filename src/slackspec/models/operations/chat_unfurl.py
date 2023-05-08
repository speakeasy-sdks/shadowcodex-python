"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from slackspec import utils
from typing import Any, Optional


@dataclasses.dataclass
class ChatUnfurlSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatUnfurlApplicationJSON:
    
    channel: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel') }})
    r"""Channel ID of the message"""
    ts: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ts') }})
    r"""Timestamp of the message to add unfurl behavior to."""
    unfurls: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unfurls'), 'exclude': lambda f: f is None }})
    r"""URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl blocks or message attachments."""
    user_auth_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_auth_message'), 'exclude': lambda f: f is None }})
    r"""Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior"""
    user_auth_required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_auth_required'), 'exclude': lambda f: f is None }})
    r"""Set to `true` or `1` to indicate the user must install your Slack app to trigger unfurls for this domain"""
    user_auth_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_auth_url'), 'exclude': lambda f: f is None }})
    r"""Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded."""
    

@dataclasses.dataclass
class ChatUnfurlRequest:
    
    request_body: ChatUnfurlApplicationJSON = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    token: str = dataclasses.field(metadata={'header': { 'field_name': 'token', 'style': 'simple', 'explode': False }})
    r"""Authentication token. Requires scope: `links:write`"""
    

@dataclasses.dataclass
class ChatUnfurlResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    chat_unfurl_error_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response"""
    chat_unfurl_success_schema: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical, minimal success response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    