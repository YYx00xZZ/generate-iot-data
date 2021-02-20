import fire
import confu


def add(a: int, b: int):
    """
    Returns sum of a and b
    :param a: first argument
    :param b: second argument
    :return: sum of a and b
    """
    return a+b

def generate(*args,**kwargs):
    """
    Returns sum of a and b
    :param a: first argument
    :param b: second argument
    :return: sum of a and b
    """
    should_be_list = confu.gen(*args,**kwargs)
    print(type(should_be_list))
    print(should_be_list)
    # confu.save_all_scripts(should_be_list)
    return should_be_list

def generate_code(*args,**kwargs):
    


def runner():
    print("RUNER RUN")
    processes = ()
    clients = os.listdir('gen_clients')
    for c in clients:
        processes = processes + ('gen_clients/'+c,)

    def run_process(process):
        os.system('python {}'.format(process))
        print(process)

    pool = Pool(processes=len(processes))
    pool.map(run_process,processes)

    # pass


if __name__ == "__main__":
    fire.Fire({
        "sum": add,
        "gen": confu.gen,
        "generate": generate,
        "runner": runner,
    })
    # print(dir(confu))