# Generated manually for entry_status choices: draft, confirmed, billable

from django.db import migrations, models


def backfill_default_to_draft(apps, schema_editor):
    """Update any existing entry_status='default' to 'draft' before applying choices."""
    TimeEntry = apps.get_model("calendar", "TimeEntry")
    TimeEntry.objects.filter(entry_status="default").update(entry_status="draft")


class Migration(migrations.Migration):

    dependencies = [
        ("calendar", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(backfill_default_to_draft, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="timeentry",
            name="entry_status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("confirmed", "Confirmed"), ("billable", "Billable")],
                db_index=True,
                default="draft",
                max_length=50,
            ),
        ),
    ]
