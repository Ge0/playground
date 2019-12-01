# Compilation

## Set up

Get antlr4:

```
$ mkdir -p ~/bin && cd ~/bin
wget https://www.antlr.org/download/antlr-4.7.2-complete.jar
```

Update `CLASSPATH` and add aliases:

```
$ export CLASSPATH=".:/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.7.2-complete.jar'
$ alias grun='java org.antlr.v4.gui.TestRig'
```

(Better add those lines to some .*rc file!).
