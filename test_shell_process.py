""" Manual tests """

import os
import sys
from pathlib import Path
import time

from shell_process import global_shell, in_dir, execute

here = Path(os.path.abspath(os.path.dirname(__file__))).expanduser()

def test_1():
    execute('echo hello from bash')
    time.sleep(2)
    execute('echo hello from bash again')

def test_2():
    p = global_shell()
    with p(show_time_elapsed=True):
        execute('echo hello from bash')
        time.sleep(2)
        execute('echo hello from bash again')

def test_3():
    """ ssh to itself. When using ssh config files, with variables inside, using `export` command can make 
    bashprocess very handy. """
    import socket
    hostname = socket.gethostname()
    # ssh to itself
    cmd = f"pwd"
    execute(f"ssh {hostname} {cmd}")
    # show difference with current process:
    os.system(cmd)

def test_4():
    """ raise exception """
    execute("dfasdfasdfkajsdfasdkfadsfajk", allow_error = True)
    execute("echo hello")
    try:
        execute("dfasdfasdfkajsdfasdkfadsfajk")
        execute("echo hello again (should not be visible)")
    except:
        print("Could not execute without errors")


def test_5():
    p = global_shell()
    p.set_silent(True)
    test_4()

def test_6():
    p = global_shell()
    with p(show_time_elapsed=True):
        execute("echo Sleeping for a while; sleep 3;")

def test_7():
    """ This works as expected, but not sure if this is wanted """
    p = global_shell()
    execute("sleep 5; echo not working", timeout = 1)
    print(f"Timeout reached: {p.has_timeout}, but will still wait next execute")
    execute("echo again waited on previous command")

def test_8():
    """ sleep and raise KeyboardInterrupt """
    global_shell().allow_user_input = True
    execute("echo Going to sleep, please raise KeyboardInterrupt..; sleep 10")


def test_9():
    """ do something with context inside bash, or advanced output from bash and handle this in python """
    pass

def test_10():
    """ read variable from user during execute """
    global_shell().allow_user_input = True
    execute("echo Hello, who are you?; read varname; echo Its nice to meet you $varname;")
    execute("read varname")
    execute("echo Its nice to meet you $varname")


def test():
    global_shell().allow_user_input = True
    execute("sudo ls")

def main(args):
    test_1()
    #test_2()
    #test_3()
    #test_4()
    #test_5()
    #test_6()
    #test_7()
    #test_8()
    #test_10()
    #test()

if __name__ == '__main__':
    main(sys.argv[1:])