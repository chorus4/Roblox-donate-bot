import config
import requests

class RAM:
    url = f'http://localhost:{config.RAM_PORT}'

    def getAccounts(self):
        accounts = requests.get(f'{self.url}/GetAccounts?password={config.RAM_PASSWORD}').text.split(',')
        return accounts

    def launchAccount(self, account, placeId, jobId = None):
        jobidUrl = ''
        if jobId != None:
            jobidUrl = f'&JobId={jobId}'

        try:
            requests.get(f'{self.url}/LaunchAccount?Account={account}&PlaceId={placeId}&password={config.RAM_PASSWORD}{jobidUrl}', timeout=1)
        except Exception:
            pass