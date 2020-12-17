import json 
import argparse
from datetime import datetime, timedelta
from functools import partial
from github import Github


def time_filters(repo, last_n_day):
    """Return True if the repo is active in last N days"""
    if repo.updated_at < datetime.today() - timedelta(days=last_n_day):
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description='Process inputs.')
    parser.add_argument('--last_active', type=int, default=None)
    parser.add_argument('--org_name', type=str, default=None)
    parser.add_argument('--token', type=str, required=True)
    parser.add_argument('--ignore', type=str, required=False, default=None)
    args = parser.parse_args()

    g = Github(args.token)
    if args.org_name != "None":
        print("org mode)
        repos = g.get_organization(args.org_name).get_repos()
    else:
        repos = g.get_user().get_repos()

    if args.last_active != 0:
        repo_filter = partial(time_filters, last_n_day=args.last_active)
        repos = filter(repo_filter, repos)
    
    repo_names =  [x.full_name for x in repos]
    
    if args.ignore:
        repo_names = list(set(repo_names).difference(set(eval(args.ignore))))

    with open("repos.txt", "w") as f:
        f.write(f'{{\\"repo\\":{repo_names}}}')
    return


if __name__ == "__main__":
    main()
