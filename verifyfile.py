#!/usr/bin/env python3

import os
import sys
import fs
from fs import open_fs
import gnupg

gpg = gnupg.GPG(gnupghome="/Users/stephenpeters/.gnupg")
home_fs = open_fs("./test")

script_to_run = str(sys.argv[1])

with open("../../signatures/" + script_to_run + ".sig", "rb") as f:
    verify = gpg.verify_file(f, script_to_run)
    print(script_to_run + " ", verify.status)
    if verify.status == "signature valid":
        print("Signature valid, launching script...")
        exec(open(script_to_run).read())
    else:
        print("Signature invalid or missing, ")
        print("aborting script execution")
