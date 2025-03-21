from collections import defaultdict, deque


class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        ingredientToRecipes = defaultdict(list)
        indegree = {recipe: 0 for recipe in recipes}

        for i in range(len(recipes)):
            recipe = recipes[i]
            ingredientList = ingredients[i]

            for ingredient in ingredientList:
                ingredientToRecipes[ingredient].append(recipe)
            indegree[recipe] = len(ingredientList)

        queue = deque(supplies)
        res = []

        while queue:
            current = queue.popleft()

            if current in indegree:
                res.append(current)

            for recipe in ingredientToRecipes[current]:
                indegree[recipe] -= 1

                if indegree[recipe] == 0:
                    queue.append(recipe)

        return res
