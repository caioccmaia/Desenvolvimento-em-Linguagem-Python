class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Mapear os símbolos para seus valores inteiros usando um dicionário
        romanos_para_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        
        # 2. Iterar sobre a string, exceto o último caractere
        for i in range(len(s) - 1):
            # 3. Lógica para a regra de subtração: se o valor atual for menor que o próximo
            if romanos_para_int[s[i]] < romanos_para_int[s[i+1]]:
                total -= romanos_para_int[s[i]]
            else:
                total += romanos_para_int[s[i]]

        # 4. Adicionar o valor do último caractere ao total
        # O último caractere sempre será somado, pois não há um próximo para comparar
        total += romanos_para_int[s[-1]]
        
        return total
