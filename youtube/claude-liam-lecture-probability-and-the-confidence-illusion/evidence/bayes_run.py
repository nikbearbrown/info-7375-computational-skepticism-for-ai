from fractions import Fraction as F
prior, sens, fpr = F(1,10000), F(99,100), F(1,100)
num = prior*sens
den = num + (1-prior)*fpr
post = num/den
print(">>> prior, sens, fpr = 1/10000, 0.99, 0.01")
print(">>> num = prior * sens")
print(f"{float(num):.6f}")
print(">>> den = num + (1 - prior) * fpr")
print(f"{float(den):.6f}")
print(">>> num / den")
print(f"{float(post):.4f}   # exactly {post}")
print(">>> 1 / (1 + 0.01 * 9999)    # the head count")
print(f"{1/(1+0.01*9999):.4f}")
