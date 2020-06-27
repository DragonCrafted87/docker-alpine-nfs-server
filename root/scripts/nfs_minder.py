#!/usr/bin/python3

from sys import exit as sys_exit
from subprocess import run
from subprocess import Popen
from pathlib import PurePath
from os import system
from signal import signal
from signal import SIGINT
from signal import SIGTERM
from time import sleep

# Local Imports
from python_logger import create_logger #pylint: disable=import-error

#pylint: disable=expression-not-assigned
#pylint: disable=subprocess-run-check

def is_process_running(process_name):
  call = 'pgrep', process_name
  return not bool(run(call, capture_output=True).returncode)

def stop_container(_signal_number, _stack_frame):
  logger = create_logger(PurePath(__file__).stem)
  logger.info('Stopping Container.')
  system('rpc.nfsd 0')
  sleep(1)
  sys_exit(0)

signal(SIGINT, stop_container)
signal(SIGTERM, stop_container)

def main():
  logger = create_logger(PurePath(__file__).stem)

  logger.info('Starting rpcbind.')
  Popen(['rpcbind', '-w']).pid

  logger.info(run(['rpcinfo'], capture_output=True).stdout)

  logger.info('Starting rpc.nfsd.')
  Popen(['rpc.nfsd', '--grace-time', '10' '--no-nfs-version', '3', '--no-nfs-version', '2', '--debug', '8']).pid

  logger.info('Starting exportfs.')
  Popen(['exportfs', '-rv']).pid

  logger.info(run(['exportfs'], capture_output=True).stdout)

  logger.info('Starting rpc.mountd.')
  Popen(['rpc.mountd', '--no-nfs-version', '3', '--no-nfs-version', '2', '--debug', 'all', '--no-udp']).pid

  # wait for the kill command
  while True:
    sleep(5)

if __name__ == "__main__":
  main()
