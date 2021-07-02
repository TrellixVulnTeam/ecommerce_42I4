from orator.migrations import Migration


class CreateDashboardsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('dashboards') as table:
            table.increments('id')
            table.string('name')
            table.string('description')
            table.string('url')
            table.integer('default')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('dashboards')
