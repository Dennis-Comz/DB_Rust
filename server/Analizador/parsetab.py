
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocIGUAL_IGUALNO_IGUALMENORMAYORMENOR_IGUALMAYOR_IGUALleftMASMENOSleftMULTIDIVMODULOrightNOTUNARIOABSOLUTO AND ARROW AS BOOL CADENA CARACTER CHAR COMA DECIMAL DIV DOS_PT ELSE ENTERO F64 FALSE GUION_B I64 ID IF IGUAL IGUAL_IGUAL LET LLAVA LLAVC MAS MATCH MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MENOS MODULO MULTI MUT NOT NO_IGUAL OR PARA PARC POW PRINTLN PT_COMA PUNTO RAIZ SEP_MATCH STR STRING TO_OWNED TO_STRING TRUE\n    inicio : instrucciones\n    \n    instrucciones : instrucciones instruccion\n    \n    instrucciones : instruccion\n    \n    instruccion : prints PT_COMA\n                | declaracion PT_COMA\n                | sent_if\n                | match\n                | expresion\n    \n    prints : PRINTLN NOT PARA CADENA COMA list_exp PARC\n    \n    prints : PRINTLN NOT PARA CADENA PARC\n    \n    list_exp : list_exp COMA expresion\n    \n    list_exp : expresion\n    \n    declaracion : LET MUT ID DOS_PT tipo IGUAL valores\n    \n    declaracion : LET MUT ID DOS_PT tipo\n    \n    declaracion : LET MUT ID IGUAL valores\n    \n    declaracion : LET MUT ID\n    \n    declaracion : LET ID DOS_PT tipo IGUAL valores\n    \n    declaracion : LET ID DOS_PT tipo\n    \n    declaracion : LET ID IGUAL valores\n    \n    declaracion : LET ID\n    \n    declaracion : ID IGUAL valores\n    \n    valores : expresion\n            | sent_if\n            | match\n    \n    sent_if : IF expresion statement sent_else\n    \n    sent_else : ELSE statement\n            | ELSE sent_if\n    \n    sent_else : \n    \n    match : MATCH expresion casos_match\n    \n    casos_match : LLAVA lista_casos default LLAVC\n    \n    lista_casos : lista_casos lista_expresiones ARROW statement COMA\n                | lista_casos lista_expresiones ARROW instruccion COMA\n    \n    lista_casos : lista_expresiones ARROW statement COMA\n                | lista_expresiones ARROW instruccion COMA\n    \n    lista_expresiones : lista_expresiones SEP_MATCH expresion\n    \n    lista_expresiones : expresion\n    \n    default : GUION_B ARROW statement COMA\n            | GUION_B ARROW instruccion COMA\n    \n    statement : LLAVA instrucciones LLAVC\n    \n    statement : LLAVA LLAVC\n    \n    tipo : I64\n        | F64\n        | BOOL\n        | STRING\n        | STR\n        | CHAR\n    \n    expresion : MENOS expresion %prec UNARIO\n            | expresion MAS expresion\n            | expresion MENOS expresion\n            | expresion MULTI expresion\n            | expresion DIV expresion\n            | expresion MODULO expresion\n    \n    expresion : I64 DOS_PT DOS_PT POW PARA expresion COMA expresion PARC\n    \n    expresion : PARA expresion PARC\n    \n    expresion : expresion IGUAL_IGUAL expresion\n            | expresion NO_IGUAL expresion\n            | expresion MAYOR expresion\n            | expresion MENOR expresion\n            | expresion MAYOR_IGUAL expresion\n            | expresion MENOR_IGUAL expresion\n    \n    expresion : expresion AND expresion\n            | expresion OR expresion\n    \n    expresion : NOT expresion %prec NOT\n    \n    expresion : ENTERO\n            | DECIMAL\n            | ID\n            | CADENA \n            | CARACTER\n            | TRUE\n            | FALSE\n    \n    expresion : expresion PUNTO TO_OWNED PARA PARC\n    \n    expresion : expresion PUNTO TO_STRING PARA PARC\n    \n    expresion : expresion PUNTO ABSOLUTO PARA PARC\n    \n    expresion : expresion PUNTO RAIZ PARA PARC\n    \n    expresion : expresion AS F64\n            | expresion AS I64\n    '
    
_lr_action_items = {'PRINTLN':([0,2,3,6,7,8,12,14,19,20,21,22,23,24,25,26,43,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,81,82,83,101,103,104,109,110,111,112,118,119,120,124,131,132,133,154,],[9,9,-3,-6,-7,-8,-67,-66,-64,-65,-68,-69,-70,-2,-4,-5,-63,-66,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,-28,9,-29,-25,9,-40,-71,-72,-73,-74,-26,-27,-39,9,-30,9,9,-53,]),'LET':([0,2,3,6,7,8,12,14,19,20,21,22,23,24,25,26,43,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,81,82,83,101,103,104,109,110,111,112,118,119,120,124,131,132,133,154,],[13,13,-3,-6,-7,-8,-67,-66,-64,-65,-68,-69,-70,-2,-4,-5,-63,-66,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,-28,13,-29,-25,13,-40,-71,-72,-73,-74,-26,-27,-39,13,-30,13,13,-53,]),'ID':([0,2,3,6,7,8,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,46,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,81,82,83,84,92,101,103,104,105,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[14,14,-3,-6,-7,-8,44,44,-67,47,-66,44,44,44,-64,-65,-68,-69,-70,-2,-4,-5,44,44,44,44,44,44,44,44,44,44,44,44,44,-63,-66,74,44,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,44,-28,14,-29,44,44,-25,14,-40,44,-71,-72,-73,-74,44,44,-26,-27,-39,14,44,44,44,-30,14,14,44,-33,-34,44,-31,-32,-53,]),'IF':([0,2,3,6,7,8,12,14,19,20,21,22,23,24,25,26,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,81,82,83,92,101,102,103,104,109,110,111,112,117,118,119,120,124,129,131,132,133,154,],[15,15,-3,-6,-7,-8,-67,-66,-64,-65,-68,-69,-70,-2,-4,-5,-63,-66,15,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,15,-28,15,-29,15,-25,15,15,-40,-71,-72,-73,-74,15,-26,-27,-39,15,15,-30,15,15,-53,]),'MATCH':([0,2,3,6,7,8,12,14,19,20,21,22,23,24,25,26,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,81,82,83,92,101,103,104,109,110,111,112,117,118,119,120,124,129,131,132,133,154,],[16,16,-3,-6,-7,-8,-67,-66,-64,-65,-68,-69,-70,-2,-4,-5,-63,-66,16,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,16,-28,16,-29,16,-25,16,-40,-71,-72,-73,-74,16,-26,-27,-39,16,16,-30,16,16,-53,]),'MENOS':([0,2,3,6,7,8,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,45,48,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,78,81,82,83,84,92,101,103,104,105,107,109,110,111,112,113,117,118,119,120,124,125,126,128,129,131,132,133,136,137,138,145,146,147,148,149,150,153,154,],[17,17,-3,-6,-7,28,17,17,-67,-66,17,17,17,-64,-65,-68,-69,-70,-2,-4,-5,17,17,17,17,17,17,17,17,17,17,17,17,17,-63,-66,28,17,28,28,-47,-48,-49,-50,-51,-52,28,28,28,28,28,28,28,28,-75,-76,-54,17,28,-28,17,-29,17,17,-25,17,-40,17,28,-71,-72,-73,-74,17,17,-26,-27,-39,17,17,17,28,17,-30,17,17,28,28,17,-33,-34,17,28,-31,-32,28,-53,]),'I64':([0,2,3,6,7,8,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,75,76,81,82,83,84,91,92,101,103,104,105,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[18,18,-3,-6,-7,-8,18,18,-67,-66,18,18,18,-64,-65,-68,-69,-70,-2,-4,-5,18,18,18,18,18,18,18,18,18,18,18,18,18,71,-63,-66,18,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,94,18,-28,18,-29,18,94,18,-25,18,-40,18,-71,-72,-73,-74,18,18,-26,-27,-39,18,18,18,18,-30,18,18,18,-33,-34,18,-31,-32,-53,]),'PARA':([0,2,3,6,7,8,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,76,81,82,83,84,92,101,103,104,105,108,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[11,11,-3,-6,-7,-8,11,11,-67,-66,11,11,11,-64,-65,-68,-69,-70,-2,-4,-5,11,11,11,11,11,11,11,11,11,11,11,11,11,72,-63,-66,11,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,86,87,88,89,-75,-76,-54,11,-28,11,-29,11,11,-25,11,-40,11,126,-71,-72,-73,-74,11,11,-26,-27,-39,11,11,11,11,-30,11,11,11,-33,-34,11,-31,-32,-53,]),'NOT':([0,2,3,6,7,8,9,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,81,82,83,84,92,101,103,104,105,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[10,10,-3,-6,-7,-8,42,10,10,-67,-66,10,10,10,-64,-65,-68,-69,-70,-2,-4,-5,10,10,10,10,10,10,10,10,10,10,10,10,10,-63,-66,10,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,10,-28,10,-29,10,10,-25,10,-40,10,-71,-72,-73,-74,10,10,-26,-27,-39,10,10,10,10,-30,10,10,10,-33,-34,10,-31,-32,-53,]),'ENTERO':([0,2,3,6,7,8,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,81,82,83,84,92,101,103,104,105,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[19,19,-3,-6,-7,-8,19,19,-67,-66,19,19,19,-64,-65,-68,-69,-70,-2,-4,-5,19,19,19,19,19,19,19,19,19,19,19,19,19,-63,-66,19,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,19,-28,19,-29,19,19,-25,19,-40,19,-71,-72,-73,-74,19,19,-26,-27,-39,19,19,19,19,-30,19,19,19,-33,-34,19,-31,-32,-53,]),'DECIMAL':([0,2,3,6,7,8,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,81,82,83,84,92,101,103,104,105,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[20,20,-3,-6,-7,-8,20,20,-67,-66,20,20,20,-64,-65,-68,-69,-70,-2,-4,-5,20,20,20,20,20,20,20,20,20,20,20,20,20,-63,-66,20,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,20,-28,20,-29,20,20,-25,20,-40,20,-71,-72,-73,-74,20,20,-26,-27,-39,20,20,20,20,-30,20,20,20,-33,-34,20,-31,-32,-53,]),'CADENA':([0,2,3,6,7,8,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,72,73,76,81,82,83,84,92,101,103,104,105,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[12,12,-3,-6,-7,-8,12,12,-67,-66,12,12,12,-64,-65,-68,-69,-70,-2,-4,-5,12,12,12,12,12,12,12,12,12,12,12,12,12,-63,-66,12,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,90,-54,12,-28,12,-29,12,12,-25,12,-40,12,-71,-72,-73,-74,12,12,-26,-27,-39,12,12,12,12,-30,12,12,12,-33,-34,12,-31,-32,-53,]),'CARACTER':([0,2,3,6,7,8,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,81,82,83,84,92,101,103,104,105,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[21,21,-3,-6,-7,-8,21,21,-67,-66,21,21,21,-64,-65,-68,-69,-70,-2,-4,-5,21,21,21,21,21,21,21,21,21,21,21,21,21,-63,-66,21,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,21,-28,21,-29,21,21,-25,21,-40,21,-71,-72,-73,-74,21,21,-26,-27,-39,21,21,21,21,-30,21,21,21,-33,-34,21,-31,-32,-53,]),'TRUE':([0,2,3,6,7,8,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,81,82,83,84,92,101,103,104,105,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[22,22,-3,-6,-7,-8,22,22,-67,-66,22,22,22,-64,-65,-68,-69,-70,-2,-4,-5,22,22,22,22,22,22,22,22,22,22,22,22,22,-63,-66,22,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,22,-28,22,-29,22,22,-25,22,-40,22,-71,-72,-73,-74,22,22,-26,-27,-39,22,22,22,22,-30,22,22,22,-33,-34,22,-31,-32,-53,]),'FALSE':([0,2,3,6,7,8,10,11,12,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,43,44,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,76,81,82,83,84,92,101,103,104,105,109,110,111,112,113,117,118,119,120,124,125,126,129,131,132,133,138,145,146,147,149,150,154,],[23,23,-3,-6,-7,-8,23,23,-67,-66,23,23,23,-64,-65,-68,-69,-70,-2,-4,-5,23,23,23,23,23,23,23,23,23,23,23,23,23,-63,-66,23,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,23,-28,23,-29,23,23,-25,23,-40,23,-71,-72,-73,-74,23,23,-26,-27,-39,23,23,23,23,-30,23,23,23,-33,-34,23,-31,-32,-53,]),'$end':([1,2,3,6,7,8,12,14,19,20,21,22,23,24,25,26,43,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,81,83,101,104,109,110,111,112,118,119,120,131,154,],[0,-1,-3,-6,-7,-8,-67,-66,-64,-65,-68,-69,-70,-2,-4,-5,-63,-66,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,-28,-29,-25,-40,-71,-72,-73,-74,-26,-27,-39,-30,-53,]),'LLAVC':([3,6,7,8,12,14,19,20,21,22,23,24,25,26,43,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,81,82,83,101,103,104,109,110,111,112,118,119,120,121,131,151,152,154,],[-3,-6,-7,-8,-67,-66,-64,-65,-68,-69,-70,-2,-4,-5,-63,-66,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,-28,104,-29,-25,120,-40,-71,-72,-73,-74,-26,-27,-39,131,-30,-37,-38,-53,]),'PT_COMA':([4,5,12,19,20,21,22,23,43,44,47,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,74,77,78,79,80,81,83,93,94,95,96,97,98,99,100,101,104,109,110,111,112,114,115,116,118,119,120,130,131,139,140,154,],[25,26,-67,-64,-65,-68,-69,-70,-63,-66,-20,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,-16,-21,-22,-23,-24,-28,-29,-18,-41,-42,-43,-44,-45,-46,-19,-25,-40,-71,-72,-73,-74,-10,-14,-15,-26,-27,-39,-17,-30,-9,-13,-53,]),'COMA':([6,7,8,12,14,19,20,21,22,23,25,26,43,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,81,83,90,101,104,109,110,111,112,118,119,120,127,128,131,134,135,137,141,142,143,144,148,154,],[-6,-7,-8,-67,-66,-64,-65,-68,-69,-70,-4,-5,-63,-66,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,-28,-29,113,-25,-40,-71,-72,-73,-74,-26,-27,-39,138,-12,-30,145,146,147,149,150,151,152,-11,-53,]),'MAS':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[27,-67,-66,-64,-65,-68,-69,-70,-63,-66,27,27,27,-47,-48,-49,-50,-51,-52,27,27,27,27,27,27,27,27,-75,-76,-54,27,27,-71,-72,-73,-74,27,27,27,27,27,-53,]),'MULTI':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[29,-67,-66,-64,-65,-68,-69,-70,-63,-66,29,29,29,-47,29,29,-50,-51,-52,29,29,29,29,29,29,29,29,-75,-76,-54,29,29,-71,-72,-73,-74,29,29,29,29,29,-53,]),'DIV':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[30,-67,-66,-64,-65,-68,-69,-70,-63,-66,30,30,30,-47,30,30,-50,-51,-52,30,30,30,30,30,30,30,30,-75,-76,-54,30,30,-71,-72,-73,-74,30,30,30,30,30,-53,]),'MODULO':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[31,-67,-66,-64,-65,-68,-69,-70,-63,-66,31,31,31,-47,31,31,-50,-51,-52,31,31,31,31,31,31,31,31,-75,-76,-54,31,31,-71,-72,-73,-74,31,31,31,31,31,-53,]),'IGUAL_IGUAL':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[32,-67,-66,-64,-65,-68,-69,-70,-63,-66,32,32,32,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,32,32,-75,-76,-54,32,32,-71,-72,-73,-74,32,32,32,32,32,-53,]),'NO_IGUAL':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[33,-67,-66,-64,-65,-68,-69,-70,-63,-66,33,33,33,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,33,33,-75,-76,-54,33,33,-71,-72,-73,-74,33,33,33,33,33,-53,]),'MAYOR':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[34,-67,-66,-64,-65,-68,-69,-70,-63,-66,34,34,34,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,34,34,-75,-76,-54,34,34,-71,-72,-73,-74,34,34,34,34,34,-53,]),'MENOR':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[35,-67,-66,-64,-65,-68,-69,-70,-63,-66,35,35,35,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,35,35,-75,-76,-54,35,35,-71,-72,-73,-74,35,35,35,35,35,-53,]),'MAYOR_IGUAL':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[36,-67,-66,-64,-65,-68,-69,-70,-63,-66,36,36,36,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,36,36,-75,-76,-54,36,36,-71,-72,-73,-74,36,36,36,36,36,-53,]),'MENOR_IGUAL':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[37,-67,-66,-64,-65,-68,-69,-70,-63,-66,37,37,37,-47,-48,-49,-50,-51,-52,None,None,None,None,None,None,37,37,-75,-76,-54,37,37,-71,-72,-73,-74,37,37,37,37,37,-53,]),'AND':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[38,-67,-66,-64,-65,-68,-69,-70,-63,-66,38,38,38,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,38,-75,-76,-54,38,38,-71,-72,-73,-74,38,38,38,38,38,-53,]),'OR':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[39,-67,-66,-64,-65,-68,-69,-70,-63,-66,39,39,39,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,39,39,-71,-72,-73,-74,39,39,39,39,39,-53,]),'PUNTO':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[40,-67,-66,-64,-65,-68,-69,-70,-63,-66,40,40,40,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,40,40,-71,-72,-73,-74,40,40,40,40,40,-53,]),'AS':([8,12,14,19,20,21,22,23,43,44,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,78,107,109,110,111,112,128,136,137,148,153,154,],[41,-67,-66,-64,-65,-68,-69,-70,-63,-66,41,41,41,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,41,41,-71,-72,-73,-74,41,41,41,41,41,-53,]),'PARC':([12,19,20,21,22,23,43,44,45,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,86,87,88,89,90,109,110,111,112,127,128,148,153,154,],[-67,-64,-65,-68,-69,-70,-63,-66,73,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,109,110,111,112,114,-71,-72,-73,-74,139,-12,-11,154,-53,]),'LLAVA':([12,19,20,21,22,23,43,44,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,102,109,110,111,112,124,132,133,154,],[-67,-64,-65,-68,-69,-70,-63,-66,82,84,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,82,-71,-72,-73,-74,82,82,82,-53,]),'ARROW':([12,19,20,21,22,23,43,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,106,107,109,110,111,112,122,123,136,154,],[-67,-64,-65,-68,-69,-70,-63,-66,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,124,-36,-71,-72,-73,-74,132,133,-35,-53,]),'SEP_MATCH':([12,19,20,21,22,23,43,44,51,53,54,55,56,57,58,59,60,61,62,63,64,65,70,71,73,106,107,109,110,111,112,122,136,154,],[-67,-64,-65,-68,-69,-70,-63,-66,-47,-48,-49,-50,-51,-52,-55,-56,-57,-58,-59,-60,-61,-62,-75,-76,-54,125,-36,-71,-72,-73,-74,125,-35,-53,]),'MUT':([13,],[46,]),'IGUAL':([14,47,74,93,94,95,96,97,98,99,115,],[48,76,92,117,-41,-42,-43,-44,-45,-46,129,]),'DOS_PT':([18,47,52,74,],[52,75,85,91,]),'TO_OWNED':([40,],[66,]),'TO_STRING':([40,],[67,]),'ABSOLUTO':([40,],[68,]),'RAIZ':([40,],[69,]),'F64':([41,75,91,],[70,95,95,]),'BOOL':([75,91,],[96,96,]),'STRING':([75,91,],[97,97,]),'STR':([75,91,],[98,98,]),'CHAR':([75,91,],[99,99,]),'ELSE':([81,104,120,],[102,-40,-39,]),'POW':([85,],[108,]),'GUION_B':([105,145,146,149,150,],[123,-33,-34,-31,-32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instrucciones':([0,82,],[2,103,]),'instruccion':([0,2,82,103,124,132,133,],[3,24,3,24,135,142,144,]),'prints':([0,2,82,103,124,132,133,],[4,4,4,4,4,4,4,]),'declaracion':([0,2,82,103,124,132,133,],[5,5,5,5,5,5,5,]),'sent_if':([0,2,48,76,82,92,102,103,117,124,129,132,133,],[6,6,79,79,6,79,119,6,79,6,79,6,6,]),'match':([0,2,48,76,82,92,103,117,124,129,132,133,],[7,7,80,80,7,80,7,80,7,80,7,7,]),'expresion':([0,2,10,11,15,16,17,27,28,29,30,31,32,33,34,35,36,37,38,39,48,76,82,84,92,103,105,113,117,124,125,126,129,132,133,138,147,],[8,8,43,45,49,50,51,53,54,55,56,57,58,59,60,61,62,63,64,65,78,78,8,107,78,8,107,128,78,8,136,137,78,8,8,148,153,]),'valores':([48,76,92,117,129,],[77,100,116,130,140,]),'statement':([49,102,124,132,133,],[81,118,134,141,143,]),'casos_match':([50,],[83,]),'tipo':([75,91,],[93,115,]),'sent_else':([81,],[101,]),'lista_casos':([84,],[105,]),'lista_expresiones':([84,105,],[106,122,]),'default':([105,],[121,]),'list_exp':([113,],[127,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instrucciones','inicio',1,'p_inicio','parser.py',99),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_lista_instrucciones','parser.py',105),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','parser.py',112),
  ('instruccion -> prints PT_COMA','instruccion',2,'p_instruccion','parser.py',118),
  ('instruccion -> declaracion PT_COMA','instruccion',2,'p_instruccion','parser.py',119),
  ('instruccion -> sent_if','instruccion',1,'p_instruccion','parser.py',120),
  ('instruccion -> match','instruccion',1,'p_instruccion','parser.py',121),
  ('instruccion -> expresion','instruccion',1,'p_instruccion','parser.py',122),
  ('prints -> PRINTLN NOT PARA CADENA COMA list_exp PARC','prints',7,'p_instruccion_println','parser.py',129),
  ('prints -> PRINTLN NOT PARA CADENA PARC','prints',5,'p_instruccion_println_cads','parser.py',135),
  ('list_exp -> list_exp COMA expresion','list_exp',3,'p_println_listexp','parser.py',141),
  ('list_exp -> expresion','list_exp',1,'p_println_listexp_exit','parser.py',148),
  ('declaracion -> LET MUT ID DOS_PT tipo IGUAL valores','declaracion',7,'p_instruccion_declaracion','parser.py',157),
  ('declaracion -> LET MUT ID DOS_PT tipo','declaracion',5,'p_declaracion_2','parser.py',170),
  ('declaracion -> LET MUT ID IGUAL valores','declaracion',5,'p_declaracion_3','parser.py',183),
  ('declaracion -> LET MUT ID','declaracion',3,'p_declaracion_4','parser.py',196),
  ('declaracion -> LET ID DOS_PT tipo IGUAL valores','declaracion',6,'p_declaracion_5','parser.py',209),
  ('declaracion -> LET ID DOS_PT tipo','declaracion',4,'p_declaracion_6','parser.py',222),
  ('declaracion -> LET ID IGUAL valores','declaracion',4,'p_declaracion_7','parser.py',235),
  ('declaracion -> LET ID','declaracion',2,'p_declaracion_8','parser.py',248),
  ('declaracion -> ID IGUAL valores','declaracion',3,'p__declaracion_asignacion','parser.py',261),
  ('valores -> expresion','valores',1,'p_declaracion_valores','parser.py',274),
  ('valores -> sent_if','valores',1,'p_declaracion_valores','parser.py',275),
  ('valores -> match','valores',1,'p_declaracion_valores','parser.py',276),
  ('sent_if -> IF expresion statement sent_else','sent_if',4,'p_instruccion_sent_if','parser.py',284),
  ('sent_else -> ELSE statement','sent_else',2,'p_sent_else','parser.py',290),
  ('sent_else -> ELSE sent_if','sent_else',2,'p_sent_else','parser.py',291),
  ('sent_else -> <empty>','sent_else',0,'p_sent_else_vacio','parser.py',297),
  ('match -> MATCH expresion casos_match','match',3,'p_instruccion_match','parser.py',306),
  ('casos_match -> LLAVA lista_casos default LLAVC','casos_match',4,'p_match_casos','parser.py',312),
  ('lista_casos -> lista_casos lista_expresiones ARROW statement COMA','lista_casos',5,'p_match_lista_casos','parser.py',319),
  ('lista_casos -> lista_casos lista_expresiones ARROW instruccion COMA','lista_casos',5,'p_match_lista_casos','parser.py',320),
  ('lista_casos -> lista_expresiones ARROW statement COMA','lista_casos',4,'p_match_lista_casos_salida','parser.py',327),
  ('lista_casos -> lista_expresiones ARROW instruccion COMA','lista_casos',4,'p_match_lista_casos_salida','parser.py',328),
  ('lista_expresiones -> lista_expresiones SEP_MATCH expresion','lista_expresiones',3,'p_match_lista_expresiones','parser.py',334),
  ('lista_expresiones -> expresion','lista_expresiones',1,'p_match_lista_expresiones2','parser.py',341),
  ('default -> GUION_B ARROW statement COMA','default',4,'p_match_default','parser.py',347),
  ('default -> GUION_B ARROW instruccion COMA','default',4,'p_match_default','parser.py',348),
  ('statement -> LLAVA instrucciones LLAVC','statement',3,'p_statement','parser.py',357),
  ('statement -> LLAVA LLAVC','statement',2,'p_statement_vacio','parser.py',363),
  ('tipo -> I64','tipo',1,'p_tipo','parser.py',371),
  ('tipo -> F64','tipo',1,'p_tipo','parser.py',372),
  ('tipo -> BOOL','tipo',1,'p_tipo','parser.py',373),
  ('tipo -> STRING','tipo',1,'p_tipo','parser.py',374),
  ('tipo -> STR','tipo',1,'p_tipo','parser.py',375),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',376),
  ('expresion -> MENOS expresion','expresion',2,'p_exp_aritmeticas','parser.py',394),
  ('expresion -> expresion MAS expresion','expresion',3,'p_exp_aritmeticas','parser.py',395),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_exp_aritmeticas','parser.py',396),
  ('expresion -> expresion MULTI expresion','expresion',3,'p_exp_aritmeticas','parser.py',397),
  ('expresion -> expresion DIV expresion','expresion',3,'p_exp_aritmeticas','parser.py',398),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_exp_aritmeticas','parser.py',399),
  ('expresion -> I64 DOS_PT DOS_PT POW PARA expresion COMA expresion PARC','expresion',9,'p_exp_potencia','parser.py',408),
  ('expresion -> PARA expresion PARC','expresion',3,'p_exp_parentesis','parser.py',414),
  ('expresion -> expresion IGUAL_IGUAL expresion','expresion',3,'p_exp_relacionales','parser.py',423),
  ('expresion -> expresion NO_IGUAL expresion','expresion',3,'p_exp_relacionales','parser.py',424),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_exp_relacionales','parser.py',425),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_exp_relacionales','parser.py',426),
  ('expresion -> expresion MAYOR_IGUAL expresion','expresion',3,'p_exp_relacionales','parser.py',427),
  ('expresion -> expresion MENOR_IGUAL expresion','expresion',3,'p_exp_relacionales','parser.py',428),
  ('expresion -> expresion AND expresion','expresion',3,'p_exp_logicas','parser.py',436),
  ('expresion -> expresion OR expresion','expresion',3,'p_exp_logicas','parser.py',437),
  ('expresion -> NOT expresion','expresion',2,'p_exp_not','parser.py',443),
  ('expresion -> ENTERO','expresion',1,'p_exp_primtivos','parser.py',452),
  ('expresion -> DECIMAL','expresion',1,'p_exp_primtivos','parser.py',453),
  ('expresion -> ID','expresion',1,'p_exp_primtivos','parser.py',454),
  ('expresion -> CADENA','expresion',1,'p_exp_primtivos','parser.py',455),
  ('expresion -> CARACTER','expresion',1,'p_exp_primtivos','parser.py',456),
  ('expresion -> TRUE','expresion',1,'p_exp_primtivos','parser.py',457),
  ('expresion -> FALSE','expresion',1,'p_exp_primtivos','parser.py',458),
  ('expresion -> expresion PUNTO TO_OWNED PARA PARC','expresion',5,'p_exp_cadena_toowned','parser.py',477),
  ('expresion -> expresion PUNTO TO_STRING PARA PARC','expresion',5,'p_exp_cadena_tostring','parser.py',483),
  ('expresion -> expresion PUNTO ABSOLUTO PARA PARC','expresion',5,'p_exp_absoluto','parser.py',489),
  ('expresion -> expresion PUNTO RAIZ PARA PARC','expresion',5,'p_exp_raiz','parser.py',495),
  ('expresion -> expresion AS F64','expresion',3,'p_exp_casteo','parser.py',501),
  ('expresion -> expresion AS I64','expresion',3,'p_exp_casteo','parser.py',502),
]
