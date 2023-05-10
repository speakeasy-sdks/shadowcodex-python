# admin_emoji

### Available Operations

* [admin_emoji_add](#admin_emoji_add) - Add an emoji.
* [admin_emoji_add_alias](#admin_emoji_add_alias) - Add an emoji alias.
* [admin_emoji_list](#admin_emoji_list) - List emoji for an Enterprise Grid organization.
* [admin_emoji_remove](#admin_emoji_remove) - Remove an emoji across an Enterprise Grid organization
* [admin_emoji_rename](#admin_emoji_rename) - Rename an emoji.

## admin_emoji_add

Add an emoji.

API method documentation
<https://api.slack.com/methods/admin.emoji.add>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiAddRequestBody(
    name='Clyde Kling',
    token='eaque',
    url='pariatur',
)

res = s.admin_emoji.admin_emoji_add(req, operations.AdminEmojiAddSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_emoji_add_alias

Add an emoji alias.

API method documentation
<https://api.slack.com/methods/admin.emoji.addAlias>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiAddAliasRequestBody(
    alias_for='nemo',
    name='Joseph Steuber DDS',
    token='corporis',
)

res = s.admin_emoji.admin_emoji_add_alias(req, operations.AdminEmojiAddAliasSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_emoji_list

List emoji for an Enterprise Grid organization.

API method documentation
<https://api.slack.com/methods/admin.emoji.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiListRequest(
    cursor='hic',
    limit=729991,
    token='nobis',
)

res = s.admin_emoji.admin_emoji_list(req, operations.AdminEmojiListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_emoji_remove

Remove an emoji across an Enterprise Grid organization

API method documentation
<https://api.slack.com/methods/admin.emoji.remove>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiRemoveRequestBody(
    name='Beatrice Lebsack II',
    token='nesciunt',
)

res = s.admin_emoji.admin_emoji_remove(req, operations.AdminEmojiRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## admin_emoji_rename

Rename an emoji.

API method documentation
<https://api.slack.com/methods/admin.emoji.rename>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.AdminEmojiRenameRequestBody(
    name='Dorothy Dach',
    new_name='dolor',
    token='vero',
)

res = s.admin_emoji.admin_emoji_rename(req, operations.AdminEmojiRenameSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
