# apps_permissions

### Available Operations

* [apps_permissions_info](#apps_permissions_info) - Returns list of permissions this app has on a team.
* [apps_permissions_request](#apps_permissions_request) - Allows an app to request additional scopes

## apps_permissions_info

Returns list of permissions this app has on a team.

API method documentation
<https://api.slack.com/methods/apps.permissions.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsPermissionsInfoRequest(
    token='soluta',
)

res = s.apps_permissions.apps_permissions_info(req, operations.AppsPermissionsInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.apps_permissions_info_schema is not None:
    # handle response
```

## apps_permissions_request

Allows an app to request additional scopes

API method documentation
<https://api.slack.com/methods/apps.permissions.request>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsPermissionsRequestRequest(
    scopes='dicta',
    token='laborum',
    trigger_id='totam',
)

res = s.apps_permissions.apps_permissions_request(req, operations.AppsPermissionsRequestSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.apps_permissions_request_schema is not None:
    # handle response
```
