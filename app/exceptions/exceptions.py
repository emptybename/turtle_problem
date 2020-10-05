class InvalidInput(Exception):
    def __init__(self, *args, **kwargs):
        super(InvalidInput, self).__init__(*args, **kwargs)
