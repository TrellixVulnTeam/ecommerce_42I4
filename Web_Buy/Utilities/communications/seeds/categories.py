from orator.seeds import Seeder


class Categories(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('categories').insert({
            'name': 'Goods',
            'description': 'This category is concerned with the sale of tangible goods',
            })
        self.db.table('categories').insert({
            'name': 'Services',
            'description': 'This category is concerned with the rendering of services',
        })

        self.db.table('categories').insert({
            'name': 'Consultancy',
            'description': 'This category is concerned with the rendering of IT consulting services',
        })

