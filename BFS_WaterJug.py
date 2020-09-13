cap1 = 12
cap2 = 8
cap3 = 5

# to mark visited states
memory = {}

# store solution path
ans = []

def get_all_states(state):
  # Let the 3 jugs be called jug1,jug2,jug3
  jug1 = state[0]
  jug2 = state[1]
  jug3 = state[2]

  if(jug1==6 and jug2==6):
      ans.append(state)
      return True

  # if current state is already visited earlier
  if((jug1,jug2,jug3) in memory):
      return False

  memory[(jug1,jug2,jug3)] = 1

  #empty jug jug1
  if(jug1>0):
      #empty jug1 into jug2
      if(jug1+jug2<=cap2):
          if( get_all_states((0,jug1+jug2,jug3)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((jug1-(cap2-jug2), cap2, jug3)) ):
              ans.append(state)
              return True
      #empty jug1 into jug3
      if(jug1+jug3<=cap3):
          if( get_all_states((0,jug2,jug1+jug3)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((jug1-(cap3-jug3), jug2, cap3)) ):
              ans.append(state)
              return True

  #empty jug jug2
  if(jug2>0):
      #empty jug2 into jug1
      if(jug1+jug2<=cap1):
          if( get_all_states((jug1+jug2, 0, jug3)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((cap1, jug2-(cap1-jug1), jug3)) ):
              ans.append(state)
              return True
      #empty jug2 into jug3
      if(jug2+jug3<=cap3):
          if( get_all_states((jug1, 0, jug2+jug3)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((jug1, jug2-(cap3-jug3), cap3)) ):
              ans.append(state)
              return True

  #empty jug jug3
  if(jug3>0):
      #empty jug3 into jug1
      if(jug1+jug3<=cap1):
          if( get_all_states((jug1+jug3, jug2, 0)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((cap1, jug2, jug3-(cap1-jug1))) ):
              ans.append(state)
              return True
      #empty jug3 into jug2
      if(jug2+jug3<=cap2):
          if( get_all_states((jug1, jug2+jug3, 0)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((jug1, cap2, jug3-(cap2-jug2))) ):
              ans.append(state)
              return True

  return False

initial_state = (12,0,0)
print("Starting work...\n")
get_all_states(initial_state)
ans.reverse()
for i in ans:
  print(i)
