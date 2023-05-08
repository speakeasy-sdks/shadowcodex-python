# admin_apps_requests

### Available Operations

* [admin_apps_requests_list](#admin_apps_requests_list) - List app requests for a team/workspace.

## admin_apps_requests_list

List app requests for a team/workspace.

API method documentation
<https://api.slack.com/methods/admin.apps.requests.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminAppsRequestsListRequest(
    cursor='amet',
    limit=643990,
    team_id='nisi',
    token='vel',
)

res = s.admin_apps_requests.admin_apps_requests_list(req, operations.AdminAppsRequestsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
