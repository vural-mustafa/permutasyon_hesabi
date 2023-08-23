class PermutationCalculator:
    def __init__(self, n, r):
        self.n = n
        self.r = r

    def factorial(self, num):
        if num == 0 or num == 1:
            return 1
        return num * self.factorial(num - 1)

    def calculate_permutation(self):
        if self.n >= self.r:
            permutation = self.factorial(self.n) / self.factorial(self.n - self.r)
            return permutation
        else:
            return "n, r'den büyük veya eşit olmalıdır."

# Kullanıcıdan n ve r değerlerini alalım
n = int(input("n değerini girin: "))
r = int(input("r değerini girin: "))

# PermutationCalculator sınıfından bir nesne oluşturalım
calculator = PermutationCalculator(n, r)

# Permütasyonu hesaplayalım
result = calculator.calculate_permutation()

# Sonucu yazdıralım
print(f"P({n},{r}) = {result}")
