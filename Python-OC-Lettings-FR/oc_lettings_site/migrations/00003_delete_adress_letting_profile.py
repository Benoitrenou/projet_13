from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_remove_letting_address_remove_profile_user'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                   name='Address',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='Address',
                    table='lettings_address',
                ),
            ],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                   name='Letting',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='Letting',
                    table='lettings_letting',
                ),
            ],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                   name='Profile',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='Profile',
                    table='profiles_profile',
                ),
            ],
        ),
    ]