# Using puppet to install flask package

package { 'flask':
  ensure   =>  '2.1.0',
  provider =>  pip3,
}
