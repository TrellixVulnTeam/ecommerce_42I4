from orator.migrations import Migration


class CreateUserAddressesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('user_addresses') as table:
            table.increments('id')
            table.string('province')
            table.string('city')
            table.string('surban')
            table.string('street_name')
            table.string('house_number')
            table.big_integer('user_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('user_addresses')
