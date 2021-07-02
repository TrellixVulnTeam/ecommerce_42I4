from orator.seeds import Seeder
from .MainAdmin import *

class DatabaseSeeder(Seeder):

    def run(self):
        self.call(MainAdmin)


