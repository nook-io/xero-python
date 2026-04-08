import functools
from types import MappingProxyType


def single_dispatch_str(func=None, key=None):
    if func is None:
        return lambda f: single_dispatch_str(f, key)
    registry = {}
    func_name = getattr(func, "__name__", "single_dispatch_str function")

    def default_get_key(*args, **kwargs):
        if not args:
            raise TypeError(f"{func_name} requires at least 1 positional argument")
        key = args[0]
        if not isinstance(key, str):
            raise TypeError(f"{func_name} requires first positional argument to be string type")
        return key

    get_key = key or default_get_key

    def dispatch(key):
        try:
            impl = registry[key]
        except KeyError:
            impl = registry[""]
        return impl

    def register(key, func=None):
        if not isinstance(key, str):
            raise TypeError(f"{func_name} requires string type key for register")
        if not key:
            raise ValueError(f"{func_name} requires non empty string type key for register")
        if func is None:
            return lambda f: register(key, f)
        registry[key] = func
        return func

    def wrapper(*args, **kw):
        key = get_key(*args, **kw)
        if not isinstance(key, str):
            raise TypeError(f"{func_name} requires key value to be string type")
        return dispatch(key)(*args, **kw)

    registry[""] = func
    wrapper.register = register
    wrapper.dispatch = dispatch
    wrapper.registry = MappingProxyType(registry)
    functools.update_wrapper(wrapper, func)
    return wrapper
