#this is a new python file
from git import *
import git
def make(commit_message,path):
	repo = Repo (path)
	print repo.git.status()
	#added a new line
	index = repo.index
	index.add([path+'/*'])  
	index.commit(commit_message)
	#g=git.cmd.Git('/home/aparna/5thsem/wta/sublime/')
	#print(g.execute(["git", "push", "origin", "master"]))
	origin = repo.remote('origin')
	origin.push()