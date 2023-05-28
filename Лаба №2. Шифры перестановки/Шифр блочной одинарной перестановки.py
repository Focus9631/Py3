 def перестановки (строка, Шаг =  0): 
    если шаг == len ( строка): 
        # мы дошли до конца, выведите перестановку 
        print  "" .join ( string ) 
     for i in range ( step , len (string )): 
        # копировать строку (хранить как массив)
 string_copy =  [ c для c в  строке] 
         # поменять текущий индекс на шаг
 string_copy [ step ], string_copy [ i]  = string_copy [ i ], string_copy [step ] 
         # рекурсия на той части строки, которая еще не была заменена
 перестановки (string_copy, step +  1 ) 
print  (перестановки ('one'))
