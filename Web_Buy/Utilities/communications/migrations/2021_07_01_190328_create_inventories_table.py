from orator.migrations import Migration


class CreateInventoriesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('inventories') as table:
            table.increments('id')
            table.big_integer('product_id')
            table.big_integer('open')
            table.big_integer('reserved')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('inventories')
