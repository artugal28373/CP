from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l, inverse

p = 159117138695601086935648462476725143896981591038416901486093706070754873563937272793294757366059667782136312013577603110660003394277897367203934519905683172161079448635248857040486200482627367334414675502994685936812333774063439076898281362682381888787053539531164627370506379676784327677612773681859553362469
a = 183170230465848410077175594145038110799
b = 177960951503783858139483105160729532851
c = 241771663291314104599898559749454094799
y = 81883801483428304918741984834363388238539421922474300691841915944763281416203781633389084991872486015041884084357260412052258732056118424392145242000539134316390251752292462492913837148154805999331901388735321855253311517735430229163344305926114721299791844599487270387540543138183327842649901510556454592197
c = (c - y + p) % p

# a*(x**2) + (b*x) + (c) = 0 (mod p)
# => x = (-b +- sqrt(s)) / (2 * a)
# => x = (-b +- r) / (2 * a)

s = b*b - 4*a*c
v = pow(2*s, (p-5)//8, p)
i = (2*s*v*v) % p
r = (s*v*(i-1)) % p

x = (-b + r) * inverse(2 * a, p)
x = (x % p + p) % p

print(l2b(x))