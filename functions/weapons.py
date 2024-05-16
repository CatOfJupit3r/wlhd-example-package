from engine.game_hooks import HookContext, WeaponHooks

custom_hooks = WeaponHooks()

@custom_hooks.hook(
    name="my_hook_name",
    schema={
        "arg1": str,
        "arg2": int
    },
    schema_name="my_custom_schema"
)
def my_custom_hook(hooks: HookContext, arg1: str, arg2: int, **_):
    pass
