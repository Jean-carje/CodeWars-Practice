# Kata link:
# https://www.codewars.com/kata/514a024011ea4fb54200004b/

# -------------------------------------
# Instructions:
'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

    domain_name("http://github.com/carbonfive/raygun") == "github" 
    domain_name("http://www.zombie-bites.com") == "zombie-bites"
    domain_name("https://www.cnet.com") == "cnet"
'''

# -------------------------------------
import re 

# Solution 1:
def domain_name(url):
    string = re.sub(r"^(.+://|w+\.)","", url)
    if 'www.' in string: 
        return domain_name(string)
    string = re.sub(r"(\..+)$", "", string)
    return string

# Solution 2:
# def domain_name(url):
#     url = url.replace('www.', "")
#     return url[url.find("//") + 2:url.find(".")]


# -------------------------------------
# Basic Tests
print(domain_name("http://google.com"), " ## google")
print(domain_name("http://google.co.jp"), " ## google")
print(domain_name("http://www.Codewars.com"), " ## Codewars")
print(domain_name("www.xakep.ru"), " ## xakep")
print(domain_name("https://youtube.com"), " ## youtube")