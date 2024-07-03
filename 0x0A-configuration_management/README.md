# Puppet Configuration Management Tasks

This repository contains Puppet manifests to accomplish various configuration management tasks. Each task is described in detail below.

## Tasks

### 0. Create a File
Using Puppet, create a file in `/tmp`.

**Requirements:**
- File path: `/tmp/school`
- File permission: `0744`
- File owner: `www-data`
- File group: `www-data`
- File content: `I love Puppet`

**Example:**
```shell
root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.5.2
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppet
root@6712bef7a528:~#
```

**Manifest:**
```puppet
# 0-create_a_file.pp
file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
```

**Repo:**
- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x0A-configuration_management`
- **File:** `0-create_a_file.pp`

### 1. Install a Package
Using Puppet, install `flask` from `pip3`.

**Requirements:**
- Install `flask`
- Version: `2.1.0`

**Example:**
```shell
root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
```

**Manifest:**
```puppet
# 1-install_a_package.pp
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
```

**Repo:**
- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x0A-configuration_management`
- **File:** `1-install_a_package.pp`

### 2. Execute a Command
Using Puppet, create a manifest that kills a process named `killmenow`.

**Requirements:**
- Must use the `exec` Puppet resource
- Must use `pkill`

**Example:**
```shell
# Terminal #0 - starting my process
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow

# Terminal #1 - executing my manifest
root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/# 

# Terminal #0 - process has been terminated
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
```

**Manifest:**
```puppet
# 2-execute_a_command.pp
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
```

**Repo:**
- **GitHub repository:** `alx-system_engineering-devops`
- **Directory:** `0x0A-configuration_management`
- **File:** `2-execute_a_command.pp`

## How to Use

1. **Clone the repository:**
   ```shell
   git clone https://github.com/your_username/alx-system_engineering-devops.git
   ```

2. **Navigate to the project directory:**
   ```shell
   cd alx-system_engineering-devops/0x0A-configuration_management
   ```

3. **Run the manifests:**
   ```shell
   puppet apply <manifest_file>.pp
   ```

4. **Check the results as shown in the examples above.**

## Author
- **Mohammad Omar Siddiq**
```

This `README.md` file provides clear instructions for each task, including the requirements, examples, and the corresponding Puppet manifests. Feel free to customize it further based on your project structure and specific needs.
