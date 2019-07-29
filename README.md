# File.io
An API wrapper for the file.io web service.

## Install
```bash
$ pip3 install fileio
```

or

```bash
$ git clone https://github.com/gr3atwh173/fileioapi
$ cd fileioapi
$ python3 setup.py install
```

## Usage
```python
import fileioapi

# upload a file
resp = fileioapi.upload("image.png", expiry="12w")

# download a file and save to 'downloaded.png'
down = fileioapi.download(resp['link'], filename='downloaded.png')

```
