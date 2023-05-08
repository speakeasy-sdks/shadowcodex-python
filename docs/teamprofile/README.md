# team_profile

### Available Operations

* [team_profile_get](#team_profile_get) - Retrieve a team's profile.

## team_profile_get

Retrieve a team's profile.

API method documentation
<https://api.slack.com/methods/team.profile.get>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.TeamProfileGetRequest(
    token='magnam',
    visibility='saepe',
)

res = s.team_profile.team_profile_get(req, operations.TeamProfileGetSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.team_profile_get_success_schema is not None:
    # handle response
```
