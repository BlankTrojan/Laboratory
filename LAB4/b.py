def product_of(m,n):
    if n==0:
        return 0
    else:
        return m+product_of(m,n-1)
print(product_of(54,45))
