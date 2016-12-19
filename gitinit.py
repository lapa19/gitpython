#this is a new python file
from git import *
import git
import requests
import sys

def make(commit_message,path,reponame):
	Repo.init(path)
	repo = Repo (path)
	print repo.git.status()
	index = repo.index
	index.add([path+'/*'])  
	index.commit(commit_message)
	data = '{"name":"'+reponame+'"}'
	requests.post('https://api.github.com/user/repos', data=data, auth=('lapa19', 'Github!23'))
	remote_path = "https://github.com/lapa19/"+reponame+".git"
	origin = repo.create_remote('origin', url=remote_path)
	#g=git.cmd.Git('/home/aparna/5thsem/wta/sublime/')
	#print(g.execute(["git", "push", "origin", "master"]))
	#origin = repo.remote('origin')
	#origin.push()
	repo.git.push('--set-upstream', 'origin','master')

if __name__ == '__main__':
	make(sys.argv[1],sys.argv[2],sys.argv[3])