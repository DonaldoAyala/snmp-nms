import re
import time

def getIps(string):
    string = string[string.find("[")+1:string.rfind("]")]
    results = re.findall(r'\[.*?\]', string)
    return results

def getMessages(string):
    return re.findall(r'\".*?\"', string)

def getHour(string):
    return string[0:19]

lines = []
def translateTraps(fileRoute):
    lines = []
    with open(fileRoute) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].startswith('2021'):
                source, destiny = getIps(lines[i])
                hour = getHour(lines[i])
                messages = getMessages(lines[i + 1])
                message = ' '.join(messages).replace('"', '')
                if (len(messages) > 0):
                    print(f'Message received at ({hour}) from {source}: {message}')
