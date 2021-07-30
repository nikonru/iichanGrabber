# iichanGrabber
Simple image grabber for iichan.hk

Now it can only read already downloaded html, finds links to pictures and save them in new directory.
 ```console
python iichan_grabber.py file [-d img, -w pictures]
```

 - Script will parse thread from this html file:
```console
file
```

- Directory name, by default it is "img":
```console
-d
```
- Name wrapper, which will be added to the names of file, 
for example if I use ```-w pic``` then the first image will 
be saved as ```pic[0].jpg```, by default it is empty string

```console
-w
```


