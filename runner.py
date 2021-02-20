import confu
import fire
import subprocess
import os


def generate(*args,**kwargs):
    print(args)
    print(kwargs)
    generated_devies = confu.gen(*args,**kwargs)
    return confu.save_all_scripts(generated_devies)

# def clear_gens():
#     process = subprocess.Popen(['rm', '-rf', 'output/ gen_clients/'],
#                         stdout=subprocess.PIPE, 
#                         stderr=subprocess.PIPE)
#     print(process)
#     stdout, stderr = process.communicate()
#     if stderr != b'':
#         print('diff')
#         print(stderr)
#         return stderr
#     else:
#         return stdout

if __name__ == '__main__':
    fire.Fire()
    # print(dir(confu))