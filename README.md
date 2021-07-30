# iichanGrabber
Simple image grabber for iichan.hk

Now it can only read already downloaded html, find where links to pictures and store them in new directory.

```console
-d```- directory name, by default it is "img"

```console
-w... - name wrapper, which will be added to files for exmple the first image will be saved as ```wrapper[0].jpg``` by default it is empty string


```console
python iichan_grabber.py file [-d img, -w pictures]
...

