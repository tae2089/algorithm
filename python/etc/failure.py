
def method(stage,stages):
    size = len(stages)
    cnt = stages.count(stage)
    fail_percent = cnt/size
    f = (stage,fail_percent)
    while stage in stages:
        stages.remove(stage)
    return stages,f

def main():
    n = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    failure = {}
    denominator = len(stages)
    if n>0 & n<500:
        if len(stages)<200000:
            for i in range(1,n+1):
                if denominator != 0:
                    count = stages.count(i)
                    failure[i] = count / denominator
                    denominator -= count
                else:
                    failure[stage] = 0
    print(sorted(failure, key=lambda x: failure[x], reverse=True))

if __name__ == "__main__":
    main()
