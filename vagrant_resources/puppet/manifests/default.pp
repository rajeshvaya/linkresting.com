# exec { "apt-get update":
#   path => "/usr/bin",
# }

# #Install apache2
# package { "apache2":
#   ensure  => present,
#   require => Exec["apt-get update"],
# }
# service { "apache2":
#   ensure  => "running",
#   require => Package["apache2"],
# }

# #Install vim
# package { 'vim':
#   ensure => present,
# }

# #Install git
# package { 'git':
#   ensure => present,
# }

# # Install mysql
# package { ['mysql-server']:
# 	ensure => present,
# 	require => Exec['apt-get update'],
# }
# service { 'mysql':
# 	ensure  => running,
# 	require => Package['mysql-server'],
# }

# # Install python-setuptools (for easy_install and pip)
# package { ['python-setuptools']:
# 	ensure => present,
# 	require => Exec['apt-get update'],
# }

# # Install pip
# exec { "easy_install pip":
#     path => "/usr/local/bin:/usr/bin:/bin",
# }

# #Install python virtualenvironment
# exec { "pip install virtualenv virtualenvwrapper":
#     path => "/usr/local/bin:/usr/bin:/bin",
# }