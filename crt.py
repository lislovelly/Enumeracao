import requests
from bs4 import BeautifulSoup

def buscar_certificados(dominio):
    url = f"https://crt.sh/?q={dominio}"

    # Envia uma solicitação GET para o site do crt.sh
    response = requests.get(url)
    
    if response.status_code == 200:
        # Analisando o HTML retornado
        soup = BeautifulSoup(response.content, 'html.parser')

        # Buscando todas as entradas de certificados
        tabela_certificados = soup.find_all('tr')
        
        # Verificando se a tabela foi encontrada
        if tabela_certificados:
            print(f"Certificados encontrados para {dominio}:\n")
            for linha in tabela_certificados[1:]:  # Ignora o cabeçalho
                colunas = linha.find_all('td')
                if len(colunas) > 3:
                    cert = {
                        'Data': colunas[0].text.strip(),
                        'Certificado': colunas[3].text.strip()
                    }
                    print(f"Data: {cert['Data']} - Certificado: {cert['Certificado']}")
        else:
            print(f"Nenhum certificado encontrado para o domínio: {dominio}")
    else:
        print("Erro ao acessar o site crt.sh")

# Exemplo de uso
if __name__ == "__main__":
    dominio = input("Digite o domínio para buscar certificados: ").strip()
    buscar_certificados(dominio)
