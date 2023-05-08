# files_comments

### Available Operations

* [files_comments_delete](#files_comments_delete) - Deletes an existing comment on a file.

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
        file='incidunt',
        id='294e3698-f447-4f60-be8b-445e80ca55ef',
    ),
    token='nulla',
)

res = s.files_comments.files_comments_delete(req, operations.FilesCommentsDeleteSecurity(
    slack_auth="Bearer YOUR_ACCESS_TOKEN_HERE",
))

if res.files_comments_delete_schema is not None:
    # handle response
```
