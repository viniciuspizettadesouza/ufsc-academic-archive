import requests
import tempfile
import subprocess

def generate_parser(g4_file):
    antlr_url = 'https://www.antlr.org/download/antlr-4.9.1-complete.jar'
    antlr_request = requests.get(antlr_url, allow_redirects=True)

    tool = tempfile.NamedTemporaryFile(mode='w+b', delete=False)
    tool.write(antlr_request.content)
    tool.close()

    antlr = ['java', '-Xmx500M', '-cp', tool.name, 'org.antlr.v4.Tool']
    param = ['-Dlanguage=Python3', '-visitor', '-no-listener']

    call = antlr
    call.extend(param)
    call.append(g4_file)

    subprocess.call(call)
