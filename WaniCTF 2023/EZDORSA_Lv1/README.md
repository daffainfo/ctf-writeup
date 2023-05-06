# EZDORSA_Lv1
> Hello there! Welcome to the world of RSA!

> In this world, there exists a crypto called RSA.

> Let's start with a simple calculation!

> p = 3

> q = 5

> n = p*q

> e = 65535

> c ≡ m^e (mod n) ≡ 10 (mod n)

> What is the smallest value of m that satisfies the above conditions?

> Please substitute the value of m into the "?" in FLAG{THE_ANSWER_IS_?}.

## About the Challenge
We need to find the smallest value of m

## How to Solve?
We are given the values of p, q, e, and c, and we need to find the smallest value of m that satisfies the given equation:

```
c ≡ m^e (mod n) ≡ 10 (mod n)
```

First, let's calculate the value of n:

```
n = pq = 35 = 15
```

Next, we need to find the value of d, which is the modular multiplicative inverse of e modulo (p-1)*(q-1). In other words, we need to find d such that:

```
ed ≡ 1 (mod (p-1)(q-1))
```

Using the extended Euclidean algorithm, we can find that d = 131071:

```
65535131071 ≡ 1 (mod 84) [since (p-1)(q-1) = (3-1)(5-1) = 8*4]
```

Now, we can use the formula for decrypting RSA ciphertext:

```
m ≡ c^d (mod n)
```

Substituting the given values, we get:

```
m ≡ 10^131071 (mod 15)
```

However, calculating 10^131071 directly would be very difficult. Fortunately, we can use the fact that:

```
10 ≡ -5 (mod 15)
```

So we can rewrite the original equation as:

```
c ≡ (-m)^e (mod n) ≡ -m^e (mod n) ≡ 10 (mod n)
```

Multiplying both sides by -1, we get:

```
m^e ≡ -10 (mod n)
```

Now we can substitute the value of e and n, and raise both sides to the power of d:

```
m ≡ (-10)^(1/d) (mod n)

m ≡ (-10)^131071 (mod 15)
```

Again, we can use the fact that:

```
-10 ≡ 5 (mod 15)
```

So we can simplify the equation as:

```
m ≡ 5^131071 (mod 15)
```

We can further simplify this by using the fact that:

```
5^2 ≡ 10 (mod 15)
```

So we can rewrite the equation as:

```
m ≡ (5^2)^65535 * 5 (mod 15)

m ≡ 10^65535 * 5 (mod 15)
```

Since 10 ≡ -5 (mod 15), we can simplify the equation as:

```
m ≡ (-5)^65535 * 5 (mod 15)

m ≡ -5 * 5 (mod 15)

m ≡ -25 (mod 15)

m ≡ 10 (mod 15)
```

Therefore, the smallest value of m that satisfies the given conditions is 10.
```
FLAG{THE_ANSWER_IS_10}
```