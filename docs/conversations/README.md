# conversations

### Available Operations

* [conversations_archive](#conversations_archive) - Archives a conversation.
* [conversations_close](#conversations_close) - Closes a direct message or multi-person direct message.
* [conversations_create](#conversations_create) - Initiates a public or private channel-based conversation
* [conversations_history](#conversations_history) - Fetches a conversation's history of messages and events.
* [conversations_info](#conversations_info) - Retrieve information about a conversation.
* [conversations_invite](#conversations_invite) - Invites users to a channel.
* [conversations_join](#conversations_join) - Joins an existing conversation.
* [conversations_kick](#conversations_kick) - Removes a user from a conversation.
* [conversations_leave](#conversations_leave) - Leaves a conversation.
* [conversations_list](#conversations_list) - Lists all channels in a Slack team.
* [conversations_mark](#conversations_mark) - Sets the read cursor in a channel.
* [conversations_members](#conversations_members) - Retrieve members of a conversation.
* [conversations_open](#conversations_open) - Opens or resumes a direct message or multi-person direct message.
* [conversations_rename](#conversations_rename) - Renames a conversation.
* [conversations_replies](#conversations_replies) - Retrieve a thread of messages posted to a conversation
* [conversations_set_purpose](#conversations_set_purpose) - Sets the purpose for a conversation.
* [conversations_set_topic](#conversations_set_topic) - Sets the topic for a conversation.
* [conversations_unarchive](#conversations_unarchive) - Reverses conversation archival.

## conversations_archive

Archives a conversation.

API method documentation
<https://api.slack.com/methods/conversations.archive>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsArchiveRequest(
    request_body=operations.ConversationsArchiveApplicationJSON(
        channel='voluptate',
    ),
    token='ipsa',
)

res = s.conversations.conversations_archive(req, operations.ConversationsArchiveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_archive_success_schema is not None:
    # handle response
```

## conversations_close

Closes a direct message or multi-person direct message.

API method documentation
<https://api.slack.com/methods/conversations.close>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsCloseRequest(
    request_body=operations.ConversationsCloseApplicationJSON(
        channel='minima',
    ),
    token='veritatis',
)

res = s.conversations.conversations_close(req, operations.ConversationsCloseSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_close_success_schema is not None:
    # handle response
```

## conversations_create

Initiates a public or private channel-based conversation

API method documentation
<https://api.slack.com/methods/conversations.create>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsCreateRequest(
    request_body=operations.ConversationsCreateApplicationJSON(
        is_private=False,
        name='Sherry Morar IV',
    ),
    token='aut',
)

res = s.conversations.conversations_create(req, operations.ConversationsCreateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_create_success_schema is not None:
    # handle response
```

## conversations_history

Fetches a conversation's history of messages and events.

API method documentation
<https://api.slack.com/methods/conversations.history>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsHistoryRequest(
    channel='laudantium',
    cursor='eum',
    inclusive=False,
    latest=6498.32,
    limit=68074,
    oldest=5445.91,
    token='non',
)

res = s.conversations.conversations_history(req, operations.ConversationsHistorySecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_history_success_schema is not None:
    # handle response
```

## conversations_info

Retrieve information about a conversation.

API method documentation
<https://api.slack.com/methods/conversations.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsInfoRequest(
    channel='voluptatem',
    include_locale=False,
    include_num_members=False,
    token='dolor',
)

res = s.conversations.conversations_info(req, operations.ConversationsInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_info_success_schema is not None:
    # handle response
```

## conversations_invite

Invites users to a channel.

API method documentation
<https://api.slack.com/methods/conversations.invite>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsInviteRequest(
    request_body=operations.ConversationsInviteApplicationJSON(
        channel='occaecati',
        users='numquam',
    ),
    token='impedit',
)

res = s.conversations.conversations_invite(req, operations.ConversationsInviteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_invite_error_schema is not None:
    # handle response
```

## conversations_join

Joins an existing conversation.

API method documentation
<https://api.slack.com/methods/conversations.join>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsJoinRequest(
    request_body=operations.ConversationsJoinApplicationJSON(
        channel='explicabo',
    ),
    token='voluptas',
)

res = s.conversations.conversations_join(req, operations.ConversationsJoinSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_join_success_schema is not None:
    # handle response
```

## conversations_kick

Removes a user from a conversation.

API method documentation
<https://api.slack.com/methods/conversations.kick>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsKickRequest(
    request_body=operations.ConversationsKickApplicationJSON(
        channel='aut',
        user='dignissimos',
    ),
    token='dicta',
)

res = s.conversations.conversations_kick(req, operations.ConversationsKickSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_kick_success_schema is not None:
    # handle response
```

## conversations_leave

Leaves a conversation.

API method documentation
<https://api.slack.com/methods/conversations.leave>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsLeaveRequest(
    request_body=operations.ConversationsLeaveApplicationJSON(
        channel='maiores',
    ),
    token='natus',
)

res = s.conversations.conversations_leave(req, operations.ConversationsLeaveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_leave_success_schema is not None:
    # handle response
```

## conversations_list

Lists all channels in a Slack team.

API method documentation
<https://api.slack.com/methods/conversations.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsListRequest(
    cursor='velit',
    exclude_archived=False,
    limit=974257,
    token='voluptas',
    types='asperiores',
)

res = s.conversations.conversations_list(req, operations.ConversationsListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_list_success_schema is not None:
    # handle response
```

## conversations_mark

Sets the read cursor in a channel.

API method documentation
<https://api.slack.com/methods/conversations.mark>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsMarkRequest(
    request_body=operations.ConversationsMarkApplicationJSON(
        channel='aperiam',
        ts=4090.54,
    ),
    token='quaerat',
)

res = s.conversations.conversations_mark(req, operations.ConversationsMarkSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_mark_success_schema is not None:
    # handle response
```

## conversations_members

Retrieve members of a conversation.

API method documentation
<https://api.slack.com/methods/conversations.members>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsMembersRequest(
    channel='consequuntur',
    cursor='repellendus',
    limit=638762,
    token='maxime',
)

res = s.conversations.conversations_members(req, operations.ConversationsMembersSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_members_success_schema is not None:
    # handle response
```

## conversations_open

Opens or resumes a direct message or multi-person direct message.

API method documentation
<https://api.slack.com/methods/conversations.open>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsOpenRequest(
    request_body=operations.ConversationsOpenApplicationJSON(
        channel='dignissimos',
        return_im=False,
        users='officia',
    ),
    token='asperiores',
)

res = s.conversations.conversations_open(req, operations.ConversationsOpenSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_open_success_schema is not None:
    # handle response
```

## conversations_rename

Renames a conversation.

API method documentation
<https://api.slack.com/methods/conversations.rename>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsRenameRequest(
    request_body=operations.ConversationsRenameApplicationJSON(
        channel='nemo',
        name='Darlene Sawayn',
    ),
    token='ab',
)

res = s.conversations.conversations_rename(req, operations.ConversationsRenameSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_rename_success_schema is not None:
    # handle response
```

## conversations_replies

Retrieve a thread of messages posted to a conversation

API method documentation
<https://api.slack.com/methods/conversations.replies>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsRepliesRequest(
    channel='adipisci',
    cursor='fuga',
    inclusive=False,
    latest=6625.05,
    limit=380729,
    oldest=2460.63,
    token='culpa',
    ts=6658.59,
)

res = s.conversations.conversations_replies(req, operations.ConversationsRepliesSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_replies_success_schema is not None:
    # handle response
```

## conversations_set_purpose

Sets the purpose for a conversation.

API method documentation
<https://api.slack.com/methods/conversations.setPurpose>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsSetPurposeRequest(
    request_body=operations.ConversationsSetPurposeApplicationJSON(
        channel='recusandae',
        purpose='totam',
    ),
    token='fugiat',
)

res = s.conversations.conversations_set_purpose(req, operations.ConversationsSetPurposeSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_set_purpose_success_schema is not None:
    # handle response
```

## conversations_set_topic

Sets the topic for a conversation.

API method documentation
<https://api.slack.com/methods/conversations.setTopic>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsSetTopicRequest(
    request_body=operations.ConversationsSetTopicApplicationJSON(
        channel='vel',
        topic='ducimus',
    ),
    token='quos',
)

res = s.conversations.conversations_set_topic(req, operations.ConversationsSetTopicSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_set_topic_success_schema is not None:
    # handle response
```

## conversations_unarchive

Reverses conversation archival.

API method documentation
<https://api.slack.com/methods/conversations.unarchive>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ConversationsUnarchiveRequest(
    request_body=operations.ConversationsUnarchiveApplicationJSON(
        channel='vel',
    ),
    token='labore',
)

res = s.conversations.conversations_unarchive(req, operations.ConversationsUnarchiveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.conversations_unarchive_success_schema is not None:
    # handle response
```
