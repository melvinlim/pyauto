import subprocess
batchFile='C:\\Users\\winuser\\scriptllama\\start-dolphin.bat'
#serverPath='C:\\Users\\winuser\\llamacpp\\server.exe'
#serverArgs='C:\\Users\\winuser\\llamacpp\\server.exe -m C:\\Users\\winuser\\scriptllama\\models\\dolphin-2.2.1-mistral-7b.Q6_K.gguf -c 4096 --host 0.0.0.0 --port 8080 -v --log-format json'
#serverArgs=serverArgs.split(' ')
#subprocess.call(['C:\\Users\\winuser\\scriptllama\\start-dolphin.bat'])
#subprocess.Popen(serverArgs,executable=serverPath)
#p=subprocess.Popen(serverArgs,executable=serverPath,stdout=subprocess.PIPE)

#p=subprocess.Popen(serverArgs,executable=serverPath)

#outs,errs=p.communicate('',timeout=15)
#print(outs)
#print(errs)

def startProc(args,ex):
    p=subprocess.Popen(args,executable=ex)

def startDolphin():
    serverPath='C:\\Users\\winuser\\llamacpp\\server.exe'
    serverArgs='C:\\Users\\winuser\\llamacpp\\server.exe -m C:\\Users\\winuser\\scriptllama\\models\\dolphin-2.2.1-mistral-7b.Q6_K.gguf -c 4096 --host 0.0.0.0 --port 8080 -v --log-format json'
    startProc(serverArgs,serverPath)

#startDolphin()

def startEdge(page=None):
    serverPath="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    serverArgs=["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"]
    if(page!=None):
        serverArgs+=[page]
    startProc(serverArgs,serverPath)

#startEdge('www.google.com')
startEdge('http://localhost:8000')
