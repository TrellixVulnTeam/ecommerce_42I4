from orator.migrations import Migration


class CreateCartsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cart_item') as table:
            table.increments('id')
            table.big_integer('user_id')
            table.big_integer('product_id')
            table.big_integer('count')
            table.big_integer('timestamp_reserved')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cart_item')
