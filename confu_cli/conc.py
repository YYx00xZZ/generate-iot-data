import os
from multiprocessing import Pool


processes = ()
clients = os.listdir('gen_clients')
for c in clients:
    processes = processes + ('gen_clients/'+c,)

def run_process(process):
    os.system('python {}'.format(process))
    print(process)

pool = Pool(processes=len(processes))
pool.map(run_process,processes)
