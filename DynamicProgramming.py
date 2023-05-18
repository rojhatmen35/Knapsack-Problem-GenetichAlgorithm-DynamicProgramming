import matplotlib.pyplot as plt

def knapsack(maxWeight, weights, values, n):
    # Tablo oluşturma
    table = [[0] * (maxWeight + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, maxWeight + 1):
            if weights[i - 1] <= w:
                table[i][w] = max(values[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]
    
    # Seçilen elemanların bulunması
    selected = [0] * (n + 1)
    i, w = n, maxWeight
    while i > 0 and w > 0:
        if table[i][w] != table[i - 1][w]:
            selected[i] = 1
            w -= weights[i - 1]
        i -= 1
    
    # Sonuç dizisi oluşturma
    result = [0] * (n + 1)
    result[0] = table[n][maxWeight]
    for i in range(1, n + 1):
        result[i] = selected[i]
    
    return result


def main():
    try:
        # Dosya okuma işlemi
        with open("ks_19_0.txt", "r") as file:
            lines = file.readlines()
            
            # İlk satırdaki değerlerin okunması
            itemNumber, maxWeight = map(int, lines[0].split())
            
            # Değer dizilerinin oluşturulması
            values = []
            weights = []
            
            # Diğer satırlardaki değerlerin okunması
            for line in lines[1:]:
                value, weight = map(int, line.split())
                values.append(value)
                weights.append(weight)
            
            # Knapsack algoritmasının çağrılması
            result = knapsack(maxWeight, weights, values, itemNumber)
            
            # Sonuçların ekrana yazdırılması
            print(result[0])
            for i in range(1, itemNumber + 1):
                print(result[i], end=" ")
    
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
