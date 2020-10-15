from revc.revc import run
from utils.run_proxy import RunProxy

if __name__ == '__main__':
    print(RunProxy.run(id='revc', sample=False, file_output=True, callback=run))
