m_oros_str=input("Δώσε μέσο όρο : ")
m_oros=int(m_oros_str)
if m_oros>0 and m_oros<=5:
  print("Κακώς")
elif m_oros<=9.4:
  print("Ανεπαρκός")
elif m_oros<=13:
  print("Σχεδόν καλώς")
elif m_oros<=16:
  print("Καλώς")
elif m_oros<=18:
  print("Λίαν καλώς")
else:
  print("Άριστα")
  
