grammar Lex;
/*
 * Parser Rules
 */

start: code? EOF;
code: statement+;

statement: ((mainStatement NEWLINE) | mainStatementNoNewLine)+;

mainStatement
	: variableDeclaration 
    | variableInitialization
    ;

mainStatementNoNewLine
	: methodDeclaration
	| forDeclaration
	| ifDeclaration
	;

methodDeclaration : methodHeader methodBody;
methodHeader : 'def ' methodName '(' methodHeaderVariables '):' NEWLINE;
methodHeaderVariables: ((methodHeaderVariable ', ')* methodHeaderVariable)? ;
methodHeaderVariable: variableName ': ' variableType;
methodBody : (((' '|'\t')+ methodStatement NEWLINE) | ((' '|'\t')+ methodStatementNoNewLine))+ ;
methodStatement
	: variableDeclaration
    | variableInitialization
	| methodCall
	;

methodStatementNoNewLine
	: forDeclaration
	| ifDeclaration
	;

methodName : VariableName;

methodCall : methodName '(' methodHeaderVariables ')';

forDeclaration: forHead forBody;
forHead: (' '|'\t')* 'for ' VariableName ' in range(' IntegerLiteral '):'NEWLINE; 
forBody: (((' '|'\t')+ forStatement NEWLINE) | (' '|'\t')+ forStatementNoNewLine)+;
forStatement
	: variableDeclaration
    | variableInitialization
	| methodCall
	;

forStatementNoNewLine
	: forDeclaration
	| ifDeclaration
	;

ifDeclaration: ifHead ifBody;
ifHead: (' '|'\t')* 'if ' condition ' '* ':' NEWLINE;
ifBody: truePart (' '|'\t')* ('else:' NEWLINE elsePart)?;
truePart: (((' '|'\t')+ ifStatement NEWLINE) | (' '|'\t')+ ifStatementNoNewLine)+;
elsePart: (((' '|'\t')+ ifStatement NEWLINE) | (' '|'\t')+ ifStatementNoNewLine)+;
ifStatement
	: variableDeclaration
    | variableInitialization
	| methodCall
	;

ifStatementNoNewLine
	: forDeclaration
	| ifDeclaration
	;

variableDeclaration: variableName ': '  variableType ( ' = '  variableValue)? ;
variableType : 'int' | 'str' | 'float';
variableName : VariableName ;
variableValue
	: FloatLiteral        #pFloatLiteral
	| IntegerLiteral	#pIntegerLiteral
	| StringLiteral		#pStringLiteral
    | mathOperation     #pMathOperation
	;

variableInitialization: variableName  ' = '  variableValue ;

condition: argument ' '* ('<=' | '<' | '==' | '!=' | '>' | '>=') ' '* argument;

mathOperation: binaryMathOperation | unaryMathOperation ;
binaryMathOperation: argument ' '* ('+' | '-' | '/' | '*') ' '* argument ;
unaryMathOperation: ;

argument: VariableName | IntegerLiteral ;

VariableName : [a-zA-Z][a-zA-Z0-9]* ;
FloatLiteral : [0-9]+'.'[0-9]* ;
IntegerLiteral : [0-9]+ ;
StringLiteral : '"' .*? '"';

WORD                : [a-zA-Z]+ ;
WHITESPACE          : (' '|'\t'){1,} -> skip;
NEWLINE             : ('\r'? '\n' | '\r')+ ;

/*methodDeclaration : methodHeader methodBody;
methodHeader : 'def' methodName '(' ')';
methodBody : '{' statement* '}';
statement : embeddedStatement ';';
embeddedStatement
	: localVariableDeclaration
	| methodCall	
	;

methodName : WORD;

localVariableDeclaration : variableType variableName ('=' variableValue)? ;
methodCall : methodName '(' ')';
*/

/*
//chat                : line line EOF ;
line                : name 'says' opinion NEWLINE;
name                : WORD ;
opinion             : TEXT ;

WORD                : [a-zA-Z]+ ;
TEXT                : '"' .*? '"' ;
WHITESPACE          : (' '|'\t')+ -> skip ;
NEWLINE             : ('\r'? '\n' | '\r')+ ;
*/
