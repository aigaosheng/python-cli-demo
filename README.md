# How to use pex to patch python project into a cli command
This is a project to demo how to use PEX tool to patch python project into a executable command

## Step-by-step
1. Create a virtual environment, if don't have. Then activate env
2. Install pex tool
```
pip install pex
```
3. Put all project code in a directory, e.g. in the demo project, it is "src"
4. Prepare entry function, e.g. in the demo, it is def run() in app.py, and import it in src/__init__.py
5. Prepare pyproject.toml. MUST: in [project.scripts], set adder = "app:run" (app:run is entry of program)
6. Run pex to patch (outside src/). server_cli.pex is output executable name (can be any, extention .pex not necessary)
```
pex . -o server_cli.pex -r requirements.txt -D src -c adder
```
7. Test command
```
./server_cli.pex

#code call server endpoint

import requests

params = {
    "msg": "u catch it?",
}
url = "http://0.0.0.0:8000"
rsp = requests.post(url, json = params)

rsp.json()

Output: {'msg': 'u catch it?', 'is_success': True}
```
