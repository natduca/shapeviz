Getting set up
---
Downlaod and install nodejs, https://nodejs.org/en/download/ on mac, apt get install nodejs. Sorry.
Then
```
npm install -g vulcanize
```

Finally
```
git submodule update --init --recursive
```

You should be good to go.


Running shapeviz
---

./shapeviz <filename>


Contributing to shapeviz
---
From shapeviz, start this and leave it going:
```
python -m SimpleHTTPServer 8003
```
Now open a chrome and go to http://localhost:8003/test/basic.html .
Debug & reload in there.