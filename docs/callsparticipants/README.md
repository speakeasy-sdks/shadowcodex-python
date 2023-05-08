# calls_participants

### Available Operations

* [calls_participants_add](#calls_participants_add) - Registers new participants added to a Call.
* [calls_participants_remove](#calls_participants_remove) - Registers participants removed from a Call.

## calls_participants_add

Registers new participants added to a Call.

API method documentation
<https://api.slack.com/methods/calls.participants.add>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.CallsParticipantsAddRequest(
    request_body=operations.CallsParticipantsAddApplicationJSON(
        id='cdca4251-904e-4523-87e0-bc7178e4796f',
        users='dolores',
    ),
    token='deserunt',
)

res = s.calls_participants.calls_participants_add(req, operations.CallsParticipantsAddSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## calls_participants_remove

Registers participants removed from a Call.

API method documentation
<https://api.slack.com/methods/calls.participants.remove>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.CallsParticipantsRemoveRequest(
    request_body=operations.CallsParticipantsRemoveApplicationJSON(
        id='70c68828-2aa4-4825-a2f2-22e9817ee17c',
        users='nam',
    ),
    token='vero',
)

res = s.calls_participants.calls_participants_remove(req, operations.CallsParticipantsRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
