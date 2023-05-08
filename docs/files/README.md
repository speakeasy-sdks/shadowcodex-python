# files

### Available Operations

* [files_comments_delete](#files_comments_delete) - Deletes an existing comment on a file.
* [files_delete](#files_delete) - Deletes a file.
* [files_info](#files_info) - Gets information about a file.
* [files_list](#files_list) - List for a team, in a channel, or from a user with applied filters.
* [files_remote_add](#files_remote_add) - Adds a file from a remote service
* [files_remote_info](#files_remote_info) - Retrieve information about a remote file added to Slack
* [files_remote_list](#files_remote_list) - Retrieve information about a remote file added to Slack
* [files_remote_remove](#files_remote_remove) - Remove a remote file.
* [files_remote_share](#files_remote_share) - Share a remote file into a channel.
* [files_remote_update](#files_remote_update) - Updates an existing remote file.
* [files_revoke_public_url](#files_revoke_public_url) - Revokes public/external sharing access for a file
* [files_shared_public_url](#files_shared_public_url) - Enables a file for public/external sharing.
* [files_upload](#files_upload) - Uploads or creates a file.

## files_comments_delete

Deletes an existing comment on a file.

API method documentation
<https://api.slack.com/methods/files.comments.delete>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesCommentsDeleteRequest(
    request_body=operations.FilesCommentsDeleteApplicationJSON(
        file='cum',
        id='375ed4f6-fbee-441f-b331-7fe35b60eb1e',
    ),
    token='similique',
)

res = s.files.files_comments_delete(req, operations.FilesCommentsDeleteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.files_comments_delete_schema is not None:
    # handle response
```

## files_delete

Deletes a file.

API method documentation
<https://api.slack.com/methods/files.delete>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesDeleteRequest(
    request_body=operations.FilesDeleteApplicationJSON(
        file='tempora',
    ),
    token='aspernatur',
)

res = s.files.files_delete(req, operations.FilesDeleteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.files_delete_schema is not None:
    # handle response
```

## files_info

Gets information about a file.

API method documentation
<https://api.slack.com/methods/files.info>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesInfoRequest(
    count='voluptas',
    cursor='voluptas',
    file='voluptas',
    limit=324405,
    page='nobis',
    token='dolorum',
)

res = s.files.files_info(req, operations.FilesInfoSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.files_info_schema is not None:
    # handle response
```

## files_list

List for a team, in a channel, or from a user with applied filters.

API method documentation
<https://api.slack.com/methods/files.list>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesListRequest(
    channel='adipisci',
    count='minus',
    page='dolores',
    show_files_hidden_by_limit=False,
    token='blanditiis',
    ts_from=4492.92,
    ts_to=2962.42,
    types='aliquam',
    user='officiis',
)

res = s.files.files_list(req, operations.FilesListSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.files_list_schema is not None:
    # handle response
```

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
    external_id='temporibus',
    external_url='ullam',
    filetype='adipisci',
    indexable_file_contents='cum',
    preview_image='blanditiis',
    title='Ms.',
    token='hic',
)

res = s.files.files_remote_add(req, operations.FilesRemoteAddSecurity(
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
    external_id='nesciunt',
    file='culpa',
    token='corrupti',
)

res = s.files.files_remote_info(req, operations.FilesRemoteInfoSecurity(
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
    channel='pariatur',
    cursor='totam',
    limit=940210,
    token='exercitationem',
    ts_from=7507.65,
    ts_to=246.19,
)

res = s.files.files_remote_list(req, operations.FilesRemoteListSecurity(
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
    external_id='rerum',
    file='sed',
    token='reiciendis',
)

res = s.files.files_remote_remove(req, operations.FilesRemoteRemoveSecurity(
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
    channels='explicabo',
    external_id='asperiores',
    file='facilis',
    token='voluptate',
)

res = s.files.files_remote_share(req, operations.FilesRemoteShareSecurity(
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
    external_id='expedita',
    external_url='ab',
    file='iste',
    filetype='dolore',
    indexable_file_contents='laborum',
    preview_image='sed',
    title='Ms.',
    token='commodi',
)

res = s.files.files_remote_update(req, operations.FilesRemoteUpdateSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.default_success_template is not None:
    # handle response
```

## files_revoke_public_url

Revokes public/external sharing access for a file

API method documentation
<https://api.slack.com/methods/files.revokePublicURL>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesRevokePublicURLRequest(
    request_body=operations.FilesRevokePublicURLApplicationJSON(
        file='quidem',
    ),
    token='explicabo',
)

res = s.files.files_revoke_public_url(req, operations.FilesRevokePublicURLSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.files_revoke_public_url_schema is not None:
    # handle response
```

## files_shared_public_url

Enables a file for public/external sharing.

API method documentation
<https://api.slack.com/methods/files.sharedPublicURL>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesSharedPublicURLRequest(
    request_body=operations.FilesSharedPublicURLApplicationJSON(
        file='voluptas',
    ),
    token='unde',
)

res = s.files.files_shared_public_url(req, operations.FilesSharedPublicURLSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.files_shared_public_url_schema is not None:
    # handle response
```

## files_upload

Uploads or creates a file.

API method documentation
<https://api.slack.com/methods/files.upload>

### Example Usage

```python
import slack_spec
from slack_spec.models import operations

s = slack_spec.SlackSpec()

req = operations.FilesUploadRequestBody(
    channels='architecto',
    content='suscipit',
    file='sapiente',
    filename='debitis',
    filetype='illo',
    initial_comment='reiciendis',
    thread_ts=193,
    title='Ms.',
    token='maiores',
)

res = s.files.files_upload(req, operations.FilesUploadSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.files_upload_schema is not None:
    # handle response
```
