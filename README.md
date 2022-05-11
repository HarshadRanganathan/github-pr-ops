# github-pr-ops
Script to extract pending PR's authored by your team members

## Steps

Update `properties.py` with required settings -

|Property |Usage |
|--|--|
|GITTOKEN |Generate a new Git Token with required permissions which will be used to extract PR details |
|ORG_NAME |Provide the Github Org Name to which the queries will be scoped  |
|OPEN_PR_QUERY |Update the query following Github documentation to search PR's based on your team member's ids in the query string |


## Usage

Run the script with below command:

```
python github_pr_ops.py
```

This will generate `pr_file.html` which will contain the list of Open PR's authored by your team members sorted by the days by which they have been open.
