# files_remote

### Available Operations

* [files_remote_add](#files_remote_add) - Adds a file from a remote service
* [files_remote_info](#files_remote_info) - Retrieve information about a remote file added to Slack
* [files_remote_list](#files_remote_list) - Retrieve information about a remote file added to Slack
* [files_remote_remove](#files_remote_remove) - Remove a remote file.
* [files_remote_share](#files_remote_share) - Share a remote file into a channel.
* [files_remote_update](#files_remote_update) - Updates an existing remote file.

## files_remote_add

Adds a file from a remote service

API method documentation
<https://api.slack.com/methods/files.remote.add>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesRemoteAddRequestBody(
    external_id='magni',
    external_url='aperiam',
    filetype='saepe',
    indexable_file_contents='numquam',
    preview_image='veniam',
    title='Ms.',
    token='officiis',
)

res = s.files_remote.files_remote_add(req, operations.FilesRemoteAddSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## files_remote_info

Retrieve information about a remote file added to Slack

API method documentation
<https://api.slack.com/methods/files.remote.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesRemoteInfoRequest(
    external_id='beatae',
    file='laudantium',
    token='exercitationem',
)

res = s.files_remote.files_remote_info(req, operations.FilesRemoteInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## files_remote_list

Retrieve information about a remote file added to Slack

API method documentation
<https://api.slack.com/methods/files.remote.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesRemoteListRequest(
    channel='praesentium',
    cursor='cum',
    limit=386827,
    token='dolorum',
    ts_from=5300.89,
    ts_to=6223.85,
)

res = s.files_remote.files_remote_list(req, operations.FilesRemoteListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## files_remote_remove

Remove a remote file.

API method documentation
<https://api.slack.com/methods/files.remote.remove>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesRemoteRemoveRequestBody(
    external_id='hic',
    file='expedita',
    token='debitis',
)

res = s.files_remote.files_remote_remove(req, operations.FilesRemoteRemoveSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## files_remote_share

Share a remote file into a channel.

API method documentation
<https://api.slack.com/methods/files.remote.share>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesRemoteShareRequest(
    channels='neque',
    external_id='dolorum',
    file='nostrum',
    token='officia',
)

res = s.files_remote.files_remote_share(req, operations.FilesRemoteShareSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## files_remote_update

Updates an existing remote file.

API method documentation
<https://api.slack.com/methods/files.remote.update>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesRemoteUpdateRequestBody(
    external_id='dolorum',
    external_url='corrupti',
    file='accusamus',
    filetype='tempora',
    indexable_file_contents='atque',
    preview_image='fugit',
    title='Mrs.',
    token='fugiat',
)

res = s.files_remote.files_remote_update(req, operations.FilesRemoteUpdateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```
