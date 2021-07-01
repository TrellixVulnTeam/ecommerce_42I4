from orator.migrations import Migration


class CreateOrdersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('orders') as table:
            table.increments('id')
            table.big_integer('user_id')

            table.big_integer('timestamp_bought')
            table.big_integer('payment_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('orders')
