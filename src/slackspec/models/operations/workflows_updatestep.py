"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class WorkflowsUpdateStepSecurity:
    
    slack_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class WorkflowsUpdateStepRequest:
    
    token: str = dataclasses.field(metadata={'header': { 'field_name': 'token', 'style': 'simple', 'explode': False }})
    r"""Authentication token. Requires scope: `workflow.steps:execute`"""
    workflow_step_edit_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'workflow_step_edit_id', 'style': 'form', 'explode': True }})
    r"""A context identifier provided with `view_submission` payloads used to call back to `workflows.updateStep`."""
    inputs: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'inputs', 'style': 'form', 'explode': True }})
    r"""A JSON key-value map of inputs required from a user during configuration. This is the data your app expects to receive when the workflow step starts. **Please note**: the embedded variable format is set and replaced by the workflow system. You cannot create custom variables that will be replaced at runtime. [Read more about variables in workflow steps here](/workflows/steps#variables)."""
    outputs: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'outputs', 'style': 'form', 'explode': True }})
    r"""An JSON array of output objects used during step execution. This is the data your app agrees to provide when your workflow step was executed."""
    step_image_url: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'step_image_url', 'style': 'form', 'explode': True }})
    r"""An optional field that can be used to override app image that is shown in the Workflow Builder."""
    step_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'step_name', 'style': 'form', 'explode': True }})
    r"""An optional field that can be used to override the step name that is shown in the Workflow Builder."""
    

@dataclasses.dataclass
class WorkflowsUpdateStepResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    default_error_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical error response"""
    default_success_template: Optional[dict[str, dict[str, Any]]] = dataclasses.field(default=None)
    r"""Typical success response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    