class Page_view:
    index = None
    offset = None
    limit =10
    query_limit = 10

    def __init__(self, index):
        self.index = index
        self.offset = (index-1)* 10
        self.limit = (index)* 10

    def __init__(self, index, limit):
        self.index = index
        self.limit = limit * index
        self.offset = (index - 1) * 10

    def get_index(self):
        return self.index

    def get_offset(self):
        return self.offset

    def get_limit(self):
        return self.limit

    def get_query_limit(self):
        return self.limit+1

    def get_data_limit(self):
        return self.limit -1
