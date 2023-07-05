accounts = [(0, 1, 3), (3, 4, 5)]

max, curr = (0,0)
print(max, curr)

for m, list in enumerate(accounts):
            if curr > max:
                max = curr
            curr = 0

            print(m)
            # for value, n in enumerate(accounts[m]):
            #     curr += value
