# gitlab-stale-branches

## Requirements

python

## Setup

1. Run `cp default_config.json config.json`
2. Edit `config.json` to add GitLab url, api token
3. Add projects to `config.json` by adding an object to the `projects` array with `id` (id of repo in GitLab - can be found in API request) and `label` which is whatever you want printed out above the results.

## Usage

To use run `python <path>/<to>/<repo>/check.py`

### Arguments

**First:** comma separated list of branch names to check

**Second:** number of days (i.e. '4' will print only branches that have not had a commit in the last 4 days, '-4' will print only branches that _have_ had a commit in the last 4 days)
