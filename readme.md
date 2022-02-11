# Identicon
Identicon image generator  
![image](screenshot.png)
## Notes
Simple API for generating icon images from string value,
with GitHub identicons style.  
There are few bash scripts for running the app in docker container.

Default URLs to use with docker:
- `http://localhost:9090/getimage/<string value>`
- `http://localhost:9090/getimage/<string value>?size=<integer value>`  
Size parameter may be set as width in pixels of one side,
in range from 5 to 255.
