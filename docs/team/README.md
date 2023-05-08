# team

### Available Operations

* [team_access_logs](#team_access_logs) - Gets the access logs for the current team.
* [team_billable_info](#team_billable_info) - Gets billable users information for the current team.
* [team_info](#team_info) - Gets information about the current team.
* [team_integration_logs](#team_integration_logs) - Gets the integration logs for the current team.
* [team_profile_get](#team_profile_get) - Retrieve a team's profile.

## team_access_logs

Gets the access logs for the current team.

API method documentation
<https://api.slack.com/methods/team.accessLogs>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.TeamAccessLogsRequest(
    before='sunt',
    count='recusandae',
    page='dolorum',
    token='repellendus',
)

res = s.team.team_access_logs(req, operations.TeamAccessLogsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.team_access_logs_schema is not None:
    # handle response
```

## team_billable_info

Gets billable users information for the current team.

API method documentation
<https://api.slack.com/methods/team.billableInfo>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.TeamBillableInfoRequest(
    token='labore',
    user='reiciendis',
)

res = s.team.team_billable_info(req, operations.TeamBillableInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## team_info

Gets information about the current team.

API method documentation
<https://api.slack.com/methods/team.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.TeamInfoRequest(
    team='doloremque',
    token='repudiandae',
)

res = s.team.team_info(req, operations.TeamInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.team_info_schema is not None:
    # handle response
```

## team_integration_logs

Gets the integration logs for the current team.

API method documentation
<https://api.slack.com/methods/team.integrationLogs>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.TeamIntegrationLogsRequest(
    app_id='dicta',
    change_type='accusantium',
    count='beatae',
    page='dolores',
    service_id='enim',
    token='laboriosam',
    user='velit',
)

res = s.team.team_integration_logs(req, operations.TeamIntegrationLogsSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.team_integration_logs_schema is not None:
    # handle response
```

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
    token='a',
    visibility='molestias',
)

res = s.team.team_profile_get(req, operations.TeamProfileGetSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.team_profile_get_success_schema is not None:
    # handle response
```
