import subprocess
from subprocess import PIPE

from multiprocessing import Pool
import multiprocessing as multi

def process(i):
    subprocess.run(['curl', 'http://192.168.1.14:5000/', '-s', '-o', '/dev/null'], stdout=PIPE, text=True)
    #subprocess.run(['curl', 'http://192.168.1.14:8080/', '-s', '-o', '/dev/null'], stdout=PIPE, text=True)

p = Pool(multi.cpu_count()*4)
p.map(process, list(range(40)))
p.close()

proc = subprocess.run(['sudo', 'k3s', 'kubectl', 'get', 'pod', '-o', 'wide'], stdout=PIPE, text=True)
data = proc.stdout
for x in data.split('\n'):
    if x.startswith('flask'):
    #if x.startswith('ad'):
        logp = subprocess.run(['sudo', 'k3s', 'kubectl', 'logs', x.split(' ')[0]], stdout=PIPE, text=True)
        i = 0
        for y in logp.stdout.split('\n')[5:]:
            i += 1
        print(x.split(' ')[0] + list(filter(lambda a: a != '', x.split(' ')))[6].rjust(13, ' ') + ' ' + str(i))
