# genCDR

A tool to generate dummy Call Detail Records (CDR) on a telcom charging system. This tool provides to generate 3 categories of
CDRs : OnNet , Xnet and Internationals and an option to define the number of CDRs to be generated.

The tool is developed in Python.

- `OnNet`: CDRs generated when customers that make or receive calls belong to the same telcom company
- `Xnet`: CDRs generated when customers that make calls to another telcom company but in the same country
- `Internationals`: CDRs generated when customers that make calls to countries abroad

## Requirements before dump generation

- `Create a python environment`: python3 -m venv .venv
- `Install Faker package`: pip install faker

## Command-line Usage

To generate a dump of CDR records and save in directory named `dumps`:

First, activate the environment

```bash
source .venv/bin/activate
```

Run generateCDR.py

```bash
python generateCDR.py
```

## Menu

```bash
--- MENU ---
[1]  OnNet
[2]  XNet
[3]  International

Please enter your choice (1, 2, or 3 ):
```

```bash
--- MENU ---
[1]  OnNet
[2]  XNet
[3]  International

Please enter your choice (1, 2, or 3 ): 1

Please enter the number of records to generate:
```

## Configuration Options

with 4 json files located in config folder that can be changed to accomadate

- `configOnNet.json`: configuration file for OnNet calls
- `configXNet.json` : configuration file for OnXnet calls
- `configIntl.json` : configuration file for Internation calls
- `menuOptions.json`: configuration file for Menu
