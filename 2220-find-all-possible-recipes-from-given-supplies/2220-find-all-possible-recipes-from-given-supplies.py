class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        d_recipes = {}
        d_supples_to_recipe = {}
        n = len(recipes)
        for i in range(n):            
            m =  len(ingredients[i])
            d_recipes[recipes[i]] = m
            for j in range(m):
                if ingredients[i][j] not in d_supples_to_recipe:
                    d_supples_to_recipe[ingredients[i][j]] = [recipes[i]]
                else:
                    d_supples_to_recipe[ingredients[i][j]].append(recipes[i])
                
        # print(d_recipes)
        # print(d_supples_to_recipe)
        dq = deque(supplies)
        ans = []
        while dq:
            supply = dq.popleft()
            
            if supply not in d_supples_to_recipe:
                continue
            for value in d_supples_to_recipe[supply]:
                if value not in d_recipes:
                    break
                d_recipes[value] -= 1
                if d_recipes[value] == 0:
                    ans.append(value)
                    dq.append(value)
        
        return ans        