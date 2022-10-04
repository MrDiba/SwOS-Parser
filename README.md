# SwOS-Parser
Parser for parsing Mikrotik SwitchOS files to JSON

## Usage
1. Clone this repository
2. Get a copy of your Mikrotik SwitchOS configuration. This can be done using the following methods.
  - 1. Go to the webinterface on the switch.
    2. Go to the `System` tab.
    3. Click on `Save Backup`.
    4. Save the file on your system.

  - On the commandline enter the following command to download the backup file: `wget --user admin --password <your_password> http://<your_sw_ip>/backup.swb`.

  - Using Ansible you could do the following:
  ```
  - name: "Get backup"
    ansible.builtin.get_url:
      url: http://<your_sw_ip>/backup.swb
      url_username: admin
      url_password: <your_password>
      validate_certs: False
      dest: <your_backup_destination>
  ```

3. Run the command using: `python3 parse.py backup.swb`
4. This will generate a file called `backup.swb.json` where your backup in JSON will be stored.
5. Have fun doing the other stuff you can do with JSON.

If you see anything that can be improved or if something is not working, please open a issue.
