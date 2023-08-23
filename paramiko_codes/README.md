# Things to Consider with Paramiko

Paramiko offers excellent flexibility and granularity in SSH and SFTP operations. However, it does require attention to certain low-level configurations and practices:

- **Set Missing Host Keys Policy**: Always ensure that you have a strategy for dealing with unknown host keys, whether that's accepting them all (`AutoAddPolicy()`) or a more conservative approach.

- **Append '\n' After Commands**: When sending commands, append a newline (`\n`) to ensure the command is executed properly in the shell.

- **Pause Execution After Commands**: Utilize `time.sleep()` to pause your script's execution, ensuring that previous commands have had adequate time to process before continuing.

- **Decode Bytes to Strings**: The output from Paramiko commands is often in byte format. Use the `.decode()` method to convert these to strings for printing or further processing.

- **Error Handling**: Always include appropriate error handling to catch and manage potential SSH connection issues or command execution problems.


- **Secure Authentication**: While Paramiko allows for password authentication, consider using key-based authentication for improved security.
  ```python
  private_key_path = "path_to_private_key.pem"
  mykey = paramiko.RSAKey(filename=private_key_path)
  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(hostname='your_host', username='your_username', pkey=mykey)
  ```

- **Logging**: Enable logging to capture details about SSH sessions and potential issues for troubleshooting.
