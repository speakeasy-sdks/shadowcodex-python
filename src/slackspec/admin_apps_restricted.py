"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from slackspec.models import operations
from typing import Any, Optional

class AdminAppsRestricted:
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
        
    
    def admin_apps_restricted_list(self, request: operations.AdminAppsRestrictedListRequest, security: operations.AdminAppsRestrictedListSecurity) -> operations.AdminAppsRestrictedListResponse:
        r"""List restricted apps for an org or workspace.
        https://api.slack.com/methods/admin.apps.restricted.list - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/admin.apps.restricted.list'
        
        query_params = utils.get_query_params(operations.AdminAppsRestrictedListRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AdminAppsRestrictedListResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    