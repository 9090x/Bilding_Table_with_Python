#СВЯТstyle
from prettytable import PrettyTable as ПретиТэйбл

принт = print

тэбл = ПретиТэйбл()
тэбл.field_names = ["№", "нэйм", "кост", "валуе", "прайс"]

принт(тэбл)
