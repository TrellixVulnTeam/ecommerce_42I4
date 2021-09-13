from orator.seeds import Seeder
from .MainAdmin import *
from .categories import *

class DatabaseSeeder(Seeder):

    def run(self):
        self.call(MainAdmin)
        self.call(Categories)


