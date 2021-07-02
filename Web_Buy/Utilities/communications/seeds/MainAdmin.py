from orator.seeds import Seeder


class MainAdmin(Seeder):

    def run(self):
        """
        Run the database seeds.

        """
        self.db.table('admins').insert({
            'first_name': 'Phindiwe',
            'last_name': 'Masemola',
            'email': 'phindy.j.ndaba@gmail.com',
            'title': 'mrs',
            'gender': 'F',
            'profile_pic': 'e96aba02-9b65-4573-bb2e-8201838b4d46.jpg',
            'password': 'adminpass12343',
            'region_id': 1
        })


