# Hospital_Module

Important to check this url http://localhost/web/database/manager

# Structure of the odoo.conf for Windows

    [options]
    ; This is the password that allows database operations:
    admin_passwd = admin
    db_host = localhost
    db_port = 5432
    db_user = odoo15
    db_password = admin123
    addons_path = C:\odoo15\odoo\addons,C:\odoo15\odoo\custom_addons
    
# To update the module when you restart pycharm
You have to add the follow command in the configuration settings on the parameters. This command is used to update form the terminal.
    -u om_hospital
