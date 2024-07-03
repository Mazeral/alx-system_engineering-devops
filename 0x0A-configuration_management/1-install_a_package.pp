#!/usr/bin/pup
# installs flask

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
