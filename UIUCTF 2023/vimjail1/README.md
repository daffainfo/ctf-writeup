# vimjail1
> Connect with `socat file:$(tty),raw,echo=0 tcp:vimjail1.chal.uiuc.tf:1337`. You may need to install socat.

## About the Challenge
We have been given several files related to this chall and I have collected them in 1 zip file (You can download the zip file [here](vimjail1.zip)). In this challenge, we enter `insert mode` in vim, and we have to escape `insert mode` to obtain the flag. If we check the `entry.sh` file

```bash
#!/usr/bin/env sh

chmod -r /flag.txt

vim -R -M -Z -u /home/user/vimrc
```

Overall, the command opens Vim in read-only mode with the `modified` option enabled and restricted mode active. It also uses a custom vimrc file located at `/home/user/vimrc`. And if we check the `vimrc` file

```
set nocompatible
set insertmode

inoremap <c-o> nope
inoremap <c-l> nope
inoremap <c-z> nope
inoremap <c-\><c-n> nope
```

I will explain this in each parts:
```
set nocompatible
set insertmode
```

This command will disable compatibility mode and also sets the vim into `insert mode`. And this part:

```
inoremap <c-o> nope
inoremap <c-l> nope
inoremap <c-z> nope
inoremap <c-\><c-n> nope
```

It means whenever we pressed `Ctrl + o`, `Ctrl + l`, `Ctrl + z`, and `Ctrl + \ -> Ctrl + n` insert mode will insert the word `nope`, but because we can't insert any character in `insert mode` this shortcut will be blocked by vim. Here is the preview of the chall when I pressed random character or trying pressed `Ctrl + o`:

![preview](images/preview.png)

## How to Solve?
Well if you read the `vimrc` file again. Especially this part

```
inoremap <c-\><c-n> nope
```

It means we can't pressed `Ctrl + \ -> Ctrl + n` right? It still can be bypassed by pressing `Ctrl + \` twice and then followed by `Ctrl + n`. And now we can input some commands into `vim`

![bypassed](images/bypassed.png)

So, how to obtain the flag? we can read the contents of any file by using `:e` command. `:e` means edit a file, so the final payload will be like this

```
:e flag.txt
```

![flag](images/flag.png)

```
uiuctf{n0_3sc4p3_f0r_y0u_8613a322d0eb0628}
```