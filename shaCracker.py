#!/usr/bin/env python3
import argparse
import sys
import os
from time import asctime
from hashcrack import Cracker, Information

def main():

    LOGO = r'''
                ┏━┓╻ ╻┏━┓┏━╸┏━┓┏━┓┏━╸╻┏ ┏━╸┏━┓
                ┗━┓┣━┫┣━┫┃  ┣┳┛┣━┫┃  ┣┻┓┣╸ ┣┳┛
                ┗━┛╹ ╹╹ ╹┗━╸╹┗╸╹ ╹┗━╸╹ ╹┗━╸╹┗╸
         https://github.com/ProfessorJarIO/shaCracker/
    '''
    print(LOGO)

    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--wordlist", help="Enter path to wordlist")
    parser.add_argument("-f", "--hashfile", help="Enter path to hashfile")
    parser.add_argument("-o", "--outfile", help="Enter the name of outfile")
    parser.add_argument("-t", "--hashtype", help="Enter the specific hash-type")
    parser.add_argument("-a", "--listhashes", required=False, action='store_true', help="OPTIONAL: Lists all supported hashes in this program")
    args = parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    if args.listhashes:
        valid_hashes = Information().available_hashes()
        print(valid_hashes)
        return
    
    if not os.path.exists(args.wordlist):
        print(f"Wordlist {args.wordlist} doesn't exist!")
        return

    if not os.path.exists(args.hashfile):
        print(f"Hashfile {args.hashfile} doesn't exist!")
        return
    
    c = Cracker(args.wordlist, args.hashfile, args.outfile, args.hashtype)

    startTime = asctime()

    c.potfileExist()
    crackedHash = c.brute()

    for key in crackedHash:
        print(f"{key} => {crackedHash[key]}")
    
    print(f"\nStarted: {startTime}\nStopped: {asctime()}")

if __name__=='__main__':
    main()