
class ctx:
    storage = None

    def __init__(self, storage):
        ctx.storage = storage

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass


def get_ctx_storage():
    return ctx.storage

