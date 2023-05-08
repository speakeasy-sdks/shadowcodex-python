# stars

### Available Operations

* [stars_add](#stars_add) - Adds a star to an item.
* [stars_list](#stars_list) - Lists stars for a user.
* [stars_remove](#stars_remove) - Removes a star from an item.

## stars_add

Adds a star to an item.

API method documentation
<https://api.slack.com/methods/stars.add>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.StarsAddRequest(
    request_body=operations.StarsAddApplicationJSON(
        channel='officiis',
        file='accusamus',
        file_comment='natus',
        timestamp='minima',
    ),
    token='aspernatur',
)

res = s.stars.stars_add(req, operations.StarsAddSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.stars_add_schema is not None:
    # handle response
```

## stars_list

Lists stars for a user.

API method documentation
<https://api.slack.com/methods/stars.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.StarsListRequest(
    count='ex',
    cursor='maiores',
    limit=544647,
    page='at',
    token='error',
)

res = s.stars.stars_list(req, operations.StarsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.stars_list_schema is not None:
    # handle response
```

## stars_remove

Removes a star from an item.

API method documentation
<https://api.slack.com/methods/stars.remove>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.StarsRemoveRequest(
    request_body=operations.StarsRemoveApplicationJSON(
        channel='blanditiis',
        file='suscipit',
        file_comment='repudiandae',
        timestamp='atque',
    ),
    token='atque',
)

res = s.stars.stars_remove(req, operations.StarsRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.stars_remove_schema is not None:
    # handle response
```
