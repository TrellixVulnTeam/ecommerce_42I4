from orator.migrations import Migration


class CreateOrderItemsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('order_items') as table:
            table.increments('id')
            table.big_integer('product_id')
            table.big_integer('count')
            table.big_integer('order_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('order_items')
