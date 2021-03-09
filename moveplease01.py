#1/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj? ')
#this code will rename a file when it is moved
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


