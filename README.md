# Output splitter

This tool allows for redirecting parts of standard output to a file.

Usage:

```
./your-app-name | splitter.py
```

Suppose your application produces the following output:

```
W--->file1.txt
This text goes to file1.txt

W--->file2.txt
This text goes to file2.txt

S--->The filename is now reset (anything can be wirtten in this line with no effect)
This content is would not go to any file. By the way... The tags should always start
from a new line. The following character sequence "W--->file2.txt" is not a tag.

A--->file2.txt
This tag text will become appended to file2.txt

W--->file1.txt
This content will overwrite file1.txt so upper-case tags are unsafe. Prefer using
lower case ones unless you know what you are doing.

w--->file1.txt
Lower case tags are safe and are are introduced to prevent you from accidentally
overwriting existing files. If a file already exists it will be renamed to something
like:

------------------------------------
file1.txt.2021-01-22_17:36:50.955739
------------------------------------

thus preserving original content.

w--->file1.txt
The time value used to concatenate an existing filename is the time of splitter.py launch

It is a good idea to concatenate the original name using the time of start because
we can launch splitter.py many times along with subject program. This would create
multiple files with common part in it. It allows for a simple groupping of different
files from a single run. What a wonderful idea, right?

w--->file1.txt
Well... No! Since such a poor choice of timestamp can now cause an overwrite of
original backed up file:

------------------------------------
file1.txt.2021-01-22_17:36:50.955739 (this filename is already used above)
------------------------------------

if we're opening for 'write' the same file several times within one session.

...

Right?

Well no, this case is handled by the splitter.py and it would save the file by
renaming that file to a name similar to the following one:

file1.txt.2021-01-22_17:36:50.955739.dead-since.2021-01-22_17:36:50.955871

The second timestamp represents the time when renaming is happened.

This second time can be helpful because now you can now see how much time
did it take between these two writes. It's like a timer that you don't
need to explicitly initialize. You can revise this information after years
if you save your logs. Just separate your outputs using splitter.py tags.

a--->file2.txt
This text will append to file2.txt

a--->file2.txt
This text will append to file2.txt

a--->file2.txt
This text will append to file2.txt

```

This would create a set of files similar to the following:

```
file1.txt
file1.txt.2021-01-22_18:37:41.217017
file1.txt.2021-01-22_18:37:41.217017.dead-since.2021-01-22_18:37:41.217250
file1.txt.2021-01-22_18:37:41.217017.dead-since.2021-01-22_18:37:41.217424
file2.txt
file2.txt.2021-01-22_18:37:41.217706
```

Just copy and paste the test output above to a `test.txt` and run `cat test.txt | splitter.py`
