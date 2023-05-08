# chat

### Available Operations

* [chat_delete](#chat_delete) - Deletes a message.
* [chat_delete_scheduled_message](#chat_delete_scheduled_message) - Deletes a pending scheduled message from the queue.
* [chat_get_permalink](#chat_get_permalink) - Retrieve a permalink URL for a specific extant message
* [chat_me_message](#chat_me_message) - Share a me message into a channel.
* [chat_post_ephemeral](#chat_post_ephemeral) - Sends an ephemeral message to a user in a channel.
* [chat_post_message](#chat_post_message) - Sends a message to a channel.
* [chat_schedule_message](#chat_schedule_message) - Schedules a message to be sent to a channel.
* [chat_scheduled_messages_list](#chat_scheduled_messages_list) - Returns a list of scheduled messages.
* [chat_unfurl](#chat_unfurl) - Provide custom unfurl behavior for user-posted URLs
* [chat_update](#chat_update) - Updates a message.

## chat_delete

Deletes a message.

API method documentation
<https://api.slack.com/methods/chat.delete>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatDeleteRequest(
    request_body=operations.ChatDeleteApplicationJSON(
        as_user=False,
        channel='aliquid',
        ts=934.59,
    ),
    token='saepe',
)

res = s.chat.chat_delete(req, operations.ChatDeleteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_delete_success_schema is not None:
    # handle response
```

## chat_delete_scheduled_message

Deletes a pending scheduled message from the queue.

API method documentation
<https://api.slack.com/methods/chat.deleteScheduledMessage>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatDeleteScheduledMessageRequest(
    request_body=operations.ChatDeleteScheduledMessageApplicationJSON(
        as_user=False,
        channel='vel',
        scheduled_message_id='harum',
    ),
    token='molestiae',
)

res = s.chat.chat_delete_scheduled_message(req, operations.ChatDeleteScheduledMessageSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_delete_scheduled_message_schema is not None:
    # handle response
```

## chat_get_permalink

Retrieve a permalink URL for a specific extant message

API method documentation
<https://api.slack.com/methods/chat.getPermalink>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatGetPermalinkRequest(
    channel='rerum',
    message_ts='occaecati',
    token='minima',
)

res = s.chat.chat_get_permalink(req, operations.ChatGetPermalinkSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_get_permalink_success_schema is not None:
    # handle response
```

## chat_me_message

Share a me message into a channel.

API method documentation
<https://api.slack.com/methods/chat.meMessage>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatMeMessageRequest(
    request_body=operations.ChatMeMessageApplicationJSON(
        channel='distinctio',
        text='eligendi',
    ),
    token='sit',
)

res = s.chat.chat_me_message(req, operations.ChatMeMessageSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_me_message_schema is not None:
    # handle response
```

## chat_post_ephemeral

Sends an ephemeral message to a user in a channel.

API method documentation
<https://api.slack.com/methods/chat.postEphemeral>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatPostEphemeralRequest(
    request_body=operations.ChatPostEphemeralApplicationJSON(
        as_user=False,
        attachments='culpa',
        blocks='tempore',
        channel='adipisci',
        icon_emoji='cumque',
        icon_url='consequuntur',
        link_names=False,
        parse='consequatur',
        text='minus',
        thread_ts='quaerat',
        user='sapiente',
        username='Darlene_Koch',
    ),
    token='a',
)

res = s.chat.chat_post_ephemeral(req, operations.ChatPostEphemeralSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_post_ephemeral_success_schema is not None:
    # handle response
```

## chat_post_message

Sends a message to a channel.

API method documentation
<https://api.slack.com/methods/chat.postMessage>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatPostMessageRequest(
    request_body=operations.ChatPostMessageApplicationJSON(
        as_user='nulla',
        attachments='quas',
        blocks='esse',
        channel='quasi',
        icon_emoji='a',
        icon_url='error',
        link_names=False,
        mrkdwn=False,
        parse='sint',
        reply_broadcast=False,
        text='pariatur',
        thread_ts='possimus',
        unfurl_links=False,
        unfurl_media=False,
        username='Carlotta_Upton8',
    ),
    token='consequuntur',
)

res = s.chat.chat_post_message(req, operations.ChatPostMessageSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_post_message_success_schema is not None:
    # handle response
```

## chat_schedule_message

Schedules a message to be sent to a channel.

API method documentation
<https://api.slack.com/methods/chat.scheduleMessage>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatScheduleMessageRequest(
    request_body=operations.ChatScheduleMessageApplicationJSON(
        as_user=False,
        attachments='quasi',
        blocks='similique',
        channel='culpa',
        link_names=False,
        parse='aliquid',
        post_at='tenetur',
        reply_broadcast=False,
        text='quae',
        thread_ts=9367.47,
        unfurl_links=False,
        unfurl_media=False,
    ),
    token='vel',
)

res = s.chat.chat_schedule_message(req, operations.ChatScheduleMessageSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_schedule_message_success_schema is not None:
    # handle response
```

## chat_scheduled_messages_list

Returns a list of scheduled messages.

API method documentation
<https://api.slack.com/methods/chat.scheduledMessages.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatScheduledMessagesListRequest(
    channel='in',
    cursor='eius',
    latest=7276.97,
    limit=849039,
    oldest=7422.38,
    token='accusantium',
)

res = s.chat.chat_scheduled_messages_list(req, operations.ChatScheduledMessagesListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_scheduled_messages_list_schema is not None:
    # handle response
```

## chat_unfurl

Provide custom unfurl behavior for user-posted URLs

API method documentation
<https://api.slack.com/methods/chat.unfurl>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatUnfurlRequest(
    request_body=operations.ChatUnfurlApplicationJSON(
        channel='aliquam',
        ts='sapiente',
        unfurls='dicta',
        user_auth_message='ullam',
        user_auth_required=False,
        user_auth_url='reprehenderit',
    ),
    token='ullam',
)

res = s.chat.chat_unfurl(req, operations.ChatUnfurlSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_unfurl_success_schema is not None:
    # handle response
```

## chat_update

Updates a message.

API method documentation
<https://api.slack.com/methods/chat.update>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.ChatUpdateRequest(
    request_body=operations.ChatUpdateApplicationJSON(
        as_user='nisi',
        attachments='aut',
        blocks='voluptatum',
        channel='qui',
        link_names='quibusdam',
        parse='ex',
        text='deleniti',
        ts='itaque',
    ),
    token='dolorum',
)

res = s.chat.chat_update(req, operations.ChatUpdateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.chat_update_success_schema is not None:
    # handle response
```
