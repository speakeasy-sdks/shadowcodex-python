"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from slackspec.models import operations
from typing import Any, Optional

class Calls:
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
        
    
    def calls_add(self, request: operations.CallsAddRequest, security: operations.CallsAddSecurity) -> operations.CallsAddResponse:
        r"""Registers a new Call.
        https://api.slack.com/methods/calls.add - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/calls.add'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CallsAddResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    
    def calls_end(self, request: operations.CallsEndRequest, security: operations.CallsEndSecurity) -> operations.CallsEndResponse:
        r"""Ends a Call.
        https://api.slack.com/methods/calls.end - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/calls.end'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CallsEndResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    
    def calls_info(self, request: operations.CallsInfoRequest, security: operations.CallsInfoSecurity) -> operations.CallsInfoResponse:
        r"""Returns information about a Call.
        https://api.slack.com/methods/calls.info - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/calls.info'
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.CallsInfoRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CallsInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    
    def calls_participants_add(self, request: operations.CallsParticipantsAddRequest, security: operations.CallsParticipantsAddSecurity) -> operations.CallsParticipantsAddResponse:
        r"""Registers new participants added to a Call.
        https://api.slack.com/methods/calls.participants.add - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/calls.participants.add'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CallsParticipantsAddResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    
    def calls_participants_remove(self, request: operations.CallsParticipantsRemoveRequest, security: operations.CallsParticipantsRemoveSecurity) -> operations.CallsParticipantsRemoveResponse:
        r"""Registers participants removed from a Call.
        https://api.slack.com/methods/calls.participants.remove - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/calls.participants.remove'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CallsParticipantsRemoveResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    
    def calls_update(self, request: operations.CallsUpdateRequest, security: operations.CallsUpdateSecurity) -> operations.CallsUpdateResponse:
        r"""Updates information about a Call.
        https://api.slack.com/methods/calls.update - API method documentation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/calls.update'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CallsUpdateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_success_template = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, dict[str, Any]]])
                res.default_error_template = out

        return res

    