<h1>ChileTrabajos</h1>
A robot app that alert about jobs published on web page chiletrabajos.cl

<h2>Dependecies</h2>
First we need to install a virtual enviroment in the project for install packages localy and not globaly.

```bash
$>sudo apt install python3.10-venv -y
....
....
$>python3 -m venv ./virtual-environment
```

<h3 style="color:#B375CF;">Run virtual environment</h3>

* On Windows
    ```bash
    $>.\virtual-environment\Scripts\activate
    ```
* On MAC and Linux:
    ```bash
    $>source virtual-environment/bin/activate
    ```

<h3 style="color:#B375CF;">Ensure that <span style="color:#FFFF00;">pip</span> was installed on the VENV</h3>

```bash
(virtual-environment)$>which pip
(virtual-environment)$>python -m ensurepip --upgrade
```

Then, we can install all project's dependencies:

```bash
$>pip install requests bs4 playsound3
```

<h3 style="color:#B375CF;">Install <span style="color:#FFFF00;">es_ES.UTF-8</span> locale</h3>

List all locales:

```bash
$>locale -a
```

```bash
$>sudo locale-gen es_ES.UTF-8
$>sudo update-locale
```

## Notes

* **Improve compare jobs**. The most efficient way is get the list of records and the list of current jobs, in sqlite do the comparison and then insert just if not exist in the table