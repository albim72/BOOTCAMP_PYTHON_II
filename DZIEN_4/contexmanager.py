class ContextManager:
    def __init__(self):
        print('funckja specjalna init uruchomiona...')

    def __enter__(self):
        print('funckja specjalna enter uruchomiona...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('funckja specjalna exit uruchomiona...')


with ContextManager() as manager:
    print("blok instrukcji with")
