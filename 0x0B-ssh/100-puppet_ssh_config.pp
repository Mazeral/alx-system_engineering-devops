# Connect to a server without typing a password

file_line { 'ssh_indentify_file':
  path => '~/.ssh/school',
  line => 'IdentityFile ~/.ssh/school',
  match   => '^#?\s*IdentityFile\s+~/.ssh/school$',
}
