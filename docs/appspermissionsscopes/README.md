# apps_permissions_scopes

### Available Operations

* [apps_permissions_scopes_list](#apps_permissions_scopes_list) - Returns list of scopes this app has on a team.

## apps_permissions_scopes_list

Returns list of scopes this app has on a team.

API method documentation
<https://api.slack.com/methods/apps.permissions.scopes.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsPermissionsScopesListRequest(
    token='distinctio',
)

res = s.apps_permissions_scopes.apps_permissions_scopes_list(req, operations.AppsPermissionsScopesListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.api_permissions_scopes_list_success_schema is not None:
    # handle response
```
