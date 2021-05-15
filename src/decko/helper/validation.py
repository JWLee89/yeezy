from typing import Callable, Any, Type
import inspect


def raise_error_if_not_callable(should_be_callable: Callable):
    if inspect.isclass(should_be_callable) \
            or not isinstance(should_be_callable, Callable):
        raise TypeError(f"Invalid type: {type(should_be_callable)}. "
                        "Please pass in a function. ")


def raise_error_if_not_class_instance(obj: Any):
    if not inspect.isclass(obj):
        raise TypeError("Target function decorates classes only. "
                        "Please pass in a class. "
                        f"Passed in type: {type(obj)}")


def is_class_instance(item) -> bool:
    """
    Check if item is a class instance.
    :param item: The item to evaluate
    """
    return inspect.isclass(item)


def is_iterable(obj) -> bool:
    iterable = True
    try:
        iter(obj)
    except TypeError:
        iterable = False
    return iterable


def validate_type(value: Any, target_type: Type):
    if type(value) != target_type:
        raise TypeError(f"{value} must be of type boolean. "
                        f"{value} is of type: {type(value)}")

