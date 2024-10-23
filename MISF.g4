grammar MISF;

// The starting point for parsing
program: statement* ;

// statements definition
statement
    : assignmentStatement
    | printStatement
    | ifStatement
    | whileStatement
    | functionDeclaration
    | functionCall
    ;

// Assignment statement: variable = expression;
assignmentStatement
    : ID '=' expression ';'
    ;

// Print statement: print(expression);
printStatement
    : 'print' '(' expression ')' ';'
    ;

// If statement: if (condition) { statement }
ifStatement
    : 'if' '(' expression ')' '{' statement* '}'
    ;

// While statement: while (condition) { statement }
whileStatement
    : 'while' '(' expression ')' '{' statement* '}'
    ;

// Function declaration: function functionName() { statement }
functionDeclaration
    : 'function' ID '(' ')' '{' statement* '}'
    ;

// Function call: functionName();
functionCall
    : ID '(' ')' ';'
    ;

// Expression: can be a number, variable, or binary operation
expression
    : expression ('+' | '-' | '*' | '/') expression     # binaryOperation
    | INT                                               # intLiteral
    | STRING                                            # stringLiteral
    | ID                                                # variable
    | '(' expression ')'                                # parenthesizedExpression
    ;

// Lexer rules
ID    : [a-zA-Z_][a-zA-Z0-9_]*; // Identifiers
INT   : [0-9]+;                  // Integer literals
STRING: '"' (~["] | '""')* '"';  // String literals (double quotes)
WS    : [ \t\n\r]+ -> skip;      // Whitespace (skip)