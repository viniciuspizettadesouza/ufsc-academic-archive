grammar cmm;

start : func* EOF
      ;

func : 'def' name=ID '(' args? ')'  statms
     ;

args : ID (',' ID)*
     ;

statms : '{' statm* '}'
       | statm
       ;

statm : ID '=' expr ';'                                       # assign
      | 'print' expr ';'                                      # print
      | 'if' cond=expr then=statms ('else' otherwise=statms)? # if
      | 'while' cond=expr statms                              # while
      | 'for' '(' cond=expr ';' cond=expr ';' expr ')' statms # for
      | 'switch' '(' atom ')' switchStatms+                   # switch
      | 'return' expr ';'                                     # return
      ;

switchStatms : '{' 'case' atom ':' switchStatms* '}'
             ;

call : name=ID '(' exprs? ')'
     ;

exprs : expr (',' expr)*
      ;

expr : left=summ (op=('>'|'<'|'<='|'>='|'<='|'=='|'!=') right=expr)*
     ;

summ : left=mult (op=('+'|'-') right=summ)*
     ;

mult : left=atom (op=('*'|'/') right=mult)*
     ;

atom : '(' expr ')'
     | INT
     | FLOAT
     | NULL
     | BOOLEAN
     | ID
     | 'input'
     | call
     ;

INPUT : 'input';
ELSE : 'else';
ID : [a-zA-Z]+[0-9a-zA-Z]*;
INT : [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
NULL: 'None';
BOOLEAN: 'True'|'False';
WS : [ \r\n\t]+ -> skip;