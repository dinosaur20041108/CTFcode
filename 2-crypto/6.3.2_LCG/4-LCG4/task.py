from Crypto.Util.number import *
flag = b'xxx'
plaintext = bytes_to_long(flag)
length = plaintext.bit_length()
a = getPrime(length)
b = getPrime(length)
m = getPrime(length)
seed = plaintext
for i in range(10):
    seed = (a*seed+b)%m
    print(seed)
'''
854956841214114093713236337419833848240770801311508883708
1253699879931788214300682725155523038214607460598303011525
2083248604522379582574920349615543135117428483131704868920
1776213990727241553631253904594305856469220241383067228692
331209347420302356981992570394902569686614999647991100629
2511329029888260873933175382533561389988084670063310635260
1796246721007430377340859639543404174227301706050675322593
674165277471819578369815642789469272418686437939088736188
2568331115671015663682740845102669199506810144342038125638
2483207742714099277802276533842642517666728517933619020765
'''