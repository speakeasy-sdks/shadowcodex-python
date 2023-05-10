# views

### Available Operations

* [views_open](#views_open) - Open a view for a user.
* [views_publish](#views_publish) - Publish a static view for a User.
* [views_push](#views_push) - Push a view onto the stack of a root view.
* [views_update](#views_update) - Update an existing view.

## views_open

Open a view for a user.

API method documentation
<https://api.slack.com/methods/views.open>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ViewsOpenRequest(
    token='repellat',
    trigger_id='doloribus',
    view='ullam',
)

res = s.views.views_open(req, operations.ViewsOpenSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## views_publish

Publish a static view for a User.

API method documentation
<https://api.slack.com/methods/views.publish>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ViewsPublishRequest(
    hash='in',
    token='nam',
    user_id='earum',
    view='officia',
)

res = s.views.views_publish(req, operations.ViewsPublishSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## views_push

Push a view onto the stack of a root view.

API method documentation
<https://api.slack.com/methods/views.push>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ViewsPushRequest(
    token='laborum',
    trigger_id='placeat',
    view='modi',
)

res = s.views.views_push(req, operations.ViewsPushSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## views_update

Update an existing view.

API method documentation
<https://api.slack.com/methods/views.update>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ViewsUpdateRequest(
    external_id='voluptatibus',
    hash='molestias',
    token='officiis',
    view='sapiente',
    view_id='cumque',
)

res = s.views.views_update(req, operations.ViewsUpdateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
