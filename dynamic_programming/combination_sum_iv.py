"""
Soru:
Size farklı tamsayılardan oluşan bir dizi veriliyor ve bu diziden elemanları
seçmenin kaç farklı yolu olduğunu söylemeniz gerekiyor, öyle ki seçilen
elemanların toplamı hedef sayı tar'a eşit olmalıdır.

Örnek

Girdi:
N = 3
hedef = 5
dizi = [1, 2, 5]

Çıktı:
9

Yaklaşım:
Temel fikir, seçilen elemanların toplamının “tar” olacak şekilde yolu
bulmak için özyinelemeli olarak gitmektir. Her eleman için iki seçeneğimiz var:
    1. Elemanı seçilen elemanlar kümesine dahil et.
    2. Elemanı seçilen elemanlar kümesine dahil etme.
"""


def combination_sum_iv(nums: list[int], target: int) -> int:
    """
    Fonksiyon tüm olası kombinasyonları kontrol eder ve üstel Zaman
    Karmaşıklığında olası kombinasyonların sayısını döndürür.

    >>> combination_sum_iv([1,2,5], 5)
    9
    """

    def count_combinations(target: int) -> int:
        if target < 0:
            return 0
        if target == 0:
            return 1
        return sum(count_combinations(target - num) for num in nums)

    return count_combinations(target)


def combination_sum_iv_dp(nums: list[int], target: int) -> int:
    """
    Fonksiyon tüm olası kombinasyonları kontrol eder ve O(N^2) Zaman
    Karmaşıklığında olası kombinasyonların sayısını döndürür, çünkü burada
    Dinamik programlama dizisi kullanıyoruz.

    >>> combination_sum_iv_dp([1,2,5], 5)
    9
    """

    def count_combinations_dp(target: int, dp: list[int]) -> int:
        if target < 0:
            return 0
        if target == 0:
            return 1
        if dp[target] != -1:
            return dp[target]
        result = sum(
            count_combinations_dp(target - num, dp)
            for num in nums
        )
        dp[target] = result
        return result

    dp = [-1] * (target + 1)
    return count_combinations_dp(target, dp)

def combination_sum_iv_bottom_up(n: int, nums: list[int], target: int) -> int:
    """
    Fonksiyon tüm olası kombinasyonları kontrol eder ve O(N^2) Zaman
    Karmaşıklığında olası kombinasyonların sayısını döndürür, çünkü burada
    Dinamik programlama dizisi kullanıyoruz.

    >>> combination_sum_iv_bottom_up(3, [1,2,5], 5)
    9
    """

    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[target]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    hedef = 5
    dizi = [1, 2, 5]
    target = 5
    nums = [1, 2, 5]
    print(combination_sum_iv(nums, target))
