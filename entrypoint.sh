#!/bin/sh

if [ $2 -ne 0 ];
then
    echo "Activate Github in last $2 days."
fi

if [ "$3" != "None" ] ;
then
    echo "The orgnization name is $3."
fi

python /src/main.py --token $1 --last_active $2 --org_name $3
echo "::set-output name=repo_list::$(cat repos.txt)"
