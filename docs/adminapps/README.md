# admin_apps

### Available Operations

* [admin_apps_approve](#admin_apps_approve) - Approve an app for installation on a workspace.
* [admin_apps_restrict](#admin_apps_restrict) - Restrict an app for installation on a workspace.

## admin_apps_approve

Approve an app for installation on a workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.approve>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsApproveRequest(
    request_body=operations.AdminAppsApproveApplicationJSON(
        app_id='accusamus',
        request_id='non',
        team_id='occaecati',
    ),
    token='enim',
)

res = s.admin_apps.admin_apps_approve(req, operations.AdminAppsApproveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_apps_restrict

Restrict an app for installation on a workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.restrict>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsRestrictRequest(
    request_body=operations.AdminAppsRestrictApplicationJSON(
        app_id='accusamus',
        request_id='delectus',
        team_id='quidem',
    ),
    token='provident',
)

res = s.admin_apps.admin_apps_restrict(req, operations.AdminAppsRestrictSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
