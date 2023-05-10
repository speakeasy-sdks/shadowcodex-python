"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from slackspec.models import operations
from typing import Any, Optional

class Team:
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
        
    
    def team_access_logs(self, request: operations.TeamAccessLogsRequest, security: operations.TeamAccessLogsSecurity) -> operations.TeamAccessLogsResponse:
        r"""Gets the access logs for the current team.
        https://api.slack.com/methods/team.accessLogs - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/team.accessLogs'
        
        query_params = utils.get_query_params(operations.TeamAccessLogsRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TeamAccessLogsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.team_access_logs_schema = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.team_access_logs_error_schema = out

        return res

    
    def team_billable_info(self, request: operations.TeamBillableInfoRequest, security: operations.TeamBillableInfoSecurity) -> operations.TeamBillableInfoResponse:
        r"""Gets billable users information for the current team.
        https://api.slack.com/methods/team.billableInfo - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/team.billableInfo'
        
        query_params = utils.get_query_params(operations.TeamBillableInfoRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TeamBillableInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    
    def team_info(self, request: operations.TeamInfoRequest, security: operations.TeamInfoSecurity) -> operations.TeamInfoResponse:
        r"""Gets information about the current team.
        https://api.slack.com/methods/team.info - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/team.info'
        
        query_params = utils.get_query_params(operations.TeamInfoRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TeamInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.team_info_schema = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.team_info_error_schema = out

        return res

    
    def team_integration_logs(self, request: operations.TeamIntegrationLogsRequest, security: operations.TeamIntegrationLogsSecurity) -> operations.TeamIntegrationLogsResponse:
        r"""Gets the integration logs for the current team.
        https://api.slack.com/methods/team.integrationLogs - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/team.integrationLogs'
        
        query_params = utils.get_query_params(operations.TeamIntegrationLogsRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TeamIntegrationLogsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.team_integration_logs_schema = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.team_integration_logs_error_schema = out

        return res

    
    def team_profile_get(self, request: operations.TeamProfileGetRequest, security: operations.TeamProfileGetSecurity) -> operations.TeamProfileGetResponse:
        r"""Retrieve a team's profile.
        https://api.slack.com/methods/team.profile.get - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/team.profile.get'
        
        query_params = utils.get_query_params(operations.TeamProfileGetRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TeamProfileGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.team_profile_get_success_schema = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.team_profile_get_error_schema = out

        return res

    