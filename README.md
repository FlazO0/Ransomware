# Ransomware Simulado

### O que é Ransomware?

O Ransomware é um tipo de malware malicioso que criptografa os arquivos do sistema da vítima, tornando-os inacessíveis, e exige um resgate em troca da chave de descriptografia. É uma ameaça séria à segurança cibernética e pode causar grandes danos a indivíduos e organizações.

### Sobre este Projeto

Este projeto simula um Ransomware para fins educativos e demonstrativos. Não deve ser usado de forma maliciosa ou ilegal.

### Funcionamento

1. **Criptografia de Arquivos**:
   - Execute o Ransomware com o script `encrypt.py`.
   - Ele criptografa todos os arquivos no diretório `PC` usando a chave gerada anteriormente.
   - Os arquivos criptografados terão o prefixo "encrypted_" em seus nomes e os originais serão excluídos.

2. **Resgate**:
   - Após a criptografia, o Ransomware exibe uma mensagem de resgate no console, informando que os arquivos foram criptografados e exigindo um pagamento em troca da chave de descriptografia.
   - Esta mensagem é simulada e não há transação monetária real envolvida neste projeto.

3. **Descriptografia de Arquivos**:
   - Para descriptografar os arquivos, execute o script `decrypt.py`.
   - Ele descriptografa todos os arquivos no diretório `PC` que possuem o prefixo "encrypted_".
   - Os arquivos descriptografados não terão mais o prefixo e os arquivos criptografados serão excluídos.

### Uso

1. Certifique-se de ter o Python instalado em seu sistema.
2. Para criptografar os arquivos, execute `python encrypt.py`.
3. Após a criptografia, siga as instruções exibidas no console para a simulação do resgate.
4. Para descriptografar os arquivos, execute `python decrypt.py` após o pagamento simulado do resgate.


## Atenção

- Este projeto é apenas uma simulação educativa e não deve ser usado para fins maliciosos.
- Não envie dinheiro ou realize qualquer transação baseada nas mensagens simuladas deste projeto.
- Mantenha a chave de criptografia (`key.key`) segura e não a compartilhe com terceiros.

