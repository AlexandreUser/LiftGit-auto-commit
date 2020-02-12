from git import Repo, remote
import subprocess
import threading
import requests
import os


def GenerateCommits(version):
    path = "../../GreenShield-core"
    myCmd = os.popen(
        "cd "+path+"&& cd __version && touch 1.0."+str(version)+".md && git add . && git commit -m 'configured lift'").read()
    repo = Repo(path)

    origin = repo.remote(name='origin')
    origin.push("master")

    return str(myCmd)


result = GenerateCommits(1)
i = 0
while i < 20:
    GenerateCommits(i)
    i += 1
