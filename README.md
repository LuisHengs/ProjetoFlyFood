# 🚀 Projeto FlyFood – Otimização de Rotas de Entrega com Drones  

Este é um projeto acadêmico desenvolvido no curso de **Bacharelado em Sistemas de Informação (UFRPE)**.  
O objetivo é resolver o clássico **Problema do Caixeiro Viajante (TSP)** aplicado à logística de entregas com drones 🛸.  

---

## 📌 Descrição do Projeto  

O **FlyFood** busca otimizar rotas de entrega considerando restrições como tempo de voo e autonomia de bateria dos drones.  
Para isso, foram implementados e comparados diferentes algoritmos de otimização:  

- 🔹 **Força Bruta** (método exato)  
- 🔹 **Algoritmo Genético** (meta-heurística inspirada na evolução biológica)  
- 🔹 **Algoritmo de Colônia de Formigas (ACO)** (meta-heurística bioinspirada)  

Cada algoritmo foi testado em diferentes cenários, avaliando **tempo de execução**, **eficiência** e **qualidade das rotas geradas**.  

---

## 🛠️ Tecnologias Utilizadas  

- **Python 3.x**  
- Bibliotecas:  
  - `random`  
  - `math`  
  - `heapq`  
  - `time`  
  - `statistics`  
  - (adicione outras se tiver usado)  

---

## 📂 Estrutura do Repositório  

📦 Projeto-FlyFood
┣ 📜 força_bruta.py # Implementação do algoritmo de Força Bruta
┣ 📜 genetico.py # Implementação do Algoritmo Genético
┣ 📜 colonia_formigas.py # Implementação do Algoritmo de Colônia de Formigas
┣ 📜 utils/ # Funções auxiliares
┣ 📜 README.md # Este arquivo
┗ 📜 relatorio.pdf # Relatório acadêmico do projeto


---

## ▶️ Como Executar  

Clone o repositório:  

```bash
git clone https://github.com/SEU-USUARIO/Projeto-FlyFood.git
cd Projeto-FlyFood

Execute cada algoritmo individualmente:
python força_bruta.py
python genetico.py
python colonia_formigas.py
```


📊 Resultados

Força Bruta → Garante a rota ótima, mas inviável para muitos pontos devido ao crescimento fatorial do tempo de execução.

Algoritmo Genético → Encontrou boas soluções em tempo reduzido, viável para instâncias médias.

Colônia de Formigas (ACO) → Excelente desempenho em instâncias maiores, convergindo para soluções próximas da ótima.

👨‍💻 Equipe

Gustavo de Melo Moreira

João Vitor Soares da Silva

Lucas Henrique Cavalcanti de Melo

Luís Henrique Gonçalves da Silva

Maycon Romario dos Santos Pereira

📖 Referências

Dorigo, M.; Stützle, T. Ant Colony Optimization

Goldberg, D. E. Genetic Algorithms in Search, Optimization and Machine Learning

Outros artigos citados no relatório
