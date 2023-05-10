# dnd

### Available Operations

* [dnd_end_dnd](#dnd_end_dnd) - Ends the current user's Do Not Disturb session immediately.
* [dnd_end_snooze](#dnd_end_snooze) - Ends the current user's snooze mode immediately.
* [dnd_info](#dnd_info) - Retrieves a user's current Do Not Disturb status.
* [dnd_set_snooze](#dnd_set_snooze) - Turns on Do Not Disturb mode for the current user, or changes its duration.
* [dnd_team_info](#dnd_team_info) - Retrieves the Do Not Disturb status for up to 50 users on a team.

## dnd_end_dnd

Ends the current user's Do Not Disturb session immediately.

API method documentation
<https://api.slack.com/methods/dnd.endDnd>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.DndEndDndRequest(
    token='commodi',
)

res = s.dnd.dnd_end_dnd(req, operations.DndEndDndSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.dnd_end_dnd_schema is not None:
    # handle response
```

## dnd_end_snooze

Ends the current user's snooze mode immediately.

API method documentation
<https://api.slack.com/methods/dnd.endSnooze>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.DndEndSnoozeRequest(
    token='in',
)

res = s.dnd.dnd_end_snooze(req, operations.DndEndSnoozeSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.dnd_end_snooze_schema is not None:
    # handle response
```

## dnd_info

Retrieves a user's current Do Not Disturb status.

API method documentation
<https://api.slack.com/methods/dnd.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.DndInfoRequest(
    token='corporis',
    user='reiciendis',
)

res = s.dnd.dnd_info(req, operations.DndInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.dnd_info_schema is not None:
    # handle response
```

## dnd_set_snooze

Turns on Do Not Disturb mode for the current user, or changes its duration.

API method documentation
<https://api.slack.com/methods/dnd.setSnooze>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.DndSetSnoozeRequestBody(
    num_minutes='assumenda',
    token='nemo',
)

res = s.dnd.dnd_set_snooze(req, operations.DndSetSnoozeSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.dnd_set_snooze_schema is not None:
    # handle response
```

## dnd_team_info

Retrieves the Do Not Disturb status for up to 50 users on a team.

API method documentation
<https://api.slack.com/methods/dnd.teamInfo>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.DndTeamInfoRequest(
    token='recusandae',
    users='aliquid',
)

res = s.dnd.dnd_team_info(req, operations.DndTeamInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
