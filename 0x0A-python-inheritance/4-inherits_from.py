def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    """
    # Check if obj is an instance of a subclass of a_class
    return issubclass(type(obj), a_class) and type(obj) != a_class

