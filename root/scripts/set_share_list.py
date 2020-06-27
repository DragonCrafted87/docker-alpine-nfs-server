#!/usr/bin/python3

from pathlib import Path
from os import listdir

# Local Imports
from python_logger import create_logger #pylint: disable=import-error

def main():
  logger = create_logger(Path(__file__).stem)
  logger.info(f'{listdir("/nfs_share/")}')

  base_directory = Path('/nfs_share')
  nfs_permisions = '*(rw,sync,no_subtree_check,no_auth_nlm,insecure,no_root_squash,crossmnt)'

  exports_file_path = Path('/etc/exports')
  with exports_file_path.open('a') as exports_file:
    for nfs_share_dir in base_directory.glob('*'):
      if nfs_share_dir.is_dir():
        logger.info(f'{str(nfs_share_dir)}')
        exports_file.write(f'{str(nfs_share_dir)} {nfs_permisions}\n')

if __name__ == "__main__":
  main()
