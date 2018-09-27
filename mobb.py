#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Ano.Mobb
#Mobb Hash Cracker
# Donate: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn
# -*- coding: utf-8

import requests, sys, re


print ("""
RedHat

                          _____                          
                   _.+sd$$$$$$$$$bs+._                   
               .+d$$$$$$$$$$$$$$$$$$$$$b+.               
            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.            
          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.          
        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.        
       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s       
     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.     
    .$$$$$$$$$$$$P                       T$$$$$$$$$$.    
   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.   
  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;  
  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$  
 :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$; 
 $$$$$$$P         `*T$$$$$b              '      `T$$$$$$ 
:$$$$$$$b            `*T$$$s                      :$$$$$;
:$$$$$$$$b.                                        $$$$$;
$$$$$$$$$$$b.                                     :$$$$$$
$$$$$$$$$$$$$bs.                                 .$$$$$$$
$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
 $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
 :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$; 
  $$$b       `T$b+                        :$$$$$$$BUG$$  
  :$P'         `"'               ,._.     ;$$$$$$$$$$$;  
   \     [Author: Ano.Mobb]     `*TP*     d$$P*******$   
    \  (Mobb  Hash  Cracker)             :$$P'      /    
     \                                  :dP'       /     
      `.                               d$P       .'      
        `.                             `'      .'        
          `-.                               .-'          
             `-.                         .-'             
                `*+-._             _.-+*'                
                      `"*-------*"'

# Donate: 1GmQaG9R5NPs3ZzR6XPMD9jZk17F9MuoWn
""")












url = 'http://hashtoolkit.com/reverse-hash?hash='
try:
    hasH = sys.argv[1]
except:
    print ("usage: python "+sys.argv[0]+" hash")
    sys.exit()


http = requests.get(url+hasH)
content = http.content
cracked = re.findall("<span title=\"decrypted (md5|sha1|sha256|sha384|sha512) hash\">(.*)</span>", content) # expression redular
print ("\n\Algoritem: "+cracked[0][0])
print ("\tPassword Cracked: "+cracked[0][1])
                     
