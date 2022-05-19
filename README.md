![](Assets/Thumbnail/725x237.png)

---

## Demo

### Auth

With Correct Password
```bash
(basic) krish@KP-Linux:~/Projects/Sudarshana$ python chakra.py
Password: password 
chakra>
chakra>
```

```bash
(basic) krish@KP-Linux:~/Projects/Sudarshana$ python chakra.py -p password
chakra>
chakra>
```

With InCorrect Password
```bash
(basic) krish@KP-Linux:~/Projects/Sudarshana$ python chakra.py
Password: abc123 
ACCESS DENIED
Exitting...
```

```bash
(basic) krish@KP-Linux:~/Projects/Sudarshana$ python chakra.py -p abc123
ACCESS DENIED
Exitting...
```

### Basic CLI
```bash
chakra> ls
Assets  chakra.py  Database  modules  README.md
chakra> pwd
/home/krish/Projects/Sudarshana
chakra> bash
$
$ exit
exit
chakra>
```

### Basic Tools
```bash
chakra> git --version
git version 2.34.1
chakra> pip --version
pip 21.2.4 from /home/krish/miniconda3/envs/basic/lib/python3.9/site-packages/pip (python 3.9)
chakra> conda --version
conda 4.12.0
```

### Robust CLI Use
```bash
chakra> !abc123
('abc123' will be excecuted in bash and the output will be shown here)
charka>
```
### Simple Utilities

```
chakra> help
im here to help you........!!!!!!
chakra> cls
[Clears the screen but i'm confused, How should i show it here]
chakra> exit
Exitting...
```