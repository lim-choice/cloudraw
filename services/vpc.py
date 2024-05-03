from services import NcloudService


class NcloudVPC(NcloudService):
    def __init__(self):
        pass
    
    def add_arguments(self):
        return super().add_arguments()
    
    @staticmethod
    def dynamic_loading():
        print("import success")