# Connect to a server without typing a password

file_line { 'ssh_indentify_file':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  match   => '^#?\s*IdentityFile\s+~/.ssh/school$',
}
