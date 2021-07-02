from orator.migrations import Migration


class CreateCategoriesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('categories') as table:
            table.increments('id')
            table.string('name')
            table.string('description')
            table.big_integer('parent_id').nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('categories')
