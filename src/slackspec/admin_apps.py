"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from slackspec.models import operations
from typing import Any, Optional

class AdminApps:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def admin_apps_approve(self, request: operations.AdminAppsApproveRequest, security: operations.AdminAppsApproveSecurity) -> operations.AdminAppsApproveResponse:
        r"""Approve an app for installation on a workspace.
        https://api.slack.com/methods/admin.apps.approve - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/admin.apps.approve'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AdminAppsApproveResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    
    def admin_apps_restrict(self, request: operations.AdminAppsRestrictRequest, security: operations.AdminAppsRestrictSecurity) -> operations.AdminAppsRestrictResponse:
        r"""Restrict an app for installation on a workspace.
        https://api.slack.com/methods/admin.apps.restrict - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/admin.apps.restrict'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AdminAppsRestrictResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    