IP=$1
PORT=$2
nmap_path=
LOGFILE=$IP_nmap_ftp_scan.log
nmap --script ftp-vuln-cve2010-4221 -p 21 $IP
nmap --script ftp-anon.nse -p 21 $IP
nmap --script ftp-bounce.nse -p 21 $IP
nmap --script ftp-brute.nse -p 21 $IP
nmap --script ftp-libopie -p 21 $IP
nmap --script ftp-brute -p 21 $IP
nmap --script ftp-vsftpd-backdoor -p 21 $IP
