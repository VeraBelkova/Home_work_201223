import random

st = []
for i in range(10):
  num = random.randint(0,1)
  st.append(num)

print(st)

st2 = []
for i in range(10):
  if st[i] == 0:
    st2.append(1)
  else:
    st2.append(0)

print(st2)

whoAmI = {'robot' : st,
        'human' : st2}
frame = pd.DataFrame(whoAmI)
frame



