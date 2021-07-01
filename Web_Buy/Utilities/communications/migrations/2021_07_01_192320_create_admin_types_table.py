from orator.migrations import Migration


class CreateAdminTypesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('admin_types') as table:
            table.increments('id')
            table.string('name')
            table.string('description')
            table.string('level')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('admin_types')
