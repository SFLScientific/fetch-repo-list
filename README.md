# fetch-repo-list action
Fetch a list of repo with given filters in the org or user.

Usage example (as a step in Github workflow):
```
  - name: Find all workable repo
    id: repo_list
    uses: SFLScientific/fetch-repo-list
    with:
      org: [ORG_NAME]
      last_active: [N_DAYS]
      token: [READ_ACCESS_TOKEN]
```
Required:
- `READ_ACCESS_TOKEN`: A Github token to read repo information.

Optional:
- `ORG_NAME`: Name of the organization. If a value is given, the action will return repos owned by the Org.
- `N_DAYS`: If a value is given, the action will return repos were active in last N days. The condition is ignored by default.