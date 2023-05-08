# pins

### Available Operations

* [pins_add](#pins_add) - Pins an item to a channel.
* [pins_list](#pins_list) - Lists items pinned to a channel.
* [pins_remove](#pins_remove) - Un-pins an item from a channel.

## pins_add

Pins an item to a channel.

API method documentation
<https://api.slack.com/methods/pins.add>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.PinsAddRequest(
    request_body=operations.PinsAddApplicationJSON(
        channel='saepe',
        timestamp='error',
    ),
    token='consequatur',
)

res = s.pins.pins_add(req, operations.PinsAddSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.pins_add_schema is not None:
    # handle response
```

## pins_list

Lists items pinned to a channel.

API method documentation
<https://api.slack.com/methods/pins.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.PinsListRequest(
    channel='incidunt',
    token='reiciendis',
)

res = s.pins.pins_list(req, operations.PinsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.pins_list_success_schema is not None:
    # handle response
```

## pins_remove

Un-pins an item from a channel.

API method documentation
<https://api.slack.com/methods/pins.remove>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.PinsRemoveRequest(
    request_body=operations.PinsRemoveApplicationJSON(
        channel='dolorem',
        timestamp='harum',
    ),
    token='dicta',
)

res = s.pins.pins_remove(req, operations.PinsRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.pins_remove_schema is not None:
    # handle response
```
