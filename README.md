# Kainexus-Multichart-Import
Service which automatically will import xlsx through kainexus multi chart functionality. 

Personally I export this code to exe with pyinstaller, below u can find code:
```
pyinstaller.exe -c --onefile main.py
```
And in next step using NSSM I'm installing service on server.
```
cd C:\Python\Tools\nssm-2.24\win64
nssm.exe install
```
![image](https://user-images.githubusercontent.com/35203089/173358031-913d48ae-2e58-4f46-952b-a3c6a8da4f10.png)

This is how it's look in windows services:
![image](https://user-images.githubusercontent.com/35203089/173358493-6edd6207-2d91-4cc6-aca3-8037a100e32c.png)
