class debugger:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_debugger_"):
            cls._debugger = super(debugger, cls).__new__(cls, * args, ** kwargs)
        return cls._debugger
