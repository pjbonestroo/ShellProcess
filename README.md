# A wrapper of a shell process

Manage the command line from Python

This is not a tool to make a CLI, but a tool to manage the command line from Python.

Works currently only on Linux

## Examples

```python
from shell_process import global_shell, in_dir, execute

execute('echo hello from bash')
time.sleep(2)
execute('echo hello from bash again')

# ssh
import socket
hostname = socket.gethostname()
cmd = 'pwd'
execute(f"ssh {hostname} {cmd}")

# exceptions
execute("dfasdfasdfkajsdfasdkfadsfajk", allow_error = True)
execute("echo hello")
try:
    execute("dfasdfasdfkajsdfasdkfadsfajk")
    execute("echo hello again (should not be visible)")
except:
    print("Could not execute without errors")


p = global_shell()
with p(show_time_elapsed=True):
    execute("echo Sleeping for a while; sleep 3;")

global_shell().allow_user_input = True
execute("echo Hello, who are you?; read varname; echo Its nice to meet you $varname;")
execute("read varname")
execute("echo Its nice to meet you $varname")



```

