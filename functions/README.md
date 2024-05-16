# Building your own hooks!

### What are hooks?

Hooks are a way to dynamically use functions in the game server.
Basically, they provide you a way to add your own functions to the game server without changing the codebase.

### How to build hooks?

Hooks have a pretty strict structure. They must be a function that returns a function. The returned function must accept
a `hooks` parameter, which is an instance of `HookContext`.
The function can accept any number of arguments, but:

- first argument ALWAYS must be of type `HookContext`
- every hook must have `kwargs` to accept any number of additional arguments
- if game servers are run in strict mode, then every hook must have a schema, which is a dictionary with keys as
  argument names and values as types.
  This schema is used to validate the arguments passed to the hook.

Every hook module must have a `custom_hooks` variable, which is an instance of `HookHolder` (or any other class that
inherits from it. For more information, see `hook_holder.py` file in game server repository)
**Every** HookHolder instance is imported, so don't worry about naming of variables.

Eventually, packages will be added to `/installed/` directory, and their hooks will be imported and used in the game
server.
Take this into account when writing code.

### Example

```python
from engine.game_hooks import HookContext, HookHolder

custom_hooks = HookHolder(
    nickname="CUSTOM_HOOKS"
)


@custom_hooks.hook(
    name="my_hook_name",
    schema={
        "arg1": str,
        "arg2": int
    },
    schema_name="my_custom_schema"
)
def my_custom_hook(hooks: HookContext, arg1: str, arg2: int, **_):
    print("Hello from my custom hook! I got arguments:", arg1, arg2)
    pass

```

### Example (Breaking down)

- `from engine.game_hooks import HookContext, HookHolder` — imports necessary classes
- `custom_hooks = HookHolder(nickname="CUSTOM_HOOKS")` — creates a new instance of HookHolder. `nickname` is a namespace
  for hooks.
- `@custom_hooks.hook(...)` — this is a decorator that adds a function to the holder.
    - `name` is the name of the hook. Can differ from the function name. If not provided, function name will be used.
      Make sure there are no duplicates in one nickname namespace.
    - `schema` is a dictionary with keys as argument names and values as types. It is used to validate the arguments
      passed to the hook. If not provided, arguments will not be validated.
    - `schema_name` is the name of the schema. It is used to identify the schema when using. If not provided, function
      name will be used.
    - **WARNING** IF game servers are running in STRICT mode, then schema OR schema_name must be provided, otherwise the
      hook will not be used.
- `def my_custom_hook(hooks: HookContext, arg1: str, arg2: int, **_):` — this is the function that will be called when
  the hook is used.
    - `hooks` is an instance of `HookContext`. It is used to interact with the game server.
    - `arg1` and `arg2` are arguments passed to the hook. They are validated by the schema.
    - `**_` is a way to accept any number of additional arguments. They are not validated by the schema.
- `print("Hello from my custom hook! I got arguments:", arg1, arg2); pass` — this is the code that will be executed when
  the hook is used.
- `pass` — this is a placeholder. You can put any code here.

If everything went well, you can now use your hook in the game logic! Here is an example:

```python

...

hooks.use_hook("CUSTOM_HOOKS", "example:my_hook_name", arg1="Hello", arg2=42)

# "Hello from my custom hook! I got arguments: Hello 42" will be printed to the console
...

```