import Tools_fileProcessing

l = Tools_fileProcessing.get_csv_file_row_number('digits.csv')
print l
print range(1,5)
#lst = range(1, l+1)
Tools_fileProcessing.add_column_to_csv('digits.csv', 'index', lst)



