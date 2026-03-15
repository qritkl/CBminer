# CBminer
minerador de arquivos do catbox para Termux

## requisitos
Termux com wget e python instalado

## comando
```
python CBminer.py
```

## funcionamento
-modo finito: testa uma quantidade finita de dúzia de vezes
-modo infinito: testa indefinidamente dúzias de tentativas
-as opções listadas por padrão são simplesmente os arquivos mais comuns.

### por que dúzias?
Eu programei e testei originalmente em um emulador android com termux pois o wget requeria configurações mais específicas e que as vezes nem funcionava no windows. As dúzias é porque se trata de um processador de 12 threads e usei o módulo threading para testar várias vezes (12) ao mesmo tempo. Se sinta livre para 
modificar o código e adapta-lo ao seu dispositivo.

## como usar?
apenas responda as opções para escolher o modo de funcionamento e veja funcionando.

--made by qritkl, programador iniciante--