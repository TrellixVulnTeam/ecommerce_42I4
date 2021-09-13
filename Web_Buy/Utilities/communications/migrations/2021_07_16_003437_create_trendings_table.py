from orator.migrations import Migration


class CreateTrendingsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('trendings') as table:
            table.increments('id')
            table.integer('product_id')
            table.integer("position")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('trendings')
