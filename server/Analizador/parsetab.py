
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftDIVMULTIMODULOrightPOTENCIArightUNARIODECIMAL DIV ENTERO MAS MENOS MODULO MULTI PARA PARC POTENCIA PT_COMA\n    inicio : expresion\n    \n    expresion : expresion MAS expresion\n           | expresion MENOS expresion\n           | expresion MULTI expresion\n           | expresion DIV expresion\n           | expresion MODULO expresion\n           | expresion POTENCIA expresion\n    \n    expresion : PARA expresion PARC\n    \n    expresion : MENOS expresion %prec UNARIO\n    \n    expresion :  ENTERO\n              | DECIMAL\n    '
    
_lr_action_items = {'PARA':([0,3,4,7,8,9,10,11,12,],[4,4,4,4,4,4,4,4,4,]),'MENOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[3,8,3,3,-10,-11,3,3,3,3,3,3,-9,8,-2,-3,-4,-5,-6,-7,-8,]),'ENTERO':([0,3,4,7,8,9,10,11,12,],[5,5,5,5,5,5,5,5,5,]),'DECIMAL':([0,3,4,7,8,9,10,11,12,],[6,6,6,6,6,6,6,6,6,]),'$end':([1,2,5,6,13,15,16,17,18,19,20,21,],[0,-1,-10,-11,-9,-2,-3,-4,-5,-6,-7,-8,]),'MAS':([2,5,6,13,14,15,16,17,18,19,20,21,],[7,-10,-11,-9,7,-2,-3,-4,-5,-6,-7,-8,]),'MULTI':([2,5,6,13,14,15,16,17,18,19,20,21,],[9,-10,-11,-9,9,9,9,-4,-5,-6,-7,-8,]),'DIV':([2,5,6,13,14,15,16,17,18,19,20,21,],[10,-10,-11,-9,10,10,10,-4,-5,-6,-7,-8,]),'MODULO':([2,5,6,13,14,15,16,17,18,19,20,21,],[11,-10,-11,-9,11,11,11,-4,-5,-6,-7,-8,]),'POTENCIA':([2,5,6,13,14,15,16,17,18,19,20,21,],[12,-10,-11,-9,12,12,12,12,12,12,12,-8,]),'PARC':([5,6,13,14,15,16,17,18,19,20,21,],[-10,-11,-9,21,-2,-3,-4,-5,-6,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'expresion':([0,3,4,7,8,9,10,11,12,],[2,13,14,15,16,17,18,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> expresion','inicio',1,'p_inicio','parser.py',29),
  ('expresion -> expresion MAS expresion','expresion',3,'p_exp_aritmeticas','parser.py',35),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_exp_aritmeticas','parser.py',36),
  ('expresion -> expresion MULTI expresion','expresion',3,'p_exp_aritmeticas','parser.py',37),
  ('expresion -> expresion DIV expresion','expresion',3,'p_exp_aritmeticas','parser.py',38),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_exp_aritmeticas','parser.py',39),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_exp_aritmeticas','parser.py',40),
  ('expresion -> PARA expresion PARC','expresion',3,'p_exp_parentesis','parser.py',46),
  ('expresion -> MENOS expresion','expresion',2,'p_exp_unario','parser.py',53),
  ('expresion -> ENTERO','expresion',1,'p_exp_numero','parser.py',60),
  ('expresion -> DECIMAL','expresion',1,'p_exp_numero','parser.py',61),
]