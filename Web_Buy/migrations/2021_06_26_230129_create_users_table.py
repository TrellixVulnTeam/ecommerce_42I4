from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('name')
            table.string('surname')
            table.string('email')
            table.string('password')
            table.string('contacts')
            table.string('address')
            table.medium_integer('age')
            table.string("token")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
