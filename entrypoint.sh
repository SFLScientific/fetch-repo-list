#!/bin/sh -l

echo "Activate Github in last $2 days."
echo "The orgnization name is $3."
python /src/main.py --token $1 --last_active $2 --org_name $3
echo "::set-output name=repo_list::$(cat repos.txt)"
