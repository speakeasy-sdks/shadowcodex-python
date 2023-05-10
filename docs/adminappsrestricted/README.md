# admin_apps_restricted

### Available Operations

* [admin_apps_restricted_list](#admin_apps_restricted_list) - List restricted apps for an org or workspace.

## admin_apps_restricted_list

List restricted apps for an org or workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.restricted.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsRestrictedListRequest(
    cursor='natus',
    enterprise_id='omnis',
    limit=474867,
    team_id='perferendis',
    token='nihil',
)

res = s.admin_apps_restricted.admin_apps_restricted_list(req, operations.AdminAppsRestrictedListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
