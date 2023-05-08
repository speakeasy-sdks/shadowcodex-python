# admin_teams

### Available Operations

* [admin_teams_create](#admin_teams_create) - Create an Enterprise team.
* [admin_teams_list](#admin_teams_list) - List all teams on an Enterprise organization

## admin_teams_create

Create an Enterprise team.

API method documentation
<https://api.slack.com/methods/admin.teams.create>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsCreateRequest(
    request_body=operations.AdminTeamsCreateApplicationJSON(
        team_description='iste',
        team_discoverability='dolorum',
        team_domain='deleniti',
        team_name='pariatur',
    ),
    token='provident',
)

res = s.admin_teams.admin_teams_create(req, operations.AdminTeamsCreateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_teams_list

List all teams on an Enterprise organization

API method documentation
<https://api.slack.com/methods/admin.teams.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminTeamsListRequest(
    cursor='nobis',
    limit=730122,
    token='delectus',
)

res = s.admin_teams.admin_teams_list(req, operations.AdminTeamsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
