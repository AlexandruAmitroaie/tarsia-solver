# About 
.. this should describe the problem we are solving. 

# Notes on the implementation

There is a segmentation fault which I was not able to identify / fix.

As such we are keeping the state in a file so we can resume the processing. 

# How to run

Create the virtual environment:

```
python -m venv venv
```

Activate the environment:

```
source .venv/bin/activate
```


Install requiered pyton modules (only once):

```
pip install -r requirements.txt
```

Execute:
```
./run.sh
```

If the application stops with the following mesage:
```
no valid state to resume from ...
You should cp state.bak to state and resume
```
just restore "state.bak" to "state" and continue running the application. 


The execution should finish when you see this:
```
No remaining placeholders.
Script completed.
```



# Problems to solve.

In triangl.py you have different triangles sets and the identified solution.