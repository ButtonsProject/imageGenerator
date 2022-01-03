from PIL import Image
from backendImageGenerator.Worker import worker


class Postcard:

    result_post = Image.new('RGB', (1080, 1080), (255, 255, 255))

    def __init__(self, type_post, params=dict()):
        self.type_post = type_post
        self.params = params

    def create_result_post(self):
        self.result_post = worker.create_post(self.type_post, self.params)

    def save(self, path):
        self.result_post.save(path)


