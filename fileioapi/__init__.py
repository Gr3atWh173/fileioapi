"""
An API wrapper for file.io
"""
import requests
from json import loads

__version__ = '0.0.2'

FILEIO = 'https://file.io'

def upload(file: str, expiry: str='14d') -> dict:
    """
    Upload a file to the service

    :params file: the file to upload
    :params expiry: expiration period (defaults to 14 days or 14d)
    :returns: the response dict
    """

    payload  = {'file': open(file, 'rb')}
    url      = FILEIO + f'?expiry={expiry}'
    response = requests.post(url, files=payload)

    return loads(response.text)

def download(location: str, filename: str=':') -> int:
    """
    Download a file from the service

    :params location: the URL or the identifier of the file to download
    :params filename: the file to write to
    :returns: the number of bytes written to disk if successfull
    """
    
    if len(location) == 6:
        location = FILEIO + '/' + location
    
    if filename == ':':
        file_on_disk = location[-6:]
    else:
        file_on_disk = filename
    
    content = requests.get(location).text
    
    fh = open(file_on_disk, 'w')
    n = fh.write(content)
    fh.close()

    return n




