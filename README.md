![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# PROWESS

Political and demographic analysis of redistricting, the POLITICO way.


## Requirements

- Python v3.9 | `brew install python@3.9` or use [pyenv](https://github.com/pyenv/pyenv)
- GEOS v3.8.1 | `brew install geos`
- AWS CLI v2 | `brew install awscli`
- Justfile | `brew install just`


## Getting started

First, copy down all the "raw data" files from S3 to your local repo.

```sh
just download_data
```

Then, create your own `.env` file:

```sh
cp .env.example .env
```

Use the hints in this file when filling in the actual values.

Once your `raw_data` folder is fully synced with S3 (and assuming everything is properly configured), you're ready to run calculations for the various states!


## Checklists

The main list you'll use is the "Newly-enacted state checklist" in [CHECKLIST__new-state.md](CHECKLIST__new-state.md).

We also have a blueprint for how to handle V.E.S.T. per-state precinct data — that file is named [CHECKLIST__precinct-data-formatting-vest.md](CHECKLIST__precinct-data-formatting-vest.md).
