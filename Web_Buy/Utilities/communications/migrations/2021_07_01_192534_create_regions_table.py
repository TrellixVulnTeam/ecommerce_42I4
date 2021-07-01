from orator.migrations import Migration


class CreateRegionsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('regions') as table:
            table.increments('id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('regions')
