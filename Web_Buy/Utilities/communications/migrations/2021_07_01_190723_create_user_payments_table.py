from orator.migrations import Migration


class CreateUserPaymentsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('user_payments') as table:
            table.increments('id')
            table.big_integer('user_id')
            table.double('amount')
            table.big_integer('payment_method_id')
            table.big_integer('timestamp_paid')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('user_payments')
