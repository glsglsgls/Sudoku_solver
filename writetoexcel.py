def writehtml(arr):
    f=open('visual.html', 'w')
    f.write('<!DOCTYPE html>' + '\n')
    f.write('<html>' + '\n')
    f.write(' <head>' + '\n')
    f.write('  <meta charset="utf-8">' + '\n')
    f.write('  <title>Тег table</title>' + '\n')
    f.write('  <style>' + '\n')
    f.write('   table {' + '\n')
    f.write('   border-spacing: 1px;' + '\n')
    f.write('   text-align: center;')
    f.write('   }')

    f.write('   td, th {' + '\n')
    f.write('   text-align: center;')
    f.write('   padding-right: 8px;}' + '\n')
    f.write('   padding: 5px;' + '\n')
    f.write('   }')

    f.write('   th.even {' + '\n')
    f.write('   border="5";')
    f.write('   }')

    f.write('  </style>' + '\n')
    
    f.write(' </head>' + '\n')
    f.write(' <body>' + '\n')
    f.write('  <table border="1">' + '\n')
    
    for i in range(9):
        f.write('   <tr>' + '\n')
        for j in range(9):
            if j==3: f.write('    <th class="even">' + str(arr[i,j]) + '</th>' + '\n')
            else: f.write('    <th>' + str(arr[i,j]) + '</th>' + '\n')
        f.write('   </tr>' + '\n')
    f.write('  </table>' + '\n')
    f.write(' </body>' + '\n')
    f.write('</html>' + '\n')
    f.close