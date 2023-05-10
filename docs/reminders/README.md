# reminders

### Available Operations

* [reminders_add](#reminders_add) - Creates a reminder.
* [reminders_complete](#reminders_complete) - Marks a reminder as complete.
* [reminders_delete](#reminders_delete) - Deletes a reminder.
* [reminders_info](#reminders_info) - Gets information about a reminder.
* [reminders_list](#reminders_list) - Lists all reminders created by or for a given user.

## reminders_add

Creates a reminder.

API method documentation
<https://api.slack.com/methods/reminders.add>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.RemindersAddRequest(
    request_body=operations.RemindersAddApplicationJSON(
        text='quisquam',
        time='repudiandae',
        user='quasi',
    ),
    token='atque',
)

res = s.reminders.reminders_add(req, operations.RemindersAddSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.reminders_add_schema is not None:
    # handle response
```

## reminders_complete

Marks a reminder as complete.

API method documentation
<https://api.slack.com/methods/reminders.complete>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.RemindersCompleteRequest(
    request_body=operations.RemindersCompleteApplicationJSON(
        reminder='reprehenderit',
    ),
    token='asperiores',
)

res = s.reminders.reminders_complete(req, operations.RemindersCompleteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.reminders_complete_schema is not None:
    # handle response
```

## reminders_delete

Deletes a reminder.

API method documentation
<https://api.slack.com/methods/reminders.delete>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.RemindersDeleteRequest(
    request_body=operations.RemindersDeleteApplicationJSON(
        reminder='totam',
    ),
    token='suscipit',
)

res = s.reminders.reminders_delete(req, operations.RemindersDeleteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.reminders_delete_schema is not None:
    # handle response
```

## reminders_info

Gets information about a reminder.

API method documentation
<https://api.slack.com/methods/reminders.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.RemindersInfoRequest(
    reminder='quidem',
    token='maxime',
)

res = s.reminders.reminders_info(req, operations.RemindersInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.reminders_info_schema is not None:
    # handle response
```

## reminders_list

Lists all reminders created by or for a given user.

API method documentation
<https://api.slack.com/methods/reminders.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.RemindersListRequest(
    token='et',
)

res = s.reminders.reminders_list(req, operations.RemindersListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.reminders_list_schema is not None:
    # handle response
```
