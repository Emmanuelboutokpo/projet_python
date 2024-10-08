def demande_user(min,max) :
     ans=input("choix entre "+ str(min) + " et " + str(max))
     try:
         ans_int = int(ans)
         if min <= ans_int <= max :
             print("Erreur choississez entre ", min, ' et ', max)
             return demande_user(min,max)
         return ans_int
     except:
        print('ERREUR')
        return demande_user(min,max)


rep=demande_user(12, 20)

print(rep)