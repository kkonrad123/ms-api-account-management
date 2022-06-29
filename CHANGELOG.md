feat:
- add API tests
- add Docker deployment

docs:
- update online auto-generated documentation - `http://127.0.0.1:8000/docs`
- add README.md

fix:
- correct `delete_account` function by writing implementation
- change account creation request from `put` to `post`. `post` is used when we create a resource, whereas `put` is used to update it. [reference](https://www.rfc-editor.org/rfc/rfc7644#section-3.5.1)