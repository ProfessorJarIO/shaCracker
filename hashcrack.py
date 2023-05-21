#!/usr/bin/env python3
import os
import sys
import hashlib

__author__ = 'ProfessorJarIO'

class Cracker:
    def __init__(self, wordlist: str, hashfile: str, outfile: str, hashtype: str):
        self.wordlist = wordlist
        self.hashfile = hashfile
        self.outfile = outfile
        self.hashtype = hashtype

    def brute(self):
        """Brute force hashes
        """

        # Cracked hashes will be put in this dictionary
        found_hash = {}

        # Opens up the hash file and reads every line
        hash_list = []
        with open(self.hashfile, 'r') as hash_file:
            for i in hash_file.readlines():
                hash_list.append(i.strip('\n'))

        # We go through every hash on each line in hash_list
        for hashes in hash_list:
            # We open up our user specified wordlist
            with open(self.wordlist, 'r', encoding="latin-1") as dictionary:
                # We read every line in the specified wordlist
                for password in dictionary.readlines():
                    # We check if the user specified hashtype and give it the appropriate methods
                    if self.hashtype == 'sha256':
                        convert_hash = hashlib.sha256(password.strip("\n").encode('latin-1')).hexdigest()
                    elif self.hashtype == 'sha512':
                        convert_hash = hashlib.sha512(password.strip("\n").encode('latin-1')).hexdigest()
                    elif self.hashtype == 'md5':
                        convert_hash = hashlib.md5(password.strip("\n").encode('latin-1')).hexdigest()
                    elif self.hashtype == 'md4':
                        convert_hash = hashlib.md4(password.strip("\n").encode('latin-1')).hexdigest()
                    elif self.hashtype == 'whirlpool':
                        convert_hash = hashlib._hashlib.new(name='whirlpool', string=password.strip("\n").encode('latin-1')).hexdigest()
                    else:
                        sys.exit(f"Invalid hash type: {self.hashtype}")

                    # We found a match from the hash and wordlist
                    if convert_hash == hashes:

                        # We save it to the user specified outfile
                        with open(self.outfile, 'a') as append_cracked_hash:
                            append_cracked_hash.write(f"{convert_hash}:{password}")

                        # We add the cracked hash into found_hash directory and strip any new lines
                        found_hash[convert_hash] = password.strip("\n")
                        break

        return found_hash

    def potfileExist(self):
        """Checks if user specified hash exists in potfile
        """

        # Opens up the hash file and reads every line
        hash_list = []
        with open(self.hashfile, 'r') as hash_file:
            for i in hash_file.readlines():
                hash_list.append(i.strip('\n'))
        
        # Checks if user specified outfile exists
        if os.path.exists(self.outfile):
            # We go through every hash in the hash_list variable
            for hashes in hash_list:
                # We open the outfile
                with open(self.outfile, 'r') as potfile:
                    # We go through every line in the outfile
                    for potfile_hash in potfile.readlines():
                        # We split on ':' and only want the hash
                        potfile_list_hash = potfile_hash.split(':')[0]
                        # If the hash matches the user specified hashfile, we prompt the user that it exists
                        if potfile_list_hash == hashes:
                            sys.exit(f"{hashes} already exists in {self.outfile}")

class Information:
    # Lists the currently available hashes this program can crack
    def available_hashes(self):
        """Lists out currently available hashes this program can crack
        """
        return 'sha256, sha512, md5, md4, whirlpool'