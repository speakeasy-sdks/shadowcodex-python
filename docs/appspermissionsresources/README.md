# apps_permissions_resources

### Available Operations

* [apps_permissions_resources_list](#apps_permissions_resources_list) - Returns list of resource grants this app has on a team.

## apps_permissions_resources_list

Returns list of resource grants this app has on a team.

API method documentation
<https://api.slack.com/methods/apps.permissions.resources.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsPermissionsResourcesListRequest(
    cursor='incidunt',
    limit=132068,
    token='dolores',
)

res = s.apps_permissions_resources.apps_permissions_resources_list(req, operations.AppsPermissionsResourcesListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.apps_permissions_resources_list_success_schema is not None:
    # handle response
```
