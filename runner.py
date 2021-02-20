import confu
import fire
import os


def generate(*args,**kwargs):
    print(args)
    print(kwargs)
    generated_devies = confu.gen(*args,**kwargs)
    return confu.save_all_scripts(generated_devies)


if __name__ == '__main__':
    fire.Fire()
    # print(dir(confu))