
import click
import json
import os

from .fcfs import FCFS
from .rr import RR
from .sjf import SJF


path = os.path.join('files', 'data.json')
with open(path, 'r') as json_file:
    data = (json.load(json_file))

processes = json.loads(data['processes'])
start_time = json.loads(data['start_time'])
quantum = json.loads(data['quantum'])
proc = json.loads(data['proc'])

# import ipdb; ipdb.set_trace()

def get_fcfs():
    return FCFS(processes, len(processes), start_time)

def get_rr():
    return RR(processes, len(processes), start_time, quantum)

def get_sjf():
    return SJF(proc, len(proc))

# click commands 
@click.command()
def get_fcfs_stats():
    get_fcfs().getStats()

@click.command()
def get_rr_stats():
    get_rr().getStats()

@click.command()
def get_sjf_stats():
    get_sjf().getStats()

@click.group()
def cli():
    """Expose multiple commands allowing one to work with lily_assistant."""
    pass


cli.add_command(get_fcfs_stats)
cli.add_command(get_rr_stats)
cli.add_command(get_sjf_stats)
