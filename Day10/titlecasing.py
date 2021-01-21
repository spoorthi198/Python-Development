def format_name(f_name,l_name):
  formated_fname=f_name.title()
  formated_lname=l_name.title()
  return f"{formated_fname},{formated_lname}"



output = format_name(f_name='spooRthi',l_name='rajEndra')
print(output)