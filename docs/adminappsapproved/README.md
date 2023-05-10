# admin_apps_approved

### Available Operations

* [admin_apps_approved_list](#admin_apps_approved_list) - List approved apps for an org or workspace.

## admin_apps_approved_list

List approved apps for an org or workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.approved.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsApprovedListRequest(
    cursor='nam',
    enterprise_id='id',
    limit=501324,
    team_id='deleniti',
    token='sapiente',
)

res = s.admin_apps_approved.admin_apps_approved_list(req, operations.AdminAppsApprovedListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
