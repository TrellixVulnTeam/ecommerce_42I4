from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('first_name')
            table.string('last_name')
            table.string('email')
            table.string('title')
            table.integer('gender')
            table.string('profile_pic')
            table.string('password')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
