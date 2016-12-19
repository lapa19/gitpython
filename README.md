# gitpython
Python scripts to perform basic Git operations. Uses Gitpython (Python library to interact with Git repositories, https://gitpython.readthedocs.io/en/stable/).

#gitinit.py:
A simple script which takes commit message(commit_message), path to repository on local machine and remote repository name and performs the following in the local system path specified:

git init

git add .

git commit -m commit_message

git remote add origin

creates a git repository with name reponame using Python's requests(http://docs.python-requests.org/en/master/) package

git push origin master

#gitf.py:
Python script to push to an existing repository. Takes path and commit message as parameters and performs the following:

git add .

git commit -m commit_message

git push origin master
