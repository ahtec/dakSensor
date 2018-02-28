cd /var/www/html
####cd /home/centos/testdir
####for entry in `ls /home/centos/testdir/*bar.html| xargs -n1 basename`;
for entry in `ls /var/www/html/*bar.html  | xargs -n1 basename`;
do
echo "<a href='$entry '> $entry </a>";
done

