# Python Tango Database DS

A python implementation of the Tango Database device server using PyTango.

The Tango interface is the same as the official C++ Tango Database device server.

It comes with a default backend which uses sqlite3.


## Installation

```bash
$ pip install pytango-db
```

## Start server

```bash
$ DataBaseds --db_access=sqlite3 --port=10000 2
```

That's all folks!

