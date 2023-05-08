# workflows

### Available Operations

* [workflows_step_completed](#workflows_step_completed) - Indicate that an app's step in a workflow completed execution.
* [workflows_step_failed](#workflows_step_failed) - Indicate that an app's step in a workflow failed to execute.
* [workflows_update_step](#workflows_update_step) - Update the configuration for a workflow extension step.

## workflows_step_completed

Indicate that an app's step in a workflow completed execution.

API method documentation
<https://api.slack.com/methods/workflows.stepCompleted>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.WorkflowsStepCompletedRequest(
    outputs='vitae',
    token='rerum',
    workflow_step_execute_id='tempora',
)

res = s.workflows.workflows_step_completed(req, operations.WorkflowsStepCompletedSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## workflows_step_failed

Indicate that an app's step in a workflow failed to execute.

API method documentation
<https://api.slack.com/methods/workflows.stepFailed>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.WorkflowsStepFailedRequest(
    error='quis',
    token='inventore',
    workflow_step_execute_id='fugit',
)

res = s.workflows.workflows_step_failed(req, operations.WorkflowsStepFailedSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## workflows_update_step

Update the configuration for a workflow extension step.

API method documentation
<https://api.slack.com/methods/workflows.updateStep>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.WorkflowsUpdateStepRequest(
    inputs='cumque',
    outputs='quae',
    step_image_url='perferendis',
    step_name='velit',
    token='aspernatur',
    workflow_step_edit_id='eum',
)

res = s.workflows.workflows_update_step(req, operations.WorkflowsUpdateStepSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
