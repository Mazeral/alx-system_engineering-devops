Here's a `README.md` file explaining each of the tasks:

```markdown
# 0x0B. SSH

## Table of Contents

- [Tasks](#tasks)
  - [0. Use a private key](#0-use-a-private-key)
  - [1. Create an SSH key pair](#1-create-an-ssh-key-pair)
  - [2. Client configuration file](#2-client-configuration-file)
  - [3. Let me in!](#3-let-me-in)
  - [4. Client configuration file (w/ Puppet)](#4-client-configuration-file-w-puppet)

## Tasks

### 0. Use a private key

Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

**Requirements:**

- Only use `ssh` single-character flags.
- You cannot use `-l`.
- You do not need to handle the case of a private key protected by a passphrase.

```bash
#!/usr/bin/env bash
ssh -i ~/.ssh/school ubuntu@server01
```

**Example:**
```shell
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0B-ssh`
- File: `0-use_a_private_key`

### 1. Create an SSH key pair

Write a Bash script that creates an RSA key pair.

**Requirements:**

- Name of the created private key must be `school`.
- Number of bits in the created key to be created: `4096`.
- The created key must be protected by the passphrase `betty`.

```bash
#!/usr/bin/env bash
ssh-keygen -t rsa -b 4096 -f school -N "betty"
```

**Example:**
```shell
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
sylvain@ubuntu$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0B-ssh`
- File: `1-create_ssh_key_pair`

### 2. Client configuration file

Configure your SSH client configuration file so that you can connect to a server without typing a password.

**Requirements:**

- Your SSH client configuration must be configured to use the private key `~/.ssh/school`.
- Your SSH client configuration must be configured to refuse to authenticate using a password.

**Example Configuration:**

Create or modify the SSH config file `~/.ssh/config`:
```text
Host server01
  HostName 98.98.98.98
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
```

**Example:**
```shell
sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
...
Authenticated to 98.98.98.98 ([98.98.98.98]:22).
...
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0B-ssh`
- File: `2-ssh_config`

### 3. Let me in!

Add the SSH public key below to your server so that we can connect using the `ubuntu` user.

**SSH Public Key:**
```text
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```

**Steps:**

1. Open the file `~/.ssh/authorized_keys` on your server.
2. Append the public key to the file.

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0B-ssh`

### 4. Client configuration file (w/ Puppet)

Use Puppet to make changes to your SSH client configuration file.

**Requirements:**

- Your SSH client configuration must be configured to use the private key `~/.ssh/school`.
- Your SSH client configuration must be configured to refuse to authenticate using a password.

**Example Puppet Manifest:**
```puppet
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => template('ssh/ssh_config.erb'),
}

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
}
```

**Example:**
```shell
vagrant@ubuntu:~$ sudo puppet apply 100-puppet_ssh_config.pp
Notice: Compiled catalog for ubuntu-xenial in environment production in 0.11 seconds
Notice: /Stage[main]/Main/File_line[Turn off passwd auth]/ensure: created
Notice: /Stage[main]/Main/File_line[Declare identity file]/ensure: created
Notice: Finished catalog run in 0.03 seconds
vagrant@ubuntu:~$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0B-ssh`
- File: `100-puppet_ssh_config.pp`
```

This `README.md` covers the instructions and requirements for each task clearly and concisely. Feel free to add more details if necessary!
