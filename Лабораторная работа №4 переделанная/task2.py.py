count_char_diсt = {}
def get_count_char(str_):
     for sumbol_ in str_.lower():
         if sumbol_.isalpha() and sumbol_ not in count_char_diсt:
             count_char_diсt[sumbol_] = 1
         else:
             if sumbol_.isalpha() and sumbol_ in count_char_diсt:
                 count_char_diсt[sumbol_] += 1
     return count_char_diсt

def percent_diсt(count_char_diсt_):
    sum_ = sum(count_char_diсt_.values())
    for i in count_char_diсt:
        count_char_diсt[i] = round((count_char_diсt_[i]/sum_) * 100, 3)
    print(sum(count_char_diсt.values()))
    return count_char_diсt
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))