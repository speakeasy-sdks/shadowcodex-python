# admin_teams_owners

### Available Operations

* [admin_teams_owners_list](#admin_teams_owners_list) - List all of the owners on a given workspace.

## admin_teams_owners_list

List all of the owners on a given workspace.

API method documentation
<https://api.slack.com/methods/admin.teams.owners.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsOwnersListRequest(
    cursor='dolorem',
    limit=222443,
    team_id='qui',
    token='ipsum',
)

res = s.admin_teams_owners.admin_teams_owners_list(req, operations.AdminTeamsOwnersListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
