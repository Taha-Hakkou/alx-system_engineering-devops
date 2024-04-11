# fixes a broken wordpress CMS
exec { 'rename_file':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => 'shell'
}
