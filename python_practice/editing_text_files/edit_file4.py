output_str  = ""
output_str += "Esta es una prueba\n"
f = open('test_file.out', 'a')
f.write(output_str)
f.close

output_str  = ""
output_str += "Esta es segunda prueba"
f = open('test_file.out', 'a')
f.write(output_str)
f.close
