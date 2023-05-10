# apps_event_authorizations

### Available Operations

* [apps_event_authorizations_list](#apps_event_authorizations_list) - Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

## apps_event_authorizations_list

Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

API method documentation
<https://api.slack.com/methods/apps.event.authorizations.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AppsEventAuthorizationsListRequest(
    cursor='qui',
    event_context='cupiditate',
    limit=807581,
    token='pariatur',
)

res = s.apps_event_authorizations.apps_event_authorizations_list(req, operations.AppsEventAuthorizationsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
