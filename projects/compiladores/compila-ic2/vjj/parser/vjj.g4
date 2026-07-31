grammar vjj;

start: func* EOF;

func: DEF name = ID '(' args? ')' statms;

args: ID (',' ID)*;

statms: '{' statm* '}' | statm;

statm:
	ID '=' expr ';'												# assign
	| PRINT expr ';'											# print
	| IF cond = expr then = statms (ELSE otherwise = statms)?	# if
	| WHILE cond = expr statms									# while
	| FOR '(' cond = expr ';' cond = expr ';' expr ')' statms	# for
	| SWITCH '(' atom ')' switchStatms+							# switch
	| CLASS classdef											# class
	| RETURN expr ';'											# return;

whileStatement: '{' statm* '}';

switchStatms: '{' CASE atom ':' switchStatms* '}';

types:
	TYPE_INT
	| TYPE_BOOLEAN
	| TYPE_FLOAT
	| TYPE_STRING
	| TYPE_NULL;

classdef: CLASS atom ('(' (args)? ')')? ':' statms;

call: name = ID '(' exprs? ')';

exprs: expr (',' expr)*;

expr:
	left = summ (
		op = ('>' | '<' | '<=' | '>=' | '==') right = expr
	)*;

summ: left = mult (op = ('+' | '-') right = summ)*;

mult: left = atom (op = ('*' | '/') right = mult)*;

atom:
	'(' expr ')'
	| INT
	| FLOAT
	| STRING
	| NULL
	| BOOLEAN
	| ID
	| INPUT
	| call;

TYPE_INT: 'int';
TYPE_FLOAT: 'float';
TYPE_BOOLEAN: 'bool';
TYPE_STRING: 'string';
TYPE_NULL: 'null';
DEF: 'def';
RETURN: 'return';
PRINT: 'print';
CASE: 'case';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
SWITCH: 'switch';
OR: 'or';
AND: 'and';
NOT: 'not';
CLASS: 'class';
INPUT: 'input';
ID: [a-zA-Z]+ [0-9a-zA-Z]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: [0-9a-zA-Z]+;
NULL: 'None';
BOOLEAN: 'True' | 'False';
WS: [ \r\n\t]+ -> skip;