# Demo Dagger Python

Demonstration of Dagger.io Python SDK.


## Setup

Follow the [Dagger documentation](https://docs.dagger.io/quickstart/) to install Dagger on your local system.

Run:

```sh
dagger login
```

[Dagger Quickstart](https://docs.dagger.io/quickstart/daggerize)

Initialize:

```sh
dagger init --sdk=python --source=./dagger
```

### Dagger function file

Dagger will create a `dagger` directory with files such as `dagger/src/hello_dagger/main.py`:

```python
import dagger
from dagger import dag, function, object_type


@object_type
class DemoDaggerPython:
    @function
    def container_echo(self, string_arg: str) -> dagger.Container:
        """Returns a container that echoes whatever string argument is provided"""
        return dag.container().from_("alpine:latest").with_exec(["echo", string_arg])

    @function
    async def grep_dir(self, directory_arg: dagger.Directory, pattern: str) -> str:
        """Returns lines that match a pattern in the files of the provided Directory"""
        return await (
            dag.container()
            .from_("alpine:latest")
            .with_mounted_directory("/mnt", directory_arg)
            .with_workdir("/mnt")
            .with_exec(["grep", "-R", pattern, "."])
            .stdout()
        )
```

### List Dagger functions

Print all the available Dagger functions:

```sh
dagger call --help
```

Output includes the functions:

```stdout
FUNCTIONS
  container-echo   Returns a container that echoes whatever string argument is provided
  grep-dir         Returns lines that match a pattern in the files of the provided Directory
```

Note that Dagger reformats the function names into kebab case. This is because Dagger works with multiple programming languages, and aims for a language-agnostic API.


### Call container-echo

Print the Dagger main.py function syntax:

```sh
dagger call container-echo --help
```

Output includes the arguments:

```stdout
ARGUMENTS
      --string-arg string   [required]
```

Call:

```sh
dagger call container-echo --string-arg hello
```

Output includes the function and argument:

```stdout
✔ .containerEcho(stringArg: "hello"): Container! 2.3s
```

### Call grep-dir

Print the Dagger main.py function syntax:

```sh
dagger call grep-dir --help
```

Output includes the arguments:

```stdout
ARGUMENTS
      --directory-arg Directory   A directory. [required]
      --pattern string            [required]
```

Call:

```sh
dagger call grep-dir --directory-arg "." --pattern "Hello"
```

Output includes the pattern matches:

```stdout

./dagger/sdk/src/dagger/client/gen.py:            (e.g., "Hello world").
./dagger/sdk/src/dagger/client/gen.py:            Content of the file to write (e.g., "Hello world!").
./dagger/sdk/src/dagger/client/gen.py:            Content of the written file (e.g., "Hello world!").
./README.md:     print ("Hello World!")
./src/demo_dagger_python/demo.py:     print ("Hello World!")
./src/demo_dagger_python/__pycache__/demo.cpython-313.pyc: Hello World!
```


## Create a demo python project

This section has steps:

* Create a python source file

* Create a python test file


## Create a python source file

Create a demo python package layout:

```sh
mkdir -p {src/demo_dagger_python,tests}
touch {src/demo_dagger_python,tests}/__init__.py
```

Create a demo python function in file `src/demo_dagger_python/demo.py`:

```python
#!/usr/bin/env python

def add(a, b):
    return a + b

def main():
     print ("Hello World!")

if __name__ == '__main__':
    main()
```

Run:

```sh
python src/demo_dagger_python/demo.py
```

```stdout
Hello World!
```


###  Create a python test file

Create a trivial python test in file `tests/test_demo.py`:

```py
import unittest
from src.demo_dagger_python import demo

class TestDemo(unittest.TestCase):

    def test_add(self):
        self.assertEqual(demo.add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
```

Verify:

```sh
python -m unittest discover
```
