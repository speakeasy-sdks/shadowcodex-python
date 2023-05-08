# admin_teams_admins

### Available Operations

* [admin_teams_admins_list](#admin_teams_admins_list) - List all of the admins on a given workspace.

## admin_teams_admins_list

List all of the admins on a given workspace.

API method documentation
<https://api.slack.com/methods/admin.teams.admins.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsAdminsListRequest(
    cursor='quaerat',
    limit=554242,
    team_id='aliquid',
    token='dolorem',
)

res = s.admin_teams_admins.admin_teams_admins_list(req, operations.AdminTeamsAdminsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
