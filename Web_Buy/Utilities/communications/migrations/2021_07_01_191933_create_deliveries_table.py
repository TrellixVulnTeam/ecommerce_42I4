from orator.migrations import Migration


class CreateDeliveriesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('deliveries') as table:
            table.increments('id')
            table.big_integer('address_id')
            table.big_integer('order_id')
            table.big_integer('estimate_date_of_delivery')
            table.big_integer('state_id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('deliveries')
