# /usr/bin/python -i


# # import json
    # import yaml

    # import pprint
    # import contextlib
    # @contextlib.contextmanager
    # def pprint_nosort():
    #     # Note: the pprint implementation changed somewhere
    #     # between 2.7.12 and 3.7.0. This is the danger of
    #     # monkeypatching!
    #     try:
    #         # Old pprint
    #         orig,pprint._sorted = pprint._sorted, lambda x:x
    #     except AttributeError:
    #         # New pprint
    #         import builtins
    #         orig,pprint.sorted = None, lambda x, key=None:x

    #     try:
    #         yield
    #     finally:
    #         if orig:
    #             pprint._sorted = orig
    #         else:
    #             del pprint.sorted

    # # For times when you don't want sorted output
    # with pprint_nosort():
    #     pprint.pprint({"def":2,"ghi":3, "abc":1})

    # #by me
    # def nosort(*arg):
    #     with pprint_nosort():
    #         pprint.pprint(arg[0])


    # def ppr(*arg):
    #     # For times when you do want sorted output
    #     pprint.pprint(arg[0])


    # file = open('/home/alex/Desktop/a_device.yml', 'r')
    # cfg = yaml.load(file, Loader=yaml.FullLoader)
    # print(cfg['device']['token'])

    # print(f'\n{cfg}\n')

    # print(yaml.dump(cfg, sort_keys=False))


# # # DONT change code line order


import os
import readline
import yaml
from random import randint
import namesgenerator
from faker import Faker
from contextvars import ContextVar

fatal_text = '[FATAL]\t'
debug_text = '[DEBUG]\t'
info_text = '[INFO]\t'
warning_text = '[WARNING]\t'

# debug PACKAGE
def printd(*args):
    # print(arg)
        # colorize
    return print(f'{debug_text}{args}')# + '\t {x}'.format(x=arg))
    # for x in arg.keys():
        # print('[DEBUG]\t{x}'.format(x=x))
# debug PACKAGE

import sys
try:
    clear = lambda: os.system('clear')
    ls = lambda *args: os.listdir(f'{args[0]}') if args else os.listdir('.')
    ls_all = ls('output')
except: # catch *all* exceptions
    e = sys.exc_info()[0]
    if e == FileNotFoundError:
        print(f'{fatal_text}Output dir not found')
        print(f'{info_text}Automatically creating now')
        os.makedirs('./output')
        os.makedirs('./gen_clients')
        print(f'{info_text}"Done."')
        printd("PLEASE RESTART SCRIPT","ctrl+d")
        """TODO
        printd("RESTARTING..")
        # os.system("python -i confu.py")
#    write_to_page( "<p>Error: %s</p>" % e )
        """
    else:
        print("<p>Error: %s</p>" % e)


fake = Faker()

def rand_eventName():
    rand_eventName = fake.name()
    rand_eventName= rand_eventName.replace(' ','-')
    rand_eventName = f'{rand_eventName}-{str(randint(0,999))}'
    return rand_eventName


fake_device = {
    'eventName': rand_eventName(),
    'device': {
        'name': [namesgenerator.get_random_name()],
        'token': [fake.uuid4()],
        'signaln': [randint(0,10)],
        # 'payload': ['msg payload line']
        'payload': [fake.word()]
        }
    }


def gen(*args, **kwargs): # x):
    """
    generate N devices;
    TODO option to specify token which to be used for every device;
    WORKING;
    """

    if args or kwargs:
        x = args[0]
        files_to_read = []
        if kwargs:
            group = fake.word()
            #single token fake devices
            for i in range(0, x):
                fake_device = {
                    'eventName': fake.word()+'-event',
                    'device': {
                        'name': namesgenerator.get_random_name(),
                        'token': kwargs['token'],
                        'signaln': randint(0,10),
                        'sensor': [str(fake.word())],
                        'value': [randint(0,999)],
                        # 'payload': [f'"sensor":{fake.word()}, "value":{randint(0,999)}']
                        }
                    }
                file_name = f'{fake_device["eventName"]}.yaml'
                with open(r'output/{filename}'.format(filename=file_name), 'w') as file:
                    documents = yaml.dump(fake_device, file, sort_keys=False)
                # print(fake_device)
                files_to_read.append(file_name)
        else:
            # random fake devices
            for i in range(0, x):
                fake_device = {
                    'eventName': fake.word()+'-event',
                    'device': {
                        'name': namesgenerator.get_random_name(),
                        'token': fake.uuid4(),
                        'signaln': randint(0,10),
                        'sensor': [str(fake.word())],
                        'value': [randint(0,999)],
                        # 'payload': [f'"sensor":{fake.word()}, "value":{randint(0,999)}']
                        }
                    }
                file_name = f'{fake_device["eventName"]}.yaml'
                with open(r'output/{filename}'.format(filename=file_name), 'w') as file:
                    documents = yaml.dump(fake_device, file, sort_keys=False)
                # print(fake_device)
                files_to_read.append(file_name)
        print('-'*7+'[END]'+'-'*7)
        print()
        print()
        return files_to_read
    else:
        print('enter num of stubs to gen, e.g. gen(1)')
        return



def read_all(*args): # files_to_read):
    """
    print config of every device;
    TODO add filtering methods etc.;
    NOT WORKING;
    """
    for x in args[0]:
        printd(f'opening {x[0]}')
        with open(r'output/{x}'.format(x=x)) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            fruits_list = yaml.load(file, Loader=yaml.FullLoader)
            print(fruits_list)


def show_config(*args, **kwargs):
    """show_config of - shows the config of a stub;
    """
    if args or kwargs:
        with open(r'output/{x}'.format(x=kwargs['of'])) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            stub_config = yaml.load(file, Loader=yaml.FullLoader)
            return stub_config
    else:
        if input(f'You have to select a stub to show config for.\nLaunch interactive pick mo? [y/N] ') == 'y':
            picked_stub = _show_menu(_pick)
            with open(r'output/{x}'.format(x=picked_stub)) as file:
                stub_config = yaml.load(file, Loader=yaml.FullLoader)
                return stub_config
        else:
            print('wtf man')
            return


__history = lambda history_len: [readline.get_history_item(hitem) for hitem in range(history_len)]


def history(*args):
    max_hist_len = readline.get_current_history_length()
    # printd(max_hist_len)
        # import time
        # time.sleep(1)
        # if args:
        #     printd("history if")
        #     scrollback = args[0]
        # else:
        #     printd("history else")
    h = __history(max_hist_len)
    h_limited = h[max_hist_len-12:]
    for each in range(max_hist_len-12, max_hist_len):
        msg = f'{each}\t{readline.get_history_item(each)}'
        print(msg)


def _show_menu(*args, **kwargs):
    """
    PRIVATE;
    """
    stubs = ls('output')
    menu = {}
    n = 0
    for x in stubs:
        menu[n] = x
        # for ele in x['0']:
            # str1 = ''
            # str1 += ele
            # print(str1)
        # printd(x, n)
        # printd({n: x})
        n += 1
    print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in menu.items()) + "}")
    _pick = args[0]
    return menu[_pick()]


def _pick(*args):
    """
    PRIVATE;
    """
    # internal use of func
    stubs = ls('output')
    stubs_count = len(stubs)
    if len(stubs) == 0:
        print(f'Nothing to _pick from :(. First generate few stubs with gen().')
        return
        # break
    else:
        # menu = {}
            # n = 0
            # for x in stubs:
            #     menu[n] = x
            #     # for ele in x['0']:
            #         # str1 = ''
            #         # str1 += ele
            #         # print(str1)
            #     # printd(x, n)
            #     # printd({n: x})
            #     n += 1
            # # printd(stubs)
            # # printd(stubs_count)
            # print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in menu.items()) + "}")
        choice = input('_pick file to read ')
        # print(choice)
        return int(choice)
    return int(choice)


def load_config(*args, **kwargs):
    """
    this WILL be used to load a device as Context so we are able to run e.g. commands;
    like remote terminal
    NOT WORKING
    """
    if args or kwargs:
        with open(r'output/{x}'.format(x=kwargs['of'])) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            stub_config = yaml.load(file, Loader=yaml.FullLoader)
            var = ContextVar('deviceName')
            deviceName = var.set(stub_config['device']['name'])
            return var
            # return stub_config
    else:
        if input(f'You have to select a stub to show config for.\nLaunch interactive pick mo? [y/N] ') == 'y':
            picked_stub = _show_menu(_pick)
            with open(r'output/{x}'.format(x=picked_stub)) as file:
                stub_config = yaml.load(file, Loader=yaml.FullLoader)
                var = ContextVar('deviceName')
                deviceName = var.set(stub_config['device']['name'])
                return var
                # return print(yaml.dump(stub_config, sort_keys=False))
        else:
            print('wtf man')
            return


### this can live in diff file
def gen_scripts(*args):
    file = args[0]
    with open(file,'r') as stream:
        z = yaml.safe_load(stream)
        return (
        f"import requests\n"
        f"import asyncio\n"
        f"import os\n"
        f"import signal\n"
        f"import time\n"
        f"# import requests\n"
        f"from pprint import pprint\n"

        f"from gmqtt import Client as MQTTClient\n"

        f"# gmqtt also compatibility with uvloop  \n"
        f"import uvloop\n"
        f"asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())\n"


        f"STOP = asyncio.Event()\n"

        f"payload='device {z['device']['name']} connected'\n"

        f"def on_connect(client, flags, rc, properties):\n"
        f"    print('Connected')\n"
        f"    if flags != 0:\n"
        f"        print(flags)\n"
        f"\n"
        f"    if rc != 0:\n"
        f"        print(rc)\n"
        f"    pprint(properties)\n"
        f"    client.subscribe('TEST/{z['device']['name']}', qos=0)\n"
        # f"    rr = requests.get('http://localhost:8080/welcome', params=payload)\n"
        # f"    print(rr.text)\n"


        f"def on_message(client, topic, payload, qos, properties):\n"
        f"    print('RECV MSG:', payload, 'ON TOPIC:', topic)\n"
        f"    if payload.decode() == 'fire':\n"
        f"        pass\n"
        f"\n"


        f"def on_disconnect(client, packet, exc=None):\n"
        f"    print('Disconnected')\n"
        f"\n"

        f"def on_subscribe(client, mid, qos, properties):\n"
        f"    print('SUBSCRIBED')\n"
        f"    client.publish('TEST/{z['device']['name']}', 'fire', qos=0)\n"
        # f"    print(properties)\n"
        f"\n"

        f"def ask_exit(*args):\n"
        f"    STOP.set()\n"
        f"\n"

        f"async def main(broker_host, token):\n"
        f"    client = MQTTClient('{z['device']['name']}')\n"
        # f"    print(dir(client))\n"
        f"    client.on_connect = on_connect\n"
        f"    client.on_message = on_message\n"
        f"    client.on_disconnect = on_disconnect\n"
        f"    client.on_subscribe = on_subscribe\n"
        f"    \n"
        f"    client.set_auth_credentials(token, None)\n"
        f"    await client.connect(broker_host)\n"
        f"\n"

        # f"    client.publish('TEST/TIME', str(time.time()), qos=0)\n"
        f"    client.publish('TEST/{z['device']['name']}', 'fire', qos=0)\n"# str({z['device']['sensor']}+{z['device']['value']}), qos=0)\n"
        f"\n"

        f"    await STOP.wait()\n"
        f"    await client.disconnect()\n"


        f"if __name__ == '__main__':\n"
        f"    loop = asyncio.get_event_loop()\n"
        f"    host = 'mqtt.flespi.io'\n"
        f"    token = '{z['device']['token']}'\n"
        f"    \n"
        f"    loop.add_signal_handler(signal.SIGINT, ask_exit)\n"
        f"    loop.add_signal_handler(signal.SIGTERM, ask_exit)\n"
        f"\n"

        f"    loop.run_until_complete(main(host, token))\n")


def save_script(*args):
    script_name = args[0]
    script_name = script_name.strip('.yaml').replace('-', '_')
    script_name = script_name+'.py'
    script_content = args[1]
    print(f'\n\n{script_name}\n\n')
    with open(script_name, 'w') as streamout:
        streamout.write(script_content)

def save_all_scripts(*args):
    devs = args[0]
    for x in devs:
        z = gen_scripts('output/'+x)
        save_script('gen_clients/'+x,z)

### this can live in diff file
def test():
    devs = gen(10,token='Umi9qoGBYmWdesfHxw3fXpy4rUIsO5vwiEvwQZWEbIHdYLIj7BoTQKN5vmm7fHtl')
    for x in devs:
        z = gen_scripts('output/'+x)
        save_script('gen_clients/'+x,z)


# flespi id Umi9qoGBYmWdesfHxw3fXpy4rUIsO5vwiEvwQZWEbIHdYLIj7BoTQKN5vmm7fHtl