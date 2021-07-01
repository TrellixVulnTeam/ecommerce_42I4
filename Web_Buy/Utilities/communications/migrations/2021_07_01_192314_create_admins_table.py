from orator.migrations import Migration


class CreateAdminsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('admins') as table:
            table.increments('id')
            table.string('first_name')
            table.string('last_name')
            table.string('title')
            table.integer('gender')
            table.string('profile_pic')
            table.string('password')
            table.big_integer('region_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('admins')
