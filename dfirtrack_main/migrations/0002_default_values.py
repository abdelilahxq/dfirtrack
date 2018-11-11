# Generated by Django 2.0.2 on 2018-03-20 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dfirtrack_main', '0001_initial'),
    ]

    operations = [

        migrations.RunSQL("INSERT INTO dfirtrack_main_analysisstatus (analysisstatus_name) VALUES ('Needs analysis');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_analysisstatus (analysisstatus_name) VALUES ('Ready for analysis');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_analysisstatus (analysisstatus_name) VALUES ('Ongoing analysis');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_analysisstatus (analysisstatus_name) VALUES ('Nothing to do');"),

        migrations.RunSQL("INSERT INTO dfirtrack_main_headline (headline_name) VALUES ('Summary');"),

        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows Server 2003');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows Server 2003 R2');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows Server 2008');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows Server 2008 R2');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows Server 2012');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows Server 2012 R2');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows Server 2016');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows XP');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows Vista');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows 7');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows 8');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows 8.1');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('Windows 10');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_os (os_name) VALUES ('tbd');"),

        migrations.RunSQL("INSERT INTO dfirtrack_main_osarch (osarch_name) VALUES ('32-Bit');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_osarch (osarch_name) VALUES ('64-Bit');"),

        migrations.RunSQL("INSERT INTO dfirtrack_main_systemstatus (systemstatus_name) VALUES ('Clean');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemstatus (systemstatus_name) VALUES ('Unknown');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemstatus (systemstatus_name) VALUES ('Analysis ongoing');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemstatus (systemstatus_name) VALUES ('Compromised');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemstatus (systemstatus_name) VALUES ('Remediation done');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemstatus (systemstatus_name) VALUES ('Reinstalled');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemstatus (systemstatus_name) VALUES ('Removed');"),

        migrations.RunSQL("INSERT INTO dfirtrack_main_systemtype (systemtype_name) VALUES ('Domaincontroller');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemtype (systemtype_name) VALUES ('Mailserver');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemtype (systemtype_name) VALUES ('Fileserver');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemtype (systemtype_name) VALUES ('USB-Drive');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_systemtype (systemtype_name) VALUES ('Client');"),

        migrations.RunSQL("INSERT INTO dfirtrack_main_tagcolor (tagcolor_name) VALUES ('primary');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_tagcolor (tagcolor_name) VALUES ('green');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_tagcolor (tagcolor_name) VALUES ('orange');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_tagcolor (tagcolor_name) VALUES ('red');"),

        migrations.RunSQL("INSERT INTO dfirtrack_main_taskpriority (taskpriority_name) VALUES ('Low');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_taskpriority (taskpriority_name) VALUES ('Medium');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_taskpriority (taskpriority_name) VALUES ('High');"),

        migrations.RunSQL("INSERT INTO dfirtrack_main_taskstatus (taskstatus_name) VALUES ('Pending');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_taskstatus (taskstatus_name) VALUES ('Working');"),
        migrations.RunSQL("INSERT INTO dfirtrack_main_taskstatus (taskstatus_name) VALUES ('Done');"),

    ]
