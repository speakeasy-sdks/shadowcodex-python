# calls

### Available Operations

* [calls_add](#calls_add) - Registers a new Call.
* [calls_end](#calls_end) - Ends a Call.
* [calls_info](#calls_info) - Returns information about a Call.
* [calls_participants_add](#calls_participants_add) - Registers new participants added to a Call.
* [calls_participants_remove](#calls_participants_remove) - Registers participants removed from a Call.
* [calls_update](#calls_update) - Updates information about a Call.

## calls_add

Registers a new Call.

API method documentation
<https://api.slack.com/methods/calls.add>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.CallsAddRequest(
    request_body=operations.CallsAddApplicationJSON(
        created_by='temporibus',
        date_start=183280,
        desktop_app_join_url='neque',
        external_display_id='fugit',
        external_unique_id='magni',
        join_url='odio',
        title='Mr.',
        users='ullam',
    ),
    token='nam',
)

res = s.calls.calls_add(req, operations.CallsAddSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## calls_end

Ends a Call.

API method documentation
<https://api.slack.com/methods/calls.end>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.CallsEndRequest(
    request_body=operations.CallsEndApplicationJSON(
        duration=940432,
        id='0cbb1e31-b8b9-40f3-843a-1108e0adcf4b',
    ),
    token='cupiditate',
)

res = s.calls.calls_end(req, operations.CallsEndSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## calls_info

Returns information about a Call.

API method documentation
<https://api.slack.com/methods/calls.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.CallsInfoRequest(
    id='21879fce-953f-473e-b7fb-c7abd74dd39c',
    token='aut',
)

res = s.calls.calls_info(req, operations.CallsInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

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
        id='f5d2cff7-c70a-4456-a6d4-36813f16d9f5',
        users='sapiente',
    ),
    token='quisquam',
)

res = s.calls.calls_participants_add(req, operations.CallsParticipantsAddSecurity(
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
        id='e6c55614-6c3e-4250-bb00-8c42e141aac3',
        users='eum',
    ),
    token='autem',
)

res = s.calls.calls_participants_remove(req, operations.CallsParticipantsRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## calls_update

Updates information about a Call.

API method documentation
<https://api.slack.com/methods/calls.update>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.CallsUpdateRequest(
    request_body=operations.CallsUpdateApplicationJSON(
        desktop_app_join_url='nobis',
        id='8dd6b144-2907-4474-b78a-7bd466d28c10',
        join_url='id',
        title='Miss',
    ),
    token='neque',
)

res = s.calls.calls_update(req, operations.CallsUpdateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
