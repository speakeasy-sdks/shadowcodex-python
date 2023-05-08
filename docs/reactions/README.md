# reactions

### Available Operations

* [reactions_add](#reactions_add) - Adds a reaction to an item.
* [reactions_get](#reactions_get) - Gets reactions for an item.
* [reactions_list](#reactions_list) - Lists reactions made by a user.
* [reactions_remove](#reactions_remove) - Removes a reaction from an item.

## reactions_add

Adds a reaction to an item.

API method documentation
<https://api.slack.com/methods/reactions.add>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ReactionsAddRequest(
    request_body=operations.ReactionsAddApplicationJSON(
        channel='architecto',
        name='Francisco Powlowski',
        timestamp='nam',
    ),
    token='tenetur',
)

res = s.reactions.reactions_add(req, operations.ReactionsAddSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.reactions_add_schema is not None:
    # handle response
```

## reactions_get

Gets reactions for an item.

API method documentation
<https://api.slack.com/methods/reactions.get>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ReactionsGetRequest(
    channel='laboriosam',
    file='alias',
    file_comment='amet',
    full=False,
    timestamp='deserunt',
    token='voluptate',
)

res = s.reactions.reactions_get(req, operations.ReactionsGetSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.reactions_get_success_schema is not None:
    # handle response
```

## reactions_list

Lists reactions made by a user.

API method documentation
<https://api.slack.com/methods/reactions.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ReactionsListRequest(
    count=600392,
    cursor='reiciendis',
    full=False,
    limit=588740,
    page=833819,
    token='delectus',
    user='voluptates',
)

res = s.reactions.reactions_list(req, operations.ReactionsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.reactions_list_schema is not None:
    # handle response
```

## reactions_remove

Removes a reaction from an item.

API method documentation
<https://api.slack.com/methods/reactions.remove>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ReactionsRemoveRequest(
    request_body=operations.ReactionsRemoveApplicationJSON(
        channel='perferendis',
        file='est',
        file_comment='quidem',
        name='Chelsea Pfannerstill',
        timestamp='veniam',
    ),
    token='voluptatem',
)

res = s.reactions.reactions_remove(req, operations.ReactionsRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.reactions_remove_schema is not None:
    # handle response
```
